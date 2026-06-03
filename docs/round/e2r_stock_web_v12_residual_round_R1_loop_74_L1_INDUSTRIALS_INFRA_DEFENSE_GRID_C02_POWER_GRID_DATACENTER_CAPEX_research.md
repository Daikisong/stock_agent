# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R1
scheduled_loop: 74
completed_round: R1
completed_loop: 74
next_round: R2
next_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME
loop_objective: "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | stage2_actionable_bonus_stress_test | green_strictness_stress_test | 4B_non_price_requirement_stress_test"
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
live_candidate_mode: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.

## 1. Current Calibrated Profile Assumption

The current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The applied calibration report shows the profile is already applied, with the global axes: Stage2-actionable bonus, Yellow/Green thresholds, stricter Green revision, cross-evidence buffer, 4B non-price requirement, and hard 4C routing. Source anchor: calibrated profile report lines 5-19. fileciteturn639file0L5-L19

The applied scoring diff states the same global changes with 347 unique cases for Stage2 bonus, 225 for Green-related axes, 282 for full-4B non-price evidence, and 92 for hard 4C routing. Source anchor: applied scoring diff lines 5-13. fileciteturn640file0L5-L13

This MD does not re-propose those global axes. It tests a C02-specific residual: **grid/transformer structural winners need the Stage2 bonus, but price/theme-only grid basket spikes should be capped unless backlog/customer/margin evidence exists.**

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R1`
- scheduled_loop: `74`
- round-sector mapping: `R1 -> L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- selected canonical archetype: `C02_POWER_GRID_DATACENTER_CAPEX`
- fine archetype: `GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME`
- scope: historical trigger-level residual calibration only.
- non-scope: live candidate discovery, portfolio construction, auto-trading, brokerage API, or stock_agent code patch.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were checked only for coverage and duplicate avoidance. The ingest summary reports 107 parsed result MDs, 1,940 validated trigger rows, 1,376 aggregate representative rows, and prior coverage across R1~R13 / loops 1~9. fileciteturn638file0L5-L20

A direct v12 filename search in the repository did not return committed v12 residual files for `e2r_stock_web_v12_residual_round_R1_loop_*`. Therefore, this run uses the immediate previous in-conversation v12 output state (`R13 / loop 73 -> next_round R1 / next_loop 74`) as the schedule source. No stock_agent source code was opened.

Duplicate-avoidance decision:

- Reused case count: 0.
- New independent symbols: 4.
- Same canonical archetype is allowed; repeated symbol+trigger+entry groups were avoided.
- Existing global axes are tested only as stress axes, not re-proposed globally.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

- source_name: `FinanceData/marcap`
- source_repo_url: `https://github.com/FinanceData/marcap`
- price_adjustment_status: `raw_unadjusted_marcap`
- min_date: `1995-05-02`
- max_date: `2026-02-20`
- tradable_row_count: `14354401`
- raw_row_count: `15214118`
- symbol_count: `5414`
- active_like_symbol_count: `2868`
- inactive_or_delisted_like_symbol_count: `2546`
- markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- raw_shard_root: `atlas/ohlcv_raw_by_symbol_year`
- schema_path: `atlas/schema.json`
- universe_path: `atlas/universe/all_symbols.csv`

Source anchor: manifest lines 4-58. fileciteturn632file0L4-L58

Schema validation:

- tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`.
- raw shard additionally has `rs`.
- calibration basis is `tradable_raw`.
- MFE/MAE formulas use max high/min low from entry date through N tradable rows.
- calibration usable requires positive OHLC/volume, entry row existence, 180 forward tradable days, and no corporate action contamination in the 180D window.

Source anchor: schema lines 4-68. fileciteturn633file0L4-L68

Diagnostic bundle also confirms generated_at, max_date, row counts, and example selftests for 267260 and 298040 with clean tradable paths. fileciteturn641file0L3-L22

## 5. Historical Eligibility Gate

All four representative triggers are historical and have entry rows in the tradable shards. 180D forward windows are available because all entry dates are in 2024 and the manifest max_date is `2026-02-20`.

Corporate-action status:

- `267260`: profile has corporate action candidates only in 2017~2019, outside the 2024 validation window; 2024 path is usable. fileciteturn650file0L100-L124
- `298040`: profile has zero corporate action candidate dates and clean tradable row status. fileciteturn651file0L90-L108
- `017040`: profile has older corporate action candidates in 2000~2001, outside the 2024 validation window. fileciteturn643file0L86-L101
- `006340`: profile has older corporate action candidates through 2010, outside the 2024 validation window. fileciteturn647file0L41-L65

## 6. Canonical Archetype Compression Map

`C02_POWER_GRID_DATACENTER_CAPEX` is compressed into two evidence routes:

1. **Structural transformer/grid capex route.** Backlog visibility + customer/order quality + margin bridge + revision confirmation. This route can justify Stage2-Actionable and later Green confirmation.
2. **Price/theme grid basket route.** Relative strength + public theme/event read-through without backlog/customer/margin evidence. This route should remain Stage2-Watch or 4B overlay, not positive promotion.

The compression is designed to keep the current Stage2-actionable bonus for genuine structural winners while preventing the same bonus from leaking into theme-only smallcap grid/cable spikes.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | MFE90 | MAE90 | outcome | current_profile |
|---|---:|---|---|---|---|---:|---:|---:|---|---|
| R1L74_C02_POS_267260_20240102 | 267260 | HD현대일렉트릭 | structural_success | 2024-01-02 | 2024-01-03 | 85,800 | 219.93 | -5.24 | structural_success_high_MFE_low_MAE | current_profile_correct |
| R1L74_C02_POS_298040_20240102 | 298040 | 효성중공업 | structural_success | 2024-01-02 | 2024-01-03 | 167,900 | 112.63 | -7.03 | structural_success_high_MFE_low_MAE | current_profile_correct |
| R1L74_C02_NEG_017040_20240508 | 017040 | 광명전기 | false_positive_green | 2024-05-08 | 2024-05-08 | 3,060 | 8.50 | -49.35 | price_theme_false_positive_high_MAE | current_profile_false_positive |
| R1L74_C02_NEG_006340_20240513 | 006340 | 대원전선 | failed_rerating | 2024-05-13 | 2024-05-13 | 4,885 | 11.57 | -47.80 | price_theme_failed_rerating_high_MAE | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 2
- 4B_or_4C_case_count: 2
- calibration_usable_case_count: 4
- new_independent_case_count: 4
- new_independent_case_ratio: 1.00

The split is intentionally symmetrical: two high-MFE low-MAE structural winners, and two high-MAE price/theme counterexamples.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B/4C evidence | evidence quality |
|---|---|---|---|---|
| R1L74_C02_POS_267260_20240102 | backlog/customer/RS/revision | revision/margin/visibility | none | high |
| R1L74_C02_POS_298040_20240102 | backlog/customer/RS/capacity | revision/margin/repeat order | none | high |
| R1L74_C02_NEG_017040_20240508 | public theme + RS only | none | price-only local peak | thin |
| R1L74_C02_NEG_006340_20240513 | public theme + RS only | none | price-only local peak/valuation blowoff | thin |

The key distinction is not whether the chart moved. It is whether the price move had a non-price bridge into backlog, customer quality, or revision.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | source anchor |
|---:|---|---|---|---|
| 267260 | HD현대일렉트릭 | atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv | atlas/symbol_profiles/267/267260.json | entry row and early path from 2024 shard lines 4-71. fileciteturn649file0L4-L71 |
| 298040 | 효성중공업 | atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv | atlas/symbol_profiles/298/298040.json | entry row and early path from 2024 shard lines 4-72. fileciteturn652file0L4-L72 |
| 017040 | 광명전기 | atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv | atlas/symbol_profiles/017/017040.json | blowoff and reversal path from May~July lines 3-71 and July~Nov lines 3-73. fileciteturn645file0L3-L71 fileciteturn654file0L3-L73 |
| 006340 | 대원전선 | atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv | atlas/symbol_profiles/006/006340.json | blowoff and reversal path from Apr~Jul lines 3-71 and Jul~Nov lines 3-71. fileciteturn648file0L3-L71 fileciteturn655file0L3-L71 |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | MFE90 | MAE90 | outcome | current_profile |
|---|---:|---|---|---|---|---:|---:|---:|---|---|
| R1L74_C02_POS_267260_20240102 | 267260 | HD현대일렉트릭 | structural_success | 2024-01-02 | 2024-01-03 | 85,800 | 219.93 | -5.24 | structural_success_high_MFE_low_MAE | current_profile_correct |
| R1L74_C02_POS_298040_20240102 | 298040 | 효성중공업 | structural_success | 2024-01-02 | 2024-01-03 | 167,900 | 112.63 | -7.03 | structural_success_high_MFE_low_MAE | current_profile_correct |
| R1L74_C02_NEG_017040_20240508 | 017040 | 광명전기 | false_positive_green | 2024-05-08 | 2024-05-08 | 3,060 | 8.50 | -49.35 | price_theme_false_positive_high_MAE | current_profile_false_positive |
| R1L74_C02_NEG_006340_20240513 | 006340 | 대원전선 | failed_rerating | 2024-05-13 | 2024-05-13 | 4,885 | 11.57 | -47.80 | price_theme_failed_rerating_high_MAE | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R1L74_C02_267260_STAGE2A_20240102 | 85,800 | 39.04 | 219.93 | 336.48 | -5.24 | -5.24 | -5.24 | 2024-07-24 | 374,500 | -39.92 |
| R1L74_C02_298040_STAGE2A_20240102 | 167,900 | 14.23 | 112.63 | 179.33 | -7.03 | -7.03 | -7.03 | 2024-11-12 | 518,000 | -29.34 |
| R1L74_C02_017040_PRICE_ONLY_20240508 | 3,060 | 8.50 | 8.50 | 8.50 | -29.25 | -49.35 | -59.15 | 2024-05-08 | 3,320 | -62.35 |
| R1L74_C02_006340_PRICE_ONLY_20240513 | 4,885 | 11.57 | 11.57 | 11.57 | -32.75 | -47.80 | -47.80 | 2024-05-13 | 5,450 | -53.21 |


Notes:

- 267260 MFE/MAE values are anchored to stock-web diagnostic selftest and verified against 2024 shard entry/peak rows; the 2024-07-24 high of 374,500 appears in the shard. fileciteturn641file0L20-L21 fileciteturn653file0L12-L13
- 298040 diagnostic selftest supplies the 30/90/180D MFE/MAE values; the 2024 shard verifies entry rows and later high progression into November. fileciteturn641file0L20-L21 fileciteturn657file0L3-L10
- 017040 and 006340 counterexamples use manually audited high/low anchors from stock-web shard rows in the cited ranges.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected label | actual path | verdict |
|---|---|---|---|
| R1L74_C02_POS_267260_20240102 | Stage3-Green or near-Green after revision confirmation | +219.93% MFE90 / -5.24% MAE90 | current_profile_correct |
| R1L74_C02_POS_298040_20240102 | Stage3-Yellow -> Green as margin bridge confirms | +112.63% MFE90 / -7.03% MAE90 | current_profile_correct |
| R1L74_C02_NEG_017040_20240508 | Risk of Stage3-Yellow if RS/theme evidence is over-counted | +8.50% MFE90 / -49.35% MAE90 | current_profile_false_positive |
| R1L74_C02_NEG_006340_20240513 | Risk of Stage3-Yellow if RS/theme evidence is over-counted | +11.57% MFE90 / -47.80% MAE90 | current_profile_false_positive |

Answers to required stress questions:

1. Current profile correctly accepts structural backlog/margin bridge winners.
2. Current profile can still be too generous if public event/theme plus RS is treated as sufficient C02 evidence.
3. Stage2 bonus is not too high globally, but it is too broad inside C02 unless gated by backlog/customer/margin evidence.
4. Yellow 75 is adequate globally but should not be reachable by RS/theme-only C02 rows.
5. Green 87 and revision 55 are adequate; the problem is pre-Green false promotion, not Green threshold relaxation.
6. Price-only blowoff guard is appropriate and should be strengthened at C02 feature construction.
7. Full 4B non-price requirement is appropriate; price-only local peaks should be 4B overlay only.
8. Hard 4C routing is appropriate when thesis evidence is absent or broken.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green proxy entry | green_lateness_ratio | comment |
|---|---|---|---:|---|
| R1L74_C02_POS_267260_20240102 | 2024-01-03 / 85,800 | 2024-04-04 area / ~198,700 | 0.39 | Green not disastrous but materially later than Stage2-actionable. |
| R1L74_C02_POS_298040_20240102 | 2024-01-03 / 167,900 | 2024-03/04 confirmation zone | 0.31 | Green confirmation arrives after a meaningful part of the move. |
| R1L74_C02_NEG_017040_20240508 | 2024-05-08 / 3,060 | no confirmed Green | null | No Green should be produced. |
| R1L74_C02_NEG_006340_20240513 | 2024-05-13 / 4,885 | no confirmed Green | null | No Green should be produced. |

## 15. 4B Local vs Full-window Timing Audit

For the two counterexamples, the local peak was effectively the trigger/entry neighborhood itself. However, this is not a full 4B exit signal for an existing structural Stage3 thesis. It is a warning that the row was never eligible for positive promotion.

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | timing verdict |
|---|---:|---:|---|---|
| R1L74_C02_NEG_017040_20240508 | 1.00 | 0.00 | price_only, positioning_overheat | price_only_local_4B_too_early_or_blocked |
| R1L74_C02_NEG_006340_20240513 | 1.00 | 0.00 | price_only, positioning_overheat, valuation_blowoff | price_only_local_4B_too_early_or_blocked |

## 16. 4C Protection Audit

The counterexamples do not represent post-Green thesis breaks. They are **watch-only 4C-style invalidation cases**: because there was no backlog/customer/margin bridge thesis, the right action is not “late 4C after collapse” but “never promote to Stage2-Actionable/Green.”

| case_id | label | rationale |
|---|---|---|
| R1L74_C02_NEG_017040_20240508 | thesis_break_watch_only | RS/theme route lacked C02 thesis evidence and later delivered -49.35% MAE90. |
| R1L74_C02_NEG_006340_20240513 | thesis_break_watch_only | Price-only cable/grid theme lacked durable backlog bridge and delivered -47.80% MAE90. |

## 17. Sector-Specific Rule Candidate

```text
rule_id = L1_C02_BACKLOG_CUSTOMER_QUALITY_GATE
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
shadow_only = true
condition:
  if canonical_archetype_id == C02_POWER_GRID_DATACENTER_CAPEX
  and large_sector_id == L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  and relative_strength_score is high
  and public_event_or_disclosure is thematic/read-through only
  and backlog_visibility_score == 0
  and customer_quality_score == 0
  and margin_bridge_score == 0:
      cap_stage = Stage2-Watch
      block_Stage2_Actionable_bonus = true
      block_Stage3_Green = true
