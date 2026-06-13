# E2R Stock-Web v12 Residual Research — R6 / C22_INSURANCE_RATE_CYCLE_RESERVE / loop 162

```text
completed_round = R6
completed_loop = 162
selected_round = R6
selected_loop = 162
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set
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

The original No-Repeat Index shows C22 as already above the 50-row minimum, but still one of the thinnest Priority 2 buckets: `C22_INSURANCE_RATE_CYCLE_RESERVE = 60 rows`. After this session's P0/P1 clearing and the recent Priority 2 quality-repair passes for C08, C19, C25, and C13, C22 became the next thin, not-yet-touched quality-repair target.

C22 is a useful residual bucket because insurance rerating is deceptively simple. IFRS17 created a shiny new dashboard — CSM, APE, K-ICS, loss ratio, reserve release, capital return — but the dashboard can lie when one-off reserve releases, forecast-only ROE, or late capital-return headlines are treated like recurring underwriting quality. This loop isolates that failure mode.

```text
index_baseline_coverage_before: C22 rows 60
index_baseline_coverage_after_if_accepted: C22 rows 68
new_independent_case_count: 8
reused_case_count: 0
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
positive_case_count: 4
counterexample_count: 4
4B_watch_or_overlay_count: 4
4C_watch_count: 0
current_profile_error_count: 6
```

## 2. Price source verification

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_rule = next_tradable_day_after_trigger_date
entry_price_field = c
MFE_window = rows after entry_date, not including entry row
MAE_window = rows after entry_date, not including entry row
```

All selected trigger rows have at least 180 forward tradable rows by manifest/profile max date. Corporate-action candidate windows were checked at profile level and did not contaminate the entry-to-D180 windows used here.

## 3. Evidence map

| ticker | company | evidence date | evidence family | source URL | use in C22 |
|---:|---|---:|---|---|---|
| 000810 | Samsung Fire & Marine | 2025-02-12 | FY2024 record net profit, CSM, K-ICS, loss ratio note | https://www.asiae.co.kr/en/article/2025021209541047492 | positive; CSM + profit + capital-quality bridge |
| 005830 | DB Insurance | 2024-05-16 | 1Q24 beat with onerous-contract-cost reversal | https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/05/15/DB_FM_240516_.pdf | counterexample; one-off reserve release guard |
| 001450 | Hyundai Marine | 2024-03-19 | 2024F profit and K-ICS/capital forecast | https://ssl.pstatic.net/imgstock/upload/research/company/1710804325262.pdf | counterexample; forecast-only/high-MAE guard |
| 032830 | Samsung Life | 2024-05-16 | 1Q24 health CSM / APE / ex-one-off profit growth | https://www.yna.co.kr/view/AKR20240516033251527 | positive; health CSM mix bridge |
| 088350 | Hanwha Life | 2024-05-15 | 1Q24 APE, new CSM, retention, organization growth | https://file.alphasquare.co.kr/media/pdfs/company-ir/20240515%ED%95%9C%ED%99%94%EC%83%9D%EB%AA%85_2024%EB%85%84_1%EB%B6%84%EA%B8%B0_%EA%B2%BD%EC%98%81%EC%8B%A4%EC%A0%81_%EB%B0%9C%ED%91%9C.pdf | counterexample; APE/CSM vocabulary alone failed |
| 003690 | Korean Re | 2024-05-16 | reinsurance profitability, portfolio/rate-cycle quality | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516002102&docno=&method=search&viewerhost= | positive-watch; low-MAE but MFE below Green |
| 138040 | Meritz Financial | 2024-11-14 | 3Q earnings, buyback/cancellation, subsidiary dividend bridge | https://www.asiae.co.kr/en/article/2024112109033861930 | positive boundary; C21/C22 split required |
| 032830 | Samsung Life | 2024-11-15 | 3Q cumulative profit, CSM balance, K-ICS | https://www.yna.co.kr/view/AKR20241115054400002 | counterexample; late headline/high-MAE guard |

## 4. Trigger-level backtest summary

