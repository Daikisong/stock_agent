# E2R Stock-Web v12 Residual Research — R8 Loop 199 — C28 Software/Security Contract Retention

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R8
selected_loop = 199
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = C28_CLOUD_SECURITY_RECURRING_CONTRACT_RETENTION_AND_PUBLIC_BUDGET_LEAF_V3
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
live_candidate_mode = false
output_filename = e2r_stock_web_v12_residual_round_R8_loop_199_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
```

## 1. Selection Rationale

The current No-Repeat Index baseline still treats C28 as an important quality-repair scope: it is listed at 28 original rows in the Priority 0 table and has since received two session passes, but the remaining C28 error mode is not simply row count. The residual problem is that **security/cloud/software vocabulary often looks like retained economics before renewal, ARR, maintenance, license, or managed-service margin actually shows up**.

Earlier session C28 files already covered Genian, Fasoo, Igloo, Dream Security, Raonsecure, Sands Lab, Douzone, Hancom, AhnLab, ESTsoft, MonitorLab, Polaris Office, Exem, and KSign. This loop avoids those clusters and moves into a new leaf: **cloud/IDC hosting, network security, zero-trust public projects, Japan cloud-mail security, managed-security service, cloud-security SI, and enterprise UI software**.

```text
index_baseline_coverage_before = C28 rows 28
index_baseline_coverage_after_if_accepted = C28 rows 36
session_aware_after_loop133_loop157_loop199_if_accepted ≈ C28 rows 59
new_independent_case_count = 8
positive_case_count = 4
counterexample_count = 4
4B_or_high_MAE_guard_count = 6
current_profile_error_count = 6
```

## 2. Price Source Validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_price_rule = close price on entry_date, or next tradable date if trigger date was not tradable
MFE/MAE_rule = max high / min low over the next N tradable rows after entry_date
```

All usable rows below have at least 180 forward tradable rows. The local stock-web shard cache used for calculation showed no >=20% shares-change contamination inside the D+180 windows for the eight selected entry windows. For `430690`, the February 2024 record-earnings row was excluded because a later May 2024 shares-change candidate would contaminate that window; the post-change August 2024 row is used instead.

## 3. Historical Eligibility Gate

| symbol | company | entry_date | last_180D_row | shares_change_abs_max_180D | usable |
|---:|---|---:|---:|---:|---|
| 079940 | 가비아 | 2024-11-14 | 2025-08-11 | 0.0 | true |
| 136540 | 윈스테크넷 | 2025-02-05 | 2025-10-30 | 0.0 | true |
| 170790 | 파이오링크 | 2024-12-20 | 2025-09-17 | 0.02 | true |
| 184230 | SGA솔루션즈 | 2024-07-23 | 2025-04-21 | 0.0 | true |
| 208350 | 지란지교시큐리티 | 2024-07-01 | 2025-03-28 | 0.0 | true |
| 356890 | 싸이버원 | 2025-03-20 | 2025-12-11 | 0.0031 | true |
| 430690 | 한싹 | 2024-08-21 | 2025-05-22 | 0.0 | true |
| 450520 | 인스웨이브시스템즈 | 2024-07-25 | 2025-04-23 | 0.0 | true |

## 4. Case Table

| case_id | symbol | company | trigger | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | role |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| C28_L199_01_079940 | 079940 | 가비아 | Stage2-Actionable | 2024-11-14 | 13,480 | 55.42% | -4.67% | 112.91% | -4.67% | positive |
| C28_L199_02_136540 | 136540 | 윈스테크넷 | Stage2-Watch | 2025-02-05 | 10,940 | 16.45% | -5.67% | 22.49% | -5.67% | positive_watch |
| C28_L199_03_170790 | 170790 | 파이오링크 | Stage2 | 2024-12-20 | 8,620 | 4.87% | -27.96% | 4.87% | -27.96% | counterexample |
| C28_L199_04_184230 | 184230 | SGA솔루션즈 | Stage2 | 2024-07-23 | 602 | 10.47% | -29.57% | 10.47% | -36.38% | counterexample |
| C28_L199_05_208350 | 208350 | 지란지교시큐리티 | Stage2 | 2024-07-01 | 3,575 | 8.53% | -22.8% | 8.53% | -30.07% | counterexample |
| C28_L199_06_356890 | 356890 | 싸이버원 | Stage2-Watch | 2025-03-20 | 4,195 | 24.43% | -24.67% | 29.2% | -26.94% | positive_watch |
| C28_L199_07_430690 | 430690 | 한싹 | Stage2-Watch | 2024-08-21 | 5,960 | 44.46% | -44.8% | 44.46% | -44.8% | counterexample |
| C28_L199_08_450520 | 450520 | 인스웨이브시스템즈 | Stage2-Watch | 2024-07-25 | 4,565 | 20.92% | -40.09% | 36.25% | -40.09% | positive_watch |

