# E2R Stock-Web v12 Residual Research — R8 loop 128 / C28 SOFTWARE_SECURITY_CONTRACT_RETENTION
---
schema_version: "e2r_stock_web_v12_residual_research"
research_session: "post_calibrated_sector_archetype_residual_research"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R8"
selected_loop: 128
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 0 static / under-50 local carryover: C28 had 28 representative rows in index; prior local C28 loop_126 and loop_127 add 16 representative rows; this loop adds 6 more representative rows and one narrative-only blocked row."
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L8_PLATFORM_CONTENT_SW_SECURITY"
canonical_archetype_id: "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
fine_archetype_id: "SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_AND_MARGIN_LEVERAGE_VS_FEATURE_OR_TRANSACTION_PROXY"
loop_objective:
  - coverage_gap_fill
  - under_50_local_completion
  - source_proxy_replacement
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - stage2_actionable_bonus_stress_test
  - canonical_archetype_compression
price_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

## 0. Execution summary

이번 파일은 C28 under-50 local completion용 follow-up이다. No-Repeat Index 원본에서 C28은 28 representative rows로 Priority 0 끝단에 남아 있었고, 이 세션의 C28 loop_126/127 산출물을 감안하면 약 44개까지 올라온 상태다. 이번 loop는 기존 C28 산출물의 symbol/date family를 피하고, 6개 representative trigger와 1개 narrative-only blocked row를 추가해 C28의 실전 보정권 50-row 부근을 메운다.

핵심 잔여 오류는 C28이 아직 `보안/소프트웨어/AI/클라우드/전자상거래/결제`라는 제품명과 `ARR·renewal·recurring contract·merchant lock-in·margin leverage`를 충분히 분리하지 못한다는 점이다. C28은 단어가 아니라 반복 과금과 재계약의 내구성이다. 물레방아가 계속 도는지 보려면 물길이 한 번 튄 순간이 아니라, 물이 계속 같은 수로로 들어오는지를 봐야 한다.

