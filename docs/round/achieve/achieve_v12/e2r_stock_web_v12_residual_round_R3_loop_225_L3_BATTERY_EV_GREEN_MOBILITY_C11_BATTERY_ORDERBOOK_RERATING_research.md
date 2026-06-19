# E2R Stock-Web v12 Residual Research — R3 / L3 / C11 Battery Orderbook Rerating
```text
completed_round = R3
completed_loop = 225
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality repair + priority_4 4B/4C path reinforcement
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```
## 1. Selection / novelty check
The latest No-Repeat Index says every C01~C32 canonical archetype is above the 80-row floor, so this run does not try to fill raw row count. It selects a quality-repair loop inside R3/L3 because C11 still has a high counterexample burden and repeated battery-material symbols often blur *nominal orderbook* with actual call-off / utilization / margin conversion.
```text
selected_round: R3
selected_loop: 225
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: C11_ORDERBOOK_TO_CALLOFF_UTILIZATION_SECOND_BRIDGE_GATE_V1
loop_objective:
  residual_false_positive_mining
  4B_non_price_requirement_stress_test
  4C_thesis_break_timing_test
  canonical_archetype_compression

minimum_new_independent_case_ratio: 1.00
new_independent_case_count: 6
new_independent_trigger_count: 6
unique_symbol_count: 6
positive_or_reopen_case_count: 2
counterexample_or_guardrail_count: 4
```
## 2. Price source validation
```text
price_source: Songdaiki/stock-web
price_basis: tradable_raw
upstream_source: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_schema: d,o,h,l,c,v,a,mc,s,m
zero_volume_and_zero_ohlc_rows_excluded: true
corporate_action_contaminated_windows_blocked_by_default: true
```
## 3. Trigger table
| case | symbol | name | trigger | entry | entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak/trough | role |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| C11-225-001 | 247540 | EcoPro BM | Stage2-Actionable | 2024-01-08 | 315500 | 2.38 / -33.12 | 2.38 / -35.82 | 2.38 / -52.87 | 2024-01-08 / 2024-09-10 | counterexample_guardrail |
| C11-225-002 | 066970 | L&F | Stage2 | 2024-01-02 | 205500 | 5.60 / -35.72 | 5.60 / -35.72 | 5.60 / -59.66 | 2024-01-02 / 2024-09-10 | false_positive_counterexample |
| C11-225-003 | 020150 | LOTTE Energy Materials | Stage4B | 2025-01-24 | 23050 | 36.88 / -12.15 | 36.88 / -15.57 | 36.88 / -15.57 | 2025-02-20 / 2025-05-22 | 4B_reopen_watch |
| C11-225-004 | 361610 | SK IE Technology | Stage4C | 2024-04-30 | 59100 | 5.25 / -27.75 | 5.25 / -48.73 | 5.25 / -63.03 | 2024-04-30 / 2025-01-02 | hard_4c_positive_control |
| C11-225-005 | 393890 | WCP | Stage4C | 2024-11-14 | 13170 | 5.85 / -17.69 | 5.85 / -44.27 | 5.85 / -48.75 | 2024-11-14 / 2025-04-09 | hard_4c_positive_control |
| C11-225-006 | 006400 | Samsung SDI | Stage4B | 2024-07-30 | 330500 | 14.98 / -10.89 | 19.06 / -28.74 | 19.06 / -48.56 | 2024-09-30 / 2025-04-09 | 4B_offset_quality_test |

## 4. Case notes
### C11-225-001 — 247540 EcoPro BM — Stage2-Actionable
- **Evidence family:** `long_term_cathode_supply_contract`
- **Evidence summary:** 5-year KRW 43.87tn / $33.4bn high-nickel NCA cathode supply contract with Samsung SDI. Direct orderbook evidence is real, but price path shows orderbook headline alone did not protect entry after EV demand/ASP/call-off pressure.
- **Evidence URL:** https://chargedevs.com/newswire/ecopro-wins-5-year-high-nickel-nca-cathode-material-supply-contract-with-samsung-sdi/
- **Actual entry OHLCV:** `2024-01-08, o=318000, h=323000, l=307000, c=315500, v=1321504`
- **Price result:** 180D MFE/MAE `2.38 / -52.87`, post-peak drawdown `-53.96`.
- **Raw component score breakdown:** EPS 18 / Vis 23 / Bott 16 / Mis 11 / Val 8 / Cap 7 / Info 17 = 100 raw but capped by orderbook-quality guard.

