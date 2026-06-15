# E2R Stock-Web V12 Residual Research — R1 / C05 EPC Mega Contract Margin Gap / loop 120

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R1
selected_loop: 120
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: mixed_C05_contract_revision_cash_collection_margin_gap_holdout_v120
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 static ledger C05 rows=47 / need-to-50=3; current-session C05 already above 50, so this is a new-symbol quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

C05는 정적 No-Repeat ledger상 Priority 1의 `need-to-50=3` 구역이다. 이 세션에서는 이미 C05를 여러 번 보강했으므로 이번 loop는 수량 채우기보다 **계약/정정 공시가 실제 revenue recognition, realized margin, working-capital, cash collection bridge로 연결되는지**를 새 symbol set으로 확인하는 quality holdout이다. 같은 `canonical_archetype_id + symbol + trigger_type + entry_date` hard duplicate는 사용하지 않았다.

## 2. Price-source audit

- `stock-web` manifest: `max_date=2026-02-20`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`, `price_adjustment_status=raw_unadjusted_marcap`.
- 사용 shard: 2023~2024 tradable shard. 모든 entry row는 trigger date 당일 또는 그 이후 첫 거래일에 존재한다.
- 180D forward window는 모두 존재한다.
- 확인한 profile상 2023~2024 forward windows에서 corporate-action contamination을 감지하지 않았고, 본 파일의 usable rows는 모두 `calibration_usable=true`로 처리했다.

## 3. Case table

| ticker | name | trigger_date | entry_date | role | trigger_type | MFE180 | MAE180 | interpretation |
|---|---|---:|---:|---|---|---:|---:|---|
| 001840 | 이화공영 | 2023-07-31 | 2023-07-31 | counterexample | Stage4B | 7.9137 | -40.6475 | small_builder_contract_extension_revenue_margin_gap |
| 026150 | 특수건설 | 2023-03-28 | 2023-03-28 | positive | Stage3-Yellow | 26.7624 | -9.9217 | civil_tunnel_contract_revenue_bridge_positive |
| 002460 | HS화성 | 2023-03-27 | 2023-03-27 | positive | Stage2-Actionable | 12.7179 | -4.5128 | public_infra_contract_low_mae_stage2 |
| 001470 | 삼부토건 | 2023-10-10 | 2023-10-10 | counterexample | Stage4B | 6.5972 | -56.7708 | contract_revision_without_cash_margin_bridge |
| 013700 | 까뮤이앤씨 | 2023-12-28 | 2023-12-28 | counterexample | Stage4B | 4.7904 | -27.2455 | medium_contract_backlog_decline_high_mae |
| 002780 | 진흥기업 | 2023-11-14 | 2023-11-14 | counterexample | Stage4B | 6.2447 | -32.9114 | old_contract_revision_cost_period_gap |

## 4. Narrative findings

핵심 결론은 **C05에서 계약금액·공사수주·정정공시 headline 자체와 Stage3 margin/FCF rerating을 분리해야 한다**는 쪽이다. 특수건설은 named tunnel contract와 90D/180D MFE가 결합된 positive였지만, peak 이후 drawdown이 있어 local 4B watch가 필요했다. HS화성은 low-MAE public infra contract로 Stage2-Actionable 품질은 있으나 Stage3에는 매출인식·마진 bridge가 더 필요했다. 반대로 이화공영·삼부토건·까뮤이앤씨·진흥기업은 contract 또는 contract-revision evidence가 있어도 working-capital/cash-collection bridge가 약하면 90D/180D MAE가 깊어지는 counterexample였다.

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 120, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "small_builder_contract_extension_revenue_margin_gap", "case_id": "C05_001840_20230731_EWHAGONG_CONTRACT_PERIOD_EXTENSION_HIGH_MAE", "symbol": "001840", "symbol_name": "이화공영", "trigger_date": "2023-07-31", "entry_date": "2023-07-31", "entry_price": 4170.0, "trigger_type": "Stage4B", "case_role": "counterexample", "evidence_summary": "단일판매ㆍ공급계약 정정/계약기간 변경 공시. 공사계약 headline은 있으나 revenue recognition·margin·cash bridge가 약한 high-MAE 반례.", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20230731000240&langTpCd=0&method=search&orgid=K&rcpno=20230731000240&tran=Y", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 7.9137, "MAE_30D_pct": -12.47, "MFE_90D_pct": 7.9137, "MAE_90D_pct": -28.0576, "MFE_180D_pct": 7.9137, "MAE_180D_pct": -40.6475, "peak_date": "2023-08-09", "peak_price": 4500.0, "drawdown_after_peak_pct": -45.0, "calibration_usable": true, "representative_for_aggregate": true, "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 120, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "civil_tunnel_contract_revenue_bridge_positive", "case_id": "C05_026150_20230328_TUKSU_TUNNEL_CONTRACT_POSITIVE_WITH_4B_WATCH", "symbol": "026150", "symbol_name": "특수건설", "trigger_date": "2023-03-28", "entry_date": "2023-03-28", "entry_price": 7660.0, "trigger_type": "Stage3-Yellow", "case_role": "positive", "evidence_summary": "이천마장 물류단지 토공·구조물·터널공사 공급계약 정정. named contract와 가격경로가 결합된 positive이나 peak 후 drawdown은 local 4B watch 필요.", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20230328001088&langTpCd=0&method=search&orgid=K&rcpno=20230328001088&tran=Y", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 15.0131, "MAE_30D_pct": -2.0888, "MFE_90D_pct": 26.7624, "MAE_90D_pct": -7.3107, "MFE_180D_pct": 26.7624, "MAE_180D_pct": -9.9217, "peak_date": "2023-06-13", "peak_price": 9710.0, "drawdown_after_peak_pct": -28.9392, "calibration_usable": true, "representative_for_aggregate": true, "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 120, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "public_infra_contract_low_mae_stage2", "case_id": "C05_002460_20230327_HS_HWASEONG_METRO_CONTRACT_LOW_MAE_STAGE2", "symbol": "002460", "symbol_name": "HS화성", "trigger_date": "2023-03-27", "entry_date": "2023-03-27", "entry_price": 9750.0, "trigger_type": "Stage2-Actionable", "case_role": "positive", "evidence_summary": "광주 도시철도 관련 공사수주 정정. low-MAE와 점진 MFE는 긍정적이나 Stage3에는 매출인식·마진 bridge 추가 확인 필요.", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20230327000784&langTpCd=0&method=search&orgid=G&rcpno=20230327000784&tran=Y", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 5.2308, "MAE_30D_pct": -4.5128, "MFE_90D_pct": 10.2564, "MAE_90D_pct": -4.5128, "MFE_180D_pct": 12.7179, "MAE_180D_pct": -4.5128, "peak_date": "2023-11-27", "peak_price": 10990.0, "drawdown_after_peak_pct": -5.0045, "calibration_usable": true, "representative_for_aggregate": true, "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 120, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "contract_revision_without_cash_margin_bridge", "case_id": "C05_001470_20231010_SAMBU_CONTRACT_REVISION_HIGH_MAE", "symbol": "001470", "symbol_name": "삼부토건", "trigger_date": "2023-10-10", "entry_date": "2023-10-10", "entry_price": 2880.0, "trigger_type": "Stage4B", "case_role": "counterexample", "evidence_summary": "공급계약 정정/계약금액 언급. 계약 headline이 있어도 PF·재무구조·현금회수 bridge 없이 Stage2/3 지속 시 high-MAE로 훼손되는 반례.", "evidence_url": "https://stock.mk.co.kr/news/view/186210?type=e", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 6.5972, "MAE_30D_pct": -15.7986, "MFE_90D_pct": 6.5972, "MAE_90D_pct": -35.3472, "MFE_180D_pct": 6.5972, "MAE_180D_pct": -56.7708, "peak_date": "2023-10-10", "peak_price": 3070.0, "drawdown_after_peak_pct": -59.4463, "calibration_usable": true, "representative_for_aggregate": true, "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 120, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "medium_contract_backlog_decline_high_mae", "case_id": "C05_013700_20231228_CAMUS_CONSTRUCTION_CONTRACT_LOW_MFE_HIGH_MAE", "symbol": "013700", "symbol_name": "까뮤이앤씨", "trigger_date": "2023-12-28", "entry_date": "2023-12-28", "entry_price": 1670.0, "trigger_type": "Stage4B", "case_role": "counterexample", "evidence_summary": "조달청/목포시 수산식품 수출단지 건축공사 226억 원 공급계약. 계약 규모는 있으나 누적 공시금액 감소와 낮은 MFE/high-MAE로 Stage3 승격 차단.", "evidence_url": "https://www.datatooza.com/article/2023122814531815253f2b944494_80", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 0.8383, "MAE_30D_pct": -10.2994, "MFE_90D_pct": 4.7904, "MAE_90D_pct": -11.976, "MFE_180D_pct": 4.7904, "MAE_180D_pct": -27.2455, "peak_date": "2024-04-12", "peak_price": 1750.0, "drawdown_after_peak_pct": -30.5714, "calibration_usable": true, "representative_for_aggregate": true, "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 120, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "old_contract_revision_cost_period_gap", "case_id": "C05_002780_20231114_JINHEUNG_CONTRACT_REVISION_MARGIN_GAP", "symbol": "002780", "symbol_name": "진흥기업", "trigger_date": "2023-11-14", "entry_date": "2023-11-14", "entry_price": 1185.0, "trigger_type": "Stage4B", "case_role": "counterexample", "evidence_summary": "단일판매ㆍ공급계약 정정. 장기 공사계약 정정 자체만으로는 realized margin·working capital·cash collection bridge가 약해 Stage3 차단 필요.", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20231114002122&langTpCd=0&method=search&orgid=G&rcpno=20231114002122&tran=Y", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 6.2447, "MAE_30D_pct": -3.7975, "MFE_90D_pct": 6.2447, "MAE_90D_pct": -19.9156, "MFE_180D_pct": 6.2447, "MAE_180D_pct": -32.9114, "peak_date": "2023-11-29", "peak_price": 1259.0, "drawdown_after_peak_pct": -36.8546, "calibration_usable": true, "representative_for_aggregate": true, "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "source_proxy_only": false, "evidence_url_pending": false}
```

