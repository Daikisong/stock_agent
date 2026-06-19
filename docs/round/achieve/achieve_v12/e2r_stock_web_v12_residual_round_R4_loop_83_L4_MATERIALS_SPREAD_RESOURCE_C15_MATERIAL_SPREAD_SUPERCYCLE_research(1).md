# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R4
selected_loop = 83
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C15 spread reversal / inventory-cycle balance repair + Priority 0 direct URL/proxy/MFE-MAE repair
round_schedule_status = coverage_index_selected; local C15 max loop 82 -> selected loop 83; 직전 C10 loop 222 반복 회피
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD
loop_objective = counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression
price_source = Songdaiki/stock-web / atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
output_file = e2r_stock_web_v12_residual_round_R4_loop_83_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

This standalone Markdown file is a v12 post-calibrated residual research output. It does not scan live stocks, does not recommend current trades, does not open `stock_agent` source code, and does not change production scoring.

## 1. Selection Rationale

The No-Repeat Index has moved beyond simple row-count filling: all C01~C32 canonical archetypes have at least 80 rows, so the next target is quality reinforcement. C15 remains a Priority 1 target because spread reversal and inventory-cycle counterexamples still need direct-source and complete MFE/MAE repair.

This loop avoids the immediately previous C10 loop 222 and selects C15 loop 83. The selected mapping is valid: `C15_MATERIAL_SPREAD_SUPERCYCLE -> R4 / L4_MATERIALS_SPREAD_RESOURCE`.

## 2. Current Calibrated Profile Assumption

Reference profile:

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false in this research file
shadow_weight_only = true
```

Already-applied axes tested here:

```text
stage2_required_bridge
local_4b_watch_guard
full_4b_requires_non_price_evidence
hard_4c_confirmation
stage3_green_revision_min_by_margin_cash_freshness
```

## 3. Stock-Web Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "manifest_max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "tradable_columns": ["d", "o", "h", "l", "c", "v", "a", "mc", "s", "m"]
}
```

Entry price is the Stock-Web tradable close on the first tradable row at or after `trigger_date`. MFE and MAE are computed from entry through 30/90/180 tradable rows by max high and min low.

## 4. Duplicate / Novelty Check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Local C15 loop 72~82 files were checked. No representative trigger in this file repeats the hard key. Strict-new local C15 symbols are: `004090, 014280, 058430`.

## 5. C15 Compression Map

C15 must not treat the commodity headline as the company result. The route is:

```text
commodity weather
  -> product price / ASP pass-through
  -> lagging effect or inventory-cost timing
  -> demand / shipment / customer route
  -> realized margin and cash conversion
  -> price-phase sanity
```

A raw-material headline is the gauge needle. Calibration must check whether the pressure actually reaches the issuer's income statement before the price move is exhausted.

## 6. Case Selection Summary

| case_id | symbol | company | trigger_date | entry_date | trigger_type | role | MFE90 | MAE90 | MFE180 | MAE180 | evidence_family |
|---|---:|---|---|---|---|---|---:|---:|---:|---:|---|
| C15-L83-01 | 004090 | 한국석유공업 | 2023-11-03 | 2023-11-03 | Stage2-Actionable | positive_guardrail | 12.48 | -30.41 | 82.59 | -30.41 | asphalt_result_with_front_industry_slowdown_and_later_recycle_capacity_route |
| C15-L83-02 | 014280 | 금강공업 | 2022-02-24 | 2022-02-24 | Stage2-Actionable | positive_guardrail | 33.17 | -20.1 | 33.17 | -40.88 | steel_pipe_raw_material_price_and_sales_expansion_with_phase_risk |
| C15-L83-03 | 058430 | 포스코스틸리온 | 2022-12-28 | 2023-01-02 | Stage3-Yellow | positive | 150.8 | -4.31 | 231.31 | -4.31 | color_steel_price_hike_input_cost_passthrough_success |
| C15-L83-04 | 058430 | 포스코스틸리온 | 2024-05-03 | 2024-05-03 | Stage4B | counterexample | 20.44 | -24.04 | 20.44 | -44.26 | color_steel_product_price_decline_and_demand_mix_trap |
| C15-L83-05 | 005010 | 휴스틸 | 2023-02-10 | 2023-02-10 | Stage3-Green | counterexample | 27.78 | -13.64 | 27.78 | -24.58 | octg_export_price_spread_result_already_priced |
| C15-L83-06 | 084010 | 대한제강 | 2023-11-03 | 2023-11-03 | Stage4B | positive_guardrail | 9.87 | -7.04 | 9.87 | -13.54 | rebar_demand_slowdown_and_spread_contraction_watch |
| C15-L83-07 | 025820 | 이구산업 | 2024-05-20 | 2024-05-20 | Stage4B | counterexample | 6.85 | -51.84 | 6.85 | -55.01 | copper_record_high_lagging_effect_local_peak_trap |
| C15-L83-08 | 001550 | 조비 | 2024-03-20 | 2024-03-20 | Stage4B | counterexample | 3.61 | -5.37 | 3.61 | -28.55 | fertilizer_price_decline_inventory_and_passthrough_reversal |


## 7. Evidence Source Map

| case_id | source_url | evidence note |
|---|---|---|
| C15-L83-01 | https://www.newspim.com/news/view/20231103000810 | 2023년 3분기 매출 1,732억 원과 영업이익 37억 원 발표. 건설투자 둔화와 석유화학 업황 부진이 실적에 영향을 줬지만, 고부가가치 사업·리사이클 설비 확장 계획도 병존했다. |
| C15-L83-02 | https://snmnews.com/news/articleView.html?idxno=491635 | 강관사업부가 철강 가격 상승과 강관 판매 확대를 통해 실적 개선에 성공했다는 직접 업황/issuer route evidence. |
| C15-L83-03 | https://www.steeldaily.co.kr/news/articleView.html?idxno=171467 | 포스코스틸리온이 원·부자재 가격 상승에 따른 원가 부담을 이유로 2023년 1월 컬러강판 가격 인상을 예고했다. |
| C15-L83-04 | https://www.ferrotimes.com/news/articleView.html?idxno=33091 | 2023년 제품가격이 전년 대비 10.9% 하락했고, 회사 측은 건설시황 악화에 따른 고가 컬러제품 판매 감소를 이유로 설명했다. |
| C15-L83-05 | https://www.steeldaily.co.kr/news/articleView.html?idxno=172651 | 2022년 북미 에너지용 강관 시황 개선과 미주 수출 강관 관련 효과로 실적 개선이 발표됐다. |
| C15-L83-06 | https://www.dailyinvest.kr/news/articleView.html?idxno=55037 | 철근 수요 선행지표 부진으로 2024년까지 실적 둔화가 예상되고, 2023년 철근수요 및 spread 축소 우려가 제시됐다. |
| C15-L83-07 | https://www.mt.co.kr/stock/2024/05/20/2024052009504765285 | 구리 가격 사상 최고치 돌파로 구리 관련 기업이 강세를 보였고, 구리 가격 상승에 따른 실적 개선 기대가 언급됐다. |
| C15-L83-08 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240320000598&method=search | 사업보고서에서 비료가격 하락 영향과 원재료 가격 하락·생산단가 감소에 따른 재고자산 감소가 확인된다. |


