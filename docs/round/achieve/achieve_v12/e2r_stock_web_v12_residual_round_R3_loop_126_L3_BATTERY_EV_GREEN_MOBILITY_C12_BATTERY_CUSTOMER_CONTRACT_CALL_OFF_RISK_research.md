# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
selected_round: R3
selected_loop: 126
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C12 customer call-off / inventory-adjustment risk split; direct URL/proxy repair; 4B vs hard 4C balance
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE
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

Assumed active profile is `e2r_2_2_rolling_calibrated` with already-applied global axes: `stage2_required_bridge`, `local_4b_watch_guard`, `earlier_thesis_break_watch`, `hard_4c_confirmation`, `price_only_blowoff_blocks_positive_stage`, and `full_4b_requires_non_price_evidence`. This loop does not propose a production global change. It proposes a C12 canonical shadow gate.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R3`
- Large sector: `L3_BATTERY_EV_GREEN_MOBILITY`
- Canonical: `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`
- Fine: `CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE`

Scope question: when is battery customer weakness a true call-off / cancellation / utilization break that deserves hard 4C, and when is it only an inventory-adjustment storm that should stay in Stage4B watch until the contract/revenue bridge is visibly broken?

## 3. Previous Coverage / Duplicate Avoidance Check

`docs/round` already contains recent local outputs for C05, C01, C13, C15, C10, C02, C16, R13, C17, C07, C06, C14, and C11. This output therefore selects C12. All six selected rows use fresh trigger families for this loop and avoid reusing the same symbol + trigger_type + entry_date combination from the immediately preceding local run set.

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
| canonical trigger labels only | pass | Stage4B and Stage4C only |
| corporate action contamination | pass | known profile corporate-action candidates are outside each 180D window |
| source URL pending | pass | no evidence_url_pending rows |
| duplicate same-entry group | pass | six unique same_entry_group_id values |

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id: CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
round: R3
```

Deep sub-routes compressed into C12:

1. customer inventory adjustment with no contract cancellation;
2. actual utilization collapse from downstream customer call-off;
3. cathode inventory valuation loss from raw-material ASP decline;
4. separator shipment collapse and fixed-cost leverage break;
5. recoverable battery material loss where hard 4C overblocks a later right-tail rebound.

## 7. Case Selection Summary

| case_id | symbol | company | trigger | entry | type | MFE90 | MAE90 | MFE180 | MAE180 | outcome | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C12-373220-20240725-LGES-SALES-TARGET-CUT | 373220 | LG에너지솔루션 | 2024-07-25 | 2024-07-26 | Stage4B | 36.62 | -4.31 | 36.62 | -4.46 | counterexample_to_hard_4c | hard_4c_overblock_if_no_customer_cancellation |
| C12-006400-20250124-SDI-MAJOR-CUSTOMER-INVENTORY | 006400 | 삼성SDI | 2025-01-24 | 2025-01-31 | Stage4B | 11.94 | -28.96 | 37.16 | -28.96 | counterexample_to_hard_4c | watch_not_death_when_customer_adjustment_is_segment_specific |
| C12-066970-20240509-LNF-INVENTORY-VALUATION-LOSS | 066970 | 엘앤에프 | 2024-05-09 | 2024-05-10 | Stage4C | 15.46 | -45.92 | 15.46 | -49.97 | risk_positive_4c_correct | hard_4c_or_strict_cap_correct_when_loss_and_inventory_break_dominate |
| C12-361610-20240430-SKIET-DOWNSTREAM-INVENTORY | 361610 | SK아이이테크놀로지 | 2024-04-30 | 2024-05-02 | Stage4C | 2.21 | -48.98 | 2.21 | -62.90 | risk_positive_4c_correct | hard_4c_correct_when_downstream_inventory_adjustment_breaks_utilization_and_margin |
| C12-020150-20250124-LOTTE-CUSTOMER-INVENTORY | 020150 | 롯데에너지머티리얼즈 | 2025-01-24 | 2025-01-31 | Stage4B | 42.76 | -11.95 | 42.76 | -11.95 | counterexample_to_hard_4c | stage4b_watch_correct_hard_4c_overblocks_when_sales_and_balance_sheet_survive |
| C12-247540-20250211-ECOPROBM-FY24-LOSS-REBOUND | 247540 | 에코프로비엠 | 2025-02-11 | 2025-02-12 | Stage4B | 16.91 | -33.09 | 48.51 | -33.09 | counterexample_to_hard_4c_with_high_mae | drawdown_aware_4b_needed_hard_4c_only_if_customer_cancellation_or_cash_break |

## 8. Positive vs Counterexample Balance

```text
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 2
counterexample_count: 4
4B_case_count: 4
4C_case_count: 2
source_proxy_only_count: 3
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 6
```

The basket is intentionally asymmetric: L&F and SKIET are risk-positive rows where 4C or strict cap protected the profile; LGES, Samsung SDI, Lotte Energy Materials, and EcoPro BM prevent a crude rule from killing every battery customer-inventory warning.

## 9. Evidence Source Map

