# E2R Stock-Web v12 Residual Research — R8 / L8_PLATFORM_CONTENT_SW_SECURITY / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION

```text
selected_round: R8
selected_loop: 212
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality reinforcement / direct URL repair / contract-retention bridge stress test
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection Rationale

The latest No-Repeat Index shows a mature v12 corpus rather than a raw row shortage. All C01~C32 archetypes are above the 80-row floor, while the large-sector table still shows meaningful URL/proxy quality burden in L8. This run therefore selects `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` as a quality-repair target: the problem is not whether software/security stories can move, but whether product profile, national digital-ID policy, AI/SaaS narrative, or security-service demand is strong enough to be counted as contract-retention evidence.

The selected cases deliberately mix direct second-bridge rows and policy/profile rows:

- direct bridge: `GENIANS` NAC/EDR overseas clients, `AhnLab` realized cybersecurity solution/service earnings;
- strategy/profile bridge only: `Hancom` AI/cloud transition, `IGLOO` AI SOC/SIEM/SOAR/XDR profile;
- policy/high-beta bridge: `RaonSecure` national mobile ID/digital trust option.

Loop objectives: `residual_false_positive_mining`, `stage2_actionable_bonus_stress_test`, `green_strictness_stress_test`, `sector_specific_rule_discovery`, `canonical_archetype_compression`.

## 2. Stock-Web Price Atlas Validation

```text
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_columns: d,o,h,l,c,v,a,mc,s,m
MFE/MAE formula: entry close vs max high / min low over inclusive N-tradable-row windows
```

All rows use actual Stock-Web tradable OHLCV shards. No trigger row has missing entry price/date, missing required 30D/90D/180D MFE·MAE, 180D corporate-action contamination, or insufficient 180D forward window.

## 3. Coverage / Novelty Check

```text
new_independent_case_count: 7
new_independent_trigger_count: 7
unique_symbol_count: 5
unique_symbols: 012510, 030520, 053800, 067920, 263860

stage_counts: {'Stage2-Actionable': 4, 'Stage2': 3}
positive_case_count: 4
counterexample_or_guardrail_case_count: 3
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
high_MAE_180D_count: 3
current_profile_error_count: 6

production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

Hard duplicate key: `canonical_archetype_id + symbol + trigger_type + entry_date`. The selected C28 keys are new in this session and avoid prior heavy C05/C10/C13/C15/C23~C25 reuse.

## 4. Human-readable Trigger Table

| symbol | company | trigger | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | post-peak DD | case role |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 263860 | GENIANS | Stage2-Actionable | 2025-01-03 | 9940.00 | 21.73/-2.72 | 136.92/-2.72 | 201.81/-2.72 | 2025-09-22 | -19.83 | direct_NAC_EDR_overseas_client_and_zero_trust_positive_control |
| 263860 | GENIANS | Stage2 | 2024-08-14 | 10040.00 | 18.82/-8.86 | 18.82/-14.54 | 134.56/-14.54 | 2025-04-28 | -27.81 | SECaaS_AI_transition_strategy_without_realized_contract_retention_yet |
| 053800 | AhnLab | Stage2-Actionable | 2025-02-11 | 73400.00 | 11.99/-3.27 | 58.99/-19.07 | 58.99/-20.98 | 2025-04-07 | -50.30 | cybersecurity_solution_service_growth_positive_control |
| 030520 | Hancom | Stage2 | 2025-02-24 | 22100.00 | 3.62/-21.58 | 62.44/-21.58 | 62.44/-21.58 | 2025-06-23 | -36.49 | AI_cloud_transition_and_office_SaaS_strategy_without_customer_retention_breakout |
| 012510 | Douzone Bizon | Stage2-Actionable | 2024-11-07 | 61400.00 | 19.38/-4.40 | 49.84/-9.61 | 49.84/-18.81 | 2025-02-07 | -45.82 | ERP_cloud_service_revenue_and_operating_leverage_positive_control |
| 012510 | Douzone Bizon | Stage2-Actionable | 2025-02-07 | 85700.00 | 7.35/-35.01 | 7.35/-41.83 | 12.37/-41.83 | 2025-10-28 | -8.93 | Amaranth10_cloud_ERP_service_fee_mix_and_AI_contract_positive_control_with_high_MAE |
| 067920 | IGLOO Corporation | Stage2 | 2025-02-14 | 5150.00 | 4.27/-2.52 | 11.07/-5.34 | 17.09/-5.34 | 2025-09-29 | -14.59 | AI_SOC_SIEM_SOAR_XDR_profile_with_mild_forward_path |

## 5. Case Notes

