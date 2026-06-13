# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
output_file: e2r_stock_web_v12_residual_round_R2_loop_109_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: "Priority 0 / under 30 rows; static C06 rows=17, need-to-30=13; current-session C06 loop_108 already used 000660/005930/222800/353200/011070, so this loop uses five new symbols"
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: mixed_C06_hbm_adjacent_bigtech_ddr5_fcbga_second_pass
loop_objective: coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
```

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_1_stock_web_calibrated` / active ledger profile `e2r_2_2_rolling_calibrated`. The loop does not re-prove global rules. It tests whether C06 needs a more precise gate between true HBM/customer/capacity allocation and HBM-adjacent substrate or FC-BGA proxy narratives.

Existing axes tested but not globally re-proposed:

```text
stage2_required_bridge
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
local_4b_watch_guard
```

## 2. Round / Large Sector / Canonical Archetype Scope

```yaml
selected_round: R2
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
scope_check: pass
```

C06 is not a generic PCB/FC-BGA/DDR5 theme bucket. For calibration it should separate:

1. confirmed big-tech / memory-customer exposure with capacity or backlog visibility;
2. DDR5 or AI server component routes that have actual revenue conversion;
3. HBM-adjacent substrate proxies that name Samsung/SK hynix/NVIDIA/AI but lack allocation, ASP, shipment, or margin bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index priority table marks C06 as Priority 0 with 17 rows and need-to-30 of 13. Current-session duplicate avoidance also excludes the immediately prior C06 loop_108 symbol set: `000660`, `005930`, `222800`, `353200`, `011070`.

This file uses five new C06 symbols:

```text
007660 이수페타시스
356860 티엘비
195870 해성디에스
007810 코리아써키트
009150 삼성전기
```

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
price_data_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
manifest_path: atlas/manifest.json
manifest_max_date: 2026-02-20
```

All entry windows have 180 stock-web trading rows. Corporate-action candidates listed in symbol profiles do not overlap any entry_date through D+180 window used here.

## 5. Historical Eligibility Gate

| symbol | trigger_date | entry_date | forward_window_trading_days | calibration_usable | corporate_action_window_status |
|---|---:|---:|---:|---|---|
| 007660 | 2023-01-19 | 2023-01-20 | 180 | true | clean_180D_window |
| 356860 | 2023-05-31 | 2023-06-01 | 180 | true | clean_180D_window |
| 195870 | 2024-05-16 | 2024-05-17 | 180 | true | clean_180D_window |
| 007810 | 2023-09-11 | 2023-09-12 | 180 | true | clean_180D_window |
| 009150 | 2024-08-26 | 2024-08-27 | 180 | true | clean_180D_window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | compressed canonical | calibration meaning |
|---|---|---|
| HBM_ADJACENT_BIGTECH_MLB_CUSTOMER_CAPACITY_POSITIVE | C06 | Big-tech customer expansion plus backlog/capex visibility can be C06-positive if price path confirms |
| SERVER_DDR5_MODULE_PCB_CUSTOMER_CAPACITY_POSITIVE | C06 | DDR5 server module PCB can be C06-Yellow when customer/revenue/margin conversion is visible |
| HBM_ADJACENT_PACKAGE_SUBSTRATE_PROXY_FALSE_STAGE2 | C06 | Merely naming Samsung/SK hynix as customers is not enough without HBM allocation or margin bridge |
| FCBGA_NAMED_CUSTOMER_REVENUE_BRIDGE_POSITIVE_NOT_FULL_HBM | C06 | Named FC-BGA customer revenue can be Stage2-Actionable, but not pure C06 Green without high-end AI/HBM lock-up |
| AI_SERVER_FCBGA_CAPACITY_TARGET_WITHOUT_NEAR_TERM_REVENUE_FALSE_STAGE2 | C06 | Future high-value mix target is too early for positive stage unless near-term revenue/revision is confirmed |

## 7. Case Selection Summary

| symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 007660 | 이수페타시스 | Stage3-Green | 2023-01-19 | 2023-01-20 | 6,380 | 157.52 | -2.51 | 578.68 | -2.51 | current_profile_correct_entry_but_4B_overlay_needed_after_peak |
| 356860 | 티엘비 | Stage3-Yellow | 2023-05-31 | 2023-06-01 | 22,650 | 39.96 | -7.06 | 45.7 | -7.06 | current_profile_correct |
| 195870 | 해성디에스 | Stage2 | 2024-05-16 | 2024-05-17 | 50,600 | 1.19 | -50.59 | 1.19 | -60.18 | current_profile_false_positive |
| 007810 | 코리아써키트 | Stage2-Actionable | 2023-09-11 | 2023-09-12 | 15,750 | 43.17 | -14.29 | 43.17 | -14.29 | current_profile_mixed_stage2_ok_green_block_needed |
| 009150 | 삼성전기 | Stage2-Actionable | 2024-08-26 | 2024-08-27 | 143,900 | 1.39 | -26.69 | 4.1 | -26.69 | current_profile_false_positive_or_too_early |

## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 3
counterexample_count: 2
4B_case_count: 3
4C_case_count: 0
calibration_usable_case_count: 5
new_independent_case_count: 5
reused_case_count: 0
new_independent_case_ratio: 1.0
```

