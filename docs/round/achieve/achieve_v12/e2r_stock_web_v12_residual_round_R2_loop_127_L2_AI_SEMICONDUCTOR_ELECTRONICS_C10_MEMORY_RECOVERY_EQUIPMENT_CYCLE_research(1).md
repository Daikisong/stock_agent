# E2R Stock-Web v12 Residual Research — R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_127_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selected_round: R2
selected_loop: 127
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under_30_representative_rows / C10 rows 13 need_to_30 17 in static No-Repeat Index; session-local C10 loops 121/122/123/126 avoided by new trigger families where possible
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_BOUNDARY_ROUTE_CONVERSION_VS_PRODUCT_IDENTITY_PROXY
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
investment_recommendation: false
loop_objective:
  - coverage_gap_fill
  - followup_new_symbol_date_family
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - stage2_actionable_bonus_stress_test
  - canonical_archetype_compression
  - sector_specific_rule_discovery
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 3
stage4b_overlay_count: 4
stage4c_case_count: 0
calibration_usable_trigger_count: 5
representative_trigger_count: 5
current_profile_error_count: 5
canonical_archetype_rule_candidate: C10_MEMORY_RECOVERY_REQUIRES_DIRECT_CONVERSION_BRIDGE_WITH_BOUNDARY_ROUTE_AND_POST_REPRICE_4B_GUARD
```

## 1. Selection Rationale

`V12_Research_No_Repeat_Index.md`의 static ledger에서 C10은 대표 row 13개, need-to-30 17개로 남아 있는 Priority 0 축이다. 이번 세션의 기존 C10 후속들이 front-end 장비, OSAT, 기판, 소모품을 이미 다뤘으므로, 이번 loop는 **진공펌프 / 칠러·스크러버 / 웨이퍼테스터 / 프리커서** 경계 route를 새 trigger family로 분리했다. C10은 R2/L2로 고정 매핑되므로 round-sector hard gate는 통과한다.

## 2. Stock-Web Manifest and Validation Scope

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
entry_price_basis = close c column on entry_date
MFE_MAE_basis = high/low over entry_date through forward 30/90/180 trading-day windows
```

## 3. Novelty / No-Repeat Check

| check | result | note |
|---|---|---|
| hard duplicate key | pass | no `canonical_archetype_id + symbol + trigger_type + entry_date` duplicate in current local C10 loop set |
| minimum_new_independent_case_ratio | pass | 5/5 = 1.00 |
| minimum_new_symbol_count | pass | 5 |
| minimum_positive_case_count | pass | 2 |
| minimum_counterexample_count | pass | 3 |
| round-sector consistency | pass | C10 -> R2 / L2 |

## 4. Evidence Register

| evidence_id | symbol | company | trigger_date | evidence family | source URL | use |
|---|---|---|---|---|---|---|
| EV_C10_FU127_083310_20241211_LOT_VACUUM_PUMP_TROUGH_REOPEN | 083310 | 엘오티베큠 | 2024-12-11 | dry_vacuum_pump_demand_reopen_after_customer_capex_pause | https://www.dailyinvest.kr/news/articleView.html?idxno=62331 | 반도체용 건식진공펌프 pure product route는 C10에 직접 닿지만 2024년 중 고객 투자 감소로 실적이 꺾였다. 2024-12-11의 핵심은 이미 확인된 악재 뒤에서 2025년 반도체 전환투자/진공펌프 수요 회복 기대가 가격 저점 부근에 붙은 reopen signal이라는 점이다. |
| EV_C10_FU127_036810_20240426_FST_CHILLER_PELLICLE_BOUNDARY_4B | 036810 | 에프에스티 | 2024-04-26 | chiller_pellicle_equipment_turnaround_without_memory_order_specificity | https://www.dailyinvest.kr/news/articleView.html?idxno=58293 | 펠리클·칠러는 반도체 제조 인프라에 직접 들어가지만, 2024-04의 공개 근거는 EUV/장비 라인업과 제품 mix 개선에 가까웠다. C10 신용은 허용하되 메모리 order cycle pure signal로 과대 승격하면 안 된다. |
| EV_C10_FU127_083450_20240729_GST_SCRUBBER_CHILLER_DELAYED_REOPEN | 083450 | GST | 2024-07-29 | scrubber_chiller_customer_investment_reopen_but_not_immediate_margin_conversion | https://www.dailyinvest.kr/news/articleView.html?idxno=59830 | 스크러버·칠러는 C10의 설비투자 회복 통로지만, 2024-07 trigger는 고객사 투자 재개 기대와 제품 mix 이야기였다. 30/90D에는 MAE가 먼저 열리고 180D에서야 MFE가 회복되어, 즉시 Yellow가 아니라 staged Stage2/watch가 맞다. |
| EV_C10_FU127_232140_20240424_YC_MEMORY_TESTER_ORDER_FAST_MFE | 232140 | 와이씨 | 2024-04-24 | named_customer_memory_tester_supply_contract | https://www.etnews.com/20240424000381 | 삼성전자향 메모리 검사장비 공급계약은 C10에서 가장 깨끗한 order/revenue bridge에 가깝다. 다만 30/90D MFE가 너무 빠르게 터지고 이후 post-peak drawdown이 커져, Stage2-Actionable positive와 local 4B profit-lock이 동시에 필요하다. |
| EV_C10_FU127_417500_20240307_JITECH_PRECURSOR_BETA_FAIL | 417500 | 제이아이테크 | 2024-03-07 | precursor_order_recovery_and_utilization_language_without_durable_forward_survival | https://www.dailyinvest.kr/news/articleView.html?idxno=57514 | 프리커서 수주 회복·가동률 상승은 메모리 회복과 연결될 수 있지만, 소재 proxy는 order/revenue bridge의 직접성이 장비보다 약하다. 2024-03 trigger는 30/90/180D MAE가 빠르게 열려 C10 false-positive guardrail에 더 값진 표본이다. |