| case | ticker | trigger | entry | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | label | profile stress |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Samsung Fire & Marine Insurance | 000810 | 2025-02-12 | 2025-02-13 @ 358,500 | 19.25% / -1.81% | 29.99% / -8.79% | 46.72% / -8.79% | positive | current_profile_too_conservative_if_CSM_and_capital_return_bridge_is_ignored |
| DB Insurance | 005830 | 2024-05-16 | 2024-05-17 @ 109,100 | 5.77% / -10.91% | 13.66% / -13.75% | 13.66% / -17.23% | counterexample | false_positive_if_one_off_reserve_release_is_treated_as_repeatable_CSM_quality |
| Hyundai Marine & Fire Insurance | 001450 | 2024-03-19 | 2024-03-20 @ 33,550 | 2.83% / -15.20% | 9.54% / -15.20% | 9.54% / -26.23% | counterexample | forecast_only_stage2_false_positive_high_MAE |
| Samsung Life Insurance | 032830 | 2024-05-16 | 2024-05-17 @ 88,900 | 5.17% / -8.89% | 15.97% / -8.89% | 24.86% / -8.89% | positive | current_profile_may_underweight_health_CSM_mix_if_treated_as_simple_life_insurer_value_up |
| Hanwha Life Insurance | 088350 | 2024-05-15 | 2024-05-16 @ 3,160 | -0.16% / -14.72% | 2.53% / -14.72% | 2.53% / -23.10% | counterexample | APE_and_new_CSM_vocabulary_false_positive_when_loss_ratio_capital_quality_unconfirmed |
| Korean Reinsurance | 003690 | 2024-05-16 | 2024-05-17 @ 7,980 | 2.76% / -4.39% | 12.78% / -4.39% | 19.67% / -4.39% | positive_watch | profile_may_miss_low_MAE_reinsurance_rate_cycle_but_MFE_below_green_threshold |
| Meritz Financial Group | 138040 | 2024-11-14 | 2024-11-15 @ 101,800 | 4.22% / -5.01% | 25.15% / -5.01% | 25.15% / -5.01% | positive_boundary_C21_C22 | boundary_positive_if_C22_insurance_profit_and_C21_capital_return_bridge_are_jointly_verified |
| Samsung Life Insurance | 032830 | 2024-11-15 | 2024-11-18 @ 108,800 | 1.47% / -16.36% | 1.47% / -26.84% | 34.93% / -32.63% | counterexample_high_MAE_then_late_MFE | too_late_green_or_actionable_entry_without_staged_entry_guard |


## 5. Case notes

### 5.1 Samsung Fire & Marine — record profit with CSM and K-ICS context

Samsung Fire's FY2024 row is the cleanest C22 positive in this pack. It had record controlling-shareholder net profit, CSM growth, a solvency context, and explicit loss-ratio notes rather than just generic insurer value-up language. The price path confirmed the bridge: 90D MFE was nearly 30% while MAE stayed below 9%. This should be allowed to move toward Stage2-Actionable or Yellow, but Green still requires reserve/loss-ratio quality to remain visible.

### 5.2 DB Insurance — one-off reserve release must not masquerade as repeatable CSM quality

DB Insurance reported a strong 1Q24 result, but the report explicitly included a large one-off onerous contract cost reversal. The stock did not collapse, but it also did not reward a Green-style interpretation: D180 MFE was only 13.66% and D180 MAE was -17.23%. For C22, this is the clean example of why reserve release and one-off accounting effects must be separated from recurring underwriting profit.

### 5.3 Hyundai Marine — forecast-only ROE and K-ICS language failed the price path

The Hyundai Marine case had forecasted profit growth, a K-ICS/capital-ratio strategy, and low valuation language. That was not enough. The price path delivered only 9.54% D180 MFE against -26.23% D180 MAE. This row blocks Stage2-Actionable when the evidence is mainly a forecast and not yet reserve/loss-ratio/capital-return execution.

### 5.4 Samsung Life Q1 — health CSM mix worked, but not as a loose life-insurer beta

The May 2024 Samsung Life trigger had health CSM mix, new-contract CSM, and APE growth. The 180D path was constructive with limited drawdown. This is not a pure value-up row; it is a C22 row because the evidence bridge runs through CSM quality and health-protection mix. It supports Stage2-Actionable but not automatic Green.

### 5.5 Hanwha Life — APE and new CSM vocabulary alone was insufficient

Hanwha Life had impressive APE, new CSM, persistency, and organization-growth language. The price path disagreed: D180 MFE was only 2.53% and MAE reached -23.10%. This is a high-value C22 counterexample. The model should not treat new CSM/APE expansion as enough when capital, loss-ratio, reserve-quality, and actual profit conversion are not visible.

