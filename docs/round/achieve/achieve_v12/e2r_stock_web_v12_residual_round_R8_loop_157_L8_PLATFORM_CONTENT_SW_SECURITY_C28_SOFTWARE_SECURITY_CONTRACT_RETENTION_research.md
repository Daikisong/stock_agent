# E2R Stock-Web v12 Residual Research — R8 / loop 157 / L8 / C28

## 0. Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R8
selected_loop: 157
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: mixed_c28_erp_saas_security_ai_pqc_retention_theme_leaf_set
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: session-aware Priority 1; original Index Priority 0
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
output_filename: e2r_stock_web_v12_residual_round_R8_loop_157_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
```

## 1. Scheduler and No-Repeat novelty check

The original No-Repeat Index places `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` at 28 representative rows, which is Priority 0 in the source ledger. This conversation already produced one C28 pass at loop 133 with 9 representative rows, so the session-aware count before this run is approximately 37. A second C28 pass is therefore useful as a clearing pass toward the 50-row practical calibration band.

This run avoids the loop 133 symbol cluster and uses eight symbols / fourteen trigger rows:

- `012510` Douzone Bizon / 더존비즈온
- `030520` Hancom / 한글과컴퓨터
- `053800` AhnLab / 안랩
- `047560` ESTsoft / 이스트소프트
- `434480` MonitorLab / 모니터랩
- `041020` Polaris Office / 폴라리스오피스
- `205100` Exem / 엑셈
- `192250` KSign / 케이사인

Hard duplicate key used for screening:

```text
canonical_archetype_id + ticker + trigger_type + entry_date
```

No row in this file repeats a session-local C28 loop 133 symbol/entry/trigger combination.

## 2. Price-source validation

```yaml
primary_price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
entry_price_rule: close price on entry_date
MFE_MAE_rule: max high / min low from entry_date through N tradable rows, compared with entry_price
forward_windows_required: [30D, 90D, 180D]
```

All fourteen rows have complete 30D/90D/180D MFE and MAE fields. No price is inferred beyond the stock-web manifest max date. Corporate-action contamination is marked from stock-web symbol profile inspection where available; no selected entry-to-180D window was blocked for corporate-action contamination in this run.

## 3. Case ledger

| case_id | ticker | company_kr | entry_date | entry_price | trigger_subtype | outcome | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C28-L157-001 | 012510 | 더존비즈온 | 2024-05-10 | 51700.00 | Stage2-Actionable | positive | 39.26 | -1.93 | 51.45 | -6.19 | 77.95 | -13.15 |
| C28-L157-002 | 012510 | 더존비즈온 | 2025-02-07 | 85700.00 | Late record-profit headline high-MAE guard | counterexample | 7.35 | -35.01 | 7.35 | -41.83 | 12.37 | -41.83 |
| C28-L157-003 | 030520 | 한글과컴퓨터 | 2024-05-14 | 30100.00 | AI-office theme without retention margin confirmation | counterexample | 10.96 | -26.74 | 10.96 | -49.83 | 10.96 | -49.83 |
| C28-L157-004 | 053800 | 안랩 | 2024-04-25 | 63600.00 | Stage2-Watch | counterexample | 4.72 | -4.09 | 4.72 | -18.87 | 40.57 | -20.28 |
| C28-L157-005 | 053800 | 안랩 | 2024-11-06 | 62500.00 | Stage2-Actionable | positive | 43.04 | -7.20 | 43.04 | -7.20 | 86.72 | -7.20 |
| C28-L157-006 | 047560 | 이스트소프트 | 2024-05-14 | 27850.00 | AI-human revenue growth but loss-making | counterexample | 10.23 | -34.11 | 10.23 | -59.71 | 10.23 | -59.71 |
| C28-L157-007 | 047560 | 이스트소프트 | 2024-11-12 | 14340.00 | Stage2-Watch positive with 4B overlay | positive_with_4B_overlay | 104.32 | -1.46 | 104.32 | -1.46 | 104.32 | -1.46 |
| C28-L157-008 | 434480 | 모니터랩 | 2024-04-24 | 6450.00 | SECaaS narrative but product sales collapse | counterexample | 1.71 | -17.83 | 1.71 | -54.26 | 1.71 | -56.90 |
| C28-L157-009 | 434480 | 모니터랩 | 2024-07-19 | 4250.00 | Cloud-security stable-service high-MAE watch | counterexample | 26.59 | -30.59 | 38.35 | -30.59 | 44.47 | -34.59 |
| C28-L157-010 | 041020 | 폴라리스오피스 | 2024-03-14 | 7330.00 | AI-office subscriber watch with exit guard | counterexample | 7.37 | -21.96 | 43.93 | -21.96 | 43.93 | -38.61 |
| C28-L157-011 | 041020 | 폴라리스오피스 | 2024-05-20 | 10120.00 | Revenue headline after theme blowoff | counterexample | 3.56 | -30.04 | 3.56 | -55.53 | 3.56 | -55.53 |
| C28-L157-012 | 205100 | 엑셈 | 2024-05-17 | 2490.00 | Stage2-Watch | counterexample | 5.82 | -12.85 | 5.82 | -35.10 | 5.82 | -35.10 |
| C28-L157-013 | 205100 | 엑셈 | 2025-03-24 | 1945.00 | Stage2-Actionable | positive | 16.20 | -7.51 | 29.56 | -7.51 | 33.16 | -7.51 |
| C28-L157-014 | 192250 | 케이사인 | 2025-03-21 | 7850.00 | Stage2-Watch positive with theme-risk overlay | positive_with_4B_overlay | 39.87 | -5.73 | 94.14 | -5.73 | 99.11 | -5.73 |

## 4. Interpretation by case

### 4.1 Positive retained-revenue / margin-conversion cases

**Douzone Bizon 2024-05-10** is the cleanest C28 positive in this batch. The event was not just an AI label: it combined ERP/Amaranth/WEHAGO installed-base monetization, operating-profit growth, and AI integration into existing enterprise software rails. The path produced high MFE across all windows while keeping 30D/90D MAE modest.

**AhnLab 2024-11-06** is a security-retention positive. The product family growth came from EDR/MDS/SOAR, not a generic cybersecurity headline, and the 180D price path showed strong upside with shallow drawdown.

**Exem 2025-03-24** is a confirmed software-license conversion case. APM, exemONE, enterprise customers, license revenue, and operating margin were all visible. This is the case type C28 should recognize earlier than a pure headline filter.

**ESTsoft 2024-11-12** and **KSign 2025-03-21** are not clean Green candidates, but they are useful Stage2-Watch positives. They show that reset-after-loss or PQC/security partnership rows can produce strong MFE if the price base has already been cleared. However, without proven recurring contract economics and margin conversion, they should keep a 4B overlay.

### 4.2 Counterexamples and residual errors

**Hancom 2024-05-14**, **Polaris Office 2024-05-20**, and **ESTsoft 2024-05-14** show the same trap: AI-office / AI-human vocabulary can be bright but brittle. If retained customer economics, renewal rates, ARR/contract backlog, or margin conversion are absent, the market can rip briefly and then fall through the floor.

**MonitorLab 2024-04-24 / 2024-07-19** is the security-cloud version of the same problem. SECaaS vocabulary and a cloud-service story were not enough while product sales and operating profit were under pressure.

**Douzone 2025-02-07** is the opposite edge case. The business quality was real, but the headline arrived after the rerating candle had already burned most of its oxygen. C28 needs a timing/4B exit guard even for good software names.

## 5. Trigger rows JSONL

```jsonl
{"MAE_180D_date": "2024-10-10", "MAE_180D_pct": -13.15, "MAE_30D_date": "2024-05-13", "MAE_30D_pct": -1.93, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -6.19, "MFE_180D_date": "2025-02-07", "MFE_180D_pct": 77.95, "MFE_30D_date": "2024-06-12", "MFE_30D_pct": 39.26, "MFE_90D_date": "2024-07-08", "MFE_90D_pct": 51.45, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-001", "company_name": "Douzone Bizon", "company_name_kr": "더존비즈온", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "underweights_C28_retained_revenue_margin_bridge", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|2|2024-05-10", "entry_date": "2024-05-10", "entry_price": 51700.0, "evidence_date": "2024-05-09", "evidence_title": "1Q24 revenue/OP growth; ERP/Amaranth/WEHAGO AI integration", "evidence_url": "https://www.newswire.co.kr/newsRead.php?no=989443", "fine_archetype_id": "ERP_SAAS_AI_RETAINED_CUSTOMER_MARGIN_BRIDGE", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Recurring ERP/SaaS installed base plus AI integration and OP growth aligned with clean 30/90/180D MFE.", "observed_path_label": "structural_positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 58, "capital_allocation": 50, "earnings_visibility": 74, "eps_fcf_explosion": 70, "information_confidence": 76, "market_mispricing": 62, "valuation_rerating": 58}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "aligned_positive", "ticker": "012510", "trigger_subtype": "Stage2-Actionable", "trigger_type": "2"}
{"MAE_180D_date": "2025-04-09", "MAE_180D_pct": -41.83, "MAE_30D_date": "2025-03-21", "MAE_30D_pct": -35.01, "MAE_90D_date": "2025-04-09", "MAE_90D_pct": -41.83, "MFE_180D_date": "2025-10-28", "MFE_180D_pct": 12.37, "MFE_30D_date": "2025-02-07", "MFE_30D_pct": 7.35, "MFE_90D_date": "2025-02-07", "MFE_90D_pct": 7.35, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-002", "company_name": "Douzone Bizon", "company_name_kr": "더존비즈온", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|4B|2025-02-07", "entry_date": "2025-02-07", "entry_price": 85700.0, "evidence_date": "2025-02-06", "evidence_title": "FY2024 record-growth / AI-service contribution headline", "evidence_url": "https://www.newswire.co.kr/newsRead.php?no=1006220", "fine_archetype_id": "ERP_SAAS_LATE_HEADLINE_HIGH_MAE", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Business quality was real, but late headline after rerating created a -40% drawdown window; C28 needs staged/4B exit guard.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "012510", "trigger_subtype": "Late record-profit headline high-MAE guard", "trigger_type": "4B"}
{"MAE_180D_date": "2024-08-05", "MAE_180D_pct": -49.83, "MAE_30D_date": "2024-06-25", "MAE_30D_pct": -26.74, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -49.83, "MFE_180D_date": "2024-05-21", "MFE_180D_pct": 10.96, "MFE_30D_date": "2024-05-21", "MFE_30D_pct": 10.96, "MFE_90D_date": "2024-05-21", "MFE_90D_pct": 10.96, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-003", "company_name": "Hancom", "company_name_kr": "한글과컴퓨터", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|030520|4B|2024-05-14", "entry_date": "2024-05-14", "entry_price": 30100.0, "evidence_date": "2024-05-13", "evidence_title": "1Q24 revenue/OP; AI new-business narrative", "evidence_url": "https://www.hellot.net/news/article.html?no=89756", "fine_archetype_id": "AI_OFFICE_THEME_ONEOFF_MARGIN_GAP", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Headline was not enough; price path showed large 90/180D MAE despite AI office vocabulary.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "030520", "trigger_subtype": "AI-office theme without retention margin confirmation", "trigger_type": "4B"}
{"MAE_180D_date": "2024-09-23", "MAE_180D_pct": -20.28, "MAE_30D_date": "2024-06-10", "MAE_30D_pct": -4.09, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -18.87, "MFE_180D_date": "2024-12-10", "MFE_180D_pct": 40.57, "MFE_30D_date": "2024-05-13", "MFE_30D_pct": 4.72, "MFE_90D_date": "2024-05-13", "MFE_90D_pct": 4.72, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-004", "company_name": "AhnLab", "company_name_kr": "안랩", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|2|2024-04-25", "entry_date": "2024-04-25", "entry_price": 63600.0, "evidence_date": "2024-04-24", "evidence_title": "1Q24 revenue but very low OP; security contract quality not enough for Actionable", "evidence_url": "https://www.ahnlab.com/kr/site/about/pressRoom/pressRoomView.do?seq=34746", "fine_archetype_id": "SECURITY_STABLE_REVENUE_LOW_OP_WATCH", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Stable security demand alone did not convert immediately into rerating; watch-only is safer.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "053800", "trigger_subtype": "Stage2-Watch", "trigger_type": "2"}
{"MAE_180D_date": "2024-11-25", "MAE_180D_pct": -7.2, "MAE_30D_date": "2024-11-25", "MAE_30D_pct": -7.2, "MAE_90D_date": "2024-11-25", "MAE_90D_pct": -7.2, "MFE_180D_date": "2025-04-07", "MFE_180D_pct": 86.72, "MFE_30D_date": "2024-12-10", "MFE_30D_pct": 43.04, "MFE_90D_date": "2024-12-10", "MFE_90D_pct": 43.04, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-005", "company_name": "AhnLab", "company_name_kr": "안랩", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "underweights_C28_retained_revenue_margin_bridge", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|2|2024-11-06", "entry_date": "2024-11-06", "entry_price": 62500.0, "evidence_date": "2024-11-05", "evidence_title": "3Q24 revenue/OP growth; EDR/MDS/SOAR contribution", "evidence_url": "https://blog.ahnlab.com/2802", "fine_archetype_id": "SECURITY_EDR_MDS_SOAR_RENEWAL_MARGIN_BRIDGE", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Security product growth and OP stability converted into strong 30/90/180D MFE with shallow MAE.", "observed_path_label": "structural_positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 58, "capital_allocation": 50, "earnings_visibility": 74, "eps_fcf_explosion": 70, "information_confidence": 76, "market_mispricing": 62, "valuation_rerating": 58}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "aligned_positive", "ticker": "053800", "trigger_subtype": "Stage2-Actionable", "trigger_type": "2"}
{"MAE_180D_date": "2024-08-05", "MAE_180D_pct": -59.71, "MAE_30D_date": "2024-06-25", "MAE_30D_pct": -34.11, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -59.71, "MFE_180D_date": "2024-05-16", "MFE_180D_pct": 10.23, "MFE_30D_date": "2024-05-16", "MFE_30D_pct": 10.23, "MFE_90D_date": "2024-05-16", "MFE_90D_pct": 10.23, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-006", "company_name": "ESTsoft", "company_name_kr": "이스트소프트", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|047560|4B|2024-05-14", "entry_date": "2024-05-14", "entry_price": 27850.0, "evidence_date": "2024-05-13", "evidence_title": "1Q24 revenue growth but operating loss remained", "evidence_url": "https://estsoft.ai/all/240513", "fine_archetype_id": "AI_HUMAN_LOSS_MAKING_THEME_BLOWOFF", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Revenue growth and loss narrowing did not prevent large drawdown; Stage2-Actionable should be blocked until margin bridge appears.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "047560", "trigger_subtype": "AI-human revenue growth but loss-making", "trigger_type": "4B"}
{"MAE_180D_date": "2024-11-12", "MAE_180D_pct": -1.46, "MAE_30D_date": "2024-11-12", "MAE_30D_pct": -1.46, "MAE_90D_date": "2024-11-12", "MAE_90D_pct": -1.46, "MFE_180D_date": "2024-12-13", "MFE_180D_pct": 104.32, "MFE_30D_date": "2024-12-13", "MFE_30D_pct": 104.32, "MFE_90D_date": "2024-12-13", "MFE_90D_pct": 104.32, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-007", "company_name": "ESTsoft", "company_name_kr": "이스트소프트", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "too_binary_loss_making_or_theme_overlay", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|047560|2|2024-11-12", "entry_date": "2024-11-12", "entry_price": 14340.0, "evidence_date": "2024-11-11", "evidence_title": "AI service sales, loss-narrowing / AI service growth follow-through", "evidence_url": "https://zdnet.co.kr/view/?no=20241111153334", "fine_archetype_id": "AI_SERVICE_LOSS_NARROWING_LOW_MAE_RELIEF", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "When the price base had reset and MAE was shallow, even loss-making AI software could produce a powerful relief path; still not Green until profit bridge.", "observed_path_label": "positive_but_requires_4B_exit_or_stage_gate", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 54, "capital_allocation": 45, "earnings_visibility": 58, "eps_fcf_explosion": 55, "information_confidence": 66, "market_mispricing": 60, "valuation_rerating": 47}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "mixed_positive_high_theme_risk", "ticker": "047560", "trigger_subtype": "Stage2-Watch positive with 4B overlay", "trigger_type": "2"}
{"MAE_180D_date": "2024-12-09", "MAE_180D_pct": -56.9, "MAE_30D_date": "2024-06-05", "MAE_30D_pct": -17.83, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -54.26, "MFE_180D_date": "2024-04-24", "MFE_180D_pct": 1.71, "MFE_30D_date": "2024-04-24", "MFE_30D_pct": 1.71, "MFE_90D_date": "2024-04-24", "MFE_90D_pct": 1.71, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-008", "company_name": "MonitorLab", "company_name_kr": "모니터랩", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|434480|4B|2024-04-24", "entry_date": "2024-04-24", "entry_price": 6450.0, "evidence_date": "2024-04-23", "evidence_title": "AIONCLOUD/SECaaS IR narrative, but product sales and OP weak", "evidence_url": "https://www.monitorapp.com/wp-content/uploads/2024/04/MonitorApp_IR_20240423.pdf", "fine_archetype_id": "SECURITY_SECAAS_PRODUCT_SALES_COLLAPSE", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Cloud-security vocabulary without revenue-quality bridge caused a severe 90/180D drawdown.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "434480", "trigger_subtype": "SECaaS narrative but product sales collapse", "trigger_type": "4B"}
{"MAE_180D_date": "2024-12-09", "MAE_180D_pct": -34.59, "MAE_30D_date": "2024-08-05", "MAE_30D_pct": -30.59, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -30.59, "MFE_180D_date": "2025-02-06", "MFE_180D_pct": 44.47, "MFE_30D_date": "2024-07-22", "MFE_30D_pct": 26.59, "MFE_90D_date": "2024-09-25", "MFE_90D_pct": 38.35, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-009", "company_name": "MonitorLab", "company_name_kr": "모니터랩", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|434480|4B|2024-07-19", "entry_date": "2024-07-19", "entry_price": 4250.0, "evidence_date": "2024-07-18", "evidence_title": "Cloud service stable but product revenue and OP pressure persisted", "evidence_url": "https://www.boannews.com/media/view.asp?idx=131153", "fine_archetype_id": "SECURITY_SECAAS_STABLE_SERVICE_HIGH_MAE", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "A 30/90D bounce did not erase high MAE; C28 should require retained economics plus margin bridge, not only SECaaS narrative.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "434480", "trigger_subtype": "Cloud-security stable-service high-MAE watch", "trigger_type": "4B"}
{"MAE_180D_date": "2024-08-05", "MAE_180D_pct": -38.61, "MAE_30D_date": "2024-04-11", "MAE_30D_pct": -21.96, "MAE_90D_date": "2024-04-11", "MAE_90D_pct": -21.96, "MFE_180D_date": "2024-05-14", "MFE_180D_pct": 43.93, "MFE_30D_date": "2024-03-19", "MFE_30D_pct": 7.37, "MFE_90D_date": "2024-05-14", "MFE_90D_pct": 43.93, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-010", "company_name": "Polaris Office", "company_name_kr": "폴라리스오피스", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|041020|2|2024-03-14", "entry_date": "2024-03-14", "entry_price": 7330.0, "evidence_date": "2024-03-13", "evidence_title": "AI office / paid subscriber expansion thesis", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1710289091656.pdf", "fine_archetype_id": "AI_OFFICE_SUBSCRIBER_WATCH_HIGH_MAE", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Early MFE existed, but later drawdown was deep; exit guard matters for AI office subscription themes.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "041020", "trigger_subtype": "AI-office subscriber watch with exit guard", "trigger_type": "2"}
{"MAE_180D_date": "2024-08-05", "MAE_180D_pct": -55.53, "MAE_30D_date": "2024-06-25", "MAE_30D_pct": -30.04, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -55.53, "MFE_180D_date": "2024-05-20", "MFE_180D_pct": 3.56, "MFE_30D_date": "2024-05-20", "MFE_30D_pct": 3.56, "MFE_90D_date": "2024-05-20", "MFE_90D_pct": 3.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-011", "company_name": "Polaris Office", "company_name_kr": "폴라리스오피스", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|041020|4B|2024-05-20", "entry_date": "2024-05-20", "entry_price": 10120.0, "evidence_date": "2024-05-17", "evidence_title": "1Q24 sales/OP headline, cloud service and global subscribers", "evidence_url": "https://www.ciokorea.com/news/338376", "fine_archetype_id": "AI_OFFICE_REVENUE_HEADLINE_LATE_BLOWOFF", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "Later confirmation came after price oxygen was exhausted; the 90/180D path was dominated by drawdown.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "041020", "trigger_subtype": "Revenue headline after theme blowoff", "trigger_type": "4B"}
{"MAE_180D_date": "2024-08-05", "MAE_180D_pct": -35.1, "MAE_30D_date": "2024-06-28", "MAE_30D_pct": -12.85, "MAE_90D_date": "2024-08-05", "MAE_90D_pct": -35.1, "MFE_180D_date": "2024-05-17", "MFE_180D_pct": 5.82, "MFE_30D_date": "2024-05-17", "MFE_30D_pct": 5.82, "MFE_90D_date": "2024-05-17", "MFE_90D_pct": 5.82, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-012", "company_name": "Exem", "company_name_kr": "엑셈", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "C28_theme_or_headline_can_still_get_too_much_stage2_credit", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|205100|2|2024-05-17", "entry_date": "2024-05-17", "entry_price": 2490.0, "evidence_date": "2024-05-16", "evidence_title": "1Q24 weak/loss phase before confirmed license run-rate", "evidence_url": "https://www.newswire.co.kr/newsRead.php?no=989805", "fine_archetype_id": "APM_AIOPS_Q1_LOSS_WATCH", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "APM/AIOps concept was not enough before license run-rate and profit bridge became visible.", "observed_path_label": "counterexample_high_MAE_or_no_conversion", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 46, "capital_allocation": 40, "earnings_visibility": 42, "eps_fcf_explosion": 38, "information_confidence": 60, "market_mispricing": 35, "valuation_rerating": 32}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "false_positive_risk", "ticker": "205100", "trigger_subtype": "Stage2-Watch", "trigger_type": "2"}
{"MAE_180D_date": "2025-03-31", "MAE_180D_pct": -7.51, "MAE_30D_date": "2025-03-31", "MAE_30D_pct": -7.51, "MAE_90D_date": "2025-03-31", "MAE_90D_pct": -7.51, "MFE_180D_date": "2025-09-12", "MFE_180D_pct": 33.16, "MFE_30D_date": "2025-04-24", "MFE_30D_pct": 16.2, "MFE_90D_date": "2025-07-11", "MFE_90D_pct": 29.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-013", "company_name": "Exem", "company_name_kr": "엑셈", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "none", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|205100|2|2025-03-24", "entry_date": "2025-03-24", "entry_price": 1945.0, "evidence_date": "2025-03-21", "evidence_title": "FY2024 record revenue/OP; APM/exemONE license growth", "evidence_url": "https://www.newswire.co.kr/newsRead.php?no=1007955", "fine_archetype_id": "APM_AIOPS_LICENSE_REVENUE_MARGIN_BRIDGE", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "License revenue, recurring enterprise customers, and margin conversion aligned with clean 30/90/180D MFE.", "observed_path_label": "structural_positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 58, "capital_allocation": 50, "earnings_visibility": 74, "eps_fcf_explosion": 70, "information_confidence": 76, "market_mispricing": 62, "valuation_rerating": 58}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "aligned_positive", "ticker": "205100", "trigger_subtype": "Stage2-Actionable", "trigger_type": "2"}
{"MAE_180D_date": "2025-03-31", "MAE_180D_pct": -5.73, "MAE_30D_date": "2025-03-31", "MAE_30D_pct": -5.73, "MAE_90D_date": "2025-03-31", "MAE_90D_pct": -5.73, "MFE_180D_date": "2025-09-24", "MFE_180D_pct": 99.11, "MFE_30D_date": "2025-04-29", "MFE_30D_pct": 39.87, "MFE_90D_date": "2025-06-13", "MFE_90D_pct": 94.14, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-014", "company_name": "KSign", "company_name_kr": "케이사인", "corporate_action_contamination_180D": "profile_checked_no_overlap_or_no_candidate_in_entry_180D_window", "current_profile_error_type": "too_binary_loss_making_or_theme_overlay", "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|192250|2|2025-03-21", "entry_date": "2025-03-21", "entry_price": 7850.0, "evidence_date": "2025-03-20", "evidence_title": "PQC joint-development / cryptography-security partnership", "evidence_url": "https://www.dailysecu.com/news/articleView.html?idxno=165468", "fine_archetype_id": "PQC_SECURITY_PARTNERSHIP_THEME_WITH_MARGIN_RISK", "is_representative_for_aggregate": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "note": "PQC/security partnership produced strong MFE after a reset, but should stay Watch until contract/revenue/margin conversion is visible.", "observed_path_label": "positive_but_requires_4B_exit_or_stage_gate", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing_power": 54, "capital_allocation": 45, "earnings_visibility": 58, "eps_fcf_explosion": 55, "information_confidence": 66, "market_mispricing": 60, "valuation_rerating": 47}, "row_type": "trigger_row", "schema_version": "stock_web_v12_residual_research_v1", "score_return_alignment": "mixed_positive_high_theme_risk", "ticker": "192250", "trigger_subtype": "Stage2-Watch positive with theme-risk overlay", "trigger_type": "2"}
```

## 6. Score simulation rows JSONL

```jsonl
{"MAE_180D_pct": -13.15, "MFE_180D_pct": 77.95, "backtest_alignment": "aligned_positive", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-001", "post_shadow_expected_stage": "2 or 3-Yellow candidate", "pre_shadow_total_proxy": 64.0, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "+2 Stage2 bridge when retained-revenue/renewal or enterprise contract plus margin bridge is visible", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "012510"}
{"MAE_180D_pct": -41.83, "MFE_180D_pct": 12.37, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-002", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "012510"}
{"MAE_180D_pct": -49.83, "MFE_180D_pct": 10.96, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-003", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "030520"}
{"MAE_180D_pct": -20.28, "MFE_180D_pct": 40.57, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-004", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "053800"}
{"MAE_180D_pct": -7.2, "MFE_180D_pct": 86.72, "backtest_alignment": "aligned_positive", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-005", "post_shadow_expected_stage": "2 or 3-Yellow candidate", "pre_shadow_total_proxy": 64.0, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "+2 Stage2 bridge when retained-revenue/renewal or enterprise contract plus margin bridge is visible", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "053800"}
{"MAE_180D_pct": -59.71, "MFE_180D_pct": 10.23, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-006", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "047560"}
{"MAE_180D_pct": -1.46, "MFE_180D_pct": 104.32, "backtest_alignment": "mixed_positive_high_theme_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-007", "post_shadow_expected_stage": "2-Watch / 4B overlay", "pre_shadow_total_proxy": 55.0, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "+1 watch-only bridge with 4B exit guard; no Green until profit/contract conversion", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "047560"}
{"MAE_180D_pct": -56.9, "MFE_180D_pct": 1.71, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-008", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "434480"}
{"MAE_180D_pct": -34.59, "MFE_180D_pct": 44.47, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-009", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "434480"}
{"MAE_180D_pct": -38.61, "MFE_180D_pct": 43.93, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-010", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "041020"}
{"MAE_180D_pct": -55.53, "MFE_180D_pct": 3.56, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-011", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "041020"}
{"MAE_180D_pct": -35.1, "MFE_180D_pct": 5.82, "backtest_alignment": "false_positive_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-012", "post_shadow_expected_stage": "2-Watch or 4B/4C-Watch", "pre_shadow_total_proxy": 41.86, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "-2 to -4 theme-only or loss-making penalty; require retained economics before Stage2-Actionable", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "205100"}
{"MAE_180D_pct": -7.51, "MFE_180D_pct": 33.16, "backtest_alignment": "aligned_positive", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-013", "post_shadow_expected_stage": "2 or 3-Yellow candidate", "pre_shadow_total_proxy": 64.0, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "+2 Stage2 bridge when retained-revenue/renewal or enterprise contract plus margin bridge is visible", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "205100"}
{"MAE_180D_pct": -5.73, "MFE_180D_pct": 99.11, "backtest_alignment": "mixed_positive_high_theme_risk", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-L157-014", "post_shadow_expected_stage": "2-Watch / 4B overlay", "pre_shadow_total_proxy": 55.0, "row_type": "score_simulation_row", "shadow_adjustment_recommendation": "+1 watch-only bridge with 4B exit guard; no Green until profit/contract conversion", "shadow_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "ticker": "192250"}
```

## 7. Aggregate row JSONL

```jsonl
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "canonical_archetype_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2", "counterexample_count": 9, "current_profile_error_count": 9, "do_not_propose_new_weight_delta": false, "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_should_not_fire_on_loss_narrowing_or_single_theme_drawdown_alone", "index_baseline_coverage_after_if_accepted": 42, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "need_to_50_after_session_aware": 0, "new_axis_proposed": "c28_recurring_contract_retention_margin_and_ai_theme_exit_gate_v2", "new_independent_case_count": 8, "next_recommended_archetypes": ["C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "C19_BRAND_RETAIL_INVENTORY_MARGIN", "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"], "original_index_rows": 28, "positive_case_count": 5, "representative_trigger_count": 14, "row_type": "aggregate_row", "schema_version": "stock_web_v12_residual_research_v1", "sector_specific_rule_candidate": "L8_SOFTWARE_SECURITY_RETAINED_REVENUE_MARGIN_AND_THEME_EXIT_GATE_V2", "selected_loop": 157, "selected_priority_bucket": "session-aware Priority 1; original Index Priority 0", "selected_round": "R8", "session_aware_after_loop133_loop157_if_accepted": 51, "session_aware_rows_before_loop157_after_loop133": 37, "stage4b_watch_or_overlay_count": 9, "stage4c_watch_count": 3, "usable_trigger_row_count": 14}
```

## 8. Shadow rule candidate

```text
canonical_archetype_rule_candidate = C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2
```

### Proposed rule logic

C28 should not grant Stage2-Actionable merely because a company is tagged with `AI`, `cybersecurity`, `SaaS`, `PQC`, `cloud`, or `enterprise software`.

Stage2-Actionable should require at least one **retained-economics bridge** and one **conversion bridge**.

```text
retained_economics_bridge:
  - maintenance / renewal revenue
  - ARR / subscription / SaaS run-rate
  - named enterprise customer expansion
  - installed-base monetization
  - software-license repeatability
  - security product retention or replacement cycle

conversion_bridge:
  - operating profit or margin expansion
  - license revenue growth with low variable cost
  - deferred / recurring revenue growth
  - contract backlog or order visibility
  - revision / guidance bridge
```

If a row only has theme vocabulary, forecast language, partnership language, or one-quarter revenue growth without profit or retained-customer proof, it should remain `Stage2-Watch` or be routed to local `4B` when price has already extended.

### 4B / 4C nuance

C28 should not immediately hard-4C a loss-making AI software/security company merely because one quarter remains loss-making or the first post-theme drawdown is large. Some rows, such as ESTsoft 2024-11 and KSign 2025-03, produced large MFE after a reset. The right guardrail is:

```text
if theme_loss_making == true and retained_economics_bridge == false:
    stage = Stage2-Watch
    attach_4B_exit_guard = true
    block_Stage3_Green = true

if price_extension_large == true and evidence_is_late_confirmation == true:
    stage = local_4B_watch
    require_staged_entry = true

if product_contract_retention + margin_bridge are both confirmed:
    allow Stage2-Actionable or Stage3-Yellow candidate
```

## 9. Current calibrated profile residual contribution

The current calibrated profile already blocks many price-only blowoffs, but C28 still has a sector-specific residual error: it can over-credit words that sound structurally sticky even when the revenue is not yet retained or converted into margin. Software vocabulary behaves like a clean coat of paint; the rule must still inspect the building frame underneath.

Residual contribution of this loop:

```yaml
new_axis_proposed: c28_recurring_contract_retention_margin_and_ai_theme_exit_gate_v2
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_on_loss_narrowing_or_single_theme_drawdown_alone
positive_case_count: 5
counterexample_count: 9
stage4b_watch_or_overlay_count: 9
current_profile_error_count: 9
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session. It is provided for a later coding/batch-ingest session.

```text
You are the coding agent for stock_agent E2R calibration ingestion.

Input artifact:
- e2r_stock_web_v12_residual_round_R8_loop_157_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

Tasks:
1. Parse every trigger_row JSONL object.
2. Validate that each row includes complete 30D/90D/180D MFE/MAE fields.
3. Validate standard v12 filename and metadata consistency.
4. Deduplicate by canonical_archetype_id + ticker + trigger_type + entry_date.
5. Add the representative rows to the v12 calibration candidate set only if stock-web price basis and corporate-action checks pass.
6. Evaluate the shadow rule candidate `C28_RECURRING_CONTRACT_RETENTION_MARGIN_AND_AI_THEME_EXIT_GATE_V2` in shadow mode only.
7. Do not loosen Stage3-Green global thresholds.
8. If applying any future patch, apply it as canonical-archetype-specific C28 logic, not as a global AI/software boost.
```

## 11. Next research state

```text
completed_round = R8
completed_loop = 157
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = session-aware Priority 1; original Index Priority 0
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C19_BRAND_RETAIL_INVENTORY_MARGIN | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
