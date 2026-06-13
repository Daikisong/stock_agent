# E2R Stock-Web v12 Residual Research — R6 / C22_INSURANCE_RATE_CYCLE_RESERVE / loop 188

```text
completed_round = R6
completed_loop = 188
selected_round = R6
selected_loop = 188
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Run contract

This standalone Markdown follows the v12 execution contract:

- It uses `Songdaiki/stock-web` actual 1D OHLCV rows only.
- It does not patch `stock_agent` code.
- It does not create a live/current watchlist.
- It does not change production scoring.
- It emits complete 30D/90D/180D MFE/MAE for every usable trigger row.
- It uses the No-Repeat Index only as a duplicate-prevention and coverage-gap ledger.

Primary execution prompt: `https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
No-repeat ledger: `https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md`
Price manifest: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json`

## 1. Selection rationale

The original No-Repeat Index has C22 above the 50-row minimum, but it remains a thin Priority 2 quality-repair bucket versus the very large R13 and L10 pools. The prior C22 loop focused on the large insurer core: Samsung Fire, DB Insurance, Hyundai Marine, Samsung Life, Hanwha Life, Korean Re, and Meritz Financial. This second C22 pass deliberately shifts to smaller and mid-cap insurers where CSM, K-ICS, investment-profit volatility, rating warnings, and valuation-reset effects can pull in opposite directions.

The residual question is narrow: **when does CSM or APE growth deserve Stage2-Actionable, and when is it just a shiny number sitting on top of weak reserve quality, K-ICS pressure, or investment P/L volatility?** The second half of the question is the mirror image: after a stock has already been heavily reset, when should an ugly reserve/K-ICS/rating event be treated as `4C-Watch` rather than hard 4C?

```text
index_baseline_coverage_before: C22 rows 60
index_baseline_coverage_after_if_accepted: C22 rows 69
session_aware_after_loop162_loop188_if_accepted: about C22 rows 77
new_independent_case_count: 9
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 9
calibration_usable_trigger_count: 9
representative_trigger_count: 9
positive_case_count: 5
counterexample_count: 4
stage4b_watch_or_overlay_count: 5
stage4c_or_false4c_audit_count: 2
current_profile_error_count: 7
```

## 2. Price source verification

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_rule = next_tradable_day_on_or_after_trigger_date
entry_price_field = c
MFE_window = rows after entry_date, not including entry row
MAE_window = rows after entry_date, not including entry row
```

All selected trigger rows have at least 180 forward tradable rows by manifest/profile max date. Profile checks showed no corporate-action candidate inside any entry-to-D180 window used here. The relevant old candidate dates were: `000370` last 2017-11-23, `000400` last 2019-10-25, `000540` last 2011-06-20, `082640` 2017-04-11, and `085620` 2018-03-23.

## 3. Evidence map

| ticker | company | evidence date | evidence family | source URL | use in C22 |
|---:|---|---:|---|---|---|
| 000370 | 한화손해보험 | 2024-04-23 | `shareholder_return_policy_CSM_growth_KICS_repair` | https://ssl.pstatic.net/imgstock/upload/research/company/1713834496047.pdf | positive_with_4B_watch |
| 000370 | 한화손해보험 | 2025-02-24 | `FY2024_record_profit_CSM_KICS_subordinated_capital_repair` | https://v.daum.net/v/bfN08CSgp3 | positive |
| 000400 | 롯데손해보험 | 2024-05-16 | `1Q24_insurance_profit_growth_but_investment_loss_asset_quality_drag` | https://www.yna.co.kr/view/AKR20240516147400002 | counterexample_high_MAE |
| 000400 | 롯데손해보험 | 2025-05-23 | `credit_negative_low_ROA_exception_model_but_price_already_reset` | https://m.kisrating.com/fileDown.do?fileName=rs20250523-13.pdf&gubun=2&menuCd=R8 | positive_false_4C_audit |
| 000540 | 흥국화재 | 2024-05-16 | `1Q24_profit_despite_investment_loss_and_nonrecurring_mix` | https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20240516002335&docno=&method=searchInitInfo | counterexample_high_MAE |
| 000540 | 흥국화재 | 2025-03-07 | `2024_3Q_credit_profile_long_term_protection_CSM_quality_low_starting_valuation` | https://m.kisrating.com/fileDown.do?fileName=rs20250307-22.pdf&gubun=2&menuCd=R8 | positive_reset |
| 082640 | 동양생명 | 2024-11-13 | `3Q24_profit_surprise_health_CSM_growth_but_accounting_guideline_risk` | https://www.yna.co.kr/view/AKR20241113077600002 | positive_with_high_MAE_guard |
| 082640 | 동양생명 | 2025-05-19 | `1Q25_profit_drop_KICS_below_150_but_capital_repair_and_group_support_offset` | https://www.yna.co.kr/view/AKR20250519136800002 | positive_false_4C_audit |
| 085620 | 미래에셋생명 | 2024-05-23 | `1Q24_profit_drop_IBNR_reserve_hit_CSM_vocabulary_only` | https://www.thebell.co.kr/front/newsview.asp?key=202405231532440400104859 | counterexample |

