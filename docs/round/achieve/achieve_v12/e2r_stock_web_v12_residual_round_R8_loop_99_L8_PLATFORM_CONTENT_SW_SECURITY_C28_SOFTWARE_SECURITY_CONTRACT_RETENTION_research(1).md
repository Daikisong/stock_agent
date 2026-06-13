# E2R Stock-Web v12 Residual Research — R8 loop 99 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 99
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: mixed_C28_verified_retention_arr_opm_bridge_and_security_label_decontamination_set
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
  - sector_specific_rule_discovery
  - verified_url_repair
loop_contribution_label: canonical_archetype_rule_candidate
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows; C28 had 28 rows and needed 2 to reach the 30-row minimum stability zone
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
standard_filename: e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
```

## 1. Scope

This file is a standalone historical calibration note for `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION`. The objective is not to prove again that software/security labels are useful. The objective is to split verified recurring software revenue and margin bridge from labels that sound recurring but fail at retention, ARR, renewal, OPM, or business-mix purity.

C28 behaves like a subscription turnstile. A customer passing through once is not enough; the model needs to see whether the same gate keeps clicking every month with paid seats, renewal, maintenance, cloud/SaaS revenue, margin, and FCF behind it.

## 2. Price source validation

```jsonl
{"row_type": "price_source_validation", "price_atlas_repo": "Songdaiki/stock-web", "manifest": "atlas/manifest.json", "source_name": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "schema_MFE": "max high from entry_date through N tradable rows / entry_price - 1", "schema_MAE": "min low from entry_date through N tradable rows / entry_price - 1", "symbol_set": ["012510", "030520", "053800", "434480", "203650"], "profile_corporate_action_window_check": "012510 historical CA dates 2002/2006/2009 only; 030520 historical CA dates through 2006 only; 053800 historical CA date 2005 only; 434480 no CA candidates; 203650 CA dates 2017/2019/2025-11/2025-12 outside selected 2024 180D window.", "notes": "Raw/unadjusted OHLC. No selected 180D calibration window overlaps a corporate-action candidate date. 1Y/2Y fields intentionally omitted."}
```

## 3. Novelty / no-repeat check

- `V12_Research_No_Repeat_Index.md` marks `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` as Priority 0 with 28 rows, 2 rows short of the 30-row floor.
- Existing compact C28 work at R8 loop 98 used 030520 / 079940 / 053800 / 053300 with source_proxy_only and evidence_url_pending flags. This loop uses `R8 loop 99`, adds three new symbols, and repairs C28 with verified non-price evidence URLs.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`. Reused symbols 030520 and 053800 use different trigger dates, different entry dates, and URL-verified evidence families.
- New symbols in this MD: 012510, 434480, 203650. Reused-with-new-trigger symbols: 030520, 053800.

## 4. Case table

| case_id | symbol | name | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | class |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C28-R8L99-01 | 012510 | 더존비즈온 | Stage3-Yellow | 2025-04-14 | 2025-04-15 | 61900 | 9.85% | -11.95% | 38.93% | -12.28% | 60.90% | -12.28% | 2025-12-05 | 99600 | -18.78% | positive |
| C28-R8L99-02 | 030520 | 한글과컴퓨터 | Stage3-Yellow | 2024-08-08 | 2024-08-09 | 17320 | 17.78% | -2.94% | 54.45% | -2.94% | 54.45% | -2.94% | 2024-12-02 | 26750 | -35.21% | positive |
| C28-R8L99-03 | 053800 | 안랩 | Stage3-Yellow | 2024-11-06 | 2024-11-07 | 63200 | 41.46% | -8.23% | 41.46% | -8.23% | 84.65% | -8.23% | 2025-04-07 | 116700 | -49.10% | counterexample_4B_guard |
| C28-R8L99-04 | 434480 | 모니터랩 | 4B | 2024-07-18 | 2024-07-19 | 4250 | 26.59% | -30.59% | 38.35% | -30.59% | 44.47% | -34.59% | 2025-02-06 | 6140 | -43.81% | counterexample |
| C28-R8L99-05 | 203650 | 드림시큐리티 | Stage2 | 2024-03-20 | 2024-03-21 | 3710 | 2.43% | -15.09% | 2.43% | -25.88% | 7.68% | -38.41% | 2024-12-12 | 3995 | -11.14% | counterexample |