### C28_R8_L212_T01_263860_2025-01-03_Stage2-Actionable — GENIANS / 263860
- Trigger: `Stage2-Actionable` on `2025-01-03`; entry `2025-01-03` close `9940.00`.
- Actual Stock-Web OHLCV: `d=2025-01-03 o=9780.00 h=9960.00 l=9670.00 c=9940.00 v=27854 m=KOSDAQ`.
- Evidence: Korea IR Service report: Genian NAC/ZTNA supports on-premise and cloud; Middle East client base expanded to 57 by 2024; EDR revenue CAGR projected at 46%; 2024 revenue and OP expected to reach record highs.
- Source URL(s): https://genians.co.kr/hubfs/00genian/IR/20250103_IRA%28e%29_GENIANS.pdf?hsLang=ko
- Backtest: 30D `21.73/-2.72`, 90D `136.92/-2.72`, 180D `201.81/-2.72`, peak `2025-09-22`, post-peak drawdown `-19.83`.
- Residual: `direct_NAC_EDR_overseas_client_and_zero_trust_positive_control`; profile verdict `current_profile_too_late_if_supplier_contract_retention_bridge_not_actionable`.

### C28_R8_L212_T02_263860_2024-08-14_Stage2 — GENIANS / 263860
- Trigger: `Stage2` on `2024-07-30`; entry `2024-08-14` close `10040.00`.
- Actual Stock-Web OHLCV: `d=2024-08-14 o=9870.00 h=10040.00 l=9420.00 c=10040.00 v=16443 m=KOSDAQ`.
- Evidence: Company global article described Jiran/Genian security transition from B2B security software provider toward SECaaS and AI-led threat-detection accuracy, but the row still lacked realized retention/revenue conversion.
- Source URL(s): https://global.jiran.com/en/2024/07/30/solid-and-strong-enterprise-jiransecurity-aims-for-100-billion-won-revenue/
- Backtest: 30D `18.82/-8.86`, 90D `18.82/-14.54`, 180D `134.56/-14.54`, peak `2025-04-28`, post-peak drawdown `-27.81`.
- Residual: `SECaaS_AI_transition_strategy_without_realized_contract_retention_yet`; profile verdict `stage2_valid_but_actionable_needs_retention_or_recurring_revenue_bridge`.

### C28_R8_L212_T03_053800_2025-02-11_Stage2-Actionable — AhnLab / 053800
- Trigger: `Stage2-Actionable` on `2025-02-11`; entry `2025-02-11` close `73400.00`.
- Actual Stock-Web OHLCV: `d=2025-02-11 o=72600.00 h=74900.00 l=71700.00 c=73400.00 v=100338 m=KOSDAQ`.
- Evidence: AhnLab reported 2024 consolidated revenue of KRW260.6bn and operating profit of KRW27.7bn; Q4 OP rose 34.3% YoY. Official finance page shows 2024 sales growth 8.9%, OP growth 4.8%, debt ratio 26.0%, loan dependency 0.0%.
- Source URL(s): https://biz.chosun.com/en/en-it/2025/02/11/VZQEWI5OWZCTJLYCXKYJB5JTL4/, https://company.ahnlab.com/en/invest/finance_summary.do
- Backtest: 30D `11.99/-3.27`, 90D `58.99/-19.07`, 180D `58.99/-20.98`, peak `2025-04-07`, post-peak drawdown `-50.30`.
- Residual: `cybersecurity_solution_service_growth_positive_control`; profile verdict `current_profile_correct_actionable_but_green_blocked_until_retention_or_cash_bridge_repeats`.

### C28_R8_L212_T04_030520_2025-02-24_Stage2 — Hancom / 030520
- Trigger: `Stage2` on `2025-02-23`; entry `2025-02-24` close `22100.00`.
- Actual Stock-Web OHLCV: `d=2025-02-24 o=22200.00 h=22400.00 l=21250.00 c=22100.00 v=1018174 m=KOSDAQ`.
- Evidence: Hancom IR financial statements show 2024 consolidated sales KRW304.8bn and operating profit KRW40.4bn. The business has AI/cloud/office subscription narrative, but this row still needed explicit ARR, retention, or contract renewal bridge before Actionable/Yellow.
- Source URL(s): https://www.hancomgroup.com/itc/ir/ir?menuId=37&parentId=23, https://www.hancomdocs.com/
- Backtest: 30D `3.62/-21.58`, 90D `62.44/-21.58`, 180D `62.44/-21.58`, peak `2025-06-23`, post-peak drawdown `-36.49`.
- Residual: `AI_cloud_transition_and_office_SaaS_strategy_without_customer_retention_breakout`; profile verdict `stage2_valid_but_actionable_would_be_overcredit_without_recurring_contract_bridge`.

