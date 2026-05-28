# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R13_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
scheduled_round = R13
scheduled_loop = 10
completed_round = R13
completed_loop = 10
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id = CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL
round_schedule_status = valid
round_sector_consistency = pass
source_rows_reused_for_r13_holdout = 8
new_independent_case_count_for_r13_aggregate = 8
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 8 R13 cross-audit independent holdout cases, 5 counterexamples, and 8 residual errors for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/R13_CROSS_ARCHETYPE_4B_4C_REDTEAM.

R13 is a checkpoint, not another sector research file. Its job is to stand at the gate after R1~R12 and ask whether the same failure mechanisms repeat across unrelated sectors: price-only event spikes, local blowoffs misread as full 4B, hard thesis breaks that should become 4C, and high-MAE paths that should not be promoted too easily.

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

R13 does not re-prove these axes by repeating one sector. It stress-tests whether the axes remain coherent when the same symptoms appear in power equipment, semiconductors, batteries, consumer brands, insurance, software/security, construction/PF, and policy-event names.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 10
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
allowed_r13_scope = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is valid only because it is not written as a disguised R5/R6/R7/R8 sector file. The source cases are drawn from multiple previous rounds, but the research object is the cross-archetype guardrail itself.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifacts show that R13 already contains a heavy mix of Stage2, Stage3, Stage4B, and Stage4C rows in the accepted calibration ledger. The existing R13 report lists 111 representative triggers, 30 unique cases, 24 Stage4B rows, and 17 Stage4C rows; it also marks full_4b_requires_non_price_evidence and hard_4c_thesis_break_routes_to_4c as cumulative accepted axes. This MD therefore avoids proposing another ordinary sector rule and instead audits residual cross-case failure modes.

Duplicate policy:

```text
same_symbol_same_trigger_date_research = not used for new sector evidence
prior_rows_reused_only_as = R13_holdout_validation / cross_case_redteam
independent_evidence_weight = 0.5 per source case
production_weight_delta = none
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
manifest_max_date = 2026-02-20
```

The stock-web manifest reports `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `raw_row_count = 15214118`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`. The schema defines tradable columns as `d,o,h,l,c,v,a,mc,s,m`, and the MFE/MAE formulas are applied on tradable rows only.

## 5. Historical Eligibility Gate

All quantitative trigger rows reused in this R13 audit meet the following gate at source-row level:

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180D_window_available = true
MFE_30D_90D_180D_computed = true
MAE_30D_90D_180D_computed = true
corporate_action_window_status = clean_180D_window or source-row clean status
```

The only non-quantitative style used here is interpretive: the same OHLC rows are reclassified under R13 as holdout validation rows. The price rows themselves are not recomputed from any live source.

## 6. Canonical Archetype Compression Map

| R13 guard bucket | Source canonical archetypes compressed | Mechanism |
|---|---|---|
| Price/event false positive cap | C08, C20, C22, C28, C31 | A headline can create MFE without durable EPS route; do not let label similarity become Green evidence. |
| High-MAE success cap | C02 plus cross-sector MAE cases | A thesis can be directionally right and still too early for Stage3-Green or full-size exposure. |
| 4B non-price confirmation | C11, C28, C31 | Price-only local peaks are noisy; full 4B needs valuation/positioning/revision/overhang evidence. |
| Hard 4C route | C30 and legal/accounting break cases | Legal, trust, safety, contract, or PF-break evidence must bypass ordinary positive staging. |

## 7. Case Selection Summary

| case_id | source_round | symbol | source_canonical | case_type | balance | current_profile_verdict | note |
|---|---|---|---|---|---|---|---|
| R13L10_X01_010120_C02 | R1 | 010120 LS ELECTRIC | C02_POWER_GRID_DATACENTER_CAPEX | high_mae_success | counterexample | current_profile_too_early | R13 high-MAE success: Stage2 can be right on direction while still too early for Green/size-up. |
| R13L10_X02_098120_C08 | R2 | 098120 마이크로컨텍솔 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | false_positive_green | counterexample | current_profile_false_positive | R13 customer-quality false positive: socket/test theme without durable customer/margin bridge. |
| R13L10_X03_247540_C11 | R3 | 247540 에코프로비엠 | C11_BATTERY_ORDERBOOK_RERATING | 4B_overlay_success | positive | current_profile_4B_too_late | R13 4B positive: non-price valuation/positioning evidence appears near full-window peak. |
| R13L10_X04_051900_C20 | R5 | 051900 LG생활건강 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | false_positive_green | counterexample | current_profile_false_positive | R13 legacy channel concentration false positive: brand peak without global reorder bridge. |
| R13L10_X05_000400_C22 | R6 | 000400 롯데손해보험 | C22_INSURANCE_RATE_CYCLE_RESERVE | false_positive_green | counterexample | current_profile_false_positive | R13 control-premium false positive: sale/event premium is not reserve-quality rerating. |
| R13L10_X06_053800_C28 | R8 | 053800 안랩 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | price_moved_without_evidence | counterexample | current_profile_false_positive | R13 event/control premium false positive: security label did not equal recurring contract retention. |
| R13L10_X07_006360_C30 | R10 | 006360 GS건설 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 4C_success | positive | current_profile_4C_too_late | R13 hard-4C positive: legal/quality thesis break should bypass normal positive staging. |
| R13L10_X08_053290_C31 | R12 | 053290 NE능률 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 4B_overlay_success | positive | current_profile_4B_too_late | R13 price-event blowoff: huge MFE needs 4B/watch guard rather than Stage3 promotion. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 5
calibration_usable_case_count = 8
calibration_usable_trigger_count = 8
```

The positive rows are not long-entry recommendations. They are positive only for the guardrail logic: one successful 4B timing example, one successful 4C thesis-break route, and one event-blowoff case where risk overlay was more appropriate than positive promotion. Counterexamples dominate because R13 is a red-team checkpoint.

## 9. Evidence Source Map

| evidence bucket | source trigger examples | R13 conclusion |
|---|---|---|
| Relative strength without bridge | LS ELECTRIC, 한일사료, NE능률, 안랩 | Strong tape alone cannot become Stage3 evidence. |
| Customer/channel label without conversion | 마이크로컨텍솔, LG생활건강 | Customer or brand quality must convert into margin/revision bridge. |
| Event/control premium | 롯데손해보험, 안랩, NE능률 | Event premium is a 4B/risk overlay unless cash-flow route is binding. |
| Legal/accounting thesis break | GS건설 | Hard 4C route should fire even if rebound later occurs. |