## 5. Evidence Source Map

| case_id | symbol | trigger_date | evidence_source | evidence_note |
|---|---:|---:|---|---|
| C28_L199_01_079940 | 079940 | 2024-11-14 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20241114001755&docno=&method=search&viewerhost= | 2024 Q3 filing showed cloud/IT, IX/IDC, and security revenue mix; recurring infrastructure/security economics were visible before the price rerating. |
| C28_L199_02_136540 | 136540 | 2025-02-05 | https://m.boannews.com/html/detail.html?idx=135835 | 2024 security-industry review noted Wins' revenue softness despite operating-profit resilience and new integrated managed-security-service push. |
| C28_L199_03_170790 | 170790 | 2024-12-20 | https://stock.pstatic.net/stock-research/company/72/20241220_company_5192000.pdf | ADC/WAF/HCI and cloud security product exposure existed, but 2024 growth/run-rate evidence was not strong enough for Actionable. |
| C28_L199_04_184230 | 184230 | 2024-07-23 | https://sgasol.kr/notice/press_view/press_no%3D203?keyword=&keywordSelect=&page=3 | The company cited KISA zero-trust pilot and cloud-security national-project wins, but revenue/margin conversion was not yet proven. |
| C28_L199_05_208350 | 208350 | 2024-07-01 | https://story.jiran.com/%EC%84%B8%EA%B3%84%EB%A1%9C-%EB%8F%84%EC%A0%84%ED%95%98%EB%8A%94-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD-%EC%82%AC%EC%9D%B4%EB%B2%84-%EB%B3%B4%EC%95%88-%EA%B8%B0%EC%97%85%EB%93%A4-%E2%91%A6-%EC%A7%80/ | Japan cloud/email-security customer-count evidence existed, but listed-entity margin/revision bridge was missing. |
| C28_L199_06_356890 | 356890 | 2025-03-20 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001478&docno=&method=search&viewerhost= | Business report described managed security and consulting core; positive path existed, but high MAE argues for staged-entry guard. |
| C28_L199_07_430690 | 430690 | 2024-08-21 | https://w4.kirs.or.kr/download/research/240821_%ED%95%9C%EC%8B%B9.pdf | 1H24 sales grew but operating loss turned negative; cloud-security vocabulary did not protect against severe post-spike drawdown. |
| C28_L199_08_450520 | 450520 | 2024-07-25 | https://file.alphasquare.co.kr/media/pdfs/company-ir/20240725%EC%9D%B8%EC%8A%A4%EC%9B%A8%EC%9D%B4%EB%B8%8C%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%A6%88_%EC%83%81%EB%B0%98%EA%B8%B0_%EC%8B%9C%EC%9E%A5_%EC%B9%A8%EC%B2%B4%EC%97%90%EB%8F%84_%27%ED%95%98%EB%B0%98%EA%B8%B0_%EA%B0%95%EC%84%B8%27_%EA%B8%B0%EB%8C%80.pdf | WebSquare, AI/DX, 900+ customers and 4,000+ projects were real, but entry needed high-MAE staging until recurring license/maintenance mix was confirmed. |

## 6. Case Notes

### 6.1 Gabia — cloud/IDC/security mix was a true retained-economics bridge

`079940 / 2024-11-14` is the cleanest C28 positive in this pass. It did not rely on a single AI/security keyword. The evidence showed recurring cloud/IT, IX/IDC, and security revenue mix at the issuer level. The price path is unusually clean for a small software-infrastructure name: `MFE90 +55.42%`, `MAE90 -4.67%`, and `MFE180 +112.91%`. This is the leaf C28 should allow: retained infrastructure usage plus operating leverage potential.

### 6.2 Wins — security quality was real, but the signal was low-alpha without acceleration

`136540 / 2025-02-05` had a stable security-company profile and operating-profit resilience, but the 90D MFE was only `+16.45%`. The row is not a failure; it is a **Stage2-Watch / low-alpha positive**. C28 should not penalize stable security earnings, but it should avoid upgrading to Actionable unless renewal, managed-service growth, or margin acceleration is visible.

### 6.3 Piolink, SGA Solutions, Jiran Security — vocabulary without conversion bridge

