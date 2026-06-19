# E2R Stock-Web v12 Residual Research — R13 / Financial Value-up Stage2 False-Positive Holdout

```text
research_session = post_calibrated_sector_archetype_residual_research_v12
selected_round = R13
selected_loop = 202
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 R13 false-positive taxonomy cleanup using recent R6 direct-evidence rows
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id = R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2

source_large_sector_focus = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
source_canonical_focus = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN + C22_INSURANCE_RATE_CYCLE_RESERVE

primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 1. Selection rationale

The MAIN prompt requires one standalone historical calibration MD, no live scan, no stock_agent code patch, and actual Songdaiki/stock-web 1D OHLCV rows. The No-Repeat Index says all C01~C32 archetypes are beyond the 80-row floor, so this run does not chase raw row count. It performs R13 taxonomy cleanup.

This file compresses recent R6 financial/insurance source rows into `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`. The target error is simple: **a low-PBR / value-up / CSM / K-ICS / dividend headline is not automatically a full conversion bridge.** Stage2 can be early, but Actionable and Yellow require a second key.

## 2. Novelty / duplicate avoidance

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
r13_new_independent_case_count = 14
r13_new_independent_trigger_count = 14
unique_symbol_count = 11
unique_source_canonical_count = 2
stage2_count = 4
stage2_actionable_count = 9
stage4b_count = 1
high_MAE_180D_count = 3
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
```

The source-sector rows are not counted as new C21/C22 weight evidence. This file is a cross-archetype holdout: the canonical key is R13, not C21 or C22.

