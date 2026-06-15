# E2R Stock-Web v12 Residual Research — R2 / C07 HBM Equipment Order Relative Strength / loop 130

```yaml
expected_v12_result_file: true
filename: e2r_stock_web_v12_residual_round_R2_loop_130_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
selected_round: R2
selected_loop: 130
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: mixed_c07_hbm_tester_order_demo_route_late_order_high_mae_leaf_set
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_used: false
stock_agent_code_patch_written: false
live_candidate_mode: false
current_stock_discovery_allowed: false
```

## 1. Coverage-index selection

`V12_Research_No_Repeat_Index.md` 기준으로 C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH는 Priority 0 구역이다. 현재 row 수는 18개이고 30-row 최소 안정권까지 12개, 50-row 실전 보정권까지 32개가 비어 있다. 세션 내 직전 산출물은 C02, C09, C14, C10, C06이었으므로 이번 loop는 다음 얇은 C07을 선택했다.

```text
coverage_before: C07 rows 18
new_representative_rows_in_this_md: 5
coverage_after_if_accepted: C07 rows 23
need_to_30_after_if_accepted: 7
need_to_50_after_if_accepted: 27
visible_top_covered_symbols_from_index: 031980, 036810, 036930, 039030, 042700, 067310
selected_symbols_this_loop: 232140, 089030, 092870
hard_duplicate_status: none_observed_from_index_visible_keys
```

Selection logic: C07은 HBM 장비 상대강도와 실제 order/revenue conversion을 분리해야 하는 archetype이다. 이번 표본은 한미반도체/EO/PSK류의 이미 자주 등장하는 central HBM-equipment cluster를 반복하지 않고, memory wafer tester, Cube Prober, CXL/SSD tester의 경계 사례를 잡았다. C07은 작은 불씨가 장비 수주라는 산소를 만나야 불꽃이 되지만, 산소가 너무 늦게 들어오면 이미 방 안은 연기로 가득 찬 뒤일 수 있다. 그래서 이번 loop의 핵심은 **demo-to-volume route는 너무 늦게 보지 말고, late signed order는 너무 쉽게 사지 말자**다.

