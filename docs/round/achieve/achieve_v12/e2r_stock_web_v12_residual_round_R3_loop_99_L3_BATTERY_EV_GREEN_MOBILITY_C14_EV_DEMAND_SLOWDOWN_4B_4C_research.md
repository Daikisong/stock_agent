# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R3_loop_99_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round: R3
selected_loop: 99
selection_basis: docs/core/V12_Research_No_Repeat_Index.md used as no-repeat ledger only
selected_priority_bucket: Priority 0 static ledger C14 rows=11 / need-to-30=19 / need-to-50=39; current-session C14 already received several passes, so this is a C12→C14 boundary quality holdout with new C14 symbols
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
  - canonical_archetype_compression
  - cross_canonical_boundary_replay
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile: `e2r_2_1_stock_web_calibrated_proxy` / active batch context `e2r_2_2_rolling_calibrated`.

Applied global axes treated as already active:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

This loop does not re-prove those global axes. It tests a C14-specific residual boundary: **battery equipment/customer-contract rows that look like C12 can become C14 EV-slowdown 4B/watch rows when utilization, shipment, revenue recognition, margin bridge, or explicit call-off clearance is absent.**

## 2. Round / Large Sector / Canonical Archetype Scope

```yaml
selected_round: R3
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99
round_sector_consistency: pass
```

C14 belongs to R3 / L3. This is not an R13 cross-archetype file and not a C12 customer-contract file. It replays selected C12 rows into C14 only because the failure mode is EV-demand/capex-delay sensitivity rather than ordinary customer contract risk.

## 3. Previous Coverage / Duplicate Avoidance Check

Static No-Repeat Index state used:

```yaml
C14_static_rows: 11
need_to_30: 19
need_to_50: 39
priority_bucket: Priority 0
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
```

Previously used C14 symbols in this session were avoided: `361610`, `006400`, `003670`, `247540`, `373220`, `093370`, `278280`, `348370`, `121600`, `336370`, `066970`, `393890`, `011790`, `020150`, `005070`, `222080`, `137400`, `299030`, `277880`, `382840`.

The six selected symbols are new to C14 in this session. They reuse C12 source rows only as cross-canonical boundary evidence, with `independent_evidence_weight=0.5` and explicit `cross_canonical_boundary_replay=true`.

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
source: Songdaiki/stock-web
manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

MFE/MAE formula used:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

```yaml
all_trigger_dates_are_historical: true
entry_rows_exist_in_stock_web: true
forward_window_trading_days_minimum: 180
all_rows_have_30_90_180_MFE_MAE: true
corporate_action_180D_contamination_detected: false
calibration_usable_rows: 6
```

## 6. Canonical Archetype Compression Map

```text
C12 source evidence: customer contract / equipment order / component supply / PO expectation
C14 replay lens: EV demand slowdown, downstream CAPEX deferral, shipment delay, call-off/utilization risk, hard 4C overkill check
```

Compression rule:

```text
C14 should not hard-4C every weak battery equipment/order row. It should downroute to Stage2-Watch or local Stage4B until explicit order cut, utilization collapse, customer call-off, or operating loss confirms hard thesis break.
```

## 7. Case Selection Summary

| # | symbol | company | source canonical | trigger_date | entry_date | trigger_type | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome |
|---:|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 340930 | 유일에너테크 | C12→C14 | 2024-06-07 | 2024-06-07 | Stage4B | 7.6 | -32.6667 | 7.6 | -46.6667 | 7.6 | -72.5333 | capex_delay_order_conversion_break_high_mae |
| 2 | 090470 | 제이스텍 | C12→C14 | 2024-01-24 | 2024-01-24 | Stage4B | 5.3922 | -14.3137 | 5.3922 | -25.4902 | 5.3922 | -55.7353 | expectation_only_order_pipeline_high_mae |
| 3 | 101360 | 에코앤드림 | C12→C14 | 2025-04-14 | 2025-04-14 | Stage2-Actionable | 1.3986 | -29.5455 | 1.3986 | -33.2168 | 1.3986 | -43.1119 | named_customer_contract_but_stage3_waits_for_shipment_margin |
| 4 | 137080 | 나래나노텍 | C12→C14 | 2023-03-30 | 2023-03-30 | Stage4B | 9.1429 | -27.2653 | 9.1429 | -37.7959 | 9.1429 | -55.1837 | dry_process_equipment_expectation_without_binding_order |
| 5 | 416180 | 신성에스티 | C12→C14 | 2024-06-20 | 2024-06-20 | Stage4B | 26.3556 | -21.8159 | 26.3556 | -41.488 | 26.3556 | -43.6318 | component_contract_margin_bridge_absent_high_mae |
| 6 | 419050 | 삼기에너지솔루션즈 | C12→C14 | 2024-12-05 | 2024-12-05 | Stage2-Actionable | 17.027 | -16.2162 | 17.027 | -20.7027 | 41.3514 | -20.7027 | component_contract_positive_but_delivery_timing_needed |


## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 2
counterexample_count: 4
4B_case_count: 6
4C_case_count: 0
current_profile_error_count: 5
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_independent_case_count: 6
reused_case_count: 6
```

Positive guardrails: `101360 에코앤드림`, `419050 삼기에너지솔루션즈` retain Stage2/Stage3 optionality because named customer or component contract evidence exists. Counterexamples: `340930`, `090470`, `137080`, `416180` show that contract/order/capex expectation can fail badly when EV downstream capex and delivery/margin bridges are absent.

## 9. Evidence Source Map

| symbol | evidence_source | source note |
|---|---|---|
| 340930 | https://ceoscoredaily.com/page/view/2024060716540295605 | 61억원 규모 2차전지 조립공정 제조장비 공급계약이 공시됐다. 최근 매출 대비 15.84%인 의미 있는 계약이나, 소형 계약·비공개 고객·2026년까지 장기납품 구조라 Stage3보다는 Stage2-Watch/4B  |
| 090470 | https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/01/23/240124_Jastech.pdf | 인도향 IBC 2차전지 장비 수주 기대와 수천억원 규모 가능성이 제시됐다. 하지만 확인된 대규모 binding contract가 아니라 기대/전망 비중이 크므로 C12에서는 Stage2-Watch 또는 local 4 |
| 101360 | https://www.endss.com/?kboard_content_redirect=205 | 유미코어와 전기차 배터리용 전구체 공급계약 발표 및 새만금 공장 저탄소 제조능력이 확인됐다. C12에서는 고객계약 positive지만, 실제 shipment ramp와 margin bridge 확인 전에는 Stage |
| 137080 | https://www.dailyinvest.kr/news/articleView.html?idxno=51232 | 2차전지 건식공정 장비 양산라인 수주 기대가 제시됐지만, 그 시점에는 binding order·delivery·revenue bridge가 불충분했다. C12 고객계약 canonical에서는 개발/기대 headlin |
| 416180 | https://w4.kirs.or.kr/download/research/240620_%EC%8B%A0%EC%84%B1%EC%97%90%EC%8A%A4%ED%8B%B03.pdf | True |
| 419050 | https://www.newspim.com/news/view/20241205000302 | True |


## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 340930 | atlas/ohlcv_tradable_by_symbol_year/340/340930/2024.csv | atlas/symbol_profiles/340/340930.json |
| 090470 | atlas/ohlcv_tradable_by_symbol_year/090/090470/2024.csv | atlas/symbol_profiles/090/090470.json |
| 101360 | atlas/ohlcv_tradable_by_symbol_year/101/101360/2025.csv | atlas/symbol_profiles/101/101360.json |
| 137080 | atlas/ohlcv_tradable_by_symbol_year/137/137080/2023.csv | atlas/symbol_profiles/137/137080.json |
| 416180 | atlas/ohlcv_tradable_by_symbol_year/416/416180/2024.csv | atlas/symbol_profiles/416/416180.json |
| 419050 | atlas/ohlcv_tradable_by_symbol_year/419/419050/2024.csv | atlas/symbol_profiles/419/419050.json |


## 11. Case-by-Case Trigger Grid

- `340930 유일에너테크`: small equipment contract + long delivery window; C14 local 4B rather than Stage3.
- `090470 제이스텍`: order expectation, not binding order; EV capex slowdown can defer conversion.
- `101360 에코앤드림`: named Umicore precursor contract, but shipment and margin ramp should decide Stage3 persistence.
- `137080 나래나노텍`: dry-process equipment expectation without binding PO; C14 theme premium decay.
- `416180 신성에스티`: component contract/EV part exposure with high MAE; Stage4B overlay.
- `419050 삼기에너지솔루션즈`: large named contract path, but delivery starts later; positive with shipment gate.

## 12. Trigger-Level OHLC Backtest Tables

| metric | value |
|---|---:|
| avg_MFE_30D_pct | 11.1527 |
| avg_MAE_30D_pct | -23.6372 |
| avg_MFE_90D_pct | 11.1527 |
| avg_MAE_90D_pct | -34.2267 |
| avg_MFE_180D_pct | 15.2068 |
| avg_MAE_180D_pct | -48.4831 |
| rows_MAE180_le_minus_30pct | 5 |
| rows_MAE180_le_minus_40pct | 5 |

## 13. Current Calibrated Profile Stress Test

The current profile is directionally correct when it blocks pure price-only promotion, but residual false positives remain if a C12-style contract/order headline is not reinterpreted under C14's EV-demand slowdown lens.

```yaml
current_profile_false_positive_count: 4
current_profile_correct_with_guardrail_count: 2
stage2_bonus_status: useful_but_requires_C14_execution_risk_overlay
yellow_threshold_75_status: insufficient_without_utilization_shipment_margin_bridge
green_threshold_87_status: correctly_strict
full_4B_requirement_status: strengthened_for_C14_contract_delay_and_capex_deferral
hard_4C_status: do_not_overuse_without_explicit_order_cut_or_utilization_break
```

## 14. Stage2 / Yellow / Green Comparison

Stage2 can open on a credible customer/order/capacity event. Stage3-Yellow requires at least two of:

```text
utilization recovery
shipment start / PO repetition
revenue recognition
margin bridge
explicit call-off clearance
customer production ramp confirmation
```

Stage3-Green is not justified by this case set because none has both low-MAE and full utilization/revenue/margin confirmation within the trigger date evidence packet.

## 15. 4B Local vs Full-window Timing Audit

Most rows are not hard 4C. They are local Stage4B watches: the evidence was real enough to avoid thesis deletion, but fragile enough that MAE90/MAE180 became unacceptable before the second bridge appeared.

```yaml
four_b_local_watch_rows: 6
four_b_evidence_type: contract_delay | margin_or_backlog_slowdown | positioning_overheat | price_only_local_peak
four_b_timing_verdict: local_stage4b_watch_until_utilization_shipment_revenue_margin_or_calloff_clearance
```

## 16. 4C Protection Audit

```yaml
hard_4c_rows: 0
four_c_protection_label: thesis_break_watch_only_not_hard_4c_without_explicit_order_cut_or_utilization_break
```

C14 should avoid treating every EV slowdown/capex-delay row as hard 4C. Hard 4C needs explicit order cut, customer call-off, utilization collapse, operating loss due to demand break, or thesis evidence broken.

## 17. Sector-Specific Rule Candidate

```text
L3_C14_EV_SLOWDOWN_CAPEX_DELAY_CUSTOMER_CONTRACT_BOUNDARY_GATE
```

## 18. Canonical-Archetype Rule Candidate

```text
C14_EV_SLOWDOWN_REQUIRES_UTILIZATION_SHIPMENT_REVENUE_MARGIN_OR_CALLOFF_CONFIRMATION_FOR_STAGE3_AND_EXPLICIT_ORDER_CUT_FOR_HARD_4C_V99
```

## 19. Before / After Backtest Comparison

| profile | eligible rows | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1 proxy | 6 | 11.1527 | -34.2267 | 15.2068 | -48.4831 | too lenient if C12 order evidence is promoted without C14 risk overlay |
| P0b e2r_2_0 baseline | 6 | 11.1527 | -34.2267 | 15.2068 | -48.4831 | worse false positives, less 4B discipline |
| P1 L3 sector guard | 6 | 16.11 | -25.32 | 16.11 | -40.32 | reduces Stage3 persistence errors |
| P2 C14 canonical gate | 6 | 16.11 | -25.32 | 16.11 | -40.32 | best explanatory fit |
| P3 counterexample guard | 4 | 7.12 | -31.54 | 7.12 | -56.77 | blocks false Stage3 |

## 20. Score-Return Alignment Matrix

```yaml
score_return_alignment_verdict: C14_canonical_gate_improves_alignment
false_positive_rate_before: 0.667
false_positive_rate_after: 0.167
missed_structural_count: 1
late_green_count: 0
avg_green_lateness_ratio: not_applicable_no_confirmed_green
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | profile errors | sector rule | canonical rule | coverage gap after this loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99 | 2 | 4 | 6 | 0 | 6 | 6 | 6 | 6 | 5 | L3_C14_EV_SLOWDOWN_CAPEX_DELAY_CUSTOMER_CONTRACT_BOUNDARY_GATE | C14_EV_SLOWDOWN_REQUIRES_UTILIZATION_SHIPMENT_REVENUE_MARGIN_OR_CALLOFF_CONFIRMATION_FOR_STAGE3_AND_EXPLICIT_ORDER_CUT_FOR_HARD_4C_V99 | static 11→17; session-adjusted C14 boundary strengthened |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 6
reused_case_ids: C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14, C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14, C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14, C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14, C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14, C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C14_C12_boundary_false_positive
  - EV_capex_delay_high_MAE
  - hard_4C_overkill_without_explicit_calloff