| case_id | primary evidence | URL | evidence quality |
| --- | --- | --- | --- |
| C12-373220-20240725-LGES-SALES-TARGET-CUT | Reuters, LGES cuts sales target on weak EV demand, 2024-07-25 | https://www.reuters.com/technology/battery-firm-lg-energy-solution-q2-profit-plunges-weak-ev-demand-2024-07-25/ | major-wire + company-linked disclosure; not proxy-only for demand/capacity thesis |
| C12-006400-20250124-SDI-MAJOR-CUSTOMER-INVENTORY | Samsung SDI 2024 Q4/final annual results, 2025-01-24 | https://samsungsdi.com/sdi-now/sdi-news/4221.html | company official |
| C12-066970-20240509-LNF-INVENTORY-VALUATION-LOSS | Asia Business Daily, L&F Q1 results, 2024-05-09 | https://www.asiae.co.kr/en/article/2024050915570493698 | earnings-news proxy with company statement; proxy-only for direct filing |
| C12-361610-20240430-SKIET-DOWNSTREAM-INVENTORY | Mirae Asset report, SK IE Technology, 2024-04-30; Reuters SKIET sale consideration, 2024-05-15 | https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220 | broker research proxy + Reuters risk confirmation |
| C12-020150-20250124-LOTTE-CUSTOMER-INVENTORY | Lotte Energy Materials preliminary 2024 results, 2025-01-24 | https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128 | company official |
| C12-247540-20250211-ECOPROBM-FY24-LOSS-REBOUND | Asia Business Daily EcoPro Q3 loss / Pulse EcoPro BM FY24 loss | https://www.asiae.co.kr/en/article/2024110110191994466 | earnings-news proxy; direct company overview used only for business mapping |

## 10. Price Data Source Map

| symbol | company | entry_year | price_shard_path | profile_path | corporate_action_window_status |
| --- | --- | --- | --- | --- | --- |
| 373220 | LG에너지솔루션 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv` | `atlas/symbol_profiles/373/373220.json` | clean_180D_window |
| 006400 | 삼성SDI | 2025 | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv` | `atlas/symbol_profiles/006/006400.json` | clean_180D_window |
| 066970 | 엘앤에프 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv` | `atlas/symbol_profiles/066/066970.json` | clean_180D_window |
| 361610 | SK아이이테크놀로지 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv` | `atlas/symbol_profiles/361/361610.json` | clean_180D_window |
| 020150 | 롯데에너지머티리얼즈 | 2025 | `atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv` | `atlas/symbol_profiles/020/020150.json` | clean_180D_window |
| 247540 | 에코프로비엠 | 2025 | `atlas/ohlcv_tradable_by_symbol_year/247/247540/2025.csv` | `atlas/symbol_profiles/247/247540.json` | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | entry_ohlc | 30D | 90D | 180D | peak/dd |
| --- | --- | --- | --- | --- | --- |
| TRG-C12-373220-20240725-STAGE4B | 2024-07-26 O332000/H334000/L322500/C325000/V165067 | 28.92/-4.31 | 36.62/-4.31 | 36.62/-4.46 | 2024-10-08 444000 / -30.07% |
| TRG-C12-006400-20250124-STAGE4B | 2025-01-31 O225500/H226000/L220000/C222000/V403390 | 11.94/-14.73 | 11.94/-28.96 | 37.16/-28.96 | 2025-10-27 304500 / -7.39% |
| TRG-C12-066970-20240509-STAGE4C | 2024-05-10 O152400/H161400/L152400/C153300/V333198 | 15.46/-4.70 | 15.46/-45.92 | 15.46/-49.97 | 2024-06-13 177000 / -56.67% |
| TRG-C12-361610-20240430-STAGE4C | 2024-05-02 O58700/H59600/L58600/C58900/V131477 | 2.21/-27.50 | 2.21/-48.98 | 2.21/-62.90 | 2024-05-03 60200 / -63.70% |
| TRG-C12-020150-20250124-STAGE4B | 2025-01-31 O22900/H23000/L22100/C22100/V113593 | 42.76/-8.37 | 42.76/-11.95 | 42.76/-11.95 | 2025-02-20 31550 / -38.32% |
| TRG-C12-247540-20250211-STAGE4B | 2025-02-12 O120600/H123500/L118500/C121200/V572381 | 16.91/-11.39 | 16.91/-33.09 | 48.51/-33.09 | 2025-10-27 180000 / -16.39% |

Each `30D`, `90D`, and `180D` cell is `MFE_pct/MAE_pct`.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_open | entry_high | entry_low | entry_close | entry_volume | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRG-C12-373220-20240725-STAGE4B | 2024-07-26 | 332000 | 334000 | 322500 | 325000 | 165067 | 2024-10-08 | 444000 | -30.07 |
| TRG-C12-006400-20250124-STAGE4B | 2025-01-31 | 225500 | 226000 | 220000 | 222000 | 403390 | 2025-10-27 | 304500 | -7.39 |
| TRG-C12-066970-20240509-STAGE4C | 2024-05-10 | 152400 | 161400 | 152400 | 153300 | 333198 | 2024-06-13 | 177000 | -56.67 |
| TRG-C12-361610-20240430-STAGE4C | 2024-05-02 | 58700 | 59600 | 58600 | 58900 | 131477 | 2024-05-03 | 60200 | -63.70 |
| TRG-C12-020150-20250124-STAGE4B | 2025-01-31 | 22900 | 23000 | 22100 | 22100 | 113593 | 2025-02-20 | 31550 | -38.32 |
| TRG-C12-247540-20250211-STAGE4B | 2025-02-12 | 120600 | 123500 | 118500 | 121200 | 572381 | 2025-10-27 | 180000 | -16.39 |

## 13. Current Calibrated Profile Stress Test

| profile_id | scope | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_count | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| e2r_2_2_rolling_calibrated_proxy | current | 20.98 | -28.87 | 30.45 | -31.89 | 2 | 4 | mixed: hard 4C can overblock recoverable inventory-adjustment prints, but Stage2 overcredits customer weakness when utilization/margin breaks are visible |
| c12_shadow_gate | canonical_archetype | 20.98 | -28.87 | 30.45 | -31.89 | 1 | 1 | better: hard 4C requires cancellation/utilization/cash break; recoverable inventory adjustment stays 4B watch |

## 14. Stage2 / Yellow / Green Comparison

