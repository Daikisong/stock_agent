# E2R Stock-Web v12 Residual Research — R4 / C17 CHEMICAL COMMODITY MARGIN SPREAD / loop 142

## Metadata

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 142
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: mixed_C17_petchem_spread_margin_fcf_and_nonchemical_mfe_decontamination_holdout_v142
output_filename: e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / quality holdout; static C17 rows=71, guidance=URL/proxy 보강 및 반례/4B/4C 균형 확인
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## Selection rationale

`V12_Research_No_Repeat_Index.md` 기준 C17은 이미 50 row 이상인 Priority 2 구역이다. 따라서 이번 실행은 새 종목 수량 채우기가 아니라, 기존 C17이 반복적으로 헷갈리는 **석유화학 spread 회복 / 손익 개선 / 비화학 optionality MFE 오염**을 분리하는 품질 holdout으로 설계했다.

기존 `v12_md_registry.jsonl`에서 C17 표준 파일은 `R4_loop_141`까지 확인되므로, loop rule에 따라 이번 파일은 `R4_loop_142`를 사용한다.

## Price source validation

```yaml
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
mfe_mae_windows: [30D, 90D, 180D]
entry_price_rule: entry_date close
corporate_action_profile_check: passed_for_selected_180D_windows
insufficient_forward_window_rows: 0
```

Corporate-action check summary:

| symbol | profile check | 180D window usable |
|---|---:|---:|
| 011170 롯데케미칼 | corporate action candidate exists in 2023-02 only; selected 2024 windows do not overlap | true |
| 051910 LG화학 | no corporate action candidate dates in profile | true |
| 011790 SKC | old candidates in 1998/2001 only; selected 2023-2024 windows do not overlap | true |

## Evidence source matrix

| symbol | trigger_date | source type | evidence summary |
|---|---:|---|---|
| 011170 롯데케미칼 | 2024-02-07 | company/news | 2023 annual revenue KRW 19.9491tn and operating loss KRW 333.2bn; basic material spread pressure remained. |
| 011170 롯데케미칼 | 2024-05-09 | company release | 2024 Q1 revenue KRW 5.0861tn and operating loss KRW 135.3bn; QoQ improvement but still no confirmed spread-to-margin bridge. |
| 051910 LG화학 | 2024-01-31 | broker/industry report | 2023 petrochemical loss and weak demand/spread backdrop; early rebound evidence remained incomplete. |
| 051910 LG화학 | 2024-07-25 | press article / earnings | 2024 Q2 petrochemical segment turned to operating profit, but improvement was constrained by demand and freight risks. |
| 011790 SKC | 2023-08-09 | YNA earnings article | Q2 operating loss and weak demand across basic materials/chemical exposure. |
| 011790 SKC | 2023-10-31 | YNA earnings article | Q3 operating loss KRW 44.7bn and revenue decline; later MFE was not clean C17 spread evidence. |

## Case table

| # | symbol | name | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 011170 | 롯데케미칼 | Stage4B | 2024-02-07 | 2024-02-08 | 134700 | 3.4150 | -13.2888 | 3.4150 | -28.6563 | 3.4150 | -43.2071 | counterexample |
| 2 | 011170 | 롯데케미칼 | Stage4B | 2024-05-09 | 2024-05-10 | 108600 | 15.5617 | -3.6832 | 15.5617 | -29.5580 | 15.5617 | -50.8287 | counterexample |
| 3 | 051910 | LG화학 | Stage4B | 2024-01-31 | 2024-02-01 | 430000 | 20.9302 | -3.0233 | 20.9302 | -18.6047 | 20.9302 | -38.7209 | counterexample |
| 4 | 051910 | LG화학 | Stage3-Yellow | 2024-07-25 | 2024-07-26 | 307000 | 13.1922 | -14.1694 | 20.0326 | -19.8697 | 20.0326 | -34.0391 | positive_with_4B_watch |
| 5 | 011790 | SKC | Stage4B | 2023-08-09 | 2023-08-10 | 97000 | 8.7629 | -19.5876 | 8.7629 | -29.8969 | 54.3299 | -29.8969 | nonchemical_MFE_contamination_counterexample |
| 6 | 011790 | SKC | Stage4B | 2023-11-02 | 2023-11-03 | 83900 | 22.6460 | -0.8343 | 38.1406 | -14.1836 | 138.3790 | -14.1836 | nonchemical_MFE_contamination_counterexample |