Positive side: Isu Petasys and TLB show that confirmed customer/capacity or server DDR5 conversion can unlock strong MFE. Korea Circuit shows that named FC-BGA revenue can support Stage2-Actionable even when it should not become pure HBM Green.

Counterexample side: Haesung DS and Samsung Electro-Mechanics show that HBM-adjacent package substrate or AI server FC-BGA target narratives can be too early without shipment/revenue/margin bridge.

## 9. Evidence Source Map

| symbol | evidence date | source URL | evidence used |
|---|---:|---|---|
| 007660 | 2023-01-19 | https://www.thelec.kr/news/articleView.html?idxno=19527 | TheElec reported that Isu Petasys had secured Google, NVIDIA, Microsoft and Intel as customers; server MLB demand, backlog expansion, and capex for customer response were visible. |
| 356860 | 2023-05-31 | https://www.tlbpcb.com/bbs/list.php?catcode=19100000&code=board2&page=3 | TLB press coverage described server DDR5 memory-module PCB readiness; DDR5 revenue contribution had risen, server share was high, Samsung/SK hynix DDR5 supply expansion would lift related revenue. |
| 195870 | 2024-05-16 | https://kind.krx.co.kr/external/2024/05/16/000853/20240516001966/11013.htm | KRX quarterly report showed package-substrate exposure and Samsung Electronics/SK hynix as major customers, but did not confirm HBM allocation, ASP, margin, or capacity lock-up. |
| 007810 | 2023-09-11 | https://www.thelec.kr/news/articleView.html?idxno=22979 | TheElec reported that Korea Circuit was supplying FC-BGA to STMicro; the article also separated mid/low-end FC-BGA and weakness in first-half substrate sales. |
| 009150 | 2024-08-26 | https://m.samsungsem.com/kr/newsroom/news/view.do?id=8381 | Samsung Electro-Mechanics announced a 2026 target to lift high-value FCBGA exposure for servers, AI, automotive and networks above 50%, but the event was target/capacity narrative rather than near-term confirmed revenue revision. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | corporate-action status |
|---|---|---|---|
| 007660 | atlas/ohlcv_tradable_by_symbol_year/007/007660/2023.csv | atlas/symbol_profiles/007/007660.json | clean_180D_window |
| 356860 | atlas/ohlcv_tradable_by_symbol_year/356/356860/2023.csv | atlas/symbol_profiles/356/356860.json | clean_180D_window |
| 195870 | atlas/ohlcv_tradable_by_symbol_year/195/195870/2024.csv | atlas/symbol_profiles/195/195870.json | clean_180D_window |
| 007810 | atlas/ohlcv_tradable_by_symbol_year/007/007810/2023.csv | atlas/symbol_profiles/007/007810.json | clean_180D_window |
| 009150 | atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv | atlas/symbol_profiles/009/009150.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### 007660 이수페타시스
The 2023-01-19 evidence had direct customer-quality force: Google, NVIDIA, Microsoft and Intel customer expansion, server MLB demand, backlog growth, and capacity investment. Entry had low MAE and exceptional MFE, so C06 should not block it merely because it is an HBM-adjacent PCB route. The later post-peak drawdown supports post-peak 4B overlay.

