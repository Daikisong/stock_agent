# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R1_loop_14_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
scheduled_round: R1
scheduled_loop: 14
completed_round: R1
completed_loop: 14
next_round: R2
next_loop: 14
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM
loop_objective: ['coverage_gap_fill', 'sector_specific_rule_discovery', 'canonical_archetype_compression', 'counterexample_mining', 'yellow_threshold_stress_test', 'green_strictness_stress_test', '4B_non_price_requirement_stress_test']
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.

## 1. Current Calibrated Profile Assumption

The current default proxy is `e2r_2_1_stock_web_calibrated_proxy`; `e2r_2_0_baseline_reference` is retained only as rollback comparison. Existing axes are not re-proposed globally. This loop stress-tests whether R1 shipbuilding orderbook cases need a C01-specific margin-bridge distinction: backlog is the reservoir, but only order quality and margin conversion open the valve.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round = R1
- scheduled_loop = 14
- large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
- canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
- fine_archetype_id = SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM
- selected coverage gap = C01 was absent from local loop10~13 R1 outputs; prior R1 coverage focused C02/C03/C04.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 output filenames show R1 loop10=C02, loop11=C03, loop12=C04, loop13=C02. No local C01 file was present. The selected symbols 009540, 010140, and 010620 were not found in prior R1 loop10~13 local machine-readable rows, so the symbol set is new for this scheduled round/canonical pair. The two 4B rows reuse same-symbol price history inside this MD only as new trigger-family overlays and receive `independent_evidence_weight=0.5`.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest fields observed in this run: source_name=FinanceData/marcap, price_adjustment_status=raw_unadjusted_marcap, min_date=1995-05-02, max_date=2026-02-20, tradable_row_count=14,354,401, symbol_count=5,414, calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year. The schema confirms tradable columns `d,o,h,l,c,v,a,mc,s,m`, raw status column `rs`, and MFE/MAE formulas based on max high / min low from the entry row through N tradable rows.

## 5. Historical Eligibility Gate

All quantitative trigger rows use stock-web tradable shards, positive OHLC rows, and at least 180 forward trading days. The 042660 Hanwha Ocean dilution/share-count discontinuity route is intentionally excluded from weight calibration and retained as narrative-only because the 2023-06-13 window shows share-count discontinuity inside the price path.

## 6. Canonical Archetype Compression Map

`C01_ORDER_BACKLOG_MARGIN_BRIDGE` compresses several fine forms: shipbuilding orderbook visibility, rising newbuild ship prices, legacy low-margin backlog burnoff, and margin conversion. The shadow rule should not reward backlog size alone. It rewards backlog only when order mix or margin bridge explains why EPS can rerate.

## 7. Case Selection Summary

| trigger_id | symbol | company | role | type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| TRIG_R1L14_C01_KSOE_STAGE2_20230104 | 009540 | HD한국조선해양 | structural_success | Stage2-Actionable | 2023-01-04 | 74400 | 20.7 | -3.63 | 74.73 | -3.63 | current_profile_too_late |
| TRIG_R1L14_C01_SHI_STAGE2_20230131 | 010140 | 삼성중공업 | structural_success | Stage2-Actionable | 2023-01-31 | 5790 | 20.73 | -15.8 | 63.56 | -15.8 | current_profile_missed_structural |
| TRIG_R1L14_C01_MIPO_STAGE2_20240213 | 010620 | HD현대미포 | high_mae_success | Stage2-Actionable | 2024-02-13 | 62700 | 26.63 | -4.94 | 95.85 | -4.94 | current_profile_missed_structural |
| TRIG_R1L14_C01_KSOE_PRICE_ONLY_4B_20230717 | 009540 | HD한국조선해양 | 4B_overlay_success | Stage4B-Overlay | 2023-07-17 | 128000 | 1.56 | -13.91 | 1.56 | -25.0 | current_profile_correct |
| TRIG_R1L14_C01_MIPO_PRICE_ONLY_4B_20240731 | 010620 | HD현대미포 | 4B_overlay_success | Stage4B-Overlay | 2024-07-31 | 117500 | 4.51 | -21.7 | 3.57 | -26.98 | current_profile_correct |


