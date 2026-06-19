# E2R Stock-Web v12 Residual Research — R13 Accounting / Trust / Price Validation

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R13
selected_loop = 153
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 taxonomy repair — R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION after loop 152; direct URL/accounting-cash/price validation holdout
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id = CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
output_filename = e2r_stock_web_v12_residual_round_R13_loop_153_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md
```

## 0. Executive Summary

이번 R13 실행은 새 C01~C32 sector winner를 찾는 연구가 아니라, **회계 숫자·공식 실적·규제/신뢰 이벤트가 실제 가격경로에서 어떻게 검증되는지**를 보는 cross-archetype holdout이다. 직전 R13 accounting loop 152는 GS건설·HDC현산·카카오 founder arrest·HLB CRL·삼성전자 HBM 보도·KB/하나 공식 value-up을 다뤘다. 이번 loop 153은 그 세트를 반복하지 않고, 삼양식품·HD현대일렉트릭·DB손해보험·한국전력을 positive/control 또는 overblock exception으로, CJ ENM·LG생활건강·SK이노베이션·SKIET를 회계/손익/활용률 품질 반례로 올렸다.

핵심 발견은 단순하다. **공식 실적 숫자도 다 같은 금속이 아니다.** 매출·OP가 실제 cash/수주/backlog/CSM/K-ICS/tariff repair와 맞물리면 Stage2/Yellow/Green의 문고리가 된다. 반대로 1개 분기 턴어라운드, AMPC·revenue ramp vocabulary, legacy channel rebound, utilization loss가 섞이면 그 숫자는 유리잔처럼 반짝이지만 충격에는 깨진다.

## 1. Guardrails / Non-Execution

- `stock_agent` source code was not opened or patched.
- No live candidate scan, trading action, brokerage/API work, or production scoring change was performed.
- All rules/weights below are `shadow_weight_only=true`.
- R13 uses `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` only.

## 2. No-Repeat / Coverage Selection

No-Repeat Index reports 2,081 v12 result MDs, 11,200 representative rows, and every C01~C32 canonical above 80 rows. Therefore this run is not a count-fill. It is a quality/taxonomy repair run. The same index lists `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` as one of the over-repeat inspection targets, with 556 representative rows and a source-quality problem across the corpus.

```text
why_R13_now = C01~C32 sweep already covered; R13 accounting/trust is the remaining cross-scope quality checkpoint
why_not_loop_152_duplicate = existing accounting loop 152 already used GS E&C, HDC Hyundai Development, Kakao 2024-07-23, HLB 2024-05-17, Samsung Electronics 2024-05-24, KB 2024-02-07, Hana 2024-10-29
new_independent_case_count = 8
positive_case_count = 4
counterexample_count = 4
stage4b_case_count = 3
stage4c_case_count = 1
source_proxy_only_count = 2
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
current_profile_error_count = 5
```

## 3. Stock-Web Price Source Validation

```jsonl
{"row_type":"price_source_validation","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","price_source":"Songdaiki/stock-web","source_basis":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","symbol_count":5414,"tradable_row_count":14354401,"forward_window_rule":"entry_date_through_N_tradable_rows_max_high_min_low","manifest_checked":true,"schema_checked":true}
```

All trigger rows use the Stock-Web schema fields `d/o/h/l/c/v/a/mc/s/m` and calculate `MFE_N_pct` from entry close to max high through N tradable rows and `MAE_N_pct` from entry close to min low through N tradable rows. Forward 180D windows are available for every trigger.

## 4. Case Grid

| case_id | ticker | company | trigger_date | entry_date | entry_price | trigger_type | source scope | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| R13ATPV153_003230_SAMYANG_2025_EXPORT_CLEAN_EARNINGS_CONTROL | 003230 | 삼양식품 | 2025-05-15 | 2025-05-16 | 1180000 | Stage3-Green | C18_CONSUMER_EXPORT_CHANNEL_REORDER / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 19.83 | -8.73 | 41.10 | -8.73 | 41.10 | -14.49 | current_profile_should_accept_with_4B_profit_lock_after_fast_reprice |
| R13ATPV153_267260_HDHE_2025_ORDER_BACKLOG_EARNINGS_CONTROL | 267260 | HD현대일렉트릭 | 2025-04-22 | 2025-04-23 | 297500 | Stage3-Green | C02_POWER_GRID_DATACENTER_CAPEX | 45.55 | -2.02 | 74.79 | -2.02 | 228.07 | -2.02 | current_profile_should_accept |
| R13ATPV153_005830_DBINS_2024_IFRS17_CSM_KICS_RETURN_CONTROL | 005830 | DB손해보험 | 2024-11-14 | 2024-11-15 | 101600 | Stage3-Yellow | C22_INSURANCE_RATE_CYCLE_RESERVE | 11.91 | -2.46 | 11.91 | -15.16 | 45.96 | -23.72 | current_profile_should_accept_but_green_requires_drawdown_aware_confirmation |
| R13ATPV153_015760_KEPCO_2025_TARIFF_DEBT_CASH_REPAIR_EXCEPTION | 015760 | 한국전력 | 2025-02-28 | 2025-03-04 | 21350 | Stage2-Actionable | C31_POLICY_SUBSIDY_LEGISLATION_EVENT / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 10.54 | -2.11 | 92.74 | -2.11 | 143.56 | -2.11 | current_profile_too_slow_if_debt_watch_blocks_all_stage2 |
| R13ATPV153_035760_CJENM_2024_Q1_TURNAROUND_LOSS_QUALITY_BREAK | 035760 | CJ ENM | 2024-05-09 | 2024-05-10 | 88600 | Stage4B | C27_CONTENT_IP_GLOBAL_MONETIZATION / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 7.11 | -9.71 | 7.11 | -22.80 | 7.11 | -41.99 | current_profile_false_positive_if_one_quarter_OP_turnaround_overweighted |
| R13ATPV153_051900_LGHNH_2024_Q1_REBOUND_LEGACY_PROFIT_BREAK | 051900 | LG생활건강 | 2024-04-25 | 2024-04-26 | 392000 | Stage4B | C19_BRAND_RETAIL_INVENTORY_MARGIN / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 22.45 | -4.46 | 22.45 | -18.11 | 22.45 | -24.87 | current_profile_should_cap_at_Stage4B_after_initial_reprice |
| R13ATPV153_096770_SKINNO_2023_AMPC_LOSS_ACCOUNTING_BRIDGE_FAIL | 096770 | SK이노베이션 | 2023-07-28 | 2023-07-28 | 189500 | Stage4B | C13_BATTERY_JV_UTILIZATION_AMPC_IRA / C14_EV_DEMAND_SLOWDOWN_4B_4C | 19.79 | -10.77 | 19.79 | -36.62 | 19.79 | -45.86 | current_profile_false_positive_if_AMPC_or_revenue_growth_overweights_loss_quality |
| R13ATPV153_361610_SKIET_2024_UTILIZATION_LOSS_HARD_4C | 361610 | SK아이이테크놀로지 | 2024-04-30 | 2024-04-30 | 59100 | Stage4C | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK / C14_EV_DEMAND_SLOWDOWN_4B_4C | 5.25 | -27.75 | 5.25 | -48.73 | 5.25 | -63.03 | current_profile_should_route_to_hard_4C |


## 5. Positive vs Counterexample Aggregate

| bucket | count | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | reading |
|---|---:|---:|---:|---:|---:|---|
| positive/accounting-cash controls | 4 | 55.13 | -7.00 | 114.67 | -10.58 | accounting bridge survived or repaired into price validation |
| accounting/trust-quality counterexamples | 4 | 13.65 | -31.56 | 13.65 | -43.94 | headline or accounting rebound existed, but bridge failed |

Interpretation: the profile should not distrust all accounting events. Samyang, HDHE, DB Insurance and KEPCO show that official financial evidence can work when it is tied to cash, orders, backlog, CSM/K-ICS, or tariff/cash repair. The counterexamples show that one-quarter rebound or revenue vocabulary without durable cash/trust conversion should be capped at 4B, and utilization/loss collapse should go to 4C.

## 6. Case Notes

### R13ATPV153_003230_SAMYANG_2025_EXPORT_CLEAN_EARNINGS_CONTROL — 삼양식품 (003230)

- trigger / entry: `2025-05-15` → `2025-05-16` at `1180000`.
- evidence: Q1 revenue and operating profit reached record levels; overseas sales exceeded KRW 400bn and reached 80% of revenue, giving accounting headline plus direct sales/margin bridge.
- source: https://www.asiae.co.kr/en/article/2025051516275873139
- price path: MFE90 `41.10%`, MAE90 `-8.73%`, MFE180 `41.10%`, MAE180 `-14.49%`, post-peak DD180 `-39.40%`.
- R13 reading: `current_profile_should_accept_with_4B_profit_lock_after_fast_reprice`.

### R13ATPV153_267260_HDHE_2025_ORDER_BACKLOG_EARNINGS_CONTROL — HD현대일렉트릭 (267260)

- trigger / entry: `2025-04-22` → `2025-04-23` at `297500`.
- evidence: Q1 orders reached USD 1.34bn, backlog USD 6.16bn, sales passed KRW 1trn, and operating profit rose sharply; official/filing-style earnings bridge validates price.
- source: https://en.yna.co.kr/view/AEN20250422006151320
- price path: MFE90 `74.79%`, MAE90 `-2.02%`, MFE180 `228.07%`, MAE180 `-2.02%`, post-peak DD180 `-24.59%`.
- R13 reading: `current_profile_should_accept`.

### R13ATPV153_005830_DBINS_2024_IFRS17_CSM_KICS_RETURN_CONTROL — DB손해보험 (005830)

- trigger / entry: `2024-11-14` → `2024-11-15` at `101600`.
- evidence: IFRS17-era CSM, K-ICS management band and shareholder return policy create a stronger accounting-to-cash bridge than generic insurance value-up headline.
- source: https://www.idbins.com/pcweb/bizxpress/cmy/inv/ir/__etc/2024.3Q_DB%20Insurance%281%29.pdf
- price path: MFE90 `11.91%`, MAE90 `-15.16%`, MFE180 `45.96%`, MAE180 `-23.72%`, post-peak DD180 `-17.94%`.
- R13 reading: `current_profile_should_accept_but_green_requires_drawdown_aware_confirmation`.

### R13ATPV153_015760_KEPCO_2025_TARIFF_DEBT_CASH_REPAIR_EXCEPTION — 한국전력 (015760)

- trigger / entry: `2025-02-28` → `2025-03-04` at `21350`.
- evidence: Operating profit turned positive on electricity-rate effects, but debt remained above KRW 200trn; the price path shows cash-repair exception, not automatic Green.
- source: https://en.yna.co.kr/view/AEN20250228005251320
- price path: MFE90 `92.74%`, MAE90 `-2.11%`, MFE180 `143.56%`, MAE180 `-2.11%`, post-peak DD180 `-10.87%`.
- R13 reading: `current_profile_too_slow_if_debt_watch_blocks_all_stage2`.

### R13ATPV153_035760_CJENM_2024_Q1_TURNAROUND_LOSS_QUALITY_BREAK — CJ ENM (035760)

- trigger / entry: `2024-05-09` → `2024-05-10` at `88600`.
- evidence: Q1 profitability recovery looked like a clean accounting turn, but the listed-company economics still carried platform/content subsidiary loss-quality risk; price validation was weak.
- source: https://www.asiae.co.kr/en/article/2024050914492233349
- price path: MFE90 `7.11%`, MAE90 `-22.80%`, MFE180 `7.11%`, MAE180 `-41.99%`, post-peak DD180 `-45.84%`.
- R13 reading: `current_profile_false_positive_if_one_quarter_OP_turnaround_overweighted`.

### R13ATPV153_051900_LGHNH_2024_Q1_REBOUND_LEGACY_PROFIT_BREAK — LG생활건강 (051900)

- trigger / entry: `2024-04-25` → `2024-04-26` at `392000`.
- evidence: Q1 sales and OP rebounded, but the legacy beauty/channel profit bridge was not clean enough to protect the 180D path; accounting rebound needed durability proof.
- source: https://www.asiae.co.kr/en/article/2024042516153988285
- price path: MFE90 `22.45%`, MAE90 `-18.11%`, MFE180 `22.45%`, MAE180 `-24.87%`, post-peak DD180 `-38.65%`.
- R13 reading: `current_profile_should_cap_at_Stage4B_after_initial_reprice`.

### R13ATPV153_096770_SKINNO_2023_AMPC_LOSS_ACCOUNTING_BRIDGE_FAIL — SK이노베이션 (096770)

- trigger / entry: `2023-07-28` → `2023-07-28` at `189500`.
- evidence: Battery revenue/ramp and AMPC-style optimism did not override consolidated operating loss and cash-quality risk; price validated a 4B loss-quality guard.
- source: https://askinno.com/global/archives/15259
- price path: MFE90 `19.79%`, MAE90 `-36.62%`, MFE180 `19.79%`, MAE180 `-45.86%`, post-peak DD180 `-54.85%`.
- R13 reading: `current_profile_false_positive_if_AMPC_or_revenue_growth_overweights_loss_quality`.

### R13ATPV153_361610_SKIET_2024_UTILIZATION_LOSS_HARD_4C — SK아이이테크놀로지 (361610)

- trigger / entry: `2024-04-30` → `2024-04-30` at `59100`.
- evidence: Operating loss, weak customer demand and utilization collapse give a company-level thesis break, not just a sector slowdown headline.
- source: https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220
- price path: MFE90 `5.25%`, MAE90 `-48.73%`, MFE180 `5.25%`, MAE180 `-63.03%`, post-peak DD180 `-64.87%`.
- R13 reading: `current_profile_should_route_to_hard_4C`.


## 7. 4B Local vs Full-Window Audit

| case_id | local 4B? | full 4B? | hard 4C? | audit note |
|---|---|---|---|---|
| R13ATPV153_003230_SAMYANG_2025_EXPORT_CLEAN_EARNINGS_CONTROL | true | false | false | fast reprice and later drawdown require profit-lock, but accounting bridge remains valid |
| R13ATPV153_267260_HDHE_2025_ORDER_BACKLOG_EARNINGS_CONTROL | false | false | false | orders/backlog/OP validated; shallow MAE and huge MFE |
| R13ATPV153_005830_DBINS_2024_IFRS17_CSM_KICS_RETURN_CONTROL | true | true | false | deep interim MAE; accept Yellow but delay Green until K-ICS/return execution continues |
| R13ATPV153_015760_KEPCO_2025_TARIFF_DEBT_CASH_REPAIR_EXCEPTION | false | false | false | debt warning remains 4B, but tariff/profit repair should not block Stage2 entirely |
| R13ATPV153_035760_CJENM_2024_Q1_TURNAROUND_LOSS_QUALITY_BREAK | true | true | false | Q1 turn did not become durable listed-company economics |
| R13ATPV153_051900_LGHNH_2024_Q1_REBOUND_LEGACY_PROFIT_BREAK | true | true | false | initial MFE confirms tradability; later MAE confirms weak durability |
| R13ATPV153_096770_SKINNO_2023_AMPC_LOSS_ACCOUNTING_BRIDGE_FAIL | true | true | false | AMPC/ramp language cannot override consolidated loss quality |
| R13ATPV153_361610_SKIET_2024_UTILIZATION_LOSS_HARD_4C | true | true | true | utilization/customer-demand loss collapse is a company-level thesis break |

## 8. Machine-Readable Trigger Rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R13_153_01","case_id":"R13ATPV153_003230_SAMYANG_2025_EXPORT_CLEAN_EARNINGS_CONTROL","symbol":"003230","company_name":"삼양식품","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C18_CONSUMER_EXPORT_CHANNEL_REORDER / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage3-Green","trigger_date":"2025-05-15","evidence_available_at_that_date":true,"evidence_source":"Asia Business Daily, 2025-05-15, Samyang Foods Q1 2025 record operating profit and overseas sales expansion","evidence_source_url":"https://www.asiae.co.kr/en/article/2025051516275873139","stage2_evidence_fields":["official/direct source","accounting-to-cash bridge","price validation"],"stage3_evidence_fields":["multi-field evidence bridge","forward price validation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-05-16","entry_price":1180000.0,"MFE_30D_pct":19.83,"MFE_90D_pct":41.1,"MFE_180D_pct":41.1,"MAE_30D_pct":-8.73,"MAE_90D_pct":-8.73,"MAE_180D_pct":-14.49,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-09-11","peak_price":1665000.0,"drawdown_after_peak_pct":-39.4,"four_b_local_peak_proximity":"computed_from_30D_90D_path","four_b_full_window_peak_proximity":"computed_from_180D_path","four_b_timing_verdict":"4B_watch_or_4C_by_accounting_trust_quality","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"watch_or_profit_lock","trigger_outcome_label":"positive_control_clean_earnings_cash_conversion","current_profile_verdict":"current_profile_should_accept_with_4B_profit_lock_after_fast_reprice","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|003230|2025-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"positive_control_clean_earnings_cash_conversion","price_note":"Stock-Web rows available through 2026-02-20; 187 forward rows after entry, so 180D window complete."}
{"row_type":"trigger","trigger_id":"R13_153_02","case_id":"R13ATPV153_267260_HDHE_2025_ORDER_BACKLOG_EARNINGS_CONTROL","symbol":"267260","company_name":"HD현대일렉트릭","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C02_POWER_GRID_DATACENTER_CAPEX","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage3-Green","trigger_date":"2025-04-22","evidence_available_at_that_date":true,"evidence_source":"Yonhap, 2025-04-22, HD Hyundai Electric Q1 sales, OP, orders and backlog","evidence_source_url":"https://en.yna.co.kr/view/AEN20250422006151320","stage2_evidence_fields":["official/direct source","accounting-to-cash bridge","price validation"],"stage3_evidence_fields":["multi-field evidence bridge","forward price validation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-04-23","entry_price":297500.0,"MFE_30D_pct":45.55,"MFE_90D_pct":74.79,"MFE_180D_pct":228.07,"MAE_30D_pct":-2.02,"MAE_90D_pct":-2.02,"MAE_180D_pct":-2.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-04","peak_price":976000.0,"drawdown_after_peak_pct":-24.59,"four_b_local_peak_proximity":"computed_from_30D_90D_path","four_b_full_window_peak_proximity":"computed_from_180D_path","four_b_timing_verdict":"4B_watch_or_4C_by_accounting_trust_quality","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"watch_or_profit_lock","trigger_outcome_label":"positive_control_order_backlog_earnings_conversion","current_profile_verdict":"current_profile_should_accept","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|267260|2025-04-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"positive_control_order_backlog_earnings_conversion","price_note":"Clean Stock-Web 180D window; immediate MAE shallow and price validation strong."}
{"row_type":"trigger","trigger_id":"R13_153_03","case_id":"R13ATPV153_005830_DBINS_2024_IFRS17_CSM_KICS_RETURN_CONTROL","symbol":"005830","company_name":"DB손해보험","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C22_INSURANCE_RATE_CYCLE_RESERVE","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage3-Yellow","trigger_date":"2024-11-14","evidence_available_at_that_date":true,"evidence_source":"DB Insurance 2024 3Q KPI / IR presentation, CSM/K-ICS/shareholder return policy","evidence_source_url":"https://www.idbins.com/pcweb/bizxpress/cmy/inv/ir/__etc/2024.3Q_DB%20Insurance%281%29.pdf","stage2_evidence_fields":["official/direct source","accounting-to-cash bridge","price validation"],"stage3_evidence_fields":["multi-field evidence bridge","forward price validation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-15","entry_price":101600.0,"MFE_30D_pct":11.91,"MFE_90D_pct":11.91,"MFE_180D_pct":45.96,"MAE_30D_pct":-2.46,"MAE_90D_pct":-15.16,"MAE_180D_pct":-23.72,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-14","peak_price":148300.0,"drawdown_after_peak_pct":-17.94,"four_b_local_peak_proximity":"computed_from_30D_90D_path","four_b_full_window_peak_proximity":"computed_from_180D_path","four_b_timing_verdict":"4B_watch_or_4C_by_accounting_trust_quality","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"watch_or_profit_lock","trigger_outcome_label":"positive_with_drawdown_watch_IFRS17_CSM_KICS_return","current_profile_verdict":"current_profile_should_accept_but_green_requires_drawdown_aware_confirmation","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005830|2024-11-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"positive_with_drawdown_watch_IFRS17_CSM_KICS_return","price_note":"Deep interim MAE means accounting-quality positive still needs staged confirmation."}
{"row_type":"trigger","trigger_id":"R13_153_04","case_id":"R13ATPV153_015760_KEPCO_2025_TARIFF_DEBT_CASH_REPAIR_EXCEPTION","symbol":"015760","company_name":"한국전력","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage2-Actionable","trigger_date":"2025-02-28","evidence_available_at_that_date":true,"evidence_source":"Yonhap, 2025-02-28, KEPCO shifted to black in 2024 but retained heavy accumulated debt burden","evidence_source_url":"https://en.yna.co.kr/view/AEN20250228005251320","stage2_evidence_fields":["official/direct source","accounting-to-cash bridge","price validation"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015760/2025.csv","profile_path":"atlas/symbol_profiles/015/015760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-04","entry_price":21350.0,"MFE_30D_pct":10.54,"MFE_90D_pct":92.74,"MFE_180D_pct":143.56,"MAE_30D_pct":-2.11,"MAE_90D_pct":-2.11,"MAE_180D_pct":-2.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-18","peak_price":52000.0,"drawdown_after_peak_pct":-10.87,"four_b_local_peak_proximity":"computed_from_30D_90D_path","four_b_full_window_peak_proximity":"computed_from_180D_path","four_b_timing_verdict":"4B_watch_or_4C_by_accounting_trust_quality","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"watch_or_profit_lock","trigger_outcome_label":"positive_exception_tariff_profit_debt_watch","current_profile_verdict":"current_profile_too_slow_if_debt_watch_blocks_all_stage2","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|015760|2025-03-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"positive_exception_tariff_profit_debt_watch","price_note":"A useful overblock exception: heavy debt is a 4B watch, but tariff/profit repair deserved Actionable tracking."}
{"row_type":"trigger","trigger_id":"R13_153_05","case_id":"R13ATPV153_035760_CJENM_2024_Q1_TURNAROUND_LOSS_QUALITY_BREAK","symbol":"035760","company_name":"CJ ENM","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C27_CONTENT_IP_GLOBAL_MONETIZATION / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4B","trigger_date":"2024-05-09","evidence_available_at_that_date":true,"evidence_source":"Asia Business Daily, 2024-05-09, CJ ENM Q1 2024 profitability recovery","evidence_source_url":"https://www.asiae.co.kr/en/article/2024050914492233349","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["accounting or trust-quality warning","forward price validation weak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035760/2024.csv","profile_path":"atlas/symbol_profiles/035/035760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-10","entry_price":88600.0,"MFE_30D_pct":7.11,"MFE_90D_pct":7.11,"MFE_180D_pct":7.11,"MAE_30D_pct":-9.71,"MAE_90D_pct":-22.8,"MAE_180D_pct":-41.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-27","peak_price":94900.0,"drawdown_after_peak_pct":-45.84,"four_b_local_peak_proximity":"computed_from_30D_90D_path","four_b_full_window_peak_proximity":"computed_from_180D_path","four_b_timing_verdict":"4B_watch_or_4C_by_accounting_trust_quality","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"watch_or_profit_lock","trigger_outcome_label":"counterexample_one_quarter_turnaround_vs_loss_quality","current_profile_verdict":"current_profile_false_positive_if_one_quarter_OP_turnaround_overweighted","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|035760|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"counterexample_one_quarter_turnaround_vs_loss_quality","price_note":"MFE capped quickly; 180D trough validates 4B/quality gate."}
{"row_type":"trigger","trigger_id":"R13_153_06","case_id":"R13ATPV153_051900_LGHNH_2024_Q1_REBOUND_LEGACY_PROFIT_BREAK","symbol":"051900","company_name":"LG생활건강","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C19_BRAND_RETAIL_INVENTORY_MARGIN / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4B","trigger_date":"2024-04-25","evidence_available_at_that_date":true,"evidence_source":"Asia Business Daily, 2024-04-25, LG H&H Q1 2024 operating profit rebound","evidence_source_url":"https://www.asiae.co.kr/en/article/2024042516153988285","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["accounting or trust-quality warning","forward price validation weak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":392000.0,"MFE_30D_pct":22.45,"MFE_90D_pct":22.45,"MFE_180D_pct":22.45,"MAE_30D_pct":-4.46,"MAE_90D_pct":-18.11,"MAE_180D_pct":-24.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":480000.0,"drawdown_after_peak_pct":-38.65,"four_b_local_peak_proximity":"computed_from_30D_90D_path","four_b_full_window_peak_proximity":"computed_from_180D_path","four_b_timing_verdict":"4B_watch_or_4C_by_accounting_trust_quality","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"watch_or_profit_lock","trigger_outcome_label":"counterexample_accounting_rebound_not_durable_profit_bridge","current_profile_verdict":"current_profile_should_cap_at_Stage4B_after_initial_reprice","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|051900|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"counterexample_accounting_rebound_not_durable_profit_bridge","price_note":"A positive 30D MFE can coexist with failed 180D validation; do not turn one-quarter rebound into Green."}
{"row_type":"trigger","trigger_id":"R13_153_07","case_id":"R13ATPV153_096770_SKINNO_2023_AMPC_LOSS_ACCOUNTING_BRIDGE_FAIL","symbol":"096770","company_name":"SK이노베이션","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA / C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4B","trigger_date":"2023-07-28","evidence_available_at_that_date":true,"evidence_source":"SK Innovation official newsroom / Yonhap, 2023-07-28, Q2 2023 operating loss with SK On battery loss narrowing but still negative","evidence_source_url":"https://askinno.com/global/archives/15259","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["accounting or trust-quality warning","forward price validation weak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv","profile_path":"atlas/symbol_profiles/096/096770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-28","entry_price":189500.0,"MFE_30D_pct":19.79,"MFE_90D_pct":19.79,"MFE_180D_pct":19.79,"MAE_30D_pct":-10.77,"MAE_90D_pct":-36.62,"MAE_180D_pct":-45.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-01","peak_price":227000.0,"drawdown_after_peak_pct":-54.85,"four_b_local_peak_proximity":"computed_from_30D_90D_path","four_b_full_window_peak_proximity":"computed_from_180D_path","four_b_timing_verdict":"4B_watch_or_4C_by_accounting_trust_quality","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"watch_or_profit_lock","trigger_outcome_label":"counterexample_AMPC_ramp_vs_consolidated_loss_quality","current_profile_verdict":"current_profile_false_positive_if_AMPC_or_revenue_growth_overweights_loss_quality","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|096770|2023-07-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"counterexample_AMPC_ramp_vs_consolidated_loss_quality","price_note":"Post-entry upside existed, but 90D/180D MAE show why accounting loss quality must block positive promotion."}
{"row_type":"trigger","trigger_id":"R13_153_08","case_id":"R13ATPV153_361610_SKIET_2024_UTILIZATION_LOSS_HARD_4C","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_ACCOUNTING_CASH_TRUST_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK / C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4C","trigger_date":"2024-04-30","evidence_available_at_that_date":true,"evidence_source":"Mirae Asset / Maeil Business News, 2024-04-30, Q1 2024 operating loss from weak SK On demand and utilization decline","evidence_source_url":"https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["accounting or trust-quality warning","forward price validation weak"],"stage4c_evidence_fields":["company-level accounting/utilization/trust thesis break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv","profile_path":"atlas/symbol_profiles/361/361610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-30","entry_price":59100.0,"MFE_30D_pct":5.25,"MFE_90D_pct":5.25,"MFE_180D_pct":5.25,"MAE_30D_pct":-27.75,"MAE_90D_pct":-48.73,"MAE_180D_pct":-63.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":62200.0,"drawdown_after_peak_pct":-64.87,"four_b_local_peak_proximity":"computed_from_30D_90D_path","four_b_full_window_peak_proximity":"computed_from_180D_path","four_b_timing_verdict":"4B_watch_or_4C_by_accounting_trust_quality","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"hard_4C","trigger_outcome_label":"counterexample_hard_4C_utilization_loss_quality_break","current_profile_verdict":"current_profile_should_route_to_hard_4C","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|361610|2024-04-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"counterexample_hard_4C_utilization_loss_quality_break","price_note":"Low MFE and deep MAE make this a clean hard-4C accounting/utilization break."}
```

## 9. Score Simulation Rows

```jsonl
{"row_type":"score_simulation","case_id":"R13ATPV153_003230_SAMYANG_2025_EXPORT_CLEAN_EARNINGS_CONTROL","profile":"current_e2r_2_2_proxy","symbol":"003230","trigger_type":"Stage3-Green","total_score_before_shadow_gate":88,"stage_before_shadow_gate":"Stage3-Yellow","total_score_after_shadow_gate":90,"stage_after_shadow_gate":"Stage3-Green","raw_component_score_breakdown_before":{"EPS":18,"Visibility":20,"Bottleneck":8,"Mispricing":12,"Valuation":12,"Capital":10,"Info":10},"shadow_gate_adjustment":{"official_source_credit":2,"accounting_cash_bridge_credit":3,"loss_quality_penalty":0,"trust_break_penalty":0,"price_validation_penalty":0},"shadow_axis":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","outcome_MFE90_pct":41.1,"outcome_MAE90_pct":-8.73}
{"row_type":"score_simulation","case_id":"R13ATPV153_267260_HDHE_2025_ORDER_BACKLOG_EARNINGS_CONTROL","profile":"current_e2r_2_2_proxy","symbol":"267260","trigger_type":"Stage3-Green","total_score_before_shadow_gate":88,"stage_before_shadow_gate":"Stage3-Yellow","total_score_after_shadow_gate":90,"stage_after_shadow_gate":"Stage3-Green","raw_component_score_breakdown_before":{"EPS":18,"Visibility":20,"Bottleneck":8,"Mispricing":12,"Valuation":12,"Capital":10,"Info":10},"shadow_gate_adjustment":{"official_source_credit":2,"accounting_cash_bridge_credit":3,"loss_quality_penalty":0,"trust_break_penalty":0,"price_validation_penalty":0},"shadow_axis":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","outcome_MFE90_pct":74.79,"outcome_MAE90_pct":-2.02}
{"row_type":"score_simulation","case_id":"R13ATPV153_005830_DBINS_2024_IFRS17_CSM_KICS_RETURN_CONTROL","profile":"current_e2r_2_2_proxy","symbol":"005830","trigger_type":"Stage3-Yellow","total_score_before_shadow_gate":80,"stage_before_shadow_gate":"Stage3-Yellow","total_score_after_shadow_gate":80,"stage_after_shadow_gate":"Stage3-Yellow","raw_component_score_breakdown_before":{"EPS":18,"Visibility":20,"Bottleneck":8,"Mispricing":12,"Valuation":12,"Capital":10,"Info":10},"shadow_gate_adjustment":{"official_source_credit":2,"accounting_cash_bridge_credit":3,"loss_quality_penalty":0,"trust_break_penalty":0,"price_validation_penalty":0},"shadow_axis":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","outcome_MFE90_pct":11.91,"outcome_MAE90_pct":-15.16}
{"row_type":"score_simulation","case_id":"R13ATPV153_015760_KEPCO_2025_TARIFF_DEBT_CASH_REPAIR_EXCEPTION","profile":"current_e2r_2_2_proxy","symbol":"015760","trigger_type":"Stage2-Actionable","total_score_before_shadow_gate":72,"stage_before_shadow_gate":"Stage2","total_score_after_shadow_gate":74,"stage_after_shadow_gate":"Stage2-Actionable","raw_component_score_breakdown_before":{"EPS":18,"Visibility":20,"Bottleneck":8,"Mispricing":12,"Valuation":12,"Capital":10,"Info":10},"shadow_gate_adjustment":{"official_source_credit":2,"accounting_cash_bridge_credit":3,"loss_quality_penalty":0,"trust_break_penalty":0,"price_validation_penalty":0},"shadow_axis":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","outcome_MFE90_pct":92.74,"outcome_MAE90_pct":-2.11}
{"row_type":"score_simulation","case_id":"R13ATPV153_035760_CJENM_2024_Q1_TURNAROUND_LOSS_QUALITY_BREAK","profile":"current_e2r_2_2_proxy","symbol":"035760","trigger_type":"Stage4B","total_score_before_shadow_gate":70,"stage_before_shadow_gate":"Stage2","total_score_after_shadow_gate":62,"stage_after_shadow_gate":"Stage4B","raw_component_score_breakdown_before":{"EPS":18,"Visibility":20,"Bottleneck":8,"Mispricing":12,"Valuation":12,"Capital":10,"Info":10},"shadow_gate_adjustment":{"official_source_credit":0,"accounting_cash_bridge_credit":0,"loss_quality_penalty":-5,"trust_break_penalty":-3,"price_validation_penalty":-4},"shadow_axis":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","outcome_MFE90_pct":7.11,"outcome_MAE90_pct":-22.8}
{"row_type":"score_simulation","case_id":"R13ATPV153_051900_LGHNH_2024_Q1_REBOUND_LEGACY_PROFIT_BREAK","profile":"current_e2r_2_2_proxy","symbol":"051900","trigger_type":"Stage4B","total_score_before_shadow_gate":70,"stage_before_shadow_gate":"Stage2","total_score_after_shadow_gate":62,"stage_after_shadow_gate":"Stage4B","raw_component_score_breakdown_before":{"EPS":18,"Visibility":20,"Bottleneck":8,"Mispricing":12,"Valuation":12,"Capital":10,"Info":10},"shadow_gate_adjustment":{"official_source_credit":0,"accounting_cash_bridge_credit":0,"loss_quality_penalty":-5,"trust_break_penalty":-3,"price_validation_penalty":-4},"shadow_axis":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","outcome_MFE90_pct":22.45,"outcome_MAE90_pct":-18.11}
{"row_type":"score_simulation","case_id":"R13ATPV153_096770_SKINNO_2023_AMPC_LOSS_ACCOUNTING_BRIDGE_FAIL","profile":"current_e2r_2_2_proxy","symbol":"096770","trigger_type":"Stage4B","total_score_before_shadow_gate":70,"stage_before_shadow_gate":"Stage2","total_score_after_shadow_gate":62,"stage_after_shadow_gate":"Stage4B","raw_component_score_breakdown_before":{"EPS":18,"Visibility":20,"Bottleneck":8,"Mispricing":12,"Valuation":12,"Capital":10,"Info":10},"shadow_gate_adjustment":{"official_source_credit":0,"accounting_cash_bridge_credit":0,"loss_quality_penalty":-5,"trust_break_penalty":-3,"price_validation_penalty":-4},"shadow_axis":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","outcome_MFE90_pct":19.79,"outcome_MAE90_pct":-36.62}
{"row_type":"score_simulation","case_id":"R13ATPV153_361610_SKIET_2024_UTILIZATION_LOSS_HARD_4C","profile":"current_e2r_2_2_proxy","symbol":"361610","trigger_type":"Stage4C","total_score_before_shadow_gate":70,"stage_before_shadow_gate":"Stage2","total_score_after_shadow_gate":58,"stage_after_shadow_gate":"Stage4C","raw_component_score_breakdown_before":{"EPS":18,"Visibility":20,"Bottleneck":8,"Mispricing":12,"Valuation":12,"Capital":10,"Info":10},"shadow_gate_adjustment":{"official_source_credit":0,"accounting_cash_bridge_credit":0,"loss_quality_penalty":-5,"trust_break_penalty":-5,"price_validation_penalty":-4},"shadow_axis":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","outcome_MFE90_pct":5.25,"outcome_MAE90_pct":-48.73}
```

## 10. Shadow Rule Candidate

```text
new_axis_proposed = R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE
rule_candidate = For cross-archetype accounting/trust events, do not score an earnings headline as Stage2-Actionable unless at least one accounting figure is tied to a second validation bridge: cash conversion, order/backlog, CSM/K-ICS/shareholder return mechanics, tariff receivable repair, utilization recovery, or regulatory/trust clearance. If accounting headline is one-quarter-only, loss-quality dominated, utilization-collapsed, or unsupported by cash/trust conversion, cap at Stage4B. If company-level operating loss/utilization collapse or hard trust break is confirmed, route to Stage4C.
existing_axis_strengthened = stage2_required_bridge; full_4b_requires_non_price_evidence; hard_4c_confirmation; drawdown_aware_confirmation; information_confidence_gate
existing_axis_weakened = none
production_scoring_changed = false
shadow_weight_only = true
```

Suggested shadow weight direction for R13 accounting/trust scope:

```text
before EPS/Vis/Bott/Mis/Val/Cap/Info = 8/12/5/10/8/20/37
after  EPS/Vis/Bott/Mis/Val/Cap/Info = 8/14/5/9/7/22/35
delta                                  0/+2/0/-1/-1/+2/-2
reading = keep information trust high, but shift a small part of generic Info into Visibility and Capital/Cash confirmation
```

## 11. Residual Contribution Summary

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","new_axis_proposed":"R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE","positive_case_count":4,"counterexample_count":4,"stage4b_case_count":3,"stage4c_case_count":1,"current_profile_error_count":5,"new_independent_case_count":8,"source_proxy_only_count":2,"evidence_url_pending_count":0,"rows_missing_required_mfe_mae":0,"avg_positive_MFE90_pct":55.13,"avg_positive_MAE90_pct":-7.00,"avg_counter_MFE90_pct":13.65,"avg_counter_MAE90_pct":-31.56,"rule_contribution":"separate official accounting evidence that converts to cash/order/backlog/CSM/tariff repair from one-quarter rebound or loss-quality dominated accounting events"}
```

## 12. Batch Ingest Self-Audit

```text
filename_regex_pass = true
filename_round_matches_metadata = true
filename_loop_matches_metadata = true
round_sector_consistency = pass
canonical_archetype_valid = true
trigger_type_canonical_stage_label_only = true
all_trigger_rows_have_MFE_30D_pct = true
all_trigger_rows_have_MFE_90D_pct = true
all_trigger_rows_have_MFE_180D_pct = true
all_trigger_rows_have_MAE_30D_pct = true
all_trigger_rows_have_MAE_90D_pct = true
all_trigger_rows_have_MAE_180D_pct = true
calibration_usable_trigger_count = 8
dedupe_for_aggregate_rows = 8
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not apply this MD directly as a production patch. First run the cumulative v12 calibration command with --include-archive, parse this file as one R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION result, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and compare against loop 152 accounting-trust rows. If representative rows survive validation, consider a shadow-only rule axis named R13_ACCOUNTING_CASH_TRUST_PRICE_VALIDATION_GATE. The rule should require accounting headlines to be tied to a second bridge family: cash conversion, order/backlog, CSM/K-ICS/shareholder return mechanics, tariff receivable repair, utilization recovery, or regulatory/trust clearance. Do not loosen Stage3-Green thresholds. Do not apply a blanket accounting-event penalty. Preserve positive controls where price validation and accounting-cash bridge are aligned.
```

## 14. Completed State

```text
completed_round = R13
completed_loop = 153
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 taxonomy repair — R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, loop 152 follow-up with non-duplicate case set
next_recommended_archetypes = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL; R13_CROSS_ARCHETYPE_4B_4C_REDTEAM; C05_EPC_MEGA_CONTRACT_MARGIN_GAP; C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