## 4. Trigger-level backtest summary

| case | ticker | trigger | entry | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | label |
|---|---:|---|---:|---:|---:|---:|---|
| 한화손해보험 | 000370 | Stage2-Actionable | 2024-04-23 @ 4,795 | 12.41 / -2.4 | 29.93 / -5.01 | 29.93 / -17.52 | positive_with_4B_watch |
| 한화손해보험 | 000370 | Stage2-Actionable | 2025-02-24 @ 4,100 | 6.46 / -8.66 | 47.56 / -11.22 | 98.78 / -11.22 | positive |
| 롯데손해보험 | 000400 | Stage2-FalsePositive | 2024-05-16 @ 3,530 | 15.86 / -17.85 | 15.86 / -32.01 | 15.86 / -50.88 | counterexample_high_MAE |
| 롯데손해보험 | 000400 | Stage4C-FalseBreak-Audit | 2025-05-23 @ 1,580 | 37.34 / -2.03 | 43.04 / -2.03 | 43.04 / -2.03 | positive_false_4C_audit |
| 흥국화재 | 000540 | Stage2-FalsePositive | 2024-05-16 @ 4,530 | -2.21 / -16.11 | 7.84 / -22.52 | 7.84 / -35.43 | counterexample_high_MAE |
| 흥국화재 | 000540 | Stage2-Actionable | 2025-03-07 @ 3,310 | 19.34 / -9.97 | 83.38 / -9.97 | 83.38 / -9.97 | positive_reset |
| 동양생명 | 082640 | Stage2-Actionable-HighMAEGuard | 2024-11-13 @ 5,570 | 9.34 / -20.47 | 9.34 / -21.45 | 59.61 / -21.45 | positive_with_high_MAE_guard |
| 동양생명 | 082640 | Stage4C-FalseBreak-Audit | 2025-05-19 @ 5,470 | 31.81 / -1.28 | 62.52 / -1.28 | 62.52 / -1.28 | positive_false_4C_audit |
| 미래에셋생명 | 085620 | Stage2-FalsePositive | 2024-05-23 @ 5,330 | 15.2 / -13.7 | 15.2 / -13.7 | 15.2 / -20.26 | counterexample |

## 5. Case notes

### 5.1 Hanwha General Insurance — shareholder-return policy plus CSM quality worked, but still needs reserve confirmation

The April 2024 trigger had a concrete shareholder-return policy and CSM-growth language. The price path was constructive: D90 MFE reached 29.93% while D90 MAE stayed at -5.01%. Yet D180 MAE eventually deepened to -17.52%, so this is a clean Stage2-Actionable or Yellow candidate, not automatic Green. C22 should recognize the combination of dividend policy and CSM growth, while still asking for reserve/loss-ratio quality.

### 5.2 Hanwha General Insurance FY2024 — capital repair plus record profit was the cleanest small-insurer positive