## 6. Score simulation / current profile stress test

```jsonl
{"row_type": "score_simulation", "case_id": "C05_001840_20230731_EWHAGONG_CONTRACT_PERIOD_EXTENSION_HIGH_MAE", "symbol": "001840", "trigger_type": "Stage4B", "raw_component_score_breakdown": {"eps_fcf_explosion": 20, "earnings_visibility": 42, "bottleneck_pricing": 20, "market_mispricing": 30, "valuation_rerating": 25, "capital_allocation": 20, "information_confidence": 60, "revision_score": 25, "margin_bridge_score": 25}, "simulated_total_score": 62.0, "current_profile_expected_route": "Stage2-Actionable unless revenue/margin/cash bridge is confirmed; Stage4B overlay if MAE90/180 breaches without second bridge", "current_profile_residual_error": "contract headline can still overstate Stage2 persistence", "red_team_risk": "high"}
{"row_type": "score_simulation", "case_id": "C05_026150_20230328_TUKSU_TUNNEL_CONTRACT_POSITIVE_WITH_4B_WATCH", "symbol": "026150", "trigger_type": "Stage3-Yellow", "raw_component_score_breakdown": {"eps_fcf_explosion": 40, "earnings_visibility": 70, "bottleneck_pricing": 20, "market_mispricing": 45, "valuation_rerating": 35, "capital_allocation": 20, "information_confidence": 60, "revision_score": 45, "margin_bridge_score": 58}, "simulated_total_score": 78.0, "current_profile_expected_route": "Stage2-Actionable unless revenue/margin/cash bridge is confirmed; Stage4B overlay if MAE90/180 breaches without second bridge", "current_profile_residual_error": "local 4B timing after fast MFE or low-MAE Stage2 confirmation", "red_team_risk": "medium"}
{"row_type": "score_simulation", "case_id": "C05_002460_20230327_HS_HWASEONG_METRO_CONTRACT_LOW_MAE_STAGE2", "symbol": "002460", "trigger_type": "Stage2-Actionable", "raw_component_score_breakdown": {"eps_fcf_explosion": 40, "earnings_visibility": 60, "bottleneck_pricing": 20, "market_mispricing": 45, "valuation_rerating": 35, "capital_allocation": 20, "information_confidence": 60, "revision_score": 35, "margin_bridge_score": 48}, "simulated_total_score": 70.0, "current_profile_expected_route": "Stage2-Actionable unless revenue/margin/cash bridge is confirmed; Stage4B overlay if MAE90/180 breaches without second bridge", "current_profile_residual_error": "local 4B timing after fast MFE or low-MAE Stage2 confirmation", "red_team_risk": "low"}
{"row_type": "score_simulation", "case_id": "C05_001470_20231010_SAMBU_CONTRACT_REVISION_HIGH_MAE", "symbol": "001470", "trigger_type": "Stage4B", "raw_component_score_breakdown": {"eps_fcf_explosion": 20, "earnings_visibility": 40, "bottleneck_pricing": 20, "market_mispricing": 30, "valuation_rerating": 25, "capital_allocation": 20, "information_confidence": 55, "revision_score": 15, "margin_bridge_score": 12}, "simulated_total_score": 55.0, "current_profile_expected_route": "Stage2-Actionable unless revenue/margin/cash bridge is confirmed; Stage4B overlay if MAE90/180 breaches without second bridge", "current_profile_residual_error": "contract headline can still overstate Stage2 persistence", "red_team_risk": "very_high"}
{"row_type": "score_simulation", "case_id": "C05_013700_20231228_CAMUS_CONSTRUCTION_CONTRACT_LOW_MFE_HIGH_MAE", "symbol": "013700", "trigger_type": "Stage4B", "raw_component_score_breakdown": {"eps_fcf_explosion": 20, "earnings_visibility": 48, "bottleneck_pricing": 20, "market_mispricing": 30, "valuation_rerating": 25, "capital_allocation": 20, "information_confidence": 60, "revision_score": 20, "margin_bridge_score": 20}, "simulated_total_score": 57.0, "current_profile_expected_route": "Stage2-Actionable unless revenue/margin/cash bridge is confirmed; Stage4B overlay if MAE90/180 breaches without second bridge", "current_profile_residual_error": "contract headline can still overstate Stage2 persistence", "red_team_risk": "high"}
{"row_type": "score_simulation", "case_id": "C05_002780_20231114_JINHEUNG_CONTRACT_REVISION_MARGIN_GAP", "symbol": "002780", "trigger_type": "Stage4B", "raw_component_score_breakdown": {"eps_fcf_explosion": 20, "earnings_visibility": 45, "bottleneck_pricing": 20, "market_mispricing": 30, "valuation_rerating": 25, "capital_allocation": 20, "information_confidence": 60, "revision_score": 18, "margin_bridge_score": 22}, "simulated_total_score": 58.0, "current_profile_expected_route": "Stage2-Actionable unless revenue/margin/cash bridge is confirmed; Stage4B overlay if MAE90/180 breaches without second bridge", "current_profile_residual_error": "contract headline can still overstate Stage2 persistence", "red_team_risk": "high"}
```

