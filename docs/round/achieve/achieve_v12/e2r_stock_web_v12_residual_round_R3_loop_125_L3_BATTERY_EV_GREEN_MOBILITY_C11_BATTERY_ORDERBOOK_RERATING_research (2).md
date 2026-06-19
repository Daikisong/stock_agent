# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
selected_round: R3
selected_loop: 125
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C11 orderbook headline vs revenue/margin/utilization bridge; URL/proxy repair; positive/counterexample balance
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG
loop_objective: sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; hard_4c_transition_timing_test; complete_30_90_180_MFE_MAE
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
```

This MD is historical calibration research, not live stock research. It uses the coverage-index-first v12 prompt state and the No-Repeat Index only as an anti-duplication ledger.

## 1. Current Calibrated Profile Assumption

Assumed active profile is `e2r_2_2_rolling_calibrated` with already-applied global axes: `stage2_required_bridge`, `local_4b_watch_guard`, `earlier_thesis_break_watch`, `hard_4c_confirmation`, `price_only_blowoff_blocks_positive_stage`, and `full_4b_requires_non_price_evidence`. This loop does not propose a production global change. It proposes a C11 canonical shadow gate.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R3`
- Large sector: `L3_BATTERY_EV_GREEN_MOBILITY`
- Canonical: `C11_BATTERY_ORDERBOOK_RERATING`
- Fine: `BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG`

Scope question: when does a battery orderbook headline become a real rerating bridge, and when is it only a long-dated promise that leaks through utilization, ASP, lithium inventory, or customer ramp risk?

## 3. Previous Coverage / Duplicate Avoidance Check

`docs/round` already contains C11 standard v12 files through R3 loop 124, so this output uses R3 loop 125. It avoids the immediately preceding local outputs C05, C01, C13, C15, C10, C02, C16, R13, C17, C07, C06, and C14. All six selected rows are new trigger families for this loop and do not reuse the same symbol + trigger_type + entry_date combination.

## 4. Stock-Web OHLC Input / Price Source Validation

- Manifest: `atlas/manifest.json`
- Schema: `atlas/schema.json`
- Shard root: `atlas/ohlcv_tradable_by_symbol_year`
- Raw shard root: `atlas/ohlcv_raw_by_symbol_year`
- Manifest max date: `2026-02-20`
- Price basis: `tradable_raw`
- Adjustment status: `raw_unadjusted_marcap`

MFE/MAE formula follows Stock-Web schema: MFE is max high over the forward trading-day window divided by entry close minus 1; MAE is min low divided by entry close minus 1. Entry is next tradable close when publication time is after market close or not safely intraday.

## 5. Historical Eligibility Gate