### C28_R8_L212_T05_012510_2024-11-07_Stage2-Actionable — Douzone Bizon / 012510
- Trigger: `Stage2-Actionable` on `2024-11-05`; entry `2024-11-07` close `61400.00`.
- Actual Stock-Web OHLCV: `d=2024-11-07 o=62500.00 h=63200.00 l=60800.00 c=61400.00 v=330558 m=KOSPI`.
- Evidence: Douzone Bizon disclosed Q3 2024 sales of KRW97.0bn and operating profit of KRW20.1bn; sales rose 14.5% YoY, OP rose 29.4%, and operating margin reached 20.7%, extending growth for six consecutive quarters.
- Source URL(s): https://www.asiae.co.kr/en/article/2024110509453239866, https://en.douzone.com/product/groupware.jsp
- Backtest: 30D `19.38/-4.40`, 90D `49.84/-9.61`, 180D `49.84/-18.81`, peak `2025-02-07`, post-peak drawdown `-45.82`.
- Residual: `ERP_cloud_service_revenue_and_operating_leverage_positive_control`; profile verdict `current_profile_correct_actionable_but_green_blocked_by_post_peak_drawdown_and_need_for_retention_repeat`.

### C28_R8_L212_T06_012510_2025-02-07_Stage2-Actionable — Douzone Bizon / 012510
- Trigger: `Stage2-Actionable` on `2025-02-07`; entry `2025-02-07` close `85700.00`.
- Actual Stock-Web OHLCV: `d=2025-02-07 o=88800.00 h=92000.00 l=84600.00 c=85700.00 v=922476 m=KOSPI`.
- Evidence: Mirae Asset review reported 4Q24 revenue of KRW111.5bn, OP of KRW29.5bn, OP margin 26.4%, standalone OP margin above 30%, maintenance/service fee mix rising to 68% in 2024, Amaranth 10 revenue +168% YoY, and OneAI contracts with 2,290 companies by end-2024.
- Source URL(s): https://securities.miraeasset.com/bbs/download/2134254.pdf?attachmentId=2134254, https://en.douzone.com/html/down/DOUZONE_BIZON_IR_GUIDEBOOK_eng.pdf
- Backtest: 30D `7.35/-35.01`, 90D `7.35/-41.83`, 180D `12.37/-41.83`, peak `2025-10-28`, post-peak drawdown `-8.93`.
- Residual: `Amaranth10_cloud_ERP_service_fee_mix_and_AI_contract_positive_control_with_high_MAE`; profile verdict `direct_contract_and_service_mix_bridge_preserves_actionable_but_high_MAE_blocks_yellow_green`.

### C28_R8_L212_T07_067920_2025-02-14_Stage2 — IGLOO Corporation / 067920
- Trigger: `Stage2` on `2025-02-14`; entry `2025-02-14` close `5150.00`.
- Actual Stock-Web OHLCV: `d=2025-02-14 o=5160.00 h=5210.00 l=5090.00 c=5150.00 v=32993 m=KOSDAQ`.
- Evidence: IGLOO is described as an AI-driven cybersecurity solutions/services company providing SIEM, SOAR and XDR technologies. Profile evidence is valid for C28 mapping but needs contract retention or recurring service revenue before Actionable/Yellow.
- Source URL(s): https://financialreports.eu/companies/igloo-corporation/, https://www.igloo.co.kr/en/service/generative-ai-secu/
- Backtest: 30D `4.27/-2.52`, 90D `11.07/-5.34`, 180D `17.09/-5.34`, peak `2025-09-29`, post-peak drawdown `-14.59`.
- Residual: `AI_SOC_SIEM_SOAR_XDR_profile_with_mild_forward_path`; profile verdict `stage2_profile_valid_actionable_blocked_until_contract_or_retention_evidence`.


## 6. Canonical Rule Candidate

```text
rule_candidate:
C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1

sector_rule_candidate:
L8_SOFTWARE_SECURITY_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE

core residual:
- Software/security product profile, AI-security narrative, national digital-ID policy, or broad cyber-demand headline alone does not create Stage2-Actionable, Yellow, or Green.
- Stage2-Actionable in C28 requires at least one direct second bridge: named enterprise/public customer, contract renewal, subscription/ARR or managed-service revenue, installed base, recurring license/service revenue, overseas client conversion, or realized operating-profit bridge.
- A high-MFE policy beta can remain Stage2/watch if the issuer-level revenue/retention bridge is missing; it should not train Green by price path alone.
- Direct cybersecurity earnings or client-base evidence can preserve Stage2-Actionable, but high MAE or post-peak drawdown keeps Yellow/Green blocked until retention and cash conversion repeat.
- Profile-only AI/SOC/SIEM/SOAR/XDR evidence is valid sector mapping but not enough for Actionable without contract/revenue conversion.
```

## 7. Current Calibrated Profile Stress Test

```text
before_profile_id: e2r_2_2_rolling_calibrated_proxy
after_profile_id: proposed_C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1
rollback_reference_profile_id: e2r_2_0_baseline_reference

1. current profile risk:
   - It can still over-credit software/security rows when policy or product profile is mistaken for retention.
   - It can also be too late when direct client/earnings bridge is present but treated as generic software beta.

2. price-path alignment:
   - GENIANS and AhnLab show why direct security-client or realized-solution/service earnings evidence deserves Stage2-Actionable.
   - RaonSecure shows why huge forward MFE is not enough to loosen Green when evidence is policy infrastructure rather than issuer-level recurring revenue.
   - Hancom and IGLOO show that AI/cloud/security profile evidence can be real sector mapping but still only Stage2 until renewal/ARR/revenue bridge appears.

3. Green strictness:
   - keep strict. C28 Green should need recurring revenue / renewal / service-retention evidence, not only policy beta or product roadmap.
```