## 5. Price Path Table

| symbol | company | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_180D_date | peak_180D_high | post_peak_drawdown_180D_pct | positive_or_counterexample | current_profile_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---|
| 083310 | 엘오티베큠 | Stage2-Actionable | 2024-12-11 | 8,200 | 22.80 | 31.95 | 51.22 | -4.63 | -6.71 | -6.71 | 2025-09-09 | 12,400 | -3.87 | positive | too_late_if_it_waits_for_accounting_profit_after_customer_capex_reopen_signal |
| 036810 | 에프에스티 | Stage2-Actionable | 2024-04-26 | 32,550 | 28.57 | 28.57 | 28.57 | -10.60 | -30.26 | -56.41 | 2024-06-11 | 41,850 | -66.09 | counterexample | false_positive_if_chiller_pellicle_product_identity_is_promoted_to_durable_memory_recovery_Yellow |
| 083450 | GST | Stage2 | 2024-07-29 | 17,640 | 8.56 | 8.56 | 32.37 | -28.51 | -28.51 | -28.51 | 2025-02-24 | 23,350 | -34.18 | counterexample | false_positive_if_customer_investment_reopen_language_gets_immediate_Yellow_before_margin_print |
| 232140 | 와이씨 | Stage2-Actionable | 2024-04-24 | 10,700 | 88.32 | 114.49 | 114.49 | -11.59 | -11.59 | -22.71 | 2024-06-13 | 22,950 | -63.97 | positive | aligned_positive_but_4B_too_late_if_fast_MFE_not_locked |
| 417500 | 제이아이테크 | Stage2 | 2024-03-07 | 5,660 | 10.25 | 10.25 | 10.25 | -23.14 | -35.87 | -52.83 | 2024-03-08 | 6,240 | -57.21 | counterexample | false_positive_if_precursor_recovery_language_is_promoted_without_customer_volume_and_margin_survival |

## 6. Case Notes

### C10_FU127_083310_20241211_LOT_VACUUM_PUMP_TROUGH_REOPEN — 엘오티베큠 (083310)
- **Trigger:** Stage2-Actionable / 2024-12-11 -> entry 2024-12-11 @ 8,200.
- **Evidence:** 반도체용 건식진공펌프 pure product route는 C10에 직접 닿지만 2024년 중 고객 투자 감소로 실적이 꺾였다. 2024-12-11의 핵심은 이미 확인된 악재 뒤에서 2025년 반도체 전환투자/진공펌프 수요 회복 기대가 가격 저점 부근에 붙은 reopen signal이라는 점이다.
- **Path:** MFE90 31.95% / MAE90 -6.71%, MFE180 51.22% / MAE180 -6.71%, post-peak DD -3.87%.
- **Interpretation:** allow_stage2_actionable_reopen_when_product_route_is_direct_and_price_is_after_earnings_trough