```

Rationale: the sector has a real structural re-rating path, but the path is carried by backlog/customer/margin bridge, not by “grid theme” language alone.

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C02_THREE_LEG_PROMOTION_CLUSTER
rule_scope = canonical_archetype_specific
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
shadow_only = true
positive_cluster:
  one_or_more(backlog_visibility_score, customer_quality_score)
  and one_or_more(margin_bridge_score, revision_score)
  and relative_strength_score >= moderate
negative_guard:
  if relative_strength_score is high
  and backlog_visibility_score/customer_quality_score/margin_bridge_score/revision_score are all unsupported:
      no_positive_promotion
      route_to_4B_overlay_or_watch_only
```

## 19. Before / After Backtest Comparison

| profile_id | selected | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 4/4 | 88.16 | -27.36 | 0.50 | mixed; positives work but false-positive high-MAE remains |
| P0b_e2r_2_0_baseline_reference | 2/4 | 166.28 | -6.14 | 0.00 | cleaner false-positive filter but too late for structural grid winners |
| P1_sector_specific_candidate_profile | 2/4 | 166.28 | -6.14 | 0.00 | improves score-return alignment by removing high-MAE theme rows |
| P2_canonical_archetype_candidate_profile | 2/4 | 166.28 | -6.14 | 0.00 | best of tested profiles |
| P3_counterexample_guard_profile | 2/4 | 166.28 | -6.14 | 0.00 | guardrail pass |


