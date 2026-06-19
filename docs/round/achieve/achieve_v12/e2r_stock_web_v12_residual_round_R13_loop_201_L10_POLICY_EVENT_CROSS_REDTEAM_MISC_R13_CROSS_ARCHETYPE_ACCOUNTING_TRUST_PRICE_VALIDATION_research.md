# E2R Stock-Web v12 Residual Research — R13 Accounting Trust / Price Validation Holdout V2

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R13
selected_loop = 201
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id = R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 representative compression / accounting-trust direct-source refresh
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection Rationale

The latest no-repeat ledger says the cumulative V12 corpus is no longer in a simple row-fill phase: all C01~C32 archetypes have crossed the 80-row area, while the remaining work is direct URL/proxy quality, representative compression, false-positive taxonomy, and residual error cleanup. This loop therefore does **not** create another sector-specific positive screen. It compresses recent C30/PF, C31/policy execution, C32/control premium, C21/C22 financial capital-return and reserve rows into one R13 accounting-trust / price-validation checkpoint.

The core question is narrow:

```text
When a price path is strong after an accounting, reserve, tariff, liquidity, tender, or control-premium event,
should the engine treat it as operating rerating?
```

Answer from this holdout: **no, not automatically.** Strong MFE can validate a catalyst, but the R13 gate must still separate price-catalyst mechanics from operating EPS/FCF/ROE/cashflow conversion.

## 2. Price Atlas Validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_columns = d,o,h,l,c,v,a,mc,s,m
corporate_action_policy = block if candidate date overlaps entry_date~D+180
```

All usable rows below have actual entry OHLCV and 30/90/180D MFE/MAE from Stock-Web tradable shards. No usable row has an in-window corporate-action candidate or insufficient 180D forward window.

## 3. Batch Self-Audit

```text
source_sector_case_reused_count = 11
new_independent_case_count_for_r13_scope = 11
new_independent_trigger_count_for_r13_scope = 11
unique_symbol_count = 11
unique_source_canonical_count = 5

source_canonical_focus:
- C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
- C22_INSURANCE_RATE_CYCLE_RESERVE
- C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
- C31_POLICY_SUBSIDY_LEGISLATION_EVENT
- C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP

Stage2-Actionable_count = 4
Stage4B_count = 6
Stage4C_count = 1
high_MAE_180D_count_MAE_le_-20 = 5
deep_MAE_180D_count_MAE_le_-40 = 2

source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0

minimum_new_independent_case_ratio = 1.00
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 4. Trigger Price Table

| ticker | name | source canonical | trigger | entry OHLCV | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak/trough 180D | role |
|---|---|---|---|---|---:|---:|---:|---|---|
| 034300 | 신세계건설 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage4B | 2024-03-21 O 10900 H 11190 L 10830 C 10890 V 2875 | 6.15/-9.55 | 71.26/-9.55 | 71.26/-9.55 | 2024-05-30 / 2024-04-26 | liquidity_support_4b_offset |
| 002410 | 범양건영 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage4C | 2023-12-21 O 2175 H 2230 L 2135 C 2185 V 180833 | 7.32/-22.47 | 7.32/-38.22 | 7.32/-48.51 | 2024-01-02 / 2024-09-09 | weak_offset_hard4c_control |
| 035890 | 서희건설 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-Actionable | 2024-08-14 O 1308 H 1352 L 1308 C 1342 V 408782 | 17.29/-2.53 | 25.19/-2.53 | 33.46/-2.53 | 2025-04-22 / 2024-08-14 | working_capital_reopen_positive_control |
| 014790 | HL D&I 한라 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage4B | 2025-02-06 O 2230 H 2280 L 2070 C 2280 V 50488 | 9.21/-9.21 | 24.56/-9.21 | 35.75/-9.21 | 2025-08-08 / 2025-02-06 | ugly_quarter_offset_watch |
| 055550 | 신한지주 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable | 2024-07-26 O 54200 H 58400 L 54200 C 58000 V 3558607 | 11.38/-11.03 | 11.38/-14.48 | 11.38/-26.72 | 2024-08-26 / 2025-04-09 | capital_return_direct_mechanics_positive_control |
| 001450 | 현대해상 | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage4B | 2025-05-14 O 21950 H 22300 L 21750 C 22150 V 242079 | 23.02/-1.81 | 38.60/-1.81 | 42.89/-1.81 | 2025-12-24 / 2025-05-14 | one_time_reserve_base_effect_4b |
| 015760 | 한국전력 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2023-11-09 O 17900 H 17990 L 17150 C 17190 V 2290944 | 14.89/-2.56 | 48.05/-2.56 | 48.05/-2.56 | 2024-03-14 / 2023-11-10 | tariff_to_profit_execution_positive_control |
| 009830 | 한화솔루션 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage4B | 2024-02-22 O 32950 H 33100 L 28900 C 29300 V 4885784 | 12.97/-9.56 | 17.92/-21.50 | 17.92/-43.48 | 2024-05-28 / 2024-11-14 | subsidy_with_oversupply_watch |
| 010130 | 고려아연 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-Actionable | 2024-09-13 O 660000 H 690000 L 655000 C 666000 V 586718 | 131.68/-1.65 | 261.41/-1.65 | 261.41/-3.45 | 2024-12-06 / 2025-04-09 | control_premium_positive_control_green_blocker |
| 041510 | 에스엠 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage4B | 2023-03-13 O 135000 H 135000 L 111300 C 113100 V 5457572 | 19.36/-22.55 | 19.36/-22.55 | 29.97/-26.70 | 2023-08-29 / 2023-12-04 | tender_fade_4b_watch |
| 011200 | HMM | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage4B | 2024-02-07 O 19030 H 20200 L 17500 C 19080 V 5677567 | 5.87/-18.45 | 5.87/-25.31 | 9.01/-25.31 | 2024-07-03 / 2024-04-19 | deal_failure_4b_watch |

