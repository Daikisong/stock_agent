# E2R Stock-Web v12 Residual Research — R8 loop 186 — C26 Platform Ad Revenue Operating Leverage

```text
completed_round = R8
completed_loop = 186
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE
output_filename = e2r_stock_web_v12_residual_round_R8_loop_186_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

## 1. Scope guard

This research follows the E2R Historical Calibration Prompt v12. It is not a live candidate scan, not a broker/API task, not a `stock_agent` code patch, and not a production scoring change. The only output is this standalone historical calibration Markdown file using actual `Songdaiki/stock-web` 1D OHLCV rows.

```text
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
must_use_actual_stock_web_1D_OHLC = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
```

## 2. Coverage-index selection rationale

The original No-Repeat Index shows `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` at 106 representative rows, already above the minimum. After this session's P0/P1 clearing and the earlier C26 passes, this loop is not a row-count expansion pass. It is a quality-repair pass for an under-specified C26 leaf: Korean adtech, digital-agency, and creator-commerce platforms often show platform/ad vocabulary before actual operating leverage appears.

```text
index_baseline_coverage_before = C26 rows 106
index_baseline_coverage_after_if_accepted = C26 rows 116
session_aware_after_loop122_loop180_loop186_if_accepted = about C26 rows 123
selection_reason = Priority 2 quality repair; adtech/commercial operating leverage vs partnership/theme blowoff
new_independent_case_count = 10
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 10
minimum_new_symbol_count = pass
minimum_positive_case_count = pass
minimum_counterexample_count = pass
```

## 3. Price source validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_price_rule = entry_date close column c
MFE_MAE_rule = max high / min low after entry_date through 30/90/180 trading rows
```

Profile check:

```text
030000 Cheil Worldwide: active_like, last_date 2026-02-20, corporate_action_candidate_dates = 1999-02-01|2010-05-10; no overlap with 2024~2025 trigger windows.
042000 Cafe24: active_like, last_date 2026-02-20, corporate_action_candidate_dates = 2021-01-28|2021-02-22; no overlap with 2024~2025 trigger windows.
237820 PlayD: active_like, last_date 2026-02-20, corporate_action_candidate_count = 0.
273060 Wisebirds: active_like, last_date 2026-02-20, corporate_action_candidate_dates = 2020-08-05; no overlap with 2024~2025 trigger windows.
363260 Mobidays: active_like, last_date 2026-02-20, corporate_action_candidate_dates = 2022-06-08|2024-05-24; the 2024-06-24 entry starts after the candidate date, so D+180 window is not contaminated.
214270 FSN: active_like, last_date 2026-02-20, corporate_action_candidate_dates = 2016-10-05|2018-03-05|2021-11-08; no overlap with 2025 trigger windows.
```

## 4. Human-readable case table