| gate | status | note |
|---|---:|---|
| 180D forward window | pass | all six trigger rows have 180 tradable rows before 2026-02-20 |
| actual 1D OHLC row | pass | entry OHLCV included per trigger |
| canonical trigger labels only | pass | Stage2, Stage2-Actionable, Stage4B, Stage4C only |
| corporate action contamination | pass | known profile corporate-action candidates are outside each 180D window |
| source URL pending | pass | no evidence_url_pending rows |
| duplicate same-entry group | pass | six unique same_entry_group_id values |

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id: BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
round: R3
```

Deep sub-routes compressed into C11:

1. direct customer orderbook + near-term shipment bridge;
2. long-dated JV/capacity headline without current revenue bridge;
3. cathode material supply contract with raw-material/inventory loss;
4. separator contract/MOU with high early MAE;
5. bad battery-material results where 4B watch is correct but hard 4C overblocks recovery.

## 7. Case Selection Summary

| case_id | symbol | company | trigger | entry | type | MFE90 | MAE90 | MFE180 | MAE180 | outcome | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C11-373220-20240725-LGES-RENAULT-LFP-HYUNDAI-JV-GUIDANCE | 373220 | LG에너지솔루션 | 2024-07-25 | 2024-07-26 | Stage2-Actionable | 36.62 | -4.31 | 36.62 | -4.46 | positive | current_profile_correct_with_green_delay_risk |
| C11-006400-20240828-SDI-GM-JV-LONGDATED | 006400 | 삼성SDI | 2024-08-28 | 2024-08-29 | Stage2 | 9.76 | -35.98 | 9.76 | -56.01 | counterexample | current_profile_false_positive_if_actionable |
| C11-051910-20240208-LGCHEM-GM-CATHODE-LONGDATED | 051910 | LG화학 | 2024-02-08 | 2024-02-13 | Stage2 | 10.40 | -25.69 | 10.40 | -44.06 | counterexample | current_profile_false_positive_if_green_or_actionable |
| C11-066970-20240325-LNF-SKON-CATHODE-LOSS-BRIDGE | 066970 | 엘앤에프 | 2024-03-25 | 2024-03-26 | Stage4C | 6.06 | -50.79 | 6.06 | -54.72 | counterexample | current_profile_false_positive_if_orderbook_overcredited |
| C11-361610-20250227-SKIET-GOTION-SEPARATOR-HIGH-MAE | 361610 | SK아이이테크놀로지 | 2025-02-27 | 2025-02-28 | Stage2-Actionable | 4.82 | -31.04 | 25.36 | -31.04 | positive | current_profile_too_early_if_green |
| C11-003670-20250203-POSCOFM-FY24-MARGIN-BREAK-OVERBLOCK | 003670 | 포스코퓨처엠 | 2025-02-03 | 2025-02-04 | Stage4B | 24.48 | -21.20 | 108.00 | -21.20 | positive | current_profile_error_if_hard_4c_without_orderbook_cancellation |


## 8. Positive vs Counterexample Balance

```text
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 3
counterexample_count: 3
4B_case_count: 1
4C_case_count: 1
current_profile_error_count: 5
```

The basket is deliberately balanced: LGES, SKIET, and POSCO Future M prevent the rule from simply killing all battery orderbook cases; Samsung SDI, LG Chem, and L&F show why contract size alone cannot unlock Green.

## 9. Evidence Source Map

| case_id | primary evidence | URL | evidence quality |
|---|---|---|---|
| C11-373220-20240725-LGES-RENAULT-LFP-HYUNDAI-JV-GUIDANCE | LGES Q2 2024 results: Renault/Ampere LFP, Hyundai Indonesia JV shipment, Arizona ESS, guidance cut | https://news.lgensol.com/company-news/press-releases/2678/ | company official |
| C11-006400-20240828-SDI-GM-JV-LONGDATED | Samsung SDI-GM U.S. JV, USD 3.5bn, 27GWh, 2027 mass production | https://news.samsungsdi.com/global/samsung-sdi-and-general-motors-finalize-agreement-to-establish-battery-joint-venture-in-the-u-s/ | company official |
| C11-051910-20240208-LGCHEM-GM-CATHODE-LONGDATED | LG Chem-GM cathode agreement, KRW 25tn, >500k tons, 2026-2035 | https://www.lgchem.com/company/information-center/press-release/news-detail-9274 | company official |
| C11-066970-20240325-LNF-SKON-CATHODE-LOSS-BRIDGE | L&F-SK On cathode supply, KRW 13.19tn, 300k tons, through 2030 | https://en.yna.co.kr/view/AEN20240325003900320 | regulatory-filing-based media |
| C11-361610-20250227-SKIET-GOTION-SEPARATOR-HIGH-MAE | SKIET-Gotion MOU for Europe/North America separator cooperation | https://en.yna.co.kr/view/AEN20250227007800320 | company-press-release-based media |
| C11-003670-20250203-POSCOFM-FY24-MARGIN-BREAK-OVERBLOCK | POSCO Future M 2024 results: revenue down 22.3%, OP down 98%, battery-materials operating loss | https://newsroom.posco.com/en/posco-future-m-announces-2024-financial-results/ | company official |

## 10. Price Data Source Map

| symbol | company | entry_year | price_shard_path | profile_path | corporate_action_window_status |
|---|---|---:|---|---|---|
| 373220 | LG에너지솔루션 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv` | `atlas/symbol_profiles/373/373220.json` | clean_180D_window |
| 006400 | 삼성SDI | 2024 | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv` | `atlas/symbol_profiles/006/006400.json` | clean_180D_window |
| 051910 | LG화학 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv` | `atlas/symbol_profiles/051/051910.json` | clean_180D_window |
| 066970 | 엘앤에프 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv` | `atlas/symbol_profiles/066/066970.json` | clean_180D_window |
| 361610 | SK아이이테크놀로지 | 2025 | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2025.csv` | `atlas/symbol_profiles/361/361610.json` | clean_180D_window |
| 003670 | 포스코퓨처엠 | 2025 | `atlas/ohlcv_tradable_by_symbol_year/003/003670/2025.csv` | `atlas/symbol_profiles/003/003670.json` | clean_180D_window |


## 11. Case-by-Case Trigger Grid

