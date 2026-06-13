# E2R Stock-Web V12 Residual Research — R8 loop 103 / C28 SOFTWARE SECURITY CONTRACT RETENTION
## Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 103
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: mixed_C28_cloud_saas_idc_api_retention_boundary_v103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger C28 rows=28 / need-to-30=2 / need-to-50=22
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
## Selection rationale
No-Repeat Index의 정적 장부에서 C28은 28 rows로 Priority 0에 남아 있으며, R8/L8에 매핑된다. 이번 파일은 기존 세션에서 사용한 보안/SaaS 대표주를 피하고, 클라우드·IDC·원격근무·API·하이브리드 클라우드 쪽의 새 symbol 6개를 사용해 C28의 `contract retention / renewal / recurring revenue / margin bridge` gate를 다시 검증한다.
## Stock-Web manifest and validation scope
- manifest max_date: 2026-02-20
- source_name: FinanceData/marcap
- calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
- raw/unadjusted OHLC; corporate-action-contaminated 180D window is blocked by default.
- MFE/MAE are computed from the entry date through 30/90/180 tradable rows using high/low.
## Case thesis summary
핵심 결론은 **C28에서 클라우드, IDC, 원격근무, API/data platform, 하이브리드·멀티 클라우드 headline 자체와 Stage3 contract-retention rerating을 분리해야 한다**는 쪽이다. Stage3-Yellow 이상은 ARR/renewal, managed-service customer expansion, recurring usage revenue, API call volume, maintenance/technical-support repeat revenue, OP-margin bridge 중 최소 두 축 이상이 붙을 때만 허용해야 한다. KINX·알서포트·쿠콘은 evidence 자체는 있었지만 second bridge가 약해 high-MAE counterexample가 되었고, 가비아는 cloud/IT·IX/IDC·security revenue mix가 low-MAE price path와 결합된 C28 positive였다. 오픈베이스와 나무기술은 delayed MFE는 있었지만 initial MAE 또는 peak drawdown 때문에 Stage2 + local 4B watch가 적합했다.
## Trigger table
| symbol | name | trigger_date | entry_date | entry_price | role | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | drawdown_after_peak |
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 093320 | 케이아이엔엑스 | 2024-02-08 | 2024-02-08 | 103400 | counterexample | 6.7698 | -18.7621 | 6.7698 | -28.3366 | 6.7698 | -40.5222 | 2024-02-13 | -44.2935 |
| 079940 | 가비아 | 2024-11-14 | 2024-11-14 | 13480 | positive | 31.5282 | -4.6736 | 55.4154 | -4.6736 | 112.9080 | -4.6736 | 2025-07-09 | -21.6028 |
| 131370 | 알서포트 | 2020-09-28 | 2020-09-28 | 14900 | counterexample | 14.7651 | -21.8121 | 17.1141 | -35.8389 | 17.1141 | -47.3826 | 2020-11-23 | -55.0716 |
| 049480 | 오픈베이스 | 2022-08-17 | 2022-08-17 | 3065 | positive_with_guardrail | 1.7945 | -26.5905 | 3.9152 | -27.7325 | 40.7830 | -27.7325 | 2023-02-09 | -35.1101 |
| 242040 | 나무기술 | 2023-11-09 | 2023-11-09 | 2050 | positive_with_guardrail | 15.1220 | -2.4878 | 42.1951 | -2.4878 | 42.1951 | -10.9756 | 2024-01-19 | -37.3928 |
| 294570 | 쿠콘 | 2024-05-14 | 2024-05-14 | 18000 | counterexample | 1.6667 | -15.6111 | 1.6667 | -43.4444 | 7.6111 | -43.4444 | 2024-12-17 | -22.8704 |