## 5. Evidence Table

| ticker | evidence summary | direct URL | price validation |
|---|---|---|---|
| 034300 신세계건설 | PF/unsold-site liquidity stress, high debt ratio, hybrid-securities liquidity support; explicit offset means 4B/watch, not sticky 4C. | https://www.asiae.co.kr/en/article/2024040307311575157 | atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv / atlas/symbol_profiles/034/034300.json |
| 002410 범양건영 | Small contractor loss/cost-liability stress proxy; forward path confirms severe thesis-break risk when offset quality is weak. | https://www.mk.co.kr/en/realestate/11242716 | atlas/ohlcv_tradable_by_symbol_year/002/002410/2023.csv / atlas/symbol_profiles/002/002410.json |
| 035890 서희건설 | Order/cash-flow bridge and buyback/order-flow evidence make this a Stage2-Actionable reopen rather than PF-basket false positive. | https://www.marketscreener.com/quote/stock/SEOHEE-CONSTRUCTION-CO-LT-6496322/ | atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv / atlas/symbol_profiles/035/035890.json |
| 014790 HL D&I 한라 | Construction balance-sheet pressure row with later offset/watch pattern; avoid hard 4C absent explicit liquidity collapse. | https://www.mk.co.kr/en/realestate/11242716 | atlas/ohlcv_tradable_by_symbol_year/014/014790/2025.csv / atlas/symbol_profiles/014/014790.json |
| 055550 신한지주 | Value-up plan uses share count reduction via buyback/cancellation and 50% shareholder-return target; direct mechanics preserve Stage2-Actionable but high MAE blocks Green. | https://www.koreaherald.com/article/3441569 | atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv / atlas/symbol_profiles/055/055550.json |
| 001450 현대해상 | 2025 Q1 net-profit decline was distorted by prior-year one-off reserve reversal; CSM/K-ICS offset argues watch before hard 4C. | https://en.topdaily.kr/articles/6530 | atlas/ohlcv_tradable_by_symbol_year/001/001450/2025.csv / atlas/symbol_profiles/001/001450.json |
| 015760 한국전력 | Tariff hikes translated into Q3 2023 profit and electricity-sales growth; policy permission crossed into earnings bridge. | https://en.yna.co.kr/view/AEN20231113005751320 | atlas/ohlcv_tradable_by_symbol_year/015/015760/2023.csv / atlas/symbol_profiles/015/015760.json |
| 009830 한화솔루션 | AMPC/IRA support is real but solar oversupply/utilization drag requires 4B watch until ex-subsidy margin appears. | https://www.reuters.com/markets/companies/009830.KS/ | atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv / atlas/symbol_profiles/009/009830.json |
| 010130 고려아연 | MBK/Young Poong tender offer generated control-premium price path; not an operating Green unless post-event earnings/cashflow bridge appears. | https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/ | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv / atlas/symbol_profiles/010/010130.json |
| 041510 에스엠 | HYBE/Kakao tender battle and HYBE withdrawal create control-premium fade; first route is 4B/watch, not operating thesis 4C. | https://www.reuters.com/markets/deals/hybe-drops-bid-take-over-sm-entertainment-2023-03-12/ | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv / atlas/symbol_profiles/041/041510.json |
| 011200 HMM | Harim/HMM sale talks fell apart; deal-failure premium fade is 4B/watch unless operating cashflow/financing damage follows. | https://en.yna.co.kr/view/AEN20240207001451320 | atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv / atlas/symbol_profiles/011/011200.json |

