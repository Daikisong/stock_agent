# E2R v12 residual calibration — R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT

```text
output_file = e2r_stock_web_v12_residual_round_R11_loop_133_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
selected_round = R11
selected_loop = 133
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C31 policy/subsidy/legislation event cashflow bridge, source/proxy repair, 4C-empty path repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Execution guardrails

이번 MD는 current/live 후보 탐색, stock_agent 코드 확인, stock_agent 패치, production scoring 변경이 아니다.
유일한 목적은 `Songdaiki/stock-web`의 실제 1D OHLC row로 C31 정책/보조금/입법 이벤트의 잔여 오류를 확인하고, 나중에 batch coding agent가 읽을 수 있는 standalone calibration row를 남기는 것이다.

C31은 정책이 만드는 큰 바람을 다룬다. 그러나 E2R이 점수로 인정해야 하는 것은 바람 자체가 아니라, 그 바람이 특정 기업의 매출·마진·현금흐름·주주환원으로 들어가는 배관이다. 그래서 이번 loop는 다음 한 문장으로 압축된다.

> 정책 이벤트는 지도 위에 그어진 노선이고, C31에서 Stage2-Actionable을 열려면 그 노선 위로 실제 현금이 달리는 열차가 확인되어야 한다.

## 2. Coverage / no-repeat rationale

No-Repeat Index는 이미 모든 C01~C32가 80 representative rows를 넘었고, 다음 우선순위가 단순 row 채우기보다 URL/proxy 품질, complete MFE/MAE, entry 기준 보강이라고 보고한다. C31은 422 representative rows, 155 symbols, positive/counter 55/86, 4B/4C 45/0으로 집계되어 있어, 특히 hard 4C path가 비어 있는 구조다.

이번 실행은 직전 세션 산출물 C29/C30 및 이전 C18~C28과 겹치지 않고, 아직 이번 묶음에서 생성하지 않은 C31로 이동했다. 기존 C31 root 파일은 R11 loop 132까지 존재하므로 이번 output은 R11 loop 133으로 둔다.

```text
novelty_check = pass
same_session_recent_archetypes_avoided = C05,C01,C13,C15,C10,C02,C16,R13,C17,C07,C06,C14,C11,C12,C09,C03,C04,C08,C18,C19,C20,C21,C22,C23,C24,C25,C26,C27,C28,C29,C30
hard_duplicate_policy = canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count = 8
reused_case_count = 0
same_archetype_new_symbol_count = 8
same_archetype_new_trigger_family_count = 8
positive_case_count = 3
counterexample_count = 5
stage4b_case_count = 3
stage4c_case_count = 2
source_proxy_only_count = 1
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
```

## 3. Stock-Web basis

```text
manifest = atlas/manifest.json
schema = atlas/schema.json
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
mfe_mae_definition = entry close 대비 forward N tradable rows의 max high / min low
```

Entry rule은 보수적으로 적용했다. 공개 시각이 명확하지 않거나 장마감 후로 볼 여지가 있으면 trigger_date 다음 tradable row의 종가를 entry로 잡았다. 모든 usable trigger는 180D window가 manifest max_date 안에 있고, 30D/90D/180D MFE·MAE 여섯 필드를 모두 채웠다.

## 4. Case table

| Symbol | Company | Trigger | Trigger date | Entry date | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Case class | Evidence family |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 005380 | 현대차 | Stage4B | 2024-08-28 | 2024-08-29 | 258,500 | 3.29 / -14.31 | 3.29 / -23.68 | 3.29 / -31.99 | counterexample_high_mae_policy_valueup_overcredit | corporate_valueup_tsr_buyback_hybrid_margin_plan_but_auto_cycle_drawdown |
| 000270 | 기아 | Stage3-Yellow | 2024-12-04 | 2024-12-05 | 94,000 | 14.79 / -2.13 | 14.79 / -13.51 | 20.43 / -13.51 | positive_policy_cash_return_bridge | corporate_valueup_tsr_minimum_dividend_buyback_cancellation_formula |
| 012330 | 현대모비스 | Stage2-Actionable | 2025-01-24 | 2025-01-31 | 263,500 | 2.09 / -8.73 | 10.25 / -11.95 | 24.1 / -11.95 | positive_policy_execution_but_slow_confirmation | tsr_30_percent_treasury_share_cancellation_profitability_bridge |
| 003620 | KG모빌리티 | Stage4C | 2024-02-21 | 2024-02-22 | 8,010 | 3.37 / -28.96 | 3.37 / -37.58 | 3.37 / -51.62 | protection_positive_4c_policy_subsidy_deterioration | ev_subsidy_reduction_forces_price_cut_and_demand_burden |
| 015760 | 한국전력 | Stage3-Yellow | 2024-10-23 | 2024-10-24 | 23,050 | 6.72 / -8.24 | 6.72 / -15.84 | 78.52 / -15.84 | positive_tariff_policy_cashflow_bridge_but_drawdown_watch | industrial_tariff_hike_financial_trouble_cashflow_bridge |
| 036460 | 한국가스공사 | Stage4B | 2024-07-05 | 2024-07-08 | 47,600 | 7.35 / -23.32 | 13.03 / -23.32 | 13.03 / -37.82 | counterexample_tariff_trueup_insufficient_high_mae | residential_city_gas_tariff_hike_but_receivables_and_cost_recovery_uncertain |
| 112610 | 씨에스윈드 | Stage4B | 2023-05-15 | 2023-05-16 | 78,300 | 14.18 / -3.7 | 14.18 / -30.14 | 14.18 / -43.1 | counterexample_policy_subsidy_direct_pay_but_margin_conversion_failure | ira_advanced_manufacturing_direct_pay_tower_margin_expectation |
| 011210 | 현대위아 | Stage4C | 2024-03-27 | 2024-03-28 | 56,900 | 4.04 / -4.22 | 8.44 / -20.12 | 8.44 / -36.03 | protection_positive_4c_policy_proxy_without_company_cashflow_bridge | group_ev_investment_policy_proxy_without_supplier_order_margin_bridge |

## 5. Machine-readable trigger JSONL

```jsonl
{"symbol":"005380","company":"Hyundai Motor","company_kr":"현대차","trigger_type":"Stage4B","trigger_date":"2024-08-28","entry_date":"2024-08-29","entry_price":258500,"MFE_30D_pct":3.29,"MAE_30D_pct":-14.31,"MFE_90D_pct":3.29,"MAE_90D_pct":-23.68,"MFE_180D_pct":3.29,"MAE_180D_pct":-31.99,"peak_30D_date":"2024-08-29","trough_30D_date":"2024-09-11","peak_90D_date":"2024-08-29","trough_90D_date":"2024-11-14","peak_180D_date":"2024-08-29","trough_180D_date":"2025-04-11","case_class":"counterexample_high_mae_policy_valueup_overcredit","evidence_family":"corporate_valueup_tsr_buyback_hybrid_margin_plan_but_auto_cycle_drawdown","evidence_summary":"Hyundai Motor's CEO Investor Day value-up plan had a clear shareholder-return formula, but the 180D path was almost all downside after entry. C31 should not treat policy/value-up disclosure as Green without continuing execution and cycle confirmation.","source_urls":["https://www.hyundai.news/eu/articles/press-releases/hyundai-2024-ceo-investor-day.html","https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/"],"source_quality":"direct_company_plus_reputable_news","source_proxy_only":false,"current_profile_error_type":"valueup_event_overcredited_without_drawdown_aware_confirmation","raw_component_breakdown":{"EPS_FCF_explosion":14,"earnings_visibility":15,"bottleneck_pricing":5,"market_mispricing":13,"valuation_rerating":16,"capital_allocation":22,"information_confidence":18},"simulated_total_score":76,"suggested_stage_after_rule":"Stage4B","row_type":"trigger","calibration_usable":true,"same_entry_group":"C31_L133_G01_005380_2024-08-28","aggregate_group_role":"representative_candidate","round":"R11","loop":133,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_count_as_new_case":false,"evidence_url_pending":false}
{"symbol":"000270","company":"Kia","company_kr":"기아","trigger_type":"Stage3-Yellow","trigger_date":"2024-12-04","entry_date":"2024-12-05","entry_price":94000,"MFE_30D_pct":14.79,"MAE_30D_pct":-2.13,"MFE_90D_pct":14.79,"MAE_90D_pct":-13.51,"MFE_180D_pct":20.43,"MAE_180D_pct":-13.51,"peak_30D_date":"2025-01-14","trough_30D_date":"2024-12-09","peak_90D_date":"2025-01-14","trough_90D_date":"2025-04-11","peak_180D_date":"2025-07-31","trough_180D_date":"2025-04-11","case_class":"positive_policy_cash_return_bridge","evidence_family":"corporate_valueup_tsr_minimum_dividend_buyback_cancellation_formula","evidence_summary":"Kia's value-up disclosure had a clearer capital-return formula than a generic policy headline: TSR target, minimum DPS, payout/buyback/cancellation path. The return path was positive but still had enough 90D drawdown to justify Yellow rather than immediate Green.","source_urls":["https://www.mk.co.kr/en/business/11184666","https://worldwide.kia.com/en/newsroom/view/?id=161489"],"source_quality":"direct_company_plus_reputable_news","source_proxy_only":false,"current_profile_error_type":"none_positive_but_green_requires_execution_followthrough","raw_component_breakdown":{"EPS_FCF_explosion":16,"earnings_visibility":19,"bottleneck_pricing":5,"market_mispricing":12,"valuation_rerating":17,"capital_allocation":24,"information_confidence":19},"simulated_total_score":84,"suggested_stage_after_rule":"Stage3-Yellow","row_type":"trigger","calibration_usable":true,"same_entry_group":"C31_L133_G02_000270_2024-12-04","aggregate_group_role":"representative_candidate","round":"R11","loop":133,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_count_as_new_case":false,"evidence_url_pending":false}
{"symbol":"012330","company":"Hyundai Mobis","company_kr":"현대모비스","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-24","entry_date":"2025-01-31","entry_price":263500,"MFE_30D_pct":2.09,"MAE_30D_pct":-8.73,"MFE_90D_pct":10.25,"MAE_90D_pct":-11.95,"MFE_180D_pct":24.1,"MAE_180D_pct":-11.95,"peak_30D_date":"2025-02-21","trough_30D_date":"2025-03-12","peak_90D_date":"2025-06-12","trough_90D_date":"2025-04-14","peak_180D_date":"2025-09-09","trough_180D_date":"2025-04-14","case_class":"positive_policy_execution_but_slow_confirmation","evidence_family":"tsr_30_percent_treasury_share_cancellation_profitability_bridge","evidence_summary":"Hyundai Mobis had an explicit TSR/cancellation framework and profitability/parts-quality bridge. The stock needed time before the 180D MFE appeared, so Stage2-Actionable is better than immediate Yellow/Green at entry.","source_urls":["https://www.mobis.com/en/aboutus/press.do?category=press&idx=5990","https://www.asiae.co.kr/en/article/2024021619040084136"],"source_quality":"direct_company_plus_reputable_news","source_proxy_only":false,"current_profile_error_type":"positive_slow_confirmation_high_information_quality","raw_component_breakdown":{"EPS_FCF_explosion":15,"earnings_visibility":17,"bottleneck_pricing":8,"market_mispricing":12,"valuation_rerating":15,"capital_allocation":22,"information_confidence":20},"simulated_total_score":79,"suggested_stage_after_rule":"Stage2-Actionable","row_type":"trigger","calibration_usable":true,"same_entry_group":"C31_L133_G03_012330_2025-01-24","aggregate_group_role":"representative_candidate","round":"R11","loop":133,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_count_as_new_case":false,"evidence_url_pending":false}
{"symbol":"003620","company":"KG Mobility","company_kr":"KG모빌리티","trigger_type":"Stage4C","trigger_date":"2024-02-21","entry_date":"2024-02-22","entry_price":8010,"MFE_30D_pct":3.37,"MAE_30D_pct":-28.96,"MFE_90D_pct":3.37,"MAE_90D_pct":-37.58,"MFE_180D_pct":3.37,"MAE_180D_pct":-51.62,"peak_30D_date":"2024-03-04","trough_30D_date":"2024-04-05","peak_90D_date":"2024-03-04","trough_90D_date":"2024-06-27","peak_180D_date":"2024-03-04","trough_180D_date":"2024-11-15","case_class":"protection_positive_4c_policy_subsidy_deterioration","evidence_family":"ev_subsidy_reduction_forces_price_cut_and_demand_burden","evidence_summary":"EV subsidy deterioration was not merely a macro policy headline: KG Mobility cut Torres EVX price to offset a subsidy drop. This is a company-level cashflow/margin burden and the price path validates hard 4C protection.","source_urls":["https://www.koreatimes.co.kr/business/companies/20240221/kg-mobility-achieves-major-turnaround-after-7-years","https://www.koreatimes.co.kr/southkorea/society/20240331/korean-government-considering-further-reduction-of-ev-subsidies"],"source_quality":"direct_company_statement_via_reputable_news","source_proxy_only":false,"current_profile_error_type":"policy_subsidy_negative_bridge_would_be_missed_by_valueup_bias","raw_component_breakdown":{"EPS_FCF_explosion":4,"earnings_visibility":5,"bottleneck_pricing":4,"market_mispricing":8,"valuation_rerating":5,"capital_allocation":4,"information_confidence":21},"simulated_total_score":38,"suggested_stage_after_rule":"Stage4C","row_type":"trigger","calibration_usable":true,"same_entry_group":"C31_L133_G04_003620_2024-02-21","aggregate_group_role":"representative_candidate","round":"R11","loop":133,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_count_as_new_case":false,"evidence_url_pending":false}
{"symbol":"015760","company":"KEPCO","company_kr":"한국전력","trigger_type":"Stage3-Yellow","trigger_date":"2024-10-23","entry_date":"2024-10-24","entry_price":23050,"MFE_30D_pct":6.72,"MAE_30D_pct":-8.24,"MFE_90D_pct":6.72,"MAE_90D_pct":-15.84,"MFE_180D_pct":78.52,"MAE_180D_pct":-15.84,"peak_30D_date":"2024-11-26","trough_30D_date":"2024-11-13","peak_90D_date":"2024-11-26","trough_90D_date":"2025-01-02","peak_180D_date":"2025-06-26","trough_180D_date":"2025-01-02","case_class":"positive_tariff_policy_cashflow_bridge_but_drawdown_watch","evidence_family":"industrial_tariff_hike_financial_trouble_cashflow_bridge","evidence_summary":"The industrial electricity tariff increase was a policy event with direct cashflow relevance. The path had material early drawdown before a large 180D MFE, so the rule should unlock Yellow only after tariff-to-earnings confirmation, not at generic utility-policy rumor stage.","source_urls":["https://www.koreatimes.co.kr/business/companies/20241023/kepco-hikes-industrial-electricity-rates-keeps-residential-fees-steady","https://www.kepco.co.kr/eng/press-center/press-release/boardView.do"],"source_quality":"official_press_board_plus_reputable_news","source_proxy_only":false,"current_profile_error_type":"positive_policy_cashflow_but_green_too_early_without_drawdown_confirmation","raw_component_breakdown":{"EPS_FCF_explosion":18,"earnings_visibility":17,"bottleneck_pricing":10,"market_mispricing":15,"valuation_rerating":16,"capital_allocation":8,"information_confidence":19},"simulated_total_score":82,"suggested_stage_after_rule":"Stage3-Yellow","row_type":"trigger","calibration_usable":true,"same_entry_group":"C31_L133_G05_015760_2024-10-23","aggregate_group_role":"representative_candidate","round":"R11","loop":133,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_count_as_new_case":false,"evidence_url_pending":false}
{"symbol":"036460","company":"KOGAS","company_kr":"한국가스공사","trigger_type":"Stage4B","trigger_date":"2024-07-05","entry_date":"2024-07-08","entry_price":47600,"MFE_30D_pct":7.35,"MAE_30D_pct":-23.32,"MFE_90D_pct":13.03,"MAE_90D_pct":-23.32,"MFE_180D_pct":13.03,"MAE_180D_pct":-37.82,"peak_30D_date":"2024-08-16","trough_30D_date":"2024-08-05","peak_90D_date":"2024-09-03","trough_90D_date":"2024-08-05","peak_180D_date":"2024-09-03","trough_180D_date":"2025-02-11","case_class":"counterexample_tariff_trueup_insufficient_high_mae","evidence_family":"residential_city_gas_tariff_hike_but_receivables_and_cost_recovery_uncertain","evidence_summary":"The household/general gas tariff increase was directly relevant, but the magnitude and cost recovery did not create a durable rerating path. C31 should treat partial true-up as 4B until receivables/cost-pass-through repair is visible.","source_urls":["https://www.koreatimes.co.kr/southkorea/society/20240705/kogas-to-raise-gas-price-for-households-by-68-from-august","https://www.asiae.co.kr/en/article/2024070514564739817"],"source_quality":"company_statement_via_reputable_news","source_proxy_only":false,"current_profile_error_type":"partial_tariff_policy_overcredited_before_balance_sheet_repair","raw_component_breakdown":{"EPS_FCF_explosion":10,"earnings_visibility":9,"bottleneck_pricing":10,"market_mispricing":16,"valuation_rerating":12,"capital_allocation":6,"information_confidence":18},"simulated_total_score":64,"suggested_stage_after_rule":"Stage4B","row_type":"trigger","calibration_usable":true,"same_entry_group":"C31_L133_G06_036460_2024-07-05","aggregate_group_role":"representative_candidate","round":"R11","loop":133,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_count_as_new_case":false,"evidence_url_pending":false}
{"symbol":"112610","company":"CS Wind","company_kr":"씨에스윈드","trigger_type":"Stage4B","trigger_date":"2023-05-15","entry_date":"2023-05-16","entry_price":78300,"MFE_30D_pct":14.18,"MAE_30D_pct":-3.7,"MFE_90D_pct":14.18,"MAE_90D_pct":-30.14,"MFE_180D_pct":14.18,"MAE_180D_pct":-43.1,"peak_30D_date":"2023-06-21","trough_30D_date":"2023-05-19","peak_90D_date":"2023-06-21","trough_90D_date":"2023-09-22","peak_180D_date":"2023-06-21","trough_180D_date":"2023-11-02","case_class":"counterexample_policy_subsidy_direct_pay_but_margin_conversion_failure","evidence_family":"ira_advanced_manufacturing_direct_pay_tower_margin_expectation","evidence_summary":"CS Wind had a direct IRA/AMPTC-style cash-payment narrative in the earnings materials, but the 90D/180D path rolled over hard. C31 should require subsidy-to-margin conversion and backlog durability, not just direct-pay vocabulary.","source_urls":["https://www.cswind.com/en/board/board.download/?n=455&seq=1&t=common","https://www.cswind.com/en/media_room/news/?board=common&category=news&page=&search=&v=536%3F%3D"],"source_quality":"direct_company_material","source_proxy_only":false,"current_profile_error_type":"subsidy_direct_pay_overcredited_without_margin_durability","raw_component_breakdown":{"EPS_FCF_explosion":13,"earnings_visibility":12,"bottleneck_pricing":9,"market_mispricing":15,"valuation_rerating":14,"capital_allocation":8,"information_confidence":18},"simulated_total_score":70,"suggested_stage_after_rule":"Stage4B","row_type":"trigger","calibration_usable":true,"same_entry_group":"C31_L133_G07_112610_2023-05-15","aggregate_group_role":"representative_candidate","round":"R11","loop":133,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_count_as_new_case":false,"evidence_url_pending":false}
{"symbol":"011210","company":"Hyundai Wia","company_kr":"현대위아","trigger_type":"Stage4C","trigger_date":"2024-03-27","entry_date":"2024-03-28","entry_price":56900,"MFE_30D_pct":4.04,"MAE_30D_pct":-4.22,"MFE_90D_pct":8.44,"MAE_90D_pct":-20.12,"MFE_180D_pct":8.44,"MAE_180D_pct":-36.03,"peak_30D_date":"2024-05-02","trough_30D_date":"2024-04-19","peak_90D_date":"2024-06-18","trough_90D_date":"2024-08-05","peak_180D_date":"2024-06-18","trough_180D_date":"2024-12-06","case_class":"protection_positive_4c_policy_proxy_without_company_cashflow_bridge","evidence_family":"group_ev_investment_policy_proxy_without_supplier_order_margin_bridge","evidence_summary":"Hyundai Motor Group's long-run EV/R&D investment plan is real, but as a supplier proxy it did not provide company-level order/margin conversion for Hyundai Wia. C31 must block policy-pass-through assumptions without named beneficiary economics.","source_urls":["https://www.reuters.com/business/autos-transportation/hyundai-motor-group-invest-51-bln-south-korea-over-three-years-2024-03-27/"],"source_quality":"reputable_news_group_level_proxy","source_proxy_only":true,"current_profile_error_type":"policy_pass_through_proxy_false_positive","raw_component_breakdown":{"EPS_FCF_explosion":6,"earnings_visibility":7,"bottleneck_pricing":7,"market_mispricing":14,"valuation_rerating":10,"capital_allocation":8,"information_confidence":12},"simulated_total_score":50,"suggested_stage_after_rule":"Stage4C","row_type":"trigger","calibration_usable":true,"same_entry_group":"C31_L133_G08_011210_2024-03-27","aggregate_group_role":"representative_candidate","round":"R11","loop":133,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_SUBSIDY_TARIFF_CASHFLOW_BRIDGE_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true,"do_not_count_as_new_case":false,"evidence_url_pending":false}
```

## 6. Score-return alignment notes

### 6.1 Value-up policy is not automatically C31 Green

Hyundai Motor and Kia both had clear shareholder-return language, but their forward price paths diverged. Hyundai Motor's plan had a 4T won buyback/TSR framework, yet the entry was followed by -31.99% 180D MAE and almost no MFE. Kia's policy row had a cleaner 180D MFE/MAE profile, but even there 90D MAE reached -13.51%, so Yellow is safer than immediate Green.

C31 lesson: policy disclosure can open the door, but Green should wait for execution follow-through, per-share economics, or a second confirming row.

### 6.2 Tariff/subsidy events must be company-level cashflow events

KEPCO and KOGAS both had direct tariff events. KEPCO's industrial electricity tariff hike eventually produced a strong 180D MFE, but the early path had -15.84% MAE. KOGAS's 6.8% city-gas tariff increase produced only +13.03% 180D MFE versus -37.82% MAE, showing that partial true-up can remain insufficient if accumulated receivables and cost recovery stay unresolved.

C31 lesson: tariff policy is actionable only when it repairs the company's economics, not when it simply acknowledges the problem.

### 6.3 Subsidy cuts and policy pass-through proxies are valid 4C routes

KG Mobility converts the EV subsidy problem into a clean hard 4C: the policy change forced a model-level price cut and the stock's 180D MAE reached -51.62%. Hyundai Wia is a different 4C: the group-level EV investment policy was real, but as a supplier proxy it lacked named order/margin conversion and fell -36.03% on 180D MAE.

C31 lesson: positive policy proximity and negative policy burden must both be forced through a named-beneficiary cashflow bridge.

### 6.4 Direct-pay/subsidy vocabulary still needs margin durability

CS Wind had direct IRA/advanced-manufacturing cash-payment language, but the 90D/180D drawdowns were severe. Direct pay is stronger than generic policy vocabulary, but not enough if order, margin, and inventory/cost durability are not visible.

## 7. Current calibrated profile stress test

```text
profile_proxy = e2r_2_1_stock_web_calibrated
stress_target = residual C31 errors after global calibration
current_profile_error_count = 6
main_residual_error_families:
  1. valueup_event_overcredit_without_execution_followthrough
  2. partial_tariff_trueup_overcredit
  3. subsidy_deterioration_missed_as_policy_negative
  4. group_policy_proxy_false_positive
  5. direct_subsidy_payment_without_margin_durability
```

The current global calibrated rules already block many price-only blowoffs. The remaining C31 problem is subtler: policy documents can look information-rich, but their economic pipe may terminate at the sector, parent group, or headline level rather than at the listed company's cashflow.

## 8. Canonical rule candidate

```text
new_axis_proposed = C31_POLICY_TO_COMPANY_CASHFLOW_CONVERSION_GATE
```

Proposed C31 gate:

```text
For C31_POLICY_SUBSIDY_LEGISLATION_EVENT, do not unlock Stage2-Actionable from policy/legislation/subsidy language alone.
Require at least two of:
  1. named listed-company beneficiary or named product/model/project directly affected
  2. quantified tariff/subsidy/tax/shareholder-return formula
  3. board-approved execution or legally operative rule/date
  4. revenue, margin, receivable, cost recovery, or per-share capital-return bridge
  5. follow-through evidence within the company, not only the sector or parent group

If a policy event causes subsidy loss, forced price cut, unresolved receivables, or group-level pass-through without symbol-level bridge, route to Stage4B or Stage4C even if the policy theme is broadly popular.
```

## 9. Shadow weight proposal

No production scoring is changed in this run. This is a shadow-only candidate for later batch review.

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
before_weights = EPS/Visibility/Bottleneck/Mispricing/Valuation/Capital/Info = 12/15/8/15/15/10/25
after_shadow = EPS/Visibility/Bottleneck/Mispricing/Valuation/Capital/Info = 11/18/8/12/13/12/26
delta = -1/+3/0/-3/-2/+2/+1
```

Interpretation:

- Raise earnings_visibility because C31 needs proof that policy reaches the company's own economics.
- Raise capital_allocation only when value-up/buyback/dividend execution is quantified and board-approved.
- Reduce market_mispricing and valuation_rerating so policy popularity does not over-score the case.
- Keep information_confidence high because C31 is prone to sector/proxy leakage.

## 10. Residual contribution summary

```text
residual_contribution_label = C31_policy_cashflow_bridge_4c_empty_repair
sector_specific_rule_candidate = L10 policy/event names should be scored only after symbol-level cashflow or capital-return conversion is identified.
canonical_archetype_rule_candidate = C31 policy/subsidy/legislation events require named-beneficiary economics; generic policy proximity is Watch/4B, and negative subsidy/tariff burden can be 4C.
new_axis_proposed = C31_POLICY_TO_COMPANY_CASHFLOW_CONVERSION_GATE
existing_axis_strengthened = stage2_required_bridge; local_4b_watch_guard; hard_4c_confirmation; full_4b_requires_non_price_evidence; drawdown_aware_confirmation; information_confidence_gate
existing_axis_weakened = null
```

## 11. Evidence source list

- https://www.hyundai.news/eu/articles/press-releases/hyundai-2024-ceo-investor-day.html
- https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/
- https://www.mk.co.kr/en/business/11184666
- https://worldwide.kia.com/en/newsroom/view/?id=161489
- https://www.mobis.com/en/aboutus/press.do?category=press&idx=5990
- https://www.asiae.co.kr/en/article/2024021619040084136
- https://www.koreatimes.co.kr/business/companies/20240221/kg-mobility-achieves-major-turnaround-after-7-years
- https://www.koreatimes.co.kr/southkorea/society/20240331/korean-government-considering-further-reduction-of-ev-subsidies
- https://www.koreatimes.co.kr/business/companies/20241023/kepco-hikes-industrial-electricity-rates-keeps-residential-fees-steady
- https://www.kepco.co.kr/eng/press-center/press-release/boardView.do
- https://www.koreatimes.co.kr/southkorea/society/20240705/kogas-to-raise-gas-price-for-households-by-68-from-august
- https://www.asiae.co.kr/en/article/2024070514564739817
- https://www.cswind.com/en/board/board.download/?n=455&seq=1&t=common
- https://www.cswind.com/en/media_room/news/?board=common&category=news&page=&search=&v=536%3F%3D
- https://www.reuters.com/business/autos-transportation/hyundai-motor-group-invest-51-bln-south-korea-over-three-years-2024-03-27/

## 12. Batch ingest self-audit

```text
required_filename_regex = pass
filename_round_matches_metadata = pass
filename_loop_matches_metadata = pass
standard_v12_filename = pass
compact_filename_forbidden = pass
large_sector_id_valid = pass
round_sector_consistency = pass
canonical_archetype_id_valid = pass
trigger_type_canonical_stage_label_only = pass
all_trigger_rows_have_MFE_30D_pct = pass
all_trigger_rows_have_MFE_90D_pct = pass
all_trigger_rows_have_MFE_180D_pct = pass
all_trigger_rows_have_MAE_30D_pct = pass
all_trigger_rows_have_MAE_90D_pct = pass
all_trigger_rows_have_MAE_180D_pct = pass
entry_price_present_all_rows = pass
entry_date_present_all_rows = pass
price_data_source_present_all_rows = pass
source_urls_present_all_rows = pass
evidence_url_pending_count = 0
source_proxy_only_count = {proxy}
calibration_usable_trigger_count = {len(rows)}
representative_trigger_candidate_count = {len(rows)}
production_scoring_changed = false
shadow_weight_only = true
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research run.

Goal:
  Batch-ingest this standalone v12 research MD as one C31 policy/subsidy/legislation quality-repair artifact.

Input file:
  docs/round/e2r_stock_web_v12_residual_round_R11_loop_133_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Expected parser actions:
  1. Parse all row_type=trigger JSONL records.
  2. Validate trigger_type is one of Stage2, Stage2-Actionable, Stage3-Yellow, Stage3-Green, Stage4B, Stage4C.
  3. Validate all six required MFE/MAE fields exist.
  4. Preserve source_proxy_only flags.
  5. Add the proposed shadow axis C31_POLICY_TO_COMPANY_CASHFLOW_CONVERSION_GATE to review queue only; do not apply production scoring directly.
  6. Treat Hyundai Wia as a source_proxy_only 4C guardrail row, not as a positive promotion row.
  7. Use same_entry_group to avoid duplicate aggregate counting if a later archive already contains exact C31 + symbol + trigger_type + entry_date matches.
```

## 14. Completed state

```text
completed_round = R11
completed_loop = 133
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C31 policy/subsidy/legislation event cashflow bridge, source/proxy repair, 4C-empty path repair
next_recommended_archetypes = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP; R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW; R13_CROSS_ARCHETYPE_4B_4C_REDTEAM; C02_POWER_GRID_DATACENTER_CAPEX
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