`170790`, `184230`, and `208350` are the center of the counterexample block. ADC/WAF/HCI, zero-trust public projects, and Japan cloud-mail user/customer growth are all legitimate C28 language. But the price paths say the language was not yet enough: Piolink had `MFE180 +4.87% / MAE180 -27.96%`, SGA Solutions had `MFE180 +10.47% / MAE180 -36.38%`, and Jiran had `MFE180 +8.53% / MAE180 -30.07%`. These should remain Stage2-Watch unless contract retention or revenue/margin conversion is verified.

### 6.4 CyberOne, Hanssak, Inswave — high-MAE positives need staged-entry, not blind Green

`356890 / CyberOne` and `450520 / Inswave` did produce meaningful 180D MFE, but both carried large MAE. The correct calibration is not hard block; it is **staged-entry and position-size guard**. `430690 / Hanssak` is harsher: after the post-corporate-action August evidence, the MFE was strong but the MAE was equally violent. C28 should treat this as a 4B/high-volatility proof, not a clean retained-contract signal.

## 7. Current Calibrated Profile Stress Test

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = C28_CLOUD_SECURITY_RECURRING_CONTRACT_RETENTION_GATE_V3_shadow
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

The current calibrated profile already blocks price-only blowoff and asks for non-price evidence. The residual C28 mistake is more subtle: **non-price evidence exists, but the evidence sits too high in the funnel**. Policy projects, security product exposure, conference decks, customer-count language, and public cloud-security demand are not yet retained economics. C28 should only open Stage2-Actionable when the evidence descends into the engine room: recurring license/maintenance, ARR-like renewal, managed-service run-rate, cloud/IDC utilization, public/enterprise contract revenue timing, or margin conversion.

## 8. Proposed Shadow Rule Candidate

```text
canonical_archetype_rule_candidate = C28_RECURRING_CONTRACT_RETENTION_CLOUD_SECURITY_AND_HIGH_MAE_GATE_V3
sector_specific_rule_candidate = L8_SOFTWARE_SECURITY_RETAINED_ECONOMICS_VS_POLICY_THEME_GATE_V3
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
new_axis_proposed = c28_recurring_contract_retention_cloud_security_and_high_mae_gate_v3
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_should_not_fire_on_security_theme_or_one_project_delay_without_retention_break
```

Rule shape:

```text
If C28 evidence is only cyber-security theme, zero-trust policy, conference deck, product category, or one-off SI/project vocabulary:
    max_stage = Stage2-Watch
    require revenue/margin conversion before Stage2-Actionable

If C28 evidence includes recurring cloud/IDC/managed-security/license/maintenance/ARR-like renewal plus OP/margin bridge:
    allow Stage2-Actionable
    allow Stage3-Yellow only after low-MAE or repeated conversion confirmation

If MFE30 >= 30 and MAE90 <= -30:
    do not classify as clean positive
    mark local_4B_or_high_MAE_guard = true

If MAE90 <= -35 but MFE180 >= 30 and contract bridge remains intact:
    do not hard-block
    use staged-entry / position-size guard
```

## 9. Trigger-Level JSONL