### C11-225-002 — 066970 L&F — Stage2
- **Evidence family:** `customer_contract_start_without_calloff`
- **Evidence summary:** High-nickel cathode contract period began in Jan 2024, but the evidence was contract-size / start-date heavy and lacked realized customer call-off or margin conversion. Later reduction confirms why orderbook quality should be capped until shipments are visible.
- **Evidence URL:** https://www.asiae.co.kr/en/article/2023030714440956645
- **Actual entry OHLCV:** `2024-01-02, o=204500, h=217000, l=200000, c=205500, v=882774`
- **Price result:** 180D MFE/MAE `5.60 / -59.66`, post-peak drawdown `-61.80`.
- **Raw component score breakdown:** EPS 12 / Vis 21 / Bott 12 / Mis 10 / Val 8 / Cap 5 / Info 14 = 82 but Actionable blocked.

### C11-225-003 — 020150 LOTTE Energy Materials — Stage4B
- **Evidence family:** `customer_inventory_adjustment_utilization_recovery`
- **Evidence summary:** FY2024/Q1 run-rate showed customer inventory adjustment, lower utilization, fixed-cost burden, and inventory valuation loss, but the company guided utilization recovery and new supply to North American OEMs / customer JVs.
- **Evidence URL:** https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=138
- **Actual entry OHLCV:** `2025-01-24, o=23150, h=23300, l=22550, c=23050, v=83993`
- **Price result:** 180D MFE/MAE `36.88 / -15.57`, post-peak drawdown `-38.32`.
- **Raw component score breakdown:** EPS 8 / Vis 17 / Bott 12 / Mis 8 / Val 7 / Cap 8 / Info 23 = 83 watch; hard 4C blocked by explicit recovery offset.

### C11-225-004 — 361610 SK IE Technology — Stage4C
- **Evidence family:** `downstream_inventory_adjustment_utilization_collapse`
- **Evidence summary:** 1Q24 earnings shock: revenue -73% QoQ, operating loss W67.4bn, weaker shipments from SK On and lower utilization; offset existed in North America/OEM shipment expectations but near-term thesis break was severe.
- **Evidence URL:** https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220
- **Actual entry OHLCV:** `2024-04-30, o=62100, h=62200, l=58600, c=59100, v=661182`
- **Price result:** 180D MFE/MAE `5.25 / -63.03`, post-peak drawdown `-64.87`.
- **Raw component score breakdown:** EPS 2 / Vis 8 / Bott 9 / Mis 8 / Val 4 / Cap 6 / Info 35 = 72; hard thesis-break route dominates.

### C11-225-005 — 393890 WCP — Stage4C
- **Evidence family:** `separator_customer_rebalancing_and_shipment_stagnation`
- **Evidence summary:** Korean/Japanese separator makers including WCP showed shipment stagnation from reduced European client demand and stock rebalancing; this turns nominal separator orderbook into utilization/call-off risk.
- **Evidence URL:** https://www.sneresearch.com/en/insight/release_view/433/page/96?s_cat=%7C1%7C&s_keyword=
- **Actual entry OHLCV:** `2024-11-14, o=13690, h=13940, l=13170, c=13170, v=203563`
- **Price result:** 180D MFE/MAE `5.85 / -48.75`, post-peak drawdown `-51.58`.
- **Raw component score breakdown:** EPS 3 / Vis 9 / Bott 12 / Mis 8 / Val 4 / Cap 5 / Info 32 = 73; hard 4C/watch favored over Actionable.