## 3. Stock-Web price atlas validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_schema = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
manifest_max_date = 2026-02-20
price_adjustment_status = raw_unadjusted_marcap
```

All rows below use actual entry OHLCV, entry close, 30/90/180D MFE/MAE, 180D peak date, and 180D trough date. No row is a current/live candidate.

## 4. Trigger-level holdout table

| symbol | company | source canonical | trigger | entry date | entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak/trough | role |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| 105560 | KB Financial Group | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable | 2024-04-25 | 69,300 | 20.35/-1.59 | 33.33/-1.59 | 49.93/-1.59 | 2024-10-25 / 2024-04-25 | positive_direct_capital_return_policy |
| 105560 | KB Financial Group | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable | 2024-10-24 | 93,200 | 11.48/-7.94 | 11.48/-18.03 | 30.90/-25.64 | 2025-07-08 / 2025-04-09 | high_mae_guardrail |
| 055550 | Shinhan Financial Group | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable | 2024-07-26 | 58,000 | 11.38/-11.03 | 11.38/-14.48 | 11.38/-26.72 | 2024-08-26 / 2025-04-09 | ambitious_plan_high_mae_counterexample |
| 086790 | Hana Financial Group | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable | 2024-10-29 | 65,000 | 3.85/-13.23 | 3.85/-13.23 | 49.38/-20.77 | 2025-07-15 / 2025-04-09 | delayed_positive_with_drawdown |
| 316140 | Woori Financial Group | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2 | 2024-07-26 | 16,180 | 4.82/-15.08 | 6.92/-15.08 | 8.16/-15.08 | 2025-02-19 / 2024-08-05 | plan_without_immediate_mechanics_counterexample |
| 138040 | Meritz Financial Group | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable | 2024-11-21 | 103,800 | 2.99/-6.84 | 22.74/-6.84 | 22.74/-6.84 | 2025-03-06 / 2024-12-09 | buyback_return_positive_control |
| 024110 | Industrial Bank of Korea | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2 | 2024-02-08 | 13,410 | 19.39/-3.65 | 19.39/-6.71 | 19.39/-6.71 | 2024-03-15 / 2024-04-15 | dividend_yield_policy_cap |
| 000810 | Samsung Fire & Marine Insurance | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2-Actionable | 2024-02-23 | 308,500 | 14.42/-7.46 | 20.10/-8.10 | 33.39/-8.10 | 2024-07-09 / 2024-03-04 | positive_control_kics_dps_valueup |
| 000810 | Samsung Fire & Marine Insurance | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2-Actionable | 2025-01-31 | 381,500 | 12.58/-5.37 | 16.91/-8.65 | 24.38/-8.65 | 2025-06-18 / 2025-03-13 | positive_control_valueup_execution_mechanics |
| 005830 | DB Insurance | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2 | 2024-11-14 | 105,500 | 7.77/-6.07 | 14.88/-13.93 | 31.75/-13.93 | 2025-07-02 / 2025-04-07 | stage2_policy_framework_cap |
| 005830 | DB Insurance | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2-Actionable | 2025-02-04 | 100,000 | 3.90/-9.40 | 23.60/-9.40 | 44.80/-9.40 | 2025-09-05 / 2025-02-10 | dps_increase_capital_return_bridge |
| 001450 | Hyundai Marine & Fire Insurance | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage4B | 2025-05-14 | 22,150 | 14.45/-3.39 | 39.95/-3.39 | 58.01/-3.39 | 2025-12-01 / 2025-05-15 | one_time_reserve_base_effect_watch_not_4c |
| 088350 | Hanwha Life Insurance | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2 | 2025-02-20 | 2,715 | 0.55/-6.81 | 19.34/-11.79 | 35.91/-11.79 | 2025-11-06 / 2025-04-07 | csm_profit_quality_cap |
| 032830 | Samsung Life Insurance | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2-Actionable | 2024-02-21 | 88,300 | 22.88/-7.47 | 22.88/-11.21 | 22.88/-19.25 | 2024-03-15 / 2024-08-05 | csm_kics_valueup_setup_green_blocked |

## 5. Case interpretation

C21 bank rows show the difference between policy beta and execution. KB and Meritz are positive controls because buyback/cancellation, CET1 excess-capital rules, or execution-linked payout mechanics are visible. Shinhan and Hana still deserve Actionable treatment, but the drawdown path makes them Green-braked rather than Green-ready. Woori and IBK are Stage2 caps because target-like value-up or dividend-yield language lacks immediate per-share execution mechanics.

C22 insurance rows show the same two-key lock in insurance language. CSM/K-ICS can support Stage2, but Stage2-Actionable needs DPS increase, buyback/cancellation mechanics, payout formula, K-ICS excess-capital rule, reserve/loss-ratio stabilization tied to return, or repeated payout execution. Hyundai Marine is deliberately included as a 4B row: a one-time reserve/accounting base effect should not become sticky hard 4C while CSM/K-ICS/profitability offset remains visible.

## 6. Residual contribution

```text
core_error_mode = single financial headline treated as full execution bridge
source_canonicals_tested = C21 + C22
current_profile_false_positive_risk_count = 5
current_profile_too_late_actionable_risk_count = 2
current_profile_too_harsh_4c_risk_count = 1

positive_control_pattern:
- CET1 excess-capital rule + buyback/cancellation
- DPS increase / shareholder-return formula
- CSM + K-ICS + payout mechanics

false_positive_pattern:
- Korea value-up headline only
- low-PBR rerating headline only
- CSM/K-ICS headline without payout mechanics
- target-only TSR/ROE plan without immediate execution
- one-time reserve shock treated as sticky 4C despite offset
```

## 7. R13 rule candidate

```text
rule_candidate = R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V2
rule_type = cross_archetype_stage2_false_positive_review
production_scoring_changed = false
shadow_weight_only = true
do_not_apply_now = true
```

Proposed rule text:

```text
- Stage2 can be early. The error is not early Stage2; it is treating a single value-up/CSM/K-ICS headline as a full execution bridge.
- Stage2-Actionable requires at least one direct second bridge:
  buyback/cancellation, dividend formula, DPS increase, CET1 excess-capital rule,
  K-ICS excess-capital rule, reserve/loss-ratio stabilization tied to capital return,
  TBVPS/EPS accretion, or repeated shareholder-return execution.