## 20. Score-Return Alignment Matrix

| bucket | trigger_count | avg_MFE90 | avg_MAE90 | interpretation |
|---|---:|---:|---:|---|
| backlog/customer/margin supported | 2 | 166.28 | -6.14 | Strong positive alignment. |
| RS/theme-only | 2 | 10.04 | -48.58 | High-MAE false-positive bucket. |
| P2 selected | 2 | 166.28 | -6.14 | Best risk-adjusted shadow profile. |
| P0 selected | 4 | 88.16 | -27.36 | Diluted by false positives. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME | 2 | 2 | 2 | 2 | 4 | 0 | 4 | 4 | 2 | true | true | C02 now has positive/counterexample split for transformer structural route vs price-only grid/cable theme route. |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C02 relative_strength_theme_can_overpromote_without_backlog
  - C02 smallcap_price_theme_high_MAE
new_axis_proposed:
  - c02_backlog_customer_quality_min_for_actionable
  - c02_no_backlog_relative_strength_cap
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses Songdaiki/stock-web tradable raw OHLCV rows.
- Uses trigger-level entry date and entry close.
- Computes or imports Stock-Web diagnostic MFE/MAE 30D/90D/180D.
- Separates Stage2, Stage3, 4B, and 4C evidence fields.
- Tests current calibrated profile against positive and counterexample cases.
- Proposes shadow-only sector/canonical rule candidates.

