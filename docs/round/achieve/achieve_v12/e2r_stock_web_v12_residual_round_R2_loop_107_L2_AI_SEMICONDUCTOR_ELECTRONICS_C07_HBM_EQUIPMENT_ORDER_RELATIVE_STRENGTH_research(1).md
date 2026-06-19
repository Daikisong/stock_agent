---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 107
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE
deep_sub_archetype_id: C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
created_at_kst: 2026-06-13T09:29:26.913082
---

# E2R Stock-Web v12 Residual Research — R2 / C07 HBM Equipment Order Relative Strength

## 0. Executive Summary

This standalone MD follows the v12 Stock-Web historical calibration prompt. It does not create a live watchlist, does not patch `stock_agent`, and does not change production scoring. The purpose is to add C07 residual evidence: where HBM/equipment relative strength was actually supported by order or revenue conversion, and where the market merely rented the HBM label before a drawdown.

- **Selected target:** `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`
- **Reason:** No-Repeat Index Priority 0 shows C07 has 18 rows, still below the 30-row minimum coverage target.
- **Loop:** existing visible C07 standard result file is loop 106; this file uses loop 107.
- **New independent cases:** 7
- **Usable trigger rows:** 8
- **Representative trigger rows:** 7
- **Positive cases:** 2
- **Counterexamples:** 5
- **Current profile residual errors:** 5
- **Rule candidate:** require verified C07 order / QA-to-mass-production / revenue conversion bridge before Stage3-Yellow or Green; route late single-contract and theme-substitution triggers to local 4B watch.

## 1. Stock-Web Price Source Validation

The run uses `Songdaiki/stock-web` tradable OHLCV shards, upstream `FinanceData/marcap`, raw/unadjusted OHLC, and manifest `max_date=2026-02-20`. Each trigger has a full 180-trading-day forward window inside the Stock-Web manifest date.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 2. Coverage-Index Selection

C07 is Priority 0 in the No-Repeat Index: 18 rows, 12 rows needed to reach 30, 32 rows needed to reach 50. The prior visible C07 file under `docs/round` is loop 106, so the selected loop is 107.

```text
selected_round = R2
selected_loop = 107
selected_priority_bucket = Priority 0
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE
deep_sub_archetype_id = C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS
```

## 3. Hypothesis

C07 should not be a pure “HBM equipment relative strength” score. The useful distinction is narrower:

1. **Positive C07 bridge:** order, QA-to-mass-production route, or process bottleneck revenue bridge is visible before the entry.
2. **Residual false positive:** the label says HBM/CXL/AI equipment, but the trigger is only theme substitution, late single-contract confirmation, customer qualification without revenue bridge, or price-only blowoff.
3. **4B watch path:** when the first verified contract appears after the local peak or after a large theme run, it should often become local 4B watch rather than Stage3-Yellow.

This loop therefore tests whether C07 needs a canonical rule: `verified_order_or_revenue_conversion_bridge_required_before_Yellow`, with `single_contract_scale_guard` and `theme_substitution_block`.

## 4. Evidence Source Map

| Symbol | Company | Evidence route | Why it belongs in C07 |
|---|---|---|---|
| 281820 | 케이씨텍 | ChosunBiz, 2024-01-04 | HBM increases CMP process intensity; KC Tech has domestic CMP equipment/slurry exposure. |
| 253590 | 네오셈 | TheBell, 2024-06-05 | HBM tester delivery / QA-stage evidence. |
| 092870 | 엑시콘 | Edaily/Daum, 2024-05-02; ZDNet Korea, 2024-07-04 | memory/CXL tester order conversion but HBM direct bridge is weaker and timing becomes late. |
| 064290 | 인텍플러스 | DailyInvest, 2024-07-16 | HBM inspection-equipment expectation without confirmed revenue bridge at entry. |
| 322310 | 오로스테크놀로지 | TheElec, 2024-05-16 | direct HBM PAD overlay equipment order, but late trigger / limited scale. |
| 083450 | GST | ChosunBiz/Daum, 2024-03-12 | AI cooling narrative substituted for equipment-order conversion; useful 4B guard. |
| 348210 | 넥스틴 | Yonhap, 2024-11-01 | HBM inspection-equipment qualification narrative without order/revenue bridge. |

## 5. Trigger-Level Backtest Summary