- Target-only TSR/ROE, dividend-yield, low-PBR, CSM, or K-ICS language remains Stage2 unless execution mechanics are visible.
- High MAE on a valid direct-bridge row blocks Yellow/Green first; it does not erase Stage2-Actionable.
- One-time reserve/accounting shocks route first to Stage4B/watch if CSM/K-ICS/profitability offset remains visible.
- Hard 4C requires solvency stress, capital-return suspension, reserve-quality break, loss-ratio deterioration with weak offset quality, liquidity/accounting trust break, or confirmed non-price thesis break.
```

## 8. Machine-readable JSONL trigger rows

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"105560","name":"KB Financial Group","trigger_type":"Stage2-Actionable","case_role":"positive_direct_capital_return_policy","evidence_date":"2024-04-25","entry_date":"2024-04-25","entry_price":69300.0,"entry_ohlcv":{"o":68300.0,"h":70600.0,"l":68200.0,"c":69300.0,"v":745906,"m":"KOSPI"},"mfe_30d_pct":20.35,"mae_30d_pct":-1.59,"mfe_90d_pct":33.33,"mae_90d_pct":-1.59,"mfe_180d_pct":49.93,"mae_180d_pct":-1.59,"peak_180d_date":"2024-10-25","trough_180d_date":"2024-04-25","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://www.sec.gov/Archives/edgar/data/1445930/000119312524242219/d901349d6k.htm","evidence_family":"direct shareholder-return policy + CET1 excess-capital rule","residual_interpretation":"Financial value-up headline requires explicit execution bridge before escalation beyond Stage2; high MAE brakes Yellow/Green first.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"105560","name":"KB Financial Group","trigger_type":"Stage2-Actionable","case_role":"high_mae_guardrail","evidence_date":"2024-10-24","entry_date":"2024-10-24","entry_price":93200.0,"entry_ohlcv":{"o":93800.0,"h":94800.0,"l":92800.0,"c":93200.0,"v":1385779,"m":"KOSPI"},"mfe_30d_pct":11.48,"mae_30d_pct":-7.94,"mfe_90d_pct":11.48,"mae_90d_pct":-18.03,"mfe_180d_pct":30.9,"mae_180d_pct":-25.64,"peak_180d_date":"2025-07-08","trough_180d_date":"2025-04-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://www.sec.gov/Archives/edgar/data/1445930/000119312524242219/d901349d6k.htm","evidence_family":"corporate value-up phase rule + buyback/cancellation decision","residual_interpretation":"Financial value-up headline requires explicit execution bridge before escalation beyond Stage2; high MAE brakes Yellow/Green first.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"055550","name":"Shinhan Financial Group","trigger_type":"Stage2-Actionable","case_role":"ambitious_plan_high_mae_counterexample","evidence_date":"2024-07-26","entry_date":"2024-07-26","entry_price":58000.0,"entry_ohlcv":{"o":54200.0,"h":58400.0,"l":54200.0,"c":58000.0,"v":3558607,"m":"KOSPI"},"mfe_30d_pct":11.38,"mae_30d_pct":-11.03,"mfe_90d_pct":11.38,"mae_90d_pct":-14.48,"mfe_180d_pct":11.38,"mae_180d_pct":-26.72,"peak_180d_date":"2024-08-26","trough_180d_date":"2025-04-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://shinhangroup.com/resources/publish/jp/resource/2024_Shinhan_Financial_Group_Value-up_Plan.pdf","evidence_family":"value-up plan: ROE/TSR/share-count reduction targets","residual_interpretation":"Financial value-up headline requires explicit execution bridge before escalation beyond Stage2; high MAE brakes Yellow/Green first.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"086790","name":"Hana Financial Group","trigger_type":"Stage2-Actionable","case_role":"delayed_positive_with_drawdown","evidence_date":"2024-10-29","entry_date":"2024-10-29","entry_price":65000.0,"entry_ohlcv":{"o":65700.0,"h":67500.0,"l":63500.0,"c":65000.0,"v":1674357,"m":"KOSPI"},"mfe_30d_pct":3.85,"mae_30d_pct":-13.23,"mfe_90d_pct":3.85,"mae_90d_pct":-13.23,"mfe_180d_pct":49.38,"mae_180d_pct":-20.77,"peak_180d_date":"2025-07-15","trough_180d_date":"2025-04-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://vpr.hkma.gov.hk/statics/assets/doc/100080/ar_24/ar_24_pt02_eng.pdf","evidence_family":"value-up plan + CET1/ROE/shareholder-return target","residual_interpretation":"Financial value-up headline requires explicit execution bridge before escalation beyond Stage2; high MAE brakes Yellow/Green first.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"316140","name":"Woori Financial Group","trigger_type":"Stage2","case_role":"plan_without_immediate_mechanics_counterexample","evidence_date":"2024-07-26","entry_date":"2024-07-26","entry_price":16180.0,"entry_ohlcv":{"o":14810.0,"h":16230.0,"l":14800.0,"c":16180.0,"v":14562584,"m":"KOSPI"},"mfe_30d_pct":4.82,"mae_30d_pct":-15.08,"mfe_90d_pct":6.92,"mae_90d_pct":-15.08,"mfe_180d_pct":8.16,"mae_180d_pct":-15.08,"peak_180d_date":"2025-02-19","trough_180d_date":"2024-08-05","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://www.kedglobal.com/earnings/newsView/ked202407260004","evidence_family":"value-up target / ROE and TSR objective","residual_interpretation":"Financial value-up headline requires explicit execution bridge before escalation beyond Stage2; high MAE brakes Yellow/Green first.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"138040","name":"Meritz Financial Group","trigger_type":"Stage2-Actionable","case_role":"buyback_return_positive_control","evidence_date":"2024-11-21","entry_date":"2024-11-21","entry_price":103800.0,"entry_ohlcv":{"o":104600.0,"h":106100.0,"l":103800.0,"c":103800.0,"v":240553,"m":"KOSPI"},"mfe_30d_pct":2.99,"mae_30d_pct":-6.84,"mfe_90d_pct":22.74,"mae_90d_pct":-6.84,"mfe_180d_pct":22.74,"mae_180d_pct":-6.84,"peak_180d_date":"2025-03-06","trough_180d_date":"2024-12-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20250219800640","evidence_family":"continued buybacks + net-profit execution","residual_interpretation":"Financial value-up headline requires explicit execution bridge before escalation beyond Stage2; high MAE brakes Yellow/Green first.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"024110","name":"Industrial Bank of Korea","trigger_type":"Stage2","case_role":"dividend_yield_policy_cap","evidence_date":"2024-02-08","entry_date":"2024-02-08","entry_price":13410.0,"entry_ohlcv":{"o":13300.0,"h":13480.0,"l":13240.0,"c":13410.0,"v":2535845,"m":"KOSPI"},"mfe_30d_pct":19.39,"mae_30d_pct":-3.65,"mfe_90d_pct":19.39,"mae_90d_pct":-6.71,"mfe_180d_pct":19.39,"mae_180d_pct":-6.71,"peak_180d_date":"2024-03-15","trough_180d_date":"2024-04-15","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://global.ibk.co.kr/en/investor/ShareholderReturn","evidence_family":"dividend payout and value-up-sensitive bank beta","residual_interpretation":"Financial value-up headline requires explicit execution bridge before escalation beyond Stage2; high MAE brakes Yellow/Green first.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"000810","name":"Samsung Fire & Marine Insurance","trigger_type":"Stage2-Actionable","case_role":"positive_control_kics_dps_valueup","evidence_date":"2024-02-23","entry_date":"2024-02-23","entry_price":308500.0,"entry_ohlcv":{"o":304500.0,"h":321500.0,"l":304500.0,"c":308500.0,"v":123013.0,"m":"KOSPI"},"mfe_30d_pct":14.42,"mae_30d_pct":-7.46,"mfe_90d_pct":20.1,"mae_90d_pct":-8.1,"mfe_180d_pct":33.39,"mae_180d_pct":-8.1,"peak_180d_date":"2024-07-09","trough_180d_date":"2024-03-04","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://www.samsungfire.com/company_eng/P_U01_08_05_480_4.html","evidence_family":"DPS/payout history + K-ICS/CSM quality","residual_interpretation":"CSM/K-ICS/value-up language must be separated from payout/execution mechanics; one-time reserve effects route to 4B/watch before hard 4C.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"000810","name":"Samsung Fire & Marine Insurance","trigger_type":"Stage2-Actionable","case_role":"positive_control_valueup_execution_mechanics","evidence_date":"2025-01-31","entry_date":"2025-01-31","entry_price":381500.0,"entry_ohlcv":{"o":350000.0,"h":383500.0,"l":348000.0,"c":381500.0,"v":272051.0,"m":"KOSPI"},"mfe_30d_pct":12.58,"mae_30d_pct":-5.37,"mfe_90d_pct":16.91,"mae_90d_pct":-8.65,"mfe_180d_pct":24.38,"mae_180d_pct":-8.65,"peak_180d_date":"2025-06-18","trough_180d_date":"2025-03-13","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://biz.chosun.com/en/en-finance/2025/01/31/7WDJYCLUCNBGVATTFLA4MMAW4I/","evidence_family":"shareholder return target + treasury-stock reduction + K-ICS/ROE target","residual_interpretation":"CSM/K-ICS/value-up language must be separated from payout/execution mechanics; one-time reserve effects route to 4B/watch before hard 4C.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB Insurance","trigger_type":"Stage2","case_role":"stage2_policy_framework_cap","evidence_date":"2024-11-14","entry_date":"2024-11-14","entry_price":105500.0,"entry_ohlcv":{"o":106600.0,"h":106700.0,"l":104700.0,"c":105500.0,"v":160040.0,"m":"KOSPI"},"mfe_30d_pct":7.77,"mae_30d_pct":-6.07,"mfe_90d_pct":14.88,"mae_90d_pct":-13.93,"mfe_180d_pct":31.75,"mae_180d_pct":-13.93,"peak_180d_date":"2025-07-02","trough_180d_date":"2025-04-07","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://www.idbins.com/pcweb/bizxpress/coe/ii/value/__etc/%5BDB%20Insurance%5D%20Response%20to%20ISS%202026%20Annual%20General%20Meeting%20%20Proxy%20Advisory%20Report.pdf","evidence_family":"shareholder-return target and K-ICS band, execution pending","residual_interpretation":"CSM/K-ICS/value-up language must be separated from payout/execution mechanics; one-time reserve effects route to 4B/watch before hard 4C.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB Insurance","trigger_type":"Stage2-Actionable","case_role":"dps_increase_capital_return_bridge","evidence_date":"2025-02-04","entry_date":"2025-02-04","entry_price":100000.0,"entry_ohlcv":{"o":99900.0,"h":101500.0,"l":99100.0,"c":100000.0,"v":363305.0,"m":"KOSPI"},"mfe_30d_pct":3.9,"mae_30d_pct":-9.4,"mfe_90d_pct":23.6,"mae_90d_pct":-9.4,"mfe_180d_pct":44.8,"mae_180d_pct":-9.4,"peak_180d_date":"2025-09-05","trough_180d_date":"2025-02-10","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://www.idbins.com/pcweb/bizxpress/coe/ii/value/__etc/Written%20Response%20to%20Align%20Partners%27%202nd%20Shareholder%20Letter.pdf","evidence_family":"DPS increase + K-ICS/distributable profit framing","residual_interpretation":"CSM/K-ICS/value-up language must be separated from payout/execution mechanics; one-time reserve effects route to 4B/watch before hard 4C.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"001450","name":"Hyundai Marine & Fire Insurance","trigger_type":"Stage4B","case_role":"one_time_reserve_base_effect_watch_not_4c","evidence_date":"2025-05-14","entry_date":"2025-05-14","entry_price":22150.0,"entry_ohlcv":{"o":21950.0,"h":22300.0,"l":21750.0,"c":22150.0,"v":242079.0,"m":"KOSPI"},"mfe_30d_pct":14.45,"mae_30d_pct":-3.39,"mfe_90d_pct":39.95,"mae_90d_pct":-3.39,"mfe_180d_pct":58.01,"mae_180d_pct":-3.39,"peak_180d_date":"2025-12-01","trough_180d_date":"2025-05-15","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://en.topdaily.kr/articles/6530","evidence_family":"one-time IBNR/reserve base-effect, CSM/K-ICS offset","residual_interpretation":"CSM/K-ICS/value-up language must be separated from payout/execution mechanics; one-time reserve effects route to 4B/watch before hard 4C.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","name":"Hanwha Life Insurance","trigger_type":"Stage2","case_role":"csm_profit_quality_cap","evidence_date":"2025-02-20","entry_date":"2025-02-20","entry_price":2715.0,"entry_ohlcv":{"o":2770.0,"h":2775.0,"l":2685.0,"c":2715.0,"v":1989293.0,"m":"KOSPI"},"mfe_30d_pct":0.55,"mae_30d_pct":-6.81,"mfe_90d_pct":19.34,"mae_90d_pct":-11.79,"mfe_180d_pct":35.91,"mae_180d_pct":-11.79,"peak_180d_date":"2025-11-06","trough_180d_date":"2025-04-07","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://www.mk.co.kr/en/economy/11245936","evidence_family":"net profit and protection insurance growth, capital-return mechanics incomplete","residual_interpretation":"CSM/K-ICS/value-up language must be separated from payout/execution mechanics; one-time reserve effects route to 4B/watch before hard 4C.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_FINANCIAL_VALUEUP_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V2","source_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","source_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"032830","name":"Samsung Life Insurance","trigger_type":"Stage2-Actionable","case_role":"csm_kics_valueup_setup_green_blocked","evidence_date":"2024-02-21","entry_date":"2024-02-21","entry_price":88300.0,"entry_ohlcv":{"o":82500.0,"h":88500.0,"l":82500.0,"c":88300.0,"v":1483219.0,"m":"KOSPI"},"mfe_30d_pct":22.88,"mae_30d_pct":-7.47,"mfe_90d_pct":22.88,"mae_90d_pct":-11.21,"mfe_180d_pct":22.88,"mae_180d_pct":-19.25,"peak_180d_date":"2024-03-15","trough_180d_date":"2024-08-05","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"source_url":"https://pulse.mk.co.kr/news/english/10947510","evidence_family":"CSM growth + net profit + K-ICS value-up setup","residual_interpretation":"CSM/K-ICS/value-up language must be separated from payout/execution mechanics; one-time reserve effects route to 4B/watch before hard 4C.","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":true}
```

## 9. Batch ingest self-audit

```text
standard_v12_filename = true
filename_round = R13
metadata_round = R13
filename_loop = 202
metadata_loop = 202
round_sector_consistency = pass
large_sector_id_valid = true
canonical_archetype_id_valid = true
r13_scope_valid = true
trigger_type_must_be_canonical_stage_label = pass

all_rows_have_actual_entry_ohlcv = true
all_rows_have_entry_price = true
all_rows_have_30_90_180_mfe_mae = true
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
source_proxy_only_count = 0
evidence_url_pending_count = 0

production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.
Later batch-coding session task:
1. Ingest this MD only through the standard v12 calibration parser.
2. Treat rows as R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW holdout rows, not as new C21/C22 source-sector weight rows.
3. Check duplicate key under R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW + symbol + trigger_type + entry_date.
4. If promoted, apply only a cross-archetype guardrail note: financial value-up / CSM / K-ICS headlines require execution bridge before Actionable/Yellow/Green.
5. Do not loosen Stage3-Green.
```

## 11. Next Research State

```text
completed_round = R13
completed_loop = 202
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 R13 false-positive taxonomy cleanup
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