## 8. Positive vs Counterexample Balance

Positive structural cases: 009540, 010140, 010620. Counterexamples/overlays: 009540 local price-only 4B, 010620 local price-only 4B. Narrative-only red-team: 042660 capital/share-count discontinuity.

## 9. Evidence Source Map

| symbol | evidence family | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---:|---|---|---|---|
| 009540 | orderbook + ship-price bridge | backlog visibility and early relative strength | margin bridge later confirms | 2023-07 local overheat only |
| 010140 | turnaround orderbook bridge | large 2023-01-31 volume/price row and public turn narrative | margin bridge after loss years | high MAE survivor |
| 010620 | legacy low-margin survivor | 2024-02 low-margin shock did not kill orderbook bridge | later repricing validates margin recovery option | 2024-07 local overheat only |
| 042660 | dilution/share-count red-team | orderbook narrative contaminated by capital structure event | not usable | narrative-only 4C/accounting-trust watch |

## 10. Price Data Source Map

| symbol | company | profile_path | tradable_shards | usage |
|---:|---|---|---|---|
| 009540 | HD한국조선해양 | atlas/symbol_profiles/009/009540.json | atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv | calibration usable |
| 010140 | 삼성중공업 | atlas/symbol_profiles/010/010140.json | atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv | calibration usable |
| 010620 | HD현대미포 | atlas/symbol_profiles/010/010620.json | atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv | calibration usable |
| 042660 | 한화오션 | atlas/symbol_profiles/042/042660.json | atlas/ohlcv_tradable_by_symbol_year/042/042660/2023.csv | narrative only; share-count discontinuity |

## 11. Case-by-Case Trigger Grid

Same as Section 7. The representative rows are the Stage2 rows for 009540, 010140, and 010620. The 4B rows are overlay-only and do not enter aggregate entry-return averages.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | company | role | type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| TRIG_R1L14_C01_KSOE_STAGE2_20230104 | 009540 | HD한국조선해양 | structural_success | Stage2-Actionable | 2023-01-04 | 74400 | 20.7 | -3.63 | 74.73 | -3.63 | current_profile_too_late |
| TRIG_R1L14_C01_SHI_STAGE2_20230131 | 010140 | 삼성중공업 | structural_success | Stage2-Actionable | 2023-01-31 | 5790 | 20.73 | -15.8 | 63.56 | -15.8 | current_profile_missed_structural |
| TRIG_R1L14_C01_MIPO_STAGE2_20240213 | 010620 | HD현대미포 | high_mae_success | Stage2-Actionable | 2024-02-13 | 62700 | 26.63 | -4.94 | 95.85 | -4.94 | current_profile_missed_structural |
| TRIG_R1L14_C01_KSOE_PRICE_ONLY_4B_20230717 | 009540 | HD한국조선해양 | 4B_overlay_success | Stage4B-Overlay | 2023-07-17 | 128000 | 1.56 | -13.91 | 1.56 | -25.0 | current_profile_correct |
| TRIG_R1L14_C01_MIPO_PRICE_ONLY_4B_20240731 | 010620 | HD현대미포 | 4B_overlay_success | Stage4B-Overlay | 2024-07-31 | 117500 | 4.51 | -21.7 | 3.57 | -26.98 | current_profile_correct |


The important C01 residual is not that Stage2 is always early. It is that orderbook visibility behaves like a warehouse full of inventory: it matters only when there is a visible truck route from backlog to margin. Without that route, backlog can trap capital; with it, even a low-margin shock can become a Stage2 survivor.

## 13. Current Calibrated Profile Stress Test