| case | symbol | company | role | trigger | entry/price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C26-L186-CASE01-030000-CHEIL-Q2-2024-DIGITAL-GP-LOW-ALPHA | 030000 | Cheil Worldwide / 제일기획 | counterexample / low-alpha ad operating leverage | Stage2-Watch 2024-07-31 | 2024-08-01 / 17800 | 5.79 / -7.87 | 5.84 / -7.87 | 7.47 / -7.87 | current_profile_false_positive_if_digital_mix_growth_is_promoted_without_operating_leverage |
| C26-L186-CASE02-030000-CHEIL-FY2024-DIGITAL-RETAIL-QUALITY | 030000 | Cheil Worldwide / 제일기획 | positive / low-MAE quality compounding | Stage2-Actionable 2025-02-04 | 2025-02-04 / 17340 | 5.54 / -1.15 | 20.82 / -2.08 | 29.47 / -2.08 | current_profile_correct_when_digital_retail_growth_is_confirmed_by_realized_OP_and_low_MAE_path |
| C26-L186-CASE03-042000-CAFE24-YOUTUBE-SHOPPING-COMMISSION-BRIDGE | 042000 | Cafe24 / 카페24 | positive with high-MAE staged-entry guard | Stage2-Watch 2024-06-21 | 2024-06-21 / 40900 | 5.01 / -32.89 | 5.01 / -44.13 | 70.42 / -44.13 | current_profile_too_binary_if_youtube_commerce_bridge_is_blocked_but_must_attach_high_MAE_staged_entry_guard |
| C26-L186-CASE04-042000-CAFE24-Q4-2024-YOUTUBE-EXPECTATION-LATE | 042000 | Cafe24 / 카페24 | counterexample / late YouTube-shopping expectation | Stage4B-Watch 2025-02-05 | 2025-02-05 / 56200 | 24.02 / -8.01 | 24.02 / -23.04 | 24.02 / -36.57 | current_profile_false_positive_if_partnership_expectation_is_treated_like_fresh_operating_leverage_after_price_revaluation |
| C26-L186-CASE05-237820-PLAYD-2024-OPERATING-LEVERAGE-FORECAST | 237820 | PlayD / 플레이디 | positive / early ad-cycle operating leverage | Stage2-Actionable 2023-11-03 | 2023-11-06 / 4360 | 27.29 / -6.31 | 144.5 / -6.31 | 144.5 / -6.31 | current_profile_too_late_if_operating_leverage_forecast_with_cost_down_and_captive_demand_is_ignored |
| C26-L186-CASE06-237820-PLAYD-2024-REALIZED-OP-LOW-ALPHA | 237820 | PlayD / 플레이디 | counterexample / realized earnings after re-rating | Stage2-Watch 2025-03-20 | 2025-03-20 / 5680 | 10.74 / -13.73 | 10.74 / -13.73 | 10.74 / -21.65 | current_profile_false_positive_if_realized_OP_growth_after_prior_rerating_is_promoted_without_new_customer_or_GMV_bridge |
| C26-L186-CASE07-273060-WISEBIRDS-AD-EFFICIENCY-ACQUISITION-UNCERTAIN | 273060 | Wisebirds / 와이즈버즈 | counterexample / acquisition synergy before profit bridge | Stage4B-Watch 2024-02-19 | 2024-02-19 / 1340 | 36.87 / -3.58 | 36.87 / -15.75 | 36.87 / -40.75 | current_profile_false_positive_if_adtech_acquisition_synergy_is_scored_before_margin_bridge_and_deleveraging_confirmation |
| C26-L186-CASE08-273060-WISEBIRDS-Q1-2025-AD-EFFICIENCY-RAMP | 273060 | Wisebirds / 와이즈버즈 | positive with high-MAE guard | Stage2-Actionable 2025-05-15 | 2025-05-15 / 1027 | 13.63 / -5.06 | 34.37 / -5.06 | 40.31 / -22.1 | current_profile_correct_if_new_advertiser_and_acquisition_integration_convert_to_OP_but_high_MAE_exit_guard_needed |
| C26-L186-CASE09-363260-MOBIDAYS-Q1-2024-TIKTOK-SHOP-OPTIONALITY | 363260 | Mobidays / 모비데이즈 | counterexample / optionality without OP bridge | Stage4B-Watch 2024-06-24 | 2024-06-24 / 2310 | 21.21 / -29.74 | 29.22 / -32.73 | 29.22 / -39.22 | current_profile_false_positive_if_tiktok_shop_or_content_optionalities_are_promoted_before_core_ad_margin_recovers |
| C26-L186-CASE10-214270-FSN-Q1-2025-BRAND-PLATFORM-OP-LEVERAGE | 214270 | FSN / 에프에스엔 | positive / brand-platform operating leverage | Stage2-Actionable 2025-05-16 | 2025-05-16 / 1806 | 97.12 / -15.01 | 118.99 / -15.01 | 118.99 / -15.01 | current_profile_too_late_if_brand_platform_OP_conversion_and_business_restructuring_are_waited_until_after_full_year_confirmation |

## 5. Case notes

### CASE01 — Cheil Worldwide / 제일기획 / 030000