```jsonl
{"case_id": "C28_L199_01_079940", "symbol": "079940", "company": "가비아", "trigger_date": "2024-11-14", "trigger_type": "Stage2-Actionable", "entry_date": "2024-11-14", "entry_price": 13480.0, "fine_leaf": "cloud_it_idc_security_mix_retention", "role": "positive", "last_180D_row": "2025-08-11", "MFE_30D_pct": 31.53, "MAE_30D_pct": -4.67, "MFE_90D_pct": 55.42, "MAE_90D_pct": -4.67, "MFE_180D_pct": 112.91, "MAE_180D_pct": -4.67, "peak_date": "2025-07-09", "peak_price": 28700.0, "drawdown_after_peak_pct": -21.6, "shares_change_abs_max_180D": 0.0, "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20241114001755&docno=&method=search&viewerhost=", "evidence_note": "2024 Q3 filing showed cloud/IT, IX/IDC, and security revenue mix; recurring infrastructure/security economics were visible before the price rerating.", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"case_id": "C28_L199_02_136540", "symbol": "136540", "company": "윈스테크넷", "trigger_date": "2025-02-05", "trigger_type": "Stage2-Watch", "entry_date": "2025-02-05", "entry_price": 10940.0, "fine_leaf": "security_solution_budget_cycle_low_alpha", "role": "positive_watch", "last_180D_row": "2025-10-30", "MFE_30D_pct": 3.02, "MAE_30D_pct": -5.67, "MFE_90D_pct": 16.45, "MAE_90D_pct": -5.67, "MFE_180D_pct": 22.49, "MAE_180D_pct": -5.67, "peak_date": "2025-07-10", "peak_price": 13400.0, "drawdown_after_peak_pct": -10.3, "shares_change_abs_max_180D": 0.0, "evidence_url": "https://m.boannews.com/html/detail.html?idx=135835", "evidence_note": "2024 security-industry review noted Wins' revenue softness despite operating-profit resilience and new integrated managed-security-service push.", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"case_id": "C28_L199_03_170790", "symbol": "170790", "company": "파이오링크", "trigger_date": "2024-12-20", "trigger_type": "Stage2", "entry_date": "2024-12-20", "entry_price": 8620.0, "fine_leaf": "adc_waf_hci_report_but_flat_growth", "role": "counterexample", "last_180D_row": "2025-09-17", "MFE_30D_pct": 4.87, "MAE_30D_pct": -12.99, "MFE_90D_pct": 4.87, "MAE_90D_pct": -27.96, "MFE_180D_pct": 4.87, "MAE_180D_pct": -27.96, "peak_date": "2024-12-26", "peak_price": 9040.0, "drawdown_after_peak_pct": -31.31, "shares_change_abs_max_180D": 0.02, "evidence_url": "https://stock.pstatic.net/stock-research/company/72/20241220_company_5192000.pdf", "evidence_note": "ADC/WAF/HCI and cloud security product exposure existed, but 2024 growth/run-rate evidence was not strong enough for Actionable.", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"case_id": "C28_L199_04_184230", "symbol": "184230", "company": "SGA솔루션즈", "trigger_date": "2024-07-23", "trigger_type": "Stage2", "entry_date": "2024-07-23", "entry_price": 602.0, "fine_leaf": "zero_trust_policy_project_but_no_revenue_bridge", "role": "counterexample", "last_180D_row": "2025-04-21", "MFE_30D_pct": 10.47, "MAE_30D_pct": -29.57, "MFE_90D_pct": 10.47, "MAE_90D_pct": -29.57, "MFE_180D_pct": 10.47, "MAE_180D_pct": -36.38, "peak_date": "2024-08-23", "peak_price": 665.0, "drawdown_after_peak_pct": -42.41, "shares_change_abs_max_180D": 0.0, "evidence_url": "https://sgasol.kr/notice/press_view/press_no%3D203?keyword=&keywordSelect=&page=3", "evidence_note": "The company cited KISA zero-trust pilot and cloud-security national-project wins, but revenue/margin conversion was not yet proven.", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"case_id": "C28_L199_05_208350", "symbol": "208350", "company": "지란지교시큐리티", "trigger_date": "2024-07-01", "trigger_type": "Stage2", "entry_date": "2024-07-01", "entry_price": 3575.0, "fine_leaf": "japan_cloud_mailgate_customer_growth_but_no_margin_bridge", "role": "counterexample", "last_180D_row": "2025-03-28", "MFE_30D_pct": 4.34, "MAE_30D_pct": -22.8, "MFE_90D_pct": 8.53, "MAE_90D_pct": -22.8, "MFE_180D_pct": 8.53, "MAE_180D_pct": -30.07, "peak_date": "2024-08-28", "peak_price": 3880.0, "drawdown_after_peak_pct": -35.57, "shares_change_abs_max_180D": 0.0, "evidence_url": "https://story.jiran.com/%EC%84%B8%EA%B3%84%EB%A1%9C-%EB%8F%84%EC%A0%84%ED%95%98%EB%8A%94-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD-%EC%82%AC%EC%9D%B4%EB%B2%84-%EB%B3%B4%EC%95%88-%EA%B8%B0%EC%97%85%EB%93%A4-%E2%91%A6-%EC%A7%80/", "evidence_note": "Japan cloud/email-security customer-count evidence existed, but listed-entity margin/revision bridge was missing.", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"case_id": "C28_L199_06_356890", "symbol": "356890", "company": "싸이버원", "trigger_date": "2025-03-20", "trigger_type": "Stage2-Watch", "entry_date": "2025-03-20", "entry_price": 4195.0, "fine_leaf": "managed_security_ai_consulting_high_mae", "role": "positive_watch", "last_180D_row": "2025-12-11", "MFE_30D_pct": 24.43, "MAE_30D_pct": -10.13, "MFE_90D_pct": 24.43, "MAE_90D_pct": -24.67, "MFE_180D_pct": 29.2, "MAE_180D_pct": -26.94, "peak_date": "2025-09-23", "peak_price": 5420.0, "drawdown_after_peak_pct": -32.47, "shares_change_abs_max_180D": 0.0031, "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001478&docno=&method=search&viewerhost=", "evidence_note": "Business report described managed security and consulting core; positive path existed, but high MAE argues for staged-entry guard.", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"case_id": "C28_L199_07_430690", "symbol": "430690", "company": "한싹", "trigger_date": "2024-08-21", "trigger_type": "Stage2-Watch", "entry_date": "2024-08-21", "entry_price": 5960.0, "fine_leaf": "cloud_security_half_loss_high_volatility", "role": "counterexample", "last_180D_row": "2025-05-22", "MFE_30D_pct": 44.46, "MAE_30D_pct": -8.72, "MFE_90D_pct": 44.46, "MAE_90D_pct": -44.8, "MFE_180D_pct": 44.46, "MAE_180D_pct": -44.8, "peak_date": "2024-08-28", "peak_price": 8610.0, "drawdown_after_peak_pct": -61.79, "shares_change_abs_max_180D": 0.0, "evidence_url": "https://w4.kirs.or.kr/download/research/240821_%ED%95%9C%EC%8B%B9.pdf", "evidence_note": "1H24 sales grew but operating loss turned negative; cloud-security vocabulary did not protect against severe post-spike drawdown.", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"case_id": "C28_L199_08_450520", "symbol": "450520", "company": "인스웨이브시스템즈", "trigger_date": "2024-07-25", "trigger_type": "Stage2-Watch", "entry_date": "2024-07-25", "entry_price": 4565.0, "fine_leaf": "websquare_ai_customer_portfolio_high_mae", "role": "positive_watch", "last_180D_row": "2025-04-23", "MFE_30D_pct": 20.92, "MAE_30D_pct": -22.78, "MFE_90D_pct": 20.92, "MAE_90D_pct": -40.09, "MFE_180D_pct": 36.25, "MAE_180D_pct": -40.09, "peak_date": "2025-02-06", "peak_price": 6220.0, "drawdown_after_peak_pct": -41.32, "shares_change_abs_max_180D": 0.0, "evidence_url": "https://file.alphasquare.co.kr/media/pdfs/company-ir/20240725%EC%9D%B8%EC%8A%A4%EC%9B%A8%EC%9D%B4%EB%B8%8C%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%A6%88_%EC%83%81%EB%B0%98%EA%B8%B0_%EC%8B%9C%EC%9E%A5_%EC%B9%A8%EC%B2%B4%EC%97%90%EB%8F%84_%27%ED%95%98%EB%B0%98%EA%B8%B0_%EA%B0%95%EC%84%B8%27_%EA%B8%B0%EB%8C%80.pdf", "evidence_note": "WebSquare, AI/DX, 900+ customers and 4,000+ projects were real, but entry needed high-MAE staging until recurring license/maintenance mix was confirmed.", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
```

