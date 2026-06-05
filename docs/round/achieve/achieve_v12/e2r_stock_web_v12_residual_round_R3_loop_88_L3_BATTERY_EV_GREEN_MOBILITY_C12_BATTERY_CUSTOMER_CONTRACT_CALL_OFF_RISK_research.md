# E2R Stock-Web v12 Residual Research — R3 Loop 88 — C12 Battery Customer Contract Call-Off Risk

```text
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

scheduled_round: R3
scheduled_loop: 88
completed_round: R3
completed_loop: 88
next_round: R4
next_loop: 88
round_schedule_status: valid
round_sector_consistency: pass

large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: EV_DEMAND_CALL_OFF_RISK_BOTTOM_GUIDANCE_VS_CUSTOMER_UTILIZATION_BRIDGE
primary_price_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
```

---

## 1. Loop objective

이번 R3/L3 연구는 C12의 잔여오류를 본다.

C12는 단순한 “배터리 수요 둔화” 라벨이 아니라, 고객사 생산계획·call-off·가동률·재고조정이 실제 출하/마진으로 연결되는지 확인하는 아키타입이다.  
즉 배터리 체인의 문은 **orderbook**으로 열리지만, 문턱을 넘는 발은 **customer call-off와 utilization**이다.

이번 loop objective:

```text
coverage_gap_fill
counterexample_mining
current_calibrated_profile_stress_test
stage2_actionable_bonus_stress_test
canonical_archetype_compression
```

---

## 2. No-Repeat / novelty gate

No-Repeat Index 기준 hard duplicate key는 다음이다.

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

이번 연구는 C12에서 반복 위험이 높은 기존 상위 조합을 피한다.

```text
avoided_top_C12_symbols:
- 121600
- 278280
- 020150
- 348370
- 091580
- 137400
```

이번 신규 표본:

```text
selected_symbols:
- 006400 Samsung SDI / 삼성SDI
- 373220 LG Energy Solution / LG에너지솔루션
- 361610 SK IE Technology / SK아이이테크놀로지
```

판정:

```text
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
same_canonical_archetype_new_symbol_count: 3
same_canonical_archetype_new_trigger_family_count: 2
minimum_positive_case_count_met: true
minimum_counterexample_count_met: true
calibration_usable_case_count: 3
```

Note: `006400` and `373220` are known C14 battery/EV slowdown names in the wider corpus, but this MD uses a different canonical scope (`C12`) and different trigger families. The hard duplicate key is therefore not reused.

---

## 3. Stock-web validation scope

Stock-web checked profile/shards:

| symbol | company | profile_path | price_shard_path(s) used | profile status | corporate action overlap |
|---|---|---|---|---|---|
| 006400 | 삼성SDI | `atlas/symbol_profiles/006/006400.json` | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv` | active_like | none in entry~D+180 |
| 373220 | LG에너지솔루션 | `atlas/symbol_profiles/373/373220.json` | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv`, `.../2025.csv` | active_like | none in entry~D+180 |
| 361610 | SK아이이테크놀로지 | `atlas/symbol_profiles/361/361610.json` | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv`, `.../2025.csv` | active_like | none in entry~D+180 |

Validation flags:

```text
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
forward_window_trading_days_required: 180
corporate_action_window_status: clean_for_180D_all_cases
calibration_usable: true for all representative trigger rows
```

---

## 4. Case thesis

### Case A — 006400 Samsung SDI — bottom guidance can work, but only after absorbing a deep call-off drawdown

Evidence timing:

```text
trigger_date: 2025-03-05
trigger_type: Stage2-Actionable-BottomGuidance-ButCustomerCallOffRisk
evidence_available_at_that_date:
  - Samsung SDI CEO said EV demand would remain sluggish until H1 2026.
  - Company expected earnings to bottom in Q1 2025 and improve from Q2.
  - Q4 2024 operating loss confirmed weak demand pressure.
evidence_source:
  - Reuters, 2025-03-05, "Samsung SDI CEO says EV demand to remain sluggish until H1 of 2026"
```

Interpretation:

This is not a clean positive at the first trigger. It is a **bottoming guidance positive** that still carried call-off risk. The later price path became strongly positive, but only after a painful drawdown. C12 should therefore not treat management “bottom” guidance as immediate Green. It can be Stage2-Actionable only when a price/volume or customer utilization bridge confirms that call-off risk is no longer widening.

### Case B — 373220 LG Energy Solution — conservative outlook and capex cuts were not enough for rerating

Evidence timing:

```text
trigger_date: 2024-10-28
trigger_type: Stage2-FalsePositive-Candidate-ConservativeOutlook
evidence_available_at_that_date:
  - LG Energy Solution reported Q3 profit decline due to slowing EV demand.
  - Management gave a conservative 2025 revenue-growth view.
  - Capex reduction was discussed as demand softened.