| Symbol | Company | Trigger | Entry | Entry Price | MFE90 | MAE90 | MFE180 | MAE180 | Current Profile Verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 281820 | 케이씨텍 | Stage2-Actionable | 2024-01-04 | 31550 | 71.47 | -14.10 | 87.00 | -14.10 | current_profile_missed_structural_or_too_conservative |
| 253590 | 네오셈 | Stage2-Actionable | 2024-06-05 | 11280 | 53.10 | -34.22 | 53.10 | -34.22 | current_profile_correct_if_green_blocked |
| 092870 | 엑시콘 | Stage2-Actionable | 2024-05-03 | 20100 | 25.12 | -50.25 | 25.12 | -58.16 | current_profile_too_early_if_yellow |
| 064290 | 인텍플러스 | Stage3-Yellow | 2024-07-16 | 21600 | 1.39 | -57.31 | 1.39 | -63.06 | current_profile_false_positive |
| 322310 | 오로스테크놀로지 | Stage3-Yellow | 2024-05-17 | 29100 | 5.50 | -48.01 | 5.50 | -54.71 | current_profile_false_positive_late_trigger |
| 083450 | GST | Stage4B | 2024-03-15 | 55100 | 11.62 | -70.94 | 11.62 | -77.11 | current_profile_4B_too_late_if_treated_as_yellow |
| 348210 | 넥스틴 | Stage2-Actionable | 2024-11-01 | 66000 | 5.30 | -28.18 | 5.30 | -31.14 | current_profile_false_positive_if_yellow |

## 6. Positive / Counterexample Balance

Positive cases are not defined by a positive story; they require forward price behavior that did not immediately punish the bridge. In this loop only **케이씨텍** and **네오셈** survive as positive or positive-high-MAE C07 cases. The rest are residual counterexamples, most of them created by late evidence, small-scale direct contracts, qualification-only narratives, or AI equipment theme substitution.

```text
positive_case_count = 2
counterexample_count = 5
stage4b_case_count = 1
stage4c_case_count = 0
current_profile_error_count = 5
```

## 7. Case Notes

### 7.1 케이씨텍 — positive process bridge

The HBM process mechanism is clean: stacked DRAM increases TSV and planarization intensity, which makes CMP a real process bottleneck rather than a loose theme. The entry did not have a single HBM order disclosure, so the correct state is not Green. But the 90D/180D path supports Stage2-Actionable moving to Yellow when the process bridge and customer route are both present.

### 7.2 네오셈 — positive but QA-to-mass-production lag

The HBM tester evidence is closer to C07 than most broad equipment narratives. The issue is that QA-stage delivery is not the same as mass-production revenue conversion. MFE was strong, but MAE became large after the peak. This supports a rule that Yellow may be allowed, but Green should require mass-production or revision bridge.

### 7.3 엑시콘 — memory tester contract does not automatically equal HBM bridge

A Samsung tester contract and later CXL tester supply route created a plausible C07 narrative. The Stock-Web path shows why the rule needs a scale and timing guard: after contract/confirmation, the stock had limited additional MFE but a severe 90D/180D drawdown.

### 7.4 인텍플러스 — expectation-only inspection equipment

HBM inspection equipment expectation did not protect the entry. The trigger was at/near the local peak. This should not be Stage3-Yellow unless a verified order/revenue bridge exists.

### 7.5 오로스테크놀로지 — direct HBM order but late price

This is the most important counterexample. It has direct HBM PAD overlay evidence, yet the forward path was poor because entry timing was late and scale was limited. C07 therefore needs a late-single-contract guard, not just a yes/no HBM evidence flag.

### 7.6 GST — theme substitution 4B guard

AI server cooling is not HBM equipment order conversion. The stock-web route shows local peak proximity and severe post-peak drawdown. This row strengthens local 4B watch and theme substitution block.

### 7.7 넥스틴 — qualification without order bridge

HBM inspection qualification can be a valid early-stage signal, but in this entry it was not enough for Yellow. The forward path supports Stage2-Watch unless order/revenue conversion appears.

## 8. Score / Return Alignment

P0 selected too many cases because it still allowed relative strength and customer-quality narratives to substitute for actual C07 conversion. P2 is stricter and produces better alignment in this loop, though the sample remains small.

| Profile | Eligible | Avg MFE90 | Avg MAE90 | Avg MFE180 | Avg MAE180 | Verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 current calibrated proxy | 7 | 24.79 | -43.29 | 27.00 | -47.50 | weak alignment, high drawdown |
| P1 sector candidate | 4 | 38.80 | -36.64 | 42.68 | -40.30 | improved but still high MAE |
| P2 canonical C07 candidate | 2 | 62.28 | -24.16 | 70.05 | -24.16 | best alignment, sample small |
| P3 counterexample guard | 3 | 49.90 | -32.86 | 55.07 | -35.49 | safer than P0 |