## 5. Evidence notes

### C28-R8L99-01 — 012510 더존비즈온
- Evidence URL: https://www.shinyoung.com/files/20250414/9b89da7d21644.pdf
- Evidence summary: WEHAGO/Amaranth 10 SaaS 전환, Lite ERP 온프레미스 지원 종료, 클라우드 전환 고객수 확대, 내재화된 D-클라우드 기반 영업레버리지, 2025 매출·영업이익 전망이 함께 확인된 verified recurring-revenue bridge.
- Price path: entry `2025-04-15` close `61900`; 180D MFE `60.90%`, 180D MAE `-12.28%`; peak `2025-12-05` `99600`; post-peak drawdown `-18.78%`.

### C28-R8L99-02 — 030520 한글과컴퓨터
- Evidence URL: https://www.hancom.com/news/article/detail/12090
- Evidence summary: 클라우드 SaaS 기반 제품군 매출 증가, 별도 매출·영업이익 동반 성장, 클라우드/웹 기반 제품군 매출 비중 상승이 공식 보도자료에서 확인된 positive bridge.
- Price path: entry `2024-08-09` close `17320`; 180D MFE `54.45%`, 180D MAE `-2.94%`; peak `2024-12-02` `26750`; post-peak drawdown `-35.21%`.

### C28-R8L99-03 — 053800 안랩
- Evidence URL: https://blog.ahnlab.com/2802
- Evidence summary: Q3 매출·영업이익 증가와 EDR/MDS/SOAR 성장 언급은 C28 Stage3-Yellow 후보를 만들지만, 180D peak 이후 -49% drawdown이 커서 full Green보다 local 4B/valuation guard가 필요하다.
- Price path: entry `2024-11-07` close `63200`; 180D MFE `84.65%`, 180D MAE `-8.23%`; peak `2025-04-07` `116700`; post-peak drawdown `-49.10%`.

### C28-R8L99-04 — 434480 모니터랩
- Evidence URL: https://m.boannews.com/html/detail.html?idx=131425
- Evidence summary: SECaaS/cloud-security 비중 확대는 확인되지만 2023 매출 목표 미달, 1Q24 적자, 제품 매출 감소와 수주 부진이 함께 확인되어 Stage3가 아니라 4B/local watch로 눌러야 하는 row.
- Price path: entry `2024-07-19` close `4250`; 180D MFE `44.47%`, 180D MAE `-34.59%`; peak `2025-02-06` `6140`; post-peak drawdown `-43.81%`.

### C28-R8L99-05 — 203650 드림시큐리티
- Evidence URL: https://www.dreamsecurity.com/contents/attachments/2024/03/%5B%EB%93%9C%EB%A6%BC%EC%8B%9C%ED%81%90%EB%A6%AC%ED%8B%B0%5D%EC%82%AC%EC%97%85%EB%B3%B4%EA%B3%A0%EC%84%9C_%EC%97%B0%EA%B2%B0%EA%B0%90%EC%82%AC%EB%B3%B4%EA%B3%A0%EC%84%9C_%EA%B0%90%EC%82%AC%EB%B3%B4%EA%B3%A0%EC%84%9C%282024.03.20%29.pdf
- Evidence summary: 정보보안/인증솔루션은 존재하지만 연결 매출 대부분이 렌탈부문이라는 mix contamination이 커서 C28 retention pure-play로 올리면 안 되는 decontamination counterexample.
- Price path: entry `2024-03-21` close `3710`; 180D MFE `7.68%`, 180D MAE `-38.41%`; peak `2024-12-12` `3995`; post-peak drawdown `-11.14%`.

## 6. Usable trigger rows JSONL