| trigger_id | entry_ohlc | 30D | 90D | 180D | peak/dd |
| --- | --- | --- | --- | --- | --- |
| TRG-C11-373220-20240725-STAGE2A | 2024-07-26 O332000/H334000/L322500/C325000/V165067 | 28.92/-4.31 | 36.62/-4.31 | 36.62/-4.46 | 2024-10-08 444000 / -30.07% |
| TRG-C11-006400-20240828-STAGE2 | 2024-08-29 O339000/H362500/L338000/C358500/V759750 | 9.76/-7.39 | 9.76/-35.98 | 9.76/-56.01 | 2024-09-30 393500 / -59.92% |
| TRG-C11-051910-20240208-STAGE2 | 2024-02-13 O473000/H475000/L469500/C471000/V379733 | 10.40/-8.70 | 10.40/-25.69 | 10.40/-44.06 | 2024-02-19 520000 / -49.33% |
| TRG-C11-066970-20240325-STAGE4C | 2024-03-26 O191600/H194200/L182800/C183100/V909509 | 6.06/-23.21 | 6.06/-50.79 | 6.06/-54.72 | 2024-03-26 194200 / -57.31% |
| TRG-C11-361610-20250227-STAGE2A | 2025-02-28 O28950/H29350/L28000/C28000/V291451 | 4.82/-31.04 | 4.82/-31.04 | 25.36/-31.04 | 2025-10-27 35100 / -23.50% |
| TRG-C11-003670-20250203-STAGE4B | 2025-02-04 O131300/H133600/L124800/C125000/V459939 | 24.48/-1.84 | 24.48/-21.20 | 108.00/-21.20 | 2025-10-27 260000 / -12.69% |


Each `30D`, `90D`, and `180D` cell is `MFE_pct/MAE_pct`.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_open | entry_high | entry_low | entry_close | entry_volume | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|
| TRG-C11-373220-20240725-STAGE2A | 2024-07-26 | 332000 | 334000 | 322500 | 325000 | 165067 | 2024-10-08 | 444000 | -30.07 |
| TRG-C11-006400-20240828-STAGE2 | 2024-08-29 | 339000 | 362500 | 338000 | 358500 | 759750 | 2024-09-30 | 393500 | -59.92 |
| TRG-C11-051910-20240208-STAGE2 | 2024-02-13 | 473000 | 475000 | 469500 | 471000 | 379733 | 2024-02-19 | 520000 | -49.33 |
| TRG-C11-066970-20240325-STAGE4C | 2024-03-26 | 191600 | 194200 | 182800 | 183100 | 909509 | 2024-03-26 | 194200 | -57.31 |
| TRG-C11-361610-20250227-STAGE2A | 2025-02-28 | 28950 | 29350 | 28000 | 28000 | 291451 | 2025-10-27 | 35100 | -23.50 |
| TRG-C11-003670-20250203-STAGE4B | 2025-02-04 | 131300 | 133600 | 124800 | 125000 | 459939 | 2025-10-27 | 260000 | -12.69 |


## 13. Current Calibrated Profile Stress Test

| profile_id | scope | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_count | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| e2r_2_2_rolling_calibrated_proxy | current | 15.36 | -28.17 | 32.70 | -35.25 | 3 | 1 | mixed: orderbook size overcredits long-dated supply, but hard 4C can overblock rebound |
| c11_shadow_gate | canonical_archetype | 15.36 | -28.17 | 32.70 | -35.25 | 2 | 0 | better: Stage2 cap until revenue/margin/utilization bridge appears; 4B not hard 4C for recoverable margin breaks |

## 14. Stage2 / Yellow / Green Comparison

C11 needs a stronger separator between “signed orderbook” and “rerating-quality orderbook.” Stage2 can open on named customer + contract volume/duration, but Stage2-Actionable should require at least two of: near-term shipment, revenue conversion, utilization evidence, margin bridge, customer ramp confirmation, or clean guidance. Green should not unlock from long-dated 2026-2035 supply contracts or 2027 JV capacity alone.

## 15. 4B Local vs Full-window Timing Audit

- LGES 2024-07-25 is a valid positive but peak-to-trough drawdown after the 180D peak was -30.07%, so local 4B watch remains useful even for winners.
- Samsung SDI and LG Chem both peaked early and then suffered deep 180D MAE, showing that long-dated orderbook can be local-peak fuel rather than durable rerating proof.
- L&F is the cleanest false positive: contract size was enormous, but contemporaneous loss/lithium-price pressure made the orderbook a thin roof over a cracked floor.

## 16. 4C Protection Audit

Hard 4C is justified when a big contract is paired with active margin collapse, inventory loss, customer ramp cuts, or contract degradation. However, POSCO Future M shows that weak reported results alone should not always hard-4C the case if customer/orderbook cancellation is absent and a future recovery bridge remains. The proposed rule is not “bad results = death”; it is “bad results + broken orderbook/cash bridge = 4C.”

## 17. Sector-Specific Rule Candidate