### 356860 티엘비
Server DDR5 memory-module PCB had a customer/revenue conversion route: higher DDR5 contribution, server share, and customer DDR5 supply expansion. The price path was positive with controlled MAE, supporting Stage3-Yellow for C06 when the route is revenue-backed.

### 195870 해성디에스
Samsung Electronics and SK hynix customer exposure in package substrate was not enough. The row lacks HBM allocation, ASP, shipment or margin bridge; the actual path was a high-MAE failed rerating.

### 007810 코리아써키트
STMicro FC-BGA supply had named customer and revenue bridge, but the article itself noted mid/low-end FC-BGA and weak first-half substrate sales. It is Stage2-Actionable, not a clean C06 Stage3-Green.

### 009150 삼성전기
The high-value FCBGA target for servers/AI was strategically important, but as of 2024-08-26 it was more of a 2026 mix target/capacity narrative than a near-term revision bridge. The price path confirms that C06 should require near-term shipment or revenue conversion.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | corp_action |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 007660 | 2023-01-20 | 6,380 | 57.99 | -2.51 | 157.52 | -2.51 | 578.68 | -2.51 | 2023-07-25 | 43,300 | -40.65 | clean_180D_window |
| 356860 | 2023-06-01 | 22,650 | 39.96 | -7.06 | 39.96 | -7.06 | 45.7 | -7.06 | 2024-01-04 | 33,000 | -30.3 | clean_180D_window |
| 195870 | 2024-05-17 | 50,600 | 1.19 | -13.74 | 1.19 | -50.59 | 1.19 | -60.18 | 2024-05-17 | 51,200 | -60.64 | clean_180D_window |
| 007810 | 2023-09-12 | 15,750 | 4.44 | -12.95 | 43.17 | -14.29 | 43.17 | -14.29 | 2023-12-14 | 22,550 | -34.32 | clean_180D_window |
| 009150 | 2024-08-27 | 143,900 | 1.39 | -12.44 | 1.39 | -26.69 | 4.1 | -26.69 | 2025-02-17 | 149,800 | -27.37 | clean_180D_window |

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely action | actual path | residual verdict |
|---|---|---|---|
| 007660 | Stage3-Green | exceptional MFE with later peak drawdown | entry correct, 4B overlay should not be late |
| 356860 | Stage3-Yellow | strong MFE with controlled MAE | aligned |
| 195870 | Stage2 from customer proximity | MFE capped near 1%, MAE below -50% by 90D | false positive |
| 007810 | Stage2-Actionable | MFE90 > 40%, MAE90 around -14% | Stage2 ok, Green should be capped |
| 009150 | Stage2-Actionable from AI FCBGA target | MFE weak, MAE90 below -26% | too early / false positive |

Residual error types:

```text
hbm_adjacent_substrate_proxy_false_stage2
capacity_target_without_revenue_conversion
post_peak_4b_too_late_after_fast_mfe
stage2_ok_but_green_cap_needed
```

## 14. Stage2 / Yellow / Green Comparison

C06 should behave like a narrowing funnel:

```text
Stage2: public customer/capacity/substrate event exists.
Stage2-Actionable: named customer or revenue route is visible.
Stage3-Yellow: customer route plus shipment/revenue/margin conversion appears.
Stage3-Green: memory/HBM capacity allocation, durable customer confirmation, financial revision and low red-team risk are all present.
```