```jsonl
{"case_id": "C28-R8L99-01", "symbol": "012510", "name": "더존비즈온", "trigger_date": "2025-04-14", "entry_date": "2025-04-15", "entry_price": 61900.0, "trigger_type": "Stage3-Yellow", "fine_trigger_family": "ERP_CLOUD_AI_RECURRING_REVENUE_MARGIN_BRIDGE_VERIFIED", "MFE_30D_pct": 9.85, "MAE_30D_pct": -11.95, "peak_30D_date": "2025-04-18", "peak_30D_price": 68000.0, "trough_30D_date": "2025-05-26", "trough_30D_price": 54500.0, "window_30D_end_date": "2025-05-29", "MFE_90D_pct": 38.93, "MAE_90D_pct": -12.28, "peak_90D_date": "2025-07-16", "peak_90D_price": 86000.0, "trough_90D_date": "2025-06-02", "trough_90D_price": 54300.0, "window_90D_end_date": "2025-08-26", "MFE_180D_pct": 60.9, "MAE_180D_pct": -12.28, "peak_180D_date": "2025-12-05", "peak_180D_price": 99600.0, "trough_180D_date": "2025-06-02", "trough_180D_price": 54300.0, "window_180D_end_date": "2026-01-09", "peak_date": "2025-12-05", "peak_price": 99600.0, "drawdown_after_peak_pct": -18.78, "drawdown_trough_date": "2025-12-18", "drawdown_trough_price": 80900.0, "source_url": "https://www.shinyoung.com/files/20250414/9b89da7d21644.pdf", "evidence_summary": "WEHAGO/Amaranth 10 SaaS 전환, Lite ERP 온프레미스 지원 종료, 클라우드 전환 고객수 확대, 내재화된 D-클라우드 기반 영업레버리지, 2025 매출·영업이익 전망이 함께 확인된 verified recurring-revenue bridge.", "case_class": "positive", "current_profile_expected_stage": "Stage3-Yellow", "residual_flag": "retention_ARR_OPM_bridge_confirms_C28_not_theme_only", "row_type": "trigger", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "corporate_action_contaminated": false, "insufficient_forward_window": false, "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage3-Yellow|2025-04-15"}
{"case_id": "C28-R8L99-02", "symbol": "030520", "name": "한글과컴퓨터", "trigger_date": "2024-08-08", "entry_date": "2024-08-09", "entry_price": 17320.0, "trigger_type": "Stage3-Yellow", "fine_trigger_family": "CLOUD_SAAS_AI_OFFICE_REVENUE_OPM_BRIDGE_VERIFIED", "MFE_30D_pct": 17.78, "MAE_30D_pct": -2.94, "peak_30D_date": "2024-08-22", "peak_30D_price": 20400.0, "trough_30D_date": "2024-09-09", "trough_30D_price": 16810.0, "window_30D_end_date": "2024-09-25", "MFE_90D_pct": 54.45, "MAE_90D_pct": -2.94, "peak_90D_date": "2024-12-02", "peak_90D_price": 26750.0, "trough_90D_date": "2024-09-09", "trough_90D_price": 16810.0, "window_90D_end_date": "2024-12-23", "MFE_180D_pct": 54.45, "MAE_180D_pct": -2.94, "peak_180D_date": "2024-12-02", "peak_180D_price": 26750.0, "trough_180D_date": "2024-09-09", "trough_180D_price": 16810.0, "window_180D_end_date": "2025-05-13", "peak_date": "2024-12-02", "peak_price": 26750.0, "drawdown_after_peak_pct": -35.21, "drawdown_trough_date": "2025-04-07", "drawdown_trough_price": 17330.0, "source_url": "https://www.hancom.com/news/article/detail/12090", "evidence_summary": "클라우드 SaaS 기반 제품군 매출 증가, 별도 매출·영업이익 동반 성장, 클라우드/웹 기반 제품군 매출 비중 상승이 공식 보도자료에서 확인된 positive bridge.", "case_class": "positive", "current_profile_expected_stage": "Stage3-Yellow", "residual_flag": "cloud_SaaS_revenue_OPM_bridge_worked_but_peak_drawdown_requires_4B_watch", "row_type": "trigger", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "corporate_action_contaminated": false, "insufficient_forward_window": false, "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|030520|Stage3-Yellow|2024-08-09"}
{"case_id": "C28-R8L99-03", "symbol": "053800", "name": "안랩", "trigger_date": "2024-11-06", "entry_date": "2024-11-07", "entry_price": 63200.0, "trigger_type": "Stage3-Yellow", "fine_trigger_family": "EDR_MDS_SOAR_SECURITY_PRODUCT_GROWTH_WITH_BLOWOFF_GUARD", "MFE_30D_pct": 41.46, "MAE_30D_pct": -8.23, "peak_30D_date": "2024-12-10", "peak_30D_price": 89400.0, "trough_30D_date": "2024-11-25", "trough_30D_price": 58000.0, "window_30D_end_date": "2024-12-18", "MFE_90D_pct": 41.46, "MAE_90D_pct": -8.23, "peak_90D_date": "2024-12-10", "peak_90D_price": 89400.0, "trough_90D_date": "2024-11-25", "trough_90D_price": 58000.0, "window_90D_end_date": "2025-03-24", "MFE_180D_pct": 84.65, "MAE_180D_pct": -8.23, "peak_180D_date": "2025-04-07", "peak_180D_price": 116700.0, "trough_180D_date": "2024-11-25", "trough_180D_price": 58000.0, "window_180D_end_date": "2025-08-04", "peak_date": "2025-04-07", "peak_price": 116700.0, "drawdown_after_peak_pct": -49.1, "drawdown_trough_date": "2025-05-19", "drawdown_trough_price": 59400.0, "source_url": "https://blog.ahnlab.com/2802", "evidence_summary": "Q3 매출·영업이익 증가와 EDR/MDS/SOAR 성장 언급은 C28 Stage3-Yellow 후보를 만들지만, 180D peak 이후 -49% drawdown이 커서 full Green보다 local 4B/valuation guard가 필요하다.", "case_class": "counterexample_4B_guard", "current_profile_expected_stage": "Stage3-Yellow_with_4B_guard", "residual_flag": "security_product_growth_can_work_but_peak_blowoff_and_non_retention_noise_need_guard", "row_type": "trigger", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "corporate_action_contaminated": false, "insufficient_forward_window": false, "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|Stage3-Yellow|2024-11-07"}
{"case_id": "C28-R8L99-04", "symbol": "434480", "name": "모니터랩", "trigger_date": "2024-07-18", "entry_date": "2024-07-19", "entry_price": 4250.0, "trigger_type": "4B", "fine_trigger_family": "SECAAS_CLOUD_SECURITY_SHARE_RISING_BUT_LOSS_ORDER_DELAY", "MFE_30D_pct": 26.59, "MAE_30D_pct": -30.59, "peak_30D_date": "2024-07-22", "peak_30D_price": 5380.0, "trough_30D_date": "2024-08-05", "trough_30D_price": 2950.0, "window_30D_end_date": "2024-08-30", "MFE_90D_pct": 38.35, "MAE_90D_pct": -30.59, "peak_90D_date": "2024-09-25", "peak_90D_price": 5880.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 2950.0, "window_90D_end_date": "2024-12-02", "MFE_180D_pct": 44.47, "MAE_180D_pct": -34.59, "peak_180D_date": "2025-02-06", "peak_180D_price": 6140.0, "trough_180D_date": "2024-12-09", "trough_180D_price": 2780.0, "window_180D_end_date": "2025-04-17", "peak_date": "2025-02-06", "peak_price": 6140.0, "drawdown_after_peak_pct": -43.81, "drawdown_trough_date": "2025-04-09", "drawdown_trough_price": 3450.0, "source_url": "https://m.boannews.com/html/detail.html?idx=131425", "evidence_summary": "SECaaS/cloud-security 비중 확대는 확인되지만 2023 매출 목표 미달, 1Q24 적자, 제품 매출 감소와 수주 부진이 함께 확인되어 Stage3가 아니라 4B/local watch로 눌러야 하는 row.", "case_class": "counterexample", "current_profile_expected_stage": "4B", "residual_flag": "cloud_security_share_without_order_OPM_bridge_produces_high_MAE", "row_type": "trigger", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "corporate_action_contaminated": false, "insufficient_forward_window": false, "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|434480|4B|2024-07-19"}
{"case_id": "C28-R8L99-05", "symbol": "203650", "name": "드림시큐리티", "trigger_date": "2024-03-20", "entry_date": "2024-03-21", "entry_price": 3710.0, "trigger_type": "Stage2", "fine_trigger_family": "SECURITY_IDENTITY_LABEL_DECONTAMINATED_BY_RENTAL_MIX_AND_OPM_FADE", "MFE_30D_pct": 2.43, "MAE_30D_pct": -15.09, "peak_30D_date": "2024-03-27", "peak_30D_price": 3800.0, "trough_30D_date": "2024-04-16", "trough_30D_price": 3150.0, "window_30D_end_date": "2024-05-03", "MFE_90D_pct": 2.43, "MAE_90D_pct": -25.88, "peak_90D_date": "2024-03-27", "peak_90D_price": 3800.0, "trough_90D_date": "2024-07-25", "trough_90D_price": 2750.0, "window_90D_end_date": "2024-07-31", "MFE_180D_pct": 7.68, "MAE_180D_pct": -38.41, "peak_180D_date": "2024-12-12", "peak_180D_price": 3995.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 2285.0, "window_180D_end_date": "2024-12-13", "peak_date": "2024-12-12", "peak_price": 3995.0, "drawdown_after_peak_pct": -11.14, "drawdown_trough_date": "2024-12-13", "drawdown_trough_price": 3550.0, "source_url": "https://www.dreamsecurity.com/contents/attachments/2024/03/%5B%EB%93%9C%EB%A6%BC%EC%8B%9C%ED%81%90%EB%A6%AC%ED%8B%B0%5D%EC%82%AC%EC%97%85%EB%B3%B4%EA%B3%A0%EC%84%9C_%EC%97%B0%EA%B2%B0%EA%B0%90%EC%82%AC%EB%B3%B4%EA%B3%A0%EC%84%9C_%EA%B0%90%EC%82%AC%EB%B3%B4%EA%B3%A0%EC%84%9C%282024.03.20%29.pdf", "evidence_summary": "정보보안/인증솔루션은 존재하지만 연결 매출 대부분이 렌탈부문이라는 mix contamination이 커서 C28 retention pure-play로 올리면 안 되는 decontamination counterexample.", "case_class": "counterexample", "current_profile_expected_stage": "Stage2_or_block", "residual_flag": "security_label_contaminated_by_non_C28_revenue_mix", "row_type": "trigger", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false, "corporate_action_contaminated": false, "insufficient_forward_window": false, "dedupe_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|203650|Stage2|2024-03-21"}
```