## 7. Aggregate summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
calibration_usable_rows: 6
representative_rows: 6
positive_case_count: 2
counterexample_count: 4
4B_case_count: 4
4C_case_count: 0
current_profile_error_count: 4
avg_MFE_180D_pct: 10.8377
avg_MAE_180D_pct: -28.6683
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
```

## 8. Shadow rule candidate

```text
C05_CONTRACT_REVISION_REQUIRES_REVENUE_MARGIN_WORKING_CAPITAL_AND_CASH_COLLECTION_GATE_V120
```

Rule meaning: C05에서 단일판매/공급계약, 정정공시, 계약기간 연장, 공사수주 headline은 Stage2-Actionable의 출발점이 될 수 있다. 그러나 Stage3-Yellow 이상은 revenue recognition, realized OPM/margin bridge, working-capital 안정, cash collection 또는 원가율 개선 중 최소 두 축 이상이 확인될 때만 허용한다. 두 번째 bridge 없이 MAE90 또는 MAE180이 깊어지면 local Stage4B overlay를 강제한다.

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute now. Later, in a coding-agent session, ingest this MD together with other V12 research files using the batch calibration pipeline. Treat all trigger rows as shadow evidence only. Consider a C05-specific guard: contract/order headlines require revenue recognition + margin/working-capital/cash-collection confirmation before Stage3-Yellow/Green. If MAE90/MAE180 breaches while this bridge is absent, route to Stage2-Watch or local Stage4B overlay. Do not change production scoring from this single file alone.
```

## 10. Batch Ingest Self-Audit

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

## 11. Next research state

```yaml
completed_round: R1
completed_loop: 120
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 static C05 / quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_or_cash_collection_path
```