## 2. Stock-Web price atlas manifest check

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Price basis used for every trigger row:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100
```

Corporate-action profile checks:

| symbol | profile path | relevant corporate-action candidate dates | 180D window status |
|---|---|---|---|
| 232140 | atlas/symbol_profiles/232/232140.json | 2017-04-05 | not_contaminated |
| 089030 | atlas/symbol_profiles/089/089030.json | 2011-12-13, 2011-12-29, 2022-08-01, 2022-08-23 | not_contaminated |
| 092870 | atlas/symbol_profiles/092/092870.json | 2015-10-22, 2024-07-31 | entry selected after 2024-07-31; not_contaminated |

## 3. Evidence source ledger

- C07_R2_L130_001_YC_20240425_GENERIC_MEMORY_TESTER_ORDER: 전자신문, 2024-04-24, 삼성전자 335억원 반도체 검사장비 공급 — https://www.etnews.com/20240424000381
- C07_R2_L130_002_YC_20240730_HBM_TESTER_MEGA_ORDER_LATE: 머니투데이/다음, 2024-07-29, 삼성전자 1017억원 HBM 검사장비 공급계약 — https://v.daum.net/v/1TLSFxdzqq
- C07_R2_L130_003_TECHWING_20240314_CUBE_PROBER_DEMO_ROUTE: 대신증권 스몰캡 탐방노트, 2024-03-14, Cube Prober demo/volume/CAPA Q&A — https://money2.daishin.com/PDF/Out/intranet_data/product/researchcenter/report/2024/03/49391_visit_techwing_240314.pdf
- C07_R2_L130_004_TECHWING_20250117_SAMSUNG_FIRST_ORDER_HIGH_MAE: 빅데이터뉴스, 2025-01-17, 삼성전자 Cube Prober 첫 양산 수주 및 2025 실적 전망 — https://www.thebigdata.co.kr/view.php?ud=202501171415543983edcbfa73b7_23
- C07_R2_L130_005_EXICON_20240930_CXL_SSD_DELAYED_RECOVERY: 더벨, 2024-09-30, CXL 시장 겨냥 엑시콘 테스터 장비 내년 본궤도 — https://m.thebell.co.kr/m/newsview.asp?newskey=202409231437564400102440&svccode=

## 4. Case set summary

| case_id | symbol | trigger | trigger→entry | 90D MFE/MAE | 180D MFE/MAE | role |
|---|---|---|---|---:|---:|---|
| C07_R2_L130_001_YC_20240425_GENERIC_MEMORY_TESTER_ORDER | 232140 와이씨 | Stage2-Actionable | 2024-04-24 → 2024-04-25 | 90.30% / -9.54% | 90.30% / -31.43% | structural_success |
| C07_R2_L130_002_YC_20240730_HBM_TESTER_MEGA_ORDER_LATE | 232140 와이씨 | Stage4B | 2024-07-29 → 2024-07-30 | 16.24% / -49.88% | 16.24% / -49.88% | failed_rerating |
| C07_R2_L130_003_TECHWING_20240314_CUBE_PROBER_DEMO_ROUTE | 089030 테크윙 | Stage2 | 2024-03-14 → 2024-03-14 | 144.14% / -6.21% | 144.14% / -6.21% | missed_structural |
| C07_R2_L130_004_TECHWING_20250117_SAMSUNG_FIRST_ORDER_HIGH_MAE | 089030 테크윙 | Stage2-Actionable | 2025-01-17 → 2025-01-17 | 8.81% / -45.28% | 39.48% / -46.01% | high_mae_success |
| C07_R2_L130_005_EXICON_20240930_CXL_SSD_DELAYED_RECOVERY | 092870 엑시콘 | Stage4C | 2024-09-30 → 2024-09-30 | 21.14% / -35.36% | 21.14% / -35.36% | 4C_success |

### Positive / counterexample balance

```text
new_independent_case_count: 5
reused_case_count: 0
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 5
new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 3
4B_watch_or_overlay_count: 3
4C_watch_or_success_count: 1
current_profile_error_count: 4
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
```

## 5. Case narratives

### 5.1 YC / 와이씨 2024-04-24 — named memory tester order before explicit HBM specificity

전자신문 보도 기준 와이씨는 삼성전자에 335억원 규모 반도체 검사장비를 공급했고, 이 장비는 D램·낸드플래시 등 메모리 반도체를 웨이퍼 상태로 검사하는 장비다. 고객 기반은 삼성전자와 SK하이닉스로 설명된다. 이 trigger는 C07 안에서 `HBM-specific`은 아니지만 **named customer + memory wafer tester + material order size**가 이미 Stage2-Actionable까지는 허용될 수 있음을 보여준다.

Price path는 Stage2 entry로 좋았다. 90D MFE가 +90.30%였고 MAE90은 -9.54%였다. 하지만 180D MAE는 -31.43%까지 열렸다. 즉 첫 수주형 tester rerating은 불이 붙는 속도는 빨랐지만, peak 이후 4B guard가 늦으면 수익이 재가 된다.

### 5.2 YC / 와이씨 2024-07-29 — HBM tester mega order, but late-order high MAE counterexample

7월 29일의 1017억원 HBM 검사장비 공급계약은 형식상 C07이 좋아하는 evidence를 거의 다 갖춘다. 삼성전자, HBM3E/HBM4 대응, 지난해 매출 대비 40% 규모라는 세 요소가 동시에 붙었다. 그런데 entry price는 이미 4월 generic tester order 이후의 상대강도와 6월 peak를 지나온 가격대였다.

결과적으로 entry 후 30D MFE는 +16.24%에 그쳤고 MAE30은 -34.36%, MAE90/180은 -49.88%였다. 이 row는 **contract size가 크더라도, late positive order는 Stage2-Actionable이 아니라 Stage4B watch일 수 있다**는 C07-specific guardrail 후보를 만든다.

### 5.3 Techwing / 테크윙 2024-03-14 — Cube Prober demo-to-volume route before formal order

대신증권 탐방노트는 2024년 3월 당시 Cube Prober 데모 장비가 아직 납품되지 않았다고 적으면서도, 2분기 데모, 하반기 50대 이상 가능성, 월 20대→30대 CAPA, 기존 handler보다 높은 margin 가능성을 동시에 제시했다. formal order는 없지만 C07의 병목 장비에서는 이 정도의 demo-to-volume route가 Stage2 watch로는 충분하다.

이 row는 current profile이 signed order만 기다리면 너무 늦을 수 있음을 보여준다. entry 후 90D/180D MFE는 +144.14%, MAE는 -6.21%에 그쳤다. 단, 이 row도 Green은 아니다. 공식 고객·가격·양산 수주가 비어 있었기 때문에 Stage2 또는 Stage2-Watch가 맞고, Stage3-Green은 이후 signed order/revenue bridge가 필요하다.

### 5.4 Techwing / 테크윙 2025-01-17 — first Samsung order, but painful entry

빅데이터뉴스 보도 기준 한국투자증권은 테크윙이 삼성전자로부터 HBM 검사장비 Cube Prober 첫 양산 수주를 받았다고 분석했고, 2025년 매출과 영업이익 급증 전망도 함께 제시했다. 표면적으로는 Stage2-Actionable evidence다.

하지만 가격경로는 다르다. entry 후 30D MFE는 +8.81%였고 MAE30은 -29.12%, MAE90은 -45.28%, MAE180은 -46.01%였다. 180D MFE는 +39.48%까지 회복했지만, 그 전에 거의 절반에 가까운 drawdown을 견뎌야 했다. 이 row는 **signed order가 늦게 확인된 장비주는 positive가 맞아도 sizing/wait-for-pullback guard가 필요하다**는 high-MAE counterexample이다.

### 5.5 Exicon / 엑시콘 2024-09-30 — CXL/SSD tester delayed recovery is not C07 HBM order

더벨 보도는 엑시콘의 CXL tester option을 설명하면서도, 2024년 상반기 매출이 전년 대비 약 72% 줄었고 BEP를 넘기지 못해 적자전환했다고 적었다. 또한 글로벌 메모리 제조사 투자가 HBM 쪽에 쏠리며 D램/SSD tester 쪽이 타격을 받았고, CXL tester 본격화는 내년으로 밀려 있다고 설명했다.

이 row는 `AI tester`, `CXL`, `삼성전자와 개발`이라는 단어가 있어도 C07로 성급하게 압축하면 안 된다는 반례다. entry 후 90D MFE는 +21.14%까지 있었지만 MAE90은 -35.36%였다. thesis evidence는 Stage4C watch에 가깝다.

## 6. Raw component score breakdown and current-profile stress test

| case_id | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | current profile total | shadow total | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C07_R2_L130_001_YC_20240425_GENERIC_MEMORY_TESTER_ORDER | 16 | 18 | 15 | 11 | 8 | 3 | 7 | 78.0 | 80.0 | current_profile_can_promote_stage2_actionable_but_needs_C07_peak_decay_guard |
| C07_R2_L130_002_YC_20240730_HBM_TESTER_MEGA_ORDER_LATE | 18 | 20 | 18 | 10 | 2 | 3 | 8 | 79.0 | 64.0 | current_profile_false_positive_if_contract_size_alone_promotes_to_actionable_without_relative_strength_decay_guard |
| C07_R2_L130_003_TECHWING_20240314_CUBE_PROBER_DEMO_ROUTE | 14 | 17 | 18 | 14 | 11 | 4 | 6 | 72.0 | 77.0 | current_profile_too_late_if_C07_requires_only_signed_order; allow_watch_with_demo_CAPA_route_but_not_green |
| C07_R2_L130_004_TECHWING_20250117_SAMSUNG_FIRST_ORDER_HIGH_MAE | 19 | 20 | 19 | 8 | 3 | 4 | 8 | 81.0 | 68.0 | current_profile_false_positive_if_late_order_ignores_MAE_guard; stage2_actionable_allowed_only_with_position_size_or_wait_for_pullback |
| C07_R2_L130_005_EXICON_20240930_CXL_SSD_DELAYED_RECOVERY | 4 | 8 | 6 | 6 | 5 | 2 | 9 | 56.0 | 38.0 | current_profile_false_positive_if_CXL_or_AI_tester_vocabulary_is_compressed_into_C07_HBM_order_without_current_order/revenue |

Interpretation:

```text
existing_axis_tested: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened: full_4b_requires_non_price_evidence|high_MAE_guard_after_late_order
existing_axis_weakened: signed_order_only_requirement_for_C07_early_stage2_should_be_softened_when_demo_CAPA_route_is_visible
new_axis_proposed: C07_DEMO_ROUTE_AND_LATE_ORDER_MAE_GATE_V1
loop_contribution_label: canonical_archetype_rule_candidate
```

### Shadow rule candidate — C07_DEMO_ROUTE_AND_LATE_ORDER_MAE_GATE_V1

```yaml
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rule_candidate: C07_DEMO_ROUTE_AND_LATE_ORDER_MAE_GATE_V1
intent: distinguish early demo-to-volume route from late signed-order high-MAE trap
stage2_watch_allow:
  conditions_any:
    - HBM equipment demo delivery timing visible
    - customer qualification route visible
    - capacity expansion tied to specific equipment line
    - margin advantage vs legacy handler/tester disclosed
  required_blockers:
    - no customer cancellation
    - no financing/dilution overhang large enough to dominate
    - entry not after parabolic local peak