## Interpretation

C17에서 가장 큰 잔여 오류는 “업황 바닥 / 적자폭 축소 / commodity beta / 그룹 내 다른 성장 옵션”을 전부 석유화학 spread 회복으로 과신하는 것이다. 이번 6개 row는 이 오류를 세 갈래로 분리한다.

첫째, 롯데케미칼은 2023년 연간 손실과 2024년 1분기 손실 축소가 있었지만, entry 기준으로는 spread → operating margin → FCF bridge가 부족했다. 두 row 모두 180D MFE가 제한적이거나 짧게 열렸고, 180D MAE는 각각 -43.2071%, -50.8287%까지 깊어졌다. 이 케이스는 C17에서 `loss narrowing`만으로 Stage2-Actionable이나 Stage3-Yellow를 열면 안 된다는 반례다.

둘째, LG화학은 2024년 2분기 석유화학 흑자전환이라는 진짜 positive evidence를 제공한다. 다만 180D MAE가 -34.0391%였으므로 Stage3-Yellow credit을 주더라도 local 4B watch가 같이 붙어야 한다. 즉 “흑자전환”은 C17 positive의 필요조건에 가깝지만, full-window drawdown guard를 해제할 충분조건은 아니다.

셋째, SKC는 C17에서 특히 위험한 `nonchemical_MFE_contamination`을 보여준다. 2023년 2~3분기 손실과 약한 화학/기초소재 환경에도 180D MFE가 크게 열렸는데, 이는 화학 spread margin bridge라기보다 동박, 반도체 패키징, 글라스기판 등 비화학 optionality가 섞인 가격경로다. 따라서 SKC 같은 다사업 소재사는 C17 positive로 credit하기 전에 chemical segment spread/OPM/FCF를 분리해야 한다.

## Proposed rule candidate

```text
C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION
```

Rule sketch:

```text
if canonical_archetype_id == C17:
  require at least two of:
    - realized product-feedstock spread improvement
    - petrochemical/chemical segment operating profit or OPM recovery
    - working-capital / inventory loss pressure easing
    - FCF or cash conversion improvement
    - management guidance explicitly tied to spread, not merely portfolio optionality
  if MFE comes mainly from battery/glass/semiconductor/material optionality outside chemical spread:
    cap C17 credit to Stage2-Watch or Stage4B overlay
  if MAE90 <= -25% or MAE180 <= -30% before confirmed bridge:
    block Stage3-Green and require local 4B watch
```

## Aggregate metrics

```yaml
positive_case_count: 1
counterexample_count: 5
stage4b_rows: 6
stage4c_rows: 0
calibration_usable_rows: 6
representative_rows: 6
avg_MFE_180D_pct: 42.1081
avg_MAE_180D_pct: -35.1460
rows_with_MAE180_below_minus_30pct: 4
high_MFE_nonchemical_contamination_rows: 2
current_profile_error_count: 5
```