## 1. Coverage / novelty check

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 static C28 rows 28 / need_to_30 2 / need_to_50 22
local_carryover_note = prior C28 loop_126 + loop_127 already added 16 representative rows in this session
this_loop_adds = 6 representative rows + 1 narrative-only blocked row
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
local_prior_C28_symbols_avoided = 012510,030520,053800,060850,067920,150900,205100,263860,042510,053580,079940,208350,263800,290270,307950,356680
this_loop_symbols = 018260,060250,049480,042000,258790,041460; narrative_only=058970
hard_duplicate = 0
round_sector_consistency = pass
```

## 2. Price-source validation scope

```json
{
  "row_type": "price_source_validation",
  "price_source": "Songdaiki/stock-web",
  "upstream_source": "FinanceData/marcap",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "manifest_max_date": "2026-02-20",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "entry_price_basis": "close_c_column_on_entry_date",
  "forward_windows": "30/90/180 trading-row windows inside stock-web manifest date",
  "corporate_action_rule": "block representative aggregation if share-count/corporate-action contamination overlaps entry~D+180"
}
```

## 3. Evidence-source map

| ticker | evidence family | source route | use |
|---|---|---|---|
| 018260 | Samsung SDS cloud / enterprise solution / recurring service | official Q3 2024 result + SRM solution page | positive control with staged-entry guard |
| 060250 | payment gateway merchant lock-in / foreign merchant transaction value | Mirae Asset NHN KCP report | positive boundary C28, margin guard required |
| 049480 | ITO / managed service / security monitoring | Openbase IR + service page | Stage2 watch / mild positive |
| 042000 | YouTube Shopping product feature route | Asiae + MK English | feature blowoff / local 4B |
| 258790 | Zero Trust / document security / SHIELD ID | Softcamp IR/company pages | security-product identity counterexample |
| 041460 | PKI/SSL/certificate recurring revenue | CrossCert official pages | mature recurring revenue counterexample |
| 058970 | SCM SaaS route but R&D margin drag | MK + Samsung SDS partnership page | narrative-only blocked due contaminated 180D window |


## 4. Representative trigger backtest table

| ticker | company | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | classification |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 018260 | Samsung SDS | Stage2-Actionable | 2024-10-31 | 143100 | 7.62 | -8.25 | 7.62 | -20.96 | 38.92 | -23.83 | positive_control_with_staged_entry_guard |
| 060250 | NHN KCP | Stage2-Actionable | 2024-11-18 | 7120 | 22.05 | -1.54 | 22.05 | -3.65 | 174.44 | -3.65 | positive_boundary_control |
| 049480 | Openbase | Stage2 | 2024-04-15 | 2490 | 10.44 | -3.21 | 10.44 | -12.45 | 18.27 | -12.45 | positive_watch_control |
| 042000 | Cafe24 | Stage4B | 2024-06-21 | 40900 | 5.01 | -32.89 | 5.01 | -44.13 | 70.42 | -44.13 | counterexample_feature_blowoff_then_reopen |
| 258790 | Softcamp | Stage4B | 2024-05-02 | 1300 | 10.69 | -12.38 | 10.69 | -28.69 | 15.31 | -35.77 | counterexample_security_product_identity_without_retention_bridge |
| 041460 | Korea Electronic Certification Authority / CrossCert | Stage2 | 2024-05-02 | 4040 | 8.66 | -5.45 | 8.66 | -19.31 | 8.66 | -36.63 | counterexample_stable_cert_revenue_not_rerating |

## 5. Case notes


### 018260 Samsung SDS — Stage2-Actionable / positive_control_with_staged_entry_guard

- Evidence family: `cloud_sds_srm_recurring_service_margin_leverage`
- Evidence summary: Q3 2024 revenue and operating profit grew YoY; cloud and enterprise solution routes provide recurring-service optionality, but the 90D/180D drawdown says staged entry is safer than immediate Green.
- Price path: MFE30/90/180 = 7.62 / 7.62 / 38.92%, MAE30/90/180 = -8.25 / -20.96 / -23.83%.
- Current-profile verdict: would_be_stage2_actionable; green_blocked_until_contract_retention_and_margin_leverage_are_visible.
- Residual error: profile may under-model staged-entry need after enterprise-software rerating when drawdown opens before 180D payoff.
- Evidence URLs:
  - https://www.samsungsds.com/en/news/news_202410311356.html
  - https://www.samsungsds.com/en/solutions/srm/srm.html

### 060250 NHN KCP — Stage2-Actionable / positive_boundary_control

- Evidence family: `payment_gateway_merchant_lock_in_transaction_billing_boundary`
- Evidence summary: Transaction value and foreign-merchant payment volume had lock-in characteristics; however payment gateway retention is a C28 boundary case and must carry a margin-dilution guard.
- Price path: MFE30/90/180 = 22.05 / 22.05 / 174.44%, MAE30/90/180 = -1.54 / -3.65 / -3.65%.
- Current-profile verdict: stage2_actionable_allowed_but_c28_discounted_for_transaction_margin_profile.
- Residual error: profile can miss high-quality payment-retention route if C28 is limited to pure SaaS/security ARR.
- Evidence URLs:
  - https://securities.miraeasset.com/bbs/maildownload/20241115163542963_155

### 049480 Openbase — Stage2 / positive_watch_control

- Evidence family: `ITO_managed_service_security_monitoring_recurring_contract_watch`
- Evidence summary: Openbase had improving revenue/operating profit and 24/7 ITO/integrated monitoring service exposure; this supports Stage2-watch, not Yellow, because SI/service mix and renewal/margin leverage are not fully separable.
- Price path: MFE30/90/180 = 10.44 / 10.44 / 18.27%, MAE30/90/180 = -3.21 / -12.45 / -12.45%.
- Current-profile verdict: stage2_watch_only_until_recurring_contract_mix_and_margin_leverage_are_explicit.
- Residual error: profile may over-credit managed-service vocabulary when renewal rate and gross-margin mix are hidden.
- Evidence URLs:
  - https://www.openbase.co.kr/eng/ir
  - https://www.openbase.co.kr/service

### 042000 Cafe24 — Stage4B / counterexample_feature_blowoff_then_reopen

- Evidence family: `youtube_shopping_feature_launch_vs_recurring_merchant_revenue_proof`
- Evidence summary: YouTube shopping integration was a real product route, but the stock had already surged; without merchant GMV take-rate and margin conversion, the trigger is a local 4B/profit-lock case rather than fresh Stage2-Actionable.
- Price path: MFE30/90/180 = 5.01 / 5.01 / 70.42%, MAE30/90/180 = -32.89 / -44.13 / -44.13%.
- Current-profile verdict: feature_or_platform_partnership_blocks_yellow_when_price_is_already_crowded.
- Residual error: profile must separate product-optionality reopen from immediate software-retention rerating.
- Evidence URLs:
  - https://www.asiae.co.kr/en/article/2024072513201180397
  - https://www.mk.co.kr/en/stock/11048173

### 258790 Softcamp — Stage4B / counterexample_security_product_identity_without_retention_bridge

- Evidence family: `zero_trust_document_security_product_launch_without_recurring_margin_proof`
- Evidence summary: Zero Trust, SHIELD ID, CDR and document-security vocabulary fit C28 thematically, but product identity without ARR/renewal/margin proof leads to high MAE and should remain Stage4B/watch.
- Price path: MFE30/90/180 = 10.69 / 10.69 / 15.31%, MAE30/90/180 = -12.38 / -28.69 / -35.77%.
- Current-profile verdict: security_product_vocabulary_must_not_auto_promote_without_contract_retention_metric.
- Residual error: profile can over-credit security keywords when billing model and renewal durability are missing.
- Evidence URLs:
  - https://www.softcamp.co.kr/en/ir/
  - https://www.softcamp.co.kr/en/company/

### 041460 Korea Electronic Certification Authority / CrossCert — Stage2 / counterexample_stable_cert_revenue_not_rerating

- Evidence family: `PKI_SSL_certificate_recurring_revenue_stability_without_growth_leverage`
- Evidence summary: Government-licensed CA, PKI/SSL and certificate sales are recurring-like, but stable certificate revenue without growth acceleration or operating leverage produced poor 180D alignment.
- Price path: MFE30/90/180 = 8.66 / 8.66 / 8.66%, MAE30/90/180 = -5.45 / -19.31 / -36.63%.
- Current-profile verdict: stable_recurring_security_revenue_is_stage2_watch_not_actionable_without_growth_or_margin_leverage.
- Residual error: profile needs a growth/margin condition so mature certificate revenue does not receive SaaS-like rerating credit.
- Evidence URLs:
  - https://www.crosscert.com/en/company/
  - https://www.crosscert.com/en/financial-information/

### Narrative-only blocked row — 058970 EMRO

- Blocked reason: `corporate_action_or_share_count_contaminated_180D_window_detected_in_stock_web_profile_or_shard`
- Evidence summary: Cloud service fee growth and Samsung SDS/o9/EMRO SaaS route are meaningful, but Q1 2024 OP collapsed from global SaaS/R&D investment and the 180D price window is share-count contaminated. Keep as narrative-only margin-drag evidence.
- Non-representative price path kept for audit only: MFE30/90/180 = 13.88 / 13.88 / 25.52%, MAE30/90/180 = -16.42 / -43.43 / -43.43%.
  - https://www.mk.co.kr/en/it/11016678
  - https://www.samsungsds.com/en/news/emro_o9_samsungsds_saas_20230614.html

## 6. Machine-readable trigger JSONL

```jsonl
{"MAE_180D_pct": -23.83, "MAE_30D_pct": -8.25, "MAE_90D_pct": -20.96, "MFE_180D_pct": 38.92, "MFE_30D_pct": 7.62, "MFE_90D_pct": 7.62, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_R8_L128_018260_2024_10_31_STAGE2A", "company": "Samsung SDS", "current_profile_verdict": "would_be_stage2_actionable; green_blocked_until_contract_retention_and_margin_leverage_are_visible", "entry_date": "2024-10-31", "entry_price": 143100, "evidence_family": "cloud_sds_srm_recurring_service_margin_leverage", "evidence_summary": "Q3 2024 revenue and operating profit grew YoY; cloud and enterprise solution routes provide recurring-service optionality, but the 90D/180D drawdown says staged entry is safer than immediate Green.", "evidence_urls": ["https://www.samsungsds.com/en/news/news_202410311356.html", "https://www.samsungsds.com/en/solutions/srm/srm.html"], "fine_archetype_id": "SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_AND_MARGIN_LEVERAGE_VS_FEATURE_OR_TRANSACTION_PROXY", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "no_repeat_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|018260|Stage2-Actionable|2024-10-31", "peak_180D_date": "2025-06-24", "positive_or_counterexample": "positive_control_with_staged_entry_guard", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "representative_for_aggregate": true, "residual_error": "profile may under-model staged-entry need after enterprise-software rerating when drawdown opens before 180D payoff", "row_type": "trigger", "selected_loop": 128, "selected_round": "R8", "stage4b_overlay": true, "strict_duplicate_check": "pass_new_symbol_or_new_trigger_family_vs_local_C28_loop_126_127", "ticker": "018260", "trigger_date": "2024-10-31", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-04-09"}
{"MAE_180D_pct": -3.65, "MAE_30D_pct": -1.54, "MAE_90D_pct": -3.65, "MFE_180D_pct": 174.44, "MFE_30D_pct": 22.05, "MFE_90D_pct": 22.05, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_R8_L128_060250_2024_11_18_STAGE2A", "company": "NHN KCP", "current_profile_verdict": "stage2_actionable_allowed_but_c28_discounted_for_transaction_margin_profile", "entry_date": "2024-11-18", "entry_price": 7120, "evidence_family": "payment_gateway_merchant_lock_in_transaction_billing_boundary", "evidence_summary": "Transaction value and foreign-merchant payment volume had lock-in characteristics; however payment gateway retention is a C28 boundary case and must carry a margin-dilution guard.", "evidence_urls": ["https://securities.miraeasset.com/bbs/maildownload/20241115163542963_155"], "fine_archetype_id": "SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_AND_MARGIN_LEVERAGE_VS_FEATURE_OR_TRANSACTION_PROXY", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "no_repeat_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|060250|Stage2-Actionable|2024-11-18", "peak_180D_date": "2025-07-11", "positive_or_counterexample": "positive_boundary_control", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "representative_for_aggregate": true, "residual_error": "profile can miss high-quality payment-retention route if C28 is limited to pure SaaS/security ARR", "row_type": "trigger", "selected_loop": 128, "selected_round": "R8", "stage4b_overlay": false, "strict_duplicate_check": "pass_new_symbol_or_new_trigger_family_vs_local_C28_loop_126_127", "ticker": "060250", "trigger_date": "2024-11-18", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-02-03"}
{"MAE_180D_pct": -12.45, "MAE_30D_pct": -3.21, "MAE_90D_pct": -12.45, "MFE_180D_pct": 18.27, "MFE_30D_pct": 10.44, "MFE_90D_pct": 10.44, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_R8_L128_049480_2024_04_15_STAGE2", "company": "Openbase", "current_profile_verdict": "stage2_watch_only_until_recurring_contract_mix_and_margin_leverage_are_explicit", "entry_date": "2024-04-15", "entry_price": 2490, "evidence_family": "ITO_managed_service_security_monitoring_recurring_contract_watch", "evidence_summary": "Openbase had improving revenue/operating profit and 24/7 ITO/integrated monitoring service exposure; this supports Stage2-watch, not Yellow, because SI/service mix and renewal/margin leverage are not fully separable.", "evidence_urls": ["https://www.openbase.co.kr/eng/ir", "https://www.openbase.co.kr/service"], "fine_archetype_id": "SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_AND_MARGIN_LEVERAGE_VS_FEATURE_OR_TRANSACTION_PROXY", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "no_repeat_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|049480|Stage2|2024-04-15", "peak_180D_date": "2024-12-12", "positive_or_counterexample": "positive_watch_control", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "representative_for_aggregate": true, "residual_error": "profile may over-credit managed-service vocabulary when renewal rate and gross-margin mix are hidden", "row_type": "trigger", "selected_loop": 128, "selected_round": "R8", "stage4b_overlay": false, "strict_duplicate_check": "pass_new_symbol_or_new_trigger_family_vs_local_C28_loop_126_127", "ticker": "049480", "trigger_date": "2024-04-15", "trigger_type": "Stage2", "trough_180D_date": "2024-08-05"}
{"MAE_180D_pct": -44.13, "MAE_30D_pct": -32.89, "MAE_90D_pct": -44.13, "MFE_180D_pct": 70.42, "MFE_30D_pct": 5.01, "MFE_90D_pct": 5.01, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_R8_L128_042000_2024_06_21_4B", "company": "Cafe24", "current_profile_verdict": "feature_or_platform_partnership_blocks_yellow_when_price_is_already_crowded", "entry_date": "2024-06-21", "entry_price": 40900, "evidence_family": "youtube_shopping_feature_launch_vs_recurring_merchant_revenue_proof", "evidence_summary": "YouTube shopping integration was a real product route, but the stock had already surged; without merchant GMV take-rate and margin conversion, the trigger is a local 4B/profit-lock case rather than fresh Stage2-Actionable.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2024072513201180397", "https://www.mk.co.kr/en/stock/11048173"], "fine_archetype_id": "SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_AND_MARGIN_LEVERAGE_VS_FEATURE_OR_TRANSACTION_PROXY", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "no_repeat_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|042000|Stage4B|2024-06-21", "peak_180D_date": "2025-02-26", "positive_or_counterexample": "counterexample_feature_blowoff_then_reopen", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "representative_for_aggregate": true, "residual_error": "profile must separate product-optionality reopen from immediate software-retention rerating", "row_type": "trigger", "selected_loop": 128, "selected_round": "R8", "stage4b_overlay": true, "strict_duplicate_check": "pass_new_symbol_or_new_trigger_family_vs_local_C28_loop_126_127", "ticker": "042000", "trigger_date": "2024-06-21", "trigger_type": "Stage4B", "trough_180D_date": "2024-10-24"}
{"MAE_180D_pct": -35.77, "MAE_30D_pct": -12.38, "MAE_90D_pct": -28.69, "MFE_180D_pct": 15.31, "MFE_30D_pct": 10.69, "MFE_90D_pct": 10.69, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_R8_L128_258790_2024_05_02_4B", "company": "Softcamp", "current_profile_verdict": "security_product_vocabulary_must_not_auto_promote_without_contract_retention_metric", "entry_date": "2024-05-02", "entry_price": 1300, "evidence_family": "zero_trust_document_security_product_launch_without_recurring_margin_proof", "evidence_summary": "Zero Trust, SHIELD ID, CDR and document-security vocabulary fit C28 thematically, but product identity without ARR/renewal/margin proof leads to high MAE and should remain Stage4B/watch.", "evidence_urls": ["https://www.softcamp.co.kr/en/ir/", "https://www.softcamp.co.kr/en/company/"], "fine_archetype_id": "SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_AND_MARGIN_LEVERAGE_VS_FEATURE_OR_TRANSACTION_PROXY", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "no_repeat_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|258790|Stage4B|2024-05-02", "peak_180D_date": "2024-12-11", "positive_or_counterexample": "counterexample_security_product_identity_without_retention_bridge", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "representative_for_aggregate": true, "residual_error": "profile can over-credit security keywords when billing model and renewal durability are missing", "row_type": "trigger", "selected_loop": 128, "selected_round": "R8", "stage4b_overlay": true, "strict_duplicate_check": "pass_new_symbol_or_new_trigger_family_vs_local_C28_loop_126_127", "ticker": "258790", "trigger_date": "2024-05-02", "trigger_type": "Stage4B", "trough_180D_date": "2024-11-21"}
{"MAE_180D_pct": -36.63, "MAE_30D_pct": -5.45, "MAE_90D_pct": -19.31, "MFE_180D_pct": 8.66, "MFE_30D_pct": 8.66, "MFE_90D_pct": 8.66, "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_R8_L128_041460_2024_05_02_STAGE2_COUNTER", "company": "Korea Electronic Certification Authority / CrossCert", "current_profile_verdict": "stable_recurring_security_revenue_is_stage2_watch_not_actionable_without_growth_or_margin_leverage", "entry_date": "2024-05-02", "entry_price": 4040, "evidence_family": "PKI_SSL_certificate_recurring_revenue_stability_without_growth_leverage", "evidence_summary": "Government-licensed CA, PKI/SSL and certificate sales are recurring-like, but stable certificate revenue without growth acceleration or operating leverage produced poor 180D alignment.", "evidence_urls": ["https://www.crosscert.com/en/company/", "https://www.crosscert.com/en/financial-information/"], "fine_archetype_id": "SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_AND_MARGIN_LEVERAGE_VS_FEATURE_OR_TRANSACTION_PROXY", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "no_repeat_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|041460|Stage2|2024-05-02", "peak_180D_date": "2024-06-03", "positive_or_counterexample": "counterexample_stable_cert_revenue_not_rerating", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "representative_for_aggregate": true, "residual_error": "profile needs a growth/margin condition so mature certificate revenue does not receive SaaS-like rerating credit", "row_type": "trigger", "selected_loop": 128, "selected_round": "R8", "stage4b_overlay": true, "strict_duplicate_check": "pass_new_symbol_or_new_trigger_family_vs_local_C28_loop_126_127", "ticker": "041460", "trigger_date": "2024-05-02", "trigger_type": "Stage2", "trough_180D_date": "2024-12-09"}
{"MAE_180D_pct": -43.43, "MAE_30D_pct": -16.42, "MAE_90D_pct": -43.43, "MFE_180D_pct": 25.52, "MFE_30D_pct": 13.88, "MFE_90D_pct": 13.88, "blocked_reason": "corporate_action_or_share_count_contaminated_180D_window_detected_in_stock_web_profile_or_shard", "calibration_usable": false, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28_R8_L128_058970_2024_05_16_NARRATIVE_ONLY", "company": "EMRO", "entry_date": "2024-05-16", "entry_price": 67000, "evidence_family": "SCM_SaaS_global_solution_RnD_investment_margin_drag", "evidence_summary": "Cloud service fee growth and Samsung SDS/o9/EMRO SaaS route are meaningful, but Q1 2024 OP collapsed from global SaaS/R&D investment and the 180D price window is share-count contaminated. Keep as narrative-only margin-drag evidence.", "evidence_urls": ["https://www.mk.co.kr/en/it/11016678", "https://www.samsungsds.com/en/news/emro_o9_samsungsds_saas_20230614.html"], "fine_archetype_id": "SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_AND_MARGIN_LEVERAGE_VS_FEATURE_OR_TRANSACTION_PROXY", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "no_repeat_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|058970|Stage2-Actionable|2024-05-16", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "representative_for_aggregate": false, "row_type": "narrative_only", "selected_loop": 128, "selected_round": "R8", "ticker": "058970", "trigger_date": "2024-05-16", "trigger_type": "Stage2-Actionable"}
```

## 7. Machine-readable score simulation JSONL

```jsonl
{"bottleneck_pricing": 7, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "capital_allocation": 5, "case_id": "C28_R8_L128_018260_2024_10_31_STAGE2A", "company": "Samsung SDS", "earnings_visibility": 15, "eps_fcf": 14, "information_confidence": 8, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market_mispricing": 7, "row_type": "score_simulation", "simulated_stage": "Stage2-Actionable", "ticker": "018260", "total_simulated": 63, "trigger_type": "Stage2-Actionable", "valuation_rerating": 7}
{"bottleneck_pricing": 7, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "capital_allocation": 4, "case_id": "C28_R8_L128_060250_2024_11_18_STAGE2A", "company": "NHN KCP", "earnings_visibility": 16, "eps_fcf": 12, "information_confidence": 8, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market_mispricing": 8, "row_type": "score_simulation", "simulated_stage": "Stage2-Actionable", "ticker": "060250", "total_simulated": 61, "trigger_type": "Stage2-Actionable", "valuation_rerating": 6}
{"bottleneck_pricing": 6, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "capital_allocation": 3, "case_id": "C28_R8_L128_049480_2024_04_15_STAGE2", "company": "Openbase", "earnings_visibility": 12, "eps_fcf": 11, "information_confidence": 7, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market_mispricing": 6, "row_type": "score_simulation", "simulated_stage": "Stage2", "ticker": "049480", "total_simulated": 49, "trigger_type": "Stage2", "valuation_rerating": 4}
{"bottleneck_pricing": 5, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "capital_allocation": 2, "case_id": "C28_R8_L128_042000_2024_06_21_4B", "company": "Cafe24", "earnings_visibility": 8, "eps_fcf": 5, "information_confidence": 7, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market_mispricing": 14, "row_type": "score_simulation", "simulated_stage": "Stage4B_local_watch", "ticker": "042000", "total_simulated": 48, "trigger_type": "Stage4B", "valuation_rerating": 7}
{"bottleneck_pricing": 7, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "capital_allocation": 1, "case_id": "C28_R8_L128_258790_2024_05_02_4B", "company": "Softcamp", "earnings_visibility": 7, "eps_fcf": 6, "information_confidence": 6, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market_mispricing": 7, "row_type": "score_simulation", "simulated_stage": "Stage4B_watch", "ticker": "258790", "total_simulated": 36, "trigger_type": "Stage4B", "valuation_rerating": 2}
{"bottleneck_pricing": 6, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "capital_allocation": 3, "case_id": "C28_R8_L128_041460_2024_05_02_STAGE2_COUNTER", "company": "Korea Electronic Certification Authority / CrossCert", "earnings_visibility": 12, "eps_fcf": 10, "information_confidence": 7, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market_mispricing": 4, "row_type": "score_simulation", "simulated_stage": "Stage2_watch", "ticker": "041460", "total_simulated": 44, "trigger_type": "Stage2", "valuation_rerating": 2}
```

## 8. Aggregate / shadow / residual JSONL

```jsonl
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "canonical_archetype_rule_candidate": "C28_RECURRING_CONTRACT_RETENTION_REQUIRES_BILLING_RENEWAL_MARGIN_LEVERAGE_WITH_FEATURE_AND_TRANSACTION_PROXY_GUARDS", "counterexample_count": 3, "current_profile_error_count": 5, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "local_carryover_estimate": "C28 static 28 + prior local representative 16 + this loop representative 6 = approximately 50 local coverage rows; exact registry dedupe must be recomputed by batch ingest.", "narrative_only_blocked_count": 1, "new_independent_case_count": 6, "positive_case_count": 3, "production_scoring_changed": false, "representative_trigger_count": 6, "row_type": "aggregate", "same_archetype_new_symbol_count": 6, "same_archetype_new_trigger_family_count": 6, "selected_loop": 128, "selected_round": "R8", "shadow_weight_only": true, "stage4b_overlay_count": 4, "stage4c_case_count": 0, "trigger_jsonl_rows": 6}
{"axis": "C28_RECURRING_CONTRACT_RETENTION_REQUIRES_BILLING_RENEWAL_MARGIN_LEVERAGE_WITH_FEATURE_AND_TRANSACTION_PROXY_GUARDS", "do_not_propose_weight_delta": false, "production_scoring_changed": false, "row_type": "shadow_weight_candidate", "rule": "For C28, Stage2-Actionable credit requires at least two of: recurring billing/transaction retention, renewal or maintenance contract evidence, customer lock-in, service mix disclosure, operating-margin leverage. Product feature launches, cybersecurity vocabulary, SI/ITO customer lists, or payment volume alone stay Stage2-watch or local 4B unless margin leverage survives the 90D/180D path.", "shadow_weight_only": true}
{"contribution_label": "canonical_archetype_rule_candidate", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": [], "new_axis_proposed": "C28_RECURRING_CONTRACT_RETENTION_REQUIRES_BILLING_RENEWAL_MARGIN_LEVERAGE_WITH_FEATURE_AND_TRANSACTION_PROXY_GUARDS", "row_type": "residual_contribution", "why": "C28 still confuses recurring contract-retention economics with product identity, platform feature optionality, payment top-line volume, or mature certificate stability. The new axis adds explicit billing/renewal/margin survival gates."}
```

## 9. Residual contribution summary

C28의 새 보강축은 다음과 같다.

```text
C28_RECURRING_CONTRACT_RETENTION_REQUIRES_BILLING_RENEWAL_MARGIN_LEVERAGE_WITH_FEATURE_AND_TRANSACTION_PROXY_GUARDS
```

적용 직관은 간단하다. C28에서 제품명은 문패이고, recurring billing은 월세다. 문패가 좋아 보여도 월세가 꾸준히 들어오지 않으면 임대사업이 아니다. 따라서 `보안/소프트웨어/AI/플랫폼/결제` 단어는 Stage2-watch까지의 문을 열 수 있지만, Stage2-Actionable~Yellow는 반복 과금, 재계약, 고객 lock-in, 서비스 mix, operating-margin leverage 중 최소 두 축이 확인될 때만 허용한다.

- Samsung SDS: enterprise/cloud solution route는 긍정이나, drawdown이 먼저 열리므로 staged-entry guard 필요.
- NHN KCP: 결제 transaction lock-in은 C28 boundary positive이나, margin dilution과 payment volume-only trap을 분리.
- Openbase: ITO/security monitoring은 Stage2-watch이며, renewal/margin mix가 분리되기 전 Yellow 금지.
- Cafe24: YouTube Shopping feature는 유효한 reopen route이나, already-crowded price는 local 4B.
- Softcamp: Zero Trust/product identity만으로 retention credit 금지.
- CrossCert: mature certificate recurring revenue는 안정적이지만 성장·margin leverage 부재 시 rerating credit 제한.
- EMRO: SaaS route는 의미 있으나 R&D margin drag와 corporate/share-count contamination 때문에 narrative-only.

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during the research session.
When batch-ingesting this MD into stock_agent, parse the machine-readable rows above and test a shadow-only rule candidate:

axis = C28_RECURRING_CONTRACT_RETENTION_REQUIRES_BILLING_RENEWAL_MARGIN_LEVERAGE_WITH_FEATURE_AND_TRANSACTION_PROXY_GUARDS
scope = canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
production_scoring_changed = false unless batch validation confirms improvement

Implementation sketch for later coding agent:
1. In v12 calibration ingest, treat representative trigger rows as C28 calibration candidates only if calibration_usable=true and representative_for_aggregate=true.
2. Keep EMRO narrative-only row out of aggregate due corporate/share-count contamination.
3. Add feature_proxy_guard tags for product launches/platform integrations without renewal or margin evidence.
4. Add transaction_boundary_discount for payment-gateway rows unless margin leverage and merchant lock-in are both explicit.
5. Add mature_recurring_revenue_guard for certificate/PKI rows when recurring sales are stable but growth/OP leverage is absent.
6. Report simulated impact separately from production scoring; no direct patch without full corpus validation.
```

## 11. Next research state

```text
completed_round = R8
completed_loop = 128
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 static / C28 under-50 local carryover completion
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_followup_to_50, C02_POWER_GRID_DATACENTER_CAPEX_followup_new_symbols_only, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_followup_after_shard_recheck, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_if_source_proxy_repair_needed
production_scoring_changed = false
shadow_weight_only = true
```