stage2_actionable_allow:
  conditions_any:
    - named customer signed order with material value
    - HBM-specific tester/bonder/prober equipment confirmed
    - order-to-sales or revenue-recognition bridge disclosed
  extra_guard:
    - if prior 60D/90D relative strength already extreme and order is late, cap at Stage2-Watch or Stage4B-watch
stage3_green_block:
  if_any:
    - no revenue recognition bridge
    - no margin/revision confirmation
    - customer qualification unresolved
    - signed order only but price already reflects multi-quarter upside
4b_watch_promote:
  if_any:
    - late mega-order after prior rerating
    - high-MAE risk visible from position crowding
    - order amount undisclosed after long expectation cycle
    - valuation blowoff without incremental quantity/margin disclosure
4c_watch_promote:
  if_any:
    - product is CXL/SSD/non-HBM tester while HBM capex is crowding out demand
    - customer line adoption pushed to next year
    - sales collapse or operating loss confirms thesis delay
```

## 7. Trigger rows — machine-readable JSONL

```jsonl
{"row_type":"trigger","round":"R2","loop":130,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"C07_R2_L130_T001","case_id":"C07_R2_L130_001_YC_20240425_GENERIC_MEMORY_TESTER_ORDER","symbol":"232140","company_name":"와이씨","fine_archetype_id":"MEMORY_WAFER_TESTER_NAMED_CUSTOMER_ORDER_NOT_YET_HBM_SPECIFIC","sector":"Semiconductor back-end memory wafer tester","primary_archetype":"HBM equipment order relative strength","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-24","evidence_available_at_that_date":true,"evidence_source":"https://www.etnews.com/20240424000381","stage2_evidence_fields":"customer_named_order|memory_wafer_tester|order_value_to_sales_13pct|Samsung/SK_customer_base","stage3_evidence_fields":"revenue_conversion_visible_but_HBM_specificity_unconfirmed|margin_bridge_pending","stage4b_evidence_fields":"post_entry_peak_drawdown_after_90pct_MFE|late_4B_needed_after_relative_strength","stage4c_evidence_fields":"none","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","entry_date":"2024-04-25","entry_price":12060.0,"MFE_30D_pct":67.08,"MFE_90D_pct":90.3,"MFE_180D_pct":90.3,"MFE_1Y_pct":90.3,"MFE_2Y_pct":null,"MAE_30D_pct":-9.54,"MAE_90D_pct":-9.54,"MAE_180D_pct":-31.43,"MAE_1Y_pct":-31.43,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":22950.0,"drawdown_after_peak_pct":-63.97,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_needed_after_initial_MFE_not_entry_day","four_b_evidence_type":"revision_slowdown|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_with_late_4B_need","current_profile_verdict":"current_profile_can_promote_stage2_actionable_but_needs_C07_peak_decay_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_contaminated_180D_window","same_entry_group_id":"C07_R2_L130_001_YC_20240425_GENERIC_MEMORY_TESTER_ORDER_2024-04-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_score_breakdown":{"eps_fcf":16,"visibility":18,"bottleneck":15,"mispricing":11,"valuation":8,"capital_allocation":3,"information_confidence":7,"profile_total_before_shadow":78.0,"shadow_total_after_rule":80.0}}
{"row_type":"trigger","round":"R2","loop":130,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"C07_R2_L130_T002","case_id":"C07_R2_L130_002_YC_20240730_HBM_TESTER_MEGA_ORDER_LATE","symbol":"232140","company_name":"와이씨","fine_archetype_id":"HBM_TESTER_MEGA_ORDER_LATE_AFTER_PRIOR_RELATIVE_STRENGTH","sector":"HBM memory wafer tester","primary_archetype":"HBM equipment order relative strength","trigger_type":"Stage4B","trigger_date":"2024-07-29","evidence_available_at_that_date":true,"evidence_source":"https://v.daum.net/v/1TLSFxdzqq","stage2_evidence_fields":"named_customer|HBM3E_HBM4_tester|order_value_to_sales_40pct","stage3_evidence_fields":"revenue_bridge_possible_but_customer_HBM_qualification_and_price_extension_risk","stage4b_evidence_fields":"late_after_prior_April_order_rerating|valuation_blowoff|positioning_overheat|peak_next_day","stage4c_evidence_fields":"none","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","entry_date":"2024-07-30","entry_price":16500.0,"MFE_30D_pct":16.24,"MFE_90D_pct":16.24,"MFE_180D_pct":16.24,"MFE_1Y_pct":16.24,"MFE_2Y_pct":null,"MAE_30D_pct":-34.36,"MAE_90D_pct":-49.88,"MAE_180D_pct":-49.88,"MAE_1Y_pct":-49.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":19180.0,"drawdown_after_peak_pct":-56.88,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":0.41,"four_b_full_window_peak_proximity":0.41,"four_b_timing_verdict":"contract_event_should_be_4B_watch_not_new_stage2_actionable","four_b_evidence_type":"valuation_blowoff|positioning_overheat|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"order_backed_but_late_entry_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_contract_size_alone_promotes_to_actionable_without_relative_strength_decay_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_contaminated_180D_window","same_entry_group_id":"C07_R2_L130_002_YC_20240730_HBM_TESTER_MEGA_ORDER_LATE_2024-07-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_score_breakdown":{"eps_fcf":18,"visibility":20,"bottleneck":18,"mispricing":10,"valuation":2,"capital_allocation":3,"information_confidence":8,"profile_total_before_shadow":79.0,"shadow_total_after_rule":64.0}}
{"row_type":"trigger","round":"R2","loop":130,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"C07_R2_L130_T003","case_id":"C07_R2_L130_003_TECHWING_20240314_CUBE_PROBER_DEMO_ROUTE","symbol":"089030","company_name":"테크윙","fine_archetype_id":"CUBE_PROBER_DEMO_TO_VOLUME_ROUTE_BEFORE_FORMAL_ORDER","sector":"HBM Cube Prober / back-end test handler","primary_archetype":"HBM equipment order relative strength","trigger_type":"Stage2","trigger_date":"2024-03-14","evidence_available_at_that_date":true,"evidence_source":"https://money2.daishin.com/PDF/Out/intranet_data/product/researchcenter/report/2024/03/49391_visit_techwing_240314.pdf","stage2_evidence_fields":"demo_timing_visibility|possible_50_units_2H24|monthly_CAPA_20_to_30|higher_margin_than_handler|new_global_IDM_optionality","stage3_evidence_fields":"formal_customer_order_not_yet_available|price_and_margin_under_negotiation","stage4b_evidence_fields":"none_at_entry|later_July_peak_drawdown_requires_local_4B_monitor","stage4c_evidence_fields":"none","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","entry_date":"2024-03-14","entry_price":29000.0,"MFE_30D_pct":34.83,"MFE_90D_pct":144.14,"MFE_180D_pct":144.14,"MFE_1Y_pct":144.14,"MFE_2Y_pct":null,"MAE_30D_pct":-6.21,"MAE_90D_pct":-6.21,"MAE_180D_pct":-6.21,"MAE_1Y_pct":-6.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800.0,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"early_stage2_watch_then_local_4B_after_parabolic_move","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"early_demo_to_volume_route_missed_structural_success","current_profile_verdict":"current_profile_too_late_if_C07_requires_only_signed_order; allow_watch_with_demo_CAPA_route_but_not_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_contaminated_180D_window","same_entry_group_id":"C07_R2_L130_003_TECHWING_20240314_CUBE_PROBER_DEMO_ROUTE_2024-03-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_score_breakdown":{"eps_fcf":14,"visibility":17,"bottleneck":18,"mispricing":14,"valuation":11,"capital_allocation":4,"information_confidence":6,"profile_total_before_shadow":72.0,"shadow_total_after_rule":77.0}}
{"row_type":"trigger","round":"R2","loop":130,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"C07_R2_L130_T004","case_id":"C07_R2_L130_004_TECHWING_20250117_SAMSUNG_FIRST_ORDER_HIGH_MAE","symbol":"089030","company_name":"테크윙","fine_archetype_id":"CUBE_PROBER_FIRST_SAMSUNG_ORDER_LATE_HIGH_MAE","sector":"HBM Cube Prober / Samsung first mass-production order","primary_archetype":"HBM equipment order relative strength","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-17","evidence_available_at_that_date":true,"evidence_source":"https://www.thebigdata.co.kr/view.php?ud=202501171415543983edcbfa73b7_23","stage2_evidence_fields":"Samsung_first_order|HBM_Cube_Prober|qualification_delay_resolved|2025_sales_OP_forecast_step_up","stage3_evidence_fields":"contract_amount_and_quantity_not_disclosed|order_delay_already_known|valuation_and_positioning_risk","stage4b_evidence_fields":"late_order_after_2024_rally|high_entry_price|30D_MAE_over_20pct","stage4c_evidence_fields":"none","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2025.csv","profile_path":"atlas/symbol_profiles/089/089030.json","entry_date":"2025-01-17","entry_price":48250.0,"MFE_30D_pct":8.81,"MFE_90D_pct":8.81,"MFE_180D_pct":39.48,"MFE_1Y_pct":43.11,"MFE_2Y_pct":null,"MAE_30D_pct":-29.12,"MAE_90D_pct":-45.28,"MAE_180D_pct":-46.01,"MAE_1Y_pct":-46.01,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-17","peak_price":67300.0,"drawdown_after_peak_pct":-10.4,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":0.46,"four_b_full_window_peak_proximity":0.46,"four_b_timing_verdict":"late_positive_order_requires_high_MAE_guard","four_b_evidence_type":"positioning_overheat|order_delay|valuation_blowoff","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"order_backed_high_MAE_success_after_long_pain","current_profile_verdict":"current_profile_false_positive_if_late_order_ignores_MAE_guard; stage2_actionable_allowed_only_with_position_size_or_wait_for_pullback","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_contaminated_180D_window","same_entry_group_id":"C07_R2_L130_004_TECHWING_20250117_SAMSUNG_FIRST_ORDER_HIGH_MAE_2025-01-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_score_breakdown":{"eps_fcf":19,"visibility":20,"bottleneck":19,"mispricing":8,"valuation":3,"capital_allocation":4,"information_confidence":8,"profile_total_before_shadow":81.0,"shadow_total_after_rule":68.0}}
{"row_type":"trigger","round":"R2","loop":130,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"C07_R2_L130_T005","case_id":"C07_R2_L130_005_EXICON_20240930_CXL_SSD_DELAYED_RECOVERY","symbol":"092870","company_name":"엑시콘","fine_archetype_id":"CXL_SSD_TESTER_DELAYED_RECOVERY_NOT_HBM_ORDER","sector":"memory/SSD/CXL tester","primary_archetype":"HBM equipment order relative strength","trigger_type":"Stage4C","trigger_date":"2024-09-30","evidence_available_at_that_date":true,"evidence_source":"https://m.thebell.co.kr/m/newsview.asp?newskey=202409231437564400102440&svccode=","stage2_evidence_fields":"CXL_tester_optionality|Samsung_customer_development_route","stage3_evidence_fields":"no_current_HBM_order|CXL_demo_not_yet_line_adopted|SSD_tester_recovery_next_year","stage4b_evidence_fields":"prior_capital_raise_overhang|HBM_capex_shift_hurts_non_HBM_tester","stage4c_evidence_fields":"customer_investment_reduced|1H24_sales_down_72pct|operating_loss|commercialization_timing_pushed_to_next_year","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","profile_path":"atlas/symbol_profiles/092/092870.json","entry_date":"2024-09-30","entry_price":13010.0,"MFE_30D_pct":4.84,"MFE_90D_pct":21.14,"MFE_180D_pct":21.14,"MFE_1Y_pct":41.97,"MFE_2Y_pct":null,"MAE_30D_pct":-21.75,"MAE_90D_pct":-35.36,"MAE_180D_pct":-35.36,"MAE_1Y_pct":-35.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":15760.0,"drawdown_after_peak_pct":-37.88,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B; hard_4C_watch_from_non_price_evidence","four_b_evidence_type":"capital_raise_or_overhang|margin_or_backlog_slowdown","four_c_protection_label":"hard_4c_success_with_interim_bounce_risk","trigger_outcome_label":"non_HBM_tester_false_positive_or_4C_watch","current_profile_verdict":"current_profile_false_positive_if_CXL_or_AI_tester_vocabulary_is_compressed_into_C07_HBM_order_without_current_order/revenue","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_contaminated_180D_window","same_entry_group_id":"C07_R2_L130_005_EXICON_20240930_CXL_SSD_DELAYED_RECOVERY_2024-09-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_score_breakdown":{"eps_fcf":4,"visibility":8,"bottleneck":6,"mispricing":6,"valuation":5,"capital_allocation":2,"information_confidence":9,"profile_total_before_shadow":56.0,"shadow_total_after_rule":38.0}}
```

## 8. Aggregate score-return alignment

```json
{
  "row_type": "aggregate",
  "round": "R2",
  "loop": 130,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "representative_trigger_count": 5,
  "calibration_usable_trigger_count": 5,
  "positive_case_count": 2,
  "counterexample_count": 3,
  "stage2_like_rows": 3,
  "stage2_like_MFE90_ge_20_count": 2,
  "stage2_like_MAE90_le_minus20_count": 1,
  "stage4b_or_4c_rows": 2,
  "current_profile_error_count": 4,
  "avg_representative_MFE90_pct": 56.33,
  "avg_representative_MAE90_pct": -29.21,
  "main_residual_error": "C07 signed-order evidence is not monotonic; early demo/CAPA route can be valuable, late mega-order can be high-MAE trap.",
  "shadow_rule_candidate": "C07_DEMO_ROUTE_AND_LATE_ORDER_MAE_GATE_V1"
}
```

## 9. Residual contribution summary

```text
diversity_score_summary: C07 is Priority 0 with only 18 representative rows. This loop adds three non-top-covered symbols and five new trigger families: generic memory wafer tester order, HBM tester mega order, Cube Prober demo-to-volume route, first Samsung Cube Prober order, and CXL/SSD tester delayed recovery.
sector_specific_rule_candidate: L2_HBM_EQUIPMENT_ORDER_TIMING_AND_MAE_GUARD_V1
canonical_archetype_rule_candidate: C07_DEMO_ROUTE_AND_LATE_ORDER_MAE_GATE_V1
new_axis_proposed: c07_demo_route_and_late_order_mae_gate
existing_axis_strengthened: full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage|hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: signed_order_only_requirement_for_C07_early_stage2
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

One-line contribution:

```text
This loop adds 5 new independent cases, 3 counterexamples, and 4 residual errors for R2/L2/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research session.

```text
You are the coding agent for Songdaiki/stock_agent. Ingest this standalone v12 research MD together with other v12 result MDs. Do not trust narrative summaries alone. Parse only row_type="trigger" JSONL rows that pass strict v12 validation: standard filename, metadata round/loop consistency, canonical trigger_type, entry_date, entry_price, stock-web price source fields, tradable_raw/raw_unadjusted_marcap basis, 30/90/180D MFE and MAE fields, non-contaminated corporate-action window, same_entry_group_id, dedupe_for_aggregate, aggregate_group_role, and calibration_usable=true.

For this MD, evaluate the proposed shadow rule C07_DEMO_ROUTE_AND_LATE_ORDER_MAE_GATE_V1. Treat it as canonical_archetype-specific only. Do not loosen Stage3-Green global thresholds. Candidate implementation direction:
1. Add a C07-specific Stage2-Watch soft allowance when demo delivery timing + capacity route + margin advantage are visible even before signed order.
2. Add a C07 late-order high-MAE guard when a signed order arrives after prior parabolic relative strength or after previous order-driven peak.
3. Block CXL/SSD/non-HBM tester narratives from C07 actionable promotion unless current customer order/revenue conversion is visible.
4. Keep Green locked behind revenue recognition, margin/revision bridge, and customer qualification confirmation.
5. Run the v12 batch promotion decision pipeline. Apply only if this rule improves C07 residual false positive/high-MAE behavior without increasing missed structural positives.
```

## 11. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 12. Next research state

```text
completed_round = R2
completed_loop = 130
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING|C01_ORDER_BACKLOG_MARGIN_BRIDGE|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION
```