## 9. Candidate Shadow Rule

```text
new_axis_proposed = C07_verified_order_or_revenue_conversion_bridge_required_before_Yellow_plus_HBM_equipment_RS_4B_watch_after_local_blowoff
```

Rule sketch:

```text
if canonical_archetype_id == C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH:
    require one of:
      - verified HBM/CXL tester or HBM process equipment order with material scale
      - QA-stage delivery plus explicit route to mass-production revenue
      - CMP / process bottleneck evidence plus major-memory customer route and revision/margin bridge
    before Stage3-Yellow.

    block Stage3-Green unless:
      - order-to-revenue conversion or revision bridge is visible;
      - customer route is not merely qualification;
      - local price blowoff has not already consumed the trigger.

    route to local 4B watch when:
      - direct contract is small/late after a prior rerating;
      - evidence is only beneficiary/qualification narrative;
      - AI cooling or generic equipment theme substitutes for HBM order conversion.
```

## 10. Existing Applied Axis Treatment

```text
existing_axis_tested:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage3_yellow_total_min
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
```

This loop does not propose a global threshold change. It proposes a C07 canonical bridge requirement and a local 4B watch rule.

## 11. Coverage Matrix

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE
positive_case_count = 2
counterexample_count = 5
4B_case_count = 1
4C_case_count = 0
new_independent_case_count = 7
reused_case_count = 0
calibration_usable_trigger_count = 8
representative_trigger_count = 7
current_profile_error_count = 5
sector_rule_candidate = true
canonical_rule_candidate = true
coverage_gap_after_this_loop = C07 rows 18 -> 25 estimated before next index refresh
```

## 12. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C07-107-281820","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C07-107-281820-S2A-20240104","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_structural_hbm_process_equipment","current_profile_verdict":"current_profile_missed_structural_or_too_conservative","price_source":"Songdaiki/stock-web","notes":"new symbol / new trigger-family for C07 loop107; no exact duplicate key reused"}
{"row_type":"case","case_id":"C07-107-253590","symbol":"253590","company_name":"네오셈","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","case_type":"structural_success_high_MAE","positive_or_counterexample":"positive","best_trigger":"C07-107-253590-S2A-20240605","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_high_MAE_due_QA_to_mass_production_lag","current_profile_verdict":"current_profile_correct_if_green_blocked","price_source":"Songdaiki/stock-web","notes":"new symbol / new trigger-family for C07 loop107; no exact duplicate key reused"}
{"row_type":"case","case_id":"C07-107-092870","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","case_type":"counterexample_high_MAE_contract_proxy","positive_or_counterexample":"counterexample","best_trigger":"C07-107-092870-S2A-20240503","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MAE_after_contract_proxy","current_profile_verdict":"current_profile_too_early_if_yellow","price_source":"Songdaiki/stock-web","notes":"new symbol / new trigger-family for C07 loop107; no exact duplicate key reused"}
{"row_type":"case","case_id":"C07-107-064290","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","case_type":"counterexample_expectation_only","positive_or_counterexample":"counterexample","best_trigger":"C07-107-064290-S3Y-20240716","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_expectation_only_no_order_revenue_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new symbol / new trigger-family for C07 loop107; no exact duplicate key reused"}
{"row_type":"case","case_id":"C07-107-322310","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","case_type":"counterexample_late_direct_order","positive_or_counterexample":"counterexample","best_trigger":"C07-107-322310-S3Y-20240517","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_direct_order_but_late_price","current_profile_verdict":"current_profile_false_positive_late_trigger","price_source":"Songdaiki/stock-web","notes":"new symbol / new trigger-family for C07 loop107; no exact duplicate key reused"}
{"row_type":"case","case_id":"C07-107-083450","symbol":"083450","company_name":"GST","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","case_type":"counterexample_4B_theme_substitution","positive_or_counterexample":"counterexample","best_trigger":"C07-107-083450-S4B-20240315","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage4b_success_high_MAE_guardrail","current_profile_verdict":"current_profile_4B_too_late_if_treated_as_yellow","price_source":"Songdaiki/stock-web","notes":"new symbol / new trigger-family for C07 loop107; no exact duplicate key reused"}
{"row_type":"case","case_id":"C07-107-348210","symbol":"348210","company_name":"넥스틴","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","case_type":"counterexample_qualification_only","positive_or_counterexample":"counterexample","best_trigger":"C07-107-348210-S2A-20241101","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_qualification_without_order_bridge","current_profile_verdict":"current_profile_false_positive_if_yellow","price_source":"Songdaiki/stock-web","notes":"new symbol / new trigger-family for C07 loop107; no exact duplicate key reused"}
{"row_type":"trigger","trigger_id":"C07-107-281820-S2A-20240104","case_id":"C07-107-281820","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","deep_sub_archetype_id":"C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS","loop_objective":"coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-04","entry_date":"2024-01-04","entry_price":31550.0,"evidence_available_at_that_date":"HBM 생산량 증가가 TSV/CMP 공정 반복수요를 키우며, 케이씨텍은 국내 CMP 장비/슬러리 exposure가 확인된 상태. 직접 HBM order 공시는 아니지만 C07 장비 상대강도 positive proxy로 쓸 수 있음.","evidence_source":"https://biz.chosun.com/it-science/ict/2024/01/04/AUIFS2XEDRCO7OYVSMDWVX7M7M/","stage2_evidence_fields":["HBM_CMP_process_intensity","domestic_CMP_equipment_and_slurry_exposure","major_memory_customer_route"],"stage3_evidence_fields":["process_bottleneck_linkage","relative_strength_with_forward_MFE"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv","profile_path":"atlas/symbol_profiles/281/281820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.49,"MFE_90D_pct":71.47,"MFE_180D_pct":87.0,"MAE_30D_pct":-14.1,"MAE_90D_pct":-14.1,"MAE_180D_pct":-14.1,"peak_date":"2024-07-11","peak_price":59000.0,"drawdown_after_peak_pct":-50.08,"green_lateness_ratio":0.28,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"positive_structural_hbm_process_equipment","current_profile_verdict":"current_profile_missed_structural_or_too_conservative","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_universe_proxy","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|281820|Stage2-Actionable|2024-01-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07-107-253590-S2A-20240605","case_id":"C07-107-253590","symbol":"253590","company_name":"네오셈","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","deep_sub_archetype_id":"C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS","loop_objective":"coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":11280.0,"evidence_available_at_that_date":"회사 측 HBM용 BX burn-in tester 납품 및 QA 단계가 확인됨. 양산 매출 전환은 아직 조건부라 Green이 아니라 Actionable/Yellow 경계로 분류.","evidence_source":"https://www.thebell.co.kr/front/newsview.asp?key=202406050911561880105029","stage2_evidence_fields":["verified_HBM_tester_delivery","QA_stage_customer_route","memory_burn_in_tester_revenue_bucket"],"stage3_evidence_fields":["customer_conversion_optional","order_to_revenue_bridge_partial"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv","profile_path":"atlas/symbol_profiles/253/253590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.1,"MFE_90D_pct":53.1,"MFE_180D_pct":53.1,"MAE_30D_pct":-15.96,"MAE_90D_pct":-34.22,"MAE_180D_pct":-34.22,"peak_date":"2024-07-04","peak_price":17270.0,"drawdown_after_peak_pct":-57.04,"green_lateness_ratio":0.2,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"positive_but_high_MAE_due_QA_to_mass_production_lag","current_profile_verdict":"current_profile_correct_if_green_blocked","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_universe_proxy","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|253590|Stage2-Actionable|2024-06-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07-107-092870-S2A-20240503","case_id":"C07-107-092870","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","deep_sub_archetype_id":"C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS","loop_objective":"coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-02","entry_date":"2024-05-03","entry_price":20100.0,"evidence_available_at_that_date":"삼성전자와 43.7억원 규모 SSD Tester 공급계약. memory tester order bridge는 있으나 HBM tester direct bridge가 아니고 규모도 제한적.","evidence_source":"https://v.daum.net/v/08ouKxqyai?f=p","stage2_evidence_fields":["verified_semiconductor_tester_contract","major_customer_Samsung","memory_tester_adjacency"],"stage3_evidence_fields":["order_bridge_exists_but_not_HBM_direct"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.92,"MFE_90D_pct":25.12,"MFE_180D_pct":25.12,"MAE_30D_pct":-9.55,"MAE_90D_pct":-50.25,"MAE_180D_pct":-58.16,"peak_date":"2024-07-08","peak_price":25150.0,"drawdown_after_peak_pct":-66.56,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"high_MAE_after_contract_proxy","current_profile_verdict":"current_profile_too_early_if_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_universe_proxy","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|092870|Stage2-Actionable|2024-05-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07-107-092870-S3Y-20240704","case_id":"C07-107-092870","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","deep_sub_archetype_id":"C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS","loop_objective":"coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-04","entry_date":"2024-07-04","entry_price":22550.0,"evidence_available_at_that_date":"삼성전자 CXL 2.0 양산용 tester 도입 보도에서 엑시콘/네오셈 공급이 언급됨. CXL memory tester conversion은 있으나 이미 주가가 선행한 뒤의 late trigger.","evidence_source":"https://zdnet.co.kr/view/?no=20240704084503","stage2_evidence_fields":["CXL_memory_tester_vendor_selected","major_customer_route"],"stage3_evidence_fields":["tester_conversion_narrative","relative_strength_after_prior_contract"],"stage4b_evidence_fields":["late_price_confirmation_after_local_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.53,"MFE_90D_pct":11.53,"MFE_180D_pct":11.53,"MAE_30D_pct":-50.11,"MAE_90D_pct":-56.59,"MAE_180D_pct":-62.71,"peak_date":"2024-07-08","peak_price":25150.0,"drawdown_after_peak_pct":-66.56,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":0.06,"four_b_full_window_peak_proximity":0.02,"trigger_outcome_label":"late_yellow_false_positive","current_profile_verdict":"current_profile_false_positive_late_trigger","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_universe_proxy","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|092870|Stage3-Yellow|2024-07-04","dedupe_for_aggregate":false,"aggregate_group_role":"supplemental_same_case_late_trigger","is_new_independent_case":false,"reuse_reason":"same_case_later_trigger_not_counted_as_new_case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"C07-107-064290-S3Y-20240716","case_id":"C07-107-064290","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","deep_sub_archetype_id":"C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS","loop_objective":"coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-16","entry_date":"2024-07-16","entry_price":21600.0,"evidence_available_at_that_date":"HBM 검사장비 추가 수주 기대/검사장비 사업 설명은 존재하지만, 2H24 매출 전환과 margin bridge가 확인되기 전의 expectation-heavy trigger.","evidence_source":"https://www.dailyinvest.kr/news/articleView.html?idxno=59633","stage2_evidence_fields":["HBM_inspection_equipment_expectation","advanced_packaging_inspection_exposure"],"stage3_evidence_fields":["expected_reorder_not_yet_revenue_bridge"],"stage4b_evidence_fields":["expectation_only_after_prior_theme_run"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.39,"MFE_90D_pct":1.39,"MFE_180D_pct":1.39,"MAE_30D_pct":-31.44,"MAE_90D_pct":-57.31,"MAE_180D_pct":-63.06,"peak_date":"2024-07-16","peak_price":21900.0,"drawdown_after_peak_pct":-63.56,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"counterexample_expectation_only_no_order_revenue_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_universe_proxy","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|064290|Stage3-Yellow|2024-07-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07-107-322310-S3Y-20240517","case_id":"C07-107-322310","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","deep_sub_archetype_id":"C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS","loop_objective":"coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":29100.0,"evidence_available_at_that_date":"HBM용 PAD overlay 장비의 삼성전자 48억원 공급 보도. 직접성이 높지만 단일 계약 규모/late trigger/valuation 선행을 같이 봐야 함.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=27898","stage2_evidence_fields":["verified_HBM_PAD_overlay_equipment_supply","Samsung_customer_route","process_yield_bottleneck"],"stage3_evidence_fields":["direct_order_but_scale_limited","late_relative_strength"],"stage4b_evidence_fields":["single_contract_after_local_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","profile_path":"atlas/symbol_profiles/322/322310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.5,"MFE_90D_pct":5.5,"MFE_180D_pct":5.5,"MAE_30D_pct":-25.6,"MAE_90D_pct":-48.01,"MAE_180D_pct":-54.71,"peak_date":"2024-05-17","peak_price":30700.0,"drawdown_after_peak_pct":-57.07,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"counterexample_direct_order_but_late_price","current_profile_verdict":"current_profile_false_positive_late_trigger","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_universe_proxy","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|322310|Stage3-Yellow|2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07-107-083450-S4B-20240315","case_id":"C07-107-083450","symbol":"083450","company_name":"GST","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","deep_sub_archetype_id":"C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS","loop_objective":"coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-03-12","entry_date":"2024-03-15","entry_price":55100.0,"evidence_available_at_that_date":"AI 데이터센터 액침냉각 narrative가 부각됐지만 C07 HBM 장비 order/revenue conversion과 직접 연결되지 않음. local blowoff 이후 4B watch로 처리할 사례.","evidence_source":"https://v.daum.net/v/20240312102259830","stage2_evidence_fields":["AI_server_cooling_narrative","semiconductor_equipment_adjacency"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_blowoff","non_HBM_order_bridge_absent","AI_cooling_theme_substitution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv","profile_path":"atlas/symbol_profiles/083/083450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.62,"MFE_90D_pct":11.62,"MFE_180D_pct":11.62,"MAE_30D_pct":-22.87,"MAE_90D_pct":-70.94,"MAE_180D_pct":-77.11,"peak_date":"2024-03-18","peak_price":61500.0,"drawdown_after_peak_pct":-79.5,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":0.05,"four_b_full_window_peak_proximity":0.05,"trigger_outcome_label":"stage4b_success_high_MAE_guardrail","current_profile_verdict":"current_profile_4B_too_late_if_treated_as_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_universe_proxy","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|083450|Stage4B|2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07-107-348210-S2A-20241101","case_id":"C07-107-348210","symbol":"348210","company_name":"넥스틴","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_CMP_CHILLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_BETA_FADE","deep_sub_archetype_id":"C07_DEEP_HBM_TESTER_CMP_PROCESS_CHILLER_AND_INSPECTION_ORDER_CONVERSION_VS_PRICE_ONLY_RS","loop_objective":"coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-01","entry_date":"2024-11-01","entry_price":66000.0,"evidence_available_at_that_date":"HBM 검사 장비 Croky와 고객사 qualification narrative는 확인되지만, 당시에는 수주/매출 bridge보다 “수혜주” 기대가 강한 trigger.","evidence_source":"https://www.yna.co.kr/view/AKR20241101022700008","stage2_evidence_fields":["HBM_inspection_equipment_customer_qualification","niche_defect_inspection_exposure"],"stage3_evidence_fields":["qualification_not_order_revenue_bridge"],"stage4b_evidence_fields":["beneficiary_label_without_contract_conversion"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv","profile_path":"atlas/symbol_profiles/348/348210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.3,"MFE_90D_pct":5.3,"MFE_180D_pct":5.3,"MAE_30D_pct":-28.18,"MAE_90D_pct":-28.18,"MAE_180D_pct":-31.14,"peak_date":"2024-11-05","peak_price":69500.0,"drawdown_after_peak_pct":-34.6,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":0.12,"four_b_full_window_peak_proximity":0.12,"trigger_outcome_label":"counterexample_qualification_without_order_bridge","current_profile_verdict":"current_profile_false_positive_if_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_universe_proxy","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|348210|Stage2-Actionable|2024-11-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07-107-281820","trigger_id":"C07-107-281820-S2A-20240104","symbol":"281820","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":62,"margin_bridge_score":55,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":42,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":62,"margin_bridge_score":55,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":42,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":76.5,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"add CMP-HBM process bottleneck and major-memory-customer route; still not Green without direct order/revision","MFE_90D_pct":71.47,"MAE_90D_pct":-14.1,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural_or_too_conservative"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07-107-253590","trigger_id":"C07-107-253590-S2A-20240605","symbol":"253590","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":75,"backlog_visibility_score":62,"margin_bridge_score":50,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":47,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":62,"margin_bridge_score":55,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":42,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":75.0,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"keep Yellow but block Green because QA-stage tester delivery lacks mass-production revenue bridge","MFE_90D_pct":53.1,"MAE_90D_pct":-34.22,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07-107-092870","trigger_id":"C07-107-092870-S2A-20240503","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":62,"margin_bridge_score":55,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":42,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":82,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":85,"execution_risk_score":72,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":20,"accounting_trust_risk_score":18},"weighted_score_after":68.0,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"demote SSD/CXL-adjacent tester contract when HBM direct bridge and scale are absent","MFE_90D_pct":25.12,"MAE_90D_pct":-50.25,"score_return_alignment_label":"current_profile_residual_error","current_profile_verdict":"current_profile_too_early_if_yellow"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07-107-064290","trigger_id":"C07-107-064290-S3Y-20240716","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":62,"margin_bridge_score":55,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":42,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":82,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":85,"execution_risk_score":72,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":20,"accounting_trust_risk_score":18},"weighted_score_after":60.0,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"demote expectation-only inspection-equipment narrative without confirmed HBM order/revenue bridge","MFE_90D_pct":1.39,"MAE_90D_pct":-57.31,"score_return_alignment_label":"current_profile_residual_error","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07-107-322310","trigger_id":"C07-107-322310-S3Y-20240517","symbol":"322310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":75,"backlog_visibility_score":62,"margin_bridge_score":50,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":47,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":80.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":82,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":85,"execution_risk_score":72,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":20,"accounting_trust_risk_score":18},"weighted_score_after":62.0,"stage_label_after":"Stage2-Watch/4B-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"direct HBM PAD overlay order exists but late price/limited scale requires 4B watch","MFE_90D_pct":5.5,"MAE_90D_pct":-48.01,"score_return_alignment_label":"current_profile_residual_error","current_profile_verdict":"current_profile_false_positive_late_trigger"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07-107-083450","trigger_id":"C07-107-083450-S4B-20240315","symbol":"083450","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":75,"backlog_visibility_score":62,"margin_bridge_score":50,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":47,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":82,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":85,"execution_risk_score":72,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":20,"accounting_trust_risk_score":18},"weighted_score_after":55.0,"stage_label_after":"Stage4B-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"AI cooling narrative substitutes for HBM equipment order conversion; local blowoff should dominate","MFE_90D_pct":11.62,"MAE_90D_pct":-70.94,"score_return_alignment_label":"current_profile_residual_error","current_profile_verdict":"current_profile_4B_too_late_if_treated_as_yellow"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07-107-348210","trigger_id":"C07-107-348210-S2A-20241101","symbol":"348210","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":62,"margin_bridge_score":55,"revision_score":52,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":42,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":82,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":85,"execution_risk_score":72,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":20,"accounting_trust_risk_score":18},"weighted_score_after":65.0,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"customer qualification/beneficiary label remains below order/revenue conversion bridge","MFE_90D_pct":5.3,"MAE_90D_pct":-28.18,"score_return_alignment_label":"current_profile_residual_error","current_profile_verdict":"current_profile_false_positive_if_yellow"}
{"row_type":"profile_aggregate","profile_id":"P0","profile_scope":"current_calibrated_proxy","profile_hypothesis":"current profile still over-rewards C07 relative strength without direct order/revenue conversion","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":24.79,"avg_MAE_90D_pct":-43.29,"avg_MFE_180D_pct":27.0,"avg_MAE_180D_pct":-47.5,"false_positive_rate":0.71,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":0.07,"avg_four_b_local_peak_proximity":0.44,"avg_four_b_full_window_peak_proximity":0.44,"score_return_alignment_verdict":"weak_alignment_high_drawdown"}
{"row_type":"profile_aggregate","profile_id":"P0b","profile_scope":"baseline_reference","profile_hypothesis":"old baseline is noisier and treats theme RS as insufficiently gated","changed_axes":["rollback_reference_only"],"changed_thresholds":{},"eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":24.79,"avg_MAE_90D_pct":-43.29,"avg_MFE_180D_pct":27.0,"avg_MAE_180D_pct":-47.5,"false_positive_rate":0.71,"missed_structural_count":1,"late_green_count":1,"avg_green_lateness_ratio":0.07,"avg_four_b_local_peak_proximity":0.44,"avg_four_b_full_window_peak_proximity":0.44,"score_return_alignment_verdict":"reference_only_no_improvement"}
{"row_type":"profile_aggregate","profile_id":"P1","profile_scope":"sector_specific_candidate_profile","profile_hypothesis":"L2 equipment RS requires verified major-customer order or process-bottleneck revenue bridge before Yellow","changed_axes":["order_or_revenue_conversion_bridge_required","local_4b_watch_after_theme_blowoff"],"changed_thresholds":{"stage3_yellow_bridge_required":true},"eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":38.8,"avg_MAE_90D_pct":-36.64,"avg_MFE_180D_pct":42.68,"avg_MAE_180D_pct":-40.3,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":0.12,"avg_four_b_local_peak_proximity":0.25,"avg_four_b_full_window_peak_proximity":0.25,"score_return_alignment_verdict":"improved_but_MAE_still_high"}
{"row_type":"profile_aggregate","profile_id":"P2","profile_scope":"canonical_archetype_candidate_profile","profile_hypothesis":"C07-specific bridge: direct HBM tester/equipment order, QA-to-mass-production evidence, or CMP process revenue bridge required before Yellow/Green","changed_axes":["C07_verified_order_or_revenue_conversion_bridge_required_before_Yellow","C07_block_Green_without_mass_production_or_revision_bridge"],"changed_thresholds":{"C07_yellow_bridge_required":true,"C07_green_revision_required":true},"eligible_trigger_count":2,"selected_entry_trigger_per_case":2,"avg_MFE_90D_pct":62.28,"avg_MAE_90D_pct":-24.16,"avg_MFE_180D_pct":70.05,"avg_MAE_180D_pct":-24.16,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":0.24,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"best_alignment_but_sample_small"}
{"row_type":"profile_aggregate","profile_id":"P3","profile_scope":"counterexample_guard_profile","profile_hypothesis":"allow only positive bridge plus cap high-MAE tester-contract proxies with 4B watch","changed_axes":["high_MAE_guard","theme_substitution_block","single_contract_scale_guard"],"changed_thresholds":{"counterexample_guard":true},"eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":49.9,"avg_MAE_90D_pct":-32.86,"avg_MFE_180D_pct":55.07,"avg_MAE_180D_pct":-35.49,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":0.16,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"safer_than_P0_less_strict_than_P2"}
{"row_type":"residual_contribution","round":"R2","loop":"107","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage3_yellow_total_min"],"residual_error_types_found":["C07_theme_relative_strength_without_order_bridge","direct_single_contract_late_trigger_false_positive","qualification_without_revenue_bridge","AI_cooling_theme_substitution","high_MAE_after_memory_tester_contract"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 13. Shadow Weight Rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_order_or_revenue_conversion_bridge_required,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,false,true,+1,"C07 positives survive only when order/QA-to-production/CMP process bridge exists; theme-only triggers produced severe MAE","P2 improves avg_MFE90 from 24.79 to 62.28 and avg_MAE90 from -43.29 to -24.16","C07-107-281820-S2A-20240104|C07-107-253590-S2A-20240605|C07-107-064290-S3Y-20240716|C07-107-322310-S3Y-20240517|C07-107-348210-S2A-20241101",8,7,5,medium,canonical_shadow_only,"not production; batch implementation only"
shadow_weight,C07_late_single_contract_scale_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,false,true,+1,"single contract after price rerating can be local 4B watch even when HBM equipment evidence is direct","blocks Oros/Exicon late false positives without blocking KC Tech/Neosem early bridge","C07-107-092870-S3Y-20240704|C07-107-322310-S3Y-20240517",2,2,2,low,canonical_shadow_only,"requires more loops before production"
shadow_weight,C07_theme_substitution_block,sector_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,false,true,+1,"AI cooling/data-center narrative is not HBM equipment order conversion unless customer/order/revenue evidence is explicit","routes GST-like blowoff to 4B watch instead of Yellow","C07-107-083450-S4B-20240315",1,1,1,medium,sector_shadow_only,"strengthens price_only_blowoff_blocks_positive_stage"
```