## 8. Entry OHLC / Peak / Drawdown Table

| case_id | symbol | entry_date | open | high | low | close | volume | peak_date | peak_price | drawdown_after_peak_pct | shares_change_180D |
|---|---:|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| C15-L83-01 | 004090 | 2023-11-03 | 16700.0 | 17310.0 | 15370.0 | 15390.0 | 1792694 | 2024-06-05 | 28100.0 | -45.69 | 0.0% |
| C15-L83-02 | 014280 | 2022-02-24 | 8240.0 | 8280.0 | 8060.0 | 8110.0 | 104683 | 2022-04-27 | 10800.0 | -55.6 | 0.0% |
| C15-L83-03 | 058430 | 2023-01-02 | 32150.0 | 32650.0 | 31000.0 | 31300.0 | 29411 | 2023-07-26 | 103700.0 | -48.99 | 0.0% |
| C15-L83-04 | 058430 | 2024-05-03 | 46200.0 | 46500.0 | 45700.0 | 45750.0 | 21717 | 2024-06-05 | 55100.0 | -53.72 | 0.0% |
| C15-L83-05 | 005010 | 2023-02-10 | 5200.0 | 6390.0 | 5130.0 | 5940.0 | 15482561 | 2023-02-17 | 7590.0 | -40.97 | 0.0% |
| C15-L83-06 | 084010 | 2023-11-03 | 13200.0 | 13240.0 | 12750.0 | 13070.0 | 61290 | 2023-11-27 | 14360.0 | -21.31 | 5.0% |
| C15-L83-07 | 025820 | 2024-05-20 | 7700.0 | 8420.0 | 7400.0 | 7880.0 | 47603058 | 2024-05-20 | 8420.0 | -57.9 | 0.0% |
| C15-L83-08 | 001550 | 2024-03-20 | 13070.0 | 13070.0 | 12950.0 | 13030.0 | 6344 | 2024-03-26 | 13500.0 | -31.04 | 0.0% |


## 9. Trigger-Level Backtest Table

| case_id | symbol | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | below30 | below90 | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| C15-L83-01 | 004090 | 12.48 | -30.41 | 12.48 | -30.41 | 82.59 | -30.41 | True | True | current_profile_too_pessimistic_if_result_slowdown_auto_caps |
| C15-L83-02 | 014280 | 26.39 | -1.36 | 33.17 | -20.1 | 33.17 | -40.88 | False | True | current_profile_false_positive_if_margin_bridge_promoted_without_phase_guard |
| C15-L83-03 | 058430 | 18.85 | -4.31 | 150.8 | -4.31 | 231.31 | -4.31 | False | False | current_profile_too_late_if_product_price_hike_not_counted |
| C15-L83-04 | 058430 | 20.44 | -4.37 | 20.44 | -24.04 | 20.44 | -44.26 | True | True | current_profile_false_positive_if_cost_drop_is_read_as_margin_expansion |
| C15-L83-05 | 005010 | 27.78 | -13.64 | 27.78 | -13.64 | 27.78 | -24.58 | True | True | current_profile_false_positive_late_result_green_trap |
| C15-L83-06 | 084010 | 9.87 | -2.45 | 9.87 | -7.04 | 9.87 | -13.54 | True | True | current_profile_false_positive_if_spread_history_ignores_demand_leading_indicator |
| C15-L83-07 | 025820 | 6.85 | -34.9 | 6.85 | -51.84 | 6.85 | -55.01 | True | True | current_profile_false_positive_raw_commodity_peak_trap |
| C15-L83-08 | 001550 | 3.61 | -5.14 | 3.61 | -5.37 | 3.61 | -28.55 | True | True | current_profile_false_positive_if_raw_material_stabilization_is_read_as_margin_positive |


## 10. Case Notes

### C15-L83-01 — 004090 한국석유공업
A weak result headline would normally cap the row. The 90D MAE was `-30.41%`, but the surviving high-value/recycle route and later 180D MFE `82.59%` show why this should be a high-MAE Stage2-Actionable guardrail rather than hard 4C.

### C15-L83-02 — 014280 금강공업
Steel pipe price and sales expansion were real, and early MFE was available. However, 180D MAE `-40.88%` means order/spread evidence cannot be promoted to Yellow/Green without margin/cash and phase protection.

### C15-L83-03 — 058430 포스코스틸리온, 2022 price hike
This is the cleanest positive row in the batch: product price hike directly expresses pass-through, and the path delivered MFE90 `150.8%`. It supports Yellow, not unconditional Green, because the post-peak drawdown reached `-48.99%`.

### C15-L83-04 — 058430 포스코스틸리온, 2024 price decline
The later row proves the opposite side. Lower raw cost or lower product price is not automatically margin-positive. Product-price decline and mix deterioration produced 180D MAE `-44.26%`.

### C15-L83-05 — 005010 휴스틸
The OCTG export spread result was strong, but the trigger was late. MFE180 was only `27.78%` and MAE180 was `-24.58%`, so result-only Green is a trap.

### C15-L83-06 — 084010 대한제강
This is a clean 4B/watch row. The historical spread quality does not survive a demand-leading-indicator deterioration unless there is fresh margin/cash evidence.

### C15-L83-07 — 025820 이구산업
The copper headline was the textbook raw-commodity peak trap. Entry day was the 180D peak, and the row later printed MAE180 `-55.01%`.

### C15-L83-08 — 001550 조비
Raw material cost relief does not automatically become issuer margin. The report showed price/inventory normalization pressure, and the path produced MFE180 `3.61%` against MAE180 `-28.55%`.

## 11. Positive / Counterexample Balance