C12 should rarely create positive Stage2 by itself. Customer weakness is negative evidence unless the company simultaneously shows offsetting order durability, ESS/North-America mix, cost reduction, balance-sheet resilience, or explicit recovery guidance. Stage2/Stage3 promotion should therefore require the risk event to be absorbed by a visible revenue/margin bridge. Otherwise, C12 rows are mostly Stage4B/Stage4C overlays.

## 15. 4B Local vs Full-window Timing Audit

- LGES and Lotte Energy Materials show that demand warnings can create early fear but still produce strong 30D/90D MFE if the market sees survivable contracts or policy/localization offsets.
- Samsung SDI and EcoPro BM show large MAE and later MFE, so Green must be drawdown-aware; the first job of the gate is not to buy the rebound but to avoid killing the name mechanically.
- L&F and SKIET show the other side: customer/inventory weakness can become a true cash/margin break. Once utilization and inventory losses dominate the bridge, hard 4C or strict Stage2 cap is correct.

## 16. 4C Protection Audit

Hard 4C is justified when at least two of these are present: named customer call-off/cancellation, utilization collapse, recurring operating loss from the affected battery line, inventory valuation loss large enough to break cash/margin bridge, weakening balance sheet, or management guidance that reduces production/capex due to demand. It is not justified by a single phrase like “customer inventory adjustment” if sales diversification, contract survival, ESS mix, balance sheet, or cost bridge remains alive.

## 17. Sector-Specific Rule Candidate

For L3 battery/EV/green mobility, customer weakness must pass through a contract-integrity sluice gate. The headline is the storm cloud; the calibration evidence is whether the factory still has customer-bound water flowing through the turbine. Stage4B should catch the storm; hard 4C should wait for the pipe to crack.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_rule_candidate: C12_CUSTOMER_CALLOFF_CONTRACT_RISK_GATE
minimum_for_Stage4B: customer inventory adjustment, demand slowdown, guidance cut, utilization warning, or inventory valuation loss
minimum_for_Stage4C: Stage4B + at least two of named customer call-off/cancellation, utilization collapse, recurring operating loss, inventory valuation loss, cash/balance-sheet break, or capacity/capex cancellation
hard_4c_exception: customer inventory adjustment without contract cancellation can remain 4B if offsetting demand segment, customer diversification, ESS/mix bridge, balance-sheet resilience, or explicit recovery path survives
stage2_positive_exception: risk event absorbed by current-year revenue/margin/utilization bridge and clean guidance, not merely lower stock price
```

## 19. Before / After Backtest Comparison

| metric | before current-profile proxy | after C12 shadow gate | interpretation |
|---|---:|---:|---|
| calibration_usable_trigger_count | 6 | 6 | no row dropped |
| hard 4C overblock rows | 4 | 1 | LGES/Samsung SDI/Lotte/EcoPro BM stay 4B watch unless cancellation/cash break appears |
| Stage2 false-positive risk rows | 2 | 0 | L&F and SKIET are capped or routed to 4C |
| counterexample containment | 4 | 4 | overblock exceptions preserved for rule calibration |
| production_scoring_changed | 0 | 0 | shadow-only |

## 20. Score-Return Alignment Matrix

| bucket | cases | price behavior | calibration message |
|---|---|---|---|
| demand warning but recoverable contract/mix | LGES, Lotte Energy Materials | strong MFE, modest-to-moderate MAE | 4B watch, not hard 4C |
| customer adjustment with later right tail but painful MAE | Samsung SDI, EcoPro BM | deep interim MAE, later recovery | drawdown-aware confirmation; hard 4C only with cancellation/cash break |
| margin/inventory break dominates contract story | L&F | small MFE, deep 90D/180D MAE | strict cap or hard 4C correct |
| utilization collapse from downstream customer inventory | SKIET | very weak MFE, severe 30D/90D/180D MAE | hard 4C correct when fixed-cost leverage breaks |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE | 2 | 4 | 4 | 2 | 6 | 0 | 6 | 6 | 6 | yes | yes | URL/proxy and C12 hard-4C/4B balance repaired; still need more direct filing rows for smaller material suppliers |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_required_bridge; local_4b_watch_guard; earlier_thesis_break_watch; hard_4c_confirmation; drawdown_aware_confirmation
residual_error_types_found: customer_inventory_adjustment_hard_4c_overblock; calloff_risk_false_positive_without_margin_bridge; proxy_only_customer_demand_evidence; deep_MAE_after_recoverable_battery_loss
new_axis_proposed: C12_CUSTOMER_CALLOFF_CONTRACT_RISK_GATE
existing_axis_strengthened: stage2_required_bridge; local_4b_watch_guard; earlier_thesis_break_watch; hard_4c_confirmation; drawdown_aware_confirmation
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L3 customer weakness requires contract-integrity and utilization/margin confirmation before hard 4C
canonical_archetype_rule_candidate: C12 inventory adjustment is 4B evidence; hard 4C requires call-off/cancellation/utilization/cash break confirmation
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger-level MFE/MAE, entry OHLC row, C12 4B/4C split, customer-calloff versus inventory-adjustment distinction, and canonical shadow gate. Non-validated: live candidate ranking, production scoring patch, intraday execution, and post-2026-02-20 price path.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C12_customer_calloff_contract_risk_gate,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"Require direct customer call-off/cancellation/utilization/margin evidence before hard 4C","Contains L&F/SKIET false positives while preserving recoverable LGES/SDI/Lotte/EcoPro BM 4B paths","TRG-C12-373220-20240725-STAGE4B|TRG-C12-006400-20250124-STAGE4B|TRG-C12-066970-20240509-STAGE4C|TRG-C12-361610-20240430-STAGE4C|TRG-C12-020150-20250124-STAGE4B|TRG-C12-247540-20250211-STAGE4B",6,6,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C12_inventory_adjustment_4b_over_4c_exception,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"Customer inventory adjustment alone is not a thesis break if contract durability and offsetting segment bridge remain","Reduces hard-4C overblock rows in 373220/006400/020150/247540","TRG-C12-373220-20240725-STAGE4B|TRG-C12-006400-20250124-STAGE4B|TRG-C12-020150-20250124-STAGE4B|TRG-C12-247540-20250211-STAGE4B",4,4,4,medium,canonical_shadow_only,"4B watch rather than hard 4C"
```