evidence_source:
  - Reuters, 2024-10-28, "Battery maker LGES offers measured 2025 outlook after slow EV demand drags down Q3 profit"
```

Interpretation:

A “measured outlook” can reduce expectation risk, but if customer production plans remain soft and capex is being cut, the evidence is still defensive. The stock did not produce a durable positive 90D/180D path from the 2024-10-28 trigger. This is a C12 counterexample against treating bad-news-clearing as a rerating bridge.

### Case C — 361610 SK IE Technology — sale/restructuring rumor was a distress signal, not a rerating trigger

Evidence timing:

```text
trigger_date: 2024-05-15
entry_date: 2024-05-16
trigger_type: Stage2-FalsePositive-Candidate-SaleRumorDistressSignal
evidence_available_at_that_date:
  - Report that SK Innovation was considering selling SKIET.
  - Rationale was battery-business restructuring amid weak EV demand.
  - SK On had widened operating losses as shipments fell.
evidence_source:
  - Reuters, 2024-05-15, "SK Innovation considering sale of battery materials unit SKIET, paper reports"
```

Interpretation:

A sale rumor can look like a catalyst. In C12, however, if the reason is customer demand weakness and balance-sheet stress, it should be treated as **distress monetization**, not rerating evidence. The price path was a clear counterexample.

---

## 5. Price-path audit

All prices are raw/unadjusted stock-web `tradable_raw` rows.

| case_id | symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R3L88_C12_006400_20250305 | 006400 | 2025-03-05 | 213500 | +3.5% | -20.4% | +3.5% | -26.1% | +66.0% | -26.1% | 2025-11-04 | 354500 | -20.9% | positive_but_high_MAE_late_recovery |
| R3L88_C12_373220_20241028 | 373220 | 2024-10-28 | 416500 | +4.6% | -10.9% | +4.6% | -22.0% | +4.6% | -31.9% | 2024-11-11 | 435500 | -34.9% | counterexample_bad_news_not_clearing |
| R3L88_C12_361610_20240516 | 361610 | 2024-05-16 | 57600 | +1.0% | -25.9% | +1.0% | -47.8% | +1.0% | -62.4% | 2024-05-16 | 58200 | -62.8% | counterexample_distress_sale_signal |

Price audit notes:

```text
006400:
  stock_web_rows_checked:
    - 2025-03-05 close 213500
    - 2025-04-09 low 170000
    - 2025-10-28 high 321000
    - 2025-11-04 high 354500
  interpretation:
    late structural rebound existed, but the initial trigger tolerated -26% MAE before the move.

373220:
  stock_web_rows_checked:
    - 2024-10-28 close 416500
    - 2024-11-11 high 435500
    - 2025-03-14 low 325000
    - 2025-05-30 low 283500
  interpretation:
    bad-news-clearing and conservative capex talk were insufficient for rerating.

361610:
  stock_web_rows_checked:
    - 2024-05-16 close 57600
    - 2024-05-17 low 54000
    - 2024-09-10 low 30050
    - 2025-02-03 low 21650
  interpretation:
    restructuring/sale rumor should be treated as a 4C/watch-risk input, not as Stage2 positive.