## 10. Aggregate / Residual Contribution

```json
{
  "selected_round": "R8",
  "selected_loop": 199,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "new_independent_case_count": 8,
  "usable_trigger_row_count": 8,
  "representative_trigger_count": 8,
  "positive_case_count": 4,
  "counterexample_count": 4,
  "stage4b_watch_or_high_mae_guard_count": 6,
  "current_profile_error_count": 6,
  "coverage_before_index_baseline": "C28 rows 28",
  "coverage_after_if_accepted_index_baseline": "C28 rows 36",
  "session_aware_after_loop133_loop157_loop199_if_accepted": "about C28 rows 59",
  "do_not_propose_new_weight_delta": false,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

When batch-applying this MD later, parse all trigger JSONL rows where calibration_usable=true and canonical_archetype_id=C28_SOFTWARE_SECURITY_CONTRACT_RETENTION. Add a shadow rule candidate named C28_RECURRING_CONTRACT_RETENTION_CLOUD_SECURITY_AND_HIGH_MAE_GATE_V3. The rule should require retained-economics bridge before Stage2-Actionable for C28 security/software names. Retained-economics bridge may include ARR-like renewal, recurring license/maintenance, managed-security run-rate, cloud/IDC utilization, enterprise/public contract revenue timing, or OP/margin conversion. Pure policy/security theme, zero-trust pilot, product-category exposure, conference/IR deck, or single project evidence should be Stage2-Watch at most. High-MAE rows with intact bridge should be staged-entry rather than hard block.
```

## 12. Next Research State

```text
completed_round = R8
completed_loop = 199
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes = C18_CONSUMER_EXPORT_CHANNEL_REORDER | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