This loop argues against treating all HBM-adjacent substrate names as equal. Big-tech customer confirmation and revenue-backed DDR5 conversion worked; mere customer proximity or future mix targets failed.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local/full timing verdict |
|---|---|---|
| 007660 | positioning_overheat, valuation_blowoff | post-peak 4B overlay needed after 2023-07-25 peak |
| 356860 | positioning_overheat | monitor after 2024-01-04 peak, not entry block |
| 195870 | margin_or_backlog_slowdown, valuation_blowoff | 4B/Stage1 watch should have blocked Stage2 promotion |
| 007810 | positioning_overheat, margin_or_backlog_slowdown | Stage2 allowed, Green capped |
| 009150 | margin_or_backlog_slowdown, valuation_blowoff | capacity target too early; 4B watch from entry |

## 16. 4C Protection Audit

No hard Stage4C row is proposed. There was no confirmed thesis-break event such as contract cancellation, qualification failure, customer call-off, accounting/trust break, or regulatory rejection within the trigger evidence. These are 4B/watch and Stage2 false-positive calibration samples, not hard 4C rows.

## 17. Sector-Specific Rule Candidate

```text
L2_C06_HBM_ADJACENT_CUSTOMER_CAPACITY_AND_REVENUE_BRIDGE_SPLIT
```

Rule wording:

```text
Within L2, HBM-adjacent PCB/substrate/FC-BGA evidence may support Stage2 only when customer quality is named or revenue route is visible. Stage3 requires capacity allocation, shipment/revenue recognition, ASP/margin bridge, or confirmed financial revision. Future mix targets and generic Samsung/SK hynix/NVIDIA proximity remain Stage1/Stage2 watch.
```

## 18. Canonical-Archetype Rule Candidate

```text
C06_HBM_ADJACENT_REQUIRES_CUSTOMER_QUALITY_CAPACITY_ALLOCATION_AND_MARGIN_BRIDGE
```

Canonical adjustment:

```text
Increase C06 weight on customer_quality_score, backlog_visibility_score, capacity_or_shipment_score and margin_bridge_score when named customer + conversion are present.
Decrease C06 promotion value for HBM-adjacent substrate proxy without named allocation/revenue/margin bridge.
```

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current broad bridge profile | 5 | 48.65 | -20.23 | 134.97 | -28.74 | 0.40 | accepts good winners but lets proxy false positives through |
| P0b e2r_2_0_baseline_reference | older looser Stage2 | 5 | 48.65 | -20.23 | 134.97 | -28.74 | 0.60 | too many HBM-adjacent proxies promoted |
| P1 sector_specific_candidate_profile | L2 customer/revenue bridge split | 4 | 60.16 | -9.48 | 167.26 | -7.48 | 0.25 | improves proxy filtering |
| P2 canonical_archetype_candidate_profile | C06 allocation/margin bridge gate | 3 | 80.22 | -7.96 | 222.52 | -7.96 | 0.00 | best alignment for true C06 positives |
| P3 counterexample_guard_profile | block future target / generic customer proximity | 3 | 80.22 | -7.96 | 222.52 | -7.96 | 0.00 | strongest guardrail but may miss early Samsung/FCBGA recovery |

## 20. Score-Return Alignment Matrix

| symbol | before score/stage | after score/stage | return alignment |
|---|---|---|---|
| 007660 | 90 / Stage3-Green | 88 / Stage3-Green + post_peak_4B_watch | aligned, but 4B overlay needed |
| 356860 | 82 / Stage3-Yellow | 84 / Stage3-Yellow | aligned |
| 195870 | 66 / Stage2 | 48 / Stage1/Watch | improved; false positive blocked |
| 007810 | 72 / Stage2-Actionable | 74 / Stage2-Actionable + green_cap | aligned with Stage2, not Green |
| 009150 | 70 / Stage2-Actionable | 59 / Stage1/Watch + 4B Watch | improved; too-early Stage2 capped |

## 21. Coverage Matrix

```yaml
static_index_C06_rows_before: 17
current_session_C06_loop_108_added: 5
this_loop_added: 5
static_index_adjusted_estimate_after_this_loop: 27
new_symbols_this_loop: 5
new_trigger_families_this_loop: 5
positive_case_count: 3
counterexample_count: 2
4B_watch_or_overlay_case_count: 3
4C_case_count: 0
```