## 6. Case Interpretation

### 6.1 C30 construction/PF and liquidity rows

Shinsegae E&C and HL D&I Halla show why a construction/PF ugly headline should first become **4B/watch** when liquidity support, cost-rate normalization, or backlog/order visibility survives. Bumyang Construction is the hard-control row: the price path has a deep -48.51% 180D MAE and only +7.32% 180D MFE, so weak-offset construction stress remains a valid hard-break warning. Seohee Construction is the opposite control: working-capital/order-flow evidence and a +33.46% 180D MFE argue for Stage2-Actionable reopen, but not Green.

### 6.2 C21/C22 financial capital-return and reserve rows

Shinhan's value-up/buyback-cancellation plan is a real second bridge; it is not merely a low-PBR headline. Yet the same row has -26.72% 180D MAE, so R13 treats it as **Actionable preserved, Green blocked**. Hyundai Marine & Fire shows the reserve-accounting mirror image: a net-profit decline distorted by prior-year one-off reserve reversal should not become hard 4C when CSM/K-ICS offset survives.

### 6.3 C31 policy execution rows

KEPCO's tariff row is the cleanest policy-to-cashflow positive control: tariff hikes translated into Q3 profit and electricity-sales growth. Hanwha Solutions is the guardrail: subsidy language and AMPC support are not enough if oversupply/utilization drag remains; that is 4B/watch until ex-subsidy economics repeats.

### 6.4 C32 governance/control-premium rows

Korea Zinc, SM Entertainment, and HMM all demonstrate that control-premium and tender mechanics can generate large price paths without becoming operating Stage3-Green. Korea Zinc's +261.41% 180D MFE is a control-premium path first. SM and HMM are fade/watch examples: tender battle withdrawal or deal failure routes to 4B/watch unless an operating EPS/FCF/cashflow bridge appears.

## 7. Residual Contribution

```text
rule_candidate = R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2

core_residual:
- Price validation is not operating validation.
- Accounting, reserve, liquidity, tariff, tender, and control-premium events can justify Stage2/Stage2-Actionable or 4B/4C watch.
- Stage3-Yellow / Stage3-Green require an operating bridge: EPS, FCF, cashflow, working-capital, ROE/TBVPS accretion, repeated capital-return execution, or post-event integration economics.
- Strong MFE after a control or policy event should not loosen Green.
- High MAE after a valid second bridge should block Yellow/Green first; it should not delete Stage2-Actionable.
- Hard 4C requires confirmed non-price thesis break plus weak offset quality.
```

## 8. Shadow Rule Candidate

```yaml
shadow_rule_id: R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2
scope:
  large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
  canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
condition:
  any_event_family:
    - accounting_reserve_item
    - liquidity_support_or_pf_stress
    - tariff_or_subsidy_policy
    - tender_offer_or_control_premium
    - capital_return_valueup
  observed_price_path:
    mfe_180d_pct: positive_or_strong
rule:
  - do_not_convert_price_path_to_operating_green_without_second_bridge
  - require_eps_fcf_roe_tbvps_cashflow_or_working_capital_bridge_for_yellow_green
  - if high_mae_and_valid_bridge: preserve_stage2_actionable_but_block_green
  - if confirmed_thesis_break_and_weak_offset: allow_hard_4c
production_scoring_changed: false
shadow_weight_only: true
```

## 9. Machine-Readable JSONL Trigger Rows