1H/Q2 2024 release: revenue and gross profit grew, but operating profit growth was modest because SG&A and digital-focused labor investment absorbed much of the gross-profit expansion. The stock-web route from `2024-08-01` close `17800` produced `30D 5.79/-7.87`, `90D 5.84/-7.87`, and `180D 7.47/-7.87` MFE/MAE. Verdict: `current_profile_false_positive_if_digital_mix_growth_is_promoted_without_operating_leverage`. Evidence: [https://www.cheil.com/upload/ir/quarterly/eng/CheilWorldwide_242Q_ENG_F.pdf](https://www.cheil.com/upload/ir/quarterly/eng/CheilWorldwide_242Q_ENG_F.pdf).

### CASE02 — Cheil Worldwide / 제일기획 / 030000

FY2024 operating profit was reported at KRW 320.7bn, up 4.2% YoY, with digital and retail highlighted as growth drivers. The stock-web route from `2025-02-04` close `17340` produced `30D 5.54/-1.15`, `90D 20.82/-2.08`, and `180D 29.47/-2.08` MFE/MAE. Verdict: `current_profile_correct_when_digital_retail_growth_is_confirmed_by_realized_OP_and_low_MAE_path`. Evidence: [https://biz.chosun.com/en/en-industry/2025/02/04/ALM4B5PEV5BEPGHAENEUG6CEQ4/](https://biz.chosun.com/en/en-industry/2025/02/04/ALM4B5PEV5BEPGHAENEUG6CEQ4/).

### CASE03 — Cafe24 / 카페24 / 042000

Cafe24 was expanding through YouTube Shopping; the model links creators and shopping malls, and Cafe24 earns commission when YouTube traffic converts into mall purchases. The stock-web route from `2024-06-21` close `40900` produced `30D 5.01/-32.89`, `90D 5.01/-44.13`, and `180D 70.42/-44.13` MFE/MAE. Verdict: `current_profile_too_binary_if_youtube_commerce_bridge_is_blocked_but_must_attach_high_MAE_staged_entry_guard`. Evidence: [https://en.topdaily.kr/articles/1424](https://en.topdaily.kr/articles/1424).

### CASE04 — Cafe24 / 카페24 / 042000

Research highlighted the YouTube Shopping partnership program, seller/creator matching, and Q4 operating-profit expectation near consensus, but the stock was already discounting the story. The stock-web route from `2025-02-05` close `56200` produced `30D 24.02/-8.01`, `90D 24.02/-23.04`, and `180D 24.02/-36.57` MFE/MAE. Verdict: `current_profile_false_positive_if_partnership_expectation_is_treated_like_fresh_operating_leverage_after_price_revaluation`. Evidence: [https://www.asiae.co.kr/en/article/2025020507520972176](https://www.asiae.co.kr/en/article/2025020507520972176).

### CASE05 — PlayD / 플레이디 / 237820

KIRS report forecast 2024 revenue +12.4% YoY and OP +134.7% YoY, citing ad-market recovery, KT captive expansion, ad-expense reduction, and operating leverage. The stock-web route from `2023-11-06` close `4360` produced `30D 27.29/-6.31`, `90D 144.5/-6.31`, and `180D 144.5/-6.31` MFE/MAE. Verdict: `current_profile_too_late_if_operating_leverage_forecast_with_cost_down_and_captive_demand_is_ignored`. Evidence: [https://ssl.pstatic.net/imgstock/upload/research/company/1698966461488.pdf](https://ssl.pstatic.net/imgstock/upload/research/company/1698966461488.pdf).

### CASE06 — PlayD / 플레이디 / 237820

The 2024 business-report evidence says revenue was up 3.6% and operating profit increased 58.1%, but this was a post-cycle realization rather than fresh ad-demand acceleration. The stock-web route from `2025-03-20` close `5680` produced `30D 10.74/-13.73`, `90D 10.74/-13.73`, and `180D 10.74/-21.65` MFE/MAE. Verdict: `current_profile_false_positive_if_realized_OP_growth_after_prior_rerating_is_promoted_without_new_customer_or_GMV_bridge`. Evidence: [https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001350&docno=&method=search&viewerhost=](https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001350&docno=&method=search&viewerhost=).

### CASE07 — Wisebirds / 와이즈버즈 / 273060

Early-2024 evidence mixed acquisition synergy language with weak prior-year profitability; 2023 operating profit had fallen sharply and the ad-efficiency acquisition bridge was not yet proven. The stock-web route from `2024-02-19` close `1340` produced `30D 36.87/-3.58`, `90D 36.87/-15.75`, and `180D 36.87/-40.75` MFE/MAE. Verdict: `current_profile_false_positive_if_adtech_acquisition_synergy_is_scored_before_margin_bridge_and_deleveraging_confirmation`. Evidence: [https://securities.miraeasset.com/bbs/download/2122413.pdf?attachmentId=2122413](https://securities.miraeasset.com/bbs/download/2122413.pdf?attachmentId=2122413).

### CASE08 — Wisebirds / 와이즈버즈 / 273060

Q1 2025 revenue rose 111.7% YoY and OP swung to KRW 641.51mn; management cited AdEfficiency integration, media partnerships, and new advertisers. The stock-web route from `2025-05-15` close `1027` produced `30D 13.63/-5.06`, `90D 34.37/-5.06`, and `180D 40.31/-22.1` MFE/MAE. Verdict: `current_profile_correct_if_new_advertiser_and_acquisition_integration_convert_to_OP_but_high_MAE_exit_guard_needed`. Evidence: [https://v.daum.net/v/V3jtvnYchI](https://v.daum.net/v/V3jtvnYchI).

### CASE09 — Mobidays / 모비데이즈 / 363260

The report described online marketing, K-pop commerce expansion, TikTok official partner optionality, but Q1 2024 operating profit was negative due to new-business investment. The stock-web route from `2024-06-24` close `2310` produced `30D 21.21/-29.74`, `90D 29.22/-32.73`, and `180D 29.22/-39.22` MFE/MAE. Verdict: `current_profile_false_positive_if_tiktok_shop_or_content_optionalities_are_promoted_before_core_ad_margin_recovers`. Evidence: [https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/06/21/240624_mobidays.pdf](https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/06/21/240624_mobidays.pdf).

### CASE10 — FSN / 에프에스엔 / 214270

FSN announced Q1 2025 revenue of KRW 86.3bn, OP of KRW 4.1bn, EBITDA of KRW 6.3bn, and a first-quarter turnaround after excluding separated tech affiliates. The stock-web route from `2025-05-16` close `1806` produced `30D 97.12/-15.01`, `90D 118.99/-15.01`, and `180D 118.99/-15.01` MFE/MAE. Verdict: `current_profile_too_late_if_brand_platform_OP_conversion_and_business_restructuring_are_waited_until_after_full_year_confirmation`. Evidence: [https://fsn.co.kr/ir/news/86](https://fsn.co.kr/ir/news/86).

## 6. Score-return alignment and residual rule

```text
calibration_usable_trigger_count = 10
representative_trigger_count = 10
positive_case_count = 5
counterexample_count = 5
Stage4B_watch_or_overlay_count = 3
current_profile_error_count = 7
```

C26 should not treat all platform/ad vocabulary as the same current. The clean positive rows had at least two connected bridges: `traffic/ad-inventory/commerce network -> revenue/GMV/gross-profit -> operating profit or low-MAE price path`. The weak rows had only one bridge: partnership language, digital mix, an acquisition narrative, or expected ad-cycle recovery. Those rows often showed either low alpha or a deep MAE before any durable MFE appeared.

```text
canonical_archetype_rule_candidate = C26_ADTECH_COMMERCE_OPERATING_LEVERAGE_AND_EXIT_GATE_V3
rule_summary = require retained advertiser/creator/merchant network bridge plus operating-profit conversion bridge; downgrade partnership-only, acquisition-synergy-only, TikTok/YouTube/AI vocabulary-only, or late realized-earnings rows to Stage2-Watch or Stage4B-Watch.
new_axis_proposed = c26_adtech_commerce_ad_operating_leverage_and_theme_exit_gate
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|stage2_required_bridge
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

## 7. Raw component score breakdown

| case | EPS/FCF | visibility | bottleneck/pricing | mispricing | valuation | capital | info | raw_total | stage alignment |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C26-L186-CASE01-030000-CHEIL-Q2-2024-DIGITAL-GP-LOW-ALPHA | 46 | 55 | 32 | 40 | 42 | 45 | 72 | 47.4 | Stage2-Actionable risk → Stage2-Watch |
| C26-L186-CASE02-030000-CHEIL-FY2024-DIGITAL-RETAIL-QUALITY | 62 | 67 | 38 | 48 | 51 | 52 | 78 | 56.6 | Stage2-Watch → Stage2-Actionable |
| C26-L186-CASE03-042000-CAFE24-YOUTUBE-SHOPPING-COMMISSION-BRIDGE | 55 | 61 | 58 | 64 | 39 | 41 | 72 | 55.7 | Stage2-Watch → Stage2-Watch_to_Actionable_after_GMV_confirmation |
| C26-L186-CASE04-042000-CAFE24-Q4-2024-YOUTUBE-EXPECTATION-LATE | 58 | 63 | 59 | 34 | 26 | 38 | 70 | 49.7 | Stage2-Actionable risk → Stage4B-Watch |
| C26-L186-CASE05-237820-PLAYD-2024-OPERATING-LEVERAGE-FORECAST | 71 | 62 | 43 | 66 | 68 | 44 | 74 | 61.1 | Stage2-Watch → Stage2-Actionable |
| C26-L186-CASE06-237820-PLAYD-2024-REALIZED-OP-LOW-ALPHA | 61 | 59 | 36 | 31 | 36 | 42 | 69 | 47.7 | Stage2-Actionable risk → Stage2-Watch |
| C26-L186-CASE07-273060-WISEBIRDS-AD-EFFICIENCY-ACQUISITION-UNCERTAIN | 37 | 43 | 41 | 35 | 30 | 31 | 60 | 39.6 | Stage2-Actionable risk → Stage4B-Watch |
| C26-L186-CASE08-273060-WISEBIRDS-Q1-2025-AD-EFFICIENCY-RAMP | 66 | 60 | 45 | 57 | 49 | 48 | 74 | 57.0 | Stage2-Watch → Stage2-Actionable_with_exit_guard |
| C26-L186-CASE09-363260-MOBIDAYS-Q1-2024-TIKTOK-SHOP-OPTIONALITY | 31 | 39 | 44 | 28 | 27 | 29 | 66 | 37.7 | Stage2-Actionable risk → Stage4B-Watch |
| C26-L186-CASE10-214270-FSN-Q1-2025-BRAND-PLATFORM-OP-LEVERAGE | 72 | 58 | 46 | 72 | 61 | 54 | 71 | 62.0 | Stage2-Watch → Stage2-Actionable |

## 8. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "case_id": "C26-L186-CASE01-030000-CHEIL-Q2-2024-DIGITAL-GP-LOW-ALPHA", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "030000", "company": "Cheil Worldwide / 제일기획", "trigger_date": "2024-07-31", "entry_date": "2024-08-01", "entry_price": 17800.0, "trigger_type": "Stage2-Watch", "MFE_30D_pct": 5.79, "MAE_30D_pct": -7.87, "MFE_90D_pct": 5.84, "MAE_90D_pct": -7.87, "MFE_180D_pct": 7.47, "MAE_180D_pct": -7.87, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://www.cheil.com/upload/ir/quarterly/eng/CheilWorldwide_242Q_ENG_F.pdf", "evidence_summary": "1H/Q2 2024 release: revenue and gross profit grew, but operating profit growth was modest because SG&A and digital-focused labor investment absorbed much of the gross-profit expansion.", "role": "counterexample / low-alpha ad operating leverage", "verdict": "current_profile_false_positive_if_digital_mix_growth_is_promoted_without_operating_leverage", "current_profile_proxy_stage": "Stage2-Actionable risk", "proposed_shadow_stage": "Stage2-Watch", "raw_component_score_breakdown": {"eps_fcf": 46, "visibility": 55, "bottleneck": 32, "mispricing": 40, "valuation": 42, "capital": 45, "info": 72}, "raw_total_score": 47.4, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE02-030000-CHEIL-FY2024-DIGITAL-RETAIL-QUALITY", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "030000", "company": "Cheil Worldwide / 제일기획", "trigger_date": "2025-02-04", "entry_date": "2025-02-04", "entry_price": 17340.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 5.54, "MAE_30D_pct": -1.15, "MFE_90D_pct": 20.82, "MAE_90D_pct": -2.08, "MFE_180D_pct": 29.47, "MAE_180D_pct": -2.08, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://biz.chosun.com/en/en-industry/2025/02/04/ALM4B5PEV5BEPGHAENEUG6CEQ4/", "evidence_summary": "FY2024 operating profit was reported at KRW 320.7bn, up 4.2% YoY, with digital and retail highlighted as growth drivers.", "role": "positive / low-MAE quality compounding", "verdict": "current_profile_correct_when_digital_retail_growth_is_confirmed_by_realized_OP_and_low_MAE_path", "current_profile_proxy_stage": "Stage2-Watch", "proposed_shadow_stage": "Stage2-Actionable", "raw_component_score_breakdown": {"eps_fcf": 62, "visibility": 67, "bottleneck": 38, "mispricing": 48, "valuation": 51, "capital": 52, "info": 78}, "raw_total_score": 56.6, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE03-042000-CAFE24-YOUTUBE-SHOPPING-COMMISSION-BRIDGE", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "042000", "company": "Cafe24 / 카페24", "trigger_date": "2024-06-21", "entry_date": "2024-06-21", "entry_price": 40900.0, "trigger_type": "Stage2-Watch", "MFE_30D_pct": 5.01, "MAE_30D_pct": -32.89, "MFE_90D_pct": 5.01, "MAE_90D_pct": -44.13, "MFE_180D_pct": 70.42, "MAE_180D_pct": -44.13, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://en.topdaily.kr/articles/1424", "evidence_summary": "Cafe24 was expanding through YouTube Shopping; the model links creators and shopping malls, and Cafe24 earns commission when YouTube traffic converts into mall purchases.", "role": "positive with high-MAE staged-entry guard", "verdict": "current_profile_too_binary_if_youtube_commerce_bridge_is_blocked_but_must_attach_high_MAE_staged_entry_guard", "current_profile_proxy_stage": "Stage2-Watch", "proposed_shadow_stage": "Stage2-Watch_to_Actionable_after_GMV_confirmation", "raw_component_score_breakdown": {"eps_fcf": 55, "visibility": 61, "bottleneck": 58, "mispricing": 64, "valuation": 39, "capital": 41, "info": 72}, "raw_total_score": 55.7, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE04-042000-CAFE24-Q4-2024-YOUTUBE-EXPECTATION-LATE", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "042000", "company": "Cafe24 / 카페24", "trigger_date": "2025-02-05", "entry_date": "2025-02-05", "entry_price": 56200.0, "trigger_type": "Stage4B-Watch", "MFE_30D_pct": 24.02, "MAE_30D_pct": -8.01, "MFE_90D_pct": 24.02, "MAE_90D_pct": -23.04, "MFE_180D_pct": 24.02, "MAE_180D_pct": -36.57, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://www.asiae.co.kr/en/article/2025020507520972176", "evidence_summary": "Research highlighted the YouTube Shopping partnership program, seller/creator matching, and Q4 operating-profit expectation near consensus, but the stock was already discounting the story.", "role": "counterexample / late YouTube-shopping expectation", "verdict": "current_profile_false_positive_if_partnership_expectation_is_treated_like_fresh_operating_leverage_after_price_revaluation", "current_profile_proxy_stage": "Stage2-Actionable risk", "proposed_shadow_stage": "Stage4B-Watch", "raw_component_score_breakdown": {"eps_fcf": 58, "visibility": 63, "bottleneck": 59, "mispricing": 34, "valuation": 26, "capital": 38, "info": 70}, "raw_total_score": 49.7, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE05-237820-PLAYD-2024-OPERATING-LEVERAGE-FORECAST", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "237820", "company": "PlayD / 플레이디", "trigger_date": "2023-11-03", "entry_date": "2023-11-06", "entry_price": 4360.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 27.29, "MAE_30D_pct": -6.31, "MFE_90D_pct": 144.5, "MAE_90D_pct": -6.31, "MFE_180D_pct": 144.5, "MAE_180D_pct": -6.31, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1698966461488.pdf", "evidence_summary": "KIRS report forecast 2024 revenue +12.4% YoY and OP +134.7% YoY, citing ad-market recovery, KT captive expansion, ad-expense reduction, and operating leverage.", "role": "positive / early ad-cycle operating leverage", "verdict": "current_profile_too_late_if_operating_leverage_forecast_with_cost_down_and_captive_demand_is_ignored", "current_profile_proxy_stage": "Stage2-Watch", "proposed_shadow_stage": "Stage2-Actionable", "raw_component_score_breakdown": {"eps_fcf": 71, "visibility": 62, "bottleneck": 43, "mispricing": 66, "valuation": 68, "capital": 44, "info": 74}, "raw_total_score": 61.1, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE06-237820-PLAYD-2024-REALIZED-OP-LOW-ALPHA", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "237820", "company": "PlayD / 플레이디", "trigger_date": "2025-03-20", "entry_date": "2025-03-20", "entry_price": 5680.0, "trigger_type": "Stage2-Watch", "MFE_30D_pct": 10.74, "MAE_30D_pct": -13.73, "MFE_90D_pct": 10.74, "MAE_90D_pct": -13.73, "MFE_180D_pct": 10.74, "MAE_180D_pct": -21.65, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001350&docno=&method=search&viewerhost=", "evidence_summary": "The 2024 business-report evidence says revenue was up 3.6% and operating profit increased 58.1%, but this was a post-cycle realization rather than fresh ad-demand acceleration.", "role": "counterexample / realized earnings after re-rating", "verdict": "current_profile_false_positive_if_realized_OP_growth_after_prior_rerating_is_promoted_without_new_customer_or_GMV_bridge", "current_profile_proxy_stage": "Stage2-Actionable risk", "proposed_shadow_stage": "Stage2-Watch", "raw_component_score_breakdown": {"eps_fcf": 61, "visibility": 59, "bottleneck": 36, "mispricing": 31, "valuation": 36, "capital": 42, "info": 69}, "raw_total_score": 47.7, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE07-273060-WISEBIRDS-AD-EFFICIENCY-ACQUISITION-UNCERTAIN", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "273060", "company": "Wisebirds / 와이즈버즈", "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 1340.0, "trigger_type": "Stage4B-Watch", "MFE_30D_pct": 36.87, "MAE_30D_pct": -3.58, "MFE_90D_pct": 36.87, "MAE_90D_pct": -15.75, "MFE_180D_pct": 36.87, "MAE_180D_pct": -40.75, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://securities.miraeasset.com/bbs/download/2122413.pdf?attachmentId=2122413", "evidence_summary": "Early-2024 evidence mixed acquisition synergy language with weak prior-year profitability; 2023 operating profit had fallen sharply and the ad-efficiency acquisition bridge was not yet proven.", "role": "counterexample / acquisition synergy before profit bridge", "verdict": "current_profile_false_positive_if_adtech_acquisition_synergy_is_scored_before_margin_bridge_and_deleveraging_confirmation", "current_profile_proxy_stage": "Stage2-Actionable risk", "proposed_shadow_stage": "Stage4B-Watch", "raw_component_score_breakdown": {"eps_fcf": 37, "visibility": 43, "bottleneck": 41, "mispricing": 35, "valuation": 30, "capital": 31, "info": 60}, "raw_total_score": 39.6, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE08-273060-WISEBIRDS-Q1-2025-AD-EFFICIENCY-RAMP", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "273060", "company": "Wisebirds / 와이즈버즈", "trigger_date": "2025-05-15", "entry_date": "2025-05-15", "entry_price": 1027.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 13.63, "MAE_30D_pct": -5.06, "MFE_90D_pct": 34.37, "MAE_90D_pct": -5.06, "MFE_180D_pct": 40.31, "MAE_180D_pct": -22.1, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://v.daum.net/v/V3jtvnYchI", "evidence_summary": "Q1 2025 revenue rose 111.7% YoY and OP swung to KRW 641.51mn; management cited AdEfficiency integration, media partnerships, and new advertisers.", "role": "positive with high-MAE guard", "verdict": "current_profile_correct_if_new_advertiser_and_acquisition_integration_convert_to_OP_but_high_MAE_exit_guard_needed", "current_profile_proxy_stage": "Stage2-Watch", "proposed_shadow_stage": "Stage2-Actionable_with_exit_guard", "raw_component_score_breakdown": {"eps_fcf": 66, "visibility": 60, "bottleneck": 45, "mispricing": 57, "valuation": 49, "capital": 48, "info": 74}, "raw_total_score": 57.0, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE09-363260-MOBIDAYS-Q1-2024-TIKTOK-SHOP-OPTIONALITY", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "363260", "company": "Mobidays / 모비데이즈", "trigger_date": "2024-06-24", "entry_date": "2024-06-24", "entry_price": 2310.0, "trigger_type": "Stage4B-Watch", "MFE_30D_pct": 21.21, "MAE_30D_pct": -29.74, "MFE_90D_pct": 29.22, "MAE_90D_pct": -32.73, "MFE_180D_pct": 29.22, "MAE_180D_pct": -39.22, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/06/21/240624_mobidays.pdf", "evidence_summary": "The report described online marketing, K-pop commerce expansion, TikTok official partner optionality, but Q1 2024 operating profit was negative due to new-business investment.", "role": "counterexample / optionality without OP bridge", "verdict": "current_profile_false_positive_if_tiktok_shop_or_content_optionalities_are_promoted_before_core_ad_margin_recovers", "current_profile_proxy_stage": "Stage2-Actionable risk", "proposed_shadow_stage": "Stage4B-Watch", "raw_component_score_breakdown": {"eps_fcf": 31, "visibility": 39, "bottleneck": 44, "mispricing": 28, "valuation": 27, "capital": 29, "info": 66}, "raw_total_score": 37.7, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "case_id": "C26-L186-CASE10-214270-FSN-Q1-2025-BRAND-PLATFORM-OP-LEVERAGE", "round": "R8", "loop": 186, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE", "symbol": "214270", "company": "FSN / 에프에스엔", "trigger_date": "2025-05-16", "entry_date": "2025-05-16", "entry_price": 1806.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 97.12, "MAE_30D_pct": -15.01, "MFE_90D_pct": 118.99, "MAE_90D_pct": -15.01, "MFE_180D_pct": 118.99, "MAE_180D_pct": -15.01, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "evidence_url": "https://fsn.co.kr/ir/news/86", "evidence_summary": "FSN announced Q1 2025 revenue of KRW 86.3bn, OP of KRW 4.1bn, EBITDA of KRW 6.3bn, and a first-quarter turnaround after excluding separated tech affiliates.", "role": "positive / brand-platform operating leverage", "verdict": "current_profile_too_late_if_brand_platform_OP_conversion_and_business_restructuring_are_waited_until_after_full_year_confirmation", "current_profile_proxy_stage": "Stage2-Watch", "proposed_shadow_stage": "Stage2-Actionable", "raw_component_score_breakdown": {"eps_fcf": 72, "visibility": 58, "bottleneck": 46, "mispricing": 72, "valuation": 61, "capital": 54, "info": 71}, "raw_total_score": 62.0, "production_scoring_changed": false, "shadow_weight_only": true}
```

## 9. Aggregate row

```json
{
  "row_type": "aggregate",
  "round": "R8",
  "loop": 186,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "fine_archetype_id": "C26_ADTECH_COMMERCE_AD_OPERATING_LEVERAGE_AND_THEME_EXIT_GATE",
  "usable_trigger_row_count": 10,
  "representative_trigger_count": 10,
  "positive_case_count": 5,
  "counterexample_count": 5,
  "current_profile_error_count": 7,
  "shadow_rule_candidate": "C26_ADTECH_COMMERCE_OPERATING_LEVERAGE_AND_EXIT_GATE_V3",
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 10. Deferred Coding Agent Handoff Prompt — do not execute in this research session

```text
You are the later coding agent. Do not rerun live discovery. Read this Markdown as one v12 residual research artifact. Parse the JSONL trigger rows, validate required fields, deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date, then consider a small C26-scoped shadow patch only if multiple accepted artifacts support it.
Candidate patch axis: C26_ADTECH_COMMERCE_OPERATING_LEVERAGE_AND_EXIT_GATE_V3.
Required behavior: strengthen Stage2 bridge requirements for adtech/commerce platform rows. Require at least one network-quality bridge (retained advertiser, merchant, creator, media partner, or acquisition-integration bridge) and one conversion bridge (OP, gross-profit leverage, GMV commission, low-MAE price path, or margin/revision confirmation). Downgrade partnership-only and optionality-only rows to Stage2-Watch or Stage4B-Watch.
Do not loosen Stage3-Green. Do not change production scoring from this single MD alone.
```

## 11. Next research state

```text
completed_round = R8
completed_loop = 186
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA|C22_INSURANCE_RATE_CYCLE_RESERVE|C19_BRAND_RETAIL_INVENTORY_MARGIN|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
