---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 100
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: mixed_C23_approval_to_commercialization_reimbursement_set
output_file: e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 / under 50 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R v12 Residual Research — R7/L7/C23 BIO REGULATORY APPROVAL → COMMERCIALIZATION

## 0. Selection Summary

이번 실행은 `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`을 선택했다. `V12_Research_No_Repeat_Index.md` 기준 C23은 `48 rows`, `21 symbols`, `need to 50 = 2`인 Priority 1 구역이다. 직전 세션 체인에서 Priority 0 및 일부 Priority 1 축을 이미 보강했기 때문에, 이번에는 50-row 실전 보정권으로 바로 들어가는 C23을 택했다.

R7/L7 hard gate는 통과한다.

```text
selected_round = R7
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
selected_loop = 100
filename = e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
```

C23의 핵심 잔여 오류는 단순하다. **regulatory approval은 문을 여는 열쇠일 뿐, Stage3는 그 문 너머에 실제 매출/royalty/reimbursement/launch route가 있는지 확인해야 한다.** 이번 케이스들은 승인 headline이 전부 같은 색으로 보이지만, 가격경로는 세 갈래로 갈라진다.

1. 승인 이후 실제 상업화 route가 바로 붙은 positive.
2. 승인 자체는 맞았지만 초기 MAE를 감내해야 했던 delayed positive.
3. 승인/EUL/허가 headline만 있고 수요·launch·reimbursement bridge가 약해 high-MAE로 무너진 counterexample.

## 1. Price Atlas Verification