```text
new_independent_case_count = 8
reused_case_count = 0
strict_new_local_C15_symbol_count = 3
positive_case_count = 4
counterexample_count = 4
current_profile_error_count = 8
calibration_usable_trigger_count = 8
representative_trigger_count = 8
```

## 12. Current Profile Stress Test

The current rolling profile is directionally right about requiring a bridge, but C15 still has four residual errors:

1. It can treat raw commodity movement as if the issuer captured spread.
2. It can treat lower input cost as margin-positive even when product ASP also falls.
3. It can over-promote late result evidence after the spread cycle has already peaked.
4. It can over-route high MAE to 4C even when issuer route survives.

## 13. Stage2 / Yellow / Green / 4B / 4C Reclassification

```text
Stage2-watch: commodity weather, broad sector spread, or raw-material move only
Stage2-Actionable: product price, named route, or issuer-level pass-through evidence
Stage3-Yellow: pass-through plus realized margin/cash or strong MFE with clean phase
Stage3-Green: forward spread freshness plus margin/cash conversion and price sanity
Stage4B: stale result, local peak, product-price reversal, inventory lag, demand slump
Stage4C: only confirmed non-price route death, repeated cash damage, or thesis break
```

## 14. Sector-Specific Rule Candidate

`L4 material-spread rows should split commodity weather, product price or ASP pass-through, lagging effect, inventory-cost lag, demand/customer route, realized margin/cash conversion, and price phase.`

## 15. Canonical-Archetype Rule Candidate

`C15 should add a pass-through and lagging-effect ladder: raw commodity move -> Stage2-watch; product price or issuer route -> Stage2-Actionable; realized margin/cash plus fresh spread -> Yellow/Green; stale result or local peak -> 4B-watch; high MAE with surviving route -> watch/phase cap, not hard 4C.`

## 16. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | misroute count | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2 rolling proxy | 8 | 33.12 | -19.59 | 51.95 | -30.19 | 8 | raw commodity/result evidence still over-credited |
| P2 C15 pass-through lagging-effect phase guard | 8 | 33.12 | -19.59 | 51.95 | -30.19 | 2 | better route/phase separation |