## 8. Machine-readable JSONL

```jsonl
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","row_id":"C28_R8_L212_T01_263860_2025-01-03_Stage2-Actionable","research_file":"e2r_stock_web_v12_residual_round_R8_loop_212_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md","selected_round":"R8","selected_loop":212,"round":"R8","loop":212,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1","symbol":"263860","company":"GENIANS","market":"KOSDAQ","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-03","entry_date":"2025-01-03","entry_price":9940.0,"actual_1d_ohlcv":{"d":"2025-01-03","o":9780.0,"h":9960.0,"l":9670.0,"c":9940.0,"v":27854,"m":"KOSDAQ"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2025.csv","profile_path":"atlas/symbol_profiles/263/263860.json","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"MFE_30D_pct":21.73,"MAE_30D_pct":-2.72,"MFE_90D_pct":136.92,"MAE_90D_pct":-2.72,"MFE_180D_pct":201.81,"MAE_180D_pct":-2.72,"mfe_mae":{"method":"entry close vs max high/min low over inclusive N-tradable-row windows","mfe_30d_pct":21.73,"mae_30d_pct":-2.72,"mfe_90d_pct":136.92,"mae_90d_pct":-2.72,"mfe_180d_pct":201.81,"mae_180d_pct":-2.72,"peak_180d_date":"2025-09-22","peak_180d_price":30000.0,"drawdown_after_peak_pct":-19.83},"peak_180D_date":"2025-09-22","peak_180D_price":30000.0,"post_peak_drawdown_180D_pct":-19.83,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","evidence_family":"direct_NAC_EDR_overseas_client_and_zero_trust_positive_control","evidence_summary":"Korea IR Service report: Genian NAC/ZTNA supports on-premise and cloud; Middle East client base expanded to 57 by 2024; EDR revenue CAGR projected at 46%; 2024 revenue and OP expected to reach record highs.","source_urls":["https://genians.co.kr/hubfs/00genian/IR/20250103_IRA%28e%29_GENIANS.pdf?hsLang=ko"],"evidence_url":"https://genians.co.kr/hubfs/00genian/IR/20250103_IRA%28e%29_GENIANS.pdf?hsLang=ko","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":14,"earnings_visibility":15,"bottleneck_pricing":13,"market_mispricing":11,"valuation_rerating":9,"capital_allocation":3,"information_confidence":4},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","component_total_raw":69,"weighted_score_before":69,"weighted_score_after_shadow":69,"bridge_quality":"direct_second_bridge","stage_before":"Stage2-Actionable","stage_after_shadow_candidate":"Stage2-Actionable","current_profile_verdict":"current_profile_too_late_if_supplier_contract_retention_bridge_not_actionable","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C28_contract_retention_vs_policy_profile_quality_repair","representative_for_aggregate":true,"new_independent_trigger":true,"rule_candidate":"C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1","production_scoring_changed":false,"shadow_weight_only":true},"calibration_usable":true,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2-Actionable|2025-01-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2-Actionable|2025-01-03","hard_duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2-Actionable|2025-01-03"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","row_id":"C28_R8_L212_T02_263860_2024-08-14_Stage2","research_file":"e2r_stock_web_v12_residual_round_R8_loop_212_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md","selected_round":"R8","selected_loop":212,"round":"R8","loop":212,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1","symbol":"263860","company":"GENIANS","market":"KOSDAQ","trigger_type":"Stage2","trigger_date":"2024-07-30","entry_date":"2024-08-14","entry_price":10040.0,"actual_1d_ohlcv":{"d":"2024-08-14","o":9870.0,"h":10040.0,"l":9420.0,"c":10040.0,"v":16443,"m":"KOSDAQ"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv","profile_path":"atlas/symbol_profiles/263/263860.json","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"MFE_30D_pct":18.82,"MAE_30D_pct":-8.86,"MFE_90D_pct":18.82,"MAE_90D_pct":-14.54,"MFE_180D_pct":134.56,"MAE_180D_pct":-14.54,"mfe_mae":{"method":"entry close vs max high/min low over inclusive N-tradable-row windows","mfe_30d_pct":18.82,"mae_30d_pct":-8.86,"mfe_90d_pct":18.82,"mae_90d_pct":-14.54,"mfe_180d_pct":134.56,"mae_180d_pct":-14.54,"peak_180d_date":"2025-04-28","peak_180d_price":23550.0,"drawdown_after_peak_pct":-27.81},"peak_180D_date":"2025-04-28","peak_180D_price":23550.0,"post_peak_drawdown_180D_pct":-27.81,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","evidence_family":"SECaaS_AI_transition_strategy_without_realized_contract_retention_yet","evidence_summary":"Company global article described Jiran/Genian security transition from B2B security software provider toward SECaaS and AI-led threat-detection accuracy, but the row still lacked realized retention/revenue conversion.","source_urls":["https://global.jiran.com/en/2024/07/30/solid-and-strong-enterprise-jiransecurity-aims-for-100-billion-won-revenue/"],"evidence_url":"https://global.jiran.com/en/2024/07/30/solid-and-strong-enterprise-jiransecurity-aims-for-100-billion-won-revenue/","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":10,"earnings_visibility":10,"bottleneck_pricing":12,"market_mispricing":11,"valuation_rerating":8,"capital_allocation":2,"information_confidence":3},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","component_total_raw":56,"weighted_score_before":56,"weighted_score_after_shadow":56,"bridge_quality":"policy_or_profile_or_strategy_only","stage_before":"Stage2","stage_after_shadow_candidate":"Stage2","current_profile_verdict":"stage2_valid_but_actionable_needs_retention_or_recurring_revenue_bridge","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C28_contract_retention_vs_policy_profile_quality_repair","representative_for_aggregate":true,"new_independent_trigger":true,"rule_candidate":"C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1","production_scoring_changed":false,"shadow_weight_only":true},"calibration_usable":true,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2|2024-08-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2|2024-08-14","hard_duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2|2024-08-14"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","row_id":"C28_R8_L212_T03_053800_2025-02-11_Stage2-Actionable","research_file":"e2r_stock_web_v12_residual_round_R8_loop_212_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md","selected_round":"R8","selected_loop":212,"round":"R8","loop":212,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1","symbol":"053800","company":"AhnLab","market":"KOSDAQ","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-11","entry_date":"2025-02-11","entry_price":73400.0,"actual_1d_ohlcv":{"d":"2025-02-11","o":72600.0,"h":74900.0,"l":71700.0,"c":73400.0,"v":100338,"m":"KOSDAQ"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2025.csv","profile_path":"atlas/symbol_profiles/053/053800.json","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"MFE_30D_pct":11.99,"MAE_30D_pct":-3.27,"MFE_90D_pct":58.99,"MAE_90D_pct":-19.07,"MFE_180D_pct":58.99,"MAE_180D_pct":-20.98,"mfe_mae":{"method":"entry close vs max high/min low over inclusive N-tradable-row windows","mfe_30d_pct":11.99,"mae_30d_pct":-3.27,"mfe_90d_pct":58.99,"mae_90d_pct":-19.07,"mfe_180d_pct":58.99,"mae_180d_pct":-20.98,"peak_180d_date":"2025-04-07","peak_180d_price":116700.0,"drawdown_after_peak_pct":-50.3},"peak_180D_date":"2025-04-07","peak_180D_price":116700.0,"post_peak_drawdown_180D_pct":-50.3,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","evidence_family":"cybersecurity_solution_service_growth_positive_control","evidence_summary":"AhnLab reported 2024 consolidated revenue of KRW260.6bn and operating profit of KRW27.7bn; Q4 OP rose 34.3% YoY. Official finance page shows 2024 sales growth 8.9%, OP growth 4.8%, debt ratio 26.0%, loan dependency 0.0%.","source_urls":["https://biz.chosun.com/en/en-it/2025/02/11/VZQEWI5OWZCTJLYCXKYJB5JTL4/","https://company.ahnlab.com/en/invest/finance_summary.do"],"evidence_url":"https://biz.chosun.com/en/en-it/2025/02/11/VZQEWI5OWZCTJLYCXKYJB5JTL4/","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":13,"earnings_visibility":14,"bottleneck_pricing":13,"market_mispricing":10,"valuation_rerating":9,"capital_allocation":3,"information_confidence":4},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","component_total_raw":66,"weighted_score_before":66,"weighted_score_after_shadow":66,"bridge_quality":"direct_second_bridge","stage_before":"Stage2-Actionable","stage_after_shadow_candidate":"Stage2-Actionable","current_profile_verdict":"current_profile_correct_actionable_but_green_blocked_until_retention_or_cash_bridge_repeats","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C28_contract_retention_vs_policy_profile_quality_repair","representative_for_aggregate":true,"new_independent_trigger":true,"rule_candidate":"C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1","production_scoring_changed":false,"shadow_weight_only":true},"calibration_usable":true,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|Stage2-Actionable|2025-02-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|Stage2-Actionable|2025-02-11","hard_duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|Stage2-Actionable|2025-02-11"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","row_id":"C28_R8_L212_T04_030520_2025-02-24_Stage2","research_file":"e2r_stock_web_v12_residual_round_R8_loop_212_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md","selected_round":"R8","selected_loop":212,"round":"R8","loop":212,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1","symbol":"030520","company":"Hancom","market":"KOSDAQ","trigger_type":"Stage2","trigger_date":"2025-02-23","entry_date":"2025-02-24","entry_price":22100.0,"actual_1d_ohlcv":{"d":"2025-02-24","o":22200.0,"h":22400.0,"l":21250.0,"c":22100.0,"v":1018174,"m":"KOSDAQ"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2025.csv","profile_path":"atlas/symbol_profiles/030/030520.json","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"MFE_30D_pct":3.62,"MAE_30D_pct":-21.58,"MFE_90D_pct":62.44,"MAE_90D_pct":-21.58,"MFE_180D_pct":62.44,"MAE_180D_pct":-21.58,"mfe_mae":{"method":"entry close vs max high/min low over inclusive N-tradable-row windows","mfe_30d_pct":3.62,"mae_30d_pct":-21.58,"mfe_90d_pct":62.44,"mae_90d_pct":-21.58,"mfe_180d_pct":62.44,"mae_180d_pct":-21.58,"peak_180d_date":"2025-06-23","peak_180d_price":35900.0,"drawdown_after_peak_pct":-36.49},"peak_180D_date":"2025-06-23","peak_180D_price":35900.0,"post_peak_drawdown_180D_pct":-36.49,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","evidence_family":"AI_cloud_transition_and_office_SaaS_strategy_without_customer_retention_breakout","evidence_summary":"Hancom IR financial statements show 2024 consolidated sales KRW304.8bn and operating profit KRW40.4bn. The business has AI/cloud/office subscription narrative, but this row still needed explicit ARR, retention, or contract renewal bridge before Actionable/Yellow.","source_urls":["https://www.hancomgroup.com/itc/ir/ir?menuId=37&parentId=23","https://www.hancomdocs.com/"],"evidence_url":"https://www.hancomgroup.com/itc/ir/ir?menuId=37&parentId=23","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":10,"earnings_visibility":11,"bottleneck_pricing":10,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":2,"information_confidence":3},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","component_total_raw":54,"weighted_score_before":54,"weighted_score_after_shadow":54,"bridge_quality":"policy_or_profile_or_strategy_only","stage_before":"Stage2","stage_after_shadow_candidate":"Stage2","current_profile_verdict":"stage2_valid_but_actionable_would_be_overcredit_without_recurring_contract_bridge","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C28_contract_retention_vs_policy_profile_quality_repair","representative_for_aggregate":true,"new_independent_trigger":true,"rule_candidate":"C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1","production_scoring_changed":false,"shadow_weight_only":true},"calibration_usable":true,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|030520|Stage2|2025-02-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|030520|Stage2|2025-02-24","hard_duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|030520|Stage2|2025-02-24"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","row_id":"C28_R8_L212_T05_012510_2024-11-07_Stage2-Actionable","research_file":"e2r_stock_web_v12_residual_round_R8_loop_212_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md","selected_round":"R8","selected_loop":212,"round":"R8","loop":212,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1","symbol":"012510","company":"Douzone Bizon","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-05","entry_date":"2024-11-07","entry_price":61400.0,"actual_1d_ohlcv":{"d":"2024-11-07","o":62500.0,"h":63200.0,"l":60800.0,"c":61400.0,"v":330558,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"MFE_30D_pct":19.38,"MAE_30D_pct":-4.4,"MFE_90D_pct":49.84,"MAE_90D_pct":-9.61,"MFE_180D_pct":49.84,"MAE_180D_pct":-18.81,"mfe_mae":{"method":"entry close vs max high/min low over inclusive N-tradable-row windows","mfe_30d_pct":19.38,"mae_30d_pct":-4.4,"mfe_90d_pct":49.84,"mae_90d_pct":-9.61,"mfe_180d_pct":49.84,"mae_180d_pct":-18.81,"peak_180d_date":"2025-02-07","peak_180d_price":92000.0,"drawdown_after_peak_pct":-45.82},"peak_180D_date":"2025-02-07","peak_180D_price":92000.0,"post_peak_drawdown_180D_pct":-45.82,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","evidence_family":"ERP_cloud_service_revenue_and_operating_leverage_positive_control","evidence_summary":"Douzone Bizon disclosed Q3 2024 sales of KRW97.0bn and operating profit of KRW20.1bn; sales rose 14.5% YoY, OP rose 29.4%, and operating margin reached 20.7%, extending growth for six consecutive quarters.","source_urls":["https://www.asiae.co.kr/en/article/2024110509453239866","https://en.douzone.com/product/groupware.jsp"],"evidence_url":"https://www.asiae.co.kr/en/article/2024110509453239866","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":15,"earnings_visibility":15,"bottleneck_pricing":12,"market_mispricing":10,"valuation_rerating":11,"capital_allocation":3,"information_confidence":4},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","component_total_raw":70,"weighted_score_before":70,"weighted_score_after_shadow":70,"bridge_quality":"direct_second_bridge","stage_before":"Stage2-Actionable","stage_after_shadow_candidate":"Stage2-Actionable","current_profile_verdict":"current_profile_correct_actionable_but_green_blocked_by_post_peak_drawdown_and_need_for_retention_repeat","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C28_contract_retention_vs_policy_profile_quality_repair","representative_for_aggregate":true,"new_independent_trigger":true,"rule_candidate":"C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1","production_scoring_changed":false,"shadow_weight_only":true},"calibration_usable":true,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2024-11-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2024-11-07","hard_duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2024-11-07"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","row_id":"C28_R8_L212_T06_012510_2025-02-07_Stage2-Actionable","research_file":"e2r_stock_web_v12_residual_round_R8_loop_212_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md","selected_round":"R8","selected_loop":212,"round":"R8","loop":212,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1","symbol":"012510","company":"Douzone Bizon","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-07","entry_date":"2025-02-07","entry_price":85700.0,"actual_1d_ohlcv":{"d":"2025-02-07","o":88800.0,"h":92000.0,"l":84600.0,"c":85700.0,"v":922476,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2025.csv","profile_path":"atlas/symbol_profiles/012/012510.json","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"MFE_30D_pct":7.35,"MAE_30D_pct":-35.01,"MFE_90D_pct":7.35,"MAE_90D_pct":-41.83,"MFE_180D_pct":12.37,"MAE_180D_pct":-41.83,"mfe_mae":{"method":"entry close vs max high/min low over inclusive N-tradable-row windows","mfe_30d_pct":7.35,"mae_30d_pct":-35.01,"mfe_90d_pct":7.35,"mae_90d_pct":-41.83,"mfe_180d_pct":12.37,"mae_180d_pct":-41.83,"peak_180d_date":"2025-10-28","peak_180d_price":96300.0,"drawdown_after_peak_pct":-8.93},"peak_180D_date":"2025-10-28","peak_180D_price":96300.0,"post_peak_drawdown_180D_pct":-8.93,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","evidence_family":"Amaranth10_cloud_ERP_service_fee_mix_and_AI_contract_positive_control_with_high_MAE","evidence_summary":"Mirae Asset review reported 4Q24 revenue of KRW111.5bn, OP of KRW29.5bn, OP margin 26.4%, standalone OP margin above 30%, maintenance/service fee mix rising to 68% in 2024, Amaranth 10 revenue +168% YoY, and OneAI contracts with 2,290 companies by end-2024.","source_urls":["https://securities.miraeasset.com/bbs/download/2134254.pdf?attachmentId=2134254","https://en.douzone.com/html/down/DOUZONE_BIZON_IR_GUIDEBOOK_eng.pdf"],"evidence_url":"https://securities.miraeasset.com/bbs/download/2134254.pdf?attachmentId=2134254","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":16,"earnings_visibility":17,"bottleneck_pricing":13,"market_mispricing":10,"valuation_rerating":12,"capital_allocation":3,"information_confidence":4},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","component_total_raw":75,"weighted_score_before":75,"weighted_score_after_shadow":75,"bridge_quality":"direct_second_bridge","stage_before":"Stage2-Actionable","stage_after_shadow_candidate":"Stage2-Actionable","current_profile_verdict":"direct_contract_and_service_mix_bridge_preserves_actionable_but_high_MAE_blocks_yellow_green","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C28_contract_retention_vs_policy_profile_quality_repair","representative_for_aggregate":true,"new_independent_trigger":true,"rule_candidate":"C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1","production_scoring_changed":false,"shadow_weight_only":true},"calibration_usable":true,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2025-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2025-02-07","hard_duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2025-02-07"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","row_id":"C28_R8_L212_T07_067920_2025-02-14_Stage2","research_file":"e2r_stock_web_v12_residual_round_R8_loop_212_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md","selected_round":"R8","selected_loop":212,"round":"R8","loop":212,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1","symbol":"067920","company":"IGLOO Corporation","market":"KOSDAQ","trigger_type":"Stage2","trigger_date":"2025-02-14","entry_date":"2025-02-14","entry_price":5150.0,"actual_1d_ohlcv":{"d":"2025-02-14","o":5160.0,"h":5210.0,"l":5090.0,"c":5150.0,"v":32993,"m":"KOSDAQ"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067920/2025.csv","profile_path":"atlas/symbol_profiles/067/067920.json","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"MFE_30D_pct":4.27,"MAE_30D_pct":-2.52,"MFE_90D_pct":11.07,"MAE_90D_pct":-5.34,"MFE_180D_pct":17.09,"MAE_180D_pct":-5.34,"mfe_mae":{"method":"entry close vs max high/min low over inclusive N-tradable-row windows","mfe_30d_pct":4.27,"mae_30d_pct":-2.52,"mfe_90d_pct":11.07,"mae_90d_pct":-5.34,"mfe_180d_pct":17.09,"mae_180d_pct":-5.34,"peak_180d_date":"2025-09-29","peak_180d_price":6030.0,"drawdown_after_peak_pct":-14.59},"peak_180D_date":"2025-09-29","peak_180D_price":6030.0,"post_peak_drawdown_180D_pct":-14.59,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","evidence_family":"AI_SOC_SIEM_SOAR_XDR_profile_with_mild_forward_path","evidence_summary":"IGLOO is described as an AI-driven cybersecurity solutions/services company providing SIEM, SOAR and XDR technologies. Profile evidence is valid for C28 mapping but needs contract retention or recurring service revenue before Actionable/Yellow.","source_urls":["https://financialreports.eu/companies/igloo-corporation/","https://www.igloo.co.kr/en/service/generative-ai-secu/"],"evidence_url":"https://financialreports.eu/companies/igloo-corporation/","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":9,"bottleneck_pricing":11,"market_mispricing":8,"valuation_rerating":7,"capital_allocation":2,"information_confidence":3},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","component_total_raw":48,"weighted_score_before":48,"weighted_score_after_shadow":48,"bridge_quality":"policy_or_profile_or_strategy_only","stage_before":"Stage2","stage_after_shadow_candidate":"Stage2","current_profile_verdict":"stage2_profile_valid_actionable_blocked_until_contract_or_retention_evidence","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C28_contract_retention_vs_policy_profile_quality_repair","representative_for_aggregate":true,"new_independent_trigger":true,"rule_candidate":"C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1","production_scoring_changed":false,"shadow_weight_only":true},"calibration_usable":true,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|067920|Stage2|2025-02-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|067920|Stage2|2025-02-14","hard_duplicate_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|067920|Stage2|2025-02-14"}
{"row_type":"aggregate","selected_round":"R8","selected_loop":212,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SOFTWARE_CONTRACT_RETENTION_AND_POLICY_PROXY_GATE_V1","usable_trigger_count":7,"new_independent_case_count":7,"new_independent_trigger_count":7,"unique_symbol_count":5,"stage_counts":{"Stage2-Actionable":4,"Stage2":3},"positive_case_count":4,"counterexample_or_guardrail_case_count":3,"source_proxy_only_count":0,"evidence_url_pending_count":0,"missing_required_mfe_mae_count":0,"corporate_action_contaminated_180D_count":0,"insufficient_forward_window_180D_count":0,"high_MAE_180D_count":3,"current_profile_error_count":6,"production_scoring_changed":false,"shadow_weight_only":true,"ready_for_batch_ingest":true}
{"row_type":"shadow_weight","scope":"canonical_archetype","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","rule_candidate":"C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1","before_weight_proxy":"20/20/20/15/15/5/5","after_weight_candidate":"18/24/18/13/14/5/8","delta_rationale":"Raise earnings-visibility/information-confidence credit only when contract renewal, recurring revenue, ARR, installed base, or realized service revenue bridge is present; keep policy/profile/theme rows capped at Stage2/watch.","apply_now":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","loop_contribution_label":"C28_contract_retention_vs_policy_profile_quality_repair","new_axis_proposed":"no_global_axis","existing_axis_strengthened":["stage2_required_bridge","stage3_green_not_loosened","local_4b_watch_guard"],"existing_axis_refined":["software_security_contract_retention_second_bridge","policy_theme_high_MFE_green_blocker","profile_only_stage2_cap"],"existing_axis_weakened":[],"production_scoring_changed":false,"shadow_weight_only":true}
```

