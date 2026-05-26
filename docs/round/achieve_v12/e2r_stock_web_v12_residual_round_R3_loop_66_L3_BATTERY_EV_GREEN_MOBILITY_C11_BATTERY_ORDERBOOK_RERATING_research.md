# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R3
loop = 66
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = CATHODE_LONG_TERM_CELL_CUSTOMER_ORDERBOOK / CATHODE_CUSTOMER_CAPACITY_ORDERBOOK_REPRICING / SEPARATOR_CUSTOMER_ORDERBOOK_HIGH_MAE_COUNTEREXAMPLE
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not a live stock recommendation, current watchlist, repository patch, or trading instruction.

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

This loop does not re-prove the global Stage2 bonus or generic Green lateness rule. It tests the residual problem inside C11: battery orderbook evidence is not one thing. A signed long-duration customer orderbook behaves differently from a theme-level “capacity/orderbook expectation” with weak margin bridge.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R3 |
| loop | 66 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| loop_objective | coverage_gap_fill, counterexample_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test |
| preferred_rule_scope | canonical_archetype_specific |
| current live scan | false |

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible repository search for `C11_BATTERY_ORDERBOOK_RERATING` returned no direct match in the visible search snapshot. This loop therefore treats C11 as an auto-selected coverage gap after the previous R3/C12 residual loop.

```text
auto_selected_coverage_gap = C11 battery orderbook/rerating lacks visible prior residual coverage in accessible artifact search
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
```

No `stock_agent/src/e2r` source was opened and no patch was produced.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | observed value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Validation status:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

## 5. Historical Eligibility Gate

| case | entry_date | 180D forward available | profile corporate-action overlap | calibration_usable |
|---|---:|---:|---|---:|
| 포스코퓨처엠 003670 | 2023-01-31 | yes | profile has 2015-05-04 / 2021-02-03 candidates, no 2023 180D overlap | true |
| 에코프로비엠 247540 | 2023-02-03 | yes | profile has 2022-06-27 / 2022-07-15 candidates, no 2023 180D overlap | true |
| 더블유씨피 393890 | 2023-02-03 | yes | no corporate-action candidate dates | true |
| 에코프로비엠 4B overlay | 2023-07-25 | yes | no 2023 180D overlap | true as overlay/risk calibration only |

The calculations use the v12 formula: `MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100`.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | mapped canonical_archetype_id | compression reason |
|---|---|---|
| CATHODE_LONG_TERM_CELL_CUSTOMER_ORDERBOOK | C11_BATTERY_ORDERBOOK_RERATING | signed long-duration cathode supply / named cell customer / backlog visibility |
| CATHODE_CUSTOMER_CAPACITY_ORDERBOOK_REPRICING | C11_BATTERY_ORDERBOOK_RERATING | customer/capacity/orderbook route reprices EPS option |
| SEPARATOR_CUSTOMER_ORDERBOOK_HIGH_MAE_COUNTEREXAMPLE | C11_BATTERY_ORDERBOOK_RERATING | same battery orderbook umbrella, but weaker customer/margin bridge creates high-MAE counterexample |

## 7. Case Selection Summary

| case_id | symbol | company | role | case_type | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---|
| CASE_R3L66_003670_POSCOFUTUREM_ORDERBOOK | 003670 | 포스코퓨처엠 | positive | structural_success | 209.82 | -5.58 | current_profile_missed_structural |
| CASE_R3L66_247540_ECOPROBM_ORDERBOOK | 247540 | 에코프로비엠 | positive | structural_success | 411.83 | -1.84 | current_profile_missed_structural |
| CASE_R3L66_393890_WCP_SEPARATOR_COUNTER | 393890 | 더블유씨피 | counterexample | high_mae_success | 70.9 | -20.7 | current_profile_false_positive |