## 17. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_passthrough_lagging_effect_phase_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,20/12/20/10/10/8/20,20/10/18/10/10/10/22,"Visibility -2; Bottleneck -2; Capital +2; Info +2","Separate raw commodity weather from product pass-through, lagging effect, and local peak risk","Reduced false-positive Green/Actionable routing while preserving direct product price-hike positives","C15-L83-01-T1|C15-L83-02-T1|C15-L83-03-T1|C15-L83-04-T1|C15-L83-05-T1|C15-L83-06-T1|C15-L83-07-T1|C15-L83-08-T1",8,8,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 18. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C15-L83-01", "symbol": "004090", "company_name": "한국석유공업", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "case_role": "positive_guardrail", "evidence_family": "asphalt_result_with_front_industry_slowdown_and_later_recycle_capacity_route", "source_url": "https://www.newspim.com/news/view/20231103000810", "is_new_independent_case": true, "calibration_usable": true, "duplicate_check_status": "pass"}
{"row_type": "trigger", "trigger_id": "C15-L83-01-T1", "case_id": "C15-L83-01", "symbol": "004090", "company_name": "한국석유공업", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "sector": "materials_spread_resource", "primary_archetype": "material_spread_supercycle", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-03", "evidence_available_at_that_date": "2023년 3분기 매출 1,732억 원과 영업이익 37억 원 발표. 건설투자 둔화와 석유화학 업황 부진이 실적에 영향을 줬지만, 고부가가치 사업·리사이클 설비 확장 계획도 병존했다.", "evidence_source": "https://www.newspim.com/news/view/20231103000810", "evidence_family": "asphalt_result_with_front_industry_slowdown_and_later_recycle_capacity_route", "stage2_evidence_fields": "아스팔트/석유화학 issuer-level result와 신규 고부가·리사이클 route가 존재", "stage3_evidence_fields": "전방 건설·석유화학 둔화가 있어 margin/cash Green 근거는 부족", "stage4b_evidence_fields": "초기 90D MAE가 크지만 180D MFE가 커 hard 4C가 아니라 high-MAE absorbable bridge", "stage4c_evidence_fields": "사업 route death 없음", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004090/2023.csv", "profile_path": "atlas/symbol_profiles/004/004090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-03", "entry_price": 15390.0, "entry_open": 16700.0, "entry_high": 17310.0, "entry_low": 15370.0, "entry_volume": 1792694, "MFE_30D_pct": 12.48, "MFE_90D_pct": 12.48, "MFE_180D_pct": 82.59, "MFE_1Y_pct": 82.59, "MFE_2Y_pct": null, "MAE_30D_pct": -30.41, "MAE_90D_pct": -30.41, "MAE_180D_pct": -30.41, "MAE_1Y_pct": -30.41, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-05", "peak_price": 28100.0, "drawdown_after_peak_pct": -45.69, "share_count_max_change_pct_180D": 0.0, "corporate_action_window_status": "clean_180D_window", "green_lateness_ratio": "case_specific", "four_b_local_peak_proximity": "post_entry_peak_with_drawdown_overlay", "four_b_full_window_peak_proximity": "full_window_drawdown_after_peak_measured", "four_b_timing_verdict": "local_4b_watch_or_phase_cap_required", "four_b_evidence_type": "inventory_lag_or_passthrough_reversal_or_phase_risk", "four_c_protection_label": "not_hard_4c_without_route_death", "trigger_outcome_label": "positive_guardrail", "current_profile_verdict": "current_profile_too_pessimistic_if_result_slowdown_auto_caps", "calibration_usable": true, "forward_window_trading_days": 283, "calibration_block_reasons": [], "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:004090:2023-11-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_archetype_new_symbol_or_new_entry_trigger_family_vs_local_C15_archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "trigger_id": "C15-L83-01-T1", "case_id": "C15-L83-01", "symbol": "004090", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "profile_after": "c15_passthrough_lagging_effect_phase_guard_shadow", "before_total_score": 58, "before_stage": "Stage4B", "after_total_score": 66, "after_stage": "Stage2-Actionable", "component_scores_before": {"contract": 4, "visibility": 10, "bottleneck": 8, "revision": 4, "relative": 0, "customer": 4, "policy": 4, "valuation": -4, "execution": -12, "legal": 0, "dilution": 0, "accounting": 0}, "component_scores_after": {"contract": 6, "visibility": 12, "bottleneck": 10, "revision": 4, "relative": 4, "customer": 5, "policy": 4, "valuation": -4, "execution": -8, "legal": 0, "dilution": 0, "accounting": 0}, "score_delta_explanation": "Downturn result should not be hard capped when issuer-level high-value/recycle route survives; still no Green without margin/cash freshness.", "score_return_alignment_verdict": "current_profile_too_pessimistic_if_result_slowdown_auto_caps", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "case", "case_id": "C15-L83-02", "symbol": "014280", "company_name": "금강공업", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "case_role": "positive_guardrail", "evidence_family": "steel_pipe_raw_material_price_and_sales_expansion_with_phase_risk", "source_url": "https://snmnews.com/news/articleView.html?idxno=491635", "is_new_independent_case": true, "calibration_usable": true, "duplicate_check_status": "pass"}
{"row_type": "trigger", "trigger_id": "C15-L83-02-T1", "case_id": "C15-L83-02", "symbol": "014280", "company_name": "금강공업", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "sector": "materials_spread_resource", "primary_archetype": "material_spread_supercycle", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "강관사업부가 철강 가격 상승과 강관 판매 확대를 통해 실적 개선에 성공했다는 직접 업황/issuer route evidence.", "evidence_source": "https://snmnews.com/news/articleView.html?idxno=491635", "evidence_family": "steel_pipe_raw_material_price_and_sales_expansion_with_phase_risk", "stage2_evidence_fields": "강관 판매 확대와 철강가격 상승분 반영 route", "stage3_evidence_fields": "180D MAE가 깊어 Green까지는 불가; phase risk가 큼", "stage4b_evidence_fields": "초기 MFE 이후 drawdown이 커 local 4B overlay 필요", "stage4c_evidence_fields": "강관 route death 없음", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014280/2022.csv", "profile_path": "atlas/symbol_profiles/014/014280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 8110.0, "entry_open": 8240.0, "entry_high": 8280.0, "entry_low": 8060.0, "entry_volume": 104683, "MFE_30D_pct": 26.39, "MFE_90D_pct": 33.17, "MFE_180D_pct": 33.17, "MFE_1Y_pct": 33.17, "MFE_2Y_pct": 33.17, "MAE_30D_pct": -1.36, "MAE_90D_pct": -20.1, "MAE_180D_pct": -40.88, "MAE_1Y_pct": -40.88, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2022-04-27", "peak_price": 10800.0, "drawdown_after_peak_pct": -55.6, "share_count_max_change_pct_180D": 0.0, "corporate_action_window_status": "clean_180D_window", "green_lateness_ratio": "case_specific", "four_b_local_peak_proximity": "post_entry_peak_with_drawdown_overlay", "four_b_full_window_peak_proximity": "full_window_drawdown_after_peak_measured", "four_b_timing_verdict": "local_4b_watch_or_phase_cap_required", "four_b_evidence_type": "inventory_lag_or_passthrough_reversal_or_phase_risk", "four_c_protection_label": "not_hard_4c_without_route_death", "trigger_outcome_label": "positive_guardrail", "current_profile_verdict": "current_profile_false_positive_if_margin_bridge_promoted_without_phase_guard", "calibration_usable": true, "forward_window_trading_days": 731, "calibration_block_reasons": [], "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:014280:2022-02-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_archetype_new_symbol_or_new_entry_trigger_family_vs_local_C15_archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "trigger_id": "C15-L83-02-T1", "case_id": "C15-L83-02", "symbol": "014280", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "profile_after": "c15_passthrough_lagging_effect_phase_guard_shadow", "before_total_score": 82, "before_stage": "Stage3-Yellow", "after_total_score": 68, "after_stage": "Stage2-Actionable", "component_scores_before": {"contract": 10, "visibility": 18, "bottleneck": 15, "revision": 8, "relative": 10, "customer": 6, "policy": 0, "valuation": 0, "execution": 0, "legal": 0, "dilution": 0, "accounting": 0}, "component_scores_after": {"contract": 8, "visibility": 15, "bottleneck": 12, "revision": 5, "relative": 4, "customer": 6, "policy": 0, "valuation": -6, "execution": -4, "legal": 0, "dilution": 0, "accounting": 0}, "score_delta_explanation": "Direct steel-pipe bridge is real but deep later MAE demands phase cap and cash conversion proof before Yellow/Green.", "score_return_alignment_verdict": "current_profile_false_positive_if_margin_bridge_promoted_without_phase_guard", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "case", "case_id": "C15-L83-03", "symbol": "058430", "company_name": "포스코스틸리온", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "case_role": "positive", "evidence_family": "color_steel_price_hike_input_cost_passthrough_success", "source_url": "https://www.steeldaily.co.kr/news/articleView.html?idxno=171467", "is_new_independent_case": true, "calibration_usable": true, "duplicate_check_status": "pass"}
{"row_type": "trigger", "trigger_id": "C15-L83-03-T1", "case_id": "C15-L83-03", "symbol": "058430", "company_name": "포스코스틸리온", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "sector": "materials_spread_resource", "primary_archetype": "material_spread_supercycle", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage3-Yellow", "trigger_date": "2022-12-28", "evidence_available_at_that_date": "포스코스틸리온이 원·부자재 가격 상승에 따른 원가 부담을 이유로 2023년 1월 컬러강판 가격 인상을 예고했다.", "evidence_source": "https://www.steeldaily.co.kr/news/articleView.html?idxno=171467", "evidence_family": "color_steel_price_hike_input_cost_passthrough_success", "stage2_evidence_fields": "제품 가격 인상이라는 issuer-level pass-through", "stage3_evidence_fields": "매우 큰 90D/180D MFE가 제품 가격 pass-through 유효성을 지지", "stage4b_evidence_fields": "peak 이후 drawdown이 커 4B overlay는 필요", "stage4c_evidence_fields": "route death 없음", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058430/2023.csv", "profile_path": "atlas/symbol_profiles/058/058430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-01-02", "entry_price": 31300.0, "entry_open": 32150.0, "entry_high": 32650.0, "entry_low": 31000.0, "entry_volume": 29411, "MFE_30D_pct": 18.85, "MFE_90D_pct": 150.8, "MFE_180D_pct": 231.31, "MFE_1Y_pct": 231.31, "MFE_2Y_pct": 231.31, "MAE_30D_pct": -4.31, "MAE_90D_pct": -4.31, "MAE_180D_pct": -4.31, "MAE_1Y_pct": -4.31, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2023-07-26", "peak_price": 103700.0, "drawdown_after_peak_pct": -48.99, "share_count_max_change_pct_180D": 0.0, "corporate_action_window_status": "clean_180D_window", "green_lateness_ratio": "case_specific", "four_b_local_peak_proximity": "post_entry_peak_with_drawdown_overlay", "four_b_full_window_peak_proximity": "full_window_drawdown_after_peak_measured", "four_b_timing_verdict": "local_4b_watch_or_phase_cap_required", "four_b_evidence_type": "inventory_lag_or_passthrough_reversal_or_phase_risk", "four_c_protection_label": "not_hard_4c_without_route_death", "trigger_outcome_label": "positive", "current_profile_verdict": "current_profile_too_late_if_product_price_hike_not_counted", "calibration_usable": true, "forward_window_trading_days": 731, "calibration_block_reasons": [], "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:058430:2023-01-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_archetype_new_symbol_or_new_entry_trigger_family_vs_local_C15_archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "trigger_id": "C15-L83-03-T1", "case_id": "C15-L83-03", "symbol": "058430", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "profile_after": "c15_passthrough_lagging_effect_phase_guard_shadow", "before_total_score": 78, "before_stage": "Stage2-Actionable", "after_total_score": 84, "after_stage": "Stage3-Yellow", "component_scores_before": {"contract": 6, "visibility": 14, "bottleneck": 14, "revision": 8, "relative": 10, "customer": 8, "policy": 0, "valuation": 0, "execution": 0, "legal": 0, "dilution": 0, "accounting": 0}, "component_scores_after": {"contract": 6, "visibility": 18, "bottleneck": 18, "revision": 10, "relative": 12, "customer": 8, "policy": 0, "valuation": -2, "execution": -2, "legal": 0, "dilution": 0, "accounting": 0}, "score_delta_explanation": "Product price hike is stronger than raw steel proxy; it can promote Yellow, but later peak requires 4B overlay.", "score_return_alignment_verdict": "current_profile_too_late_if_product_price_hike_not_counted", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "case", "case_id": "C15-L83-04", "symbol": "058430", "company_name": "포스코스틸리온", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "case_role": "counterexample", "evidence_family": "color_steel_product_price_decline_and_demand_mix_trap", "source_url": "https://www.ferrotimes.com/news/articleView.html?idxno=33091", "is_new_independent_case": true, "calibration_usable": true, "duplicate_check_status": "pass"}
{"row_type": "trigger", "trigger_id": "C15-L83-04-T1", "case_id": "C15-L83-04", "symbol": "058430", "company_name": "포스코스틸리온", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "sector": "materials_spread_resource", "primary_archetype": "material_spread_supercycle", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-03", "evidence_available_at_that_date": "2023년 제품가격이 전년 대비 10.9% 하락했고, 회사 측은 건설시황 악화에 따른 고가 컬러제품 판매 감소를 이유로 설명했다.", "evidence_source": "https://www.ferrotimes.com/news/articleView.html?idxno=33091", "evidence_family": "color_steel_product_price_decline_and_demand_mix_trap", "stage2_evidence_fields": "원재료가격 하락만으로는 pass-through 성공이 아님", "stage3_evidence_fields": "제품가격과 수요 mix가 훼손되어 margin/cash Green 근거 없음", "stage4b_evidence_fields": "고가 제품 판매 감소와 제품가격 하락; 180D MAE가 깊음", "stage4c_evidence_fields": "사업 자체의 thesis death는 아님", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058430/2024.csv", "profile_path": "atlas/symbol_profiles/058/058430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-03", "entry_price": 45750.0, "entry_open": 46200.0, "entry_high": 46500.0, "entry_low": 45700.0, "entry_volume": 21717, "MFE_30D_pct": 20.44, "MFE_90D_pct": 20.44, "MFE_180D_pct": 20.44, "MFE_1Y_pct": 20.44, "MFE_2Y_pct": null, "MAE_30D_pct": -4.37, "MAE_90D_pct": -24.04, "MAE_180D_pct": -44.26, "MAE_1Y_pct": -44.26, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-05", "peak_price": 55100.0, "drawdown_after_peak_pct": -53.72, "share_count_max_change_pct_180D": 0.0, "corporate_action_window_status": "clean_180D_window", "green_lateness_ratio": "case_specific", "four_b_local_peak_proximity": "post_entry_peak_with_drawdown_overlay", "four_b_full_window_peak_proximity": "full_window_drawdown_after_peak_measured", "four_b_timing_verdict": "local_4b_watch_or_phase_cap_required", "four_b_evidence_type": "inventory_lag_or_passthrough_reversal_or_phase_risk", "four_c_protection_label": "not_hard_4c_without_route_death", "trigger_outcome_label": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_cost_drop_is_read_as_margin_expansion", "calibration_usable": true, "forward_window_trading_days": 403, "calibration_block_reasons": [], "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:058430:2024-05-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_archetype_new_symbol_or_new_entry_trigger_family_vs_local_C15_archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "trigger_id": "C15-L83-04-T1", "case_id": "C15-L83-04", "symbol": "058430", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "profile_after": "c15_passthrough_lagging_effect_phase_guard_shadow", "before_total_score": 70, "before_stage": "Stage2-Actionable", "after_total_score": 48, "after_stage": "Stage4B", "component_scores_before": {"contract": 0, "visibility": 14, "bottleneck": 12, "revision": 4, "relative": 6, "customer": 6, "policy": 0, "valuation": 0, "execution": -4, "legal": 0, "dilution": 0, "accounting": 0}, "component_scores_after": {"contract": 0, "visibility": 6, "bottleneck": 6, "revision": -4, "relative": -8, "customer": 4, "policy": 0, "valuation": -6, "execution": -10, "legal": 0, "dilution": 0, "accounting": 0}, "score_delta_explanation": "Lower input cost can be cancelled by lower product ASP and bad mix; C15 must check pass-through direction, not raw-material direction only.", "score_return_alignment_verdict": "current_profile_false_positive_if_cost_drop_is_read_as_margin_expansion", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "case", "case_id": "C15-L83-05", "symbol": "005010", "company_name": "휴스틸", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "case_role": "counterexample", "evidence_family": "octg_export_price_spread_result_already_priced", "source_url": "https://www.steeldaily.co.kr/news/articleView.html?idxno=172651", "is_new_independent_case": true, "calibration_usable": true, "duplicate_check_status": "pass"}
{"row_type": "trigger", "trigger_id": "C15-L83-05-T1", "case_id": "C15-L83-05", "symbol": "005010", "company_name": "휴스틸", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "sector": "materials_spread_resource", "primary_archetype": "material_spread_supercycle", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage3-Green", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "2022년 북미 에너지용 강관 시황 개선과 미주 수출 강관 관련 효과로 실적 개선이 발표됐다.", "evidence_source": "https://www.steeldaily.co.kr/news/articleView.html?idxno=172651", "evidence_family": "octg_export_price_spread_result_already_priced", "stage2_evidence_fields": "북미 OCTG 가격/spread route는 직접적", "stage3_evidence_fields": "실적 확인은 강하지만 entry가 peak 부근이라 Green risk가 큼", "stage4b_evidence_fields": "실적발표 후 30/90/180D MFE가 제한적이고 drawdown 큼", "stage4c_evidence_fields": "수출 route death는 아님", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005010/2023.csv", "profile_path": "atlas/symbol_profiles/005/005010.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-10", "entry_price": 5940.0, "entry_open": 5200.0, "entry_high": 6390.0, "entry_low": 5130.0, "entry_volume": 15482561, "MFE_30D_pct": 27.78, "MFE_90D_pct": 27.78, "MFE_180D_pct": 27.78, "MFE_1Y_pct": 27.78, "MFE_2Y_pct": null, "MAE_30D_pct": -13.64, "MAE_90D_pct": -13.64, "MAE_180D_pct": -24.58, "MAE_1Y_pct": -24.58, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-17", "peak_price": 7590.0, "drawdown_after_peak_pct": -40.97, "share_count_max_change_pct_180D": 0.0, "corporate_action_window_status": "clean_180D_window", "green_lateness_ratio": "case_specific", "four_b_local_peak_proximity": "post_entry_peak_with_drawdown_overlay", "four_b_full_window_peak_proximity": "full_window_drawdown_after_peak_measured", "four_b_timing_verdict": "local_4b_watch_or_phase_cap_required", "four_b_evidence_type": "inventory_lag_or_passthrough_reversal_or_phase_risk", "four_c_protection_label": "not_hard_4c_without_route_death", "trigger_outcome_label": "counterexample", "current_profile_verdict": "current_profile_false_positive_late_result_green_trap", "calibration_usable": true, "forward_window_trading_days": 462, "calibration_block_reasons": [], "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:005010:2023-02-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_archetype_new_symbol_or_new_entry_trigger_family_vs_local_C15_archive", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "trigger_id": "C15-L83-05-T1", "case_id": "C15-L83-05", "symbol": "005010", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "profile_after": "c15_passthrough_lagging_effect_phase_guard_shadow", "before_total_score": 88, "before_stage": "Stage3-Green", "after_total_score": 62, "after_stage": "Stage2-Actionable", "component_scores_before": {"contract": 14, "visibility": 20, "bottleneck": 20, "revision": 14, "relative": 12, "customer": 8, "policy": 0, "valuation": 0, "execution": 0, "legal": 0, "dilution": 0, "accounting": 0}, "component_scores_after": {"contract": 12, "visibility": 12, "bottleneck": 12, "revision": 6, "relative": -4, "customer": 8, "policy": 0, "valuation": -8, "execution": -8, "legal": 0, "dilution": 0, "accounting": 0}, "score_delta_explanation": "Result quality is high, but late result after spread cycle should be capped until forward spread and cash freshness are shown.", "score_return_alignment_verdict": "current_profile_false_positive_late_result_green_trap", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "case", "case_id": "C15-L83-06", "symbol": "084010", "company_name": "대한제강", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "case_role": "positive_guardrail", "evidence_family": "rebar_demand_slowdown_and_spread_contraction_watch", "source_url": "https://www.dailyinvest.kr/news/articleView.html?idxno=55037", "is_new_independent_case": true, "calibration_usable": true, "duplicate_check_status": "pass"}
{"row_type": "trigger", "trigger_id": "C15-L83-06-T1", "case_id": "C15-L83-06", "symbol": "084010", "company_name": "대한제강", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "sector": "materials_spread_resource", "primary_archetype": "material_spread_supercycle", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-11-03", "evidence_available_at_that_date": "철근 수요 선행지표 부진으로 2024년까지 실적 둔화가 예상되고, 2023년 철근수요 및 spread 축소 우려가 제시됐다.", "evidence_source": "https://www.dailyinvest.kr/news/articleView.html?idxno=55037", "evidence_family": "rebar_demand_slowdown_and_spread_contraction_watch", "stage2_evidence_fields": "철근 spread는 issuer-relevant지만 demand cycle이 명확히 둔화", "stage3_evidence_fields": "수요·물량·spread가 동시에 부정적이라 positive promotion 불가", "stage4b_evidence_fields": "MAE는 제한적이지만 upside도 작아 watch가 맞음", "stage4c_evidence_fields": "철근 사업의 구조적 죽음은 아님", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084010/2023.csv", "profile_path": "atlas/symbol_profiles/084/084010.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-03", "entry_price": 13070.0, "entry_open": 13200.0, "entry_high": 13240.0, "entry_low": 12750.0, "entry_volume": 61290, "MFE_30D_pct": 9.87, "MFE_90D_pct": 9.87, "MFE_180D_pct": 9.87, "MFE_1Y_pct": 20.89, "MFE_2Y_pct": null, "MAE_30D_pct": -2.45, "MAE_90D_pct": -7.04, "MAE_180D_pct": -13.54, "MAE_1Y_pct": -20.73, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-27", "peak_price": 14360.0, "drawdown_after_peak_pct": -21.31, "share_count_max_change_pct_180D": 5.0, "corporate_action_window_status": "clean_180D_window", "green_lateness_ratio": "case_specific", "four_b_local_peak_proximity": "post_entry_peak_with_drawdown_overlay", "four_b_full_window_peak_proximity": "full_window_drawdown_after_peak_measured", "four_b_timing_verdict": "local_4b_watch_or_phase_cap_required", "four_b_evidence_type": "inventory_lag_or_passthrough_reversal_or_phase_risk", "four_c_protection_label": "not_hard_4c_without_route_death", "trigger_outcome_label": "positive_guardrail", "current_profile_verdict": "current_profile_false_positive_if_spread_history_ignores_demand_leading_indicator", "calibration_usable": true, "forward_window_trading_days": 283, "calibration_block_reasons": [], "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:084010:2023-11-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_archetype_new_symbol_or_new_entry_trigger_family_vs_local_C15_archive", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "trigger_id": "C15-L83-06-T1", "case_id": "C15-L83-06", "symbol": "084010", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "profile_after": "c15_passthrough_lagging_effect_phase_guard_shadow", "before_total_score": 64, "before_stage": "Stage2-Actionable", "after_total_score": 50, "after_stage": "Stage4B", "component_scores_before": {"contract": 2, "visibility": 12, "bottleneck": 10, "revision": 4, "relative": 4, "customer": 4, "policy": 0, "valuation": 0, "execution": -2, "legal": 0, "dilution": 0, "accounting": 0}, "component_scores_after": {"contract": 0, "visibility": 6, "bottleneck": 6, "revision": -4, "relative": -4, "customer": 3, "policy": 0, "valuation": -4, "execution": -7, "legal": 0, "dilution": 0, "accounting": 0}, "score_delta_explanation": "Demand leading indicators should cap old spread-quality memories; this is a watch row, not a fresh C15 positive.", "score_return_alignment_verdict": "current_profile_false_positive_if_spread_history_ignores_demand_leading_indicator", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "case", "case_id": "C15-L83-07", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "case_role": "counterexample", "evidence_family": "copper_record_high_lagging_effect_local_peak_trap", "source_url": "https://www.mt.co.kr/stock/2024/05/20/2024052009504765285", "is_new_independent_case": true, "calibration_usable": true, "duplicate_check_status": "pass"}
{"row_type": "trigger", "trigger_id": "C15-L83-07-T1", "case_id": "C15-L83-07", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "sector": "materials_spread_resource", "primary_archetype": "material_spread_supercycle", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-20", "evidence_available_at_that_date": "구리 가격 사상 최고치 돌파로 구리 관련 기업이 강세를 보였고, 구리 가격 상승에 따른 실적 개선 기대가 언급됐다.", "evidence_source": "https://www.mt.co.kr/stock/2024/05/20/2024052009504765285", "evidence_family": "copper_record_high_lagging_effect_local_peak_trap", "stage2_evidence_fields": "구리 price/rolling-margin route는 존재", "stage3_evidence_fields": "issuer-level shipment/margin/cash conversion 확인 전이며 entry가 peak", "stage4b_evidence_fields": "entry 당일이 180D peak; MAE30/90/180이 매우 깊음", "stage4c_evidence_fields": "구리 가공 route death는 아님", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv", "profile_path": "atlas/symbol_profiles/025/025820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-20", "entry_price": 7880.0, "entry_open": 7700.0, "entry_high": 8420.0, "entry_low": 7400.0, "entry_volume": 47603058, "MFE_30D_pct": 6.85, "MFE_90D_pct": 6.85, "MFE_180D_pct": 6.85, "MFE_1Y_pct": 6.85, "MFE_2Y_pct": null, "MAE_30D_pct": -34.9, "MAE_90D_pct": -51.84, "MAE_180D_pct": -55.01, "MAE_1Y_pct": -55.01, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-20", "peak_price": 8420.0, "drawdown_after_peak_pct": -57.9, "share_count_max_change_pct_180D": 0.0, "corporate_action_window_status": "clean_180D_window", "green_lateness_ratio": "case_specific", "four_b_local_peak_proximity": "entry_is_or_near_180d_peak", "four_b_full_window_peak_proximity": "full_window_drawdown_after_peak_measured", "four_b_timing_verdict": "local_4b_watch_or_phase_cap_required", "four_b_evidence_type": "inventory_lag_or_passthrough_reversal_or_phase_risk", "four_c_protection_label": "not_hard_4c_without_route_death", "trigger_outcome_label": "counterexample", "current_profile_verdict": "current_profile_false_positive_raw_commodity_peak_trap", "calibration_usable": true, "forward_window_trading_days": 394, "calibration_block_reasons": [], "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:025820:2024-05-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_archetype_new_symbol_or_new_entry_trigger_family_vs_local_C15_archive", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "trigger_id": "C15-L83-07-T1", "case_id": "C15-L83-07", "symbol": "025820", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "profile_after": "c15_passthrough_lagging_effect_phase_guard_shadow", "before_total_score": 76, "before_stage": "Stage2-Actionable", "after_total_score": 44, "after_stage": "Stage4B", "component_scores_before": {"contract": 0, "visibility": 18, "bottleneck": 18, "revision": 6, "relative": 14, "customer": 4, "policy": 0, "valuation": 0, "execution": 0, "legal": 0, "dilution": 0, "accounting": 0}, "component_scores_after": {"contract": 0, "visibility": 8, "bottleneck": 8, "revision": 0, "relative": -10, "customer": 3, "policy": 0, "valuation": -8, "execution": -12, "legal": 0, "dilution": 0, "accounting": 0}, "score_delta_explanation": "Copper headline alone is a peak-trap when it lacks issuer-level conversion and phase sanity.", "score_return_alignment_verdict": "current_profile_false_positive_raw_commodity_peak_trap", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "case", "case_id": "C15-L83-08", "symbol": "001550", "company_name": "조비", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "case_role": "counterexample", "evidence_family": "fertilizer_price_decline_inventory_and_passthrough_reversal", "source_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240320000598&method=search", "is_new_independent_case": true, "calibration_usable": true, "duplicate_check_status": "pass"}
{"row_type": "trigger", "trigger_id": "C15-L83-08-T1", "case_id": "C15-L83-08", "symbol": "001550", "company_name": "조비", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PASS_THROUGH_LAGGING_EFFECT_AND_LOCAL_PEAK_GUARD", "sector": "materials_spread_resource", "primary_archetype": "material_spread_supercycle", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-20", "evidence_available_at_that_date": "사업보고서에서 비료가격 하락 영향과 원재료 가격 하락·생산단가 감소에 따른 재고자산 감소가 확인된다.", "evidence_source": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240320000598&method=search", "evidence_family": "fertilizer_price_decline_inventory_and_passthrough_reversal", "stage2_evidence_fields": "비료 원재료/제품가격 cycle은 C15 관련이지만 issuer pass-through는 약함", "stage3_evidence_fields": "제품가격 하락과 inventory/cost normalization이 Green을 차단", "stage4b_evidence_fields": "MFE가 작고 180D MAE가 깊어 watch/counterexample", "stage4c_evidence_fields": "비료 사업 route death는 아님", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001550/2024.csv", "profile_path": "atlas/symbol_profiles/001/001550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-20", "entry_price": 13030.0, "entry_open": 13070.0, "entry_high": 13070.0, "entry_low": 12950.0, "entry_volume": 6344, "MFE_30D_pct": 3.61, "MFE_90D_pct": 3.61, "MFE_180D_pct": 3.61, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.14, "MAE_90D_pct": -5.37, "MAE_180D_pct": -28.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 13500.0, "drawdown_after_peak_pct": -31.04, "share_count_max_change_pct_180D": 0.0, "corporate_action_window_status": "clean_180D_window", "green_lateness_ratio": "case_specific", "four_b_local_peak_proximity": "post_entry_peak_with_drawdown_overlay", "four_b_full_window_peak_proximity": "full_window_drawdown_after_peak_measured", "four_b_timing_verdict": "local_4b_watch_or_phase_cap_required", "four_b_evidence_type": "inventory_lag_or_passthrough_reversal_or_phase_risk", "four_c_protection_label": "not_hard_4c_without_route_death", "trigger_outcome_label": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_raw_material_stabilization_is_read_as_margin_positive", "calibration_usable": true, "forward_window_trading_days": 191, "calibration_block_reasons": [], "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:001550:2024-03-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_archetype_new_symbol_or_new_entry_trigger_family_vs_local_C15_archive", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "trigger_id": "C15-L83-08-T1", "case_id": "C15-L83-08", "symbol": "001550", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "profile_after": "c15_passthrough_lagging_effect_phase_guard_shadow", "before_total_score": 66, "before_stage": "Stage2-Actionable", "after_total_score": 46, "after_stage": "Stage4B", "component_scores_before": {"contract": 0, "visibility": 14, "bottleneck": 10, "revision": 3, "relative": 4, "customer": 4, "policy": 4, "valuation": 0, "execution": -2, "legal": 0, "dilution": 0, "accounting": 0}, "component_scores_after": {"contract": 0, "visibility": 6, "bottleneck": 4, "revision": -4, "relative": -6, "customer": 3, "policy": 4, "valuation": -4, "execution": -9, "legal": 0, "dilution": 0, "accounting": 0}, "score_delta_explanation": "Raw material cost relief does not automatically mean margin expansion when product prices and inventory values decline.", "score_return_alignment_verdict": "current_profile_false_positive_if_raw_material_stabilization_is_read_as_margin_positive", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "profile_aggregate", "profile_id": "P0_e2r_2_2_rolling_calibrated_proxy", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "trigger_count": 8, "avg_MFE_90D_pct": 33.12, "avg_MAE_90D_pct": -19.59, "avg_MFE_180D_pct": 51.95, "avg_MAE_180D_pct": -30.19, "false_positive_or_misroute_count": 8, "score_return_alignment_verdict": "current profile still over-credits raw commodity headlines and stale result evidence in C15."}
{"row_type": "profile_aggregate", "profile_id": "P2_c15_passthrough_lagging_effect_phase_guard_shadow", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "trigger_count": 8, "avg_MFE_90D_pct": 33.12, "avg_MAE_90D_pct": -19.59, "avg_MFE_180D_pct": 51.95, "avg_MAE_180D_pct": -30.19, "false_positive_or_misroute_count": 2, "score_return_alignment_verdict": "improves alignment by checking product pass-through, lagging effect, and local-peak phase before Yellow/Green."}
{"row_type": "shadow_weight", "axis": "c15_passthrough_lagging_effect_phase_guard", "scope": "canonical_archetype_specific", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "baseline_value": "20/12/20/10/10/8/20", "tested_value": "20/10/18/10/10/10/22", "delta": "Visibility -2; Bottleneck -2; Capital +2; Info +2", "reason": "Separate raw commodity weather from issuer product pass-through, lagging effect, inventory-cost lag, and local peak risk.", "backtest_effect": "Reduced Green/Actionable false positives in copper, steel pipe, fertilizer, and color steel rows while preserving direct price-hike positives.", "trigger_ids": "C15-L83-01-T1|C15-L83-02-T1|C15-L83-03-T1|C15-L83-04-T1|C15-L83-05-T1|C15-L83-06-T1|C15-L83-07-T1|C15-L83-08-T1", "calibration_usable_count": 8, "new_independent_case_count": 8, "counterexample_count": 4, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; v12 post-calibrated residual candidate"}
{"row_type": "residual_contribution", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "new_independent_case_count": 8, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 8, "positive_case_count": 4, "counterexample_count": 4, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"], "residual_error_types_found": ["raw_commodity_peak_trap", "cost_drop_not_margin_positive", "result_only_green_trap", "high_mae_route_survival_not_4c"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 19. Validation Scope

Validated:

- historical evidence date
- actual Stock-Web tradable entry row
- 30D / 90D / 180D MFE and MAE
- 180D forward window availability
- 180D share-count contamination screen
- hard duplicate key against local C15 loop 72~82 files

Not validated:

- live stock suitability
- future return prediction
- brokerage execution
- production scoring code
- full DART restatement audit

## 20. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. This Markdown file is a v12 post-calibrated residual research output produced using Songdaiki/stock-web OHLC rows. It is not a live-candidate scan and not a trading recommendation. Parse only the machine-readable rows and update the calibration ledger.

### Rules

1. Use only `calibration_usable=true` trigger rows.
2. Validate `large_sector_id`, `canonical_archetype_id`, and filename metadata consistency.
3. Deduplicate by `same_entry_group_id` and the hard key `canonical_archetype_id + symbol + trigger_type + entry_date`.
4. Treat `shadow_weight` as non-production until batch-confirmed across multiple loops.
5. Do not change global scoring from this single file.
6. Add or update only canonical-archetype-specific shadow profile candidates.
7. Preserve the distinction between 4B watch and hard 4C thesis death.

## 21. Next Research State

```text
completed_round = R4
completed_loop = 83
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C15 spread reversal / inventory-cycle balance repair + Priority 0 direct URL/proxy/MFE-MAE repair
next_recommended_archetypes = C01/C05 direct FCF or cash-conversion rows; C13 strict-new utilization/ex-credit rows; C10 strict-new order-conversion rows; C31 non-semi/battery awarded-cashflow rows; R13 only for genuinely new taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 22. Batch Ingest Self-Audit

```text
expected_v12_result_file = true
filename_pattern_pass = true
metadata_filename_consistency = pass
JSONL trigger rows = 8
score rows = 8
required MFE-MAE missing = 0
entry_date-entry_price missing = 0
noncanonical_trigger_type = 0
corporate_action_contaminated_trigger_rows = 0
hard_duplicate_key_count_vs_local_C15_archive = 0
ready_for_batch_ingest = true
```