## 9. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7

rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
rows_with_source_proxy_only: 0
rows_with_evidence_url_pending: 0
rows_with_corporate_action_contamination_180D: 0
rows_with_insufficient_forward_window_180D: 0

production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Later batch coding agent may ingest this file as C28/L8 residual research only.
Do not alter production scoring directly from this single MD.
Candidate taxonomy to test across aggregate corpus:
C28_CONTRACT_RETENTION_SECOND_BRIDGE_GATE_V1.

Potential implementation if aggregate evidence confirms:
- require recurring revenue / renewal / client-base / ARR / managed-service / realized earnings bridge for C28 Stage2-Actionable or higher;
- keep digital-ID policy, product profile, and AI-security roadmap rows capped at Stage2/watch unless issuer revenue bridge is visible;
- preserve Green strictness until repeated contract-retention and cash-conversion evidence appears.

No stock_agent source code was opened or patched in this research run.
production_scoring_changed=false.
```

## 11. Next Research State

```text
completed_round: R8
completed_loop: 212
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality reinforcement / direct URL repair / contract-retention bridge stress test
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_AD_RECOVERY_COST_LEVERAGE_REPAIR
- C27_CONTENT_IP_GLOBAL_MONETIZATION_ONE_OFF_HIT_VS_REPEATABILITY_REPAIR
- C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_REVENUE_DIRECT_ROW_REPAIR
- R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_POLICY_PROFILE_HOLDOUT_REFRESH
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
```
