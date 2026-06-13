# E2R Stock-Web v12 Residual Research — R2 / Loop 150 / C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF

```text
completed_round = R2
completed_loop = 150
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = mixed_c09_lithography_frontend_substrate_backend_robot_sic_leaf_set
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Executive summary

이번 loop는 세션-aware 기준으로 아직 30-row 안정권을 막 넘기지 못한 C09를 한 번 더 보강한다. No-Repeat Index 원본에서는 C09가 10 rows / Priority 0로 남아 있고, 이번 세션의 C09 loop 126·135·143까지 감안하면 약 29 representative rows 근처다. 따라서 loop 150은 C09를 최소 안정권 위로 올리는 clearing pass다.

이번 샘플은 기존 C09의 DIT·파크시스템스·와이씨·오로스테크놀로지·인텍플러스·한미반도체·HPSP·예스티·레이저쎌·네오셈·이오테크닉스·주성엔지니어링·펨트론·넥스틴·엘오티베큠·프로텍·고영 조합을 피했다. 새 심볼은 에스앤에스텍, 유진테크, 기가비스, 코세스, 제너셈, 케이엔제이, 라온테크/라온로보틱스다.

**Rule candidate:** `C09_HARD_COMMERCIAL_BRIDGE_QUALIFICATION_LADDER_AND_EXIT_GATE_V4`

C09에서는 “AI/HBM/EUV/글라스기판/전공정/후공정”이라는 단어가 불꽃처럼 붙지만, 불꽃만으로는 엔진이 아니다. 실제 엔진은 `명명 고객 수주`, `hard CAPA`, `양산 qualification`, `매출 인식 window`, `margin/revision bridge`다. 반대로 리포트의 시장규모·독점적 지위·forecast만 있고 commercial bridge가 비어 있으면 valuation oxygen이 먼저 타버려 4B-watch 또는 Stage2-Watch로 낮춰야 한다.

## 2. Price source validation

| item | value |
|---|---|
| primary_price_source | Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| source_name | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| entry_price_basis | entry date close `c` |
| MFE/MAE basis | entry 이후 30/90/180 trading rows의 max high / min low |

## 3. Novelty / no-repeat check

| check | result |
|---|---|
| canonical selected | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF |
| index baseline rows | 10 |
| session-aware prior C09 rows | about 29 after loop126 + loop135 + loop143 |
| after this loop if accepted | about 37 representative rows |
| hard duplicate key avoided | canonical_archetype_id + symbol + trigger_type + entry_date |
| existing C09 symbols avoided | 110990, 232140, 140860, 322310, 064290, 042700, 403870, 122640, 412350, 253590, 039030, 036930, 168360, 348210, 083310, 053610, 098460 |
| new symbols in this loop | 101490, 084370, 420770, 089890, 217190, 272110, 232680 |
| same-symbol repeat inside loop | 272110 has two different trigger families: 2024-03 customer/margin bridge and 2024-12 CAPA expansion |

## 4. Case summary

|case_id|symbol|company|trigger_date|trigger_type|case_label|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|C09_L150_101490_EUV_REVENUE_EXPECTATION|101490|에스앤에스텍|2023-11-09|Stage2-Watch|counterexample|18.6|-16.74|18.6|-37.09|current_profile_false_positive_if_stage2_actionable|
|C09_L150_084370_FRONT_END_DEPOSITION_RECOVERY|084370|유진테크|2024-04-24|Stage2-Watch|counterexample|13.21|-29.43|13.21|-42.83|current_profile_false_positive_late_equipment_recovery|
|C09_L150_420770_FCBGA_GLASS_SUBSTRATE_BLOWOFF|420770|기가비스|2024-04-09|Stage4B-Watch|counterexample|7.98|-54.84|7.98|-73.43|current_profile_false_positive_if_promoted_on_ai_substrate_narrative|
|C09_L150_089890_POST_PROCESS_LASER_EQUIPMENT_MOMENTUM|089890|코세스|2023-10-23|Stage2-Actionable|positive|152.01|-3.33|152.01|-3.33|current_profile_missed_structural_if_blocked_as_generic_equipment|
|C09_L150_217190_HBM_BACKEND_AUTOMATION|217190|제너셈|2023-12-08|Stage2-Actionable|positive_with_4B_overlay|37.3|-4.6|37.3|-40.56|current_profile_too_late_without_hbm_backend_revenue_bridge|
|C09_L150_272110_SIC_RING_CUSTOMER_PENETRATION|272110|케이엔제이|2024-03-06|Stage3-Yellow|positive_with_4B_overlay|55.13|-3.46|55.13|-29.91|current_profile_missed_structural_if_treated_as_generic_part|
|C09_L150_232680_VACUUM_ROBOT_ORDER_DISCUSSION|232680|라온테크/라온로보틱스|2024-02-26|Stage2-Watch|counterexample|2.15|-19.35|2.15|-35.48|current_profile_false_positive_if_customer_discussion_promoted|
|C09_L150_272110_SIC_CAPA_EXPANSION|272110|케이엔제이|2024-12-27|Stage2-Actionable|positive|34.52|-12.53|77.22|-12.53|current_profile_missed_structural_if_c09_blocks_all_non_order_capex|


## 5. Evidence source map

| symbol | company | trigger_date | evidence summary | evidence_url |
|---|---|---:|---|---|
| 101490 | 에스앤에스텍 | 2023-11-09 | 중국향 본업 성장과 EUV 매출 forecast가 있었지만 signed order bridge는 약했다. | https://www.newspim.com/news/view/20231109000376 |
| 084370 | 유진테크 | 2024-04-24 | DRAM 1b / NAND V8 전환 투자와 OPM 회복 기대가 있었지만 entry 이후 MAE가 커졌다. | https://www.dailyinvest.kr/news/articleView.html?idxno=58253 |
| 420770 | 기가비스 | 2024-04-09 | FC-BGA/글라스기판 검사 독점성 narrative가 강했으나 가격은 4B blowoff 형태였다. | https://file.alphasquare.co.kr/media/pdfs/company-report/%EB%A9%94%EB%A6%AC%EC%B8%A020240409%EA%B8%B0%EA%B0%80%EB%B9%84%EC%8A%A4.pdf |
| 089890 | 코세스 | 2023-10-23 | HBM/AI 후공정 장비 route가 강한 초기 momentum으로 이어졌다. 다만 source는 proxy 품질이라 URL 보강 대상이다. | https://snusmic.com/wp-content/uploads/2023/10/23_2_1%EC%A3%BC%EC%B0%A8_%EC%88%98%EC%A0%95%EB%B3%B4%EA%B3%A0%EC%84%9C_3%ED%8C%80_%EC%BD%94%EC%84%B8%EC%8A%A4.pdf |
| 217190 | 제너셈 | 2023-12-08 | HBM 후공정 장비 신규 매출과 Saw/EMI 장비 회복 기대가 가격경로와 맞았다. | https://ssl.pstatic.net/imgstock/upload/research/company/1701903635257.pdf |
| 272110 | 케이엔제이 | 2024-03-06 | 메모리 고객, SiC 포커스링 침투율, 수율/마진 bridge가 명확했다. | https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/05/240306_KNJ_f.pdf |
| 232680 | 라온테크/라온로보틱스 | 2024-02-26 | 진공 로봇 국내 1위, 고객사 다변화, 중국 양산오더 언급이 있었지만 가격경로는 따라오지 못했다. | https://raonrobot.com/board/board.php?bo_table=press&idx=4 |
| 272110 | 케이엔제이 | 2024-12-27 | CVD SiC Ring 등 반도체 공정용 소재·부품 CAPA 확보 200억원 투자. | https://www.thelec.kr/news/articleView.html?idxno=32010 |

## 6. Symbol profile and corporate-action window check

|symbol|company|profile_path|price_shards|corporate_action_window_status|
|---|---|---|---|---|
|101490|에스앤에스텍|atlas/symbol_profiles/101/101490.json|atlas/ohlcv_tradable_by_symbol_year/101/101490/2023.csv / atlas/ohlcv_tradable_by_symbol_year/101/101490/2024.csv|candidate 2009-04-30 only; outside trigger~D+180|
|084370|유진테크|atlas/symbol_profiles/084/084370.json|atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv / atlas/ohlcv_tradable_by_symbol_year/084/084370/2025.csv|candidates 2007-05-17, 2010-01-22, 2012-06-07 only; outside trigger~D+180|
|420770|기가비스|atlas/symbol_profiles/420/420770.json|atlas/ohlcv_tradable_by_symbol_year/420/420770/2024.csv / atlas/ohlcv_tradable_by_symbol_year/420/420770/2025.csv|none|
|089890|코세스|atlas/symbol_profiles/089/089890.json|atlas/ohlcv_tradable_by_symbol_year/089/089890/2023.csv / atlas/ohlcv_tradable_by_symbol_year/089/089890/2024.csv|candidates 2011-05-13, 2018-05-28, 2018-06-15 only; outside trigger~D+180|
|217190|제너셈|atlas/symbol_profiles/217/217190.json|atlas/ohlcv_tradable_by_symbol_year/217/217190/2023.csv / atlas/ohlcv_tradable_by_symbol_year/217/217190/2024.csv|candidates 2015-11-10, 2015-12-07, 2025-11-24, 2025-12-17; outside trigger~D+180|
|272110|케이엔제이|atlas/symbol_profiles/272/272110.json|atlas/ohlcv_tradable_by_symbol_year/272/272110/2024.csv / atlas/ohlcv_tradable_by_symbol_year/272/272110/2025.csv|none|
|232680|라온테크/라온로보틱스|atlas/symbol_profiles/232/232680.json|atlas/ohlcv_tradable_by_symbol_year/232/232680/2024.csv / atlas/ohlcv_tradable_by_symbol_year/232/232680/2025.csv|candidates 2016-06-28, 2017-07-17, 2022-04-19, 2022-05-11 only; outside trigger~D+180|


## 7. Trigger-level price path table

|trigger_id|symbol|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|T_C09_L150_101490_EUV_REVENUE_EXPECTATION|101490|2023-11-09|45700|18.6|-10.5|18.6|-16.74|18.6|-37.09|2023-11-28|-46.96|
|T_C09_L150_084370_FRONT_END_DEPOSITION_RECOVERY|084370|2024-04-24|53000|13.21|-11.89|13.21|-29.43|13.21|-42.83|2024-05-28|-49.5|
|T_C09_L150_420770_FCBGA_GLASS_SUBSTRATE_BLOWOFF|420770|2024-04-09|76400|7.98|-19.9|7.98|-54.84|7.98|-73.43|2024-04-09|-75.39|
|T_C09_L150_089890_POST_PROCESS_LASER_EQUIPMENT_MOMENTUM|089890|2023-10-23|8710|36.74|-3.33|152.01|-3.33|152.01|-3.33|2024-01-31|-37.95|
|T_C09_L150_217190_HBM_BACKEND_AUTOMATION|217190|2023-12-08|12600|17.06|-1.98|37.3|-4.6|37.3|-40.56|2024-03-07|-56.71|
|T_C09_L150_272110_SIC_RING_CUSTOMER_PENETRATION|272110|2024-03-06|17050|55.13|-3.46|55.13|-3.46|55.13|-29.91|2024-04-08|-54.82|
|T_C09_L150_232680_VACUUM_ROBOT_ORDER_DISCUSSION|232680|2024-02-26|9300|2.15|-9.57|2.15|-19.35|2.15|-35.48|2024-02-26|-36.84|
|T_C09_L150_272110_SIC_CAPA_EXPANSION|272110|2024-12-27|14050|20.07|-12.53|34.52|-12.53|77.22|-12.53|2025-09-23|-5.62|


## 8. Interpretation

### 8.1 False-positive side

에스앤에스텍, 유진테크, 기가비스, 라온테크는 모두 “첨단 장비/소부장” 문법을 갖고 있었다. 하지만 C09의 실패는 대체로 같은 곳에서 난다. 기술의 방향은 맞아도, entry 시점에 hard commercial bridge가 비어 있거나 이미 valuation이 산소를 태운 상태면 MFE는 짧고 MAE는 깊어진다.

기가비스가 가장 선명하다. FC-BGA와 글라스기판 검사장비 narrative는 훌륭했지만, 2024-04-09 entry 이후 180D MFE는 7.98%에 그치고 MAE는 -73.43%였다. 이건 Stage2-Actionable이 아니라 local 4B-watch가 맞다.

### 8.2 Positive exception side

코세스, 제너셈, 케이엔제이 쪽은 다르다. 후공정 장비 momentum, HBM backend automation 매출, SiC ring 고객/수율/마진 bridge, CAPA expansion처럼 실제 commercial bridge가 있었고 가격경로도 반응했다. 다만 제너셈과 케이엔제이 2024-03 row는 peak 이후 drawdown이 커서, positive로 보되 4B exit guard를 같이 붙여야 한다.

### 8.3 C09-specific rule candidate

```text
C09_HARD_COMMERCIAL_BRIDGE_QUALIFICATION_LADDER_AND_EXIT_GATE_V4:
  allow_stage2_actionable_when:
    - named_customer_order_or_repeated_customer_revenue == true
      OR hard_CAPA_expansion_tied_to_advanced_process_consumable == true
      OR production_qualification_and_revenue_window_confirmed == true
    AND at_least_one_of:
      - margin_or_OPM_bridge_visible
      - revision_or_consensus_upgrade_visible
      - shipment_or_revenue_recognition_window_visible
      - customer_quality_high_and_repeatable
  keep_stage2_watch_or_4B_watch_when:
    - evidence_is_market_size_or_technology_forecast_only
    - glass_substrate_or_EUV_or_HBM_vocabulary_without_customer_bridge
    - entry_after_relative_strength_exhaustion
    - 30D/90D local peak proximity high and MAE90 <= -20
  add_exit_guard_when:
    - MFE90 >= 30 but drawdown_after_peak <= -35