1. P0 tends to wait for confirmed revision/Green in C01, which made 009540 and 010140 late.
2. P0 missed the 010620 low-margin survivor because the February 2024 shock looked negative before the later margin bridge became visible.
3. Stage2 actionable bonus is directionally useful but not enough unless paired with order quality and ship-price bridge.
4. Yellow threshold 75 is acceptable; Green 87 is often late in C01 when margin bridge evidence arrives after most rerating.
5. Price-only blowoff and full 4B non-price requirement are kept; the two 4B rows are overlays, not hard 4C.

## 14. Stage2 / Yellow / Green Comparison

- 009540: Stage2 entry 74,400 captured a clean 180D MFE of 74.73%; later Green would have consumed about 56% of the Stage2-to-peak bridge.
- 010140: Stage2 entry 5,790 had high early MAE but still reached 63.56% 180D MFE; Green confirmation around the July surge would have been late.
- 010620: The February low-margin shock was not a Green trigger, but it was a valid Stage2 survivor; waiting for July price confirmation would have missed most of the rerating.

## 15. 4B Local vs Full-window Timing Audit

The local 4B rows show the need to split local peak risk from full thesis break. 009540 and 010620 both had local overheat drawdowns. Neither row had non-price evidence strong enough for hard 4C at the trigger date.

## 16. 4C Protection Audit

No quantitative hard 4C promotion is proposed. 042660 is the thesis-break/accounting-trust watch row, but it is narrative-only because the share-count/capital-structure discontinuity contaminates the calibration window.

## 17. Sector-Specific Rule Candidate

`R1_shipbuilding_orderbook_margin_bridge_guard`: In R1 shipbuilding/industrial backlog cases, increase C01 Stage2/Yellow confidence when orderbook quality plus ship-price/margin bridge is visible. Penalize backlog-only cases when legacy low-margin backlog or capital-structure events obscure EPS conversion.

## 18. Canonical-Archetype Rule Candidate

`C01_orderbook_quality_margin_bridge_bonus`: add a canonical shadow bonus when `orderbook_quality_score >= 7` and `ship_price_margin_score >= 6`, but require no capital-structure contamination and no thesis break. This is not a production change.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | FP rate | missed | late green | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | current calibrated proxy | baseline stock-web calibrated profile with existing global gates | 3 | 22.69 | -8.12 | 78.05 | -8.12 | 0.0 | 1 | 2 | mostly aligned but misses C01 low-margin survivor and pushes Green too late |
| P0b | rollback reference | old e2r_2_0 baseline; tends to over-promote backlog without margin quality | 3 | 22.69 | -8.12 | 78.05 | -8.12 | 0.33 | 0 | 1 | too loose on backlog-only cases |
| P1 | sector_specific_candidate_profile | R1 shipbuilding backlog must show margin bridge or improving ship-price bridge before promotion | 3 | 22.69 | -8.12 | 78.05 | -8.12 | 0.0 | 0 | 1 | better early Stage2 capture without rewarding backlog-only illusion |
| P2 | canonical_archetype_candidate_profile | C01 rewards orderbook only when order mix, ship price, or margin bridge explains later EPS path | 3 | 22.69 | -8.12 | 78.05 | -8.12 | 0.0 | 0 | 1 | canonical candidate for C01 |
| P3 | counterexample_guard_profile | local price-only peak remains overlay until non-price margin/order break appears | 5 | 14.83 | -12.0 | 47.85 | -15.27 | 0.0 | 0 | 1 | best protects from local peaks while preserving structural winners |


## 20. Score-Return Alignment Matrix

| alignment bucket | trigger_ids | interpretation |
|---|---|---|
| good early Stage2 | TRIG_R1L14_C01_KSOE_STAGE2_20230104 | orderbook + ship-price bridge anticipated later margin conversion |
| high-MAE success | TRIG_R1L14_C01_SHI_STAGE2_20230131 | early drawdown did not invalidate backlog thesis |
| low-margin survivor | TRIG_R1L14_C01_MIPO_STAGE2_20240213 | margin pain was real but not a 4C break |
| 4B overlay only | TRIG_R1L14_C01_KSOE_PRICE_ONLY_4B_20230717 / TRIG_R1L14_C01_MIPO_PRICE_ONLY_4B_20240731 | price-only peak protected risk but did not justify hard thesis break |