## 7. Score-return alignment

### 7.1 Positive bridge rows

`012510` and `030520` are constructive C28 rows. Their non-price evidence is not just a software label: it ties product conversion to cloud/SaaS revenue, AI adoption, operating margin, and repeat customer base. Their 180D paths were also consistent with positive calibration: `012510` produced 60.90% MFE with -12.28% MAE, while `030520` produced 54.45% MFE with only -2.94% MAE.

### 7.2 4B / blowoff guard row

`053800` shows why C28 should not be a blind Green bucket. Product growth in EDR/MDS/SOAR was real enough to create a Stage3-Yellow candidate, but the full-window path later had an 84.65% MFE followed by a -49.10% post-peak drawdown. C28 needs a local 4B guard when security product evidence is not paired with retention/ARR disclosure and the path becomes valuation or external-noise driven.

### 7.3 Counterexample rows

`434480` and `203650` are counterexamples. `434480` had rising cloud-security share, but the evidence simultaneously showed missed sales, operating loss, and order delay; the path carried -34.59% 180D MAE. `203650` had security/authentication language, but the business mix was dominated by non-C28 rental revenue and the 180D path had just 7.68% MFE against -38.41% MAE.

## 8. Current calibrated profile stress test

The current global calibrated profile already blocks price-only blowoff and asks for Stage2 bridge evidence. C28 needs a narrower sector/archetype version of the same idea: software/security words should be treated as labels until renewal, paid-seat expansion, ARR/maintenance revenue, gross retention, churn control, OPM, FCF, or EPS revision connects the label to durable economics.