For L3 battery/EV/green mobility, orderbook quality must pass through a utilization and margin sluice gate. The contract is the reservoir; revenue and margin are the water actually reaching the turbine. Large announced volumes should be capped at Stage2/watch unless the case has near-term shipment/revenue conversion or a clean profitability bridge.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_rule_candidate: C11_ORDERBOOK_TO_REVENUE_MARGIN_UTILIZATION_BRIDGE_GATE
minimum_for_Stage2: named customer/orderbook + contract duration/volume OR capacity route
minimum_for_Stage2_Actionable: Stage2 + at least two of near-term shipment, revenue conversion, utilization, margin bridge, clean guidance, customer ramp confirmation
minimum_for_Green: Stage2-Actionable + revision/profitability proof + no severe demand/guidance cut
4B_watch: long-dated supply, weak utilization, guidance cut, inventory/lithium loss, or high early MAE
4C: orderbook cancellation/reduction, durable operating loss from core battery material, customer demand ramp collapse, or cash/balance-sheet break
4C_exception: bad reported year without contract cancellation can remain 4B if rebound bridge survives
```

## 19. Before / After Backtest Comparison

| metric | before current-profile proxy | after C11 shadow gate | interpretation |
|---|---:|---:|---|
| calibration_usable_trigger_count | 6 | 6 | no row dropped |
| Stage2-Actionable/Green overcredit rows | 4 | 2 | long-dated JV/supply and loss-dominated contract are capped |
| hard 4C overblock rows | 1 | 0 | POSCOFM stays 4B rather than hard 4C |
| counterexample containment | 3 | 3 | C11 false positives preserved for risk calibration |
| production_scoring_changed | 0 | 0 | shadow-only |

## 20. Score-Return Alignment Matrix

| bucket | cases | price behavior | calibration message |
|---|---|---|---|
| orderbook + shipment bridge | LGES | strong MFE, shallow initial MAE | Stage2-Actionable valid, Green delayed by guidance cut |
| long-dated capacity/supply | Samsung SDI, LG Chem | small early MFE, deep MAE | Stage2 cap; no Green until revenue bridge |
| orderbook + loss bridge | L&F | weak MFE, -50%+ MAE | 4C candidate |
| partnership/MOU + later MFE | SKIET | early -31% MAE, later +25% MFE | drawdown-aware confirmation needed |
| bad results but no cancellation | POSCOFM | huge later MFE after bad print | hard 4C overblock exception |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG | 3 | 3 | 1 | 1 | 6 | 0 | 6 | 6 | 5 | yes | yes | URL/proxy and balance repaired; still need more official filing rows for smaller cathode/separator suppliers |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_required_bridge; local_4b_watch_guard; earlier_thesis_break_watch; hard_4c_confirmation; full_4b_requires_non_price_evidence
residual_error_types_found: long_dated_orderbook_false_positive; orderbook_overcredit_without_margin_bridge; loss_dominated_contract_headline; high_MAE_after_orderbook_positive; hard_4c_overblock_when_bad_results_recover
new_axis_proposed: C11_ORDERBOOK_TO_REVENUE_MARGIN_UTILIZATION_BRIDGE_GATE
existing_axis_strengthened: stage2_required_bridge; local_4b_watch_guard; earlier_thesis_break_watch; hard_4c_confirmation
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L3 battery orderbook requires utilization/margin bridge before Actionable/Green
canonical_archetype_rule_candidate: C11 signed orderbook is Stage2 evidence, not Green evidence, until revenue/margin/utilization conversion appears
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger-level MFE/MAE, entry OHLC row, C11 positive/counterexample split, 4B vs 4C timing, and canonical shadow gate. Non-validated: live candidate ranking, production scoring patch, intraday execution, and post-2026-02-20 price path.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_margin_utilization_gate,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Require current revenue/margin/utilization bridge before Stage2-Actionable or Green","Reduces long-dated orderbook false positives in 006400/051910/066970 while preserving 373220/361610/003670 watch paths","TRG-C11-006400-20240828-STAGE2|TRG-C11-051910-20240208-STAGE2|TRG-C11-066970-20240325-STAGE4C|TRG-C11-373220-20240725-STAGE2A|TRG-C11-361610-20250227-STAGE2A|TRG-C11-003670-20250203-STAGE4B",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_hard_4c_overblock_exception,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Do not hard-4C bad battery-material earnings unless customer/orderbook cancellation or durable cash impairment is present","Preserves POSCOFM rebound path after FY24 margin break","TRG-C11-003670-20250203-STAGE4B",1,1,0,low,canonical_shadow_only,"4B watch rather than hard 4C"
```

Suggested component nudge, shadow-only:

```text
before: contract/backlog/margin/revision/customer/execution/accounting = 24/22/13/10/13/-6/-2
after:  contract/backlog/margin/revision/customer/execution/accounting = 22/20/17/12/13/-10/-3
delta:  -2/-2/+4/+2/0/-4/-1
rationale: reduce contract-size overcredit; increase margin/revenue/utilization bridge; penalize long-dated or loss-dominated orderbook.
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C11-373220-20240725-LGES-RENAULT-LFP-HYUNDAI-JV-GUIDANCE", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "case_type": "structural_success_mixed_guidance", "positive_or_counterexample": "positive", "best_trigger": "TRG-C11-373220-20240725-STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_right_tail_with_guidance_cut; Stage2-Actionable valid but Green should wait for demand/utilization confirmation", "current_profile_verdict": "current_profile_correct_with_green_delay_risk", "price_source": "Songdaiki/stock-web", "notes": "C11 orderbook calibration row; not live candidate research."}
{"row_type": "case", "case_id": "C11-006400-20240828-SDI-GM-JV-LONGDATED", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "case_type": "long_dated_orderbook_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-C11-006400-20240828-STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "long_dated_JV_headline_failed_to_protect; cap at Stage2/watch", "current_profile_verdict": "current_profile_false_positive_if_actionable", "price_source": "Songdaiki/stock-web", "notes": "C11 orderbook calibration row; not live candidate research."}
{"row_type": "case", "case_id": "C11-051910-20240208-LGCHEM-GM-CATHODE-LONGDATED", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "case_type": "long_dated_material_orderbook_without_near_term_margin", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-C11-051910-20240208-STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "contract_size_not_enough_without_current_year_conversion; Stage2 cap", "current_profile_verdict": "current_profile_false_positive_if_green_or_actionable", "price_source": "Songdaiki/stock-web", "notes": "C11 orderbook calibration row; not live candidate research."}
{"row_type": "case", "case_id": "C11-066970-20240325-LNF-SKON-CATHODE-LOSS-BRIDGE", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "case_type": "large_orderbook_overruled_by_margin_inventory_loss", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-C11-066970-20240325-STAGE4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "orderbook_headline_failed_against_loss_and_price_collapse; 4C confirmation path", "current_profile_verdict": "current_profile_false_positive_if_orderbook_overcredited", "price_source": "Songdaiki/stock-web", "notes": "C11 orderbook calibration row; not live candidate research."}
{"row_type": "case", "case_id": "C11-361610-20250227-SKIET-GOTION-SEPARATOR-HIGH-MAE", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "case_type": "orderbook_positive_with_severe_early_drawdown", "positive_or_counterexample": "positive", "best_trigger": "TRG-C11-361610-20250227-STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "late_positive_but_uninvestable_without_drawdown_aware_confirmation", "current_profile_verdict": "current_profile_too_early_if_green", "price_source": "Songdaiki/stock-web", "notes": "C11 orderbook calibration row; not live candidate research."}
{"row_type": "case", "case_id": "C11-003670-20250203-POSCOFM-FY24-MARGIN-BREAK-OVERBLOCK", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "case_type": "margin_break_but_not_hard_4c_overblock_exception", "positive_or_counterexample": "positive", "best_trigger": "TRG-C11-003670-20250203-STAGE4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "4B_watch_needed_but_hard_4C_would_overblock_later_right_tail", "current_profile_verdict": "current_profile_error_if_hard_4c_without_orderbook_cancellation", "price_source": "Songdaiki/stock-web", "notes": "C11 orderbook calibration row; not live candidate research."}
{"row_type": "trigger", "trigger_id": "TRG-C11-373220-20240725-STAGE2A", "case_id": "C11-373220-20240725-LGES-RENAULT-LFP-HYUNDAI-JV-GUIDANCE", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; complete_30_90_180_MFE_MAE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-25", "entry_date": "2024-07-26", "entry_price": 325000.0, "entry_ohlc_1d": {"d": "2024-07-26", "o": 332000.0, "h": 334000.0, "l": 322500.0, "c": 325000.0, "v": 165067.0, "a": 53916369961.0, "mc": 76050000000000.0, "s": 234000000.0, "m": "KOSPI"}, "evidence_available_at_that_date": "Q2 2024 results disclosed Renault/Ampere 39GWh LFP supply agreement, Hyundai Indonesia JV mass production/shipment, Arizona ESS 4.8GWh, while lowering full-year revenue guidance due customer demand ramp adjustment.", "evidence_source": "LG Energy Solution Q2 2024 earnings release / company news", "evidence_url": "https://news.lgensol.com/company-news/press-releases/2678/", "stage2_evidence_fields": ["named_customer_supply_agreement", "JV_mass_production_or_shipment", "ESS_orderbook"], "stage3_evidence_fields": ["near_term_shipment_bridge", "multi_customer_orderbook"], "stage4b_evidence_fields": ["full_year_guidance_cut"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.92, "MFE_90D_pct": 36.62, "MFE_180D_pct": 36.62, "MAE_30D_pct": -4.31, "MAE_90D_pct": -4.31, "MAE_180D_pct": -4.46, "peak_date": "2024-10-08", "peak_price": 444000.0, "drawdown_after_peak_pct": -30.07, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "positive_right_tail_with_guidance_cut; Stage2-Actionable valid but Green should wait for demand/utilization confirmation", "current_profile_verdict": "current_profile_correct_with_green_delay_risk", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "373220|Stage2-Actionable|2024-07-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-C11-006400-20240828-STAGE2", "case_id": "C11-006400-20240828-SDI-GM-JV-LONGDATED", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; complete_30_90_180_MFE_MAE", "trigger_type": "Stage2", "trigger_date": "2024-08-28", "entry_date": "2024-08-29", "entry_price": 358500.0, "entry_ohlc_1d": {"d": "2024-08-29", "o": 339000.0, "h": 362500.0, "l": 338000.0, "c": 358500.0, "v": 759750.0, "a": 269212984500.0, "mc": 24652084005000.0, "s": 68764530.0, "m": "KOSPI"}, "evidence_available_at_that_date": "Samsung SDI and GM finalized U.S. JV terms: USD 3.5bn investment, 27GWh initial capacity expandable to 36GWh, 2027 mass production, NCA prismatic batteries.", "evidence_source": "Samsung SDI official release", "evidence_url": "https://news.samsungsdi.com/global/samsung-sdi-and-general-motors-finalize-agreement-to-establish-battery-joint-venture-in-the-u-s/", "stage2_evidence_fields": ["named_customer_JV", "capacity_plan"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["2027_mass_production_long_dated", "no_current_revenue_bridge"], "stage4c_evidence_fields": ["deep_180D_MAE_after_limited_MFE"], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.76, "MFE_90D_pct": 9.76, "MFE_180D_pct": 9.76, "MAE_30D_pct": -7.39, "MAE_90D_pct": -35.98, "MAE_180D_pct": -56.01, "peak_date": "2024-09-30", "peak_price": 393500.0, "drawdown_after_peak_pct": -59.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "long_dated_JV_headline_failed_to_protect; cap at Stage2/watch", "current_profile_verdict": "current_profile_false_positive_if_actionable", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "006400|Stage2|2024-08-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-C11-051910-20240208-STAGE2", "case_id": "C11-051910-20240208-LGCHEM-GM-CATHODE-LONGDATED", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; complete_30_90_180_MFE_MAE", "trigger_type": "Stage2", "trigger_date": "2024-02-08", "entry_date": "2024-02-13", "entry_price": 471000.0, "entry_ohlc_1d": {"d": "2024-02-13", "o": 473000.0, "h": 475000.0, "l": 469500.0, "c": 471000.0, "v": 379733.0, "a": 179071633073.0, "mc": 33248993553000.0, "s": 70592343.0, "m": "KOSPI"}, "evidence_available_at_that_date": "LG Chem announced a KRW 25tn GM cathode-material supply deal for more than 500k tons from 2026 to 2035, linked to Tennessee localization and IRA supply-chain needs.", "evidence_source": "LG Chem official press release", "evidence_url": "https://www.lgchem.com/company/information-center/press-release/news-detail-9274", "stage2_evidence_fields": ["named_customer_supply_agreement", "contract_value_and_volume", "localization_IRA_bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["supply_starts_2026", "no_current_margin_bridge"], "stage4c_evidence_fields": ["large_MAE_after_short_MFE"], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv", "profile_path": "atlas/symbol_profiles/051/051910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.4, "MFE_90D_pct": 10.4, "MFE_180D_pct": 10.4, "MAE_30D_pct": -8.7, "MAE_90D_pct": -25.69, "MAE_180D_pct": -44.06, "peak_date": "2024-02-19", "peak_price": 520000.0, "drawdown_after_peak_pct": -49.33, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "contract_size_not_enough_without_current_year_conversion; Stage2 cap", "current_profile_verdict": "current_profile_false_positive_if_green_or_actionable", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "051910|Stage2|2024-02-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-C11-066970-20240325-STAGE4C", "case_id": "C11-066970-20240325-LNF-SKON-CATHODE-LOSS-BRIDGE", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; complete_30_90_180_MFE_MAE", "trigger_type": "Stage4C", "trigger_date": "2024-03-25", "entry_date": "2024-03-26", "entry_price": 183100.0, "entry_ohlc_1d": {"d": "2024-03-26", "o": 191600.0, "h": 194200.0, "l": 182800.0, "c": 183100.0, "v": 909509.0, "a": 171228023800.0, "mc": 6638472318300.0, "s": 36255993.0, "m": "KOSPI"}, "evidence_available_at_that_date": "L&F disclosed a KRW 13.19tn high-nickel cathode deal with SK On through 2030; contemporaneous reporting also noted an annual operating loss caused by lithium-price decline.", "evidence_source": "Yonhap / Korea JoongAng Daily based on regulatory filing", "evidence_url": "https://en.yna.co.kr/view/AEN20240325003900320", "stage2_evidence_fields": ["named_customer_supply_agreement", "contract_value_and_volume"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["inventory_price_loss_warning", "market_reaction_failed"], "stage4c_evidence_fields": ["operating_loss_bridge", "MAE_180D_above_50pct"], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.06, "MFE_90D_pct": 6.06, "MFE_180D_pct": 6.06, "MAE_30D_pct": -23.21, "MAE_90D_pct": -50.79, "MAE_180D_pct": -54.72, "peak_date": "2024-03-26", "peak_price": 194200.0, "drawdown_after_peak_pct": -57.31, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "orderbook_headline_failed_against_loss_and_price_collapse; 4C confirmation path", "current_profile_verdict": "current_profile_false_positive_if_orderbook_overcredited", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "066970|Stage4C|2024-03-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-C11-361610-20250227-STAGE2A", "case_id": "C11-361610-20250227-SKIET-GOTION-SEPARATOR-HIGH-MAE", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; complete_30_90_180_MFE_MAE", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-27", "entry_date": "2025-02-28", "entry_price": 28000.0, "entry_ohlc_1d": {"d": "2025-02-28", "o": 28950.0, "h": 29350.0, "l": 28000.0, "c": 28000.0, "v": 291451.0, "a": 8307364350.0, "mc": 1996332576000.0, "s": 71297592.0, "m": "KOSPI"}, "evidence_available_at_that_date": "SKIET signed an initial pact with Gotion for Europe/North America separator supply and planned to provide separators to Gotion plants in Slovakia and Illinois; this followed a mid/long-term LFP separator contract.", "evidence_source": "Yonhap / ChosunBiz event reporting", "evidence_url": "https://en.yna.co.kr/view/AEN20250227007800320", "stage2_evidence_fields": ["named_customer_partnership", "separator_supply_scope", "technical_or_geographic_route"], "stage3_evidence_fields": ["late_180D_positive_MFE"], "stage4b_evidence_fields": ["MOU_not_fixed_contract_for_all_scope", "early_30D_MAE_above_30pct"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2025.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.82, "MFE_90D_pct": 4.82, "MFE_180D_pct": 25.36, "MAE_30D_pct": -31.04, "MAE_90D_pct": -31.04, "MAE_180D_pct": -31.04, "peak_date": "2025-10-27", "peak_price": 35100.0, "drawdown_after_peak_pct": -23.5, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "late_positive_but_uninvestable_without_drawdown_aware_confirmation", "current_profile_verdict": "current_profile_too_early_if_green", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "361610|Stage2-Actionable|2025-02-28", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-C11-003670-20250203-STAGE4B", "case_id": "C11-003670-20250203-POSCOFM-FY24-MARGIN-BREAK-OVERBLOCK", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_REVENUE_MARGIN_UTILIZATION_BRIDGE_VS_LONG_DATED_BACKLOG", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; complete_30_90_180_MFE_MAE", "trigger_type": "Stage4B", "trigger_date": "2025-02-03", "entry_date": "2025-02-04", "entry_price": 125000.0, "entry_ohlc_1d": {"d": "2025-02-04", "o": 131300.0, "h": 133600.0, "l": 124800.0, "c": 125000.0, "v": 459939.0, "a": 59032337900.0, "mc": 9682902500000.0, "s": 77463220.0, "m": "KOSPI"}, "evidence_available_at_that_date": "POSCO Future M announced 2024 revenue KRW 3.6999tn, operating profit KRW 0.7bn, revenue down 22.3%, operating profit down 98%, battery materials operating loss KRW 36.9bn, but with high-nickel volume and post-chasm recovery plan.", "evidence_source": "POSCO Group Newsroom official release", "evidence_url": "https://newsroom.posco.com/en/posco-future-m-announces-2024-financial-results/", "stage2_evidence_fields": ["high_nickel_sales_volume_reference", "future_product_pipeline"], "stage3_evidence_fields": ["post_chasm_recovery_plan"], "stage4b_evidence_fields": ["OP_down_98pct", "battery_materials_operating_loss", "inventory_valuation_loss"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2025.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.48, "MFE_90D_pct": 24.48, "MFE_180D_pct": 108.0, "MAE_30D_pct": -1.84, "MAE_90D_pct": -21.2, "MAE_180D_pct": -21.2, "peak_date": "2025-10-27", "peak_price": 260000.0, "drawdown_after_peak_pct": -12.69, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "4B_watch_needed_but_hard_4C_would_overblock_later_right_tail", "current_profile_verdict": "current_profile_error_if_hard_4c_without_orderbook_cancellation", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "003670|Stage4B|2025-02-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C11-373220-20240725-LGES-RENAULT-LFP-HYUNDAI-JV-GUIDANCE", "trigger_id": "TRG-C11-373220-20240725-STAGE2A", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 22, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 22, "backlog_visibility_score": 18, "margin_bridge_score": 14, "revision_score": 10, "relative_strength_score": 6, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 4, "execution_risk_score": -6, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C11 adjustment separates named orderbook from current revenue/margin/utilization conversion and penalizes long-dated or loss-dominated orderbook.", "MFE_90D_pct": 36.62, "MAE_90D_pct": -4.31, "score_return_alignment_label": "positive_right_tail_with_guidance_cut; Stage2-Actionable valid but Green should wait for demand/utilization confirmation", "current_profile_verdict": "current_profile_correct_with_green_delay_risk"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C11-006400-20240828-SDI-GM-JV-LONGDATED", "trigger_id": "TRG-C11-006400-20240828-STAGE2", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 22, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 22, "backlog_visibility_score": 18, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 4, "execution_risk_score": -12, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C11 adjustment separates named orderbook from current revenue/margin/utilization conversion and penalizes long-dated or loss-dominated orderbook.", "MFE_90D_pct": 9.76, "MAE_90D_pct": -35.98, "score_return_alignment_label": "long_dated_JV_headline_failed_to_protect; cap at Stage2/watch", "current_profile_verdict": "current_profile_false_positive_if_actionable"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C11-051910-20240208-LGCHEM-GM-CATHODE-LONGDATED", "trigger_id": "TRG-C11-051910-20240208-STAGE2", "symbol": "051910", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 22, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 22, "backlog_visibility_score": 18, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 4, "execution_risk_score": -12, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 67, "stage_label_after": "Stage2", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C11 adjustment separates named orderbook from current revenue/margin/utilization conversion and penalizes long-dated or loss-dominated orderbook.", "MFE_90D_pct": 10.4, "MAE_90D_pct": -25.69, "score_return_alignment_label": "contract_size_not_enough_without_current_year_conversion; Stage2 cap", "current_profile_verdict": "current_profile_false_positive_if_green_or_actionable"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C11-066970-20240325-LNF-SKON-CATHODE-LOSS-BRIDGE", "trigger_id": "TRG-C11-066970-20240325-STAGE4C", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 22, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 22, "backlog_visibility_score": 18, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 4, "execution_risk_score": -12, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -2}, "weighted_score_after": 58, "stage_label_after": "Stage4C", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C11 adjustment separates named orderbook from current revenue/margin/utilization conversion and penalizes long-dated or loss-dominated orderbook.", "MFE_90D_pct": 6.06, "MAE_90D_pct": -50.79, "score_return_alignment_label": "orderbook_headline_failed_against_loss_and_price_collapse; 4C confirmation path", "current_profile_verdict": "current_profile_false_positive_if_orderbook_overcredited"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C11-361610-20250227-SKIET-GOTION-SEPARATOR-HIGH-MAE", "trigger_id": "TRG-C11-361610-20250227-STAGE2A", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 22, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 22, "backlog_visibility_score": 18, "margin_bridge_score": 14, "revision_score": 10, "relative_strength_score": 6, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 4, "execution_risk_score": -6, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage2", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C11 adjustment separates named orderbook from current revenue/margin/utilization conversion and penalizes long-dated or loss-dominated orderbook.", "MFE_90D_pct": 4.82, "MAE_90D_pct": -31.04, "score_return_alignment_label": "late_positive_but_uninvestable_without_drawdown_aware_confirmation", "current_profile_verdict": "current_profile_too_early_if_green"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C11-003670-20250203-POSCOFM-FY24-MARGIN-BREAK-OVERBLOCK", "trigger_id": "TRG-C11-003670-20250203-STAGE4B", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 22, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 62, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 22, "backlog_visibility_score": 18, "margin_bridge_score": 14, "revision_score": 10, "relative_strength_score": 6, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 4, "execution_risk_score": -6, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -2}, "weighted_score_after": 66, "stage_label_after": "Stage4B", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C11 adjustment separates named orderbook from current revenue/margin/utilization conversion and penalizes long-dated or loss-dominated orderbook.", "MFE_90D_pct": 24.48, "MAE_90D_pct": -21.2, "score_return_alignment_label": "4B_watch_needed_but_hard_4C_would_overblock_later_right_tail", "current_profile_verdict": "current_profile_error_if_hard_4c_without_orderbook_cancellation"}
{"row_type": "residual_contribution", "round": "R3", "loop": "125", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 6, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "earlier_thesis_break_watch", "hard_4c_confirmation", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["long_dated_orderbook_false_positive", "orderbook_overcredit_without_margin_bridge", "loss_dominated_contract_headline", "4C_overblock_when_bad_results_recover", "high_MAE_after_orderbook_positive"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied `e2r_2_2_rolling_calibrated` profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Deduplicate same_entry_group_id and reused cases.
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

```yaml
completed_state: true
completed_round: R3
completed_loop: 125
completed_large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
completed_canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selected_priority_bucket: Priority 0/1 quality repair — C11 orderbook headline vs revenue/margin/utilization bridge
next_recommended_archetypes:
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

## 28. Source Notes

- Stock-Web rows are raw/unadjusted FinanceData/marcap rows, so this MD treats corporate-action candidate windows as blocked if they overlap the measured window.
- This is a historical calibration artifact only. It is not investment advice and not a live signal.
- Evidence timing is conservative: after-close or unknown publication timing uses the next tradable entry date.