### 5.6 Korean Re — low-MAE rate-cycle quality, but not enough for Green

Korean Re is a positive-watch rather than a clean Green candidate. The row had low MAE across all windows and D180 MFE approached 20%, but it did not cross the stronger positive threshold. This row argues for a reinsurance-specific subgate: portfolio quality and rate-cycle discipline can create safer entries, but Green still needs stronger earnings/revision confirmation.

### 5.7 Meritz Financial — capital-return positive, but C21/C22 boundary must be explicit

Meritz Financial performed well after the November 2024 trigger, with D90/D180 MFE above 25% and only -5.01% MAE. But this row sits on the boundary between C21 and C22. If the evidence is only buyback/cancellation, classify it as C21. It can remain in C22 only when the insurance subsidiary profit, dividend stream, solvency, and capital-return execution are all part of the bridge.

### 5.8 Samsung Life Q3 — a true thesis can still be too late

Samsung Life's November 2024 trigger had strong cumulative profit, CSM balance growth, and K-ICS context. The later 180D MFE was strong, but the route first suffered -26.84% MAE by D90 and -32.63% by D180. This is the important timing counterexample: C22 evidence can be fundamentally good and still require staged-entry/high-MAE guards when the trigger is late or crowded.

## 6. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "round_id": "R6", "loop_id": 162, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set", "case_id": "C22_R6_L162_000810_20250212", "ticker": "000810", "company_name": "Samsung Fire & Marine Insurance", "market_country": "KR", "trigger_date": "2025-02-12", "entry_date": "2025-02-13", "entry_price": 358500.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Actionable", "evidence_family": "FY2024_record_net_profit_CSM_KICS_capital_return_quality", "source_url": "https://www.asiae.co.kr/en/article/2025021209541047492", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 19.25, "MAE_30D_pct": -1.81, "MFE_90D_pct": 29.99, "MAE_90D_pct": -8.79, "MFE_180D_pct": 46.72, "MAE_180D_pct": -8.79, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive", "expected_stage_path": "Stage2-Actionable -> Stage3-Yellow candidate; Green still gated by loss-ratio/reserve quality", "current_profile_error": "current_profile_too_conservative_if_CSM_and_capital_return_bridge_is_ignored", "component_score_breakdown": {"eps_fcf_explosion": 7, "earnings_visibility": 8, "bottleneck_pricing_power": 4, "market_mispricing": 6, "valuation_rerating": 7, "capital_allocation": 8, "information_confidence": 8, "total_raw_score": 76}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 162, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set", "case_id": "C22_R6_L162_005830_20240516", "ticker": "005830", "company_name": "DB Insurance", "market_country": "KR", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 109100.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Watch", "evidence_family": "1Q24_beat_with_onerous_contract_reversal_one_off", "source_url": "https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/05/15/DB_FM_240516_.pdf", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 5.77, "MAE_30D_pct": -10.91, "MFE_90D_pct": 13.66, "MAE_90D_pct": -13.75, "MFE_180D_pct": 13.66, "MAE_180D_pct": -17.23, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "counterexample", "expected_stage_path": "Stage2-Watch; block Actionable without repeat reserve/loss-ratio bridge", "current_profile_error": "false_positive_if_one_off_reserve_release_is_treated_as_repeatable_CSM_quality", "component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 6, "bottleneck_pricing_power": 3, "market_mispricing": 5, "valuation_rerating": 5, "capital_allocation": 5, "information_confidence": 8, "total_raw_score": 63}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 162, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set", "case_id": "C22_R6_L162_001450_20240319", "ticker": "001450", "company_name": "Hyundai Marine & Fire Insurance", "market_country": "KR", "trigger_date": "2024-03-19", "entry_date": "2024-03-20", "entry_price": 33550.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-FalsePositive", "evidence_family": "2024F_profit_KICS_forecast_without_reserve_quality_confirmation", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1710804325262.pdf", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 2.83, "MAE_30D_pct": -15.2, "MFE_90D_pct": 9.54, "MAE_90D_pct": -15.2, "MFE_180D_pct": 9.54, "MAE_180D_pct": -26.23, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "counterexample", "expected_stage_path": "Stage2-Watch -> local 4B/high-MAE guard; no Green", "current_profile_error": "forecast_only_stage2_false_positive_high_MAE", "component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 5, "bottleneck_pricing_power": 3, "market_mispricing": 5, "valuation_rerating": 4, "capital_allocation": 5, "information_confidence": 7, "total_raw_score": 57}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 162, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set", "case_id": "C22_R6_L162_032830_20240516", "ticker": "032830", "company_name": "Samsung Life Insurance", "market_country": "KR", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 88900.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Actionable", "evidence_family": "1Q24_health_CSM_APE_growth_ex_oneoff_profit_growth", "source_url": "https://www.yna.co.kr/view/AKR20240516033251527", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 5.17, "MAE_30D_pct": -8.89, "MFE_90D_pct": 15.97, "MAE_90D_pct": -8.89, "MFE_180D_pct": 24.86, "MAE_180D_pct": -8.89, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive", "expected_stage_path": "Stage2-Actionable -> Yellow candidate; Green requires CSM amortization/reserve persistence", "current_profile_error": "current_profile_may_underweight_health_CSM_mix_if_treated_as_simple_life_insurer_value_up", "component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 7, "bottleneck_pricing_power": 3, "market_mispricing": 5, "valuation_rerating": 6, "capital_allocation": 6, "information_confidence": 8, "total_raw_score": 68}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 162, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set", "case_id": "C22_R6_L162_088350_20240515", "ticker": "088350", "company_name": "Hanwha Life Insurance", "market_country": "KR", "trigger_date": "2024-05-15", "entry_date": "2024-05-16", "entry_price": 3160.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-FalsePositive", "evidence_family": "1Q24_APE_new_CSM_retention_growth_without_price_confirmation", "source_url": "https://file.alphasquare.co.kr/media/pdfs/company-ir/20240515%ED%95%9C%ED%99%94%EC%83%9D%EB%AA%85_2024%EB%85%84_1%EB%B6%84%EA%B8%B0_%EA%B2%BD%EC%98%81%EC%8B%A4%EC%A0%81_%EB%B0%9C%ED%91%9C.pdf", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": -0.16, "MAE_30D_pct": -14.72, "MFE_90D_pct": 2.53, "MAE_90D_pct": -14.72, "MFE_180D_pct": 2.53, "MAE_180D_pct": -23.1, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "counterexample", "expected_stage_path": "Stage2-Watch -> high-MAE/4B guard; no Actionable", "current_profile_error": "APE_and_new_CSM_vocabulary_false_positive_when_loss_ratio_capital_quality_unconfirmed", "component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 5, "bottleneck_pricing_power": 2, "market_mispricing": 4, "valuation_rerating": 4, "capital_allocation": 4, "information_confidence": 8, "total_raw_score": 52}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 162, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set", "case_id": "C22_R6_L162_003690_20240516", "ticker": "003690", "company_name": "Korean Reinsurance", "market_country": "KR", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 7980.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Watch", "evidence_family": "1Q24_reinsurance_profitability_portfolio_quality_rate_cycle", "source_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516002102&docno=&method=search&viewerhost=", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 2.76, "MAE_30D_pct": -4.39, "MFE_90D_pct": 12.78, "MAE_90D_pct": -4.39, "MFE_180D_pct": 19.67, "MAE_180D_pct": -4.39, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive_watch", "expected_stage_path": "Stage2-Watch/Actionable boundary; low-MAE positive but not Green", "current_profile_error": "profile_may_miss_low_MAE_reinsurance_rate_cycle_but_MFE_below_green_threshold", "component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 7, "bottleneck_pricing_power": 5, "market_mispricing": 5, "valuation_rerating": 5, "capital_allocation": 6, "information_confidence": 8, "total_raw_score": 66}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 162, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set", "case_id": "C22_R6_L162_138040_20241114", "ticker": "138040", "company_name": "Meritz Financial Group", "market_country": "KR", "trigger_date": "2024-11-14", "entry_date": "2024-11-15", "entry_price": 101800.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage2-Actionable", "evidence_family": "3Q24_earnings_share_buyback_cancellation_subsidiary_dividend_bridge", "source_url": "https://www.asiae.co.kr/en/article/2024112109033861930", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 4.22, "MAE_30D_pct": -5.01, "MFE_90D_pct": 25.15, "MAE_90D_pct": -5.01, "MFE_180D_pct": 25.15, "MAE_180D_pct": -5.01, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "positive_boundary_C21_C22", "expected_stage_path": "Stage2-Actionable -> Yellow candidate; classify boundary not pure C22 if only buyback evidence", "current_profile_error": "boundary_positive_if_C22_insurance_profit_and_C21_capital_return_bridge_are_jointly_verified", "component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 8, "bottleneck_pricing_power": 3, "market_mispricing": 7, "valuation_rerating": 7, "capital_allocation": 10, "information_confidence": 7, "total_raw_score": 78}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
{"row_type": "trigger", "round_id": "R6", "loop_id": 162, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "mixed_c22_ifrs17_csm_reserve_rate_cycle_capital_return_leaf_set", "case_id": "C22_R6_L162_032830_20241115", "ticker": "032830", "company_name": "Samsung Life Insurance", "market_country": "KR", "trigger_date": "2024-11-15", "entry_date": "2024-11-18", "entry_price": 108800.0, "entry_price_source": "stock-web tradable shard close c", "trigger_type": "Stage3-Yellow-TooLate-4BWatch", "evidence_family": "3Q24_cumulative_profit_CSM_balance_KICS_late_headline_high_MAE", "source_url": "https://www.yna.co.kr/view/AKR20241115054400002", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "validation_scope": ["30D", "90D", "180D"], "MFE_30D_pct": 1.47, "MAE_30D_pct": -16.36, "MFE_90D_pct": 1.47, "MAE_90D_pct": -26.84, "MFE_180D_pct": 34.93, "MAE_180D_pct": -32.63, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_window_status": "clean_180D", "label": "counterexample_high_MAE_then_late_MFE", "expected_stage_path": "local 4B/high-MAE watch despite later D180 MFE; staged entry required", "current_profile_error": "too_late_green_or_actionable_entry_without_staged_entry_guard", "component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 8, "bottleneck_pricing_power": 3, "market_mispricing": 5, "valuation_rerating": 6, "capital_allocation": 6, "information_confidence": 8, "total_raw_score": 72}, "notes": "C22 shadow calibration row; no production scoring change in this research run."}
```

## 7. Score-return alignment

```text
positive_or_watch_rows = 4
counterexample_or_high_MAE_rows = 4
D180_MFE_ge_20_count = 4
D90_MAE_le_minus_20_count = 1
D180_MAE_le_minus_20_count = 3
highest_clean_positive = 000810 / Samsung Fire / 2025-02-12 / MFE180 46.72 / MAE180 -8.79
highest_drawdown_counterexample = 032830 / Samsung Life / 2024-11-15 / MFE180 34.93 / MAE180 -32.63
best low_MAE_watch = 003690 / Korean Re / 2024-05-16 / MFE180 19.67 / MAE180 -4.39
```

The alignment is mixed but useful. Insurance rerating can be very forgiving when the bridge is real; it can also hide a deep drawdown behind later recovery. Therefore C22 needs a two-step gate: first non-price quality, then timing/risk guard.

## 8. Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff and requires non-price evidence. The remaining C22-specific residual errors are narrower:

1. **CSM/APE vocabulary false positive** — new CSM and APE growth are not enough without reserve quality, loss-ratio, or conversion evidence. Hanwha Life and Hyundai Marine are the main examples.
2. **One-off reserve release pollution** — DB Insurance shows that one-off onerous-contract-cost reversal can make a quarter look cleaner than its recurring quality.
3. **Late headline / high-MAE timing risk** — Samsung Life Q3 proves that strong CSM/profit evidence can still be a bad immediate entry if crowding and valuation reset are ignored.
4. **C21/C22 boundary leakage** — Meritz works only if insurance-sub profit and capital-return execution are jointly verified. Buyback-only rows should remain C21.
5. **Reinsurance subgate** — Korean Re needs a different path: underwriting portfolio/rate-cycle discipline can produce low-MAE quality, but Green requires stronger revision or capital-return confirmation.

## 9. Shadow rule candidate

```text
rule_id = C22_CSM_RESERVE_QUALITY_RATE_CYCLE_AND_CAPITAL_RETURN_GATE_V1
scope = C22_INSURANCE_RATE_CYCLE_RESERVE
production_scoring_changed = false
shadow_weight_only = true
```

### Proposed gate

C22 Stage2-Actionable should require at least one **insurance-profit bridge** and one **quality/risk bridge**.

Insurance-profit bridge:

- CSM balance growth with new-contract CSM or health/protection mix improvement.
- Underwriting profit growth or reinsurance rate-cycle/portfolio discipline.
- Recurring insurance service result, not just investment profit or one-off reserve release.

Quality/risk bridge:

- Loss ratio or experience variance stability.
- K-ICS/capital adequacy not deteriorating into the trigger window.
- Reserve release identified as recurring or explicitly separated from one-off gains.
- Capital return execution, not just a policy plan.

### Stage handling

```text
if CSM_or_APE_growth_only and no loss_ratio_or_reserve_quality_confirmation:
    cap_stage = Stage2-Watch
    add_false_positive_risk = true