```yaml
primary_price_source: Songdaiki/stock-web
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
required_forward_window: 180 trading rows
MFE_formula: (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_formula: (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

All six trigger rows have complete 30D/90D/180D MFE and MAE fields. Raw/unadjusted corporate-action risk was checked from the stock-web symbol profile snippets. No row has a corporate-action candidate inside entry~180D.

## 2. No-Repeat / Novelty Check

```yaml
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_detected: false
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count_estimate: 4
same_archetype_reused_top_covered_symbols_with_new_trigger_family: 2
reason_for_reused_top_symbols: 006280 and 170900 are already top-covered C23 symbols, but these rows use new trigger families / dates and are not hard duplicates.
positive_case_count: 3
counterexample_count: 3
4B_case_count: 3
4C_case_count: 0
calibration_usable_trigger_count: 6
```

C23 has top-covered prior symbols such as `006280` and `170900`. I still included them because ALYGLO and IMULDOSA create clean approval-to-commercialization contrast pairs: ALYGLO later gets commercialization/PBM route support, while IMULDOSA shows approval without immediate revenue timing and a severe 180D MAE. These are not duplicate `trigger_type + entry_date` rows.

## 3. Trigger-Level Backtest Table

| symbol | name | trigger_type | entry_date | entry_price | outcome | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak / post-peak DD |
|---|---|---|---:|---:|---|---:|---:|---:|---|
| 068270 | 셀트리온 | Stage3-Yellow | 2024-03-18 | 182,500 | positive_with_4b_watch | 6.36/-7.01 | 12.33/-7.01 | 15.62/-12.16 | 2024-07-30 / -24.03% |
| 145020 | 휴젤 | Stage3-Yellow | 2024-03-04 | 202,500 | positive | 8.15/-14.91 | 29.63/-14.91 | 60.99/-14.91 | 2024-11-07 / -22.85% |
| 195940 | HK이노엔 | Stage2-Actionable | 2022-04-14 | 42,700 | counterexample_local_mfe_full_window_high_mae | 22.48/-12.65 | 22.48/-12.65 | 22.48/-26.70 | 2022-05-23 / -40.15% |
| 302440 | SK바이오사이언스 | Stage2-Actionable | 2023-06-19 | 80,500 | counterexample_approval_without_demand | 4.60/-12.42 | 10.06/-29.07 | 10.06/-29.07 | 2023-08-03 / -35.55% |
| 006280 | 녹십자 | Stage3-Yellow | 2023-12-18 | 120,500 | positive_delayed_commercialization | 8.80/-10.71 | 8.80/-10.71 | 47.30/-10.71 | 2024-08-28 / -20.28% |
| 170900 | 동아에스티 | Stage2-Actionable | 2024-10-14 | 76,300 | counterexample_commercialization_lag_high_mae | 5.77/-20.05 | 5.77/-36.24 | 5.77/-46.40 | 2024-10-21 / -49.32% |

## 4. Case Notes

### 4.1 068270 셀트리온 — ZYMFENTRA U.S. commercial availability

- Trigger family: `C23_ZYMFENTRA_US_COMMERCIAL_AVAILABILITY`
- Entry: 2024-03-18 close 182,500
- Path: 180D MFE +15.62%, MAE -12.16%, post-peak drawdown -24.03%
- Interpretation: This is not a bare FDA-approval row. The March 2024 evidence is commercial availability across the U.S. The shadow rule should keep it eligible for Stage3-Yellow, but not Green, because the path still had a meaningful post-peak drawdown before access/reimbursement expanded.
- Source: https://www.celltrion.com/en-us/company/media-center/press-release/3128

### 4.2 145020 휴젤 — Letybo FDA approval with U.S. launch plan

- Trigger family: `C23_LETYBO_US_FDA_APPROVAL_LAUNCH_PLAN`
- Entry: 2024-03-04 close 202,500
- Path: 180D MFE +60.99%, MAE -14.91%
- Interpretation: FDA approval plus explicit launch plan converted into a strong C23 positive. However, the early -14.91% MAE argues against immediate Stage3-Green; the better calibration is Stage3-Yellow with launch execution/revenue confirmation required for Green.
- Source: https://hugel-aesthetics.com/news-press-releases/

### 4.3 195940 HK이노엔 — K-CAB China NMPA approval / local MFE then long drawdown

- Trigger family: `C23_KCAB_CHINA_NMPA_APPROVAL`
- Entry: 2022-04-14 close 42,700
- Path: 30D MFE +22.48%, 180D MAE -26.70%, 2Y MAE -34.66%
- Interpretation: This is the cleanest local-MFE / full-window-MAE split. Approval produced a tradable spike, but without a scored reimbursement/royalty/revenue bridge, the stock failed the full-window alignment test. C23 should not convert approval-only local MFE into Stage3 without a commercialization gate.
- Source: https://pulse.mk.co.kr/news/english/10289876

### 4.4 302440 SK바이오사이언스 — SKYCovione WHO EUL but weak commercial pull-through

- Trigger family: `C23_SKYCOVIONE_WHO_EUL_LOW_DEMAND_COUNTEREXAMPLE`
- Entry: 2023-06-19 close 80,500
- Path: 180D MFE +10.06%, MAE -29.07%, 2Y MAE -55.53%
- Interpretation: WHO EUL is valid regulatory evidence, but COVID vaccine procurement/demand was the real bottleneck. The current profile should cap this at Stage2-Actionable or 4B-watch unless procurement/revenue demand is visible.
- Source: https://www.skbioscience.com/en/news/news_01_01?id=214&mode=view

### 4.5 006280 녹십자 — ALYGLO FDA approval, delayed but real U.S. commercialization bridge

- Trigger family: `C23_ALYGLO_FDA_APPROVAL_US_COMMERCIALIZATION`
- Entry: 2023-12-18 close 120,500
- Path: 180D MFE +47.30%, MAE -10.71%
- Interpretation: At the approval date, Stage2-Actionable is enough. Stage3-Yellow becomes justified when launch/PBM/reimbursement route evidence appears. This is a delayed positive and a useful contrast against approval-only false positives.
- Source: https://www.gcbiopharma.com/eng/news_view.do?currentPage=1&idx=1379

### 4.6 170900 동아에스티 — IMULDOSA FDA approval with commercialization lag

- Trigger family: `C23_IMULDOSA_FDA_APPROVAL_COMMERCIALIZATION_LAG`
- Entry: 2024-10-14 close 76,300
- Path: 180D MFE +5.77%, MAE -46.40%
- Interpretation: FDA approval was real, but commercialization was partner-led and not immediate. This case strongly supports a C23-specific 4B cap: biosimilar approval without launch timing/reimbursement/revenue evidence should not be Stage3.
- Source: https://www.businesswire.com/news/home/20241011360476/en/US-FDA-Approves-Dong-A-STs-IMULDOSA-ustekinumab-srlf-a-Biosimilar-to-STELARA

## 5. Current Calibrated Profile Stress Test

Current C23 weights emphasize information confidence heavily. That is logical for regulatory evidence, but the residual error is that **information confidence from approval is being confused with commercial visibility**.

| issue | current behavior risk | observed path | shadow correction |
|---|---|---|---|
| FDA/NMPA/WHO approval only | Stage2/Stage3 unlock too early | HK이노엔, SK바이오사이언스, 동아에스티 show high full-window MAE | require launch/reimbursement/procurement/revenue bridge |
| commercial availability | may be underweighted if parsed as old approval | 셀트리온 has positive MFE but drawdown risk | Stage3-Yellow, not Green, until access/revenue confirms |
| FDA approval + named U.S. launch plan | strong positive but early volatility | 휴젤 +60.99% MFE, -14.91% MAE | Yellow with execution check |
| approval + later PBM/launch route | delayed positive | 녹십자 +47.30% MFE | Stage2 at approval, Stage3 after bridge evidence |

## 6. Shadow Rule Candidate

```text
C23_APPROVAL_TO_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_OR_ROYALTY_BRIDGE
```

### Rule draft

```yaml
rule_candidate: C23_APPROVAL_TO_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_OR_ROYALTY_BRIDGE
scope: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
shadow_only: true
positive_unlock:
  any_of:
    - commercial_availability_announced
    - named_launch_timing_executed_or_near_executed
    - reimbursement_or_PBM_formulary_access
    - procurement_or_contract_demand_confirmed
    - royalty_or_first_sales_visibility