```

---

## 6. Machine-readable JSONL trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R3L88_C12_006400_20250305","case_id":"R3L88_C12_006400","symbol":"006400","company_name":"Samsung SDI / 삼성SDI","round":"R3","loop":88,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"EV_DEMAND_CALL_OFF_RISK_BOTTOM_GUIDANCE_VS_CUSTOMER_UTILIZATION_BRIDGE","sector":"battery_ev","primary_archetype":"bottom_guidance_after_calloff_drawdown","loop_objective":"residual_error_found|counterexample_mining|positive_control","trigger_type":"Stage2-Actionable-BottomGuidance-ButCustomerCallOffRisk","trigger_date":"2025-03-05","evidence_available_at_that_date":"CEO said EV demand likely sluggish until H1 2026; Q1 2025 likely earnings bottom; Q4 2024 operating loss confirmed demand pressure","evidence_source":"Reuters 2025-03-05 Samsung SDI CEO says EV demand to remain sluggish until H1 of 2026","stage2_evidence_fields":"bottom_guidance; demand_sluggishness_acknowledged; earnings_trough_language","stage3_evidence_fields":"not_available_at_entry; needs_customer_utilization_or_order_conversion_bridge","stage4b_evidence_fields":"later_local_recovery_required_4B_overlay_only_after_rebound","stage4c_evidence_fields":"none_at_entry; watch_if_customer_calloff_deepens","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-05","entry_price":213500,"MFE_30D_pct":3.5,"MFE_90D_pct":3.5,"MFE_180D_pct":66.0,"MFE_1Y_pct":"contaminated_or_unavailable_not_needed","MFE_2Y_pct":"unavailable","MAE_30D_pct":-20.4,"MAE_90D_pct":-26.1,"MAE_180D_pct":-26.1,"MAE_1Y_pct":"contaminated_or_unavailable_not_needed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-04","peak_price":354500,"drawdown_after_peak_pct":-20.9,"green_lateness_ratio":"not_applicable_no_confirmed_green_trigger_at_entry","four_b_local_peak_proximity":"not_applicable_initial_stage2_entry","four_b_full_window_peak_proximity":"not_applicable_initial_stage2_entry","four_b_timing_verdict":"later_4B_overlay_required_after_full_recovery_not_at_entry","four_b_evidence_type":"none_at_entry","four_c_protection_label":"watch_only_if_calloff_deepens","trigger_outcome_label":"positive_but_high_MAE_late_recovery","current_profile_verdict":"stage2_actionable_too_early_without_utilization_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_180D","same_entry_group_id":"R3L88_C12_006400_20250305","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L88_C12_373220_20241028","case_id":"R3L88_C12_373220","symbol":"373220","company_name":"LG Energy Solution / LG에너지솔루션","round":"R3","loop":88,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"EV_DEMAND_CALL_OFF_RISK_BOTTOM_GUIDANCE_VS_CUSTOMER_UTILIZATION_BRIDGE","sector":"battery_ev","primary_archetype":"conservative_outlook_not_rerating_bridge","loop_objective":"counterexample_mining|residual_error_found","trigger_type":"Stage2-FalsePositive-Candidate-ConservativeOutlook","trigger_date":"2024-10-28","evidence_available_at_that_date":"Q3 profit down on weak EV demand; conservative 2025 growth outlook; capex reduction discussed","evidence_source":"Reuters 2024-10-28 Battery maker LGES offers measured 2025 outlook after slow EV demand drags down Q3 profit","stage2_evidence_fields":"bad_news_clearing_candidate; conservative_outlook; capex_cut","stage3_evidence_fields":"missing_customer_utilization_reacceleration; missing_revenue_growth_bridge","stage4b_evidence_fields":"price_only_local_peak; no_non_price_4B_at_entry","stage4c_evidence_fields":"customer_calloff_watch; capex_cut_watch","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv; atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-28","entry_price":416500,"MFE_30D_pct":4.6,"MFE_90D_pct":4.6,"MFE_180D_pct":4.6,"MFE_1Y_pct":"contaminated_or_unavailable_not_needed","MFE_2Y_pct":"unavailable","MAE_30D_pct":-10.9,"MAE_90D_pct":-22.0,"MAE_180D_pct":-31.9,"MAE_1Y_pct":"contaminated_or_unavailable_not_needed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":435500,"drawdown_after_peak_pct":-34.9,"green_lateness_ratio":"not_applicable_no_confirmed_green_trigger","four_b_local_peak_proximity":0.046,"four_b_full_window_peak_proximity":0.046,"four_b_timing_verdict":"price_only_local_4B_not_full_4B","four_b_evidence_type":"price_only","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_bad_news_not_clearing","current_profile_verdict":"stage2_false_positive_if_conservative_outlook_counted_as_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_180D","same_entry_group_id":"R3L88_C12_373220_20241028","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L88_C12_361610_20240516","case_id":"R3L88_C12_361610","symbol":"361610","company_name":"SK IE Technology / SK아이이테크놀로지","round":"R3","loop":88,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"EV_DEMAND_CALL_OFF_RISK_BOTTOM_GUIDANCE_VS_CUSTOMER_UTILIZATION_BRIDGE","sector":"battery_ev","primary_archetype":"distress_sale_rumor_customer_calloff_risk","loop_objective":"counterexample_mining|4C_watch_stress_test","trigger_type":"Stage2-FalsePositive-Candidate-SaleRumorDistressSignal","trigger_date":"2024-05-15","evidence_available_at_that_date":"Reported SK Innovation consideration of SKIET sale; reason tied to SK On financial pressure and weakening EV demand; no confirmed buyer/valuation bridge","evidence_source":"Reuters 2024-05-15 SK Innovation considering sale of battery materials unit SKIET paper reports","stage2_evidence_fields":"sale_rumor; restructuring; possible_balance_sheet_relief","stage3_evidence_fields":"missing_confirmed_sale; missing_customer_volume_recovery; missing_utilization_bridge","stage4b_evidence_fields":"none_at_entry; distress_not_overheat","stage4c_evidence_fields":"distress_monetization; customer_calloff_risk; battery_unit_loss_widening","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv; atlas/ohlcv_tradable_by_symbol_year/361/361610/2025.csv","profile_path":"atlas/symbol_profiles/361/361610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":57600,"MFE_30D_pct":1.0,"MFE_90D_pct":1.0,"MFE_180D_pct":1.0,"MFE_1Y_pct":"contaminated_or_unavailable_not_needed","MFE_2Y_pct":"unavailable","MAE_30D_pct":-25.9,"MAE_90D_pct":-47.8,"MAE_180D_pct":-62.4,"MAE_1Y_pct":"not_required_observed_lower_later","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":58200,"drawdown_after_peak_pct":-62.8,"green_lateness_ratio":"not_applicable_failed_stage2_candidate","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B_distress_4C_watch","four_b_evidence_type":"none","four_c_protection_label":"hard_4c_watch_would_have_helped","trigger_outcome_label":"counterexample_distress_sale_signal","current_profile_verdict":"stage2_false_positive_if_sale_rumor_counted_as_positive_event","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_180D","same_entry_group_id":"R3L88_C12_361610_20240516","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

---

## 7. Component breakdown — research proxy score

The component scores below are not production scores. They are a research proxy to explain why the same “EV demand is weak” evidence can be positive, neutral, or negative depending on whether customer-calloff risk is resolved.

### 7.1 Baseline / P0 proxy

| case | contract_score | backlog_visibility_score | margin_bridge_score | revision_score | customer_quality_score | policy_or_regulatory_score | valuation_repricing_score | execution_risk_score | weighted_score_before | stage_label_before |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 006400 | 5 | 4 | 5 | 7 | 8 | 3 | 5 | -7 | 66 | Stage2-Actionable candidate |
| 373220 | 5 | 3 | 2 | 2 | 7 | 4 | 3 | -8 | 59 | Stage2-Watch |
| 361610 | 2 | 1 | 1 | 1 | 4 | 1 | 3 | -10 | 46 | Stage1/4C-Watch |

### 7.2 Proposed C12 guard profile

Guard principle:

```text
if evidence_family in [bottom_guidance, conservative_outlook, sale_restructuring_rumor]
AND customer_utilization_bridge is missing
AND calloff_or_capex_cut_risk is present:
    cap Stage2-Actionable at Watch unless price/volume confirmation or revenue conversion bridge appears.