Non-validation scope:

- No stock_agent source code inspection.
- No production scoring patch.
- No current/live candidate discovery.
- No investment recommendation.
- No brokerage or auto-trading integration.
- 1Y/2Y fields are present as null because this loop's calibration target is 180D trigger-level alignment; later holdout can fill extended windows.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c02_backlog_customer_quality_min_for_actionable,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Require at least one backlog/customer-quality leg for C02 Stage2-Actionable promotion.","False-positive rate 50% -> 0% in 4-case shadow backtest; avg MAE90 improves -27.36% -> -6.14%.","R1L74_C02_267260_STAGE2A_20240102|R1L74_C02_298040_STAGE2A_20240102|R1L74_C02_017040_PRICE_ONLY_20240508|R1L74_C02_006340_PRICE_ONLY_20240513",4,4,2,low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c02_no_backlog_relative_strength_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,none,6,n/a,"Cap RS/theme score when backlog/customer/margin bridge are unsupported.","Blocks smallcap price-theme rows without weakening structural transformer winners.","R1L74_C02_017040_PRICE_ONLY_20240508|R1L74_C02_006340_PRICE_ONLY_20240513",2,2,2,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L74_C02_POS_267260_20240102", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L74_C02_267260_STAGE2A_20240102", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2024 opening continuation of transformer backlog, export/customer-quality route and margin-bridge visibility; diagnostic selftest validates clean tradable path."}
{"row_type": "case", "case_id": "R1L74_C02_POS_298040_20240102", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L74_C02_298040_STAGE2A_20240102", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Transformer/grid capex route with high customer/order quality and repeat margin bridge; diagnostic selftest validates clean tradable path."}
{"row_type": "case", "case_id": "R1L74_C02_NEG_017040_20240508", "symbol": "017040", "company_name": "광명전기", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R1L74_C02_017040_PRICE_ONLY_20240508", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_price_theme_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Price/volume spike inside grid-theme basket, but no confirmed backlog conversion, margin bridge, customer-quality upgrade or durable revision evidence at trigger date."}
{"row_type": "case", "case_id": "R1L74_C02_NEG_006340_20240513", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R1L74_C02_006340_PRICE_ONLY_20240513", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_price_theme_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Cable/grid theme blowoff after rapid run; available evidence was mainly price/volume and thematic read-through, not transformer-style backlog/customer/margin visibility."}
{"row_type": "trigger", "trigger_id": "R1L74_C02_267260_STAGE2A_20240102", "case_id": "R1L74_C02_POS_267260_20240102", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME", "sector": "전력기기/변압기", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | stage2_actionable_bonus_stress_test | green_strictness_stress_test | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "2024 opening continuation of transformer backlog, export/customer-quality route and margin-bridge visibility; diagnostic selftest validates clean tradable path.", "evidence_source": "stock-web diagnostic selftest + public order/backlog/revision context; OHLC shard 2024 row", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv", "profile_path": "atlas/symbol_profiles/267/267260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-03", "entry_price": 85800, "MFE_30D_pct": 39.04, "MFE_90D_pct": 219.93, "MFE_180D_pct": 336.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.24, "MAE_90D_pct": -5.24, "MAE_180D_pct": -5.24, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-24", "peak_price": 374500, "drawdown_after_peak_pct": -39.92, "green_lateness_ratio": 0.39, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_low_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L74_C02_POS_267260_20240102:2024-01-03:85800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L74_C02_298040_STAGE2A_20240102", "case_id": "R1L74_C02_POS_298040_20240102", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME", "sector": "전력기기/중전기", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | stage2_actionable_bonus_stress_test | green_strictness_stress_test | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "Transformer/grid capex route with high customer/order quality and repeat margin bridge; diagnostic selftest validates clean tradable path.", "evidence_source": "stock-web diagnostic selftest + public order/backlog/revision context; OHLC shard 2024 row", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "backlog_or_delivery_visibility", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv", "profile_path": "atlas/symbol_profiles/298/298040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-03", "entry_price": 167900, "MFE_30D_pct": 14.23, "MFE_90D_pct": 112.63, "MFE_180D_pct": 179.33, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.03, "MAE_90D_pct": -7.03, "MAE_180D_pct": -7.03, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-12", "peak_price": 518000, "drawdown_after_peak_pct": -29.34, "green_lateness_ratio": 0.31, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_low_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L74_C02_POS_298040_20240102:2024-01-03:167900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L74_C02_017040_PRICE_ONLY_20240508", "case_id": "R1L74_C02_NEG_017040_20240508", "symbol": "017040", "company_name": "광명전기", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME", "sector": "배전/전력설비 테마", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | stage2_actionable_bonus_stress_test | green_strictness_stress_test | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2024-05-08", "evidence_available_at_that_date": "Price/volume spike inside grid-theme basket, but no confirmed backlog conversion, margin bridge, customer-quality upgrade or durable revision evidence at trigger date.", "evidence_source": "stock-web OHLC shard; public-theme route treated as price/theme-only unless independent backlog evidence exists", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv", "profile_path": "atlas/symbol_profiles/017/017040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-08", "entry_price": 3060, "MFE_30D_pct": 8.5, "MFE_90D_pct": 8.5, "MFE_180D_pct": 8.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -29.25, "MAE_90D_pct": -49.35, "MAE_180D_pct": -59.15, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-08", "peak_price": 3320, "drawdown_after_peak_pct": -62.35, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "price_only_local_4B_too_early_or_blocked", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_theme_false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L74_C02_NEG_017040_20240508:2024-05-08:3060", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L74_C02_006340_PRICE_ONLY_20240513", "case_id": "R1L74_C02_NEG_006340_20240513", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_DATACENTER_BACKLOG_VS_PRICE_ONLY_SMALLCAP_THEME", "sector": "전선/전력망 테마", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | stage2_actionable_bonus_stress_test | green_strictness_stress_test | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2024-05-13", "evidence_available_at_that_date": "Cable/grid theme blowoff after rapid run; available evidence was mainly price/volume and thematic read-through, not transformer-style backlog/customer/margin visibility.", "evidence_source": "stock-web OHLC shard; public-theme route treated as price/theme-only unless independent order-quality evidence exists", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv", "profile_path": "atlas/symbol_profiles/006/006340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-13", "entry_price": 4885, "MFE_30D_pct": 11.57, "MFE_90D_pct": 11.57, "MFE_180D_pct": 11.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.75, "MAE_90D_pct": -47.8, "MAE_180D_pct": -47.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-13", "peak_price": 5450, "drawdown_after_peak_pct": -53.21, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "price_only_local_4B_too_early_or_blocked", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_theme_failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L74_C02_NEG_006340_20240513:2024-05-13:4885", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L74_C02_POS_267260_20240102", "trigger_id": "R1L74_C02_267260_STAGE2A_20240102", "symbol": "267260", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 13, "backlog_visibility_score": 14, "margin_bridge_score": 13, "revision_score": 12, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 6, "valuation_repricing_score": 7, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88.5, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 13, "backlog_visibility_score": 15, "margin_bridge_score": 14, "revision_score": 12, "relative_strength_score": 10, "customer_quality_score": 12, "policy_or_regulatory_score": 6, "valuation_repricing_score": 7, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 90.0, "stage_label_after": "Stage3-Green", "changed_components": ["backlog_visibility_score", "+customer_quality_score", "+margin_bridge_score"], "component_delta_explanation": "C02 shadow adds weight only when backlog/customer/margin bridge are all supported.", "MFE_90D_pct": 219.93, "MAE_90D_pct": -5.24, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L74_C02_POS_298040_20240102", "trigger_id": "R1L74_C02_298040_STAGE2A_20240102", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 13, "margin_bridge_score": 11, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 11, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 14, "margin_bridge_score": 12, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 87.5, "stage_label_after": "Stage3-Green", "changed_components": ["backlog_visibility_score", "+customer_quality_score", "+margin_bridge_score"], "component_delta_explanation": "C02 shadow adds weight only when backlog/customer/margin bridge are all supported.", "MFE_90D_pct": 112.63, "MAE_90D_pct": -7.03, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L74_C02_NEG_017040_20240508", "trigger_id": "R1L74_C02_017040_PRICE_ONLY_20240508", "symbol": "017040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 5, "execution_risk_score": -9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77.0, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": -9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63.0, "stage_label_after": "Stage2-Watch_or_blocked", "changed_components": ["relative_strength_score_cap", "valuation_repricing_score_cap", "price_theme_block"], "component_delta_explanation": "C02 guard caps relative-strength/theme evidence when backlog/customer/margin bridge are unsupported.", "MFE_90D_pct": 8.5, "MAE_90D_pct": -49.35, "score_return_alignment_label": "after_guard_aligns_by_blocking_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L74_C02_NEG_006340_20240513", "trigger_id": "R1L74_C02_006340_PRICE_ONLY_20240513", "symbol": "006340", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 6, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79.0, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61.0, "stage_label_after": "Stage2-Watch_or_blocked", "changed_components": ["relative_strength_score_cap", "valuation_repricing_score_cap", "price_theme_block"], "component_delta_explanation": "C02 guard caps relative-strength/theme evidence when backlog/customer/margin bridge are unsupported.", "MFE_90D_pct": 11.57, "MAE_90D_pct": -47.8, "score_return_alignment_label": "after_guard_aligns_by_blocking_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R1", "loop": "74", "scheduled_round": "R1", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "new_symbols=4, new_trigger_families=4, counterexample_gap_filled=2, wrong_round_penalty=0", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["C02 relative_strength_theme_can_overpromote_without_backlog", "C02 smallcap_price_theme_high_MAE"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c02_backlog_customer_quality_min_for_actionable,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Require at least one backlog/customer-quality leg for C02 Stage2-Actionable promotion.","False-positive rate 50% -> 0% in 4-case shadow backtest; avg MAE90 improves -27.36% -> -6.14%.","R1L74_C02_267260_STAGE2A_20240102|R1L74_C02_298040_STAGE2A_20240102|R1L74_C02_017040_PRICE_ONLY_20240508|R1L74_C02_006340_PRICE_ONLY_20240513",4,4,2,low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c02_no_backlog_relative_strength_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,none,6,n/a,"Cap RS/theme score when backlog/customer/margin bridge are unsupported.","Blocks smallcap price-theme rows without weakening structural transformer winners.","R1L74_C02_017040_PRICE_ONLY_20240508|R1L74_C02_006340_PRICE_ONLY_20240513",2,2,2,low,canonical_shadow_only,"not production; post-calibrated residual"
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
completed_round = R1
completed_loop = 74
next_round = R2
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest confirms generated atlas version, source name, max date, row counts, shard roots, schema path, and universe path. fileciteturn632file0L4-L58
- Stock-Web schema confirms tradable/raw columns, MFE/MAE formulas, and calibration-usable rules. fileciteturn633file0L4-L68
- Stock-Web diagnostic bundle confirms source metadata and selftest rows for 267260 and 298040 with clean tradable paths. fileciteturn641file0L3-L22
- The stock_agent calibration reports confirm already-applied axes; this MD only proposes shadow candidate rules. fileciteturn639file0L12-L24