stage3_block:
  if:
    - approval_or_EUL_only
    - and no_launch_or_reimbursement_or_revenue_bridge
  then:
    max_stage: Stage2-Actionable
4b_watch:
  if:
    - approval_only_event
    - and MFE_90D_pct < 12
    - and MAE_90D_pct <= -20
  then:
    route: local_4b_watch
stage3_green_block:
  always_require:
    - commercial_bridge
    - margin_or_royalty_visibility
    - no high_MAE guardrail breach
```

## 7. Residual Contribution Summary

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
sector_specific_rule_candidate: L7_C23_APPROVAL_COMMERCIALIZATION_BRIDGE_GATE
canonical_archetype_rule_candidate: C23_APPROVAL_TO_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_OR_ROYALTY_BRIDGE
new_axis_proposed:
  - C23_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_GATE
  - C23_APPROVAL_ONLY_HIGH_MAE_4B_CAP
  - C23_REIMBURSEMENT_OR_PBM_ACCESS_STAGE3_UNLOCK
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: []
do_not_propose_new_weight_delta: false
production_scoring_changed: false
shadow_weight_only: true
```

## 8. Machine-Readable JSONL Rows

```jsonl
{"row_type": "trigger", "case_id": "C23_R7_L100_01_068270_20240318", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_to_commercialization_reimbursement_set", "symbol": "068270", "name": "셀트리온", "trigger_type": "Stage3-Yellow", "trigger_family": "C23_ZYMFENTRA_US_COMMERCIAL_AVAILABILITY", "trigger_date": "2024-03-18", "entry_date": "2024-03-18", "entry_price": 182500, "entry_market": "KOSPI", "MFE_30D_pct": 6.36, "MAE_30D_pct": -7.01, "MFE_90D_pct": 12.33, "MAE_90D_pct": -7.01, "MFE_180D_pct": 15.62, "MAE_180D_pct": -12.16, "MFE_1Y_pct": 15.62, "MAE_1Y_pct": -12.16, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_180D_date": "2024-07-30", "peak_180D_price": 211000, "trough_180D_date": "2024-11-15", "trough_180D_price": 160300, "drawdown_after_peak_180D_pct": -24.03, "four_b_local_peak_proximity": 0.43, "four_b_full_window_proximity": 0.36, "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://www.celltrion.com/en-us/company/media-center/press-release/3128", "source_proxy_only": false, "evidence_url_pending": false, "outcome_label": "positive_with_4b_watch", "current_profile_error": "underweights_commercial_availability_if_modeled_as_approval_only", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 22, "bottleneck_pricing": 5, "market_mispricing": 9, "valuation_rerating": 10, "capital_allocation": 6, "information_confidence": 28}, "current_profile_score_proxy": 78, "shadow_profile_score_proxy": 80, "shadow_stage_candidate": "Stage3-Yellow"}
{"row_type": "trigger", "case_id": "C23_R7_L100_02_145020_20240304", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_to_commercialization_reimbursement_set", "symbol": "145020", "name": "휴젤", "trigger_type": "Stage3-Yellow", "trigger_family": "C23_LETYBO_US_FDA_APPROVAL_LAUNCH_PLAN", "trigger_date": "2024-03-04", "entry_date": "2024-03-04", "entry_price": 202500, "entry_market": "KOSDAQ GLOBAL", "MFE_30D_pct": 8.15, "MAE_30D_pct": -14.91, "MFE_90D_pct": 29.63, "MAE_90D_pct": -14.91, "MFE_180D_pct": 60.99, "MAE_180D_pct": -14.91, "MFE_1Y_pct": 70.86, "MAE_1Y_pct": -14.91, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_180D_date": "2024-11-07", "peak_180D_price": 326000, "trough_180D_date": "2024-03-21", "trough_180D_price": 172300, "drawdown_after_peak_180D_pct": -22.85, "four_b_local_peak_proximity": 0.35, "four_b_full_window_proximity": 0.3, "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://hugel-aesthetics.com/news-press-releases/", "source_proxy_only": false, "evidence_url_pending": false, "outcome_label": "positive", "current_profile_error": "green_too_early_if_approval_not_launch_gated", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 15, "bottleneck_pricing": 5, "market_mispricing": 13, "valuation_rerating": 10, "capital_allocation": 6, "information_confidence": 28}, "current_profile_score_proxy": 82, "shadow_profile_score_proxy": 83, "shadow_stage_candidate": "Stage3-Yellow"}
{"row_type": "trigger", "case_id": "C23_R7_L100_03_195940_20220414", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_to_commercialization_reimbursement_set", "symbol": "195940", "name": "HK이노엔", "trigger_type": "Stage2-Actionable", "trigger_family": "C23_KCAB_CHINA_NMPA_APPROVAL", "trigger_date": "2022-04-14", "entry_date": "2022-04-14", "entry_price": 42700, "entry_market": "KOSDAQ", "MFE_30D_pct": 22.48, "MAE_30D_pct": -12.65, "MFE_90D_pct": 22.48, "MAE_90D_pct": -12.65, "MFE_180D_pct": 22.48, "MAE_180D_pct": -26.7, "MFE_1Y_pct": 22.48, "MAE_1Y_pct": -26.7, "MFE_2Y_pct": 22.48, "MAE_2Y_pct": -34.66, "peak_180D_date": "2022-05-23", "peak_180D_price": 52300, "trough_180D_date": "2022-10-11", "trough_180D_price": 31300, "drawdown_after_peak_180D_pct": -40.15, "four_b_local_peak_proximity": 0.88, "four_b_full_window_proximity": 0.91, "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://pulse.mk.co.kr/news/english/10289876", "source_proxy_only": false, "evidence_url_pending": false, "outcome_label": "counterexample_local_mfe_full_window_high_mae", "current_profile_error": "approval_headline_overcredits_commercialization_without_reimbursement_or_royalty_visibility", "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 15, "bottleneck_pricing": 5, "market_mispricing": 13, "valuation_rerating": 10, "capital_allocation": 6, "information_confidence": 18}, "current_profile_score_proxy": 76, "shadow_profile_score_proxy": 66, "shadow_stage_candidate": "Stage2-blocked/4B-watch"}
{"row_type": "trigger", "case_id": "C23_R7_L100_04_302440_20230619", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_to_commercialization_reimbursement_set", "symbol": "302440", "name": "SK바이오사이언스", "trigger_type": "Stage2-Actionable", "trigger_family": "C23_SKYCOVIONE_WHO_EUL_LOW_DEMAND_COUNTEREXAMPLE", "trigger_date": "2023-06-19", "entry_date": "2023-06-19", "entry_price": 80500, "entry_market": "KOSPI", "MFE_30D_pct": 4.6, "MAE_30D_pct": -12.42, "MFE_90D_pct": 10.06, "MAE_90D_pct": -29.07, "MFE_180D_pct": 10.06, "MAE_180D_pct": -29.07, "MFE_1Y_pct": 10.06, "MAE_1Y_pct": -39.32, "MFE_2Y_pct": 10.06, "MAE_2Y_pct": -55.53, "peak_180D_date": "2023-08-03", "peak_180D_price": 88600, "trough_180D_date": "2023-10-24", "trough_180D_price": 57100, "drawdown_after_peak_180D_pct": -35.55, "four_b_local_peak_proximity": 0.82, "four_b_full_window_proximity": 0.94, "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://www.skbioscience.com/en/news/news_01_01?id=214&mode=view", "source_proxy_only": false, "evidence_url_pending": false, "outcome_label": "counterexample_approval_without_demand", "current_profile_error": "approval_or_eul_event_can_false_unlock_stage2_without_procurement_demand", "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 15, "bottleneck_pricing": 5, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 6, "information_confidence": 18}, "current_profile_score_proxy": 74, "shadow_profile_score_proxy": 57, "shadow_stage_candidate": "Stage2-blocked/4B-watch"}
{"row_type": "trigger", "case_id": "C23_R7_L100_05_006280_20231218", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_to_commercialization_reimbursement_set", "symbol": "006280", "name": "녹십자", "trigger_type": "Stage3-Yellow", "trigger_family": "C23_ALYGLO_FDA_APPROVAL_US_COMMERCIALIZATION", "trigger_date": "2023-12-18", "entry_date": "2023-12-18", "entry_price": 120500, "entry_market": "KOSPI", "MFE_30D_pct": 8.8, "MAE_30D_pct": -10.71, "MFE_90D_pct": 8.8, "MAE_90D_pct": -10.71, "MFE_180D_pct": 47.3, "MAE_180D_pct": -10.71, "MFE_1Y_pct": 50.87, "MAE_1Y_pct": -10.71, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_180D_date": "2024-08-28", "peak_180D_price": 177500, "trough_180D_date": "2024-01-31", "trough_180D_price": 107600, "drawdown_after_peak_180D_pct": -20.28, "four_b_local_peak_proximity": 0.37, "four_b_full_window_proximity": 0.31, "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://www.gcbiopharma.com/eng/news_view.do?currentPage=1&idx=1379", "source_proxy_only": false, "evidence_url_pending": false, "outcome_label": "positive_delayed_commercialization", "current_profile_error": "approval_day_stage3_should_wait_for_launch_or_pbm_but_stage2_actionable_is_valid", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 22, "bottleneck_pricing": 5, "market_mispricing": 13, "valuation_rerating": 10, "capital_allocation": 6, "information_confidence": 28}, "current_profile_score_proxy": 74, "shadow_profile_score_proxy": 79, "shadow_stage_candidate": "Stage2-Actionable_then_Stage3-Yellow_after_launch_bridge"}
{"row_type": "trigger", "case_id": "C23_R7_L100_06_170900_20241014", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_to_commercialization_reimbursement_set", "symbol": "170900", "name": "동아에스티", "trigger_type": "Stage2-Actionable", "trigger_family": "C23_IMULDOSA_FDA_APPROVAL_COMMERCIALIZATION_LAG", "trigger_date": "2024-10-11", "entry_date": "2024-10-14", "entry_price": 76300, "entry_market": "KOSPI", "MFE_30D_pct": 5.77, "MAE_30D_pct": -20.05, "MFE_90D_pct": 5.77, "MAE_90D_pct": -36.24, "MFE_180D_pct": 5.77, "MAE_180D_pct": -46.4, "MFE_1Y_pct": 5.77, "MAE_1Y_pct": -46.4, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_180D_date": "2024-10-21", "peak_180D_price": 80700, "trough_180D_date": "2025-04-09", "trough_180D_price": 40900, "drawdown_after_peak_180D_pct": -49.32, "four_b_local_peak_proximity": 0.92, "four_b_full_window_proximity": 0.97, "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://www.businesswire.com/news/home/20241011360476/en/US-FDA-Approves-Dong-A-STs-IMULDOSA-ustekinumab-srlf-a-Biosimilar-to-STELARA", "source_proxy_only": false, "evidence_url_pending": false, "outcome_label": "counterexample_commercialization_lag_high_mae", "current_profile_error": "biosimilar_fda_approval_overcredits_near_term_revenue_if_partner_launch_timing_is_not_gated", "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 22, "bottleneck_pricing": 5, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 6, "information_confidence": 18}, "current_profile_score_proxy": 75, "shadow_profile_score_proxy": 59, "shadow_stage_candidate": "Stage2-blocked/4B-watch"}
{"row_type": "aggregate", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_to_commercialization_reimbursement_set", "case_count": 6, "calibration_usable_rows": 6, "positive_case_count": 3, "counterexample_count": 3, "four_b_case_count": 3, "four_c_case_count": 0, "current_profile_error_count": 4, "same_archetype_new_symbol_count_estimate": 4, "same_archetype_reused_top_covered_symbols_with_new_trigger_family": 2, "mean_MFE_180D_pct": 27.04, "mean_MAE_180D_pct": -23.32, "positive_mean_MFE_180D_pct": 41.3, "counterexample_mean_MAE_180D_pct": -34.06}
{"row_type": "shadow_weight", "target_profile": "shadow_only_not_applied", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "rule_candidate": "C23_APPROVAL_TO_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_OR_ROYALTY_BRIDGE", "positive_unlock": "approval plus one of commercial availability, PBM/reimbursement access, named launch timing executed, first revenue/royalty evidence", "stage3_block": "approval/EUL alone without launch, reimbursement, partner commercialization timing, procurement, or revenue bridge", "local_4b_watch": "if 90D MAE <= -20% or 180D drawdown_after_peak <= -30% after approval-only spike, cap at Stage2/4B-watch until commercial bridge appears", "suggested_shadow_delta": "do not change global weights; add C23-specific gating before applying information_confidence credit", "production_scoring_changed": false}
{"row_type": "residual_contribution", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "residual_error": "C23 approval events are too heterogeneous: some are commercial launch unlocks, others are approval-only local spikes that collapse before revenue/royalty/reimbursement conversion.", "new_axis_proposed": ["C23_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_GATE", "C23_APPROVAL_ONLY_HIGH_MAE_4B_CAP", "C23_REIMBURSEMENT_OR_PBM_ACCESS_STAGE3_UNLOCK"], "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": [], "coding_agent_handoff_required": true, "handoff_prompt_executed_now": false}
```

## 9. Batch Ingest Self-Audit

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
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in /home/eorb915/projects/stock_agent after the research session has ended.
Do not reinterpret this MD as production-scoring instruction by itself. Batch-ingest it with other v12 residual research MD files.

Input file:
e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md

Tasks:
1. Validate filename, metadata, selected_round, selected_loop, large_sector_id, canonical_archetype_id.
2. Parse every JSONL row in the Machine-Readable JSONL Rows section.
3. Reject any trigger row missing entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
4. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Preserve production scoring until aggregate batch promotion gates pass.
6. Consider the shadow rule candidate C23_APPROVAL_TO_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_OR_ROYALTY_BRIDGE only as a C23-specific gate proposal.
7. If promoted, implement as a gated boost/cap around C23 information_confidence and earnings_visibility, not as a global Stage3 threshold change.
```

## 11. Next Research State

```text
completed_round = R7
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / C23 rows 48 -> expected 54 after acceptance
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_followup_if_below_50 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