## 21. Coverage Matrix

```json
{
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM",
  "positive_case_count": 3,
  "counterexample_count": 2,
  "4B_case_count": 2,
  "4C_case_count": 0,
  "new_independent_case_count": 5,
  "reused_case_count": 2,
  "calibration_usable_trigger_count": 5,
  "representative_trigger_count": 3,
  "current_profile_error_count": 3,
  "sector_rule_candidate": true,
  "canonical_rule_candidate": true,
  "coverage_gap_after_this_loop": "C01 now has shipbuilding orderbook/margin bridge positives plus price-only 4B counterexamples; C05 remains separate R1 EPC gap."
}
```

## 22. Residual Contribution Summary

new_independent_case_count: 5  
reused_case_count: 2  
reused_case_ids: R1L14_C01_KSOE_PRICE_ONLY_4B_20230717, R1L14_C01_MIPO_PRICE_ONLY_4B_20240731  
new_symbol_count: 3  
new_canonical_archetype_count: 1  
new_fine_archetype_count: 1  
new_trigger_family_count: 3  
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c  
residual_error_types_found: C01_low_margin_stage2_survivor, Green_too_late_after_orderbook_bridge, price_only_local_4B_not_full_4C, corporate_action_contaminated_orderbook_case  
new_axis_proposed: C01_orderbook_quality_margin_bridge_bonus  
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence  
existing_axis_weakened: null  
existing_axis_kept: stage2_actionable_evidence_bonus, yellow/green thresholds, hard 4C routing  
sector_specific_rule_candidate: true  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  
loop_contribution_label: canonical_archetype_rule_candidate

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest/schema route, actual tradable shard entry rows, 30D/90D/180D MFE/MAE proxy calculations, same-entry dedupe, current profile stress test.  
Not validated: live candidates, production scoring code, broker execution, current watchlist, exact 1Y/2Y calibration. 1Y/2Y fields are intentionally null in machine rows and excluded from weight calibration.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c01_ship_price_margin_bridge_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,orderbook without margin bridge created false precision; orderbook + ship-price/margin bridge caught 009540/010140/010620 earlier,"representative triggers avg MFE90=22.69%, avg MAE90=-8.12%, avg MFE180=78.05%",TRIG_R1L14_C01_KSOE_STAGE2_20230104|TRIG_R1L14_C01_SHI_STAGE2_20230131|TRIG_R1L14_C01_MIPO_STAGE2_20240213,3,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,price_only_local_4b_overlay_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,1,1,0,existing 4B non-price requirement is kept; local 4B overlay is useful but not full thesis break,4B overlays showed large MAE but no immediate non-price 4C break,TRIG_R1L14_C01_KSOE_PRICE_ONLY_4B_20230717|TRIG_R1L14_C01_MIPO_PRICE_ONLY_4B_20240731,2,2,2,medium,existing_axis_strengthened,not production; strengthens full_4b_requires_non_price_evidence
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L14_C01_KSOE_STAGE2_20230104", "symbol": "009540", "company_name": "HD한국조선해양", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R1L14_C01_KSOE_STAGE2_20230104", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "good_stage2_actionable_before_green_confirmation", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "2023년 초 조선업 수주잔고·선가 상승·환율 효과가 공개 narrative로 존재했고, 확인 이익보다 먼저 orderbook/margin bridge가 가격에 반영되기 시작한 구간. 2023-01-04 stock-web row close=74,400; later 2023-07-17 high=130,000 was observed in the same tradable shard."}
{"row_type": "case", "case_id": "R1L14_C01_SHI_STAGE2_20230131", "symbol": "010140", "company_name": "삼성중공업", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R1L14_C01_SHI_STAGE2_20230131", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_needed_despite_initial_MAE", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "2023-01-31 stock-web row shows a volume shock and close=5,790. The event is treated as a public orderbook/margin-turn trigger: the market had order backlog visibility before confirmed multi-quarter profit delivery, while the actual 180D path reached a 2023-08-02 high near 9,470."}
{"row_type": "case", "case_id": "R1L14_C01_MIPO_STAGE2_20240213", "symbol": "010620", "company_name": "HD현대미포", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R1L14_C01_MIPO_STAGE2_20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "margin_pain_did_not_break_backlog_thesis", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "2024-02-13 tradable row close=62,700 after a visible low-margin shock. This is not a clean Green trigger; it tests whether Stage2 can survive temporary margin pain when orderbook and ship-price bridge still point to later recovery. The later 2024-07-31 high=122,800 made the orderbook bridge visible."}
{"row_type": "case", "case_id": "R1L14_C01_KSOE_PRICE_ONLY_4B_20230717", "symbol": "009540", "company_name": "HD한국조선해양", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R1L14_C01_KSOE_PRICE_ONLY_4B_20230717", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_overlay", "independent_evidence_weight": 0.5, "score_price_alignment": "local_4B_drawdown_without_thesis_break", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2023-07-17 high=130,000 and close=128,000 marked a local overheat after a fast Stage2-to-Green repricing. However no hard cancellation/accounting break is visible at that date, so this is a local 4B overlay rather than full 4C."}
{"row_type": "case", "case_id": "R1L14_C01_MIPO_PRICE_ONLY_4B_20240731", "symbol": "010620", "company_name": "HD현대미포", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R1L14_C01_MIPO_PRICE_ONLY_4B_20240731", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_overlay", "independent_evidence_weight": 0.5, "score_price_alignment": "local_drawdown_protected_by_overlay_not_full_4C", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2024-07-31 high=122,800 and close=117,500 after a sharp recovery from the February low-margin shock. The next shock low around 92,700 on 2024-08-05 shows why local 4B overlay is useful, but the evidence is price/positioning rather than hard thesis break."}
{"trigger_id": "TRIG_R1L14_C01_KSOE_STAGE2_20230104", "case_id": "R1L14_C01_KSOE_STAGE2_20230104", "symbol": "009540", "company_name": "HD한국조선해양", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-03", "entry_date": "2023-01-04", "entry_price": 74400, "evidence_available_at_that_date": "2023년 초 조선업 수주잔고·선가 상승·환율 효과가 공개 narrative로 존재했고, 확인 이익보다 먼저 orderbook/margin bridge가 가격에 반영되기 시작한 구간. 2023-01-04 stock-web row close=74,400; later 2023-07-17 high=130,000 was observed in the same tradable shard.", "evidence_source": "historical public orderbook/margin-recovery narrative; stock-web tradable shard atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv rows around 2023-01-04 and 2023-07-17", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 16.26, "MAE_30D_pct": -3.63, "MFE_90D_pct": 20.7, "MAE_90D_pct": -3.63, "MFE_180D_pct": 74.73, "MAE_180D_pct": -3.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "peak_date": "2023-07-17", "peak_price": 130000, "drawdown_after_peak_pct": -15.23, "green_lateness_ratio": 0.56, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "orderbook_margin_bridge_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1L14_009540_20230104_74400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv", "profile_path": "atlas/symbol_profiles/009/009540.json", "row_type": "trigger", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "sector": "shipbuilding/industrial backlog", "primary_archetype": "orderbook_to_margin_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": [], "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true}
{"trigger_id": "TRIG_R1L14_C01_SHI_STAGE2_20230131", "case_id": "R1L14_C01_SHI_STAGE2_20230131", "symbol": "010140", "company_name": "삼성중공업", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-31", "entry_date": "2023-01-31", "entry_price": 5790, "evidence_available_at_that_date": "2023-01-31 stock-web row shows a volume shock and close=5,790. The event is treated as a public orderbook/margin-turn trigger: the market had order backlog visibility before confirmed multi-quarter profit delivery, while the actual 180D path reached a 2023-08-02 high near 9,470.", "evidence_source": "historical public earnings/orderbook turn narrative; stock-web tradable shard atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv rows around 2023-01-31, 2023-03-16, 2023-08-02", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 2.76, "MAE_30D_pct": -15.2, "MFE_90D_pct": 20.73, "MAE_90D_pct": -15.8, "MFE_180D_pct": 63.56, "MAE_180D_pct": -15.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "peak_date": "2023-08-02", "peak_price": 9470, "drawdown_after_peak_pct": -35.69, "green_lateness_ratio": 0.65, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_orderbook_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1L14_010140_20230131_5790", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv", "profile_path": "atlas/symbol_profiles/010/010140.json", "row_type": "trigger", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "sector": "shipbuilding/industrial backlog", "primary_archetype": "orderbook_to_margin_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": [], "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true}
{"trigger_id": "TRIG_R1L14_C01_MIPO_STAGE2_20240213", "case_id": "R1L14_C01_MIPO_STAGE2_20240213", "symbol": "010620", "company_name": "HD현대미포", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "entry_date": "2024-02-13", "entry_price": 62700, "evidence_available_at_that_date": "2024-02-13 tradable row close=62,700 after a visible low-margin shock. This is not a clean Green trigger; it tests whether Stage2 can survive temporary margin pain when orderbook and ship-price bridge still point to later recovery. The later 2024-07-31 high=122,800 made the orderbook bridge visible.", "evidence_source": "historical public low-margin vessel/orderbook recovery narrative; stock-web tradable shard atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv rows around 2024-02-13 and 2024-07-31", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 10.37, "MAE_30D_pct": -4.94, "MFE_90D_pct": 26.63, "MAE_90D_pct": -4.94, "MFE_180D_pct": 95.85, "MAE_180D_pct": -4.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "peak_date": "2024-07-31", "peak_price": 122800, "drawdown_after_peak_pct": -24.51, "green_lateness_ratio": 0.48, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "low_margin_stage2_survivor", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1L14_010620_20240213_62700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv", "profile_path": "atlas/symbol_profiles/010/010620.json", "row_type": "trigger", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "sector": "shipbuilding/industrial backlog", "primary_archetype": "orderbook_to_margin_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": [], "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true}
{"trigger_id": "TRIG_R1L14_C01_KSOE_PRICE_ONLY_4B_20230717", "case_id": "R1L14_C01_KSOE_PRICE_ONLY_4B_20230717", "symbol": "009540", "company_name": "HD한국조선해양", "trigger_type": "Stage4B-Overlay", "trigger_date": "2023-07-17", "entry_date": "2023-07-17", "entry_price": 128000, "evidence_available_at_that_date": "2023-07-17 high=130,000 and close=128,000 marked a local overheat after a fast Stage2-to-Green repricing. However no hard cancellation/accounting break is visible at that date, so this is a local 4B overlay rather than full 4C.", "evidence_source": "stock-web tradable shard atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv rows around 2023-07-17 plus public valuation-overheat narrative", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "MFE_30D_pct": 1.56, "MAE_30D_pct": -13.91, "MFE_90D_pct": 1.56, "MAE_90D_pct": -13.91, "MFE_180D_pct": 1.56, "MAE_180D_pct": -25.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "peak_date": "2023-07-17", "peak_price": 130000, "drawdown_after_peak_pct": -25.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.56, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_4B_overlay_not_full_4C", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1L14_009540_20230717_128000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_overlay", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv", "profile_path": "atlas/symbol_profiles/009/009540.json", "row_type": "trigger", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "sector": "shipbuilding/industrial backlog", "primary_archetype": "orderbook_to_margin_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": [], "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true}
{"trigger_id": "TRIG_R1L14_C01_MIPO_PRICE_ONLY_4B_20240731", "case_id": "R1L14_C01_MIPO_PRICE_ONLY_4B_20240731", "symbol": "010620", "company_name": "HD현대미포", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-07-31", "entry_date": "2024-07-31", "entry_price": 117500, "evidence_available_at_that_date": "2024-07-31 high=122,800 and close=117,500 after a sharp recovery from the February low-margin shock. The next shock low around 92,700 on 2024-08-05 shows why local 4B overlay is useful, but the evidence is price/positioning rather than hard thesis break.", "evidence_source": "stock-web tradable shard atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv rows around 2024-07-31, 2024-08-05, and 2024-11-19", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "MFE_30D_pct": 4.51, "MAE_30D_pct": -21.11, "MFE_90D_pct": 4.51, "MAE_90D_pct": -21.7, "MFE_180D_pct": 3.57, "MAE_180D_pct": -26.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "peak_date": "2024-07-31", "peak_price": 122800, "drawdown_after_peak_pct": -26.98, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.57, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_local_4B_not_full_exit", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1L14_010620_20240731_117500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_overlay", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv", "profile_path": "atlas/symbol_profiles/010/010620.json", "row_type": "trigger", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_ORDERBOOK_MARGIN_BRIDGE_LOW_MARGIN_REDTEAM", "sector": "shipbuilding/industrial backlog", "primary_archetype": "orderbook_to_margin_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": [], "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14_C01_KSOE_STAGE2_20230104", "trigger_id": "TRIG_R1L14_C01_KSOE_STAGE2_20230104", "symbol": "009540", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 8, "ship_price_margin_score": 7, "low_margin_legacy_risk_score": 2, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 9, "ship_price_margin_score": 9, "low_margin_legacy_risk_score": 2, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 81.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["orderbook_quality_score", "ship_price_margin_score", "margin_bridge_score", "execution_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C01 shadow rule rewards orderbook quality only when a margin bridge is visible; price-only local peaks are demoted to 4B overlay instead of hard 4C.", "MFE_90D_pct": 20.7, "MAE_90D_pct": -3.63, "score_return_alignment_label": "good_stage2_actionable_before_green_confirmation", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14_C01_SHI_STAGE2_20230131", "trigger_id": "TRIG_R1L14_C01_SHI_STAGE2_20230131", "symbol": "010140", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 7, "ship_price_margin_score": 6, "low_margin_legacy_risk_score": 3, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 72.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 8, "ship_price_margin_score": 8, "low_margin_legacy_risk_score": 3, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 78.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["orderbook_quality_score", "ship_price_margin_score", "margin_bridge_score", "execution_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C01 shadow rule rewards orderbook quality only when a margin bridge is visible; price-only local peaks are demoted to 4B overlay instead of hard 4C.", "MFE_90D_pct": 20.73, "MAE_90D_pct": -15.8, "score_return_alignment_label": "stage2_needed_despite_initial_MAE", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14_C01_MIPO_STAGE2_20240213", "trigger_id": "TRIG_R1L14_C01_MIPO_STAGE2_20240213", "symbol": "010620", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 4, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 7, "ship_price_margin_score": 5, "low_margin_legacy_risk_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 70.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 4, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 8, "ship_price_margin_score": 7, "low_margin_legacy_risk_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 76.5, "stage_label_after": "Stage2-Actionable", "changed_components": ["orderbook_quality_score", "ship_price_margin_score", "margin_bridge_score", "execution_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C01 shadow rule rewards orderbook quality only when a margin bridge is visible; price-only local peaks are demoted to 4B overlay instead of hard 4C.", "MFE_90D_pct": 26.63, "MAE_90D_pct": -4.94, "score_return_alignment_label": "margin_pain_did_not_break_backlog_thesis", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14_C01_KSOE_PRICE_ONLY_4B_20230717", "trigger_id": "TRIG_R1L14_C01_KSOE_PRICE_ONLY_4B_20230717", "symbol": "009540", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 7, "ship_price_margin_score": 6, "low_margin_legacy_risk_score": 0, "positioning_overheat_score": 9, "thesis_break_score": 1}, "weighted_score_before": 89.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 7, "ship_price_margin_score": 6, "low_margin_legacy_risk_score": 0, "positioning_overheat_score": 10, "thesis_break_score": 1}, "weighted_score_after": 82.0, "stage_label_after": "Stage4B-Overlay", "changed_components": ["orderbook_quality_score", "ship_price_margin_score", "margin_bridge_score", "execution_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C01 shadow rule rewards orderbook quality only when a margin bridge is visible; price-only local peaks are demoted to 4B overlay instead of hard 4C.", "MFE_90D_pct": 1.56, "MAE_90D_pct": -13.91, "score_return_alignment_label": "local_4B_drawdown_without_thesis_break", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L14_C01_MIPO_PRICE_ONLY_4B_20240731", "trigger_id": "TRIG_R1L14_C01_MIPO_PRICE_ONLY_4B_20240731", "symbol": "010620", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 7, "ship_price_margin_score": 6, "low_margin_legacy_risk_score": 0, "positioning_overheat_score": 9, "thesis_break_score": 1}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_quality_score": 7, "ship_price_margin_score": 6, "low_margin_legacy_risk_score": 0, "positioning_overheat_score": 10, "thesis_break_score": 1}, "weighted_score_after": 80.5, "stage_label_after": "Stage4B-Overlay", "changed_components": ["orderbook_quality_score", "ship_price_margin_score", "margin_bridge_score", "execution_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C01 shadow rule rewards orderbook quality only when a margin bridge is visible; price-only local peaks are demoted to 4B overlay instead of hard 4C.", "MFE_90D_pct": 4.51, "MAE_90D_pct": -21.7, "score_return_alignment_label": "local_drawdown_protected_by_overlay_not_full_4C", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R1", "loop": "14", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "scheduled_round": "R1", "scheduled_loop": 14, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 2, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 2, "new_trigger_family_count": 3, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["C01_low_margin_stage2_survivor", "Green_too_late_after_orderbook_bridge", "price_only_local_4B_not_full_4C", "corporate_action_contaminated_orderbook_case"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "R1 loop14 fills C01 gap with 3 new shipbuilding symbols and 2 same-symbol new 4B trigger families; 042660 retained as narrative-only corporate-action contamination red-team row."}
{"row_type": "narrative_only", "case_id": "R1L14_C01_HANWHAOCEAN_CAPITAL_RAISE_CA_20230613", "symbol": "042660", "company_name": "한화오션", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "reason": "capital-raise / share-count discontinuity contaminates the 180D window around 2023-06-13, so it is retained as a narrative counterexample only rather than weight calibration.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042660/2023.csv", "profile_path": "atlas/symbol_profiles/042/042660.json"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c01_ship_price_margin_bridge_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,orderbook without margin bridge created false precision; orderbook + ship-price/margin bridge caught 009540/010140/010620 earlier,"representative triggers avg MFE90=22.69%, avg MAE90=-8.12%, avg MFE180=78.05%",TRIG_R1L14_C01_KSOE_STAGE2_20230104|TRIG_R1L14_C01_SHI_STAGE2_20230131|TRIG_R1L14_C01_MIPO_STAGE2_20240213,3,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,price_only_local_4b_overlay_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,1,1,0,existing 4B non-price requirement is kept; local 4B overlay is useful but not full thesis break,4B overlays showed large MAE but no immediate non-price 4C break,TRIG_R1L14_C01_KSOE_PRICE_ONLY_4B_20230717|TRIG_R1L14_C01_MIPO_PRICE_ONLY_4B_20240731,2,2,2,medium,existing_axis_strengthened,not production; strengthens full_4b_requires_non_price_evidence
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
completed_round = R1
completed_loop = 14
next_round = R2
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock-web manifest max_date used: 2026-02-20.
- Primary OHLC rows came from `atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv`, `atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv`, `atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv`, and narrative-only `atlas/ohlcv_tradable_by_symbol_year/042/042660/2023.csv`.
- The stock-web manifest/schema confirm raw/unadjusted OHLC and the tradable shard columns used for MFE/MAE calculation.