## Aggregate alignment
```yaml
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
calibration_usable_rows: 6
representative_rows: 6
positive_case_count: 1
positive_with_guardrail_count: 2
counterexample_count: 3
local_4b_watch_count: 5
avg_MFE_30D_pct: 11.9411
avg_MAE_30D_pct: -14.9895
avg_MFE_90D_pct: 21.1794
avg_MAE_90D_pct: -23.7523
avg_MFE_180D_pct: 37.8969
avg_MAE_180D_pct: -29.1218
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
```
## Residual contribution summary
```yaml
sector_specific_rule_candidate: L8_C28_CLOUD_SAAS_IDC_API_RETENTION_MARGIN_BRIDGE_GATE
canonical_archetype_rule_candidate: C28_RECURRING_REVENUE_RETENTION_REQUIRES_USAGE_RENEWAL_OR_MARGIN_BRIDGE_WITH_THEME_4B_CAP_V103
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C28_second_bridge_confirmation_for_cloud_saas_idc_api_rows
existing_axis_strengthened: stage2_required_bridge | local_4b_watch_guard | full_4b_requires_non_price_evidence | price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
```
## Machine-readable trigger rows JSONL
```jsonl
{"MAE_180D_pct": -40.5222, "MAE_30D_pct": -18.7621, "MAE_90D_pct": -28.3366, "MFE_180D_pct": 6.7698, "MFE_30D_pct": 6.7698, "MFE_90D_pct": 6.7698, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_role": "counterexample", "drawdown_after_peak_pct": -44.2935, "entry_date": "2024-02-08", "entry_price": 103400.0, "evidence_family": "IDC_Cloudhub_capacity_opening_without_margin_bridge", "evidence_url": "https://company.kinx.net/wp-content/uploads/2024/02/KINX_IR_Book_Kor_240208.pdf", "evidence_url_pending": false, "fine_archetype_id": "mixed_C28_cloud_saas_idc_api_retention_boundary_v103", "insufficient_forward_window": false, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "케이아이엔엑스", "peak_date": "2024-02-13", "peak_price": 110400.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 50, "capital_allocation": 20, "earnings_visibility": 45, "eps_fcf_explosion": 35, "information_confidence": 65, "market_mispricing": 42, "profile_decision": "block_Stage3; Stage2-Watch + local_4B", "total_score_proxy": 61.5, "valuation_rerating": 30}, "representative_for_aggregate": true, "rule_note": "과천 데이터센터 CAPEX와 Cloudhub 성장은 강하지만, C28 contract-retention 관점에서는 고객 계약률·매출인식·마진 레버리지 확인 전 Stage3 금지.", "source_proxy_only": false, "stage_outcome": "Stage2-Watch_to_4B_LocalWatch", "symbol": "093320", "trigger_date": "2024-02-08", "trigger_type": "Stage2-Actionable", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -4.6736, "MAE_30D_pct": -4.6736, "MAE_90D_pct": -4.6736, "MFE_180D_pct": 112.908, "MFE_30D_pct": 31.5282, "MFE_90D_pct": 55.4154, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_role": "positive", "drawdown_after_peak_pct": -21.6028, "entry_date": "2024-11-14", "entry_price": 13480.0, "evidence_family": "cloud_IT_security_revenue_mix_and_recurring_service_bridge", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20241114001755&docno=&method=search&viewerhost=", "evidence_url_pending": false, "fine_archetype_id": "mixed_C28_cloud_saas_idc_api_retention_boundary_v103", "insufficient_forward_window": false, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "가비아", "peak_date": "2025-07-09", "peak_price": 28700.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 55, "capital_allocation": 45, "earnings_visibility": 70, "eps_fcf_explosion": 62, "information_confidence": 72, "market_mispricing": 65, "profile_decision": "allow_Stage3-Yellow; Green only after renewal/margin confirmation", "total_score_proxy": 78.4, "valuation_rerating": 68}, "representative_for_aggregate": true, "rule_note": "클라우드·IT, IX/IDC, 보안 매출비중이 함께 확인되어 C28 recurring service bridge가 비교적 선명하고 MAE도 낮았다.", "source_proxy_only": false, "stage_outcome": "Stage3-Yellow_positive", "symbol": "079940", "trigger_date": "2024-11-14", "trigger_type": "Stage3-Yellow", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -47.3826, "MAE_30D_pct": -21.8121, "MAE_90D_pct": -35.8389, "MFE_180D_pct": 17.1141, "MFE_30D_pct": 14.7651, "MFE_90D_pct": 17.1141, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_role": "counterexample", "drawdown_after_peak_pct": -55.0716, "entry_date": "2020-09-28", "entry_price": 14900.0, "evidence_family": "remote_work_solution_demand_spike_not_retention_persistence", "evidence_url": "https://www.datanews.co.kr/news/article.html?no=108136", "evidence_url_pending": false, "fine_archetype_id": "mixed_C28_cloud_saas_idc_api_retention_boundary_v103", "insufficient_forward_window": false, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "알서포트", "peak_date": "2020-11-23", "peak_price": 17450.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 40, "capital_allocation": 20, "earnings_visibility": 50, "eps_fcf_explosion": 65, "information_confidence": 70, "market_mispricing": 35, "profile_decision": "local_4B; pandemic demand spike de-rated", "total_score_proxy": 60.2, "valuation_rerating": 25}, "representative_for_aggregate": true, "rule_note": "상반기 실적 급증과 원격근무 수요는 실제였지만, pandemic demand spike 이후 retention/renewal 지속성 확인 전 Stage3 유지 시 deep MAE가 발생.", "source_proxy_only": false, "stage_outcome": "Theme_peak_4B_LocalWatch", "symbol": "131370", "trigger_date": "2020-09-28", "trigger_type": "Stage4B-LocalWatch", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -27.7325, "MAE_30D_pct": -26.5905, "MAE_90D_pct": -27.7325, "MFE_180D_pct": 40.783, "MFE_30D_pct": 1.7945, "MFE_90D_pct": 3.9152, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_role": "positive_with_guardrail", "drawdown_after_peak_pct": -35.1101, "entry_date": "2022-08-17", "entry_price": 3065.0, "evidence_family": "hybrid_multi_cloud_record_half_year_result", "evidence_url": "https://www.openbase.co.kr/notice/view/19?keyname=&keyword=&page=4&seq=166", "evidence_url_pending": false, "fine_archetype_id": "mixed_C28_cloud_saas_idc_api_retention_boundary_v103", "insufficient_forward_window": false, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "오픈베이스", "peak_date": "2023-02-09", "peak_price": 4315.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 45, "capital_allocation": 30, "earnings_visibility": 55, "eps_fcf_explosion": 54, "information_confidence": 68, "market_mispricing": 55, "profile_decision": "Stage2-Actionable but not Stage3", "total_score_proxy": 67.1, "valuation_rerating": 45}, "representative_for_aggregate": true, "rule_note": "하이브리드·멀티 클라우드 실적 evidence는 유효하지만, 초기 90D MAE가 깊어 C28 Stage3보다 Stage2+4B watch가 적합.", "source_proxy_only": false, "stage_outcome": "Stage2_to_delayed_MFE_with_4B_watch", "symbol": "049480", "trigger_date": "2022-08-17", "trigger_type": "Stage2-Actionable", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -10.9756, "MAE_30D_pct": -2.4878, "MAE_90D_pct": -2.4878, "MFE_180D_pct": 42.1951, "MFE_30D_pct": 15.122, "MFE_90D_pct": 42.1951, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_role": "positive_with_guardrail", "drawdown_after_peak_pct": -37.3928, "entry_date": "2023-11-09", "entry_price": 2050.0, "evidence_family": "cloud_native_partner_strategy_and_PaaS_channel_expansion", "evidence_url": "https://www.namutech.co.kr/%EB%82%98%EB%AC%B4%EA%B8%B0%EC%88%A0-%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EB%84%A4%EC%9D%B4%ED%8B%B0%EB%B8%8C-%EC%8B%9C%EB%84%88%EC%A7%80-2024-%EA%B0%9C%EC%B5%9C/", "evidence_url_pending": false, "fine_archetype_id": "mixed_C28_cloud_saas_idc_api_retention_boundary_v103", "insufficient_forward_window": false, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "나무기술", "peak_date": "2024-01-19", "peak_price": 2915.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 48, "capital_allocation": 25, "earnings_visibility": 52, "eps_fcf_explosion": 50, "information_confidence": 62, "market_mispricing": 58, "profile_decision": "Stage2-Actionable + peak 4B watch", "total_score_proxy": 69.0, "valuation_rerating": 55}, "representative_for_aggregate": true, "rule_note": "PaaS/파트너 확장 이벤트는 MFE로 이어졌으나, peak 이후 drawdown이 커서 renewal/ARR/margin bridge 없는 Stage3 지속은 제한.", "source_proxy_only": false, "stage_outcome": "Stage2_positive_with_peak_4B_watch", "symbol": "242040", "trigger_date": "2023-11-09", "trigger_type": "Stage2-Actionable", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -43.4444, "MAE_30D_pct": -15.6111, "MAE_90D_pct": -43.4444, "MFE_180D_pct": 7.6111, "MFE_30D_pct": 1.6667, "MFE_90D_pct": 1.6667, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_role": "counterexample", "drawdown_after_peak_pct": -22.8704, "entry_date": "2024-05-14", "entry_price": 18000.0, "evidence_family": "API_data_platform_revenue_without_visible_retention_margin_reacceleration", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240514001417&docno=&method=search&viewerhost=", "evidence_url_pending": false, "fine_archetype_id": "mixed_C28_cloud_saas_idc_api_retention_boundary_v103", "insufficient_forward_window": false, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "쿠콘", "peak_date": "2024-12-17", "peak_price": 19370.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 45, "capital_allocation": 25, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "profile_decision": "block_positive_stage; local_4B watch", "total_score_proxy": 56.4, "valuation_rerating": 25}, "representative_for_aggregate": true, "rule_note": "API/data 플랫폼 서사는 C28에 맞지만, as-of 시점의 call volume/usage-price/retention/margin bridge가 약해 MAE가 크게 열렸다.", "source_proxy_only": false, "stage_outcome": "Stage2_false_positive_to_4B_LocalWatch", "symbol": "294570", "trigger_date": "2024-05-14", "trigger_type": "Stage4B-LocalWatch", "window_180D_corporate_action_contaminated": false}
```
## Machine-readable aggregate / shadow rows JSONL
```jsonl
{"avg_MAE_180D_pct": -29.1218, "avg_MAE_30D_pct": -14.9895, "avg_MAE_90D_pct": -23.7523, "avg_MFE_180D_pct": 37.8969, "avg_MFE_30D_pct": 11.9411, "avg_MFE_90D_pct": 21.1794, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_count": 6, "counterexample_count": 3, "fine_archetype_id": "mixed_C28_cloud_saas_idc_api_retention_boundary_v103", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "local_4b_watch_count": 5, "positive_case_count": 1, "positive_with_guardrail_count": 2, "row_type": "aggregate", "rule_candidate": "C28_RECURRING_REVENUE_RETENTION_REQUIRES_USAGE_RENEWAL_OR_MARGIN_BRIDGE_WITH_THEME_4B_CAP_V103", "selected_loop": 103, "selected_round": "R8"}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "production_scoring_changed": false, "proposal": "increase information_confidence/earnings_visibility gating for C28 only when recurring usage or renewal bridge is visible; cap valuation_rerating when evidence is only cloud/IDC/API theme", "row_type": "shadow_weight", "shadow_weight_only": true}
```
## Evidence URL ledger
- 093320 케이아이엔엑스: https://company.kinx.net/wp-content/uploads/2024/02/KINX_IR_Book_Kor_240208.pdf
- 079940 가비아: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20241114001755&docno=&method=search&viewerhost=
- 131370 알서포트: https://www.datanews.co.kr/news/article.html?no=108136
- 049480 오픈베이스: https://www.openbase.co.kr/notice/view/19?keyname=&keyword=&page=4&seq=166
- 242040 나무기술: https://www.namutech.co.kr/%EB%82%98%EB%AC%B4%EA%B8%B0%EC%88%A0-%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EB%84%A4%EC%9D%B4%ED%8B%B0%EB%B8%8C-%EC%8B%9C%EB%84%88%EC%A7%80-2024-%EA%B0%9C%EC%B5%9C/
- 294570 쿠콘: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240514001417&docno=&method=search&viewerhost=
## Batch Ingest Self-Audit
```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 6
representative_rows: 6
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
## Deferred Coding Agent Handoff Prompt
```text
This prompt is for a later coding-agent session only. Do not execute during this research run.
Ingest this standalone MD together with other V12 research MD files. Validate that all trigger rows contain canonical_archetype_id, large_sector_id, trigger_type, entry_date, entry_price, and complete 30D/90D/180D MFE/MAE fields. Deduplicate on canonical_archetype_id + symbol + trigger_type + entry_date. If accepted, evaluate the proposed C28 shadow rule: recurring revenue / retention / usage / renewal / margin bridge must be present before C28 Stage3-Yellow/Green; cloud/IDC/API/SaaS theme-only rows should be capped at Stage2-Watch or local 4B when MAE90/180 is deep. Do not alter production scoring unless batch validation supports the patch.
```
## Next research state
```yaml
completed_round: R8
completed_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / C28 rows 28 -> expected 34 after acceptance
next_recommended_archetypes: C02_POWER_GRID_DATACENTER_CAPEX | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