Selection intent: two high-quality positive cases and one counterexample inside the same C11 umbrella. This is the “same shelf, different weight-bearing beam” problem: both cathode and separator names may sit on the battery orderbook shelf, but only direct customer-quality and margin bridge decide whether the shelf can carry Green-level scoring.

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
new_independent_case_count = 3
reused_case_count = 0
```

Balance verdict: usable. Positive cases are not merely momentum wins; both show large 180D MFE and controlled early MAE. Counterexample is not “no upside”; it is a high-MAE, weak-quality orderbook case that would make Green promotion too loose if C11 does not distinguish customer/order certainty and margin bridge.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 포스코퓨처엠 | public event/disclosure, customer quality, backlog visibility, relative strength | multiple public sources, financial visibility, durable customer confirmation | none at entry | none |
| 에코프로비엠 | public event/disclosure, customer quality, capacity route, relative strength | multiple public sources, financial visibility, repeat order/conversion | valuation blowoff and positioning overheat near July 2023 | none |
| 더블유씨피 | relative strength, capacity route, customer/order expectation | limited financial visibility only | valuation/positioning risk later | thesis-break watch only |

Evidence rule: price-only action is not used to create Stage2/Stage3 evidence. The price rows validate outcome after the date; they do not define the trigger.

## 10. Price Data Source Map

| symbol | company | profile_path | representative price_shard_path | raw status |
|---:|---|---|---|---|
| 003670 | 포스코퓨처엠 | atlas/symbol_profiles/003/003670.json | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | no 2023 180D corporate-action overlap |
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | no 2023 180D corporate-action overlap |
| 393890 | 더블유씨피 | atlas/symbol_profiles/393/393890.json | atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv | clean 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict | aggregate_role |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| TR_R3L66_003670_20230131_S2A | 003670 | 포스코퓨처엠 | Stage2-Actionable | 2023-01-30 | 2023-01-31 | 224000 | 88.62 | -5.58 | 209.82 | -5.58 | current_profile_missed_structural | representative |
| TR_R3L66_247540_20230203_S2A | 247540 | 에코프로비엠 | Stage2-Actionable | 2023-02-03 | 2023-02-03 | 114100 | 176.51 | -1.84 | 411.83 | -1.84 | current_profile_missed_structural | representative |
| TR_R3L66_393890_20230203_S2A | 393890 | 더블유씨피 | Stage2-Actionable | 2023-02-03 | 2023-02-03 | 51200 | 36.33 | -20.7 | 70.9 | -20.7 | current_profile_false_positive | representative |
| TR_R3L66_247540_20230725_4B | 247540 | 에코프로비엠 | 4B-Overlay | 2023-07-25 | 2023-07-25 | 462000 | 26.41 | -59.39 | 26.41 | -59.39 | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| symbol | entry | entry_price | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 003670 | 2023-01-31 | 224000 | +20.54 / -5.58 | +88.62 / -5.58 | +209.82 / -5.58 | 2023-07-26 | 694000 | -69.52 |
| 247540 | 2023-02-03 | 114100 | +101.14 / -1.84 | +176.51 / -1.84 | +411.83 / -1.84 | 2023-07-26 | 584000 | -67.88 |
| 393890 | 2023-02-03 | 51200 | +5.86 / -20.70 | +36.33 / -20.70 | +70.90 / -20.70 | 2023-08-01 | 87700 | -51.66 |

### 4B overlay trigger

| symbol | 4B entry | entry_price | full_window_peak | local_peak_proximity | full_window_peak_proximity | 90D MFE / MAE | verdict |
|---:|---:|---:|---:|---:|---:|---:|---|
| 247540 | 2023-07-25 | 462000 | 584000 | 0.740 | 0.740 | +26.41 / -59.39 | good_full_window_4B_timing |

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| current profile 판단 | direct orderbook positives likely remain Yellow longer than ideal; generic WCP-like orderbook can be over-promoted if theme evidence is weighted too similarly |
| 실제 MFE/MAE와 맞았나 | partially: positives show high MFE with low MAE; counterexample shows much higher early MAE and weaker durability |
| Stage2 bonus | kept; not the residual issue |
| Yellow threshold 75 | kept; WCP can be Yellow but should not become Green |
| Green 87 / revision 55 | too strict for signed direct customer orderbook; not too strict for generic separator narrative |
| price-only blowoff guard | kept |
| full 4B non-price requirement | strengthened by EcoProBM 4B overlay |
| hard 4C routing | kept; no hard 4C row in this loop |

Case-level verdicts:

```text
003670 = current_profile_missed_structural
247540 = current_profile_missed_structural
393890 = current_profile_false_positive
247540_4B = current_profile_correct
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2_Actionable entry | proxy Green date/price | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 003670 | 224000 | 2023-03-07 / 260500 | 694000 | 0.078 | Green not dangerously late if direct contract bridge is allowed |
| 247540 | 114100 | 2023-03-06 / 217000 | 584000 | 0.219 | still acceptable, but current strict revision gate can delay recognition |
| 393890 | 51200 | no confirmed Green | 87700 | n/a | do not force Green; high MAE and weak bridge argue for guard |

C11 conclusion: Green strictness should not be globally relaxed. Instead, direct contracted orderbook with named customer and backlog visibility gets a canonical bridge; generic battery orderbook narrative needs a guard.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| TR_R3L66_247540_20230725_4B | 0.740 | 0.740 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing |

This strengthens the existing `full_4b_requires_non_price_evidence` axis. The 4B row is not a price-only local top call; it is a risk overlay after a structural orderbook run has already been validated.

## 16. 4C Protection Audit

No hard 4C trigger is proposed in this loop. WCP is labelled `thesis_break_watch_only`, not hard 4C, because the 180D window still produced positive MFE. The residual lesson is not “short the weak case”; it is “do not promote weak-quality orderbook evidence to Green.”

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = canonical_archetype_specific preferred, sector_specific acceptable
axis = c11_direct_contracted_orderbook_green_bridge
effect = named customer + long-duration contract + backlog visibility can bridge Stage3-Green even before full revision confirmation
guard = generic orderbook/capacity narrative without customer quality and margin bridge cannot be Green
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
new_axis_proposed =
  1. c11_direct_contracted_orderbook_green_bridge
  2. c11_generic_orderbook_quality_guard
  3. c11_valuation_blowoff_4b_overlay
```

Rule wording:

> In C11, direct contracted orderbook evidence should be scored as a higher-quality bridge than generic capacity/orderbook narrative. The promotion path requires named customer quality, duration/volume visibility, and no early high-MAE warning. If those are absent, the case may remain Stage2/Yellow but should not be Green.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | default current proxy | none | 3 | all three S2A reps | 100.49 | -9.37 | 230.85 | -9.37 | 0.33 | 2 | 0.149 | 0.740 | 0.740 | mixed: positives under-promoted, WCP over-promoted |
| P0b | e2r_2_0_baseline_reference | old baseline reference | rollback comparison only | 3 | all three S2A reps | 100.49 | -9.37 | 230.85 | -9.37 | 0.33 | 2 | 0.149 | 0.740 | 0.740 | worse explainability; no C11 split |
| P1 | sector_specific_candidate_profile | L3 orderbook quality split | customer-quality guard; direct orderbook bridge | 3 | two promoted, WCP blocked | 132.56 | -3.71 | 310.82 | -3.71 | 0.00 | 0 | 0.149 | 0.740 | 0.740 | improved score-return alignment |
| P2 | canonical_archetype_candidate_profile | C11 canonical compression | direct contracted orderbook + generic narrative guard | 3 | two promoted, WCP blocked | 132.56 | -3.71 | 310.82 | -3.71 | 0.00 | 0 | 0.149 | 0.740 | 0.740 | best fit for this loop |
| P3 | counterexample_guard_profile | WCP-like high MAE guard | weak margin/customer quality blocks Green | 1 | WCP blocked | 36.33 | -20.70 | 70.90 | -20.70 | 0.00 | 0 | n/a | n/a | n/a | improves false-positive control only |

## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | MFE_180D | MAE_180D | alignment |
|---|---|---|---:|---:|---|
| 003670 | 84 / Stage3-Yellow | 89 / Stage3-Green_shadow | +209.82 | -5.58 | after profile better captures structural orderbook |
| 247540 | 86 / Stage3-Yellow_high | 90 / Stage3-Green_shadow | +411.83 | -1.84 | after profile better captures extreme rerating |
| 393890 | 77 / Yellow/Green candidate risk | 66 / Stage2-Watch_or_Yellow_blocked | +70.90 | -20.70 | after profile reduces false-positive Green risk |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | mixed C11 fine types | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 3 | true | true | C11 now has 2 positive, 1 counterexample, 1 4B overlay; needs C13/C14 next |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_false_positive
  - high_mae_orderbook_counterexample
new_axis_proposed:
  - c11_direct_contracted_orderbook_green_bridge
  - c11_generic_orderbook_quality_guard
  - c11_valuation_blowoff_4b_overlay
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: avg=30.0; new symbols=3; same_archetype_new_symbol_count=3; counterexample=1
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Songdaiki/stock-web manifest/schema/profile/price rows.
- 003670, 247540, 393890 representative 2023 entry windows.
- 30D/90D/180D MFE/MAE proxy calculations.
- 4B local vs full-window split for 247540 July 2023 overlay.
- Same-entry dedupe and aggregate inclusion fields.
```

Not validated:

```text
- No live 2026 candidate scan.
- No broker/API execution.
- No stock_agent source code.
- No production scoring change.
- No recommendation or watchlist.
- 1Y/2Y figures are not used for weight calibration in this loop.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_direct_contracted_orderbook_green_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Direct named customer + long-duration contracted orderbook should bridge Stage3-Green even before full revision confirmation when MAE is controlled.","Keeps 2 positives; avg 180D MFE 310.82% for promoted positives.","TR_R3L66_003670_20230131_S2A|TR_R3L66_247540_20230203_S2A",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c11_generic_orderbook_quality_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Generic battery orderbook/theme without direct customer quality and margin bridge should not be promoted to Green.","Blocks WCP-like high-MAE counterexample from Green; false positive rate falls from 0.33 to 0.00 in this loop.","TR_R3L66_393890_20230203_S2A",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c11_valuation_blowoff_4b_overlay,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"After orderbook rerating, valuation/positioning evidence near 0.7+ full-window peak proximity is a 4B overlay, not a price-only sell rule.","EcoproBM 4B overlay at 0.740 full-window proximity captured drawdown risk after July 2023 blowoff.","TR_R3L66_247540_20230725_4B",1,0,0,low,canonical_shadow_only,"overlay row; not entry calibration"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"CASE_R3L66_003670_POSCOFUTUREM_ORDERBOOK","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"66","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_LONG_TERM_CELL_CUSTOMER_ORDERBOOK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R3L66_003670_20230131_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"direct large contract + backlog visibility aligned with +209.82% 180D MFE","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"C11 needs contract-quality promotion, not generic Stage2 repeat."}
{"row_type":"case","case_id":"CASE_R3L66_247540_ECOPROBM_ORDERBOOK","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"66","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_CUSTOMER_CAPACITY_ORDERBOOK_REPRICING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R3L66_247540_20230203_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer/capacity/orderbook route aligned with +411.83% 180D MFE; 4B overlay needed near July blowoff","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Positive entry and 4B overlay separated."}
{"row_type":"case","case_id":"CASE_R3L66_393890_WCP_SEPARATOR_COUNTER","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"66","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SEPARATOR_CUSTOMER_ORDERBOOK_HIGH_MAE_COUNTEREXAMPLE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TR_R3L66_393890_20230203_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"theme/orderbook narrative produced upside but high early MAE and weak durability; requires guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample for treating all battery orderbook narratives as equal."}
{"row_type":"trigger","trigger_id":"TR_R3L66_003670_20230131_S2A","case_id":"CASE_R3L66_003670_POSCOFUTUREM_ORDERBOOK","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"66","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_LONG_TERM_CELL_CUSTOMER_ORDERBOOK","sector":"battery_materials","primary_archetype":"long_duration_cathode_supply_orderbook","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-30","evidence_available_at_that_date":"대형 셀 고객 장기 양극재 공급계약/수주잔고 확대가 공개되어 다음 거래일 종가 진입으로 처리.","evidence_source":"company disclosure/news; price rows from Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-31","entry_price":224000,"MFE_30D_pct":20.54,"MFE_90D_pct":88.62,"MFE_180D_pct":209.82,"MFE_1Y_pct":209.82,"MFE_2Y_pct":null,"MAE_30D_pct":-5.58,"MAE_90D_pct":-5.58,"MAE_180D_pct":-5.58,"MAE_1Y_pct":-5.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-69.52,"green_lateness_ratio":0.078,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_MFE_clean_180D","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R3L66_003670_20230131_224000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R3L66_247540_20230203_S2A","case_id":"CASE_R3L66_247540_ECOPROBM_ORDERBOOK","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"66","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_CUSTOMER_CAPACITY_ORDERBOOK_REPRICING","sector":"battery_materials","primary_archetype":"cathode_orderbook_capacity_rerating","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-03","evidence_available_at_that_date":"양극재 수요/고객/증설 서사가 공시·뉴스·상대강도로 동시에 확인되기 시작한 구간. 당일 장중 반응 가능으로 종가 진입 처리.","evidence_source":"company disclosure/news; price rows from Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-03","entry_price":114100,"MFE_30D_pct":101.14,"MFE_90D_pct":176.51,"MFE_180D_pct":411.83,"MFE_1Y_pct":411.83,"MFE_2Y_pct":null,"MAE_30D_pct":-1.84,"MAE_90D_pct":-1.84,"MAE_180D_pct":-1.84,"MAE_1Y_pct":-1.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-67.88,"green_lateness_ratio":0.219,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_extreme_MFE_clean_180D","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R3L66_247540_20230203_114100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R3L66_393890_20230203_S2A","case_id":"CASE_R3L66_393890_WCP_SEPARATOR_COUNTER","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"66","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SEPARATOR_CUSTOMER_ORDERBOOK_HIGH_MAE_COUNTEREXAMPLE","sector":"battery_materials","primary_archetype":"separator_orderbook_counterexample","loop_objective":"counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-03","evidence_available_at_that_date":"분리막 증설/고객 기대와 2차전지 동반 랠리가 존재했으나, 계약 확정성·마진 브리지·반복 고객 신호는 양극재 대표주보다 약했다.","evidence_source":"company/news narrative; price rows from Songdaiki/stock-web","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-03","entry_price":51200,"MFE_30D_pct":5.86,"MFE_90D_pct":36.33,"MFE_180D_pct":70.9,"MFE_1Y_pct":71.0,"MFE_2Y_pct":null,"MAE_30D_pct":-20.7,"MAE_90D_pct":-20.7,"MAE_180D_pct":-20.7,"MAE_1Y_pct":-25.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-01","peak_price":87700,"drawdown_after_peak_pct":-51.66,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_from_entry","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_counterexample_orderbook_quality_gap","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R3L66_393890_20230203_51200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R3L66_247540_20230725_4B","case_id":"CASE_R3L66_247540_ECOPROBM_ORDERBOOK","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"66","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_CUSTOMER_CAPACITY_ORDERBOOK_REPRICING","sector":"battery_materials","primary_archetype":"cathode_orderbook_capacity_rerating","loop_objective":"4B_non_price_requirement_stress_test|sector_specific_rule_discovery","trigger_type":"4B-Overlay","trigger_date":"2023-07-25","evidence_available_at_that_date":"급격한 밸류에이션 리프라이싱과 포지셔닝 과열이 관찰된 구간. 가격 고점 자체가 아니라 밸류에이션/수급 과열 overlay로만 기록.","evidence_source":"market valuation/positioning narrative; price rows from Songdaiki/stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-25","entry_price":462000,"MFE_30D_pct":26.41,"MFE_90D_pct":26.41,"MFE_180D_pct":26.41,"MFE_1Y_pct":26.41,"MFE_2Y_pct":null,"MAE_30D_pct":-35.39,"MAE_90D_pct":-59.39,"MAE_180D_pct":-59.39,"MAE_1Y_pct":-59.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-67.88,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R3L66_247540_20230725_462000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_different_trigger_family_4B_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R3L66_003670_POSCOFUTUREM_ORDERBOOK","trigger_id":"TR_R3L66_003670_20230131_S2A","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":9,"backlog_visibility_score":9,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":10,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":8,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green_shadow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score"],"component_delta_explanation":"C11 shadow splits direct contracted orderbook quality from generic battery theme/orderbook narrative.","MFE_90D_pct":88.62,"MAE_90D_pct":-5.58,"score_return_alignment_label":"promotion_aligns_with_large_MFE","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R3L66_247540_ECOPROBM_ORDERBOOK","trigger_id":"TR_R3L66_247540_20230203_S2A","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":8,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":10,"customer_quality_score":8,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow_high","raw_component_scores_after":{"contract_score":9,"backlog_visibility_score":9,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green_shadow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score"],"component_delta_explanation":"C11 shadow splits direct contracted orderbook quality from generic battery theme/orderbook narrative.","MFE_90D_pct":176.51,"MAE_90D_pct":-1.84,"score_return_alignment_label":"promotion_aligns_with_extreme_MFE","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R3L66_393890_WCP_SEPARATOR_COUNTER","trigger_id":"TR_R3L66_393890_20230203_S2A","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Watch_or_Yellow_blocked","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C11 shadow splits direct contracted orderbook quality from generic battery theme/orderbook narrative.","MFE_90D_pct":36.33,"MAE_90D_pct":-20.7,"score_return_alignment_label":"guard_improves_false_positive_control","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"66","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3,"diversity_score_summary":"avg=30.0; new symbols=3; counterexample=1; no same-symbol same-trigger reuse","auto_selected_coverage_gap":"C11_BATTERY_ORDERBOOK_RERATING","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive","high_mae_orderbook_counterexample"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_round = R3_loop_67_C13_BATTERY_JV_UTILIZATION_AMPC_IRA
coverage_goal = add AMPC/IRA/JV utilization positive + call-off or utilization counterexample
avoid_reuse = do not reuse 003670/247540/393890 same trigger dates
```

## 28. Source Notes

Stock-Web source files inspected in this session:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/003/003670.json
atlas/symbol_profiles/247/247540.json
atlas/symbol_profiles/393/393890.json
atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv
atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv
atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv
```

Important data caveat:

```text
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_contaminated_window = blocked by default
```

This file intentionally contains no production patch and no live investment recommendation.