## 14. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage3_yellow_total_min
residual_error_types_found: C07_theme_relative_strength_without_order_bridge, direct_single_contract_late_trigger_false_positive, qualification_without_revenue_bridge, AI_cooling_theme_substitution, high_MAE_after_memory_tester_contract
new_axis_proposed: C07_verified_order_or_revenue_conversion_bridge_required_before_Yellow_plus_HBM_equipment_RS_4B_watch_after_local_blowoff
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 15. Batch Ingest Self-Audit

```text
standard_filename: pass
compact_filename_forbidden: pass
selected_round_metadata_match: pass
selected_loop_metadata_match: pass
round_sector_consistency: pass
stock_web_manifest_checked: pass
stock_web_manifest_max_date: 2026-02-20
all_trigger_rows_have_entry_date_price_MFE_MAE_30_90_180: pass
trigger_type_canonical_stage_label: pass
jsonl_machine_rows_present: pass
representative_dedupe_applied: pass
positive_counterexample_balance: pass
new_independent_case_ratio: 7/7 = 1.00
new_symbol_count: 7
production_scoring_changed: false
handoff_prompt_executed_now: false
```

## 16. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent E2R calibration. Do not treat this MD as production truth by itself. Ingest it together with other V12 residual MDs. Parse all JSONL rows under section 12. Validate stock-web paths, profile JSONs, corporate-action windows, duplicate keys, and 30/90/180 MFE/MAE values. If validation passes, consider adding a C07 canonical shadow rule candidate:

C07_verified_order_or_revenue_conversion_bridge_required_before_Yellow_plus_HBM_equipment_RS_4B_watch_after_local_blowoff

Implementation intent:
- C07 Stage3-Yellow requires direct HBM/CXL tester order, QA-to-mass-production bridge, or CMP/process bottleneck revenue bridge.
- C07 Green requires revenue/revision bridge and cannot be unlocked by customer qualification or theme RS alone.
- Late small single-contract confirmations after a local rerating should become local 4B watch, not automatic Yellow.
- AI cooling or generic AI equipment narratives must not substitute for HBM equipment order conversion.

Apply only as shadow candidate unless multiple later loops confirm the same residual pattern. Do not alter global Stage3 thresholds from this MD alone.
```

## 17. Next Research State

```text
completed_round = R2
completed_loop = 107
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