### C11-225-006 — 006400 Samsung SDI — Stage4B
- **Evidence family:** `ev_demand_slowdown_ess_customer_offset`
- **Evidence summary:** Q2 2024 operating profit fell on EV demand slowdown, but ESS demand and North American customer projects remained explicit offsets. This is 4B/watch before sticky hard 4C.
- **Evidence URL:** https://www.samsungsdi.com/sdi-now/sdi-news/3862.html
- **Actual entry OHLCV:** `2024-07-30, o=333000, h=344500, l=330500, c=330500, v=423808`
- **Price result:** 180D MFE/MAE `19.06 / -48.56`, post-peak drawdown `-56.80`.
- **Raw component score breakdown:** EPS 8 / Vis 14 / Bott 12 / Mis 9 / Val 8 / Cap 8 / Info 22 = 81 watch; offset quality prevents hard 4C.

## 5. Residual contribution
```text
rule_candidate:
C11_ORDERBOOK_TO_CALLOFF_UTILIZATION_SECOND_BRIDGE_GATE_V1

core residual:
- Battery orderbook / supply-contract headline can create Stage2 or Stage2-Actionable only when the contract is tied to shipment, customer call-off, utilization, realized revenue, margin conversion, or cashflow conversion.
- Contract size alone is a poor Green signal because raw-material price adjustment, customer schedule changes, EV demand slowdown, and utilization collapse can erase the apparent orderbook quality.
- Stage2-Actionable may be preserved for direct named customer contracts, but Stage3-Yellow/Green stays blocked until a second bridge appears.
- Customer inventory adjustment, low utilization, or shipment stagnation routes first to Stage4B/watch when explicit recovery offsets exist; hard 4C requires weak offset quality plus confirmed non-price thesis break.
- High MAE after direct orderbook evidence is an escalation brake, not a Stage2 deletion signal.
```
## 6. Shadow scoring / weight note
```text
do_not_propose_global_weight_delta: true
production_scoring_changed: false
shadow_weight_only: true

current_profile_stress:
- C11 already has heavy Information/Confidence emphasis. This loop does not ask to loosen Green.
- Residual error is not lack of orderbook detection; it is over-crediting nominal contract size without actual call-off/utilization/margin bridge.

shadow_delta_candidate:
C11_BATTERY_ORDERBOOK_RERATING:
  information_confidence: keep high but split into contract_quality_subfactor
  earnings_visibility: +small only when shipment/revenue bridge appears
  bottleneck_pricing: no bonus unless utilization/call-off supports scarcity
  stage3_green: blocked until >=2 evidence families confirm conversion
```
## 7. Machine-readable JSONL rows
```jsonl
{"calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11-225-001", "case_role": "counterexample_guardrail", "corporate_action_contaminated_180D": false, "entry_date": "2024-01-08", "entry_ohlcv": {"c": 315500.0, "h": 323000.0, "l": 307000.0, "m": "KOSDAQ GLOBAL", "o": 318000.0, "v": 1321504}, "entry_price": 315500.0, "evidence_date": "2024-01-08", "evidence_family": "long_term_cathode_supply_contract", "evidence_url": "https://chargedevs.com/newswire/ecopro-wins-5-year-high-nickel-nca-cathode-material-supply-contract-with-samsung-sdi/", "fine_archetype_id": "C11_ORDERBOOK_TO_CALLOFF_UTILIZATION_SECOND_BRIDGE_GATE_V1", "insufficient_forward_window_180D": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mae_180": -52.87, "mae_30": -33.12, "mae_90": -35.82, "mfe_180": 2.38, "mfe_30": 2.38, "mfe_90": 2.38, "name": "EcoPro BM", "peak_180_date": "2024-01-08", "post_peak_drawdown_180": -53.96, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "production_scoring_changed": false, "profile_error_label": "orderbook_headline_without_calloff_or_utilization_bridge", "row_type": "trigger", "selected_loop": 225, "selected_round": "R3", "shadow_weight_only": true, "symbol": "247540", "trigger_type": "Stage2-Actionable", "trough_180_date": "2024-09-10"}
{"calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11-225-002", "case_role": "false_positive_counterexample", "corporate_action_contaminated_180D": false, "entry_date": "2024-01-02", "entry_ohlcv": {"c": 205500.0, "h": 217000.0, "l": 200000.0, "m": "KOSDAQ GLOBAL", "o": 204500.0, "v": 882774}, "entry_price": 205500.0, "evidence_date": "2024-01-02", "evidence_family": "customer_contract_start_without_calloff", "evidence_url": "https://www.asiae.co.kr/en/article/2023030714440956645", "fine_archetype_id": "C11_ORDERBOOK_TO_CALLOFF_UTILIZATION_SECOND_BRIDGE_GATE_V1", "insufficient_forward_window_180D": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mae_180": -59.66, "mae_30": -35.72, "mae_90": -35.72, "mfe_180": 5.6, "mfe_30": 5.6, "mfe_90": 5.6, "name": "L&F", "peak_180_date": "2024-01-02", "post_peak_drawdown_180": -61.8, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "production_scoring_changed": false, "profile_error_label": "orderbook_headline_without_calloff_or_utilization_bridge", "row_type": "trigger", "selected_loop": 225, "selected_round": "R3", "shadow_weight_only": true, "symbol": "066970", "trigger_type": "Stage2", "trough_180_date": "2024-09-10"}
{"calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11-225-003", "case_role": "4B_reopen_watch", "corporate_action_contaminated_180D": false, "entry_date": "2025-01-24", "entry_ohlcv": {"c": 23050.0, "h": 23300.0, "l": 22550.0, "m": "KOSPI", "o": 23150.0, "v": 83993}, "entry_price": 23050.0, "evidence_date": "2025-01-24", "evidence_family": "customer_inventory_adjustment_utilization_recovery", "evidence_url": "https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=138", "fine_archetype_id": "C11_ORDERBOOK_TO_CALLOFF_UTILIZATION_SECOND_BRIDGE_GATE_V1", "insufficient_forward_window_180D": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mae_180": -15.57, "mae_30": -12.15, "mae_90": -15.57, "mfe_180": 36.88, "mfe_30": 36.88, "mfe_90": 36.88, "name": "LOTTE Energy Materials", "peak_180_date": "2025-02-20", "post_peak_drawdown_180": -38.32, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "production_scoring_changed": false, "profile_error_label": "4B_4C_offset_quality_boundary", "row_type": "trigger", "selected_loop": 225, "selected_round": "R3", "shadow_weight_only": true, "symbol": "020150", "trigger_type": "Stage4B", "trough_180_date": "2025-05-22"}
{"calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11-225-004", "case_role": "hard_4c_positive_control", "corporate_action_contaminated_180D": false, "entry_date": "2024-04-30", "entry_ohlcv": {"c": 59100.0, "h": 62200.0, "l": 58600.0, "m": "KOSPI", "o": 62100.0, "v": 661182}, "entry_price": 59100.0, "evidence_date": "2024-04-30", "evidence_family": "downstream_inventory_adjustment_utilization_collapse", "evidence_url": "https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220", "fine_archetype_id": "C11_ORDERBOOK_TO_CALLOFF_UTILIZATION_SECOND_BRIDGE_GATE_V1", "insufficient_forward_window_180D": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mae_180": -63.03, "mae_30": -27.75, "mae_90": -48.73, "mfe_180": 5.25, "mfe_30": 5.25, "mfe_90": 5.25, "name": "SK IE Technology", "peak_180_date": "2024-04-30", "post_peak_drawdown_180": -64.87, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "production_scoring_changed": false, "profile_error_label": "4B_4C_offset_quality_boundary", "row_type": "trigger", "selected_loop": 225, "selected_round": "R3", "shadow_weight_only": true, "symbol": "361610", "trigger_type": "Stage4C", "trough_180_date": "2025-01-02"}
{"calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11-225-005", "case_role": "hard_4c_positive_control", "corporate_action_contaminated_180D": false, "entry_date": "2024-11-14", "entry_ohlcv": {"c": 13170.0, "h": 13940.0, "l": 13170.0, "m": "KOSDAQ GLOBAL", "o": 13690.0, "v": 203563}, "entry_price": 13170.0, "evidence_date": "2024-11-14", "evidence_family": "separator_customer_rebalancing_and_shipment_stagnation", "evidence_url": "https://www.sneresearch.com/en/insight/release_view/433/page/96?s_cat=%7C1%7C&s_keyword=", "fine_archetype_id": "C11_ORDERBOOK_TO_CALLOFF_UTILIZATION_SECOND_BRIDGE_GATE_V1", "insufficient_forward_window_180D": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mae_180": -48.75, "mae_30": -17.69, "mae_90": -44.27, "mfe_180": 5.85, "mfe_30": 5.85, "mfe_90": 5.85, "name": "WCP", "peak_180_date": "2024-11-14", "post_peak_drawdown_180": -51.58, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "production_scoring_changed": false, "profile_error_label": "4B_4C_offset_quality_boundary", "row_type": "trigger", "selected_loop": 225, "selected_round": "R3", "shadow_weight_only": true, "symbol": "393890", "trigger_type": "Stage4C", "trough_180_date": "2025-04-09"}
{"calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11-225-006", "case_role": "4B_offset_quality_test", "corporate_action_contaminated_180D": false, "entry_date": "2024-07-30", "entry_ohlcv": {"c": 330500.0, "h": 344500.0, "l": 330500.0, "m": "KOSPI", "o": 333000.0, "v": 423808}, "entry_price": 330500.0, "evidence_date": "2024-07-30", "evidence_family": "ev_demand_slowdown_ess_customer_offset", "evidence_url": "https://www.samsungsdi.com/sdi-now/sdi-news/3862.html", "fine_archetype_id": "C11_ORDERBOOK_TO_CALLOFF_UTILIZATION_SECOND_BRIDGE_GATE_V1", "insufficient_forward_window_180D": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "mae_180": -48.56, "mae_30": -10.89, "mae_90": -28.74, "mfe_180": 19.06, "mfe_30": 14.98, "mfe_90": 19.06, "name": "Samsung SDI", "peak_180_date": "2024-09-30", "post_peak_drawdown_180": -56.8, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "production_scoring_changed": false, "profile_error_label": "4B_4C_offset_quality_boundary", "row_type": "trigger", "selected_loop": 225, "selected_round": "R3", "shadow_weight_only": true, "symbol": "006400", "trigger_type": "Stage4B", "trough_180_date": "2025-04-09"}
```
## 8. Batch Ingest Self-Audit
```text
ready_for_batch_ingest: true
filename_matches_required_regex: true
metadata_round_matches_filename: true
metadata_loop_matches_filename: true
round_sector_consistency: pass
selected_canonical_archetype_present: true
all_trigger_rows_have_entry_date: true
all_trigger_rows_have_entry_price: true
all_trigger_rows_have_30_90_180_mfe_mae: true
all_trigger_rows_use_stock_web_price_source: true
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
source_proxy_only_count: 1
evidence_url_pending_count: 0
production_scoring_changed: false
shadow_weight_only: true
```
## 9. Deferred Coding Agent Handoff Prompt — do not execute in this research run
```text
Use this MD only as a batch calibration input. Do not patch production scoring from this file alone. When enough C11 rows confirm the same residual, implement a scoped canonical-archetype guard that requires shipment/call-off/utilization/margin bridge before allowing Stage3-Yellow/Green from battery orderbook evidence. Preserve Stage2 for direct named-customer contracts.
```
## 10. Next Research State
```text
completed_round = R3
completed_loop = 225
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality repair + priority_4 4B/4C path reinforcement
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