```jsonl
{"row_type": "current_profile_stress_test", "scope": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "current_global_rules_tested": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error": "C28 still needs an archetype-specific bridge that separates verified SaaS/retention economics from security/cloud/certificate labels and from external price-noise blowoffs.", "supporting_cases": ["C28-R8L99-01", "C28-R8L99-02", "C28-R8L99-03", "C28-R8L99-04", "C28-R8L99-05"], "production_scoring_changed": false}
```

## 9. Raw component score breakdown

These are shadow research scores only. They are not production weights.

```jsonl
{"row_type": "score_simulation", "case_id": "C28-R8L99-01", "symbol": "012510", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "eps_fcf_explosion": 70, "earnings_visibility": 82, "bottleneck_pricing": 52, "market_mispricing": 58, "valuation_rerating": 66, "capital_allocation": 45, "information_confidence": 78, "shadow_total": 72, "shadow_stage": "Stage3-Yellow", "price_confirmation": {"MFE_90D_pct": 38.93, "MAE_90D_pct": -12.28, "MFE_180D_pct": 60.9, "MAE_180D_pct": -12.28}, "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8L99-02", "symbol": "030520", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "eps_fcf_explosion": 62, "earnings_visibility": 74, "bottleneck_pricing": 40, "market_mispricing": 64, "valuation_rerating": 68, "capital_allocation": 40, "information_confidence": 76, "shadow_total": 69, "shadow_stage": "Stage3-Yellow", "price_confirmation": {"MFE_90D_pct": 54.45, "MAE_90D_pct": -2.94, "MFE_180D_pct": 54.45, "MAE_180D_pct": -2.94}, "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8L99-03", "symbol": "053800", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "eps_fcf_explosion": 45, "earnings_visibility": 58, "bottleneck_pricing": 38, "market_mispricing": 55, "valuation_rerating": 60, "capital_allocation": 35, "information_confidence": 68, "shadow_total": 58, "shadow_stage": "Stage3-Yellow_with_local_4B_guard", "price_confirmation": {"MFE_90D_pct": 41.46, "MAE_90D_pct": -8.23, "MFE_180D_pct": 84.65, "MAE_180D_pct": -8.23}, "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8L99-04", "symbol": "434480", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "eps_fcf_explosion": 15, "earnings_visibility": 25, "bottleneck_pricing": 35, "market_mispricing": 45, "valuation_rerating": 50, "capital_allocation": 20, "information_confidence": 65, "shadow_total": 39, "shadow_stage": "4B_local_watch", "price_confirmation": {"MFE_90D_pct": 38.35, "MAE_90D_pct": -30.59, "MFE_180D_pct": 44.47, "MAE_180D_pct": -34.59}, "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8L99-05", "symbol": "203650", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "eps_fcf_explosion": 25, "earnings_visibility": 28, "bottleneck_pricing": 15, "market_mispricing": 20, "valuation_rerating": 18, "capital_allocation": 25, "information_confidence": 70, "shadow_total": 32, "shadow_stage": "Stage2_or_block", "price_confirmation": {"MFE_90D_pct": 2.43, "MAE_90D_pct": -25.88, "MFE_180D_pct": 7.68, "MAE_180D_pct": -38.41}, "production_scoring_changed": false}
```