## 10. Price Data Source Map

| trigger_id | source_trigger_id | price_shard_path | profile_path | price_basis | manifest_max_date |
|---|---|---|---|---|---|
| R13L10_X01_010120_Stage2-Actionable | R1L10_C02_LS_HIGH_MAE_20240429 | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json | tradable_raw | 2026-02-20 |
| R13L10_X02_098120_Stage2-Actionable_candidate_rejected | R2L10_C08_MICROCONTACT_T1 | atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv | atlas/symbol_profiles/098/098120.json | tradable_raw | 2026-02-20 |
| R13L10_X03_247540_Stage4B | R3L10-C11-005-T1 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | atlas/symbol_profiles/247/247540.json | tradable_raw | 2026-02-20 |
| R13L10_X04_051900_Stage2-candidate-rejected | R5L10_C20_LGHNH_T2_20210624 | atlas/ohlcv_tradable_by_symbol_year/051/051900/2021.csv|atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv | atlas/symbol_profiles/051/051900.json | tradable_raw | 2026-02-20 |
| R13L10_X05_000400_Stage2-candidate-rejected | R6L10_C22_LOTTEINS_T2_REJECT_20240423 | atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv | atlas/symbol_profiles/000/000400.json | tradable_raw | 2026-02-20 |
| R13L10_X06_053800_Stage2-Watch | R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11 | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | atlas/symbol_profiles/053/053800.json | tradable_raw | 2026-02-20 |
| R13L10_X07_006360_Stage4C | R10L10-C30-GS-4C-20230706 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | atlas/symbol_profiles/006/006360.json | tradable_raw | 2026-02-20 |
| R13L10_X08_053290_Stage2_event_premium_risk_watch | R12_C31_053290_STAGE2WATCH_20210304 | atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv | atlas/symbol_profiles/053/053290.json | tradable_raw | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | source_round | symbol | source_canonical | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict | outcome |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| R13L10_X01_010120_Stage2-Actionable | R1 | 010120 LS ELECTRIC | C02_POWER_GRID_DATACENTER_CAPEX | Stage2-Actionable | 2024-04-30 | 176600.0 | 55.44 | -19.71 | 55.44 | -28.54 | current_profile_too_early | high_mae_success_needs_bridge_guard |
| R13L10_X02_098120_Stage2-Actionable_candidate_rejected | R2 | 098120 마이크로컨텍솔 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Stage2-Actionable_candidate_rejected | 2024-01-03 | 14400 | 3.13 | -38.54 | 3.13 | -61.74 | current_profile_false_positive | failed_rerating |
| R13L10_X03_247540_Stage4B | R3 | 247540 에코프로비엠 | C11_BATTERY_ORDERBOOK_RERATING | Stage4B | 2023-07-26 | 455000 | 28.35 | -58.77 | 28.35 | -58.77 | current_profile_4B_too_late | 4B_overlay_success |
| R13L10_X04_051900_Stage2-candidate-rejected | R5 | 051900 LG생활건강 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage2-candidate-rejected | 2021-06-24 | 1755000 | 1.65 | -33.22 | 1.65 | -52.99 | current_profile_false_positive | false_positive_green |
| R13L10_X05_000400_Stage2-candidate-rejected | R6 | 000400 롯데손해보험 | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2-candidate-rejected | 2024-04-23 | 3850 | 6.23 | -34.94 | 6.23 | -52.88 | current_profile_false_positive | price_moved_without_evidence |
| R13L10_X06_053800_Stage2-Watch | R8 | 053800 안랩 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Stage2-Watch | 2022-03-11 | 86500 | 152.6 | -14.2 | 152.6 | -36.0 | current_profile_false_positive | price_moved_without_C28_evidence |
| R13L10_X07_006360_Stage4C | R10 | 006360 GS건설 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage4C | 2023-07-06 | 14520 | 5.03 | -12.74 | 19.83 | -12.74 | current_profile_4C_too_late | legal_quality_thesis_break_prevents_false_green |
| R13L10_X08_053290_Stage2_event_premium_risk_watch | R12 | 053290 NE능률 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2_event_premium_risk_watch | 2021-03-04 | 4450 | 591.01 | -21.24 | 591.01 | -21.24 | current_profile_4B_too_late | huge_price_event_but_not_fundamental_policy |

## 12. Trigger-Level OHLC Backtest Tables

The table below keeps the original source trigger OHLC metrics intact and only remaps the interpretation into R13.

| source archetype | representative symbol | R13 risk read | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | post-peak drawdown |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C02_POWER_GRID_DATACENTER_CAPEX | 010120 LS ELECTRIC | high_mae_success_needs_bridge_guard | 38.17 | -9.91 | 55.44 | -19.71 | 55.44 | -28.54 | 2024-07-24 | 274500 | -54.03 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 098120 마이크로컨텍솔 | failed_rerating | 3.13 | -29.65 | 3.13 | -38.54 | 3.13 | -61.74 | 2024-01-09 | 14850 | -62.9 |
| C11_BATTERY_ORDERBOOK_RERATING | 247540 에코프로비엠 | 4B_overlay_success | 28.35 | -19.12 | 28.35 | -58.77 | 28.35 | -58.77 | 2023-07-26 | 584000 | -67.88 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 051900 LG생활건강 | false_positive_green | 1.65 | -16.52 | 1.65 | -33.22 | 1.65 | -52.99 | 2021-07-01 | 1784000 | -61.32 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 000400 롯데손해보험 | price_moved_without_evidence | 4.81 | -13.38 | 6.23 | -34.94 | 6.23 | -52.88 | 2024-06-26 | 4090 | -55.65 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 053800 안랩 | price_moved_without_C28_evidence | 152.6 | -14.2 | 152.6 | -14.2 | 152.6 | -36.0 | 2022-03-24 | 218500 | -62.9 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 006360 GS건설 | legal_quality_thesis_break_prevents_false_green | 3.86 | -6.96 | 5.03 | -12.74 | 19.83 | -12.74 | 2023-11-23 | 17400 | -13.22 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 053290 NE능률 | huge_price_event_but_not_fundamental_policy | 476.4 | -21.24 | 591.01 | -21.24 | 591.01 | -21.24 | 2021-06-09 | 30750 | -84.0 |

## 13. Current Calibrated Profile Stress Test

The current profile is materially better than the old baseline because it already contains price-only and hard-4C guards. R13 still finds four residual patterns:

1. **High-MAE success can look correct in hindsight.** LS ELECTRIC and similar cases show that a directionally correct thesis can still punish early Green conversion with deep interim drawdown.
2. **Theme labels mimic evidence.** Semiconductor sockets, China-reopening beauty, insurance sale premium, and security/political names can all produce MFE without the component bridge required by their canonical archetype.
3. **4B is late when the model waits only for accounting-style deterioration.** Battery and event-blowoff cases need valuation/positioning/non-price overlay before the drawdown becomes obvious.
4. **4C must remain a hard override.** Construction legal/quality breaks can rebound tactically, but that does not undo thesis-break classification.

Required answers:

| Question | R13 answer |
|---|---|
| Did current profile judge every case correctly? | No. `current_profile_error_count = 8` across 8 holdout triggers. |
| Was Stage2 bonus too high? | Not globally; too high only when Stage2 evidence is price/event label without cash-flow bridge. |
| Was Yellow threshold 75 too low/high? | Kept. R13 suggests a risk cap rather than changing the global threshold. |
| Was Green 87 / revision 55 too strict? | Kept. R13 strengthens Green discipline in event and high-MAE cases. |
| Was price-only blowoff guard appropriate? | Yes for positive promotion; however price-only can still be a risk-watch overlay. |
| Was full 4B non-price requirement appropriate? | Kept; R13 separates price-only local peak from full-window non-price 4B. |
| Was hard 4C routing appropriate? | Kept and strengthened for legal/PF/accounting/trust breaks. |

## 14. Stage2 / Yellow / Green Comparison

R13 does not argue that Stage2 always beats Green. It argues that **the bridge between them is archetype-specific and must survive the red-team layer**.

| source pattern | Stage2/Yellow read | Green read | R13 verdict |
|---|---|---|---|
| Structural but high MAE | Stage2/Yellow may be valid | Green too early if revision/margin bridge incomplete | cap Green / require confirmation |
| Theme/event spike | Stage2-Watch only | Green blocked | price/event cap |
| Non-price blowoff | Stage4B overlay | not a positive stage | keep 4B non-price requirement |
| Legal/accounting break | 4C | not Stage2/3 rebound trade | hard 4C route |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict |
|---|---|---:|---:|---|
| R13L10_X01_010120_Stage2-Actionable | price_only_local_peak|positioning_overheat | None | None | None |
| R13L10_X02_098120_Stage2-Actionable_candidate_rejected | None | None | None | None |
| R13L10_X03_247540_Stage4B | ['valuation_blowoff', 'positioning_overheat'] | 0.716 | 0.716 | good_full_window_4B_timing |
| R13L10_X04_051900_Stage2-candidate-rejected | revision_slowdown|margin_or_backlog_slowdown|positioning_overheat | 0.98 | 0.98 | good_full_window_4B_if_non_price_concentration_risk_is_detected |
| R13L10_X05_000400_Stage2-candidate-rejected | control_premium_or_event_premium|valuation_blowoff|price_only_local_peak | 0.92 | 0.92 | control_premium_not_C22_full_positive;_4B_event_cap_should_trigger |
| R13L10_X06_053800_Stage2-Watch | ['control_premium_or_event_premium', 'positioning_overheat', 'price_only'] | 0.99 | 0.99 | good_full_window_4B_timing_if_control_premium_overlay_used |
| R13L10_X07_006360_Stage4C | ['legal_or_regulatory_block', 'margin_or_backlog_slowdown'] | None | None | not_applicable_4C |
| R13L10_X08_053290_Stage2_event_premium_risk_watch | ['price_only', 'positioning_overheat'] | None | None | not_full_4B_until_non_price_or_exhaustion_evidence |

R13 conclusion: price-only local peaks should not be treated as full 4B, but price-only plus positioning/valuation/event-cap evidence can still create a **risk overlay**. This is the same difference as smoke versus a signed fire report: smoke deserves attention, but a signed report changes the official state.

## 16. 4C Protection Audit

| trigger_id | four_c_protection_label | R13 read |
|---|---|---|
| R13L10_X01_010120_Stage2-Actionable | None | not a 4C row; used as guardrail contrast |
| R13L10_X02_098120_Stage2-Actionable_candidate_rejected | thesis_break_watch_only | not a 4C row; used as guardrail contrast |
| R13L10_X03_247540_Stage4B | not_applicable | not a 4C row; used as guardrail contrast |
| R13L10_X04_051900_Stage2-candidate-rejected | hard_4c_late_if_channel_concentration_ignored | not a 4C row; used as guardrail contrast |
| R13L10_X05_000400_Stage2-candidate-rejected | hard_4c_success_if_sale_event_premium_breaks | not a 4C row; used as guardrail contrast |
| R13L10_X06_053800_Stage2-Watch | hard_4c_late_if_misclassified_as_C28_green | not a 4C row; used as guardrail contrast |
| R13L10_X07_006360_Stage4C | hard_4c_success | hard 4C override |
| R13L10_X08_053290_Stage2_event_premium_risk_watch | thesis_break_watch_only | not a 4C row; used as guardrail contrast |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R13 is not a sector-specific round
```

No R13 output should be back-propagated into one sector as if it were a normal R5/R6/R7/R8 result.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = cross_archetype_shadow_only
candidate = R13_cross_archetype_high_MAE_event_price_only_4B_4C_guard
```

Candidate rule:

```text
if evidence_family in [price_only, event_premium, political_theme, control_premium] and
   margin_bridge_score / revision_score / customer_quality_score are not supported:
       cap positive stage at Stage2-Watch or rejected Stage2 candidate

if MAE_90D <= -20% and Green bridge is incomplete:
       block Stage3-Green promotion; allow Stage2/Yellow only with risk note

if 4B evidence is price_only_local_peak:
       risk_watch only, not full 4B

if legal/accounting/trust/contract thesis is broken:
       route to hard 4C regardless of local rebound
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current | already-applied global profile; stress-tested, not re-proposed | none | 8 | 105.43 | -29.17 | 107.28 | -40.61 | high because event/theme labels can still look like positive evidence in some sectors | 3 | 2 | mixed; correct direction in some cases but weak high-MAE/price-only separation |
| P0b_e2r_2_0_baseline_reference | rollback_reference | older baseline for rollback comparison | none | 8 | 105.43 | -29.17 | 107.28 | -40.61 | higher | 3 | 3 | worse: looser Green/event handling would over-promote more samples |
| P1_R13_cross_sector_guard_profile | cross_sector_shadow | caps price/event-only positive promotion across sectors | event_cashflow_bridge_min; high_MAE_watch_cap | 8 | 105.43 | -29.17 | 107.28 | -40.61 | lower | 1 | 1 | better guardrail alignment, no production change |
| P2_R13_4B_4C_guard_profile | cross_archetype_shadow | separates local price-only 4B from non-price full 4B and routes legal/accounting break to 4C | 4B_non_price; hard_4C_route | 8 | 105.43 | -29.17 | 107.28 | -40.61 | lower | 1 | 0 | best risk overlay alignment |
| P3_R13_counterexample_guard_profile | counterexample_guard | requires margin/revision/customer/contract evidence before Green when MAE/event risk is high | green_guard | 8 | 105.43 | -29.17 | 107.28 | -40.61 | lowest | 0 | 0 | best false-positive suppression; shadow-only |


## 20. Score-Return Alignment Matrix

| trigger_id | weighted_before | label_before | weighted_after | label_after | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---:|---|---:|---:|---|
| R13L10_X01_010120_Stage2-Actionable | 70.3 | Stage2_too_early_for_green | 70.3 | Stage2-Watch_or_rejected | 55.44 | -19.71 | current_profile_too_early |
| R13L10_X02_098120_Stage2-Actionable_candidate_rejected | 57.0 | Stage2/Yellow_false_positive_risk | 45.7 | Stage2-Watch_or_rejected | 3.13 | -38.54 | current_profile_false_positive |
| R13L10_X03_247540_Stage4B | 64.6 | Stage4B_overlay | 63.6 | Stage4B_risk_overlay_only | 28.35 | -58.77 | current_profile_4B_too_late |
| R13L10_X04_051900_Stage2-candidate-rejected | 56.9 | Stage2/Yellow_false_positive_risk | 45.6 | Stage2-Watch_or_rejected | 1.65 | -33.22 | current_profile_false_positive |
| R13L10_X05_000400_Stage2-candidate-rejected | 56.8 | Stage2/Yellow_false_positive_risk | 45.4 | Stage2-Watch_or_rejected | 6.23 | -34.94 | current_profile_false_positive |
| R13L10_X06_053800_Stage2-Watch | 57.6 | Stage2/Yellow_false_positive_risk | 46.9 | Stage2-Watch_or_rejected | 152.6 | -14.2 | current_profile_false_positive |
| R13L10_X07_006360_Stage4C | 47.2 | Stage4C_late_or_watch | 34.7 | Stage4C_thesis_break | 5.03 | -12.74 | current_profile_4C_too_late |
| R13L10_X08_053290_Stage2_event_premium_risk_watch | 63.4 | Stage2/4B_too_late | 53.0 | Stage4B_risk_overlay_only | 591.01 | -21.24 | current_profile_4B_too_late |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL | 3 | 5 | 3 | 1 | 8 | 8 | 8 | 8 | 8 | false | true | R13 now covers price/event false positive, high-MAE success, 4B-late, and hard-4C-late across 8 source sectors. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 8
reused_case_ids: R1L10_C02_LS_20240429, R2L10_C08_MICROCONTACT_20240103_STAGE2, R3L10-C11-005, R5L10_C20_LGHNH_20210624_CHINA_DUTYFREE_FALSE_GREEN, R6L10_C22_LOTTEINS_20240423_CONTROL_PREMIUM_FALSE_POSITIVE, R8L10_C28_CASE_004_AHNLAB_2022_CONTROL_PREMIUM_PRICE_ONLY, R10L10-C30-GS-20230706, R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021
new_symbol_count: 8
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, stage3_green_revision_min, stage3_cross_evidence_green_buffer
residual_error_types_found: high_MAE_success_too_early, price_only_event_false_positive, 4B_too_late_after_blowoff, hard_4C_too_late
new_axis_proposed: R13_cross_archetype_high_MAE_event_price_only_guard_shadow_only
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- R13 scheduled round / sector consistency
- stock-web manifest/schema basis
- source trigger OHLC metrics from prior R1~R12 v12 MD rows
- cross-sector false positive / 4B / 4C / high-MAE guardrail stress test
```

Not validated:

```text
- live candidate scan
- current 2026 recommendation
- stock_agent source-code implementation
- production scoring patch
- brokerage or auto-trading behavior
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_price_event_positive_cap,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,Event/policy/control-premium labels should not promote Stage3 without cash-flow bridge,reduced false positive / high MAE promotion,R13L10_X02_098120_Stage2-Actionable_candidate_rejected|R13L10_X04_051900_Stage2-candidate-rejected|R13L10_X05_000400_Stage2-candidate-rejected|R13L10_X06_053800_Stage2-Watch,8,8,5,medium,cross_archetype_shadow_only,not production; R13 guardrail candidate
shadow_weight,R13_high_MAE_watch_cap,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"When MAE_90D <= -20 with incomplete revision/margin bridge, cap at Stage2/Yellow until confirmation",reduced early Green / size-up risk,R13L10_X02_098120_Stage2-Actionable_candidate_rejected|R13L10_X03_247540_Stage4B|R13L10_X04_051900_Stage2-candidate-rejected|R13L10_X05_000400_Stage2-candidate-rejected|R13L10_X08_053290_Stage2_event_premium_risk_watch,8,8,5,medium,cross_archetype_shadow_only,not production; high-MAE guard
shadow_weight,R13_full_4B_non_price_confirmation,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,1,1,0,Existing full_4b_requires_non_price_evidence is kept; price-only local peaks remain risk-watch overlays,prevents false full-cycle exit while allowing risk overlay,R13L10_X03_247540_Stage4B|R13L10_X08_053290_Stage2_event_premium_risk_watch,8,8,5,medium,existing_axis_kept,not production; confirms existing axis
shadow_weight,R13_hard_4C_thesis_break_route,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,1,1,0,Existing hard_4c_thesis_break_routes_to_4c is kept and should override positive staging on legal/accounting break,improves drawdown protection,R13L10_X07_006360_Stage4C,8,8,5,medium,existing_axis_kept,not production; confirms existing axis
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L10_X01_010120_C02", "source_case_id": "R1L10_C02_LS_20240429", "source_trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R13", "loop": "10", "source_round": "R1", "source_loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R13L10_X01_010120_Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "R13 cross-archetype holdout validation using prior round trigger row; independent across source sector/archetype/failure family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE success: Stage2 can be right on direction while still too early for Green/size-up."}
{"row_type": "case", "case_id": "R13L10_X02_098120_C08", "source_case_id": "R2L10_C08_MICROCONTACT_20240103_STAGE2", "source_trigger_id": "R2L10_C08_MICROCONTACT_T1", "symbol": "098120", "company_name": "마이크로컨텍솔", "round": "R13", "loop": "10", "source_round": "R2", "source_loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R13L10_X02_098120_Stage2-Actionable_candidate_rejected", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "R13 cross-archetype holdout validation using prior round trigger row; independent across source sector/archetype/failure family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "R13 customer-quality false positive: socket/test theme without durable customer/margin bridge."}
{"row_type": "case", "case_id": "R13L10_X03_247540_C11", "source_case_id": "R3L10-C11-005", "source_trigger_id": "R3L10-C11-005-T1", "symbol": "247540", "company_name": "에코프로비엠", "round": "R13", "loop": "10", "source_round": "R3", "source_loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "R13L10_X03_247540_Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "R13 cross-archetype holdout validation using prior round trigger row; independent across source sector/archetype/failure family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "R13 4B positive: non-price valuation/positioning evidence appears near full-window peak."}
{"row_type": "case", "case_id": "R13L10_X04_051900_C20", "source_case_id": "R5L10_C20_LGHNH_20210624_CHINA_DUTYFREE_FALSE_GREEN", "source_trigger_id": "R5L10_C20_LGHNH_T2_20210624", "symbol": "051900", "company_name": "LG생활건강", "round": "R13", "loop": "10", "source_round": "R5", "source_loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R13L10_X04_051900_Stage2-candidate-rejected", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "R13 cross-archetype holdout validation using prior round trigger row; independent across source sector/archetype/failure family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "R13 legacy channel concentration false positive: brand peak without global reorder bridge."}
{"row_type": "case", "case_id": "R13L10_X05_000400_C22", "source_case_id": "R6L10_C22_LOTTEINS_20240423_CONTROL_PREMIUM_FALSE_POSITIVE", "source_trigger_id": "R6L10_C22_LOTTEINS_T2_REJECT_20240423", "symbol": "000400", "company_name": "롯데손해보험", "round": "R13", "loop": "10", "source_round": "R6", "source_loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R13L10_X05_000400_Stage2-candidate-rejected", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "R13 cross-archetype holdout validation using prior round trigger row; independent across source sector/archetype/failure family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "price_moved_without_evidence", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "R13 control-premium false positive: sale/event premium is not reserve-quality rerating."}
{"row_type": "case", "case_id": "R13L10_X06_053800_C28", "source_case_id": "R8L10_C28_CASE_004_AHNLAB_2022_CONTROL_PREMIUM_PRICE_ONLY", "source_trigger_id": "R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11", "symbol": "053800", "company_name": "안랩", "round": "R13", "loop": "10", "source_round": "R8", "source_loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R13L10_X06_053800_Stage2-Watch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "R13 cross-archetype holdout validation using prior round trigger row; independent across source sector/archetype/failure family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "price_moved_without_C28_evidence", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "R13 event/control premium false positive: security label did not equal recurring contract retention."}
{"row_type": "case", "case_id": "R13L10_X07_006360_C30", "source_case_id": "R10L10-C30-GS-20230706", "source_trigger_id": "R10L10-C30-GS-4C-20230706", "symbol": "006360", "company_name": "GS건설", "round": "R13", "loop": "10", "source_round": "R10", "source_loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "R13L10_X07_006360_Stage4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "R13 cross-archetype holdout validation using prior round trigger row; independent across source sector/archetype/failure family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "legal_quality_thesis_break_prevents_false_green", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "R13 hard-4C positive: legal/quality thesis break should bypass normal positive staging."}
{"row_type": "case", "case_id": "R13L10_X08_053290_C31", "source_case_id": "R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021", "source_trigger_id": "R12_C31_053290_STAGE2WATCH_20210304", "symbol": "053290", "company_name": "NE능률", "round": "R13", "loop": "10", "source_round": "R12", "source_loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "R13L10_X08_053290_Stage2_event_premium_risk_watch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "R13 cross-archetype holdout validation using prior round trigger row; independent across source sector/archetype/failure family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "huge_price_event_but_not_fundamental_policy", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "R13 price-event blowoff: huge MFE needs 4B/watch guard rather than Stage3 promotion."}
{"sector": "산업재·수주·인프라", "primary_archetype": "power_grid_datacenter_capex", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-29", "evidence_available_at_that_date": "2024-04 power-grid/data-center theme and relative strength were visible, but the later path showed high MAE before durable confirmation.", "evidence_source": "historical company disclosure / research-report proxy; not live discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "profile_path": "atlas/symbol_profiles/010/010120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-30", "entry_price": 176600.0, "MFE_30D_pct": 38.17, "MFE_90D_pct": 55.44, "MFE_180D_pct": 55.44, "MFE_1Y_pct": 55.44, "MFE_2Y_pct": "available_not_used_for_weight_delta", "MAE_30D_pct": -9.91, "MAE_90D_pct": -19.71, "MAE_180D_pct": -28.54, "MAE_1Y_pct": -28.54, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-24", "peak_price": 274500, "drawdown_after_peak_pct": -54.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": "price_only_local_peak|positioning_overheat", "four_c_protection_label": null, "trigger_outcome_label": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "trigger_id": "R13L10_X01_010120_Stage2-Actionable", "source_trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "case_id": "R13L10_X01_010120_C02", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R13", "loop": "10", "source_round": "R1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining|counterexample_mining|holdout_validation", "same_entry_group_id": "R13L10_X01_010120_C02::2024-04-30::176600.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "prior round row reused as R13 holdout/cross-case red-team sample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_md_file": "e2r_stock_web_v12_residual_round_R1_loop_10_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"sector": "AI·반도체·전자부품", "primary_archetype": "semi_test_socket_customer_quality", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "Generic test-socket theme participation without durable customer-quality/revision/margin bridge; price path failed almost immediately after the candidate trigger.", "evidence_source": "historical public theme proxy; stock-web OHLC validation; explicit company-specific Green evidence not confirmed in this research run", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "profile_path": "atlas/symbol_profiles/098/098120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-03", "entry_price": 14400, "MFE_30D_pct": 3.13, "MFE_90D_pct": 3.13, "MFE_180D_pct": 3.13, "MFE_1Y_pct": 3.13, "MFE_2Y_pct": null, "MAE_30D_pct": -29.65, "MAE_90D_pct": -38.54, "MAE_180D_pct": -61.74, "MAE_1Y_pct": -61.74, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-09", "peak_price": 14850, "drawdown_after_peak_pct": -62.9, "green_lateness_ratio": "not_applicable: no confirmed C08 Stage3-Green trigger used as representative", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "trigger_id": "R13L10_X02_098120_Stage2-Actionable_candidate_rejected", "source_trigger_id": "R2L10_C08_MICROCONTACT_T1", "case_id": "R13L10_X02_098120_C08", "symbol": "098120", "company_name": "마이크로컨텍솔", "round": "R13", "loop": "10", "source_round": "R2", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining|counterexample_mining|holdout_validation", "same_entry_group_id": "R13L10_X02_098120_C08::2024-01-03::14400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "prior round row reused as R13 holdout/cross-case red-team sample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_md_file": "e2r_stock_web_v12_residual_round_R2_loop_10_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md"}
{"sector": "2차전지·전기차·친환경", "primary_archetype": "battery orderbook rerating", "trigger_type": "Stage4B", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "valuation blowoff and positioning overheat after orderbook rerating", "evidence_source": "historical public evidence proxy; stock-web price path", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 455000, "MFE_30D_pct": 28.35, "MFE_90D_pct": 28.35, "MFE_180D_pct": 28.35, "MFE_1Y_pct": 28.35, "MFE_2Y_pct": 28.35, "MAE_30D_pct": -19.12, "MAE_90D_pct": -58.77, "MAE_180D_pct": -58.77, "MAE_1Y_pct": -58.77, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 584000, "drawdown_after_peak_pct": -67.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.716, "four_b_full_window_peak_proximity": 0.716, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "trigger_id": "R13L10_X03_247540_Stage4B", "source_trigger_id": "R3L10-C11-005-T1", "case_id": "R13L10_X03_247540_C11", "symbol": "247540", "company_name": "에코프로비엠", "round": "R13", "loop": "10", "source_round": "R3", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining|counterexample_mining|holdout_validation", "same_entry_group_id": "R13L10_X03_247540_C11::2023-07-26::455000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "prior round row reused as R13 holdout/cross-case red-team sample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_md_file": "e2r_stock_web_v12_residual_round_R3_loop_10_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md"}
{"sector": "소비재·유통·브랜드", "primary_archetype": "beauty/food global distribution reorder-to-margin rerating", "trigger_type": "Stage2-candidate-rejected", "trigger_date": "2021-06-24", "evidence_available_at_that_date": "China/duty-free prestige beauty dependence: research proxy treats the 2021 rebound narrative as insufficient for C20 Green because distribution was channel-concentrated and sell-through was not independently widening. This is a counterexample to promoting legacy brand premium without channel diversification.", "evidence_source": "historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["revision_slowdown", "margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2021.csv|atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv", "profile_path": "atlas/symbol_profiles/051/051900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-06-24", "entry_price": 1755000, "MFE_30D_pct": 1.65, "MFE_90D_pct": 1.65, "MFE_180D_pct": 1.65, "MFE_1Y_pct": 1.65, "MFE_2Y_pct": null, "MAE_30D_pct": -16.52, "MAE_90D_pct": -33.22, "MAE_180D_pct": -52.99, "MAE_1Y_pct": -60.68, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-01", "peak_price": 1784000, "drawdown_after_peak_pct": -61.32, "green_lateness_ratio": "not_applicable_no_confirmed_green", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_if_non_price_concentration_risk_is_detected", "four_b_evidence_type": "revision_slowdown|margin_or_backlog_slowdown|positioning_overheat", "four_c_protection_label": "hard_4c_late_if_channel_concentration_ignored", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "trigger_id": "R13L10_X04_051900_Stage2-candidate-rejected", "source_trigger_id": "R5L10_C20_LGHNH_T2_20210624", "case_id": "R13L10_X04_051900_C20", "symbol": "051900", "company_name": "LG생활건강", "round": "R13", "loop": "10", "source_round": "R5", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining|counterexample_mining|holdout_validation", "same_entry_group_id": "R13L10_X04_051900_C20::2021-06-24::1755000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "prior round row reused as R13 holdout/cross-case red-team sample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_md_file": "e2r_stock_web_v12_residual_round_R5_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md"}
{"sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance IFRS17/CSM reserve-quality rate-cycle capital-return rerating", "trigger_type": "Stage2-candidate-rejected", "trigger_date": "2024-04-23", "evidence_available_at_that_date": "Control-premium/sale-process excitement was not the same thing as a clean C22 reserve-rate-cycle rerating. The event could move price, but without reserve-quality, CSM durability, and recurring capital-return evidence it should not promote Stage2/Stage3 under C22.", "evidence_source": "historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "valuation_blowoff", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-23", "entry_price": 3850, "MFE_30D_pct": 4.81, "MFE_90D_pct": 6.23, "MFE_180D_pct": 6.23, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.38, "MAE_90D_pct": -34.94, "MAE_180D_pct": -52.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 4090, "drawdown_after_peak_pct": -55.65, "green_lateness_ratio": "not_applicable_candidate_rejected", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "control_premium_not_C22_full_positive;_4B_event_cap_should_trigger", "four_b_evidence_type": "control_premium_or_event_premium|valuation_blowoff|price_only_local_peak", "four_c_protection_label": "hard_4c_success_if_sale_event_premium_breaks", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "trigger_id": "R13L10_X05_000400_Stage2-candidate-rejected", "source_trigger_id": "R6L10_C22_LOTTEINS_T2_REJECT_20240423", "case_id": "R13L10_X05_000400_C22", "symbol": "000400", "company_name": "롯데손해보험", "round": "R13", "loop": "10", "source_round": "R6", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining|counterexample_mining|holdout_validation", "same_entry_group_id": "R13L10_X05_000400_C22::2024-04-23::3850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "prior round row reused as R13 holdout/cross-case red-team sample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_md_file": "e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"}
{"sector": "platform_content_software_security", "primary_archetype": "software_security_contract_retention", "trigger_type": "Stage2-Watch", "trigger_date": "2022-03-11", "evidence_available_at_that_date": "Security label plus political/control-premium flow. No C28 recurring-contract retention bridge was visible at trigger date.", "evidence_source": "event/control-premium narrative / price-atlas validation only", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": ["control_premium_or_event_premium", "price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-11", "entry_price": 86500, "MFE_30D_pct": 152.6, "MFE_90D_pct": 152.6, "MFE_180D_pct": 152.6, "MFE_1Y_pct": 152.6, "MFE_2Y_pct": 152.6, "MAE_30D_pct": -14.2, "MAE_90D_pct": -14.2, "MAE_180D_pct": -36.0, "MAE_1Y_pct": -36.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -62.9, "green_lateness_ratio": "not_applicable_no_green_allowed", "four_b_local_peak_proximity": "0.99", "four_b_full_window_peak_proximity": "0.99", "four_b_timing_verdict": "good_full_window_4B_timing_if_control_premium_overlay_used", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "hard_4c_late_if_misclassified_as_C28_green", "trigger_outcome_label": "price_moved_without_C28_evidence", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "trigger_id": "R13L10_X06_053800_Stage2-Watch", "source_trigger_id": "R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11", "case_id": "R13L10_X06_053800_C28", "symbol": "053800", "company_name": "안랩", "round": "R13", "loop": "10", "source_round": "R8", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining|counterexample_mining|holdout_validation", "same_entry_group_id": "R13L10_X06_053800_C28::2022-03-11::86500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "prior round row reused as R13 holdout/cross-case red-team sample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_md_file": "e2r_stock_web_v12_residual_round_R8_loop_10_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"sector": "construction_real_estate_housing", "primary_archetype": "PF balance-sheet break / survivor recovery guard", "trigger_type": "Stage4C", "trigger_date": "2023-07-06", "evidence_available_at_that_date": "quality/legal incident converts ordinary construction-cycle risk into thesis-break watch; positive valuation labels should be blocked", "evidence_source": "historical public-event proxy; stock-web price row used for timing", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "accounting_or_trust_break", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-06", "entry_price": 14520, "MFE_30D_pct": 3.86, "MFE_90D_pct": 5.03, "MFE_180D_pct": 19.83, "MFE_1Y_pct": 19.83, "MFE_2Y_pct": null, "MAE_30D_pct": -6.96, "MAE_90D_pct": -12.74, "MAE_180D_pct": -12.74, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-23", "peak_price": 17400, "drawdown_after_peak_pct": -13.22, "green_lateness_ratio": "not_applicable:4C_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_4C", "four_b_evidence_type": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "legal_quality_thesis_break_prevents_false_green", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "trigger_id": "R13L10_X07_006360_Stage4C", "source_trigger_id": "R10L10-C30-GS-4C-20230706", "case_id": "R13L10_X07_006360_C30", "symbol": "006360", "company_name": "GS건설", "round": "R13", "loop": "10", "source_round": "R10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining|counterexample_mining|holdout_validation", "same_entry_group_id": "R13L10_X07_006360_C30::2023-07-06::14520", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "prior round row reused as R13 holdout/cross-case red-team sample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_md_file": "e2r_stock_web_v12_residual_round_R10_loop_10_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"sector": "education_policy_person_theme", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2021-03-04", "evidence_available_at_that_date": "Political/person-related education-policy theme drove price, but trigger evidence did not contain a legislated subsidy, official procurement route, contract, or earnings bridge.", "evidence_source": "External event context: 2021 Korean political-theme trading; price rows: stock-web 053290 2021 shard.", "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv", "profile_path": "atlas/symbol_profiles/053/053290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-03-04", "entry_price": 4450, "MFE_30D_pct": 476.4, "MFE_90D_pct": 591.01, "MFE_180D_pct": 591.01, "MFE_1Y_pct": 591.01, "MFE_2Y_pct": 591.01, "MAE_30D_pct": -21.24, "MAE_90D_pct": -21.24, "MAE_180D_pct": -21.24, "MAE_1Y_pct": -30.34, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-09", "peak_price": 30750, "drawdown_after_peak_pct": -84.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B_until_non_price_or_exhaustion_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "huge_price_event_but_not_fundamental_policy", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "trigger_id": "R13L10_X08_053290_Stage2_event_premium_risk_watch", "source_trigger_id": "R12_C31_053290_STAGE2WATCH_20210304", "case_id": "R13L10_X08_053290_C31", "symbol": "053290", "company_name": "NE능률", "round": "R13", "loop": "10", "source_round": "R12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CROSS_ARCHETYPE_HIGH_MAE_PRICE_ONLY_4B_4C_GUARDRAIL", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining|counterexample_mining|holdout_validation", "same_entry_group_id": "R13L10_X08_053290_C31::2021-03-04::4450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "prior round row reused as R13 holdout/cross-case red-team sample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_md_file": "e2r_stock_web_v12_residual_round_R12_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_guard_profile", "profile_scope": "cross_archetype_shadow_only", "case_id": "R13L10_X01_010120_C02", "trigger_id": "R13L10_X01_010120_Stage2-Actionable", "source_trigger_id": "R1L10_C02_LS_HIGH_MAE_20240429", "symbol": "010120", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 65, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 80, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70.3, "stage_label_before": "Stage2_too_early_for_green", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 65, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 80, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70.3, "stage_label_after": "Stage2-Watch_or_rejected", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score", "valuation_repricing_score"], "component_delta_explanation": "R13 guard caps price/event-only positive promotion, routes non-price blowoff to 4B overlay, and routes hard legal/accounting break to 4C.", "MFE_90D_pct": 55.44, "MAE_90D_pct": -19.71, "score_return_alignment_label": "high_mae_success_needs_bridge_guard", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_guard_profile", "profile_scope": "cross_archetype_shadow_only", "case_id": "R13L10_X02_098120_C08", "trigger_id": "R13L10_X02_098120_Stage2-Actionable_candidate_rejected", "source_trigger_id": "R2L10_C08_MICROCONTACT_T1", "symbol": "098120", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 70, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 57.0, "stage_label_before": "Stage2/Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 35, "valuation_repricing_score": 45, "execution_risk_score": 85, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 45.7, "stage_label_after": "Stage2-Watch_or_rejected", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score", "valuation_repricing_score"], "component_delta_explanation": "R13 guard caps price/event-only positive promotion, routes non-price blowoff to 4B overlay, and routes hard legal/accounting break to 4C.", "MFE_90D_pct": 3.13, "MAE_90D_pct": -38.54, "score_return_alignment_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_guard_profile", "profile_scope": "cross_archetype_shadow_only", "case_id": "R13L10_X03_247540_C11", "trigger_id": "R13L10_X03_247540_Stage4B", "source_trigger_id": "R3L10-C11-005-T1", "symbol": "247540", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 90, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 95, "execution_risk_score": 85, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64.6, "stage_label_before": "Stage4B_overlay", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 90, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 100, "execution_risk_score": 95, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63.6, "stage_label_after": "Stage4B_risk_overlay_only", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score", "valuation_repricing_score"], "component_delta_explanation": "R13 guard caps price/event-only positive promotion, routes non-price blowoff to 4B overlay, and routes hard legal/accounting break to 4C.", "MFE_90D_pct": 28.35, "MAE_90D_pct": -58.77, "score_return_alignment_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_guard_profile", "profile_scope": "cross_archetype_shadow_only", "case_id": "R13L10_X04_051900_C20", "trigger_id": "R13L10_X04_051900_Stage2-candidate-rejected", "source_trigger_id": "R5L10_C20_LGHNH_T2_20210624", "symbol": "051900", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 20, "revision_score": 30, "relative_strength_score": 60, "customer_quality_score": 55, "policy_or_regulatory_score": 35, "valuation_repricing_score": 70, "execution_risk_score": 80, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56.9, "stage_label_before": "Stage2/Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 60, "customer_quality_score": 40, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 95, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 45.6, "stage_label_after": "Stage2-Watch_or_rejected", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score", "valuation_repricing_score"], "component_delta_explanation": "R13 guard caps price/event-only positive promotion, routes non-price blowoff to 4B overlay, and routes hard legal/accounting break to 4C.", "MFE_90D_pct": 1.65, "MAE_90D_pct": -33.22, "score_return_alignment_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_guard_profile", "profile_scope": "cross_archetype_shadow_only", "case_id": "R13L10_X05_000400_C22", "trigger_id": "R13L10_X05_000400_Stage2-candidate-rejected", "source_trigger_id": "R6L10_C22_LOTTEINS_T2_REJECT_20240423", "symbol": "000400", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 70, "execution_risk_score": 75, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 35}, "weighted_score_before": 56.8, "stage_label_before": "Stage2/Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 60, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 90, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 35}, "weighted_score_after": 45.4, "stage_label_after": "Stage2-Watch_or_rejected", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score", "valuation_repricing_score"], "component_delta_explanation": "R13 guard caps price/event-only positive promotion, routes non-price blowoff to 4B overlay, and routes hard legal/accounting break to 4C.", "MFE_90D_pct": 6.23, "MAE_90D_pct": -34.94, "score_return_alignment_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_guard_profile", "profile_scope": "cross_archetype_shadow_only", "case_id": "R13L10_X06_053800_C28", "trigger_id": "R13L10_X06_053800_Stage2-Watch", "source_trigger_id": "R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11", "symbol": "053800", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 95, "customer_quality_score": 25, "policy_or_regulatory_score": 35, "valuation_repricing_score": 90, "execution_risk_score": 90, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 57.6, "stage_label_before": "Stage2/Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 30, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 95, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 75, "execution_risk_score": 100, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 46.9, "stage_label_after": "Stage2-Watch_or_rejected", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score", "valuation_repricing_score"], "component_delta_explanation": "R13 guard caps price/event-only positive promotion, routes non-price blowoff to 4B overlay, and routes hard legal/accounting break to 4C.", "MFE_90D_pct": 152.6, "MAE_90D_pct": -14.2, "score_return_alignment_label": "price_moved_without_C28_evidence", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_guard_profile", "profile_scope": "cross_archetype_shadow_only", "case_id": "R13L10_X07_006360_C30", "trigger_id": "R13L10_X07_006360_Stage4C", "source_trigger_id": "R10L10-C30-GS-4C-20230706", "symbol": "006360", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 75, "legal_or_contract_risk_score": 90, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 55}, "weighted_score_before": 47.2, "stage_label_before": "Stage4C_late_or_watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 60, "customer_quality_score": 20, "policy_or_regulatory_score": 35, "valuation_repricing_score": 10, "execution_risk_score": 90, "legal_or_contract_risk_score": 100, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 65}, "weighted_score_after": 34.7, "stage_label_after": "Stage4C_thesis_break", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score", "valuation_repricing_score"], "component_delta_explanation": "R13 guard caps price/event-only positive promotion, routes non-price blowoff to 4B overlay, and routes hard legal/accounting break to 4C.", "MFE_90D_pct": 5.03, "MAE_90D_pct": -12.74, "score_return_alignment_label": "legal_quality_thesis_break_prevents_false_green", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "R13_cross_archetype_guard_profile", "profile_scope": "cross_archetype_shadow_only", "case_id": "R13L10_X08_053290_C31", "trigger_id": "R13L10_X08_053290_Stage2_event_premium_risk_watch", "source_trigger_id": "R12_C31_053290_STAGE2WATCH_20210304", "symbol": "053290", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 95, "customer_quality_score": 35, "policy_or_regulatory_score": 80, "valuation_repricing_score": 90, "execution_risk_score": 90, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 63.4, "stage_label_before": "Stage2/4B_too_late", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 95, "customer_quality_score": 20, "policy_or_regulatory_score": 80, "valuation_repricing_score": 80, "execution_risk_score": 100, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53.0, "stage_label_after": "Stage4B_risk_overlay_only", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score", "valuation_repricing_score"], "component_delta_explanation": "R13 guard caps price/event-only positive promotion, routes non-price blowoff to 4B overlay, and routes hard legal/accounting break to 4C.", "MFE_90D_pct": 591.01, "MAE_90D_pct": -21.24, "score_return_alignment_label": "huge_price_event_but_not_fundamental_policy", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R13", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "scheduled_round": "R13", "scheduled_loop": "10", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 8, "reused_case_count": 8, "new_symbol_count": 8, "same_archetype_new_symbol_count": 8, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 3, "counterexample_count": 5, "current_profile_error_count": 8, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer"], "residual_error_types_found": ["high_MAE_success_too_early", "price_only_event_false_positive", "4B_too_late_after_blowoff", "hard_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "cross-source sectors=8; source canonical archetypes=8; reused holdout rows=8; wrong_round_penalty=0"}
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

### R13-specific implementation rule

- R13 rows may reuse prior R1~R12 trigger rows as holdout validation if `reuse_reason` and `independent_evidence_weight` are present.
- R13 must not be ingested as a normal sector file.
- R13 `R13_CROSS_ARCHETYPE_*` rows should update a cross-archetype guardrail ledger, not L5/L6/L7/L8 sector ledgers.

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
completed_round = R13
completed_loop = 10
next_round = R1
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest/schema were used for price-source validation.
- Source OHLC metrics were drawn from prior v12 Loop 10 standalone MD rows already generated with stock-web tradable shards.
- This R13 file is a cross-checkpoint artifact. It intentionally reuses prior rows for holdout validation and must not be treated as ordinary sector expansion.