The February 2025 row had record profit, CSM growth, and subordinated-capital/K-ICS repair context. D180 MFE reached 98.78% against only -11.22% MAE. This is the main positive row for the second C22 pass. The mechanism is simple: CSM is the reservoir, K-ICS is the dam wall, and capital repair raised the wall just as the reservoir filled.

### 5.3 Lotte Non-Life 1Q24 — insurance profit growth was not enough because investment quality was the leak

Lotte's 1Q24 insurance operating profit and CSM looked good, but investment profit collapsed and asset-quality concerns sat behind the headline. The price path punished that weakness: D180 MFE was only 15.86% while D180 MAE reached -50.88%. This is a Stage2 false-positive blocker for any row that treats long-term insurance growth as clean without investment/asset-quality checks.

### 5.4 Lotte Non-Life credit warning — after a deep reset, ugly credit language was not an automatic hard 4C

The May 2025 credit report was negative: low ROA, high volatility, and model-risk concerns. But by then the stock had already been compressed. The 180D path produced +43.04% MFE with only -2.03% MAE. This is not a bullish proof of quality; it is a hard-4C timing warning. After valuation reset, rating-risk evidence should become `4C-Watch` unless a second confirming break follows.

### 5.5 Heungkuk Fire 1Q24 — headline profit masked investment loss and drawdown risk

Heungkuk's 1Q24 row had net profit and K-ICS stability, but investment loss and business-quality ambiguity were visible. The price path was bad: 90D MAE -22.52%, 180D MAE -35.43%, and only 7.84% MFE. This blocks Stage2-Actionable when the headline profit is driven by mixed or unstable sources.

### 5.6 Heungkuk Fire 2025 credit profile — prior investment-loss memory should not permanently block reset positives

By March 2025, the rating material showed long-term protection insurance concentration, CSM quality, and reasonable insurance profitability. Starting valuation was much lower. The stock then produced 83.38% MFE at 90D and 180D with a -9.97% MAE floor. This shows that C22 should not permanently blacklist a small insurer after one bad investment-loss row. Reset entry plus insurance-quality evidence can rehabilitate Stage2.

### 5.7 Tongyang Life 3Q24 — earnings surprise worked eventually, but the path demanded staged entry

Tongyang Life's 3Q24 cumulative profit and CSM figures were strong, but accounting guideline risk was already present. The path confirms both sides: D180 MFE reached 59.61%, but D90 MAE hit -21.45%. This is the exact kind of row where the stage should be `Stage2-Actionable-HighMAEGuard`, not immediate clean Green.

### 5.8 Tongyang Life 1Q25 — weak profit and K-ICS below 150% were not hard 4C after capital repair offset

The May 2025 row looked ugly: profit fell and K-ICS dropped below the supervisory comfort line. However, the evidence also included subordinated-debt capital repair and ALM improvement plans. The price path was very strong with 62.52% D180 MFE and only -1.28% MAE. This is a false-hard-4C audit row: capital repair and group-support offset can convert a negative headline into reset entry.

### 5.9 Mirae Asset Life 1Q24 — CSM vocabulary could not offset simultaneous insurance and investment profit decline

Mirae Asset Life had a reasonable CSM story, but 1Q24 net profit, insurance profit, and investment profit all weakened, with IBNR/reserve pressure in the background. D180 MFE was only 15.20% and D180 MAE reached -20.26%. This is a CSM-vocabulary false-positive row.