## 22. Residual Contribution Summary

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2/C06.

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
new_axis_proposed: C06_HBM_ADJACENT_REQUIRES_CUSTOMER_QUALITY_CAPACITY_ALLOCATION_AND_MARGIN_BRIDGE
existing_axis_strengthened: stage2_required_bridge | local_4b_watch_guard | full_4b_requires_non_price_evidence
existing_axis_weakened: null
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- historical trigger dates
- actual stock-web entry_date and entry_price
- 30D/90D/180D MFE and MAE
- 180 trading-day forward window
- clean corporate-action window status
- C06 duplicate avoidance against current-session loop_108 symbols
```

Not validated:

```text
- live candidate status
- investment recommendation
- production scoring patch
- broker API or current watchlist
- exact intraday publication time beyond conservative next-trading-day entry when needed
```

## 24. Shadow Weight Calibration

```yaml
rule_scope: canonical_archetype_specific
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
shadow_profile_candidate: C06_HBM_ADJACENT_CUSTOMER_CAPACITY_MARGIN_BRIDGE_GATE
suggested_weight_direction:
  customer_quality_score: up when named customer + allocation/revenue conversion present
  backlog_visibility_score: up when capex/backlog tied to named customer response
  margin_bridge_score: up only with revenue/ASP/margin evidence
  execution_risk_score: penalty when only future mix target or generic customer proximity exists
  valuation_repricing_score: cap when MFE is fast but evidence remains Stage2-only
