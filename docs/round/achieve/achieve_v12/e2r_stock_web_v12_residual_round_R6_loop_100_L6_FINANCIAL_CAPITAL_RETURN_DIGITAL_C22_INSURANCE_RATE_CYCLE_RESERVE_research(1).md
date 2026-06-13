# E2R Stock-Web V12 Residual Research — R6 / C22 Insurance Rate Cycle Reserve

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R6
selected_loop: 100
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: mixed_C22_ifrs17_csm_kics_rate_cycle_reserve_quality_holdout
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout; static C22 rows=60, guidance=URL/proxy repair + counterexample/4B balance
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
output_file: e2r_stock_web_v12_residual_round_R6_loop_100_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

This execution follows the V12 coverage-index-first scheduler. C22 is not an under-30 archetype, but the current No-Repeat ledger marks it as a **Priority 2 quality-holdout area**: enough rows for directional weighting, but still useful for URL/proxy repair, counterexample balance, and 4B guardrail sharpening. Since the current session has already added multiple passes to the static Priority 0 / Priority 1 buckets, this file intentionally avoids another rematerialization of C02/C09/C14/C10/C06/C07/C11/C28/C12 and uses C22 as a financial-sector quality holdout.

The output is mapped by canonical archetype:

```text
C21~C22 -> R6 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

No live-stock scan, code patch, production scoring update, or stock-agent source-code reading is included.

## 2. Stock-Web price atlas check

```yaml
manifest: atlas/manifest.json
schema: atlas/schema.json
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
max_date: 2026-02-20
forward_window_basis: stock_web_manifest_max_date_not_current_date
```

All six selected rows have full 30D/90D/180D windows before the manifest max date. Corporate-action profile checks were used to block contaminated windows.

| symbol | profile corporate-action check |
|---|---|
| 000810 | corporate_action_candidate_dates are 1999~2000 only; 2024-05-14~2025-02-11 180D window clean. |
| 003690 | corporate_action_candidate_dates end in 2004; 2024-07-01~2025-03-28 180D window clean. |
| 088350 | corporate_action_candidate_dates empty; 2024-11-13~2025-08-08 180D window clean. |
| 005830 | corporate_action_candidate_dates end in 1999; 2024-05-16~2025-02-12 180D window clean. |
| 001450 | corporate_action_candidate_dates end in 2004; 2024-10-15~2025-07-10 180D window clean. |
| 000370 | corporate_action_candidate_dates end in 2017; 2024-11-12~2025-08-07 180D window clean. |

## 3. C22 working thesis

C22 should not treat every insurance rally as the same signal. A C22 positive needs more than “insurance sector value-up” or “interest-rate beta.” The durable version normally requires at least two of the following bridges:

```text
CSM / new-contract profitability
K-ICS or excess-capital buffer
reserve-quality confirmation
rate-cycle / underwriting margin confirmation
capital-return execution or credible policy
investment-loss / FVPL risk decontamination
```

If only valuation rerating or shareholder-return expectation is visible while reserve quality, experience variance, investment losses, or loss-ratio pressure is unresolved, the row should remain Stage2-Actionable or local 4B watch. Think of the insurer as a dam: capital return is the water released downstream, but CSM, reserve quality, and K-ICS are the concrete wall. If the wall is cracked, a bigger release headline does not make the structure safer.

## 4. Case set summary

| symbol | company | trigger_date | trigger_type | role | entry | MFE/MAE 30D | MFE/MAE 90D | MFE/MAE 180D | price conclusion |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 000810 | 삼성화재 | 2024-05-14 | Stage3-Yellow | positive_structural_success | 336500 | 12.93% / -3.71% | 16.94% / -3.71% | 29.27% / -3.71% | Stage3 유지 |
| 003690 | 코리안리 | 2024-07-01 | Stage3-Yellow | positive_structural_success | 7920 | 7.32% / -1.52% | 20.58% / -1.52% | 20.58% / -2.78% | Stage3 유지 |
| 088350 | 한화생명 | 2024-11-13 | Stage2-Actionable | positive_with_high_mae_delayed_unlock | 2750 | 2.55% / -11.27% | 3.45% / -11.64% | 58.36% / -13.82% | delayed positive + 4B |
| 005830 | DB손해보험 | 2024-05-16 | Stage2-Actionable | counterexample_capital_return_without_reserve_margin_confirmation | 111500 | 2.42% / -12.83% | 11.21% / -15.61% | 11.21% / -19.01% | Stage2/4B cap |
| 001450 | 현대해상 | 2024-10-15 | Stage4B | counterexample_investment_loss_reserve_trust_guard | 31900 | 0.31% / -14.58% | 0.31% / -25.86% | 0.31% / -37.81% | Stage2/4B cap |
| 000370 | 한화손해보험 | 2024-11-12 | Stage2-Actionable | high_mfe_high_mae_success_with_4b_watch | 4550 | 5.38% / -13.08% | 5.38% / -15.93% | 79.12% / -20.00% | delayed positive + 4B |

Aggregate price path:

```yaml
trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
positive_case_count: 3
counterexample_count: 3
local_4b_watch_count: 5
hard_4c_count: 0
current_profile_error_count: 4
avg_MFE_30D_pct: 5.1526
avg_MAE_30D_pct: -9.4969
avg_MFE_90D_pct: 9.6472
avg_MAE_90D_pct: -12.378
avg_MFE_180D_pct: 33.1436
avg_MAE_180D_pct: -16.1883
```

## 5. Case notes

### 5.1 000810 Samsung Fire & Marine — capital buffer positive, but not Green by default

Trigger evidence showed a strong capital buffer / K-ICS setup. The 180D path was cleanly positive with shallow MAE, supporting Stage3-Yellow. But the drawdown after the 180D peak was still more than 20%, so the shadow rule should not auto-Green the row unless capital-return execution and reserve-quality persistence are both visible.

### 5.2 003690 Korean Re — reinsurance rate-cycle positive

Korean Re is the cleanest C22 rate-cycle example in this holdout. The 30D/90D/180D MAE stayed shallow while 90D MFE exceeded 20%. This is the row that argues against over-penalizing the entire insurance sector under a generic financial 4B overlay.

### 5.3 088350 Hanwha Life — CSM delayed unlock

The CSM / new-contract APE evidence was real, but the first 90D path was weak. The 180D MFE later opened materially. This case should not be discarded as a failed Stage2; it is better treated as Stage2-Actionable with a delayed CSM unlock buffer and local 4B watch.

### 5.4 005830 DB Insurance — capital-return headline is not enough

DB Insurance had shareholder-return and K-ICS-oriented evidence, but the forward path produced limited MFE and meaningful MAE. The row is a useful C22 false-positive guard: capital return has to be paired with reserve quality, underwriting margin, and investment-loss decontamination before Stage3-Yellow.

### 5.5 001450 Hyundai Marine & Fire — investment-loss / reserve trust guard

This is the hardest C22 counterexample in the batch. MFE was almost absent and MAE deepened across 30D, 90D, and 180D. Any model that opens Stage2/3 here from broad insurance value-up or rate-cycle beta is likely too permissive.

### 5.6 000370 Hanwha General Insurance — high-MFE / high-MAE success with 4B watch

Hanwha General Insurance produced large 180D MFE, but the entry path first cut deeply below the trigger price. The thesis should not be deleted, but sizing/staging should be guarded: Stage2-Actionable is acceptable; Stage3 should wait for experience variance, auto/general loss, and reserve-quality confirmation.

## 6. Score simulation summary

| case_id | simulated_current_score | shadow_score | expected current | expected shadow | key error |
|---|---:|---:|---|---|---|
| C22_000810_20240514_SAMSUNG_FIRE_KICS_CAPITAL_BUFFER | 82.4 | 85.0 | Stage3-Yellow | Stage3-Yellow | - |
| C22_003690_20240701_KOREAN_RE_REINSURANCE_HARD_MARKET | 80.1 | 83.2 | Stage3-Yellow | Stage3-Yellow | - |
| C22_088350_20241113_HANWHA_LIFE_CSM_APE_DELAYED_UNLOCK | 74.0 | 77.8 | Stage2-Actionable | Stage3-Yellow_after_CSM_bridge | reserve/capital-return bridge or high-MAE cap |
| C22_005830_20240516_DB_INSURANCE_CAPITAL_RETURN_LOW_MFE_HIGH_MAE | 77.3 | 70.2 | Stage3-Yellow_false_positive | Stage2-Actionable_with_4B_watch | reserve/capital-return bridge or high-MAE cap |
| C22_001450_20241015_HYUNDAI_MARINE_FVPL_INVESTMENT_LOSS_GUARD | 67.5 | 55.1 | Stage2_false_positive_risk | Stage4B | reserve/capital-return bridge or high-MAE cap |
| C22_000370_20241112_HANWHA_GENERAL_PROFIT_UP_EXPERIENCE_VARIANCE | 72.2 | 75.5 | Stage2-Actionable | Stage2-Actionable_with_high_MAE_guard | reserve/capital-return bridge or high-MAE cap |

The current profile can recognize the strongest positives, but it still tends to treat shareholder-return / insurance value-up evidence too generously when reserve quality or investment-loss risk is unresolved. The proposed C22 shadow gate is therefore not a broad negative weight; it is a **bridge requirement**.

## 7. Proposed shadow rule

```text
C22_INSURANCE_RATE_CYCLE_RESERVE_REQUIRES_CSM_KICS_RESERVE_QUALITY_AND_CAPITAL_RETURN_EXECUTION_GATE_WITH_HIGH_MAE_4B_CAP
```

Implementation intent for later batch work:

```yaml
rule_scope: C22_INSURANCE_RATE_CYCLE_RESERVE
positive_gate:
  require_any_two:
    - CSM_or_new_contract_profitability_growth
    - KICS_or_excess_capital_buffer
    - reserve_quality_or_experience_variance_stability
    - rate_cycle_or_underwriting_margin_confirmation
    - executed_or_highly_credible_capital_return_policy