```

| case | raw_component_scores_after | weighted_score_after | stage_label_after | component_delta_explanation |
|---|---|---:|---|---|
| 006400 | bottom_guidance 7, customer_quality 8, execution_risk -7, utilization_bridge unknown | 62 | Stage2-Watch until bridge; later Stage2-Actionable after confirmation | good later outcome, but early trigger had -26% MAE |
| 373220 | conservative_outlook 3, capex_cut -5, customer_calloff_risk -8 | 54 | Stage2-Watch / FalsePositive guard | defensive outlook was not a revenue bridge |
| 361610 | sale_rumor 3, distress_signal -10, customer_calloff_risk -9 | 39 | 4C-Watch / no positive stage | sale rumor came from stress, not structural demand |

---

## 8. Profile simulation table

| profile_id | profile_scope | hypothesis | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | allow bottom/conservative/sale-rumor triggers as Stage2 if EV-demand evidence exists | 3 | +3.0% | -32.0% | +23.9% | -40.1% | 66.7% | 0 | poor; high-MAE positive hidden by late rebound |
| P0b | e2r_2_0_baseline_reference | looser Stage2 headline sensitivity | 3 | +3.0% | -32.0% | +23.9% | -40.1% | 66.7% | 0 | poor |
| P1 | sector_specific_candidate_profile | require utilization/revenue bridge before C12 Stage2-Actionable | 1 | +3.5% | -26.1% | +66.0% | -26.1% | 0.0% | 0 | improved but still high-MAE |
| P2 | canonical_archetype_candidate_profile | treat sale/restructuring rumor caused by weak demand as 4C-watch, not Stage2 | 2 | +4.1% | -24.1% | +35.3% | -29.0% | 0.0% | 0 | improved; avoids 361610 false positive |
| P3 | counterexample_guard_profile | cap bottom guidance to Watch until price-volume or shipment bridge confirms | 0 immediate entries | n/a | n/a | n/a | n/a | n/a | 1 possible delayed entry | conservative; may miss 006400 early but reduces drawdown |

---

## 9. 4B / 4C timing audit

### 4B

No full 4B should be assigned from the initial C12 trigger in these cases.

```text
006400:
  later full-window peak existed, but not available at entry.
  4B timing should come after recovery/revision evidence, not from bottom guidance.