```

## 9. Residual contribution summary

| item | value |
|---|---:|
| new_independent_case_count | 8 |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | 7 |
| same_archetype_new_trigger_family_count | 8 |
| calibration_usable trigger count | 8 |
| positive_case_count | 4 |
| counterexample_count | 4 |
| stage4b_watch_or_overlay_count | 7 |
| current_profile_error_count | 7 |
| index_baseline C09 rows | 10 |
| session-aware C09 rows after this loop if accepted | about 37 |

## 10. Machine-readable JSONL rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C09_L150_101490_EUV_REVENUE_EXPECTATION", "symbol": "101490", "company_name": "에스앤에스텍", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "EUV_BLANK_MASK_PELLICLE_REVENUE_FORECAST_WITHOUT_SIGNED_ORDER", "case_type": "qualification_revenue_forecast_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "T_C09_L150_101490_EUV_REVENUE_EXPECTATION", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "current_profile_verdict": "current_profile_false_positive_if_stage2_actionable", "price_source": "Songdaiki/stock-web", "evidence_url": "https://www.newspim.com/news/view/20231109000376"}
{"row_type": "trigger", "trigger_id": "T_C09_L150_101490_EUV_REVENUE_EXPECTATION", "case_id": "C09_L150_101490_EUV_REVENUE_EXPECTATION", "symbol": "101490", "company_name": "에스앤에스텍", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "EUV_BLANK_MASK_PELLICLE_REVENUE_FORECAST_WITHOUT_SIGNED_ORDER", "trigger_type": "Stage2-Watch", "trigger_date": "2023-11-09", "entry_date": "2023-11-09", "entry_price": 45700.0, "MFE_30D_pct": 18.6, "MAE_30D_pct": -10.5, "MFE_90D_pct": 18.6, "MAE_90D_pct": -16.74, "MFE_180D_pct": 18.6, "MAE_180D_pct": -37.09, "peak_date": "2023-11-28", "peak_price": 54200.0, "trough_after_peak_date": "2024-07-31", "drawdown_after_peak_pct": -46.96, "calibration_usable": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence_url": "https://www.newspim.com/news/view/20231109000376", "current_profile_verdict": "current_profile_false_positive_if_stage2_actionable", "trigger_outcome_label": "counterexample"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C09_L150_101490_EUV_REVENUE_EXPECTATION", "trigger_id": "T_C09_L150_101490_EUV_REVENUE_EXPECTATION", "symbol": "101490", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_or_hard_bridge": 2, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 2, "relative_strength": 4, "valuation_oxygen_risk": 8, "execution_or_qualification_risk": 7}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_or_hard_bridge": 2, "qualification_or_customer_quality": 4, "margin_or_revision_bridge": 2, "relative_strength": 3, "valuation_oxygen_risk": 9, "execution_or_qualification_risk": 8}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch", "changed_components": ["hard_commercial_bridge_required", "qualification_ladder_guard", "high_MAE_and_4B_exit_guard"], "MFE_90D_pct": 18.6, "MAE_90D_pct": -16.74, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive_if_stage2_actionable"}
{"row_type": "case", "case_id": "C09_L150_084370_FRONT_END_DEPOSITION_RECOVERY", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "FRONT_END_DEPOSITION_MEMORY_NODE_CONVERSION_LATE_ENTRY", "case_type": "front_end_equipment_recovery_high_mae_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "T_C09_L150_084370_FRONT_END_DEPOSITION_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "current_profile_verdict": "current_profile_false_positive_late_equipment_recovery", "price_source": "Songdaiki/stock-web", "evidence_url": "https://www.dailyinvest.kr/news/articleView.html?idxno=58253"}
{"row_type": "trigger", "trigger_id": "T_C09_L150_084370_FRONT_END_DEPOSITION_RECOVERY", "case_id": "C09_L150_084370_FRONT_END_DEPOSITION_RECOVERY", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "FRONT_END_DEPOSITION_MEMORY_NODE_CONVERSION_LATE_ENTRY", "trigger_type": "Stage2-Watch", "trigger_date": "2024-04-24", "entry_date": "2024-04-24", "entry_price": 53000.0, "MFE_30D_pct": 13.21, "MAE_30D_pct": -11.89, "MFE_90D_pct": 13.21, "MAE_90D_pct": -29.43, "MFE_180D_pct": 13.21, "MAE_180D_pct": -42.83, "peak_date": "2024-05-28", "peak_price": 60000.0, "trough_after_peak_date": "2024-12-20", "drawdown_after_peak_pct": -49.5, "calibration_usable": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence_url": "https://www.dailyinvest.kr/news/articleView.html?idxno=58253", "current_profile_verdict": "current_profile_false_positive_late_equipment_recovery", "trigger_outcome_label": "counterexample"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C09_L150_084370_FRONT_END_DEPOSITION_RECOVERY", "trigger_id": "T_C09_L150_084370_FRONT_END_DEPOSITION_RECOVERY", "symbol": "084370", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_or_hard_bridge": 2, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 2, "relative_strength": 4, "valuation_oxygen_risk": 8, "execution_or_qualification_risk": 7}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_or_hard_bridge": 2, "qualification_or_customer_quality": 4, "margin_or_revision_bridge": 2, "relative_strength": 3, "valuation_oxygen_risk": 9, "execution_or_qualification_risk": 8}, "weighted_score_after": 66, "stage_label_after": "Stage2-Watch", "changed_components": ["hard_commercial_bridge_required", "qualification_ladder_guard", "high_MAE_and_4B_exit_guard"], "MFE_90D_pct": 13.21, "MAE_90D_pct": -29.43, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive_late_equipment_recovery"}
{"row_type": "case", "case_id": "C09_L150_420770_FCBGA_GLASS_SUBSTRATE_BLOWOFF", "symbol": "420770", "company_name": "기가비스", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SUBSTRATE_INSPECTION_GLASS_SUBSTRATE_VALUATION_BLOWOFF", "case_type": "valuation_blowoff_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "T_C09_L150_420770_FCBGA_GLASS_SUBSTRATE_BLOWOFF", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "current_profile_verdict": "current_profile_false_positive_if_promoted_on_ai_substrate_narrative", "price_source": "Songdaiki/stock-web", "evidence_url": "https://file.alphasquare.co.kr/media/pdfs/company-report/%EB%A9%94%EB%A6%AC%EC%B8%A020240409%EA%B8%B0%EA%B0%80%EB%B9%84%EC%8A%A4.pdf"}
{"row_type": "trigger", "trigger_id": "T_C09_L150_420770_FCBGA_GLASS_SUBSTRATE_BLOWOFF", "case_id": "C09_L150_420770_FCBGA_GLASS_SUBSTRATE_BLOWOFF", "symbol": "420770", "company_name": "기가비스", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SUBSTRATE_INSPECTION_GLASS_SUBSTRATE_VALUATION_BLOWOFF", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-04-09", "entry_date": "2024-04-09", "entry_price": 76400.0, "MFE_30D_pct": 7.98, "MAE_30D_pct": -19.9, "MFE_90D_pct": 7.98, "MAE_90D_pct": -54.84, "MFE_180D_pct": 7.98, "MAE_180D_pct": -73.43, "peak_date": "2024-04-09", "peak_price": 82500.0, "trough_after_peak_date": "2024-12-09", "drawdown_after_peak_pct": -75.39, "calibration_usable": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence_url": "https://file.alphasquare.co.kr/media/pdfs/company-report/%EB%A9%94%EB%A6%AC%EC%B8%A020240409%EA%B8%B0%EA%B0%80%EB%B9%84%EC%8A%A4.pdf", "current_profile_verdict": "current_profile_false_positive_if_promoted_on_ai_substrate_narrative", "trigger_outcome_label": "counterexample"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C09_L150_420770_FCBGA_GLASS_SUBSTRATE_BLOWOFF", "trigger_id": "T_C09_L150_420770_FCBGA_GLASS_SUBSTRATE_BLOWOFF", "symbol": "420770", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_or_hard_bridge": 2, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 2, "relative_strength": 4, "valuation_oxygen_risk": 8, "execution_or_qualification_risk": 7}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_or_hard_bridge": 2, "qualification_or_customer_quality": 4, "margin_or_revision_bridge": 2, "relative_strength": 3, "valuation_oxygen_risk": 9, "execution_or_qualification_risk": 8}, "weighted_score_after": 54, "stage_label_after": "Stage4B-Watch", "changed_components": ["hard_commercial_bridge_required", "qualification_ladder_guard", "high_MAE_and_4B_exit_guard"], "MFE_90D_pct": 7.98, "MAE_90D_pct": -54.84, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive_if_promoted_on_ai_substrate_narrative"}
{"row_type": "case", "case_id": "C09_L150_089890_POST_PROCESS_LASER_EQUIPMENT_MOMENTUM", "symbol": "089890", "company_name": "코세스", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "POST_PROCESS_LASER_SOLDERBALL_HBM_ADVANCED_PACKAGING_ROUTE", "case_type": "advanced_packaging_equipment_positive", "positive_or_counterexample": "positive", "best_trigger": "T_C09_L150_089890_POST_PROCESS_LASER_EQUIPMENT_MOMENTUM", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "current_profile_verdict": "current_profile_missed_structural_if_blocked_as_generic_equipment", "price_source": "Songdaiki/stock-web", "evidence_url": "https://snusmic.com/wp-content/uploads/2023/10/23_2_1%EC%A3%BC%EC%B0%A8_%EC%88%98%EC%A0%95%EB%B3%B4%EA%B3%A0%EC%84%9C_3%ED%8C%80_%EC%BD%94%EC%84%B8%EC%8A%A4.pdf"}
{"row_type": "trigger", "trigger_id": "T_C09_L150_089890_POST_PROCESS_LASER_EQUIPMENT_MOMENTUM", "case_id": "C09_L150_089890_POST_PROCESS_LASER_EQUIPMENT_MOMENTUM", "symbol": "089890", "company_name": "코세스", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "POST_PROCESS_LASER_SOLDERBALL_HBM_ADVANCED_PACKAGING_ROUTE", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-23", "entry_date": "2023-10-23", "entry_price": 8710.0, "MFE_30D_pct": 36.74, "MAE_30D_pct": -3.33, "MFE_90D_pct": 152.01, "MAE_90D_pct": -3.33, "MFE_180D_pct": 152.01, "MAE_180D_pct": -3.33, "peak_date": "2024-01-31", "peak_price": 21950.0, "trough_after_peak_date": "2024-04-16", "drawdown_after_peak_pct": -37.95, "calibration_usable": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence_url": "https://snusmic.com/wp-content/uploads/2023/10/23_2_1%EC%A3%BC%EC%B0%A8_%EC%88%98%EC%A0%95%EB%B3%B4%EA%B3%A0%EC%84%9C_3%ED%8C%80_%EC%BD%94%EC%84%B8%EC%8A%A4.pdf", "current_profile_verdict": "current_profile_missed_structural_if_blocked_as_generic_equipment", "trigger_outcome_label": "positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C09_L150_089890_POST_PROCESS_LASER_EQUIPMENT_MOMENTUM", "trigger_id": "T_C09_L150_089890_POST_PROCESS_LASER_EQUIPMENT_MOMENTUM", "symbol": "089890", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_or_hard_bridge": 4, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 5, "relative_strength": 7, "valuation_oxygen_risk": 4, "execution_or_qualification_risk": 4}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_or_hard_bridge": 7, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 6, "relative_strength": 6, "valuation_oxygen_risk": 5, "execution_or_qualification_risk": 4}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["hard_commercial_bridge_required", "qualification_ladder_guard", "high_MAE_and_4B_exit_guard"], "MFE_90D_pct": 152.01, "MAE_90D_pct": -3.33, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural_if_blocked_as_generic_equipment"}
{"row_type": "case", "case_id": "C09_L150_217190_HBM_BACKEND_AUTOMATION", "symbol": "217190", "company_name": "제너셈", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_BACKEND_AUTOMATION_ORDER_AND_REVENUE_BRIDGE", "case_type": "order_revenue_bridge_positive_with_4b_exit", "positive_or_counterexample": "positive_with_4B_overlay", "best_trigger": "T_C09_L150_217190_HBM_BACKEND_AUTOMATION", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "current_profile_verdict": "current_profile_too_late_without_hbm_backend_revenue_bridge", "price_source": "Songdaiki/stock-web", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1701903635257.pdf"}
{"row_type": "trigger", "trigger_id": "T_C09_L150_217190_HBM_BACKEND_AUTOMATION", "case_id": "C09_L150_217190_HBM_BACKEND_AUTOMATION", "symbol": "217190", "company_name": "제너셈", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_BACKEND_AUTOMATION_ORDER_AND_REVENUE_BRIDGE", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-08", "entry_date": "2023-12-08", "entry_price": 12600.0, "MFE_30D_pct": 17.06, "MAE_30D_pct": -1.98, "MFE_90D_pct": 37.3, "MAE_90D_pct": -4.6, "MFE_180D_pct": 37.3, "MAE_180D_pct": -40.56, "peak_date": "2024-03-07", "peak_price": 17300.0, "trough_after_peak_date": "2024-08-05", "drawdown_after_peak_pct": -56.71, "calibration_usable": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1701903635257.pdf", "current_profile_verdict": "current_profile_too_late_without_hbm_backend_revenue_bridge", "trigger_outcome_label": "positive_with_4B_overlay"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C09_L150_217190_HBM_BACKEND_AUTOMATION", "trigger_id": "T_C09_L150_217190_HBM_BACKEND_AUTOMATION", "symbol": "217190", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_or_hard_bridge": 4, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 5, "relative_strength": 4, "valuation_oxygen_risk": 8, "execution_or_qualification_risk": 4}, "weighted_score_before": 70, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_or_hard_bridge": 7, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 6, "relative_strength": 6, "valuation_oxygen_risk": 5, "execution_or_qualification_risk": 4}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable", "changed_components": ["hard_commercial_bridge_required", "qualification_ladder_guard", "high_MAE_and_4B_exit_guard"], "MFE_90D_pct": 37.3, "MAE_90D_pct": -4.6, "score_return_alignment_label": "aligned_positive_but_exit_needed", "current_profile_verdict": "current_profile_too_late_without_hbm_backend_revenue_bridge"}
{"row_type": "case", "case_id": "C09_L150_272110_SIC_RING_CUSTOMER_PENETRATION", "symbol": "272110", "company_name": "케이엔제이", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SIC_ETCH_CONSUMABLE_CUSTOMER_PENETRATION_MARGIN_BRIDGE", "case_type": "advanced_process_consumable_positive_with_exit_guard", "positive_or_counterexample": "positive_with_4B_overlay", "best_trigger": "T_C09_L150_272110_SIC_RING_CUSTOMER_PENETRATION", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "current_profile_verdict": "current_profile_missed_structural_if_treated_as_generic_part", "price_source": "Songdaiki/stock-web", "evidence_url": "https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/05/240306_KNJ_f.pdf"}
{"row_type": "trigger", "trigger_id": "T_C09_L150_272110_SIC_RING_CUSTOMER_PENETRATION", "case_id": "C09_L150_272110_SIC_RING_CUSTOMER_PENETRATION", "symbol": "272110", "company_name": "케이엔제이", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SIC_ETCH_CONSUMABLE_CUSTOMER_PENETRATION_MARGIN_BRIDGE", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-03-06", "entry_date": "2024-03-06", "entry_price": 17050.0, "MFE_30D_pct": 55.13, "MAE_30D_pct": -3.46, "MFE_90D_pct": 55.13, "MAE_90D_pct": -3.46, "MFE_180D_pct": 55.13, "MAE_180D_pct": -29.91, "peak_date": "2024-04-08", "peak_price": 26450.0, "trough_after_peak_date": "2024-11-28", "drawdown_after_peak_pct": -54.82, "calibration_usable": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence_url": "https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/05/240306_KNJ_f.pdf", "current_profile_verdict": "current_profile_missed_structural_if_treated_as_generic_part", "trigger_outcome_label": "positive_with_4B_overlay"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C09_L150_272110_SIC_RING_CUSTOMER_PENETRATION", "trigger_id": "T_C09_L150_272110_SIC_RING_CUSTOMER_PENETRATION", "symbol": "272110", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_or_hard_bridge": 4, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 5, "relative_strength": 7, "valuation_oxygen_risk": 4, "execution_or_qualification_risk": 4}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_or_hard_bridge": 7, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 6, "relative_strength": 6, "valuation_oxygen_risk": 5, "execution_or_qualification_risk": 4}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["hard_commercial_bridge_required", "qualification_ladder_guard", "high_MAE_and_4B_exit_guard"], "MFE_90D_pct": 55.13, "MAE_90D_pct": -3.46, "score_return_alignment_label": "aligned_positive_but_exit_needed", "current_profile_verdict": "current_profile_missed_structural_if_treated_as_generic_part"}
{"row_type": "case", "case_id": "C09_L150_232680_VACUUM_ROBOT_ORDER_DISCUSSION", "symbol": "232680", "company_name": "라온테크/라온로보틱스", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "VACUUM_ROBOT_CUSTOMER_DIVERSIFICATION_WITH_WEAK_ORDER_BRIDGE", "case_type": "customer_diversification_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "T_C09_L150_232680_VACUUM_ROBOT_ORDER_DISCUSSION", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "current_profile_verdict": "current_profile_false_positive_if_customer_discussion_promoted", "price_source": "Songdaiki/stock-web", "evidence_url": "https://raonrobot.com/board/board.php?bo_table=press&idx=4"}
{"row_type": "trigger", "trigger_id": "T_C09_L150_232680_VACUUM_ROBOT_ORDER_DISCUSSION", "case_id": "C09_L150_232680_VACUUM_ROBOT_ORDER_DISCUSSION", "symbol": "232680", "company_name": "라온테크/라온로보틱스", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "VACUUM_ROBOT_CUSTOMER_DIVERSIFICATION_WITH_WEAK_ORDER_BRIDGE", "trigger_type": "Stage2-Watch", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 9300.0, "MFE_30D_pct": 2.15, "MAE_30D_pct": -9.57, "MFE_90D_pct": 2.15, "MAE_90D_pct": -19.35, "MFE_180D_pct": 2.15, "MAE_180D_pct": -35.48, "peak_date": "2024-02-26", "peak_price": 9500.0, "trough_after_peak_date": "2024-10-22", "drawdown_after_peak_pct": -36.84, "calibration_usable": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence_url": "https://raonrobot.com/board/board.php?bo_table=press&idx=4", "current_profile_verdict": "current_profile_false_positive_if_customer_discussion_promoted", "trigger_outcome_label": "counterexample"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C09_L150_232680_VACUUM_ROBOT_ORDER_DISCUSSION", "trigger_id": "T_C09_L150_232680_VACUUM_ROBOT_ORDER_DISCUSSION", "symbol": "232680", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_or_hard_bridge": 2, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 2, "relative_strength": 4, "valuation_oxygen_risk": 8, "execution_or_qualification_risk": 7}, "weighted_score_before": 70, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_or_hard_bridge": 2, "qualification_or_customer_quality": 4, "margin_or_revision_bridge": 2, "relative_strength": 3, "valuation_oxygen_risk": 9, "execution_or_qualification_risk": 8}, "weighted_score_after": 61, "stage_label_after": "Stage2-Watch", "changed_components": ["hard_commercial_bridge_required", "qualification_ladder_guard", "high_MAE_and_4B_exit_guard"], "MFE_90D_pct": 2.15, "MAE_90D_pct": -19.35, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive_if_customer_discussion_promoted"}
{"row_type": "case", "case_id": "C09_L150_272110_SIC_CAPA_EXPANSION", "symbol": "272110", "company_name": "케이엔제이", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SIC_RING_CAPA_EXPANSION_HARD_COMMERCIAL_BRIDGE", "case_type": "capa_expansion_positive", "positive_or_counterexample": "positive", "best_trigger": "T_C09_L150_272110_SIC_CAPA_EXPANSION", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "current_profile_verdict": "current_profile_missed_structural_if_c09_blocks_all_non_order_capex", "price_source": "Songdaiki/stock-web", "evidence_url": "https://www.thelec.kr/news/articleView.html?idxno=32010"}
{"row_type": "trigger", "trigger_id": "T_C09_L150_272110_SIC_CAPA_EXPANSION", "case_id": "C09_L150_272110_SIC_CAPA_EXPANSION", "symbol": "272110", "company_name": "케이엔제이", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SIC_RING_CAPA_EXPANSION_HARD_COMMERCIAL_BRIDGE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-12-27", "entry_date": "2024-12-27", "entry_price": 14050.0, "MFE_30D_pct": 20.07, "MAE_30D_pct": -12.53, "MFE_90D_pct": 34.52, "MAE_90D_pct": -12.53, "MFE_180D_pct": 77.22, "MAE_180D_pct": -12.53, "peak_date": "2025-09-23", "peak_price": 24900.0, "trough_after_peak_date": "2025-09-23", "drawdown_after_peak_pct": -5.62, "calibration_usable": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence_url": "https://www.thelec.kr/news/articleView.html?idxno=32010", "current_profile_verdict": "current_profile_missed_structural_if_c09_blocks_all_non_order_capex", "trigger_outcome_label": "positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C09_L150_272110_SIC_CAPA_EXPANSION", "trigger_id": "T_C09_L150_272110_SIC_CAPA_EXPANSION", "symbol": "272110", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_or_hard_bridge": 4, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 5, "relative_strength": 7, "valuation_oxygen_risk": 4, "execution_or_qualification_risk": 4}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_or_hard_bridge": 7, "qualification_or_customer_quality": 6, "margin_or_revision_bridge": 6, "relative_strength": 6, "valuation_oxygen_risk": 5, "execution_or_qualification_risk": 4}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["hard_commercial_bridge_required", "qualification_ladder_guard", "high_MAE_and_4B_exit_guard"], "MFE_90D_pct": 34.52, "MAE_90D_pct": -12.53, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural_if_c09_blocks_all_non_order_capex"}
{"row_type": "aggregate", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "new_independent_case_count": 8, "same_archetype_new_symbol_count": 7, "same_archetype_new_trigger_family_count": 8, "positive_case_count": 4, "counterexample_count": 4, "stage4b_watch_or_overlay_count": 7, "current_profile_error_count": 7, "coverage_before_index_baseline": 10, "coverage_after_if_accepted_index_baseline": 18, "session_aware_after_loop126_loop135_loop143_loop150": "about_37_representative_rows"}
{"row_type": "shadow_weight", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "shadow_rule_candidate": "C09_HARD_COMMERCIAL_BRIDGE_QUALIFICATION_LADDER_AND_EXIT_GATE_V4", "do_not_propose_new_weight_delta": false, "weight_delta_candidate": {"stage2_required_bridge_scope": "tighten", "qualification_only_penalty": "+", "hard_order_or_CAPA_exception_bonus": "+", "local_4b_exit_guard": "tighten"}}
{"row_type": "residual_contribution", "round": "R2", "loop": 150, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["qualification_or_forecast_only_false_positive", "advanced_substrate_valuation_blowoff", "front_end_equipment_late_entry_high_MAE", "hard_CAPA_or_revenue_bridge_exception_positive", "local_4b_exit_after_positive_MFE"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this during research.

You are the later batch implementation agent for stock_agent. Read this MD only as one v12 residual research artifact. Validate trigger rows, deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date, and compare against data/e2r/calibration/v12 ledgers. If rows pass validation, consider a small C09-scoped patch candidate:

- require hard commercial bridge for C09 Stage2-Actionable;
- penalize qualification-only, market-size-only, and technology-forecast-only evidence when MAE90 is large;
- allow exception positive when named customer/order, hard CAPA, production qualification, or revenue-recognition window is visible;
- add local 4B exit guard for rows with high MFE but drawdown_after_peak <= -35%.

Do not loosen Stage3-Green thresholds. Do not convert this shadow rule directly into production without batch-level confirmation.
```

## 12. Next research state

```text
completed_round = R2
completed_loop = 150
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = index baseline C09 rows 10 -> 18 if accepted; session-aware after C09 loop126+135+143+150 about 37 rows
sector_specific_rule_candidate = L2_ADVANCED_EQUIPMENT_COMMERCIAL_BRIDGE_QUALIFICATION_AND_EXIT_GATE_V4
canonical_archetype_rule_candidate = C09_HARD_COMMERCIAL_BRIDGE_QUALIFICATION_LADDER_AND_EXIT_GATE_V4
loop_contribution_label = canonical_archetype_rule_candidate
```