stage3_yellow_gate:
  require:
    - positive_gate_passed
    - MAE90_not_worse_than_minus_15pct_or_explicit_high_MAE_buffer
stage3_green_gate:
  require:
    - stage3_yellow_gate_passed
    - executed_capital_return_or_sustained_CSM_margin_bridge
    - investment_loss_FVPL_or_reserve_trust_risk_absent
4b_overlay:
  trigger_if_any:
    - MAE90_pct <= -15 and non_price_bridge_incomplete
    - MAE180_pct <= -20 and peak_drawdown_after_positive_MFE > 25
    - investment_loss_or_FVPL_risk_visible
    - experience_variance_or_loss_ratio_pressure_visible
hard_4c:
  do_not_route_by_price_alone: true
```

## 8. Machine-readable rows

```jsonl
{"row_type": "trigger", "case_id": "C22_000810_20240514_SAMSUNG_FIRE_KICS_CAPITAL_BUFFER", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_PNC_EXCESS_CAPITAL_KICS_SHAREHOLDER_RETURN", "symbol": "000810", "company_name": "삼성화재", "trigger_date": "2024-05-14", "entry_date": "2024-05-14", "entry_price": 336500.0, "trigger_type": "Stage3-Yellow", "case_role": "positive_structural_success", "evidence_summary": "1Q24 이후 높은 K-ICS와 excess capital이 확인된 손해보험 capital-buffer positive. Stage3-Yellow는 허용하되, peak 이후 drawdown 때문에 Green은 capital return 실행 확인 전까지 보류.", "evidence_url": "https://www.bondweb.co.kr/_research/downloadPage.asp?gn=1&number=772115", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 12.9272, "MAE_30D_pct": -3.7147, "MFE_90D_pct": 16.9391, "MAE_90D_pct": -3.7147, "MFE_180D_pct": 29.2719, "MAE_180D_pct": -3.7147, "peak_date_180D": "2024-12-03", "peak_price_180D": 435000.0, "drawdown_after_peak_180D_pct": -21.8391, "window_end_180D": "2025-02-11", "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_usable_reason": "complete 30D/90D/180D MFE/MAE, clean 180D corporate-action window, stock-web forward window available", "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "current_profile_error": false, "local_4b_watch": true, "hard_4c_candidate": false, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "duplicate_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|000810|Stage3-Yellow|2024-05-14"}
{"row_type": "trigger", "case_id": "C22_003690_20240701_KOREAN_RE_REINSURANCE_HARD_MARKET", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_REINSURANCE_RATE_CYCLE_MARKET_SHARE", "symbol": "003690", "company_name": "코리안리", "trigger_date": "2024-07-01", "entry_date": "2024-07-01", "entry_price": 7920.0, "trigger_type": "Stage3-Yellow", "case_role": "positive_structural_success", "evidence_summary": "국내 재보험 선도 지위와 hard-market/rate-cycle 지속성이 함께 붙은 C22 positive. 단순 금융주 beta가 아니라 재보험 rate cycle과 underwriting quality가 같이 확인된 케이스.", "evidence_url": "https://m.kisrating.com/fileDown.do?fileName=rs20240701-25.pdf&gubun=2&menuCd=R8", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 7.3232, "MAE_30D_pct": -1.5152, "MFE_90D_pct": 20.5808, "MAE_90D_pct": -1.5152, "MFE_180D_pct": 20.5808, "MAE_180D_pct": -2.7778, "peak_date_180D": "2024-11-05", "peak_price_180D": 9550.0, "drawdown_after_peak_180D_pct": -19.3717, "window_end_180D": "2025-03-28", "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_usable_reason": "complete 30D/90D/180D MFE/MAE, clean 180D corporate-action window, stock-web forward window available", "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "current_profile_error": false, "local_4b_watch": false, "hard_4c_candidate": false, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "duplicate_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|003690|Stage3-Yellow|2024-07-01"}
{"row_type": "trigger", "case_id": "C22_088350_20241113_HANWHA_LIFE_CSM_APE_DELAYED_UNLOCK", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_LIFE_CSM_APE_NEW_CONTRACT_PROFITABILITY", "symbol": "088350", "company_name": "한화생명", "trigger_date": "2024-11-13", "entry_date": "2024-11-13", "entry_price": 2750.0, "trigger_type": "Stage2-Actionable", "case_role": "positive_with_high_mae_delayed_unlock", "evidence_summary": "3Q24 신계약 APE와 CSM 증가가 확인됐지만 보험손익/단기 변동성 때문에 즉시 Stage3-Green은 과하다. 이후 180D MFE가 크게 열려 C22에서 delayed positive를 막지 않는 buffer가 필요했다.", "evidence_url": "https://www.newswire.co.kr/newsRead.php?no=1000693", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 2.5455, "MAE_30D_pct": -11.2727, "MFE_90D_pct": 3.4545, "MAE_90D_pct": -11.6364, "MFE_180D_pct": 58.3636, "MAE_180D_pct": -13.8182, "peak_date_180D": "2025-07-14", "peak_price_180D": 4355.0, "drawdown_after_peak_180D_pct": -24.4546, "window_end_180D": "2025-08-08", "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_usable_reason": "complete 30D/90D/180D MFE/MAE, clean 180D corporate-action window, stock-web forward window available", "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "current_profile_error": true, "local_4b_watch": true, "hard_4c_candidate": false, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "duplicate_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|088350|Stage2-Actionable|2024-11-13"}
{"row_type": "trigger", "case_id": "C22_005830_20240516_DB_INSURANCE_CAPITAL_RETURN_LOW_MFE_HIGH_MAE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_PNC_SHAREHOLDER_RETURN_KICS_BUT_RESERVE_MARGIN_GAP", "symbol": "005830", "company_name": "DB손해보험", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 111500.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_capital_return_without_reserve_margin_confirmation", "evidence_summary": "배당/자사주/중장기 주주환원 정책은 Stage2 근거가 되지만, 보험손익·reserve quality·CSM/손해율 bridge가 약하면 90~180D MAE가 커졌다. Stage3 승격 전 reserve/margin 확인 gate 필요.", "evidence_url": "https://www.idbins.com/pcweb/bizxpress/cmy/inv/ir/__etc/2024.1Q_IR%20Reprot_Eng.pdf", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 2.4215, "MAE_30D_pct": -12.8251, "MFE_90D_pct": 11.2108, "MAE_90D_pct": -15.6054, "MFE_180D_pct": 11.2108, "MAE_180D_pct": -19.0135, "peak_date_180D": "2024-08-22", "peak_price_180D": 124000.0, "drawdown_after_peak_180D_pct": -27.1774, "window_end_180D": "2025-02-12", "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_usable_reason": "complete 30D/90D/180D MFE/MAE, clean 180D corporate-action window, stock-web forward window available", "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "current_profile_error": true, "local_4b_watch": true, "hard_4c_candidate": false, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "duplicate_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage2-Actionable|2024-05-16"}
{"row_type": "trigger", "case_id": "C22_001450_20241015_HYUNDAI_MARINE_FVPL_INVESTMENT_LOSS_GUARD", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_PNC_RESERVE_INVESTMENT_LOSS_ACCOUNTING_TRUST", "symbol": "001450", "company_name": "현대해상", "trigger_date": "2024-10-15", "entry_date": "2024-10-15", "entry_price": 31900.0, "trigger_type": "Stage4B", "case_role": "counterexample_investment_loss_reserve_trust_guard", "evidence_summary": "FVPL·해외 대체투자 등 투자손익 리스크가 드러난 상태에서는 밸류업/보험업 beta로 Stage2/3를 열면 안 된다. 180D MAE가 -37.8%까지 내려가 C22 4B/accounting-trust guard가 필요했다.", "evidence_url": "https://m.kisrating.com/fileDown.do?fileName=rs20241015-27.pdf&gubun=2&menuCd=R8", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 0.3135, "MAE_30D_pct": -14.5768, "MFE_90D_pct": 0.3135, "MAE_90D_pct": -25.8621, "MFE_180D_pct": 0.3135, "MAE_180D_pct": -37.8056, "peak_date_180D": "2024-10-15", "peak_price_180D": 32000.0, "drawdown_after_peak_180D_pct": -38.0, "window_end_180D": "2025-07-10", "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_usable_reason": "complete 30D/90D/180D MFE/MAE, clean 180D corporate-action window, stock-web forward window available", "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "current_profile_error": true, "local_4b_watch": true, "hard_4c_candidate": false, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "duplicate_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|001450|Stage4B|2024-10-15"}
{"row_type": "trigger", "case_id": "C22_000370_20241112_HANWHA_GENERAL_PROFIT_UP_EXPERIENCE_VARIANCE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_PNC_PROFIT_IMPROVEMENT_EXPERIENCE_VARIANCE_AUTO_LOSS", "symbol": "000370", "company_name": "한화손해보험", "trigger_date": "2024-11-12", "entry_date": "2024-11-12", "entry_price": 4550.0, "trigger_type": "Stage2-Actionable", "case_role": "high_mfe_high_mae_success_with_4b_watch", "evidence_summary": "3Q24 이익 개선과 장기보험 개선은 positive지만, experience variance·자동차/일반보험 손실이 같이 있어 entry MAE가 컸다. thesis를 폐기하지 말고 Stage2-Actionable + local 4B watch로 눌러야 했던 케이스.", "evidence_url": "https://bbn.kiwoom.com/rfCR11075", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 5.3846, "MAE_30D_pct": -13.0769, "MFE_90D_pct": 5.3846, "MAE_90D_pct": -15.9341, "MFE_180D_pct": 79.1209, "MAE_180D_pct": -20.0, "peak_date_180D": "2025-07-14", "peak_price_180D": 8150.0, "drawdown_after_peak_180D_pct": -31.1656, "window_end_180D": "2025-08-07", "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_usable_reason": "complete 30D/90D/180D MFE/MAE, clean 180D corporate-action window, stock-web forward window available", "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "current_profile_error": true, "local_4b_watch": true, "hard_4c_candidate": false, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "duplicate_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|000370|Stage2-Actionable|2024-11-12"}
{"row_type": "score_simulation", "case_id": "C22_000810_20240514_SAMSUNG_FIRE_KICS_CAPITAL_BUFFER", "symbol": "000810", "company_name": "삼성화재", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 66, "earnings_visibility": 83, "bottleneck_pricing": 51, "market_mispricing": 63, "valuation_rerating": 72, "capital_allocation": 90, "information_confidence": 86}, "simulated_current_score": 82.4, "simulated_shadow_score": 85.0, "expected_stage_current_profile": "Stage3-Yellow", "expected_stage_shadow_rule": "Stage3-Yellow", "residual_error_label": "none"}
{"row_type": "score_simulation", "case_id": "C22_003690_20240701_KOREAN_RE_REINSURANCE_HARD_MARKET", "symbol": "003690", "company_name": "코리안리", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 62, "earnings_visibility": 80, "bottleneck_pricing": 65, "market_mispricing": 65, "valuation_rerating": 68, "capital_allocation": 72, "information_confidence": 82}, "simulated_current_score": 80.1, "simulated_shadow_score": 83.2, "expected_stage_current_profile": "Stage3-Yellow", "expected_stage_shadow_rule": "Stage3-Yellow", "residual_error_label": "none"}
{"row_type": "score_simulation", "case_id": "C22_088350_20241113_HANWHA_LIFE_CSM_APE_DELAYED_UNLOCK", "symbol": "088350", "company_name": "한화생명", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 58, "earnings_visibility": 72, "bottleneck_pricing": 42, "market_mispricing": 72, "valuation_rerating": 76, "capital_allocation": 61, "information_confidence": 76}, "simulated_current_score": 74.0, "simulated_shadow_score": 77.8, "expected_stage_current_profile": "Stage2-Actionable", "expected_stage_shadow_rule": "Stage3-Yellow_after_CSM_bridge", "residual_error_label": "C22_rate_cycle_reserve_bridge_or_high_MAE_guardrail_error"}
{"row_type": "score_simulation", "case_id": "C22_005830_20240516_DB_INSURANCE_CAPITAL_RETURN_LOW_MFE_HIGH_MAE", "symbol": "005830", "company_name": "DB손해보험", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 53, "earnings_visibility": 63, "bottleneck_pricing": 38, "market_mispricing": 65, "valuation_rerating": 70, "capital_allocation": 86, "information_confidence": 78}, "simulated_current_score": 77.3, "simulated_shadow_score": 70.2, "expected_stage_current_profile": "Stage3-Yellow_false_positive", "expected_stage_shadow_rule": "Stage2-Actionable_with_4B_watch", "residual_error_label": "C22_rate_cycle_reserve_bridge_or_high_MAE_guardrail_error"}
{"row_type": "score_simulation", "case_id": "C22_001450_20241015_HYUNDAI_MARINE_FVPL_INVESTMENT_LOSS_GUARD", "symbol": "001450", "company_name": "현대해상", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 41, "earnings_visibility": 44, "bottleneck_pricing": 35, "market_mispricing": 58, "valuation_rerating": 56, "capital_allocation": 50, "information_confidence": 60}, "simulated_current_score": 67.5, "simulated_shadow_score": 55.1, "expected_stage_current_profile": "Stage2_false_positive_risk", "expected_stage_shadow_rule": "Stage4B", "residual_error_label": "C22_rate_cycle_reserve_bridge_or_high_MAE_guardrail_error"}
{"row_type": "score_simulation", "case_id": "C22_000370_20241112_HANWHA_GENERAL_PROFIT_UP_EXPERIENCE_VARIANCE", "symbol": "000370", "company_name": "한화손해보험", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 60, "earnings_visibility": 64, "bottleneck_pricing": 39, "market_mispricing": 78, "valuation_rerating": 78, "capital_allocation": 54, "information_confidence": 70}, "simulated_current_score": 72.2, "simulated_shadow_score": 75.5, "expected_stage_current_profile": "Stage2-Actionable", "expected_stage_shadow_rule": "Stage2-Actionable_with_high_MAE_guard", "residual_error_label": "C22_rate_cycle_reserve_bridge_or_high_MAE_guardrail_error"}
{"row_type": "aggregate", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_C22_ifrs17_csm_kics_rate_cycle_reserve_quality_holdout", "trigger_row_count": 6, "calibration_usable_rows": 6, "representative_rows": 6, "positive_case_count": 3, "counterexample_count": 3, "local_4b_watch_count": 5, "hard_4c_count": 0, "current_profile_error_count": 4, "avg_MFE_30D_pct": 5.1526, "avg_MAE_30D_pct": -9.4969, "avg_MFE_90D_pct": 9.6472, "avg_MAE_90D_pct": -12.378, "avg_MFE_180D_pct": 33.1436, "avg_MAE_180D_pct": -16.1883, "rows_with_MAE90_below_minus_15pct": 3, "rows_with_MAE180_below_minus_20pct": 2, "shadow_rule_candidate": "C22_INSURANCE_RATE_CYCLE_RESERVE_REQUIRES_CSM_KICS_RESERVE_QUALITY_AND_CAPITAL_RETURN_EXECUTION_GATE_WITH_HIGH_MAE_4B_CAP"}
{"row_type": "shadow_weight", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "rule_candidate": "C22_INSURANCE_RATE_CYCLE_RESERVE_REQUIRES_CSM_KICS_RESERVE_QUALITY_AND_CAPITAL_RETURN_EXECUTION_GATE_WITH_HIGH_MAE_4B_CAP", "do_not_apply_now": true, "proposed_effect": {"increase": ["earnings_visibility", "capital_allocation", "information_confidence"], "decrease_or_cap": ["market_mispricing_when_reserve_quality_missing", "valuation_rerating_when_MAE90_below_-15pct"], "guardrail": "If CSM/K-ICS/capital-return evidence is present but reserve quality, investment-loss, or experience-variance bridge is weak, cap Stage at Stage2-Actionable or local 4B watch."}, "supporting_case_ids": ["C22_000810_20240514_SAMSUNG_FIRE_KICS_CAPITAL_BUFFER", "C22_003690_20240701_KOREAN_RE_REINSURANCE_HARD_MARKET", "C22_088350_20241113_HANWHA_LIFE_CSM_APE_DELAYED_UNLOCK", "C22_005830_20240516_DB_INSURANCE_CAPITAL_RETURN_LOW_MFE_HIGH_MAE", "C22_001450_20241015_HYUNDAI_MARINE_FVPL_INVESTMENT_LOSS_GUARD", "C22_000370_20241112_HANWHA_GENERAL_PROFIT_UP_EXPERIENCE_VARIANCE"]}
{"row_type": "residual_contribution", "contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "C22_insurance_rate_cycle_reserve_quality_gate", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": [], "residual_error_found": true, "coding_agent_should_batch_ingest_later": true, "production_scoring_changed_now": false}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for Songdaiki/stock_agent. Do not treat this file as an immediate production patch. Batch-ingest it together with the other V12 research MD files. Validate each trigger row against the stock-web tradable shard and symbol profile. If all rows pass schema validation, add the C22 shadow rule candidate to the review set:

C22_INSURANCE_RATE_CYCLE_RESERVE_REQUIRES_CSM_KICS_RESERVE_QUALITY_AND_CAPITAL_RETURN_EXECUTION_GATE_WITH_HIGH_MAE_4B_CAP

Do not apply a global financial-sector penalty. The intended patch is canonical-archetype-specific: it strengthens Stage2 bridge requirements and local 4B watch behavior for insurance rate-cycle/reserve cases. It should preserve clean C22 positives such as strong capital-buffer and reinsurance-rate-cycle rows, while capping capital-return-only or investment-loss-contaminated rows.
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

## 11. Research state footer

```yaml
completed_round: R6
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout; C22 rows=60
next_recommended_archetypes:
  - C22_INSURANCE_RATE_CYCLE_RESERVE_holdout_only_if_new_reserve_or_rate_cycle_path
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_quality_holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