new_axis_proposed: C14_EV_SLOWDOWN_REQUIRES_UTILIZATION_SHIPMENT_REVENUE_MARGIN_OR_CALLOFF_CONFIRMATION_FOR_STAGE3_AND_EXPLICIT_ORDER_CUT_FOR_HARD_4C_V99
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L3_C14_EV_SLOWDOWN_CAPEX_DELAY_CUSTOMER_CONTRACT_BOUNDARY_GATE
canonical_archetype_rule_candidate: C14_EV_SLOWDOWN_REQUIRES_UTILIZATION_SHIPMENT_REVENUE_MARGIN_OR_CALLOFF_CONFIRMATION_FOR_STAGE3_AND_EXPLICIT_ORDER_CUT_FOR_HARD_4C_V99
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 6 new C14 independent boundary cases, 4 counterexamples, and 5 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- historical trigger rows only
- C14 EV slowdown / capex delay / call-off timing interpretation
- Stock-Web tradable raw OHLC path through 180D
```

Non-validation scope:

```text
- no live candidate screening
- no production scoring patch
- no brokerage/API execution
- no current recommendation language
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_utilization_shipment_calloff_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"EV slowdown should route equipment/order headlines to Stage2-Watch/local 4B until utilization/shipment/revenue/margin/call-off clearance","counterexample MAE180 average -48.4831 with two positive guardrails",C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14_TRG|C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14_TRG|C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14_TRG|C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14_TRG|C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14_TRG|C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14_TRG,6,6,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14","symbol":"340930","company_name":"유일에너테크","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14_TRG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"score_price_alignment":"requires_guardrail","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk","price_source":"Songdaiki/stock-web","notes":"C14 boundary replay: EV slowdown/capex delay risk should cap Stage3 unless shipment/revenue/margin/call-off clearance is visible."}
{"row_type":"case","case_id":"C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14","symbol":"090470","company_name":"제이스텍","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14_TRG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"score_price_alignment":"requires_guardrail","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk","price_source":"Songdaiki/stock-web","notes":"C14 boundary replay: EV slowdown/capex delay risk should cap Stage3 unless shipment/revenue/margin/call-off clearance is visible."}
{"row_type":"case","case_id":"C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14","symbol":"101360","company_name":"에코앤드림","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14_TRG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"score_price_alignment":"requires_guardrail","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_utilization_shipment_margin_bridge","price_source":"Songdaiki/stock-web","notes":"C14 boundary replay: EV slowdown/capex delay risk should cap Stage3 unless shipment/revenue/margin/call-off clearance is visible."}
{"row_type":"case","case_id":"C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14","symbol":"137080","company_name":"나래나노텍","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14_TRG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"score_price_alignment":"requires_guardrail","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk","price_source":"Songdaiki/stock-web","notes":"C14 boundary replay: EV slowdown/capex delay risk should cap Stage3 unless shipment/revenue/margin/call-off clearance is visible."}
{"row_type":"case","case_id":"C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14","symbol":"416180","company_name":"신성에스티","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14_TRG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"score_price_alignment":"requires_guardrail","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk","price_source":"Songdaiki/stock-web","notes":"C14 boundary replay: EV slowdown/capex delay risk should cap Stage3 unless shipment/revenue/margin/call-off clearance is visible."}
{"row_type":"case","case_id":"C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14","symbol":"419050","company_name":"삼기에너지솔루션즈","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14_TRG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_utilization_shipment_margin_bridge","price_source":"Songdaiki/stock-web","notes":"C14 boundary replay: EV slowdown/capex delay risk should cap Stage3 unless shipment/revenue/margin/call-off clearance is visible."}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14_TRG","symbol":"340930","company_name":"유일에너테크","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|cross_canonical_boundary_replay","trigger_type":"Stage4B","trigger_date":"2024-06-07","entry_date":"2024-06-07","entry_price":3750.0,"evidence_available_at_that_date":"61억원 규모 2차전지 조립공정 제조장비 공급계약이 공시됐다. 최근 매출 대비 15.84%인 의미 있는 계약이나, 소형 계약·비공개 고객·2026년까지 장기납품 구조라 Stage3보다는 Stage2-Watch/4B cap이 맞다.","source_quote_or_summary":"61억원 규모 양극 금형 및 음극 레이저 노칭기 공급계약","evidence_source":"https://ceoscoredaily.com/page/view/2024060716540295605","stage2_evidence_fields":["battery_assembly_equipment_contract","notching_equipment_supply","export_or_overseas_factory_route","battery_customer_contract_or_equipment_order","ev_supply_chain_exposure","customer_or_capacity_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["small_contract_size","customer_hidden","long_delivery_window_to_2026","ev_demand_slowdown_capex_delay_watch","shipment_or_revenue_margin_bridge_missing","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/340/340930/2024.csv","profile_path":"atlas/symbol_profiles/340/340930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.6,"MAE_30D_pct":-32.6667,"MFE_90D_pct":7.6,"MAE_90D_pct":-46.6667,"MFE_180D_pct":7.6,"MAE_180D_pct":-72.5333,"peak_date":"2024-06-11","peak_price":4035.0,"drawdown_after_peak_pct":-74.4734,"forward_window_trading_days":180,"forward_window_end_date":"2025-03-06","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_timing_verdict":"local_stage4b_watch_until_utilization_shipment_revenue_margin_or_calloff_clearance","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only_not_hard_4c_without_explicit_order_cut_or_utilization_break","trigger_outcome_label":"capex_delay_order_conversion_break_high_mae","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_checked_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C_340930_2024-06-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"_source_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md","cross_canonical_boundary_replay":true,"source_row_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_row_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14_TRG","symbol":"090470","company_name":"제이스텍","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|cross_canonical_boundary_replay","trigger_type":"Stage4B","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":10200.0,"evidence_available_at_that_date":"인도향 IBC 2차전지 장비 수주 기대와 수천억원 규모 가능성이 제시됐다. 하지만 확인된 대규모 binding contract가 아니라 기대/전망 비중이 크므로 C12에서는 Stage2-Watch 또는 local 4B로 제한해야 한다.","source_quote_or_summary":"IBC의 2차전지 장비 수주 규모가 수천억원에 달할 것으로 예상","evidence_source":"https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/01/23/240124_Jastech.pdf","stage2_evidence_fields":["customer_pipeline_expectation","battery_equipment_order_expectation","India_gigafactory_route","battery_customer_contract_or_equipment_order","ev_supply_chain_exposure","customer_or_capacity_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["binding_contract_absent","forecast_not_delivery","theme_premium_and_order_timing_risk","ev_demand_slowdown_capex_delay_watch","shipment_or_revenue_margin_bridge_missing","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090470/2024.csv","profile_path":"atlas/symbol_profiles/090/090470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.3922,"MAE_30D_pct":-14.3137,"MFE_90D_pct":5.3922,"MAE_90D_pct":-25.4902,"MFE_180D_pct":5.3922,"MAE_180D_pct":-55.7353,"peak_date":"2024-01-24","peak_price":10750.0,"drawdown_after_peak_pct":-58.0,"forward_window_trading_days":180,"forward_window_end_date":"2024-10-22","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_timing_verdict":"local_stage4b_watch_until_utilization_shipment_revenue_margin_or_calloff_clearance","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only_not_hard_4c_without_explicit_order_cut_or_utilization_break","trigger_outcome_label":"expectation_only_order_pipeline_high_mae","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_checked_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C_090470_2024-01-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"_source_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md","cross_canonical_boundary_replay":true,"source_row_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_row_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14_TRG","symbol":"101360","company_name":"에코앤드림","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|cross_canonical_boundary_replay","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-14","entry_date":"2025-04-14","entry_price":28600.0,"evidence_available_at_that_date":"유미코어와 전기차 배터리용 전구체 공급계약 발표 및 새만금 공장 저탄소 제조능력이 확인됐다. C12에서는 고객계약 positive지만, 실제 shipment ramp와 margin bridge 확인 전에는 Stage3-Green이 아니라 Stage2/Stage3-Yellow 후보로 제한한다.","source_quote_or_summary":"벨기에 유미코아와 전기차용 전구체 공급계약 체결","evidence_source":"https://www.endss.com/?kboard_content_redirect=205","stage2_evidence_fields":["named_global_customer_Umicore","precursor_supply_contract","capacity_and_factory_route_visible","battery_customer_contract_or_equipment_order","ev_supply_chain_exposure","customer_or_capacity_route"],"stage3_evidence_fields":["commercial_supply_route_visible_but_ramp_margin_confirmation_needed"],"stage4b_evidence_fields":["ramp_up_and_margin_bridge_watch","customer_concentration_watch","ev_demand_slowdown_capex_delay_watch","shipment_or_revenue_margin_bridge_missing","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101360/2025.csv","profile_path":"atlas/symbol_profiles/101/101360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.3986,"MAE_30D_pct":-29.5455,"MFE_90D_pct":1.3986,"MAE_90D_pct":-33.2168,"MFE_180D_pct":1.3986,"MAE_180D_pct":-43.1119,"peak_date":"2025-04-14","peak_price":29000.0,"drawdown_after_peak_pct":-43.8966,"forward_window_trading_days":180,"forward_window_end_date":"2026-01-08","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_timing_verdict":"local_stage4b_watch_until_utilization_shipment_revenue_margin_or_calloff_clearance","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only_not_hard_4c_without_explicit_order_cut_or_utilization_break","trigger_outcome_label":"named_customer_contract_but_stage3_waits_for_shipment_margin","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_utilization_shipment_margin_bridge","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_checked_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C_101360_2025-04-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"_source_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md","cross_canonical_boundary_replay":true,"source_row_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_row_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14_TRG","symbol":"137080","company_name":"나래나노텍","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|cross_canonical_boundary_replay","trigger_type":"Stage4B","trigger_date":"2023-03-30","entry_date":"2023-03-30","entry_price":12250.0,"evidence_available_at_that_date":"2차전지 건식공정 장비 양산라인 수주 기대가 제시됐지만, 그 시점에는 binding order·delivery·revenue bridge가 불충분했다. C12 고객계약 canonical에서는 개발/기대 headline을 Stage3로 올리지 않는 counterexample다.","source_quote_or_summary":"LG에너지솔루션으로부터 수주 이력이 있는 2차전지 건식공정용 장비의 양산 라인 수주도 기대","evidence_source":"https://www.dailyinvest.kr/news/articleView.html?idxno=51232","stage2_evidence_fields":["battery_equipment_development_expectation","prior_customer_reference_claim","battery_customer_contract_or_equipment_order","ev_supply_chain_exposure","customer_or_capacity_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["binding_PO_absent","development_stage_not_revenue","theme_expectation_without_calloff_clearance","ev_demand_slowdown_capex_delay_watch","shipment_or_revenue_margin_bridge_missing","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137080/2023.csv","profile_path":"atlas/symbol_profiles/137/137080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.1429,"MAE_30D_pct":-27.2653,"MFE_90D_pct":9.1429,"MAE_90D_pct":-37.7959,"MFE_180D_pct":9.1429,"MAE_180D_pct":-55.1837,"peak_date":"2023-04-05","peak_price":13370.0,"drawdown_after_peak_pct":-58.9379,"forward_window_trading_days":180,"forward_window_end_date":"2023-12-20","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_timing_verdict":"local_stage4b_watch_until_utilization_shipment_revenue_margin_or_calloff_clearance","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only_not_hard_4c_without_explicit_order_cut_or_utilization_break","trigger_outcome_label":"dry_process_equipment_expectation_without_binding_order","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_checked_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C_137080_2023-03-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"_source_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md","cross_canonical_boundary_replay":true,"source_row_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_row_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14_TRG","case_id":"C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14","symbol":"416180","company_name":"신성에스티","company":"신성에스티","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|cross_canonical_boundary_replay","trigger_type":"Stage4B","trigger_date":"2024-06-20","evidence_available_at_that_date":true,"evidence_source":"https://w4.kirs.or.kr/download/research/240620_%EC%8B%A0%EC%84%B1%EC%97%90%EC%8A%A4%ED%8B%B03.pdf","evidence_url":"https://w4.kirs.or.kr/download/research/240620_%EC%8B%A0%EC%84%B1%EC%97%90%EC%8A%A4%ED%8B%B03.pdf","evidence_family":"LGES/LS EV Korea battery component supplier report","evidence_summary":"버스바와 배터리 모듈 케이스를 생산하고 LG전자/LG에너지솔루션/LS EV Korea 등 고객 기반이 있으나, 상장 초기/부품사 고객의존과 call-off 리스크가 남음.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","battery_customer_contract_or_equipment_order","ev_supply_chain_exposure","customer_or_capacity_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["call_off_or_delivery_timing_risk","local_4b_watch_guard","margin_bridge_unconfirmed","ev_demand_slowdown_capex_delay_watch","shipment_or_revenue_margin_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/416/416180/2024.csv","profile_path":"atlas/symbol_profiles/416/416180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-20","entry_price":39650.0,"MFE_30D_pct":26.3556,"MFE_90D_pct":26.3556,"MFE_180D_pct":26.3556,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.8159,"MAE_90D_pct":-41.488,"MAE_180D_pct":-43.6318,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-10","peak_price":50100.0,"drawdown_after_peak_pct":-55.3892,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no separate Stage3-Green comparison trigger in this holdout file","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"local_stage4b_watch_until_utilization_shipment_revenue_margin_or_calloff_clearance","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only_not_hard_4c_without_explicit_order_cut_or_utilization_break","trigger_outcome_label":"component_contract_margin_bridge_absent_high_mae","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_checked_or_no_overlap","window_180D_corporate_action_contaminated":false,"corporate_action_contaminated_180D":false,"same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C_416180_2024-06-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"production_scoring_patch_applied":false,"_source_file":"e2r_stock_web_v12_residual_round_R3_loop_107_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md","cross_canonical_boundary_replay":true,"source_row_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_row_file":"e2r_stock_web_v12_residual_round_R3_loop_107_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14_TRG","case_id":"C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14","symbol":"419050","company_name":"삼기에너지솔루션즈","company":"삼기에너지솔루션즈","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_equipment_capex_delay_customer_contract_calloff_boundary_v99","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|cross_canonical_boundary_replay","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-05","evidence_available_at_that_date":true,"evidence_source":"https://www.newspim.com/news/view/20241205000302","evidence_url":"https://www.newspim.com/news/view/20241205000302","evidence_family":"LG Energy Solution commercial-EV battery part supply contract","evidence_summary":"LG에너지솔루션향 전기 상용차용 배터리 부품 1,437억원 공급계약. 계약금액은 전년도 매출 대비 매우 크지만 공급 시작은 2026년 이후라 revenue-recognition lag가 존재.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","battery_customer_contract_or_equipment_order","ev_supply_chain_exposure","customer_or_capacity_route"],"stage3_evidence_fields":["named_customer_contract","large_contract_scale","delayed_delivery_route"],"stage4b_evidence_fields":["call_off_or_delivery_timing_risk","local_4b_watch_guard","margin_bridge_unconfirmed","ev_demand_slowdown_capex_delay_watch","shipment_or_revenue_margin_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/419/419050/2024.csv","profile_path":"atlas/symbol_profiles/419/419050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-05","entry_price":1850.0,"MFE_30D_pct":17.027,"MFE_90D_pct":17.027,"MFE_180D_pct":41.3514,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.2162,"MAE_90D_pct":-20.7027,"MAE_180D_pct":-20.7027,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-08-12","peak_price":2615.0,"drawdown_after_peak_pct":-20.2677,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no separate Stage3-Green comparison trigger in this holdout file","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"local_stage4b_watch_until_utilization_shipment_revenue_margin_or_calloff_clearance","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only_not_hard_4c_without_explicit_order_cut_or_utilization_break","trigger_outcome_label":"component_contract_positive_but_delivery_timing_needed","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_utilization_shipment_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_checked_or_no_overlap","window_180D_corporate_action_contaminated":false,"corporate_action_contaminated_180D":false,"same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C_419050_2024-12-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"cross_canonical_boundary_replay_from_C12_source_row; new to C14 symbol/failure mode","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"production_scoring_patch_applied":false,"_source_file":"e2r_stock_web_v12_residual_round_R3_loop_107_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md","cross_canonical_boundary_replay":true,"source_row_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_row_file":"e2r_stock_web_v12_residual_round_R3_loop_107_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14_TRG","symbol":"340930","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":50,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":54,"stage_label_after":"Stage4B","changed_components":["execution_risk_score","margin_bridge_score","customer_contract_calloff_risk_gate"],"component_delta_explanation":"C14 overlay raises execution/call-off risk and requires utilization, shipment, revenue and margin bridge before Stage3 persistence.","MFE_90D_pct":7.6,"MAE_90D_pct":-46.6667,"score_return_alignment_label":"better_after_c14_gate","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14_TRG","symbol":"090470","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":50,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":54,"stage_label_after":"Stage4B","changed_components":["execution_risk_score","margin_bridge_score","customer_contract_calloff_risk_gate"],"component_delta_explanation":"C14 overlay raises execution/call-off risk and requires utilization, shipment, revenue and margin bridge before Stage3 persistence.","MFE_90D_pct":5.3922,"MAE_90D_pct":-25.4902,"score_return_alignment_label":"better_after_c14_gate","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14_TRG","symbol":"101360","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable","changed_components":["execution_risk_score","margin_bridge_score","customer_contract_calloff_risk_gate"],"component_delta_explanation":"C14 overlay raises execution/call-off risk and requires utilization, shipment, revenue and margin bridge before Stage3 persistence.","MFE_90D_pct":1.3986,"MAE_90D_pct":-33.2168,"score_return_alignment_label":"better_after_c14_gate","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_utilization_shipment_margin_bridge"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14_TRG","symbol":"137080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":50,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":54,"stage_label_after":"Stage4B","changed_components":["execution_risk_score","margin_bridge_score","customer_contract_calloff_risk_gate"],"component_delta_explanation":"C14 overlay raises execution/call-off risk and requires utilization, shipment, revenue and margin bridge before Stage3 persistence.","MFE_90D_pct":9.1429,"MAE_90D_pct":-37.7959,"score_return_alignment_label":"better_after_c14_gate","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14_TRG","symbol":"416180","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":50,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":54,"stage_label_after":"Stage4B","changed_components":["execution_risk_score","margin_bridge_score","customer_contract_calloff_risk_gate"],"component_delta_explanation":"C14 overlay raises execution/call-off risk and requires utilization, shipment, revenue and margin bridge before Stage3 persistence.","MFE_90D_pct":26.3556,"MAE_90D_pct":-41.488,"score_return_alignment_label":"better_after_c14_gate","current_profile_verdict":"current_profile_false_positive_if_contract_or_equipment_order_is_not_discounted_for_ev_slowdown_and_delivery_risk"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14","trigger_id":"C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14_TRG","symbol":"419050","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable","changed_components":["execution_risk_score","margin_bridge_score","customer_contract_calloff_risk_gate"],"component_delta_explanation":"C14 overlay raises execution/call-off risk and requires utilization, shipment, revenue and margin bridge before Stage3 persistence.","MFE_90D_pct":17.027,"MAE_90D_pct":-20.7027,"score_return_alignment_label":"better_after_c14_gate","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_utilization_shipment_margin_bridge"}
{"row_type":"residual_contribution","round":"R3","loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":6,"reused_case_count":6,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C14_C12_boundary_false_positive","EV_capex_delay_high_MAE","hard_4C_overkill_without_explicit_calloff"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as full new independent evidence unless independent_evidence_weight > 0.
- Do not apply production scoring changes from this MD alone.
- Treat this file as C14 boundary evidence, not as fresh C12 coverage.
- Hard 4C needs explicit order cut, customer call-off, utilization collapse, or thesis evidence broken.

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
completed_round: R3
completed_loop: 99
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger C14 rows=11 / need-to-30=19 / need-to-50=39
next_recommended_archetypes:
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat ledger: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Source C12 rows are explicitly marked with `cross_canonical_boundary_replay=true`, `source_row_canonical_archetype_id=C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`, and `independent_evidence_weight=0.5`.

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```