if one_off_reserve_release_material and recurring_insurance_profit_bridge_weak:
    block_Stage2_Actionable = true
    label = C22_one_off_reserve_release_pollution

if D90_MAE_pct <= -20 or D180_MAE_pct <= -25 after a late headline:
    add_local_4B_high_MAE_guard = true
    require_staged_entry = true

if buyback_or_cancellation_is_primary_evidence:
    require_C21_C22_boundary_check = true
    C22_valid_only_if_insurance_subsidiary_profit_and_solvency_bridge_present = true

if reinsurance_portfolio_quality_and_rate_cycle_present and MAE_low but MFE_below_20:
    allow_Stage2_Watch_or_low_MAE_positive_watch
    block_Green_until_revision_or_capital_return_confirms = true
```

## 10. Residual contribution summary

```text
new_axis_proposed = c22_csm_reserve_quality_rate_cycle_and_capital_return_gate
existing_axis_strengthened = stage2_required_bridge|local_4b_watch_guard|price_only_blowoff_blocks_positive_stage
existing_axis_weakened = hard_green_on_insurance_profit_headline_without_MAE_guard
sector_specific_rule_candidate = L6_C22_INSURANCE_CSM_RESERVE_QUALITY_AND_CAPITAL_RETURN_GATE_V1
canonical_archetype_rule_candidate = C22_CSM_RESERVE_QUALITY_RATE_CYCLE_AND_CAPITAL_RETURN_GATE_V1
loop_contribution_label = canonical_archetype_rule_candidate
```

C22 behaves like a dam system. CSM is the reservoir, APE is incoming rain, reserve releases are sluice gates, and K-ICS is the concrete wall. A headline can show the lake rising, but the investment case only works if the wall is sound and the gates are not being opened just once to create a temporary surge.

## 11. Narrative-only / blocked rows

```jsonl
{"row_type":"narrative_only","round_id":"R6","loop_id":162,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","ticker":"003690","company_name":"Korean Reinsurance","trigger_date":"2025-07-01","reason":"insufficient_forward_window_in_stock_web_for_D180_by_manifest_max_date_2026-02-20","calibration_usable":false,"notes":"Later 2025 reinsurance rating/portfolio-quality discussion was not used as a regular trigger row because the 180-trading-day forward window was unavailable."}
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When the batch implementation session runs after validating this MD together with the rest of docs/round:

1. Ingest this file only if the filename matches required v12 regex and all JSONL trigger rows pass required fields.
2. Validate all 8 trigger rows against stock-web tradable shards and symbol profiles.
3. If accepted, create a C22-only patch candidate named:
   C22_CSM_RESERVE_QUALITY_RATE_CYCLE_AND_CAPITAL_RETURN_GATE_V1
4. Do not loosen Stage3-Green globally.
5. Implement the patch as a scoped Stage2/4B guard:
   - CSM/APE growth alone: Stage2-Watch only.
   - one-off reserve release materiality: block Stage2-Actionable unless recurring bridge exists.
   - buyback-only evidence: route to C21 unless insurance-sub profit/solvency bridge is explicit.
   - late headline with D90 MAE <= -20 or D180 MAE <= -25 in representative rows: add local 4B/high-MAE guard.
6. Keep production_scoring_changed=false until aggregate validation says apply_next_patch.
```

## 13. Research state for next run

```text
completed_round = R6
completed_loop = 162
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
next_recommended_archetypes = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|C24_BIO_TRIAL_DATA_EVENT_RISK|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|C15_MATERIAL_SPREAD_SUPERCYCLE
```