373220:
  2024-11 local high was price-only.
  No non-price 4B evidence.
  do_not_treat_as_full_4B = true.

361610:
  distress route, not overheat.
  4B not applicable.
```

### 4C

```text
361610:
  hard_4c_watch would have helped.
  sale rumor caused by weak demand and balance-sheet pressure should route to thesis_break_watch_only.

373220:
  conservative outlook + capex cut should remain watch, not positive.
  hard 4C only if customer call-off/revenue cuts persist.

006400:
  not hard 4C because later recovery was real.
  But initial trigger required MAE guard because drawdown exceeded -25%.
```

---

## 10. Sector/canonical rule proposal

Rule scope:

```text
rule_scope: canonical_archetype_specific
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
new_axis_proposed: none
existing_axis_tested:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
existing_axis_kept: true
existing_axis_strengthened: null
existing_axis_weakened: null
```

Candidate guard, shadow-only:

```text
C12_calloff_bridge_required_guard:
  if trigger evidence is bottom_guidance or conservative_outlook or sale_restructuring_rumor
  and customer utilization / shipment / revenue conversion bridge is missing
  and EV demand slowdown or customer call-off risk is explicitly present:
      Stage2-Actionable should be capped to Stage2-Watch
      Green should be blocked
      if trigger is distress sale/restructuring caused by weak demand:
          route to 4C-watch / thesis-break-watch-only
```

Do not promote as new global delta:

```text
do_not_propose_new_weight_delta: true
reason:
  - sample size = 3
  - one positive case has high early MAE
  - rule is C12-specific, not global
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_watch_count | calibration_usable_case_count | new_symbol_count |
|---|---|---|---:|---:|---:|---:|---:|---:|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | EV_DEMAND_CALL_OFF_RISK_BOTTOM_GUIDANCE_VS_CUSTOMER_UTILIZATION_BRIDGE | 1 | 2 | 0 | 2 | 3 | 3 |

---

## 12. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence

residual_error_types_found:
  - bottom_guidance_positive_can_hide_high_MAE
  - conservative_outlook_not_sufficient_rerating_bridge
  - distress_sale_rumor_misclassified_as_positive_event
  - customer_calloff_bridge_missing

new_axis_proposed: null
existing_axis_strengthened: null
existing_axis_weakened: null
existing_axis_kept:
  - Stage2-Actionable requires evidence bridge, not just bottoming language.
  - Hard 4C should remain thesis-break/customer-calloff dependent.
  - Full 4B requires non-price evidence.

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: small_sample_shadow_only

loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
```

---

## 13. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent for Songdaiki/stock_agent. Do not execute this during the research run.

Goal:
Ingest this MD as a v12 research artifact only. Do not change production scoring directly.

Suggested parser checks:
1. Parse all JSONL rows under "Machine-readable JSONL trigger rows".
2. Confirm round=R3, loop=88, large_sector_id=L3_BATTERY_EV_GREEN_MOBILITY.
3. Confirm canonical_archetype_id=C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.
4. Deduplicate on canonical_archetype_id + symbol + trigger_type + entry_date.
5. Treat the proposed C12_calloff_bridge_required_guard as shadow-only.
6. Do not promote as global delta; sample size is insufficient.
7. Aggregate the 006400 case as positive_but_high_MAE_late_recovery, not clean Stage2 success.
8. Aggregate 373220 and 361610 as counterexamples.
```

---

## 14. Round state

```text
completed_round = R3
completed_loop = 88
next_round = R4
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