## 10. Aggregate metric

```jsonl
{"row_type": "aggregate_metric", "round": "R8", "loop": "99", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "sample_count": 5, "positive_case_count": 2, "counterexample_count": 3, "4B_case_count": 2, "4C_case_count": 0, "current_profile_error_count": 3, "new_symbol_count": 3, "reused_symbol_new_trigger_count": 2, "MFE_30D_pct": 19.62, "MAE_30D_pct": -13.76, "MFE_90D_pct": 35.12, "MAE_90D_pct": -15.98, "MFE_180D_pct": 50.43, "MAE_180D_pct": -19.29, "median_MFE_30D_pct": 17.78, "median_MAE_30D_pct": -11.95, "median_MFE_90D_pct": 38.93, "median_MAE_90D_pct": -12.28, "median_MFE_180D_pct": 54.45, "median_MAE_180D_pct": -12.28, "interpretation": "Verified SaaS/retention/OPM rows create favorable MFE/MAE, but C28 label rows with operating loss, order delay, non-C28 revenue mix, or blowoff noise need Stage2/4B caps."}
```

## 11. Shadow rule candidates

```jsonl
{"row_type": "shadow_weight", "axis": "C28_RETENTION_ARR_OPM_BRIDGE_GATE", "scope": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "candidate_action": "stage3_yellow_unlock_if_verified", "rule": "Promote C28 above Stage2 only when software/security evidence connects to renewal, paid-seat expansion, ARR/maintenance revenue, cloud/SaaS revenue mix, OPM, FCF, or EPS revision.", "supporting_cases": ["C28-R8L99-01", "C28-R8L99-02"], "counterbalanced_by": ["C28-R8L99-04", "C28-R8L99-05"], "production_scoring_changed": false}
{"row_type": "shadow_weight", "axis": "C28_SECURITY_PRODUCT_BLOWOFF_4B_GUARD", "scope": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "candidate_action": "local_4b_watch_guard", "rule": "Security product growth can justify Stage3-Yellow, but if retention/ARR proof is thin and the stock-web path shows fast MFE plus severe post-peak drawdown, keep a local 4B guard active.", "supporting_cases": ["C28-R8L99-03", "C28-R8L99-04"], "production_scoring_changed": false}
{"row_type": "shadow_weight", "axis": "C28_BUSINESS_MIX_DECONTAMINATION", "scope": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "candidate_action": "block_or_stage2_cap", "rule": "Do not treat security/authentication vocabulary as C28 recurring software quality when most revenue is from non-C28 rental, hardware, SI, or other segments and the price path has high MAE.", "supporting_cases": ["C28-R8L99-05"], "production_scoring_changed": false}
```