### C10_FU127_036810_20240426_FST_CHILLER_PELLICLE_BOUNDARY_4B — 에프에스티 (036810)
- **Trigger:** Stage2-Actionable / 2024-04-26 -> entry 2024-04-26 @ 32,550.
- **Evidence:** 펠리클·칠러는 반도체 제조 인프라에 직접 들어가지만, 2024-04의 공개 근거는 EUV/장비 라인업과 제품 mix 개선에 가까웠다. C10 신용은 허용하되 메모리 order cycle pure signal로 과대 승격하면 안 된다.
- **Path:** MFE90 28.57% / MAE90 -30.26%, MFE180 28.57% / MAE180 -56.41%, post-peak DD -66.09%.
- **Interpretation:** Stage2-Actionable is allowed but attach local_4B once MFE30 approaches 25-30 without named order or margin conversion

### C10_FU127_083450_20240729_GST_SCRUBBER_CHILLER_DELAYED_REOPEN — GST (083450)
- **Trigger:** Stage2 / 2024-07-29 -> entry 2024-07-29 @ 17,640.
- **Evidence:** 스크러버·칠러는 C10의 설비투자 회복 통로지만, 2024-07 trigger는 고객사 투자 재개 기대와 제품 mix 이야기였다. 30/90D에는 MAE가 먼저 열리고 180D에서야 MFE가 회복되어, 즉시 Yellow가 아니라 staged Stage2/watch가 맞다.
- **Path:** MFE90 8.56% / MAE90 -28.51%, MFE180 32.37% / MAE180 -28.51%, post-peak DD -34.18%.
- **Interpretation:** keep Stage2-watch until delayed order/revenue conversion appears; do not Green through early -28% MAE

### C10_FU127_232140_20240424_YC_MEMORY_TESTER_ORDER_FAST_MFE — 와이씨 (232140)
- **Trigger:** Stage2-Actionable / 2024-04-24 -> entry 2024-04-24 @ 10,700.
- **Evidence:** 삼성전자향 메모리 검사장비 공급계약은 C10에서 가장 깨끗한 order/revenue bridge에 가깝다. 다만 30/90D MFE가 너무 빠르게 터지고 이후 post-peak drawdown이 커져, Stage2-Actionable positive와 local 4B profit-lock이 동시에 필요하다.
- **Path:** MFE90 114.49% / MAE90 -11.59%, MFE180 114.49% / MAE180 -22.71%, post-peak DD -63.97%.
- **Interpretation:** credit named memory tester order as Stage2-Actionable; add local 4B after parabolic MFE without follow-on order confirmation

### C10_FU127_417500_20240307_JITECH_PRECURSOR_BETA_FAIL — 제이아이테크 (417500)
- **Trigger:** Stage2 / 2024-03-07 -> entry 2024-03-07 @ 5,660.
- **Evidence:** 프리커서 수주 회복·가동률 상승은 메모리 회복과 연결될 수 있지만, 소재 proxy는 order/revenue bridge의 직접성이 장비보다 약하다. 2024-03 trigger는 30/90/180D MAE가 빠르게 열려 C10 false-positive guardrail에 더 값진 표본이다.
- **Path:** MFE90 10.25% / MAE90 -35.87%, MFE180 10.25% / MAE180 -52.83%, post-peak DD -57.21%.
- **Interpretation:** material proxy stays Stage2-watch unless customer volume and sustained margin bridge are confirmed; local 4B if trigger is near the immediate post-report peak

## 7. Profile / Corporate-Action Scope

| symbol | profile | tradable shard | corporate-action / discontinuity handling | calibration usable |
|---|---|---|---|---|
| 083310 | `atlas/symbol_profiles/083/083310.json` | `atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv` | corporate_action_candidate_dates are 2007-05-29 and 2007-06-19; no overlap with 2024-12-11~D+180 window | true |
| 036810 | `atlas/symbol_profiles/036/036810.json` | `atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv` | corporate_action_candidate_dates are 2000-05-02 and 2004-06-17; no overlap with 2024-04-26~D+180 window | true |
| 083450 | `atlas/symbol_profiles/083/083450.json` | `atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv` | corporate_action_candidate_dates include 2024-06-26 and 2024-07-24; trigger entry 2024-07-29 is after the candidate dates, so D+180 window is treated usable but caveated | true |
| 232140 | `atlas/symbol_profiles/232/232140.json` | `atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv` | corporate_action_candidate_date is 2017-04-05; no overlap with 2024-04-24~D+180 window. Name changed from 와이아이케이 to 와이씨 on 2024-04-25, but ticker continuity is valid. | true |
| 417500 | `atlas/symbol_profiles/417/417500.json` | `atlas/ohlcv_tradable_by_symbol_year/417/417500/2024.csv` | corporate_action_candidate_dates are 2023-05-22 and 2023-06-12; no overlap with 2024-03-07~D+180 window | true |