## 6. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_000370_20240423", "ticker": "000370", "company_name": "Hanwha General Insurance", "market_country": "KR", "trigger_date": "2024-04-23", "entry_date": "2024-04-23", "entry_price": 4795.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Actionable", "evidence_family": "shareholder_return_policy_CSM_growth_KICS_repair", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1713834496047.pdf", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 12.41, "MAE_30D_pct": -2.4, "MFE_90D_pct": 29.93, "MAE_90D_pct": -5.01, "MFE_180D_pct": 29.93, "MAE_180D_pct": -17.52, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive_with_4B_watch", "expected_stage_path": "Stage2-Actionable -> Yellow candidate with reserve/K-ICS confirmation; no Green without repeat quality", "current_profile_error": "could_underweight_DPS_policy_plus_CSM_growth_when_treated_as_generic_small_insurer", "component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 7, "bottleneck_pricing_power": 3, "market_mispricing": 6, "valuation_rerating": 7, "capital_allocation": 8, "information_confidence": 8, "total_raw_score": 75}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_000370_20250224", "ticker": "000370", "company_name": "Hanwha General Insurance", "market_country": "KR", "trigger_date": "2025-02-24", "entry_date": "2025-02-24", "entry_price": 4100.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Actionable", "evidence_family": "FY2024_record_profit_CSM_KICS_subordinated_capital_repair", "source_url": "https://v.daum.net/v/bfN08CSgp3", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 6.46, "MAE_30D_pct": -8.66, "MFE_90D_pct": 47.56, "MAE_90D_pct": -11.22, "MFE_180D_pct": 98.78, "MAE_180D_pct": -11.22, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive", "expected_stage_path": "Stage2-Actionable -> Yellow; strongest row after K-ICS/capital and CSM bridge align", "current_profile_error": "too_conservative_if_KICS_repair_and_CSM_growth_are_not_combined", "component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 8, "bottleneck_pricing_power": 3, "market_mispricing": 7, "valuation_rerating": 8, "capital_allocation": 8, "information_confidence": 8, "total_raw_score": 80}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_000400_20240516", "ticker": "000400", "company_name": "Lotte Non-Life Insurance", "market_country": "KR", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 3530.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-FalsePositive", "evidence_family": "1Q24_insurance_profit_growth_but_investment_loss_asset_quality_drag", "source_url": "https://www.yna.co.kr/view/AKR20240516147400002", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 15.86, "MAE_30D_pct": -17.85, "MFE_90D_pct": 15.86, "MAE_90D_pct": -32.01, "MFE_180D_pct": 15.86, "MAE_180D_pct": -50.88, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "counterexample_high_MAE", "expected_stage_path": "Stage2-Watch only; investment/asset-quality drag blocks Actionable", "current_profile_error": "false_positive_if_CSM_and_long_term_insurance_growth_ignore_investment_volatility", "component_score_breakdown": {"eps_fcf_explosion": 4, "earnings_visibility": 5, "bottleneck_pricing_power": 2, "market_mispricing": 5, "valuation_rerating": 5, "capital_allocation": 4, "information_confidence": 8, "total_raw_score": 55}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_000400_20250523", "ticker": "000400", "company_name": "Lotte Non-Life Insurance", "market_country": "KR", "trigger_date": "2025-05-23", "entry_date": "2025-05-23", "entry_price": 1580.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage4C-FalseBreak-Audit", "evidence_family": "credit_negative_low_ROA_exception_model_but_price_already_reset", "source_url": "https://m.kisrating.com/fileDown.do?fileName=rs20250523-13.pdf&gubun=2&menuCd=R8", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 37.34, "MAE_30D_pct": -2.03, "MFE_90D_pct": 43.04, "MAE_90D_pct": -2.03, "MFE_180D_pct": 43.04, "MAE_180D_pct": -2.03, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive_false_4C_audit", "expected_stage_path": "4C-Watch not hard 4C after valuation reset; require second confirmation", "current_profile_error": "hard_4c_too_early_if_rating_warning_is_applied_after_price_reset_without_forward_validation", "component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 4, "bottleneck_pricing_power": 2, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 3, "information_confidence": 8, "total_raw_score": 60}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_000540_20240516", "ticker": "000540", "company_name": "Heungkuk Fire & Marine Insurance", "market_country": "KR", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 4530.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-FalsePositive", "evidence_family": "1Q24_profit_despite_investment_loss_and_nonrecurring_mix", "source_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20240516002335&docno=&method=searchInitInfo", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": -2.21, "MAE_30D_pct": -16.11, "MFE_90D_pct": 7.84, "MAE_90D_pct": -22.52, "MFE_180D_pct": 7.84, "MAE_180D_pct": -35.43, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "counterexample_high_MAE", "expected_stage_path": "Stage2-Watch; insurance profit and K-ICS not enough when investment loss/quality unclear", "current_profile_error": "false_positive_if_headline_net_profit_ignores_investment_loss_and_insurance_quality_decay", "component_score_breakdown": {"eps_fcf_explosion": 4, "earnings_visibility": 4, "bottleneck_pricing_power": 2, "market_mispricing": 5, "valuation_rerating": 5, "capital_allocation": 4, "information_confidence": 7, "total_raw_score": 51}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_000540_20250307", "ticker": "000540", "company_name": "Heungkuk Fire & Marine Insurance", "market_country": "KR", "trigger_date": "2025-03-07", "entry_date": "2025-03-07", "entry_price": 3310.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Actionable", "evidence_family": "2024_3Q_credit_profile_long_term_protection_CSM_quality_low_starting_valuation", "source_url": "https://m.kisrating.com/fileDown.do?fileName=rs20250307-22.pdf&gubun=2&menuCd=R8", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 19.34, "MAE_30D_pct": -9.97, "MFE_90D_pct": 83.38, "MAE_90D_pct": -9.97, "MFE_180D_pct": 83.38, "MAE_180D_pct": -9.97, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive_reset", "expected_stage_path": "Stage2-Watch -> Actionable if insurance profitability and CSM quality persist", "current_profile_error": "too_late_if_small_insurer_CSM_quality_is_blocked_by_prior_investment_loss_memory", "component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 7, "bottleneck_pricing_power": 3, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 5, "information_confidence": 8, "total_raw_score": 74}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_082640_20241113", "ticker": "082640", "company_name": "Tongyang Life Insurance", "market_country": "KR", "trigger_date": "2024-11-13", "entry_date": "2024-11-13", "entry_price": 5570.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Actionable-HighMAEGuard", "evidence_family": "3Q24_profit_surprise_health_CSM_growth_but_accounting_guideline_risk", "source_url": "https://www.yna.co.kr/view/AKR20241113077600002", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 9.34, "MAE_30D_pct": -20.47, "MFE_90D_pct": 9.34, "MAE_90D_pct": -21.45, "MFE_180D_pct": 59.61, "MAE_180D_pct": -21.45, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive_with_high_MAE_guard", "expected_stage_path": "Actionable only with staged-entry guard; high MAE before D180 MFE", "current_profile_error": "too_early_actionable_without_KICS_and_guideline_risk_buffer", "component_score_breakdown": {"eps_fcf_explosion": 7, "earnings_visibility": 7, "bottleneck_pricing_power": 3, "market_mispricing": 6, "valuation_rerating": 7, "capital_allocation": 5, "information_confidence": 8, "total_raw_score": 73}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_082640_20250519", "ticker": "082640", "company_name": "Tongyang Life Insurance", "market_country": "KR", "trigger_date": "2025-05-19", "entry_date": "2025-05-19", "entry_price": 5470.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage4C-FalseBreak-Audit", "evidence_family": "1Q25_profit_drop_KICS_below_150_but_capital_repair_and_group_support_offset", "source_url": "https://www.yna.co.kr/view/AKR20250519136800002", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 31.81, "MAE_30D_pct": -1.28, "MFE_90D_pct": 62.52, "MAE_90D_pct": -1.28, "MFE_180D_pct": 62.52, "MAE_180D_pct": -1.28, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive_false_4C_audit", "expected_stage_path": "4C-Watch -> reset/staged entry; not hard 4C after debt/group support offset", "current_profile_error": "false_4c_if_KICS_drop_is_not_cross_checked_with_capital_repair_and_price_reset", "component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 4, "bottleneck_pricing_power": 2, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 6, "information_confidence": 9, "total_raw_score": 65}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_small_mid_insurer_csm_kics_investment_volatility_leaf_set", "case_id": "C22_R6_L188_085620_20240523", "ticker": "085620", "company_name": "Mirae Asset Life Insurance", "market_country": "KR", "trigger_date": "2024-05-23", "entry_date": "2024-05-23", "entry_price": 5330.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-FalsePositive", "evidence_family": "1Q24_profit_drop_IBNR_reserve_hit_CSM_vocabulary_only", "source_url": "https://www.thebell.co.kr/front/newsview.asp?key=202405231532440400104859", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 15.2, "MAE_30D_pct": -13.7, "MFE_90D_pct": 15.2, "MAE_90D_pct": -13.7, "MFE_180D_pct": 15.2, "MAE_180D_pct": -20.26, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "counterexample", "expected_stage_path": "Stage2-Watch; CSM growth not enough while insurance/investment profit both decline", "current_profile_error": "false_positive_if_CSM_language_masks_IBNR_and_investment_profit_drop", "component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 5, "bottleneck_pricing_power": 2, "market_mispricing": 5, "valuation_rerating": 4, "capital_allocation": 4, "information_confidence": 8, "total_raw_score": 51}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
```

## 7. Aggregate / shadow-weight / residual rows JSONL

```jsonl
{"row_type": "aggregate", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "usable_trigger_row_count": 9, "representative_trigger_count": 9, "positive_case_count": 5, "counterexample_count": 4, "stage4b_watch_or_overlay_count": 5, "stage4c_or_false4c_audit_count": 2, "current_profile_error_count": 7, "avg_MFE_90D_pct": 34.96, "avg_MAE_90D_pct": -13.24, "avg_MFE_180D_pct": 46.24, "avg_MAE_180D_pct": -18.89, "shadow_rule_candidate": "C22_CSM_KICS_INVESTMENT_VOLATILITY_AND_FALSE_4C_RESET_GATE_V2", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "shadow_weight", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "rule_id": "C22_CSM_KICS_INVESTMENT_VOLATILITY_AND_FALSE_4C_RESET_GATE_V2", "scope": "C22_INSURANCE_RATE_CYCLE_RESERVE", "do_not_propose_new_weight_delta": false, "proposed_effect": "tighten Stage2-Actionable when CSM/APE vocabulary is unsupported by recurring insurance profit, reserve quality, K-ICS, or capital repair; weaken immediate hard 4C after price reset if capital repair or group-support offset is visible.", "evidence_rows": ["C22_R6_L188_000370_20240423", "C22_R6_L188_000370_20250224", "C22_R6_L188_000400_20240516", "C22_R6_L188_000400_20250523", "C22_R6_L188_000540_20240516", "C22_R6_L188_000540_20250307", "C22_R6_L188_082640_20241113", "C22_R6_L188_082640_20250519", "C22_R6_L188_085620_20240523"], "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "residual_contribution", "round_id": "R6", "loop_id": 188, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_axis_proposed": "c22_csm_kics_investment_volatility_and_false_4c_reset_gate_v2", "existing_axis_strengthened": "full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c|price_only_blowoff_blocks_positive_stage", "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_should_not_fire_after_valuation_reset_without_second_confirming_break", "next_recommended_archetypes": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM"}
```

## 8. Score-return alignment

```text
positive_or_false_4C_audit_rows = 5
counterexample_or_high_MAE_rows = 4
D180_MFE_ge_20_count = 6
D90_MAE_le_minus_20_count = 3
D180_MAE_le_minus_20_count = 4
highest_clean_positive = 000370 / Hanwha General Insurance / 2025-02-24 / MFE180 98.78 / MAE180 -11.22
highest_reset_positive = 000540 / Heungkuk Fire / 2025-03-07 / MFE180 83.38 / MAE180 -9.97
highest_false_4C_audit = 082640 / Tongyang Life / 2025-05-19 / MFE180 62.52 / MAE180 -1.28
worst_high_MAE_counterexample = 000400 / Lotte Non-Life / 2024-05-16 / MFE180 15.86 / MAE180 -50.88
```

The alignment is useful because the same vocabulary changes meaning by balance-sheet timing. CSM growth before capital repair is just a promise; CSM growth after K-ICS repair becomes a bridge. Conversely, a credit/rating warning before price reset can be a 4C candidate, but the same warning after price reset may be a false-break audit.

## 9. Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff and requires non-price evidence. The remaining C22-specific residual errors are narrower:

1. **CSM/APE vocabulary false positive** — CSM, new-contract CSM, and APE growth are not enough without recurring insurance profit and reserve/loss-ratio quality. Mirae Asset Life and Lotte 1Q24 are the main examples.
2. **Investment P/L pollution** — small insurers can look like underwriting positives while investment profit or asset-quality volatility dominates the stock path. Lotte and Heungkuk 1Q24 both show this.
3. **K-ICS/capital repair timing** — K-ICS weakness can be a real risk, but if subordinated debt, group support, or ALM repair is visible after a valuation reset, hard 4C should wait for a second break.
4. **Staged entry for high-MAE positives** — Tongyang 3Q24 had strong D180 MFE, but the D90 drawdown means clean Stage2-Actionable without staged-entry guard is too aggressive.
5. **Small-insurer rehabilitation** — a prior false positive should not permanently block a later reset positive when the evidence changes from headline profit to verified CSM quality plus capital repair.

## 10. Shadow rule candidate

```text
rule_id = C22_CSM_KICS_INVESTMENT_VOLATILITY_AND_FALSE_4C_RESET_GATE_V2
scope = C22_INSURANCE_RATE_CYCLE_RESERVE
production_scoring_changed = false
shadow_weight_only = true
```

### Proposed gate

C22 Stage2-Actionable should require at least one **insurance-profit bridge** and one **quality/risk bridge**.

Insurance-profit bridge:

- CSM balance growth with new-contract CSM or protection/health mix improvement.
- Recurring insurance service result, not just headline net profit.
- Rate-cycle or underwriting-quality evidence for non-life/reinsurance rows.

Quality/risk bridge:

- K-ICS or capital-repair visibility.
- Reserve/loss-ratio quality, including whether profit came from one-off reserve release.
- Investment P/L and asset-quality check, especially for small insurers.
- If evidence is a negative rating/K-ICS event after a deep price reset, hard 4C requires a second confirming break.

### Suggested implementation language for later coding agent

```text
if canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE:
    if csm_or_ape_vocabulary and not recurring_insurance_profit_bridge:
        cap_stage2_actionable = true
        force_stage2_watch_reason = csm_vocabulary_without_profit_bridge
    if investment_loss_or_asset_quality_drag and not capital_repair_visible:
        cap_stage2_actionable = true
        add_high_mae_guard = true
    if kics_drop_or_rating_negative and price_reset_already_deep and capital_repair_or_group_support_visible:
        downgrade_hard_4c_to_4c_watch = true
    if recurring_insurance_profit_bridge and csm_quality_bridge and kics_or_capital_repair_visible:
        allow_stage2_actionable = true
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this in the research session. Use it only in a later coding agent session.

```text
You are a coding agent operating on Songdaiki/stock_agent after the user has batch-collected v12 residual research MDs. Do not re-run live discovery. Read this MD only as a research artifact. Parse the JSONL trigger rows, aggregate row, shadow_weight row, and residual_contribution row. Validate that every usable trigger row has entry_date, entry_price, trigger_type, large_sector_id, canonical_archetype_id, and complete 30D/90D/180D MFE/MAE. If validation passes, consider adding a scoped patch candidate named C22_CSM_KICS_INVESTMENT_VOLATILITY_AND_FALSE_4C_RESET_GATE_V2. The patch must be shadow-tested first and must not loosen Stage3-Green. The intended effect is to require recurring insurance profit, reserve/loss-ratio quality, and K-ICS/capital-repair visibility before C22 Stage2-Actionable, while downgrading post-reset rating/K-ICS shocks from hard 4C to 4C-Watch unless a second confirming thesis break is present.
```

## 12. Next research state

```text
completed_round = R6
completed_loop = 188
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