```jsonl
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","case_id":"R13_ACCOUNTING_V2_01_034300_2024-03-21","symbol":"034300","company_name_kr":"신세계건설","trigger_type":"Stage4B","entry_date":"2024-03-21","entry_price":10890.0,"entry_ohlcv":{"o":10900.0,"h":11190.0,"l":10830.0,"c":10890.0,"v":2875.0},"mfe_30d_pct":6.15,"mae_30d_pct":-9.55,"mfe_90d_pct":71.26,"mae_90d_pct":-9.55,"mfe_180d_pct":71.26,"mae_180d_pct":-9.55,"peak_180d_date":"2024-05-30","trough_180d_date":"2024-04-26","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv","profile_path":"atlas/symbol_profiles/034/034300.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://www.asiae.co.kr/en/article/2024040307311575157","source_proxy_only":false,"evidence_url_pending":false,"case_role":"liquidity_support_4b_offset","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":8,"bottleneck_pricing":2,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":4,"information_confidence":9},"score_simulation_total_proxy":40,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|034300|Stage4B|2024-03-21"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","case_id":"R13_ACCOUNTING_V2_02_002410_2023-12-21","symbol":"002410","company_name_kr":"범양건영","trigger_type":"Stage4C","entry_date":"2023-12-21","entry_price":2185.0,"entry_ohlcv":{"o":2175.0,"h":2230.0,"l":2135.0,"c":2185.0,"v":180833.0},"mfe_30d_pct":7.32,"mae_30d_pct":-22.47,"mfe_90d_pct":7.32,"mae_90d_pct":-38.22,"mfe_180d_pct":7.32,"mae_180d_pct":-48.51,"peak_180d_date":"2024-01-02","trough_180d_date":"2024-09-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/002/002410/2023.csv","profile_path":"atlas/symbol_profiles/002/002410.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://www.mk.co.kr/en/realestate/11242716","source_proxy_only":false,"evidence_url_pending":false,"case_role":"weak_offset_hard4c_control","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":3,"bottleneck_pricing":2,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":4,"information_confidence":9},"score_simulation_total_proxy":30,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|002410|Stage4C|2023-12-21"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","case_id":"R13_ACCOUNTING_V2_03_035890_2024-08-14","symbol":"035890","company_name_kr":"서희건설","trigger_type":"Stage2-Actionable","entry_date":"2024-08-14","entry_price":1342.0,"entry_ohlcv":{"o":1308.0,"h":1352.0,"l":1308.0,"c":1342.0,"v":408782.0},"mfe_30d_pct":17.29,"mae_30d_pct":-2.53,"mfe_90d_pct":25.19,"mae_90d_pct":-2.53,"mfe_180d_pct":33.46,"mae_180d_pct":-2.53,"peak_180d_date":"2025-04-22","trough_180d_date":"2024-08-14","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv","profile_path":"atlas/symbol_profiles/035/035890.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://www.marketscreener.com/quote/stock/SEOHEE-CONSTRUCTION-CO-LT-6496322/","source_proxy_only":false,"evidence_url_pending":false,"case_role":"working_capital_reopen_positive_control","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":12,"bottleneck_pricing":2,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":4,"information_confidence":9},"score_simulation_total_proxy":48,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|035890|Stage2-Actionable|2024-08-14"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","case_id":"R13_ACCOUNTING_V2_04_014790_2025-02-06","symbol":"014790","company_name_kr":"HL D&I 한라","trigger_type":"Stage4B","entry_date":"2025-02-06","entry_price":2280.0,"entry_ohlcv":{"o":2230.0,"h":2280.0,"l":2070.0,"c":2280.0,"v":50488.0},"mfe_30d_pct":9.21,"mae_30d_pct":-9.21,"mfe_90d_pct":24.56,"mae_90d_pct":-9.21,"mfe_180d_pct":35.75,"mae_180d_pct":-9.21,"peak_180d_date":"2025-08-08","trough_180d_date":"2025-02-06","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/014/014790/2025.csv","profile_path":"atlas/symbol_profiles/014/014790.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://www.mk.co.kr/en/realestate/11242716","source_proxy_only":false,"evidence_url_pending":false,"case_role":"ugly_quarter_offset_watch","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":8,"bottleneck_pricing":2,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":4,"information_confidence":9},"score_simulation_total_proxy":40,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|014790|Stage4B|2025-02-06"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","case_id":"R13_ACCOUNTING_V2_05_055550_2024-07-26","symbol":"055550","company_name_kr":"신한지주","trigger_type":"Stage2-Actionable","entry_date":"2024-07-26","entry_price":58000.0,"entry_ohlcv":{"o":54200.0,"h":58400.0,"l":54200.0,"c":58000.0,"v":3558607.0},"mfe_30d_pct":11.38,"mae_30d_pct":-11.03,"mfe_90d_pct":11.38,"mae_90d_pct":-14.48,"mfe_180d_pct":11.38,"mae_180d_pct":-26.72,"peak_180d_date":"2024-08-26","trough_180d_date":"2025-04-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv","profile_path":"atlas/symbol_profiles/055/055550.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://www.koreaherald.com/article/3441569","source_proxy_only":false,"evidence_url_pending":false,"case_role":"capital_return_direct_mechanics_positive_control","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":12,"bottleneck_pricing":2,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":12,"information_confidence":9},"score_simulation_total_proxy":51,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|055550|Stage2-Actionable|2024-07-26"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","case_id":"R13_ACCOUNTING_V2_06_001450_2025-05-14","symbol":"001450","company_name_kr":"현대해상","trigger_type":"Stage4B","entry_date":"2025-05-14","entry_price":22150.0,"entry_ohlcv":{"o":21950.0,"h":22300.0,"l":21750.0,"c":22150.0,"v":242079.0},"mfe_30d_pct":23.02,"mae_30d_pct":-1.81,"mfe_90d_pct":38.6,"mae_90d_pct":-1.81,"mfe_180d_pct":42.89,"mae_180d_pct":-1.81,"peak_180d_date":"2025-12-24","trough_180d_date":"2025-05-14","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2025.csv","profile_path":"atlas/symbol_profiles/001/001450.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://en.topdaily.kr/articles/6530","source_proxy_only":false,"evidence_url_pending":false,"case_role":"one_time_reserve_base_effect_4b","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":8,"bottleneck_pricing":2,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":12,"information_confidence":9},"score_simulation_total_proxy":48,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|001450|Stage4B|2025-05-14"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","case_id":"R13_ACCOUNTING_V2_07_015760_2023-11-09","symbol":"015760","company_name_kr":"한국전력","trigger_type":"Stage2-Actionable","entry_date":"2023-11-09","entry_price":17190.0,"entry_ohlcv":{"o":17900.0,"h":17990.0,"l":17150.0,"c":17190.0,"v":2290944.0},"mfe_30d_pct":14.89,"mae_30d_pct":-2.56,"mfe_90d_pct":48.05,"mae_90d_pct":-2.56,"mfe_180d_pct":48.05,"mae_180d_pct":-2.56,"peak_180d_date":"2024-03-14","trough_180d_date":"2023-11-10","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/015/015760/2023.csv","profile_path":"atlas/symbol_profiles/015/015760.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://en.yna.co.kr/view/AEN20231113005751320","source_proxy_only":false,"evidence_url_pending":false,"case_role":"tariff_to_profit_execution_positive_control","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":12,"bottleneck_pricing":2,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":4,"information_confidence":12},"score_simulation_total_proxy":51,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|015760|Stage2-Actionable|2023-11-09"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","case_id":"R13_ACCOUNTING_V2_08_009830_2024-02-22","symbol":"009830","company_name_kr":"한화솔루션","trigger_type":"Stage4B","entry_date":"2024-02-22","entry_price":29300.0,"entry_ohlcv":{"o":32950.0,"h":33100.0,"l":28900.0,"c":29300.0,"v":4885784.0},"mfe_30d_pct":12.97,"mae_30d_pct":-9.56,"mfe_90d_pct":17.92,"mae_90d_pct":-21.5,"mfe_180d_pct":17.92,"mae_180d_pct":-43.48,"peak_180d_date":"2024-05-28","trough_180d_date":"2024-11-14","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv","profile_path":"atlas/symbol_profiles/009/009830.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://www.reuters.com/markets/companies/009830.KS/","source_proxy_only":false,"evidence_url_pending":false,"case_role":"subsidy_with_oversupply_watch","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":8,"bottleneck_pricing":2,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":4,"information_confidence":12},"score_simulation_total_proxy":38,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|009830|Stage4B|2024-02-22"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","case_id":"R13_ACCOUNTING_V2_09_010130_2024-09-13","symbol":"010130","company_name_kr":"고려아연","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_price":666000.0,"entry_ohlcv":{"o":660000.0,"h":690000.0,"l":655000.0,"c":666000.0,"v":586718.0},"mfe_30d_pct":131.68,"mae_30d_pct":-1.65,"mfe_90d_pct":261.41,"mae_90d_pct":-1.65,"mfe_180d_pct":261.41,"mae_180d_pct":-3.45,"peak_180d_date":"2024-12-06","trough_180d_date":"2025-04-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/","source_proxy_only":false,"evidence_url_pending":false,"case_role":"control_premium_positive_control_green_blocker","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":12,"bottleneck_pricing":2,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":12,"information_confidence":12},"score_simulation_total_proxy":62,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|010130|Stage2-Actionable|2024-09-13"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","case_id":"R13_ACCOUNTING_V2_10_041510_2023-03-13","symbol":"041510","company_name_kr":"에스엠","trigger_type":"Stage4B","entry_date":"2023-03-13","entry_price":113100.0,"entry_ohlcv":{"o":135000.0,"h":135000.0,"l":111300.0,"c":113100.0,"v":5457572.0},"mfe_30d_pct":19.36,"mae_30d_pct":-22.55,"mfe_90d_pct":19.36,"mae_90d_pct":-22.55,"mfe_180d_pct":29.97,"mae_180d_pct":-26.7,"peak_180d_date":"2023-08-29","trough_180d_date":"2023-12-04","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://www.reuters.com/markets/deals/hybe-drops-bid-take-over-sm-entertainment-2023-03-12/","source_proxy_only":false,"evidence_url_pending":false,"case_role":"tender_fade_4b_watch","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":8,"bottleneck_pricing":2,"market_mispricing":5,"valuation_rerating":8,"capital_allocation":12,"information_confidence":12},"score_simulation_total_proxy":49,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|041510|Stage4B|2023-03-13"}
{"row_type":"trigger","v12_schema_version":"v12_stock_web_residual","research_file":"e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md","selected_round":"R13","selected_loop":201,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2","source_large_sector_id":"mixed_L6_L9_L10_policy_cross","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","case_id":"R13_ACCOUNTING_V2_11_011200_2024-02-07","symbol":"011200","company_name_kr":"HMM","trigger_type":"Stage4B","entry_date":"2024-02-07","entry_price":19080.0,"entry_ohlcv":{"o":19030.0,"h":20200.0,"l":17500.0,"c":19080.0,"v":5677567.0},"mfe_30d_pct":5.87,"mae_30d_pct":-18.45,"mfe_90d_pct":5.87,"mae_90d_pct":-25.31,"mfe_180d_pct":9.01,"mae_180d_pct":-25.31,"peak_180d_date":"2024-07-03","trough_180d_date":"2024-04-19","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv","profile_path":"atlas/symbol_profiles/011/011200.json","corporate_action_overlap_180d":false,"insufficient_forward_window_180d":false,"calibration_usable":true,"evidence_url":"https://en.yna.co.kr/view/AEN20240207001451320","source_proxy_only":false,"evidence_url_pending":false,"case_role":"deal_failure_4b_watch","score_simulation_raw_component_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":8,"bottleneck_pricing":2,"market_mispricing":5,"valuation_rerating":8,"capital_allocation":12,"information_confidence":12},"score_simulation_total_proxy":49,"current_profile_error_type":"stage2_bridge_quality_check","residual_contribution":"accounting_trust_price_path_is_not_operating_green; require cashflow/control-premium separation","shadow_weight_only":true,"production_scoring_changed":false,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|011200|Stage4B|2024-02-07"}
```