Suggested component nudge, shadow-only:

```text
before: EPS/Vis/Bott/Mis/Val/Cap/Info = 20/18/14/10/10/8/20
after:  EPS/Vis/Bott/Mis/Val/Cap/Info = 18/16/12/9/8/8/29
delta:  -2/-2/-2/-1/-2/0/+9
rationale: reduce generic battery contract/demand overcredit; increase information-confidence and risk-gate emphasis for customer call-off, utilization, inventory, and cash break evidence.
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C12-373220-20240725-LGES-SALES-TARGET-CUT", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "case_type": "customer_demand_slowdown_guidance_cut_rebound_exception", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-C12-373220-20240725-STAGE4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_overblock_if_no_customer_cancellation", "current_profile_verdict": "hard_4c_overblock_if_no_customer_cancellation", "price_source": "Songdaiki/stock-web", "notes": "C12 customer contract/call-off risk calibration row; not live candidate research."}
{"row_type": "trigger", "trigger_id": "TRG-C12-373220-20240725-STAGE4B", "case_id": "C12-373220-20240725-LGES-SALES-TARGET-CUT", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "trigger_type": "Stage4B", "trigger_date": "2024-07-25", "entry_date": "2024-07-26", "entry_price": 325000.0, "entry_open": 332000.0, "entry_high": 334000.0, "entry_low": 322500.0, "entry_close": 325000.0, "entry_volume": 165067.0, "entry_amount": 53916369961.0, "entry_marcap": 76050000000000.0, "market": "KOSPI", "MFE_30D_pct": 28.9231, "MAE_30D_pct": -4.3077, "MFE_90D_pct": 36.6154, "MAE_90D_pct": -4.3077, "MFE_180D_pct": 36.6154, "MAE_180D_pct": -4.4615, "peak_30D_date": "2024-09-03", "peak_30D_high": 419000.0, "trough_30D_date": "2024-08-05", "trough_30D_low": 311000.0, "peak_90D_date": "2024-10-08", "peak_90D_high": 444000.0, "trough_90D_date": "2024-08-05", "trough_90D_low": 311000.0, "peak_180D_date": "2024-10-08", "peak_180D_high": 444000.0, "trough_180D_date": "2025-04-03", "trough_180D_low": 310500.0, "drawdown_after_peak_180D_pct": -30.0676, "drawdown_after_peak_180D_trough_date": "2025-04-03", "forward_180D_last_date": "2025-04-24", "window_30D_available": true, "window_90D_available": true, "window_180D_available": true, "window_180D_corporate_action_contaminated": false, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "same_entry_group_id": "373220-2024-07-26-Stage4B-C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "dedupe_representative": true, "calibration_usable": true, "evidence_url": "https://www.reuters.com/technology/battery-firm-lg-energy-solution-q2-profit-plunges-weak-ev-demand-2024-07-25/", "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "Reuters reported a 2024 revenue target cut, slower EV demand, lower IRA-credit volume estimate, capacity-expansion adjustment, and no-IRA operating loss; price later rebounded sharply, so this is 4B/watch rather than hard 4C unless contract cancellation appears.", "score_return_alignment_label": "hard_4c_overblock_if_no_customer_cancellation", "current_profile_verdict": "hard_4c_overblock_if_no_customer_cancellation"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C12-373220-20240725-LGES-SALES-TARGET-CUT", "trigger_id": "TRG-C12-373220-20240725-STAGE4B", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"EPS_FCF": 12, "visibility": 14, "bottleneck_pricing": 8, "mispricing": 10, "valuation": 8, "capital_allocation": 8, "information_confidence": 20, "risk_penalty": -22}, "weighted_score_before": 58, "stage_label_before": "Stage4C", "raw_component_scores_after": {"EPS_FCF": 14, "visibility": 16, "bottleneck_pricing": 8, "mispricing": 10, "valuation": 8, "capital_allocation": 8, "information_confidence": 20, "risk_penalty": -18}, "weighted_score_after": 66, "stage_label_after": "Stage4B", "changed_components": ["visibility", "EPS_FCF", "information_confidence", "risk_penalty"], "component_delta_explanation": "C12 gate separates temporary customer inventory adjustment from actual call-off/cancellation/cash break and requires evidence-quality confirmation before hard 4C.", "MFE_90D_pct": 36.62, "MAE_90D_pct": -4.31, "MFE_180D_pct": 36.62, "MAE_180D_pct": -4.46, "score_return_alignment_label": "hard_4c_overblock_if_no_customer_cancellation", "current_profile_verdict": "hard_4c_overblock_if_no_customer_cancellation"}
{"row_type": "case", "case_id": "C12-006400-20250124-SDI-MAJOR-CUSTOMER-INVENTORY", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "case_type": "major_customer_inventory_adjustment_with_ESS_JV_offset", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-C12-006400-20250124-STAGE4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "watch_not_death_when_customer_adjustment_is_segment_specific", "current_profile_verdict": "watch_not_death_when_customer_adjustment_is_segment_specific", "price_source": "Songdaiki/stock-web", "notes": "C12 customer contract/call-off risk calibration row; not live candidate research."}
{"row_type": "trigger", "trigger_id": "TRG-C12-006400-20250124-STAGE4B", "case_id": "C12-006400-20250124-SDI-MAJOR-CUSTOMER-INVENTORY", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "trigger_type": "Stage4B", "trigger_date": "2025-01-24", "entry_date": "2025-01-31", "entry_price": 222000.0, "entry_open": 225500.0, "entry_high": 226000.0, "entry_low": 220000.0, "entry_close": 222000.0, "entry_volume": 403390.0, "entry_amount": 89516630000.0, "entry_marcap": 15265725660000.0, "market": "KOSPI", "MFE_30D_pct": 11.9369, "MAE_30D_pct": -14.7297, "MFE_90D_pct": 11.9369, "MAE_90D_pct": -28.964, "MFE_180D_pct": 37.1622, "MAE_180D_pct": -28.964, "peak_30D_date": "2025-02-24", "peak_30D_high": 248500.0, "trough_30D_date": "2025-03-14", "trough_30D_low": 189300.0, "peak_90D_date": "2025-02-24", "peak_90D_high": 248500.0, "trough_90D_date": "2025-05-22", "trough_90D_low": 157700.0, "peak_180D_date": "2025-10-27", "peak_180D_high": 304500.0, "trough_180D_date": "2025-05-22", "trough_180D_low": 157700.0, "drawdown_after_peak_180D_pct": -7.3892, "drawdown_after_peak_180D_trough_date": "2025-10-27", "forward_180D_last_date": "2025-10-27", "window_30D_available": true, "window_90D_available": true, "window_180D_available": true, "window_180D_corporate_action_contaminated": false, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "same_entry_group_id": "006400-2025-01-31-Stage4B-C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "dedupe_representative": true, "calibration_usable": true, "evidence_url": "https://samsungsdi.com/sdi-now/sdi-news/4221.html", "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "Samsung SDI reported a Q4 operating loss and EV/power-tool battery revenue decline from major-customer inventory adjustments, but also showed ESS strength, JV/contracts, and strategic foundation for 2025; hard 4C would have overblocked the later right tail.", "score_return_alignment_label": "watch_not_death_when_customer_adjustment_is_segment_specific", "current_profile_verdict": "watch_not_death_when_customer_adjustment_is_segment_specific"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C12-006400-20250124-SDI-MAJOR-CUSTOMER-INVENTORY", "trigger_id": "TRG-C12-006400-20250124-STAGE4B", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"EPS_FCF": 10, "visibility": 12, "bottleneck_pricing": 7, "mispricing": 9, "valuation": 8, "capital_allocation": 7, "information_confidence": 22, "risk_penalty": -18}, "weighted_score_before": 57, "stage_label_before": "Stage4C", "raw_component_scores_after": {"EPS_FCF": 12, "visibility": 14, "bottleneck_pricing": 7, "mispricing": 9, "valuation": 8, "capital_allocation": 7, "information_confidence": 22, "risk_penalty": -14}, "weighted_score_after": 65, "stage_label_after": "Stage4B", "changed_components": ["visibility", "EPS_FCF", "information_confidence", "risk_penalty"], "component_delta_explanation": "C12 gate separates temporary customer inventory adjustment from actual call-off/cancellation/cash break and requires evidence-quality confirmation before hard 4C.", "MFE_90D_pct": 11.94, "MAE_90D_pct": -28.96, "MFE_180D_pct": 37.16, "MAE_180D_pct": -28.96, "score_return_alignment_label": "watch_not_death_when_customer_adjustment_is_segment_specific", "current_profile_verdict": "watch_not_death_when_customer_adjustment_is_segment_specific"}
{"row_type": "case", "case_id": "C12-066970-20240509-LNF-INVENTORY-VALUATION-LOSS", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "case_type": "cathode_customer_mix_inventory_loss_false_positive_protection", "positive_or_counterexample": "positive", "best_trigger": "TRG-C12-066970-20240509-STAGE4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_or_strict_cap_correct_when_loss_and_inventory_break_dominate", "current_profile_verdict": "hard_4c_or_strict_cap_correct_when_loss_and_inventory_break_dominate", "price_source": "Songdaiki/stock-web", "notes": "C12 customer contract/call-off risk calibration row; not live candidate research."}
{"row_type": "trigger", "trigger_id": "TRG-C12-066970-20240509-STAGE4C", "case_id": "C12-066970-20240509-LNF-INVENTORY-VALUATION-LOSS", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "trigger_type": "Stage4C", "trigger_date": "2024-05-09", "entry_date": "2024-05-10", "entry_price": 153300.0, "entry_open": 152400.0, "entry_high": 161400.0, "entry_low": 152400.0, "entry_close": 153300.0, "entry_volume": 333198.0, "entry_amount": 52280225800.0, "entry_marcap": 5563983335400.0, "market": "KOSPI", "MFE_30D_pct": 15.4599, "MAE_30D_pct": -4.6967, "MFE_90D_pct": 15.4599, "MAE_90D_pct": -45.923, "MFE_180D_pct": 15.4599, "MAE_180D_pct": -49.9674, "peak_30D_date": "2024-06-13", "peak_30D_high": 177000.0, "trough_30D_date": "2024-06-24", "trough_30D_low": 146100.0, "peak_90D_date": "2024-06-13", "peak_90D_high": 177000.0, "trough_90D_date": "2024-09-10", "trough_90D_low": 82900.0, "peak_180D_date": "2024-06-13", "peak_180D_high": 177000.0, "trough_180D_date": "2025-01-03", "trough_180D_low": 76700.0, "drawdown_after_peak_180D_pct": -56.6667, "drawdown_after_peak_180D_trough_date": "2025-01-03", "forward_180D_last_date": "2025-02-07", "window_30D_available": true, "window_90D_available": true, "window_180D_available": true, "window_180D_corporate_action_contaminated": false, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "same_entry_group_id": "066970-2024-05-10-Stage4C-C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "dedupe_representative": true, "calibration_usable": true, "evidence_url": "https://www.asiae.co.kr/en/article/2024050915570493698", "source_proxy_only": true, "evidence_url_pending": false, "evidence_summary": "L&F reported Q1 sales of KRW 635.7bn and operating loss of KRW 203.8bn, with raw-material-price-driven ASP decline plus sales and inventory valuation losses. The later -45% to -50% MAE confirms that customer/order headlines cannot offset a broken margin/inventory bridge.", "score_return_alignment_label": "hard_4c_or_strict_cap_correct_when_loss_and_inventory_break_dominate", "current_profile_verdict": "hard_4c_or_strict_cap_correct_when_loss_and_inventory_break_dominate"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C12-066970-20240509-LNF-INVENTORY-VALUATION-LOSS", "trigger_id": "TRG-C12-066970-20240509-STAGE4C", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"EPS_FCF": 18, "visibility": 18, "bottleneck_pricing": 10, "mispricing": 12, "valuation": 10, "capital_allocation": 8, "information_confidence": 14, "risk_penalty": -20}, "weighted_score_before": 70, "stage_label_before": "Stage2", "raw_component_scores_after": {"EPS_FCF": 8, "visibility": 12, "bottleneck_pricing": 6, "mispricing": 8, "valuation": 6, "capital_allocation": 8, "information_confidence": 16, "risk_penalty": -25}, "weighted_score_after": 53, "stage_label_after": "Stage4C", "changed_components": ["visibility", "EPS_FCF", "information_confidence", "risk_penalty"], "component_delta_explanation": "C12 gate separates temporary customer inventory adjustment from actual call-off/cancellation/cash break and requires evidence-quality confirmation before hard 4C.", "MFE_90D_pct": 15.46, "MAE_90D_pct": -45.92, "MFE_180D_pct": 15.46, "MAE_180D_pct": -49.97, "score_return_alignment_label": "hard_4c_or_strict_cap_correct_when_loss_and_inventory_break_dominate", "current_profile_verdict": "hard_4c_or_strict_cap_correct_when_loss_and_inventory_break_dominate"}
{"row_type": "case", "case_id": "C12-361610-20240430-SKIET-DOWNSTREAM-INVENTORY", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "case_type": "separator_customer_inventory_adjustment_utilization_collapse", "positive_or_counterexample": "positive", "best_trigger": "TRG-C12-361610-20240430-STAGE4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_correct_when_downstream_inventory_adjustment_breaks_utilization_and_margin", "current_profile_verdict": "hard_4c_correct_when_downstream_inventory_adjustment_breaks_utilization_and_margin", "price_source": "Songdaiki/stock-web", "notes": "C12 customer contract/call-off risk calibration row; not live candidate research."}
{"row_type": "trigger", "trigger_id": "TRG-C12-361610-20240430-STAGE4C", "case_id": "C12-361610-20240430-SKIET-DOWNSTREAM-INVENTORY", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "trigger_type": "Stage4C", "trigger_date": "2024-04-30", "entry_date": "2024-05-02", "entry_price": 58900.0, "entry_open": 58700.0, "entry_high": 59600.0, "entry_low": 58600.0, "entry_close": 58900.0, "entry_volume": 131477.0, "entry_amount": 7771642900.0, "entry_marcap": 4199428168800.0, "market": "KOSPI", "MFE_30D_pct": 2.2071, "MAE_30D_pct": -27.5042, "MFE_90D_pct": 2.2071, "MAE_90D_pct": -48.9813, "MFE_180D_pct": 2.2071, "MAE_180D_pct": -62.9032, "peak_30D_date": "2024-05-03", "peak_30D_high": 60200.0, "trough_30D_date": "2024-06-04", "trough_30D_low": 42700.0, "peak_90D_date": "2024-05-03", "peak_90D_high": 60200.0, "trough_90D_date": "2024-09-10", "trough_90D_low": 30050.0, "peak_180D_date": "2024-05-03", "peak_180D_high": 60200.0, "trough_180D_date": "2025-01-02", "trough_180D_low": 21850.0, "drawdown_after_peak_180D_pct": -63.7043, "drawdown_after_peak_180D_trough_date": "2025-01-02", "forward_180D_last_date": "2025-01-31", "window_30D_available": true, "window_90D_available": true, "window_180D_available": true, "window_180D_corporate_action_contaminated": false, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "same_entry_group_id": "361610-2024-05-02-Stage4C-C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "dedupe_representative": true, "calibration_usable": true, "evidence_url": "https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220", "source_proxy_only": true, "evidence_url_pending": false, "evidence_summary": "Mirae described 1Q24 earnings shock from sluggish downstream-customer demand and inventory adjustments, revenue -73% QoQ, operating loss KRW 67.4bn, and gross/OP margin collapse; Reuters later tied SKIET sale consideration to weak EV demand and SK On losses.", "score_return_alignment_label": "hard_4c_correct_when_downstream_inventory_adjustment_breaks_utilization_and_margin", "current_profile_verdict": "hard_4c_correct_when_downstream_inventory_adjustment_breaks_utilization_and_margin"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C12-361610-20240430-SKIET-DOWNSTREAM-INVENTORY", "trigger_id": "TRG-C12-361610-20240430-STAGE4C", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"EPS_FCF": 16, "visibility": 16, "bottleneck_pricing": 8, "mispricing": 11, "valuation": 9, "capital_allocation": 8, "information_confidence": 16, "risk_penalty": -15}, "weighted_score_before": 69, "stage_label_before": "Stage2", "raw_component_scores_after": {"EPS_FCF": 6, "visibility": 10, "bottleneck_pricing": 4, "mispricing": 6, "valuation": 5, "capital_allocation": 8, "information_confidence": 14, "risk_penalty": -25}, "weighted_score_after": 50, "stage_label_after": "Stage4C", "changed_components": ["visibility", "EPS_FCF", "information_confidence", "risk_penalty"], "component_delta_explanation": "C12 gate separates temporary customer inventory adjustment from actual call-off/cancellation/cash break and requires evidence-quality confirmation before hard 4C.", "MFE_90D_pct": 2.21, "MAE_90D_pct": -48.98, "MFE_180D_pct": 2.21, "MAE_180D_pct": -62.9, "score_return_alignment_label": "hard_4c_correct_when_downstream_inventory_adjustment_breaks_utilization_and_margin", "current_profile_verdict": "hard_4c_correct_when_downstream_inventory_adjustment_breaks_utilization_and_margin"}
{"row_type": "case", "case_id": "C12-020150-20250124-LOTTE-CUSTOMER-INVENTORY", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "case_type": "customer_inventory_adjustment_loss_but_customer_diversification_offset", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-C12-020150-20250124-STAGE4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage4b_watch_correct_hard_4c_overblocks_when_sales_and_balance_sheet_survive", "current_profile_verdict": "stage4b_watch_correct_hard_4c_overblocks_when_sales_and_balance_sheet_survive", "price_source": "Songdaiki/stock-web", "notes": "C12 customer contract/call-off risk calibration row; not live candidate research."}
{"row_type": "trigger", "trigger_id": "TRG-C12-020150-20250124-STAGE4B", "case_id": "C12-020150-20250124-LOTTE-CUSTOMER-INVENTORY", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "trigger_type": "Stage4B", "trigger_date": "2025-01-24", "entry_date": "2025-01-31", "entry_price": 22100.0, "entry_open": 22900.0, "entry_high": 23000.0, "entry_low": 22100.0, "entry_close": 22100.0, "entry_volume": 113593.0, "entry_amount": 2539240650.0, "entry_marcap": 1019049453500.0, "market": "KOSPI", "MFE_30D_pct": 42.7602, "MAE_30D_pct": -8.371, "MFE_90D_pct": 42.7602, "MAE_90D_pct": -11.9457, "MFE_180D_pct": 42.7602, "MAE_180D_pct": -11.9457, "peak_30D_date": "2025-02-20", "peak_30D_high": 31550.0, "trough_30D_date": "2025-02-03", "trough_30D_low": 20250.0, "peak_90D_date": "2025-02-20", "peak_90D_high": 31550.0, "trough_90D_date": "2025-05-22", "trough_90D_low": 19460.0, "peak_180D_date": "2025-02-20", "peak_180D_high": 31550.0, "trough_180D_date": "2025-05-22", "trough_180D_low": 19460.0, "drawdown_after_peak_180D_pct": -38.3201, "drawdown_after_peak_180D_trough_date": "2025-05-22", "forward_180D_last_date": "2025-10-27", "window_30D_available": true, "window_90D_available": true, "window_180D_available": true, "window_180D_corporate_action_contaminated": false, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "same_entry_group_id": "020150-2025-01-31-Stage4B-C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "dedupe_representative": true, "calibration_usable": true, "evidence_url": "https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128", "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "Company official preliminary 2024 results showed operating loss from lower utilization for customer inventory adjustments and overseas inventory valuation losses, while sales increased on diversified customers/North America and balance sheet remained stable; price path strongly supports 4B over hard 4C.", "score_return_alignment_label": "stage4b_watch_correct_hard_4c_overblocks_when_sales_and_balance_sheet_survive", "current_profile_verdict": "stage4b_watch_correct_hard_4c_overblocks_when_sales_and_balance_sheet_survive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C12-020150-20250124-LOTTE-CUSTOMER-INVENTORY", "trigger_id": "TRG-C12-020150-20250124-STAGE4B", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"EPS_FCF": 10, "visibility": 12, "bottleneck_pricing": 7, "mispricing": 10, "valuation": 8, "capital_allocation": 9, "information_confidence": 22, "risk_penalty": -22}, "weighted_score_before": 56, "stage_label_before": "Stage4C", "raw_component_scores_after": {"EPS_FCF": 12, "visibility": 16, "bottleneck_pricing": 7, "mispricing": 10, "valuation": 8, "capital_allocation": 10, "information_confidence": 22, "risk_penalty": -19}, "weighted_score_after": 66, "stage_label_after": "Stage4B", "changed_components": ["visibility", "EPS_FCF", "information_confidence", "risk_penalty"], "component_delta_explanation": "C12 gate separates temporary customer inventory adjustment from actual call-off/cancellation/cash break and requires evidence-quality confirmation before hard 4C.", "MFE_90D_pct": 42.76, "MAE_90D_pct": -11.95, "MFE_180D_pct": 42.76, "MAE_180D_pct": -11.95, "score_return_alignment_label": "stage4b_watch_correct_hard_4c_overblocks_when_sales_and_balance_sheet_survive", "current_profile_verdict": "stage4b_watch_correct_hard_4c_overblocks_when_sales_and_balance_sheet_survive"}
{"row_type": "case", "case_id": "C12-247540-20250211-ECOPROBM-FY24-LOSS-REBOUND", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "case_type": "cathode_inventory_loss_high_mae_rebound_exception", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-C12-247540-20250211-STAGE4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "drawdown_aware_4b_needed_hard_4c_only_if_customer_cancellation_or_cash_break", "current_profile_verdict": "drawdown_aware_4b_needed_hard_4c_only_if_customer_cancellation_or_cash_break", "price_source": "Songdaiki/stock-web", "notes": "C12 customer contract/call-off risk calibration row; not live candidate research."}
{"row_type": "trigger", "trigger_id": "TRG-C12-247540-20250211-STAGE4B", "case_id": "C12-247540-20250211-ECOPROBM-FY24-LOSS-REBOUND", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CUSTOMER_CALLOFF_INVENTORY_ADJUSTMENT_CONTRACT_RISK_GATE", "trigger_type": "Stage4B", "trigger_date": "2025-02-11", "entry_date": "2025-02-12", "entry_price": 121200.0, "entry_open": 120600.0, "entry_high": 123500.0, "entry_low": 118500.0, "entry_close": 121200.0, "entry_volume": 572381.0, "entry_amount": 69371875900.0, "entry_marcap": 11853522892800.0, "market": "KOSDAQ GLOBAL", "MFE_30D_pct": 16.9142, "MAE_30D_pct": -11.3861, "MFE_90D_pct": 16.9142, "MAE_90D_pct": -33.0858, "MFE_180D_pct": 48.5149, "MAE_180D_pct": -33.0858, "peak_30D_date": "2025-02-24", "peak_30D_high": 141700.0, "trough_30D_date": "2025-03-25", "trough_30D_low": 107400.0, "peak_90D_date": "2025-02-24", "peak_90D_high": 141700.0, "trough_90D_date": "2025-05-27", "trough_90D_low": 81100.0, "peak_180D_date": "2025-10-27", "peak_180D_high": 180000.0, "trough_180D_date": "2025-05-27", "trough_180D_low": 81100.0, "drawdown_after_peak_180D_pct": -16.3889, "drawdown_after_peak_180D_trough_date": "2025-11-05", "forward_180D_last_date": "2025-11-06", "window_30D_available": true, "window_90D_available": true, "window_180D_available": true, "window_180D_corporate_action_contaminated": false, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "same_entry_group_id": "247540-2025-02-12-Stage4B-C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "dedupe_representative": true, "calibration_usable": true, "evidence_url": "https://www.asiae.co.kr/en/article/2024110110191994466", "source_proxy_only": true, "evidence_url_pending": false, "evidence_summary": "EcoPro/EcoPro BM suffered EV-chasm losses, lower product sales and inventory valuation provisions, but later price path produced a strong 180D right tail after large MAE; the row calibrates 4B/high-MAE watch, not automatic hard 4C.", "score_return_alignment_label": "drawdown_aware_4b_needed_hard_4c_only_if_customer_cancellation_or_cash_break", "current_profile_verdict": "drawdown_aware_4b_needed_hard_4c_only_if_customer_cancellation_or_cash_break"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C12-247540-20250211-ECOPROBM-FY24-LOSS-REBOUND", "trigger_id": "TRG-C12-247540-20250211-STAGE4B", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"EPS_FCF": 9, "visibility": 12, "bottleneck_pricing": 6, "mispricing": 9, "valuation": 8, "capital_allocation": 8, "information_confidence": 18, "risk_penalty": -18}, "weighted_score_before": 55, "stage_label_before": "Stage4C", "raw_component_scores_after": {"EPS_FCF": 11, "visibility": 14, "bottleneck_pricing": 6, "mispricing": 9, "valuation": 8, "capital_allocation": 8, "information_confidence": 18, "risk_penalty": -16}, "weighted_score_after": 63, "stage_label_after": "Stage4B", "changed_components": ["visibility", "EPS_FCF", "information_confidence", "risk_penalty"], "component_delta_explanation": "C12 gate separates temporary customer inventory adjustment from actual call-off/cancellation/cash break and requires evidence-quality confirmation before hard 4C.", "MFE_90D_pct": 16.91, "MAE_90D_pct": -33.09, "MFE_180D_pct": 48.51, "MAE_180D_pct": -33.09, "score_return_alignment_label": "drawdown_aware_4b_needed_hard_4c_only_if_customer_cancellation_or_cash_break", "current_profile_verdict": "drawdown_aware_4b_needed_hard_4c_only_if_customer_cancellation_or_cash_break"}
{"row_type": "shadow_weight", "axis": "C12_customer_calloff_contract_risk_gate", "scope": "canonical_archetype", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Require direct customer call-off/cancellation/utilization/margin evidence before hard 4C; avoid overblocking recoverable inventory-adjustment prints.", "backtest_effect": "Contains L&F and SKIET false positives while preserving LGES, Samsung SDI, Lotte Energy Materials and EcoPro BM 4B rebound paths.", "trigger_ids": "TRG-C12-373220-20240725-STAGE4B|TRG-C12-006400-20250124-STAGE4B|TRG-C12-066970-20240509-STAGE4C|TRG-C12-361610-20240430-STAGE4C|TRG-C12-020150-20250124-STAGE4B|TRG-C12-247540-20250211-STAGE4B", "calibration_usable_count": 6, "new_independent_case_count": 6, "counterexample_count": 4, "confidence": "medium", "proposal_type": "canonical_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "residual_contribution", "round": "R3", "loop": "126", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 6, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "earlier_thesis_break_watch", "hard_4c_confirmation", "drawdown_aware_confirmation"], "residual_error_types_found": ["customer_inventory_adjustment_hard_4c_overblock", "calloff_risk_false_positive_without_margin_bridge", "proxy_only_customer_demand_evidence", "deep_MAE_after_recoverable_battery_loss"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop: 126
completed_large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
completed_canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selected_priority_bucket: Priority 0/1 quality repair — C12 customer call-off / inventory-adjustment risk split
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