## 8. Score / Return Alignment Summary

| rule candidate | protected failures | allowed positives | net conclusion |
|---|---|---|---|
| C10_MEMORY_RECOVERY_REQUIRES_DIRECT_CONVERSION_BRIDGE_WITH_BOUNDARY_ROUTE_AND_POST_REPRICE_4B_GUARD | FST post-peak 4B, GST staged-entry drawdown, JI Tech precursor beta false positive | LOT Vacuum reopen after trough, YC named memory-tester order | C10 should credit actual conversion routes, but product identity or broad beta must stay Stage2-watch/local 4B until margin/order survival appears. |

## 9. Machine-Readable JSONL Rows

```jsonl
{"source_row_type":"case","row_type":"case","case_id":"C10_FU127_083310_20241211_LOT_VACUUM_PUMP_TROUGH_REOPEN","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"DRY_VACUUM_PUMP_MEMORY_CAPEX_REOPEN_AFTER_EARNINGS_TROUGH","case_role":"positive_reopen_control","positive_or_counterexample":"positive","evidence_family":"dry_vacuum_pump_demand_reopen_after_customer_capex_pause","evidence_summary":"반도체용 건식진공펌프 pure product route는 C10에 직접 닿지만 2024년 중 고객 투자 감소로 실적이 꺾였다. 2024-12-11의 핵심은 이미 확인된 악재 뒤에서 2025년 반도체 전환투자/진공펌프 수요 회복 기대가 가격 저점 부근에 붙은 reopen signal이라는 점이다.","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=62331","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"case","row_type":"case","case_id":"C10_FU127_036810_20240426_FST_CHILLER_PELLICLE_BOUNDARY_4B","symbol":"036810","company_name":"에프에스티","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CHILLER_AND_PELLICLE_MEMORY_INFRA_BOUNDARY_ROUTE_WITH_POST_PEAK_4B","case_role":"mixed_positive_then_4B_guardrail","positive_or_counterexample":"counterexample","evidence_family":"chiller_pellicle_equipment_turnaround_without_memory_order_specificity","evidence_summary":"펠리클·칠러는 반도체 제조 인프라에 직접 들어가지만, 2024-04의 공개 근거는 EUV/장비 라인업과 제품 mix 개선에 가까웠다. C10 신용은 허용하되 메모리 order cycle pure signal로 과대 승격하면 안 된다.","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=58293","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"case","row_type":"case","case_id":"C10_FU127_083450_20240729_GST_SCRUBBER_CHILLER_DELAYED_REOPEN","symbol":"083450","company_name":"GST","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SCRUBBER_CHILLER_CUSTOMER_INVESTMENT_REOPEN_WITH_RAW_ACTION_CAVEAT","case_role":"staged_entry_counterexample","positive_or_counterexample":"counterexample","evidence_family":"scrubber_chiller_customer_investment_reopen_but_not_immediate_margin_conversion","evidence_summary":"스크러버·칠러는 C10의 설비투자 회복 통로지만, 2024-07 trigger는 고객사 투자 재개 기대와 제품 mix 이야기였다. 30/90D에는 MAE가 먼저 열리고 180D에서야 MFE가 회복되어, 즉시 Yellow가 아니라 staged Stage2/watch가 맞다.","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=59830","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"case","row_type":"case","case_id":"C10_FU127_232140_20240424_YC_MEMORY_TESTER_ORDER_FAST_MFE","symbol":"232140","company_name":"와이씨","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_WAFER_TESTER_NAMED_ORDER_TO_FAST_MFE_WITH_4B_PROFIT_LOCK","case_role":"positive_order_conversion_with_profit_lock_guardrail","positive_or_counterexample":"positive","evidence_family":"named_customer_memory_tester_supply_contract","evidence_summary":"삼성전자향 메모리 검사장비 공급계약은 C10에서 가장 깨끗한 order/revenue bridge에 가깝다. 다만 30/90D MFE가 너무 빠르게 터지고 이후 post-peak drawdown이 커져, Stage2-Actionable positive와 local 4B profit-lock이 동시에 필요하다.","evidence_url":"https://www.etnews.com/20240424000381","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"case","row_type":"case","case_id":"C10_FU127_417500_20240307_JITECH_PRECURSOR_BETA_FAIL","symbol":"417500","company_name":"제이아이테크","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"PRECURSOR_UTILIZATION_RECOVERY_BETA_WITHOUT_DURABLE_ORDER_MARGIN_SURVIVAL","case_role":"material_proxy_false_positive","positive_or_counterexample":"counterexample","evidence_family":"precursor_order_recovery_and_utilization_language_without_durable_forward_survival","evidence_summary":"프리커서 수주 회복·가동률 상승은 메모리 회복과 연결될 수 있지만, 소재 proxy는 order/revenue bridge의 직접성이 장비보다 약하다. 2024-03 trigger는 30/90/180D MAE가 빠르게 열려 C10 false-positive guardrail에 더 값진 표본이다.","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=57514","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"trigger","row_type":"trigger","trigger_id":"T_C10_FU127_083310_20241211_Stage2_Actionable","case_id":"C10_FU127_083310_20241211_LOT_VACUUM_PUMP_TROUGH_REOPEN","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"DRY_VACUUM_PUMP_MEMORY_CAPEX_REOPEN_AFTER_EARNINGS_TROUGH","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-11","entry_date":"2024-12-11","entry_price":8200,"price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv","profile_path":"atlas/symbol_profiles/083/083310.json","MFE_30D_pct":22.8,"MFE_90D_pct":31.95,"MFE_180D_pct":51.22,"MAE_30D_pct":-4.63,"MAE_90D_pct":-6.71,"MAE_180D_pct":-6.71,"peak_180D_date":"2025-09-09","peak_180D_high":12400,"post_peak_drawdown_180D_pct":-3.87,"positive_or_counterexample":"positive","current_profile_verdict":"too_late_if_it_waits_for_accounting_profit_after_customer_capex_reopen_signal","proposed_profile_action":"allow_stage2_actionable_reopen_when_product_route_is_direct_and_price_is_after_earnings_trough","calibration_usable":true,"representative_for_aggregate":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|083310|Stage2-Actionable|2024-12-11","validation_status":"pass","validation_notes":"corporate_action_candidate_dates are 2007-05-29 and 2007-06-19; no overlap with 2024-12-11~D+180 window","raw_component_score_breakdown":{"eps_fcf_visibility":9,"earnings_visibility":10,"bottleneck_pricing":9,"market_mispricing":11,"valuation_rerating":11,"capital_allocation":4,"information_confidence":11,"total_proxy":65},"stage_component_tags":{"stage2":["direct_memory_capex_product_route","as_of_negative_result_already_known","reopen_after_customer_capex_pause"],"stage3":["needs confirmed order or margin print before Yellow"],"stage4b":[],"stage4c":[]}}
{"source_row_type":"trigger","row_type":"trigger","trigger_id":"T_C10_FU127_036810_20240426_Stage2_Actionable","case_id":"C10_FU127_036810_20240426_FST_CHILLER_PELLICLE_BOUNDARY_4B","symbol":"036810","company_name":"에프에스티","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CHILLER_AND_PELLICLE_MEMORY_INFRA_BOUNDARY_ROUTE_WITH_POST_PEAK_4B","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":32550,"price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv","profile_path":"atlas/symbol_profiles/036/036810.json","MFE_30D_pct":28.57,"MFE_90D_pct":28.57,"MFE_180D_pct":28.57,"MAE_30D_pct":-10.6,"MAE_90D_pct":-30.26,"MAE_180D_pct":-56.41,"peak_180D_date":"2024-06-11","peak_180D_high":41850,"post_peak_drawdown_180D_pct":-66.09,"positive_or_counterexample":"counterexample","current_profile_verdict":"false_positive_if_chiller_pellicle_product_identity_is_promoted_to_durable_memory_recovery_Yellow","proposed_profile_action":"Stage2-Actionable is allowed but attach local_4B once MFE30 approaches 25-30 without named order or margin conversion","calibration_usable":true,"representative_for_aggregate":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|036810|Stage2-Actionable|2024-04-26","validation_status":"pass","validation_notes":"corporate_action_candidate_dates are 2000-05-02 and 2004-06-17; no overlap with 2024-04-26~D+180 window","raw_component_score_breakdown":{"eps_fcf_visibility":7,"earnings_visibility":8,"bottleneck_pricing":10,"market_mispricing":7,"valuation_rerating":8,"capital_allocation":3,"information_confidence":10,"total_proxy":53},"stage_component_tags":{"stage2":["product_route_to_semiconductor_fab","EUV_and_chiller_lineup"],"stage3":[],"stage4b":["post_peak_drawdown_large","no_named_memory_order_in_trigger"],"stage4c":[]}}
{"source_row_type":"trigger","row_type":"trigger","trigger_id":"T_C10_FU127_083450_20240729_Stage2","case_id":"C10_FU127_083450_20240729_GST_SCRUBBER_CHILLER_DELAYED_REOPEN","symbol":"083450","company_name":"GST","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SCRUBBER_CHILLER_CUSTOMER_INVESTMENT_REOPEN_WITH_RAW_ACTION_CAVEAT","trigger_type":"Stage2","trigger_date":"2024-07-29","entry_date":"2024-07-29","entry_price":17640,"price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv","profile_path":"atlas/symbol_profiles/083/083450.json","MFE_30D_pct":8.56,"MFE_90D_pct":8.56,"MFE_180D_pct":32.37,"MAE_30D_pct":-28.51,"MAE_90D_pct":-28.51,"MAE_180D_pct":-28.51,"peak_180D_date":"2025-02-24","peak_180D_high":23350,"post_peak_drawdown_180D_pct":-34.18,"positive_or_counterexample":"counterexample","current_profile_verdict":"false_positive_if_customer_investment_reopen_language_gets_immediate_Yellow_before_margin_print","proposed_profile_action":"keep Stage2-watch until delayed order/revenue conversion appears; do not Green through early -28% MAE","calibration_usable":true,"representative_for_aggregate":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|083450|Stage2|2024-07-29","validation_status":"pass","validation_notes":"corporate_action_candidate_dates include 2024-06-26 and 2024-07-24; trigger entry 2024-07-29 is after the candidate dates, so D+180 window is treated usable but caveated","raw_component_score_breakdown":{"eps_fcf_visibility":6,"earnings_visibility":8,"bottleneck_pricing":9,"market_mispricing":9,"valuation_rerating":8,"capital_allocation":3,"information_confidence":9,"total_proxy":52},"stage_component_tags":{"stage2":["scrubber_chiller_fab_infra_route","customer_investment_reopen_language"],"stage3":[],"stage4b":["early_MAE_above_20","corporate_action_profile_caveat_before_entry"],"stage4c":[]}}
{"source_row_type":"trigger","row_type":"trigger","trigger_id":"T_C10_FU127_232140_20240424_Stage2_Actionable","case_id":"C10_FU127_232140_20240424_YC_MEMORY_TESTER_ORDER_FAST_MFE","symbol":"232140","company_name":"와이씨","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_WAFER_TESTER_NAMED_ORDER_TO_FAST_MFE_WITH_4B_PROFIT_LOCK","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":10700,"price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","MFE_30D_pct":88.32,"MFE_90D_pct":114.49,"MFE_180D_pct":114.49,"MAE_30D_pct":-11.59,"MAE_90D_pct":-11.59,"MAE_180D_pct":-22.71,"peak_180D_date":"2024-06-13","peak_180D_high":22950,"post_peak_drawdown_180D_pct":-63.97,"positive_or_counterexample":"positive","current_profile_verdict":"aligned_positive_but_4B_too_late_if_fast_MFE_not_locked","proposed_profile_action":"credit named memory tester order as Stage2-Actionable; add local 4B after parabolic MFE without follow-on order confirmation","calibration_usable":true,"representative_for_aggregate":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|232140|Stage2-Actionable|2024-04-24","validation_status":"pass","validation_notes":"corporate_action_candidate_date is 2017-04-05; no overlap with 2024-04-24~D+180 window. Name changed from 와이아이케이 to 와이씨 on 2024-04-25, but ticker continuity is valid.","raw_component_score_breakdown":{"eps_fcf_visibility":10,"earnings_visibility":12,"bottleneck_pricing":12,"market_mispricing":11,"valuation_rerating":12,"capital_allocation":3,"information_confidence":12,"total_proxy":72},"stage_component_tags":{"stage2":["named_customer","supply_contract","memory_wafer_tester"],"stage3":["order_size_to_revenue_conversion"],"stage4b":["MFE90_above_100","post_peak_drawdown_large"],"stage4c":[]}}
{"source_row_type":"trigger","row_type":"trigger","trigger_id":"T_C10_FU127_417500_20240307_Stage2","case_id":"C10_FU127_417500_20240307_JITECH_PRECURSOR_BETA_FAIL","symbol":"417500","company_name":"제이아이테크","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"PRECURSOR_UTILIZATION_RECOVERY_BETA_WITHOUT_DURABLE_ORDER_MARGIN_SURVIVAL","trigger_type":"Stage2","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":5660,"price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/417/417500/2024.csv","profile_path":"atlas/symbol_profiles/417/417500.json","MFE_30D_pct":10.25,"MFE_90D_pct":10.25,"MFE_180D_pct":10.25,"MAE_30D_pct":-23.14,"MAE_90D_pct":-35.87,"MAE_180D_pct":-52.83,"peak_180D_date":"2024-03-08","peak_180D_high":6240,"post_peak_drawdown_180D_pct":-57.21,"positive_or_counterexample":"counterexample","current_profile_verdict":"false_positive_if_precursor_recovery_language_is_promoted_without_customer_volume_and_margin_survival","proposed_profile_action":"material proxy stays Stage2-watch unless customer volume and sustained margin bridge are confirmed; local 4B if trigger is near the immediate post-report peak","calibration_usable":true,"representative_for_aggregate":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|417500|Stage2|2024-03-07","validation_status":"pass","validation_notes":"corporate_action_candidate_dates are 2023-05-22 and 2023-06-12; no overlap with 2024-03-07~D+180 window","raw_component_score_breakdown":{"eps_fcf_visibility":5,"earnings_visibility":7,"bottleneck_pricing":6,"market_mispricing":8,"valuation_rerating":7,"capital_allocation":3,"information_confidence":8,"total_proxy":44},"stage_component_tags":{"stage2":["precursor_recovery_language","utilization_recovery_language"],"stage3":[],"stage4b":["post_report_peak","MAE90_below_minus_30"],"stage4c":[]}}
{"source_row_type":"score_simulation","row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_with_C10_shadow_candidate","case_id":"C10_FU127_083310_20241211_LOT_VACUUM_PUMP_TROUGH_REOPEN","trigger_id":"T_C10_FU127_083310_20241211_Stage2_Actionable","symbol":"083310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","current_profile_verdict":"too_late_if_it_waits_for_accounting_profit_after_customer_capex_reopen_signal","proposed_profile_action":"allow_stage2_actionable_reopen_when_product_route_is_direct_and_price_is_after_earnings_trough","score_total_proxy":65,"positive_or_counterexample":"positive","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"score_simulation","row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_with_C10_shadow_candidate","case_id":"C10_FU127_036810_20240426_FST_CHILLER_PELLICLE_BOUNDARY_4B","trigger_id":"T_C10_FU127_036810_20240426_Stage2_Actionable","symbol":"036810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","current_profile_verdict":"false_positive_if_chiller_pellicle_product_identity_is_promoted_to_durable_memory_recovery_Yellow","proposed_profile_action":"Stage2-Actionable is allowed but attach local_4B once MFE30 approaches 25-30 without named order or margin conversion","score_total_proxy":53,"positive_or_counterexample":"counterexample","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"score_simulation","row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_with_C10_shadow_candidate","case_id":"C10_FU127_083450_20240729_GST_SCRUBBER_CHILLER_DELAYED_REOPEN","trigger_id":"T_C10_FU127_083450_20240729_Stage2","symbol":"083450","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","current_profile_verdict":"false_positive_if_customer_investment_reopen_language_gets_immediate_Yellow_before_margin_print","proposed_profile_action":"keep Stage2-watch until delayed order/revenue conversion appears; do not Green through early -28% MAE","score_total_proxy":52,"positive_or_counterexample":"counterexample","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"score_simulation","row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_with_C10_shadow_candidate","case_id":"C10_FU127_232140_20240424_YC_MEMORY_TESTER_ORDER_FAST_MFE","trigger_id":"T_C10_FU127_232140_20240424_Stage2_Actionable","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","current_profile_verdict":"aligned_positive_but_4B_too_late_if_fast_MFE_not_locked","proposed_profile_action":"credit named memory tester order as Stage2-Actionable; add local 4B after parabolic MFE without follow-on order confirmation","score_total_proxy":72,"positive_or_counterexample":"positive","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"score_simulation","row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_with_C10_shadow_candidate","case_id":"C10_FU127_417500_20240307_JITECH_PRECURSOR_BETA_FAIL","trigger_id":"T_C10_FU127_417500_20240307_Stage2","symbol":"417500","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","current_profile_verdict":"false_positive_if_precursor_recovery_language_is_promoted_without_customer_volume_and_margin_survival","proposed_profile_action":"material proxy stays Stage2-watch unless customer volume and sustained margin bridge are confirmed; local 4B if trigger is near the immediate post-report peak","score_total_proxy":44,"positive_or_counterexample":"counterexample","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"aggregate","row_type":"aggregate","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_family":"MEMORY_RECOVERY_BOUNDARY_ROUTE_CONVERSION_VS_PRODUCT_IDENTITY_PROXY","trigger_count":5,"representative_trigger_count":5,"positive_case_count":2,"counterexample_count":3,"stage4b_overlay_count":4,"stage4c_case_count":0,"avg_MFE_90D_pct":38.76,"avg_MAE_90D_pct":-22.59,"current_profile_error_count":5,"production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"shadow_weight","row_type":"shadow_weight","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","rule_candidate":"C10_MEMORY_RECOVERY_REQUIRES_DIRECT_CONVERSION_BRIDGE_WITH_BOUNDARY_ROUTE_AND_POST_REPRICE_4B_GUARD","direction":"credit direct conversion routes such as named tester orders and post-trough direct equipment reopen; discount product-identity-only chiller/pellicle/scrubber/precursor proxy; require local 4B after fast MFE without follow-on margin/order survival","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"residual_contribution","row_type":"residual_contribution","round":"R2","loop":127,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":5,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["boundary_route_discount_needed","post_reprice_4B_after_fast_MFE","material_proxy_false_positive","staged_entry_required_after_customer_investment_reopen_language"],"new_axis_proposed":"C10_MEMORY_RECOVERY_REQUIRES_DIRECT_CONVERSION_BRIDGE_WITH_BOUNDARY_ROUTE_AND_POST_REPRICE_4B_GUARD","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 10. Batch Ingest Self-Audit
```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
compact_filename_forbidden: complied
production_scoring_changed: false
ready_for_batch_ingest: true
```
## 11. Residual Contribution Summary
```text
new_independent_case_count: 5
reused_case_count: 0
new_symbol_count: 5
new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 3
stage4b_overlay_count: 4
stage4c_case_count: 0
new_axis_proposed: C10_MEMORY_RECOVERY_REQUIRES_DIRECT_CONVERSION_BRIDGE_WITH_BOUNDARY_ROUTE_AND_POST_REPRICE_4B_GUARD
existing_axis_strengthened: stage2_required_bridge; full_4b_requires_non_price_evidence; price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
sector_specific_rule_candidate: L2_MEMORY_RECOVERY_BOUNDARY_ROUTE_DISCOUNT_AND_4B_REPRICE_GUARD
canonical_archetype_rule_candidate: C10_MEMORY_RECOVERY_REQUIRES_DIRECT_CONVERSION_BRIDGE_WITH_BOUNDARY_ROUTE_AND_POST_REPRICE_4B_GUARD
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
## 12. Deferred Coding Agent Handoff Prompt
```text
Do not execute this prompt during the research session.
Later, in a coding-agent batch session, ingest this MD together with other v12 research files.
Validate filename, metadata round/loop consistency, required MFE/MAE fields, canonical_archetype_id, large_sector_id, and hard duplicate key.
If the trigger rows pass validation, include them as candidate C10 representative rows and evaluate the shadow rule:
C10_MEMORY_RECOVERY_REQUIRES_DIRECT_CONVERSION_BRIDGE_WITH_BOUNDARY_ROUTE_AND_POST_REPRICE_4B_GUARD.
Do not change production scoring unless the batch promotion planner accepts the patch across the full v12 corpus.
```
## 13. Next Research State
```text
completed_round = R2
completed_loop = 127
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under_30_representative_rows / C10 rows 13 need_to_30 17 in static No-Repeat Index
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = [
  C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_customer_route,
  C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_followup_new_order_route,
  C11_BATTERY_ORDERBOOK_RERATING_followup_margin_FCF_bridge,
  C01_ORDER_BACKLOG_MARGIN_BRIDGE_followup_new_symbol_only,
  C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_followup_to_50
]
```