## 10. Aggregate Row

```json
{
  "row_type": "aggregate",
  "research_file": "e2r_stock_web_v12_residual_round_R13_loop_201_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md",
  "selected_round": "R13",
  "selected_loop": 201,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
  "fine_archetype_id": "R13_ACCOUNTING_CASHFLOW_CONTROL_PREMIUM_PRICE_VALIDATION_GATE_V2",
  "usable_trigger_count": 11,
  "unique_symbol_count": 11,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "corporate_action_contaminated_180d_count": 0,
  "insufficient_forward_window_180d_count": 0,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "residual_contribution_label": "price_validation_not_operating_green_accounting_control_policy_gate"
}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not apply this MD alone as a production patch.
Batch-ingest this file with the rest of docs/round using the standard v12 calibration CLI.
If promoted, implement only a scoped R13 accounting-trust / price-validation guardrail:
price path after accounting, reserve, tariff, liquidity, tender, or control-premium events must not become operating Stage3-Yellow/Green without a second bridge such as EPS, FCF, ROE/TBVPS accretion, cashflow, working-capital repair, repeated capital-return execution, or post-event integration economics.
Keep production_scoring_changed=false for this research file.
```

## 12. Next Research State

```text
completed_round = R13
completed_loop = 201
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 representative compression / accounting trust direct-source refresh
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