production_change_now: false
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C06_R2L109_007660_BIGTECH_MLB_CUSTOMER_EXPANSION_20230119","symbol":"007660","company_name":"이수페타시스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_ADJACENT_BIGTECH_MLB_CUSTOMER_CAPACITY_POSITIVE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C06_R2L109_007660_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct_entry_but_4B_overlay_needed_after_peak","price_source":"Songdaiki/stock-web","notes":"Big-tech customer confirmation and capex/backlog visibility deserved Stage3; the later blowoff argues for 4B overlay timing rather than blocking the entry."}
{"row_type":"trigger","trigger_id":"C06_R2L109_007660_T1","case_id":"C06_R2L109_007660_BIGTECH_MLB_CUSTOMER_EXPANSION_20230119","symbol":"007660","company_name":"이수페타시스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_ADJACENT_BIGTECH_MLB_CUSTOMER_CAPACITY_POSITIVE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage3-Green","trigger_date":"2023-01-19","evidence_available_at_that_date":"TheElec reported that Isu Petasys had secured Google, NVIDIA, Microsoft and Intel as customers; server MLB demand, backlog expansion, and capex for customer response were visible.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=19527","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_visibility"],"stage3_evidence_fields":["durable_customer_confirmation","financial_visibility","capacity_or_shipment_route","relative_strength_confirmation"],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007660/2023.csv","profile_path":"atlas/symbol_profiles/007/007660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-20","entry_price":6380.0,"MFE_30D_pct":57.99,"MFE_90D_pct":157.52,"MFE_180D_pct":578.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.51,"MAE_90D_pct":-2.51,"MAE_180D_pct":-2.51,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-07-25","peak_price":43300.0,"drawdown_after_peak_pct":-40.65,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"post_peak_4B_watch_needed","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"bigtech_mlb_customer_capacity_success_post_peak_watch","current_profile_verdict":"current_profile_correct_entry_but_4B_overlay_needed_after_peak","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|007660|2023-01-20|6380.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L109_007660_BIGTECH_MLB_CUSTOMER_EXPANSION_20230119","trigger_id":"C06_R2L109_007660_T1","symbol":"007660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":86,"margin_bridge_score":82,"revision_score":80,"relative_strength_score":95,"customer_quality_score":90,"policy_or_regulatory_score":5,"valuation_repricing_score":80,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":90,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":88,"margin_bridge_score":82,"revision_score":80,"relative_strength_score":92,"customer_quality_score":92,"policy_or_regulatory_score":5,"valuation_repricing_score":68,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":88,"stage_label_after":"Stage3-Green + post_peak_4B_watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Big-tech customer confirmation and capex/backlog visibility deserved Stage3; the later blowoff argues for 4B overlay timing rather than blocking the entry.","MFE_90D_pct":157.52,"MAE_90D_pct":-2.51,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct_entry_but_4B_overlay_needed_after_peak"}
{"row_type":"case","case_id":"C06_R2L109_356860_SERVER_DDR5_MODULE_PCB_CUSTOMER_CAPACITY_20230531","symbol":"356860","company_name":"티엘비","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"SERVER_DDR5_MODULE_PCB_CUSTOMER_CAPACITY_POSITIVE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C06_R2L109_356860_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"The DDR5 server module route had customer quality and revenue conversion, so C06 should allow Yellow even though it is not pure HBM."}
{"row_type":"trigger","trigger_id":"C06_R2L109_356860_T1","case_id":"C06_R2L109_356860_SERVER_DDR5_MODULE_PCB_CUSTOMER_CAPACITY_20230531","symbol":"356860","company_name":"티엘비","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"SERVER_DDR5_MODULE_PCB_CUSTOMER_CAPACITY_POSITIVE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage3-Yellow","trigger_date":"2023-05-31","evidence_available_at_that_date":"TLB press coverage described server DDR5 memory-module PCB readiness; DDR5 revenue contribution had risen, server share was high, Samsung/SK hynix DDR5 supply expansion would lift related revenue.","evidence_source":"https://www.tlbpcb.com/bbs/list.php?catcode=19100000&code=board2&page=3","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","repeat_revenue_conversion","margin_bridge","durable_customer_confirmation"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/356/356860/2023.csv","profile_path":"atlas/symbol_profiles/356/356860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-01","entry_price":22650.0,"MFE_30D_pct":39.96,"MFE_90D_pct":39.96,"MFE_180D_pct":45.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.06,"MAE_90D_pct":-7.06,"MAE_180D_pct":-7.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-04","peak_price":33000.0,"drawdown_after_peak_pct":-30.3,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"server_ddr5_customer_capacity_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|356860|2023-06-01|22650.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L109_356860_SERVER_DDR5_MODULE_PCB_CUSTOMER_CAPACITY_20230531","trigger_id":"C06_R2L109_356860_T1","symbol":"356860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":70,"margin_bridge_score":72,"revision_score":78,"relative_strength_score":82,"customer_quality_score":85,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":72,"margin_bridge_score":76,"revision_score":80,"relative_strength_score":80,"customer_quality_score":88,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":32,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"The DDR5 server module route had customer quality and revenue conversion, so C06 should allow Yellow even though it is not pure HBM.","MFE_90D_pct":39.96,"MAE_90D_pct":-7.06,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C06_R2L109_195870_PACKAGE_SUBSTRATE_SAMSUNG_SKHYNIX_PROXY_FALSE_STAGE2_20240516","symbol":"195870","company_name":"해성디에스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_ADJACENT_PACKAGE_SUBSTRATE_PROXY_FALSE_STAGE2","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_R2L109_195870_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Customer-name proximity alone was not enough; without HBM allocation or margin bridge, the path became a high-MAE false positive."}
{"row_type":"trigger","trigger_id":"C06_R2L109_195870_T1","case_id":"C06_R2L109_195870_PACKAGE_SUBSTRATE_SAMSUNG_SKHYNIX_PROXY_FALSE_STAGE2_20240516","symbol":"195870","company_name":"해성디에스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_ADJACENT_PACKAGE_SUBSTRATE_PROXY_FALSE_STAGE2","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage2","trigger_date":"2024-05-16","evidence_available_at_that_date":"KRX quarterly report showed package-substrate exposure and Samsung Electronics/SK hynix as major customers, but did not confirm HBM allocation, ASP, margin, or capacity lock-up.","evidence_source":"https://kind.krx.co.kr/external/2024/05/16/000853/20240516001966/11013.htm","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/195/195870/2024.csv","profile_path":"atlas/symbol_profiles/195/195870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":50600.0,"MFE_30D_pct":1.19,"MFE_90D_pct":1.19,"MFE_180D_pct":1.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.74,"MAE_90D_pct":-50.59,"MAE_180D_pct":-60.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-17","peak_price":51200.0,"drawdown_after_peak_pct":-60.64,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"post_peak_4B_watch_needed","four_b_evidence_type":["margin_or_backlog_slowdown","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"package_substrate_customer_proxy_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|195870|2024-05-17|50600.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L109_195870_PACKAGE_SUBSTRATE_SAMSUNG_SKHYNIX_PROXY_FALSE_STAGE2_20240516","trigger_id":"C06_R2L109_195870_T1","symbol":"195870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":30,"revision_score":45,"relative_strength_score":40,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":70,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":28,"margin_bridge_score":20,"revision_score":35,"relative_strength_score":35,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":42,"execution_risk_score":86,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":48,"stage_label_after":"Stage1/Watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Customer-name proximity alone was not enough; without HBM allocation or margin bridge, the path became a high-MAE false positive.","MFE_90D_pct":1.19,"MAE_90D_pct":-50.59,"score_return_alignment_label":"misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_R2L109_007810_STMICRO_FCBGA_CUSTOMER_REVENUE_POSITIVE_BUT_NOT_HBM_GREEN_20230911","symbol":"007810","company_name":"코리아써키트","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"FCBGA_NAMED_CUSTOMER_REVENUE_BRIDGE_POSITIVE_NOT_FULL_HBM","case_type":"stage2_success_with_green_cap","positive_or_counterexample":"positive","best_trigger":"C06_R2L109_007810_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_mixed_stage2_ok_green_block_needed","price_source":"Songdaiki/stock-web","notes":"Named FC-BGA revenue bridge was real enough for Stage2-Actionable, but the end-market was not a pure HBM capacity lock-up, so C06 should cap Green."}
{"row_type":"trigger","trigger_id":"C06_R2L109_007810_T1","case_id":"C06_R2L109_007810_STMICRO_FCBGA_CUSTOMER_REVENUE_POSITIVE_BUT_NOT_HBM_GREEN_20230911","symbol":"007810","company_name":"코리아써키트","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"FCBGA_NAMED_CUSTOMER_REVENUE_BRIDGE_POSITIVE_NOT_FULL_HBM","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-11","evidence_available_at_that_date":"TheElec reported that Korea Circuit was supplying FC-BGA to STMicro; the article also separated mid/low-end FC-BGA and weakness in first-half substrate sales.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=22979","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","revenue_conversion_route"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007810/2023.csv","profile_path":"atlas/symbol_profiles/007/007810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-12","entry_price":15750.0,"MFE_30D_pct":4.44,"MFE_90D_pct":43.17,"MFE_180D_pct":43.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.95,"MAE_90D_pct":-14.29,"MAE_180D_pct":-14.29,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-14","peak_price":22550.0,"drawdown_after_peak_pct":-34.32,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"named_customer_fcbga_positive_but_hbm_green_blocked","current_profile_verdict":"current_profile_mixed_stage2_ok_green_block_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|007810|2023-09-12|15750.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L109_007810_STMICRO_FCBGA_CUSTOMER_REVENUE_POSITIVE_BUT_NOT_HBM_GREEN_20230911","trigger_id":"C06_R2L109_007810_T1","symbol":"007810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":55,"margin_bridge_score":48,"revision_score":50,"relative_strength_score":62,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":55,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":62,"backlog_visibility_score":55,"margin_bridge_score":50,"revision_score":50,"relative_strength_score":62,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":58,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable + green_cap","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Named FC-BGA revenue bridge was real enough for Stage2-Actionable, but the end-market was not a pure HBM capacity lock-up, so C06 should cap Green.","MFE_90D_pct":43.17,"MAE_90D_pct":-14.29,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_mixed_stage2_ok_green_block_needed"}
{"row_type":"case","case_id":"C06_R2L109_009150_AI_SERVER_FCBGA_TARGET_NO_IMMEDIATE_REVENUE_FALSE_STAGE2_20240826","symbol":"009150","company_name":"삼성전기","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_SERVER_FCBGA_CAPACITY_TARGET_WITHOUT_NEAR_TERM_REVENUE_FALSE_STAGE2","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_R2L109_009150_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"misaligned","current_profile_verdict":"current_profile_false_positive_or_too_early","price_source":"Songdaiki/stock-web","notes":"A capacity-mix target can be Stage2 watch, but without immediate shipment/revenue/margin conversion it should not be treated as C06 structural unlock."}
{"row_type":"trigger","trigger_id":"C06_R2L109_009150_T1","case_id":"C06_R2L109_009150_AI_SERVER_FCBGA_TARGET_NO_IMMEDIATE_REVENUE_FALSE_STAGE2_20240826","symbol":"009150","company_name":"삼성전기","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_SERVER_FCBGA_CAPACITY_TARGET_WITHOUT_NEAR_TERM_REVENUE_FALSE_STAGE2","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-26","evidence_available_at_that_date":"Samsung Electro-Mechanics announced a 2026 target to lift high-value FCBGA exposure for servers, AI, automotive and networks above 50%, but the event was target/capacity narrative rather than near-term confirmed revenue revision.","evidence_source":"https://m.samsungsem.com/kr/newsroom/news/view.do?id=8381","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv","profile_path":"atlas/symbol_profiles/009/009150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-27","entry_price":143900.0,"MFE_30D_pct":1.39,"MFE_90D_pct":1.39,"MFE_180D_pct":4.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.44,"MAE_90D_pct":-26.69,"MAE_180D_pct":-26.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-17","peak_price":149800.0,"drawdown_after_peak_pct":-27.37,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"post_peak_4B_watch_needed","four_b_evidence_type":["margin_or_backlog_slowdown","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ai_server_fcbga_capacity_target_too_early_high_mae","current_profile_verdict":"current_profile_false_positive_or_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|009150|2024-08-27|143900.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L109_009150_AI_SERVER_FCBGA_TARGET_NO_IMMEDIATE_REVENUE_FALSE_STAGE2_20240826","trigger_id":"C06_R2L109_009150_T1","symbol":"009150","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":52,"relative_strength_score":45,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":55,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":45,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":42,"customer_quality_score":68,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":72,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":59,"stage_label_after":"Stage1/Watch + 4B Watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"A capacity-mix target can be Stage2 watch, but without immediate shipment/revenue/margin conversion it should not be treated as C06 structural unlock.","MFE_90D_pct":1.39,"MAE_90D_pct":-26.69,"score_return_alignment_label":"misaligned","current_profile_verdict":"current_profile_false_positive_or_too_early"}
{"row_type":"aggregate","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","case_count":5,"trigger_count":5,"calibration_usable_trigger_count":5,"positive_case_count":3,"counterexample_count":2,"current_profile_error_count":3,"avg_MFE_90D_pct":48.65,"avg_MAE_90D_pct":-20.23,"avg_MFE_180D_pct":134.57,"avg_MAE_180D_pct":-22.15,"selection_basis":"docs/core/V12_Research_No_Repeat_Index.md","new_independent_case_ratio":1.0}
{"row_type":"shadow_weight","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","rule_scope":"canonical_archetype_specific","rule_candidate":"C06_HBM_ADJACENT_REQUIRES_CUSTOMER_QUALITY_CAPACITY_ALLOCATION_AND_MARGIN_BRIDGE","suggested_direction":"increase_customer_quality_and_capacity_allocation_weight; cap_hbm_adjacent_substrate_proxy_without_margin_bridge","do_not_propose_global_delta":true,"shadow_only":true}
{"row_type":"residual_contribution","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["hbm_adjacent_substrate_proxy_false_stage2","capacity_target_without_revenue_conversion","post_peak_4b_too_late_after_fast_mfe"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R2
completed_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_if_still_below_30 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Evidence URLs are listed in Section 9 and JSONL trigger rows.
- Price shard paths are listed in Section 10 and JSONL trigger rows.

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