## 12. Residual contribution summary

```jsonl
{"row_type": "residual_contribution", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "round": "R8", "loop": "99", "auto_selected_coverage_gap": "C28 rows 28 -> expected 33 after acceptance", "sector_specific_rule_candidate": "L8_C28_VERIFIED_RECURRING_REVENUE_MARGIN_BRIDGE_VS_LABEL_DECONTAMINATION", "canonical_archetype_rule_candidate": "C28_RETENTION_ARR_OPM_BRIDGE_GATE_WITH_4B_BLOWOFF_CAP", "new_axis_proposed": ["C28_RETENTION_ARR_OPM_BRIDGE_GATE", "C28_SECURITY_PRODUCT_BLOWOFF_4B_GUARD", "C28_BUSINESS_MIX_DECONTAMINATION"], "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": [], "promotion_readiness": "shadow_candidate_ready_for_batch_validation", "source_proxy_only_rows": 0, "evidence_url_pending_rows": 0, "production_scoring_changed": false}
```

## 13. Validation flags

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
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 14. Next research state

```text
completed_round = R8
completed_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C28 rows 28 / need to 30 = 2
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C27_CONTENT_IP_GLOBAL_MONETIZATION
```

## 15. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest `e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md` into the v12 calibration corpus.
- Validate all trigger rows against the v12 schema.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Confirm that the rows use stock-web tradable_raw price basis and complete 30D/90D/180D MFE/MAE.
- Test the three candidate axes: C28_RETENTION_ARR_OPM_BRIDGE_GATE, C28_SECURITY_PRODUCT_BLOWOFF_4B_GUARD, C28_BUSINESS_MIX_DECONTAMINATION.
- Keep production scoring unchanged unless batch validation supports a safe patch.

Expected behavior:
- Verified SaaS/cloud/ARR/OPM evidence can unlock Stage3-Yellow for C28.
- Security/cloud/identity labels without renewal, ARR, OPM, or pure C28 revenue mix remain Stage2 or 4B.
- Fast MFE followed by severe post-peak drawdown should remain local 4B watch unless durable retention economics are visible.
```