## Machine-readable rows

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "mixed_C17_petchem_spread_margin_fcf_and_nonchemical_mfe_decontamination_holdout_v142", "symbol": "011170", "name": "롯데케미칼", "trigger_type": "Stage4B", "trigger_date": "2024-02-07", "entry_date": "2024-02-08", "entry_price": 134700.0, "MFE_30D_pct": 3.415, "MAE_30D_pct": -13.2888, "MFE_90D_pct": 3.415, "MAE_90D_pct": -28.6563, "MFE_180D_pct": 3.415, "MAE_180D_pct": -43.2071, "peak_date_180D": "2024-02-19", "peak_price_180D": 139300.0, "drawdown_after_peak_180D_pct": -45.0826, "last_window_date_180D": "2024-11-06", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "evidence_url": "https://www.investchosun.com/site/data/html_dir/2024/02/07/2024020780224.html", "evidence_summary": "2023 full-year loss and basic-material spread weakness; naphtha/spread pressure remained.", "role": "counterexample", "positive_case": false, "counterexample": true, "current_profile_error": true, "proposed_shadow_rule": "C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION", "raw_component_score_breakdown": {"eps_fcf_explosion": 16, "earnings_visibility": 24, "bottleneck_pricing": 18, "market_mispricing": 32, "valuation_rerating": 22, "capital_allocation": 18, "information_confidence": 58}}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "mixed_C17_petchem_spread_margin_fcf_and_nonchemical_mfe_decontamination_holdout_v142", "symbol": "011170", "name": "롯데케미칼", "trigger_type": "Stage4B", "trigger_date": "2024-05-09", "entry_date": "2024-05-10", "entry_price": 108600.0, "MFE_30D_pct": 15.5617, "MAE_30D_pct": -3.6832, "MFE_90D_pct": 15.5617, "MAE_90D_pct": -29.558, "MFE_180D_pct": 15.5617, "MAE_180D_pct": -50.8287, "peak_date_180D": "2024-05-20", "peak_price_180D": 125500.0, "drawdown_after_peak_180D_pct": -57.4502, "last_window_date_180D": "2025-02-07", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "evidence_url": "https://www.lottechem.com/ko/media/news/917/view.do", "evidence_summary": "2024 Q1 sales improved QoQ but operating loss remained KRW 135.3bn; portfolio reorganization rather than confirmed spread/FCF bridge.", "role": "counterexample", "positive_case": false, "counterexample": true, "current_profile_error": true, "proposed_shadow_rule": "C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION", "raw_component_score_breakdown": {"eps_fcf_explosion": 20, "earnings_visibility": 30, "bottleneck_pricing": 20, "market_mispricing": 36, "valuation_rerating": 24, "capital_allocation": 20, "information_confidence": 63}}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "mixed_C17_petchem_spread_margin_fcf_and_nonchemical_mfe_decontamination_holdout_v142", "symbol": "051910", "name": "LG화학", "trigger_type": "Stage4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 430000.0, "MFE_30D_pct": 20.9302, "MAE_30D_pct": -3.0233, "MFE_90D_pct": 20.9302, "MAE_90D_pct": -18.6047, "MFE_180D_pct": 20.9302, "MAE_180D_pct": -38.7209, "peak_date_180D": "2024-02-19", "peak_price_180D": 520000.0, "drawdown_after_peak_180D_pct": -49.3269, "last_window_date_180D": "2024-10-30", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "evidence_url": "https://securities.miraeasset.com/bbs/download/2121597.pdf?attachmentId=2121597", "evidence_summary": "2023 petrochemical business loss/weak spread context; early rebound thesis lacked confirmed spread-to-margin-to-FCF bridge at entry.", "role": "counterexample", "positive_case": false, "counterexample": true, "current_profile_error": true, "proposed_shadow_rule": "C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION", "raw_component_score_breakdown": {"eps_fcf_explosion": 28, "earnings_visibility": 36, "bottleneck_pricing": 24, "market_mispricing": 42, "valuation_rerating": 34, "capital_allocation": 22, "information_confidence": 62}}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "mixed_C17_petchem_spread_margin_fcf_and_nonchemical_mfe_decontamination_holdout_v142", "symbol": "051910", "name": "LG화학", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-07-25", "entry_date": "2024-07-26", "entry_price": 307000.0, "MFE_30D_pct": 13.1922, "MAE_30D_pct": -14.1694, "MFE_90D_pct": 20.0326, "MAE_90D_pct": -19.8697, "MFE_180D_pct": 20.0326, "MAE_180D_pct": -34.0391, "peak_date_180D": "2024-09-27", "peak_price_180D": 368500.0, "drawdown_after_peak_180D_pct": -45.0475, "last_window_date_180D": "2025-04-24", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "evidence_url": "https://www.etnews.com/20240725000186", "evidence_summary": "2024 Q2 petrochemical segment turned to operating profit, but management still noted limited improvement due to global demand and freight constraints.", "role": "positive_with_4B_watch", "positive_case": true, "counterexample": false, "current_profile_error": false, "proposed_shadow_rule": "C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION", "raw_component_score_breakdown": {"eps_fcf_explosion": 54, "earnings_visibility": 60, "bottleneck_pricing": 42, "market_mispricing": 52, "valuation_rerating": 48, "capital_allocation": 32, "information_confidence": 70}}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "mixed_C17_petchem_spread_margin_fcf_and_nonchemical_mfe_decontamination_holdout_v142", "symbol": "011790", "name": "SKC", "trigger_type": "Stage4B", "trigger_date": "2023-08-09", "entry_date": "2023-08-10", "entry_price": 97000.0, "MFE_30D_pct": 8.7629, "MAE_30D_pct": -19.5876, "MFE_90D_pct": 8.7629, "MAE_90D_pct": -29.8969, "MFE_180D_pct": 54.3299, "MAE_180D_pct": -29.8969, "peak_date_180D": "2024-04-09", "peak_price_180D": 149700.0, "drawdown_after_peak_180D_pct": -29.7261, "last_window_date_180D": "2024-05-08", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "evidence_url": "https://en.yna.co.kr/view/AEN20230809002751320", "evidence_summary": "2023 Q2 operating loss and weak basic materials/chemical demand; later price MFE was contaminated by battery/semiconductor optionality rather than chemical spread margin.", "role": "nonchemical_MFE_contamination_counterexample", "positive_case": false, "counterexample": true, "current_profile_error": true, "proposed_shadow_rule": "C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION", "raw_component_score_breakdown": {"eps_fcf_explosion": 22, "earnings_visibility": 28, "bottleneck_pricing": 22, "market_mispricing": 46, "valuation_rerating": 52, "capital_allocation": 30, "information_confidence": 66}}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "mixed_C17_petchem_spread_margin_fcf_and_nonchemical_mfe_decontamination_holdout_v142", "symbol": "011790", "name": "SKC", "trigger_type": "Stage4B", "trigger_date": "2023-11-02", "entry_date": "2023-11-03", "entry_price": 83900.0, "MFE_30D_pct": 22.646, "MAE_30D_pct": -0.8343, "MFE_90D_pct": 38.1406, "MAE_90D_pct": -14.1836, "MFE_180D_pct": 138.379, "MAE_180D_pct": -14.1836, "peak_date_180D": "2024-06-18", "peak_price_180D": 200000.0, "drawdown_after_peak_180D_pct": -33.95, "last_window_date_180D": "2024-07-26", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "evidence_url": "https://www.yna.co.kr/view/AKR20231031048700527", "evidence_summary": "2023 Q3 operating loss of KRW 44.7bn and revenue decline; strong later MFE is not clean C17 chemical spread evidence.", "role": "nonchemical_MFE_contamination_counterexample", "positive_case": false, "counterexample": true, "current_profile_error": true, "proposed_shadow_rule": "C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION", "raw_component_score_breakdown": {"eps_fcf_explosion": 24, "earnings_visibility": 30, "bottleneck_pricing": 24, "market_mispricing": 58, "valuation_rerating": 68, "capital_allocation": 34, "information_confidence": 68}}
{"row_type": "aggregate_metric", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "calibration_usable_rows": 6, "representative_rows": 6, "positive_case_count": 1, "counterexample_count": 5, "stage4b_rows": 6, "stage4c_rows": 0, "avg_MFE_180D_pct": 42.1081, "avg_MAE_180D_pct": -35.146, "rows_with_MAE180_below_minus_30pct": 4, "high_MFE_nonchemical_contamination_rows": 2, "current_profile_error_count": 5, "aggregate_read": "C17 chemical spread evidence remains fragile unless spread improvement converts into OPM/FCF; SKC rows show why nonchemical MFE must be decontaminated before crediting C17."}
{"row_type": "shadow_weight", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "candidate_rule_id": "C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION", "suggested_effect": {"earnings_visibility_gate": "+", "bottleneck_pricing_requires_realized_spread": "+", "market_mispricing_reduce_if_loss_continues": "+", "valuation_rerating_cap_if_nonchemical_MFE": "+", "local_4b_overlay_if_MAE90_or_MAE180_deep": "+"}, "do_not_apply_now": true, "shadow_weight_only": true}
{"row_type": "residual_contribution", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "loop_contribution_label": "quality_holdout_rule_candidate", "new_axis_proposed": "C17_nonchemical_MFE_decontamination_and_spread_margin_FCF_gate", "existing_axis_strengthened": "stage2_required_bridge | local_4b_watch_guard | price_only_blowoff_blocks_positive_stage", "existing_axis_weakened": null}
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "011170", "entry_date": "2024-02-08", "trigger_type_before_shadow": "Stage4B", "score_before_shadow_rule": 70.0, "score_after_shadow_rule": 57.0, "stage_after_shadow_rule": "Stage2-Watch_or_Stage4B", "reason": "Require realized spread-to-OPM/FCF bridge and cap nonchemical optionality-driven MFE before C17 Stage3 credit."}
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "011170", "entry_date": "2024-05-10", "trigger_type_before_shadow": "Stage4B", "score_before_shadow_rule": 70.0, "score_after_shadow_rule": 57.0, "stage_after_shadow_rule": "Stage2-Watch_or_Stage4B", "reason": "Require realized spread-to-OPM/FCF bridge and cap nonchemical optionality-driven MFE before C17 Stage3 credit."}
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "051910", "entry_date": "2024-02-01", "trigger_type_before_shadow": "Stage4B", "score_before_shadow_rule": 70.0, "score_after_shadow_rule": 57.0, "stage_after_shadow_rule": "Stage2-Watch_or_Stage4B", "reason": "Require realized spread-to-OPM/FCF bridge and cap nonchemical optionality-driven MFE before C17 Stage3 credit."}
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "051910", "entry_date": "2024-07-26", "trigger_type_before_shadow": "Stage3-Yellow", "score_before_shadow_rule": 78.0, "score_after_shadow_rule": 74.5, "stage_after_shadow_rule": "Stage2-Actionable_or_Stage3-Yellow_with_4B_watch", "reason": "Require realized spread-to-OPM/FCF bridge and cap nonchemical optionality-driven MFE before C17 Stage3 credit."}
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "011790", "entry_date": "2023-08-10", "trigger_type_before_shadow": "Stage4B", "score_before_shadow_rule": 72.0, "score_after_shadow_rule": 59.0, "stage_after_shadow_rule": "Stage4B_nonchemical_MFE_decontaminated", "reason": "Require realized spread-to-OPM/FCF bridge and cap nonchemical optionality-driven MFE before C17 Stage3 credit."}
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "round": "R4", "loop": 142, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "011790", "entry_date": "2023-11-03", "trigger_type_before_shadow": "Stage4B", "score_before_shadow_rule": 72.0, "score_after_shadow_rule": 59.0, "stage_after_shadow_rule": "Stage4B_nonchemical_MFE_decontaminated", "reason": "Require realized spread-to-OPM/FCF bridge and cap nonchemical optionality-driven MFE before C17 Stage3 credit."}
```

## Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent E2R calibration. Do not treat this MD as an instruction to patch production scoring immediately. In the next batch ingest, parse this file as v12_sector_archetype_residual. Validate that every trigger row has entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct. Then evaluate whether C17_CHEMICAL_COMMODITY_SPREAD_REQUIRES_SPREAD_OPM_FCF_BRIDGE_AND_NONCHEMICAL_MFE_DECONTAMINATION should become a shadow rule candidate for C17 only. Do not generalize it to C15/C16 without separate evidence. Preserve production scoring until the broader batch promotion decision confirms enough C17 holdout support.
```

## Next research state

```yaml
completed_round: R4
completed_loop: 142
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_holdout_only_if_new_naphtha_or_derivative_spread_bridge
  - C22_INSURANCE_RATE_CYCLE_RESERVE_quality_holdout
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
```

## Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```
