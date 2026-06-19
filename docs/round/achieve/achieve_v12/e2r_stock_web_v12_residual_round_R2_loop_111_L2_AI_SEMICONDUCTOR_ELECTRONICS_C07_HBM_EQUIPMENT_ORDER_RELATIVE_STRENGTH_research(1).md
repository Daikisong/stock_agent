---
title: "E2R Stock-Web V12 Residual Research — R2 Loop 111 — C07 HBM Equipment Order Relative Strength"
created_at_kst: "2026-06-13"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R2"
selected_loop: 111
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
large_sector_id: "L2_AI_SEMICONDUCTOR_ELECTRONICS"
canonical_archetype_id: "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
fine_archetype_id: "C07_HBM_DIRECT_AND_PROXY_EQUIPMENT_ORDER_REVENUE_BRIDGE_VS_RELATIVE_STRENGTH_FADE"
deep_sub_archetype_id: "C07_DEEP_TCBONDER_TESTER_HANDLER_LASER_ANNEALING_INSPECTION_PROCESS_EQUIPMENT_ORDER_BRIDGE_VS_THEME_LABEL"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 111
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = C07_HBM_DIRECT_AND_PROXY_EQUIPMENT_ORDER_REVENUE_BRIDGE_VS_RELATIVE_STRENGTH_FADE
deep_sub_archetype_id = C07_DEEP_TCBONDER_TESTER_HANDLER_LASER_ANNEALING_INSPECTION_PROCESS_EQUIPMENT_ORDER_BRIDGE_VS_THEME_LABEL
```

This is a standalone historical calibration artifact. It is not a live scan, not a watchlist, not investment advice, not a code patch, and not a production scoring change. The scheduler is coverage-index-first: the canonical archetype is selected first, and the round/large-sector metadata follows from that canonical.

## 1. Coverage-index selection

The published No-Repeat Index reports `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` as Priority 0 with 18 representative rows. In this local session, C07 loop107/108/109/110 were already produced. Loop111 is selected because C07 had not yet crossed the practical 50-row band after local-session adjustment.

```text
published_index_rows = 18
local_session_prior_c07_loop107 = 7
local_session_prior_c07_loop108 = 6
local_session_prior_c07_loop109 = 7
local_session_prior_c07_loop110 = 7
local_session_adjusted_before_this_loop = 45
this_loop_representative_trigger_count = 7
local_session_adjusted_after_this_loop = 52
need_to_30_after_this_loop = 0
need_to_50_after_this_loop = 0
```

Prior C07 symbol groups were excluded where possible:

```text
loop107 = 064290, 083450, 092870, 253590, 281820, 322310, 348210
loop108 = 089890, 217190, 232140, 240810, 319660, 382800
loop109 = 031980, 036810, 039030, 079370, 084370, 140860, 160980, 396470
loop110 = 039440, 053610, 089970, 140860, 240810, 281820, 348210
loop111 = 042700, 003160, 110990, 168360, 089790, 098460, 036930
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No loop111 representative trigger shares that hard duplicate key with the prior local C07 loops.

## 2. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The stock-web manifest basis used for this loop is `raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, and `symbol_count=5414`. Every representative trigger row below includes the canonical 30D/90D/180D MFE/MAE fields.

## 3. Historical Eligibility Gate

All representative rows use trigger dates with at least 180 stock-web trading-day forward windows before the atlas max date. Corporate-action screening is recorded as `clean_180D_window_profile_checked_no_recent_overlap`; rows requiring URL repair are retained as residual calibration coverage but blocked from promotion until evidence URLs are repaired.

## 4. Canonical Archetype Compression Map

| level | id | meaning |
|---|---|---|
| large sector | `L2_AI_SEMICONDUCTOR_ELECTRONICS` | AI / semiconductor / electronics historical calibration |
| canonical | `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` | HBM equipment relative strength that must convert into order/revenue/margin evidence |
| fine | `C07_HBM_DIRECT_AND_PROXY_EQUIPMENT_ORDER_REVENUE_BRIDGE_VS_RELATIVE_STRENGTH_FADE` | direct TC bonder/tester/laser/inspection positives versus source-proxy relative-strength fade |
| deep | `C07_DEEP_TCBONDER_TESTER_HANDLER_LASER_ANNEALING_INSPECTION_PROCESS_EQUIPMENT_ORDER_BRIDGE_VS_THEME_LABEL` | split direct customer order bridge from broad HBM label, C09 premium multiple, or C10 memory capex beta |

## 5. Research Hypothesis

C07 is a narrow bottleneck archetype. It should reward **verified HBM or advanced-packaging equipment order/revenue conversion**, not every semiconductor equipment chart that rises during an HBM cycle. The residual error after the current calibrated profile is boundary confusion:

```text
C07-positive = direct equipment order / tester supply / customer qualification-to-revenue bridge
C07-watch = HBM label + relative strength but no order/revenue bridge
C07-C09-redirect = advanced equipment premium multiple without order/revenue bridge
C07-C10-redirect = broad memory recovery equipment beta without C07-specific conversion
```

This loop does not loosen Stage3-Green. It proposes a C07-specific bridge gate and a stronger Stage4B-watch route for source-proxy label spikes.

## 6. Case Selection Summary

| case | symbol | company | trigger | entry_date | entry_price | role | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current verdict |
|---|---:|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| C07-R2-L111-042700 | 042700 | 한미반도체 | Stage3-Yellow | 2024-06-10 | 159,700 | positive_structural_success | 22.98% | -13.40% | 24.29% | -29.18% | 31.18% | -39.07% | current_profile_correct_if_Yellow_requires_confirmed_order_and_Green_keeps_revision_gate |
| C07-R2-L111-003160 | 003160 | 디아이 | Stage2-Actionable | 2024-10-22 | 18,450 | positive_structural_success | 16.26% | -17.34% | 49.59% | -21.95% | 84.28% | -21.95% | current_profile_too_conservative_if_domestic_HBM_tester_supply_bridge_not_counted_as_C07_actionable |
| C07-R2-L111-110990 | 110990 | 디아이티 | Stage2-Actionable | 2024-03-28 | 29,600 | positive_structural_success | 29.39% | -9.46% | 68.92% | -15.54% | 74.32% | -28.38% | current_profile_missed_actionable_if_laser_annealing_supply_bridge_is_zeroed_out |
| C07-R2-L111-168360 | 168360 | 펨트론 | Stage2-Actionable | 2024-12-03 | 7,720 | stage2_promote_candidate | 10.36% | -20.08% | 34.72% | -22.80% | 82.64% | -25.26% | current_profile_too_strict_if_HBM_inspection_tool_qualification_has_non_price_customer_signal |
| C07-R2-L111-089790 | 089790 | 제이티 | Stage4B | 2024-03-11 | 10,950 | failed_rerating | 33.79% | -11.87% | 35.16% | -33.79% | 35.16% | -42.92% | current_profile_false_positive_if_handler_proxy_unlocks_Yellow_without_order_revenue_bridge |
| C07-R2-L111-098460 | 098460 | 고영 | Stage4B | 2024-01-24 | 17,800 | failed_rerating | 22.47% | -13.20% | 28.09% | -32.58% | 28.09% | -42.70% | current_profile_false_positive_if_sector_candidate_label_promotes_without_contract_or_revenue_bridge |
| C07-R2-L111-036930 | 036930 | 주성엔지니어링 | Stage4B | 2025-04-04 | 38,600 | failed_rerating | 19.17% | -8.55% | 26.42% | -26.17% | 26.42% | -35.62% | current_profile_false_positive_if_broad_semicap_earnings_momentum_counted_as_C07_equipment_order_RS |


## 7. Case Notes

### 7.1 Positive structural paths

`042700 / 한미반도체` is the clean direct-order row. TC bonder order value and customer identity make this C07 rather than C09 price premium. The price path still requires a Green guard because large post-peak drawdown appears in the 180D window.

`003160 / 디아이` is a tester-localization row. The residual point is that domestic HBM tester supply evidence can deserve Stage2-Actionable credit before full revision confirmation, but the MAE path keeps it below unguarded Green.

`110990 / 디아이티` is a laser-annealing / strategic equipment bridge. It helps C07 because the trigger has non-price customer supply evidence, not just HBM vocabulary.

`168360 / 펨트론` is a qualification-to-revenue case. It should be counted as Stage2-Actionable only after customer test/commercialization evidence, and promotion remains blocked until URL repair or direct customer confirmation is available.

### 7.2 Counterexample and 4B-watch paths

`089790 / 제이티` shows the handler-proxy problem. A plausible HBM handler route can spike, but without direct order/revenue conversion it should stay at Stage4B-watch after local blowoff.

`098460 / 고영` shows the sector-candidate label problem. HBM inspection candidacy is not the same as C07 order conversion. It should not unlock Yellow by itself.

`036930 / 주성엔지니어링` is an important boundary row. It may be a strong semicap cycle name, but broad process-equipment earnings momentum is closer to C10/C09 unless the trigger explicitly contains C07 HBM equipment order/revenue conversion.

## 8. Machine-readable rows — JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C07-R2-L111-042700","symbol":"042700","ticker":"042700","company_name":"한미반도체","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_TCBONDER_CONFIRMED_CUSTOMER_ORDER_REVENUE_BRIDGE","case_type":"positive_structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"direct_TCBonder_order_positive_but_Green_not_loosened_due_to_post_peak_drawdown","current_profile_verdict":"current_profile_correct_if_Yellow_requires_confirmed_order_and_Green_keeps_revision_gate","price_source":"Songdaiki/stock-web","notes":"YNA / company disclosure reported SK hynix HBM dual TC bonder order; the non-price bridge is direct order value, not only relative strength."}
{"row_type":"trigger","trigger_id":"C07-R2-L111-042700-Stage3Yellow-2024-06-10","case_id":"C07-R2-L111-042700","symbol":"042700","ticker":"042700","company_name":"한미반도체","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_TCBONDER_CONFIRMED_CUSTOMER_ORDER_REVENUE_BRIDGE","sector":"AI_semiconductor_equipment","primary_archetype":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-06-07","evidence_available_at_that_date":"YNA / company disclosure reported SK hynix HBM dual TC bonder order; the non-price bridge is direct order value, not only relative strength.","evidence_source":"https://www.yna.co.kr/view/AKR20240607063600003","stage2_evidence_fields":["customer_order_quality","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-10","entry_price":159700,"MFE_30D_pct":22.98,"MFE_90D_pct":24.29,"MFE_180D_pct":31.18,"MAE_30D_pct":-13.4,"MAE_90D_pct":-29.18,"MAE_180D_pct":-39.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":209500,"drawdown_after_peak_pct":-46.92,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.58,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"valuation_blowoff;positioning_overheat","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"direct_TCBonder_order_positive_but_Green_not_loosened_due_to_post_peak_drawdown","current_profile_verdict":"current_profile_correct_if_Yellow_requires_confirmed_order_and_Green_keeps_revision_gate","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_checked_no_recent_overlap","same_entry_group_id":"C07_042700_Stage3-Yellow_2024-06-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"C07-R2-L111-042700","trigger_id":"C07-R2-L111-042700-Stage3Yellow-2024-06-10","symbol":"042700","company_name":"한미반도체","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":36,"margin_bridge_score":34,"revision_score":32,"relative_strength_score":78,"customer_quality_score":62,"valuation_repricing_score":66,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":46,"margin_bridge_score":42,"revision_score":36,"relative_strength_score":70,"customer_quality_score":68,"valuation_repricing_score":56,"execution_risk_score":62,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_after":80.5,"stage_label_after":"Stage3-Yellow_with_Green_guard","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow rule rewards verified HBM/advanced-packaging equipment order, tester supply, or revenue conversion; it caps broad relative-strength labels and reroutes premium multiple cases to Stage4B-watch/C09/C10 until non-price bridge appears.","MFE_90D_pct":24.29,"MAE_90D_pct":-29.18,"score_return_alignment_label":"direct_TCBonder_order_positive_but_Green_not_loosened_due_to_post_peak_drawdown","current_profile_verdict":"current_profile_correct_if_Yellow_requires_confirmed_order_and_Green_keeps_revision_gate"}
{"row_type":"case","case_id":"C07-R2-L111-003160","symbol":"003160","ticker":"003160","company_name":"디아이","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_BURNIN_TESTER_SUPPLY_BRIDGE","case_type":"positive_structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"tester_localization_positive_after_initial_MAE","current_profile_verdict":"current_profile_too_conservative_if_domestic_HBM_tester_supply_bridge_not_counted_as_C07_actionable","price_source":"Songdaiki/stock-web","notes":"DailyInvest / analyst channel described HBM burn-in tester supply and tester localization beneficiary route; source quality is usable as proxy until official order rows are repaired."}
{"row_type":"trigger","trigger_id":"C07-R2-L111-003160-Stage2Actionable-2024-10-22","case_id":"C07-R2-L111-003160","symbol":"003160","ticker":"003160","company_name":"디아이","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_BURNIN_TESTER_SUPPLY_BRIDGE","sector":"AI_semiconductor_equipment","primary_archetype":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-21","evidence_available_at_that_date":"DailyInvest / analyst channel described HBM burn-in tester supply and tester localization beneficiary route; source quality is usable as proxy until official order rows are repaired.","evidence_source":"https://www.dailyinvest.kr/news/articleView.html?idxno=61164","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv","profile_path":"atlas/symbol_profiles/003/003160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-22","entry_price":18450,"MFE_30D_pct":16.26,"MFE_90D_pct":49.59,"MFE_180D_pct":84.28,"MAE_30D_pct":-17.34,"MAE_90D_pct":-21.95,"MAE_180D_pct":-21.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-04-08","peak_price":34000,"drawdown_after_peak_pct":-38.97,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"positioning_overheat","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"tester_localization_positive_after_initial_MAE","current_profile_verdict":"current_profile_too_conservative_if_domestic_HBM_tester_supply_bridge_not_counted_as_C07_actionable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_checked_no_recent_overlap","same_entry_group_id":"C07_003160_Stage2-Actionable_2024-10-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"C07-R2-L111-003160","trigger_id":"C07-R2-L111-003160-Stage2Actionable-2024-10-22","symbol":"003160","company_name":"디아이","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":36,"margin_bridge_score":34,"revision_score":32,"relative_strength_score":78,"customer_quality_score":62,"valuation_repricing_score":66,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":68.5,"stage_label_before":"Watchlist-only","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":46,"margin_bridge_score":42,"revision_score":36,"relative_strength_score":70,"customer_quality_score":68,"valuation_repricing_score":56,"execution_risk_score":62,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_after":74.0,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow rule rewards verified HBM/advanced-packaging equipment order, tester supply, or revenue conversion; it caps broad relative-strength labels and reroutes premium multiple cases to Stage4B-watch/C09/C10 until non-price bridge appears.","MFE_90D_pct":49.59,"MAE_90D_pct":-21.95,"score_return_alignment_label":"tester_localization_positive_after_initial_MAE","current_profile_verdict":"current_profile_too_conservative_if_domestic_HBM_tester_supply_bridge_not_counted_as_C07_actionable"}
{"row_type":"case","case_id":"C07-R2-L111-110990","symbol":"110990","ticker":"110990","company_name":"디아이티","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_LASER_ANNEALING_CUSTOMER_SUPPLY_BRIDGE","case_type":"positive_structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"laser_annealing_positive_with_high_drawdown_guard","current_profile_verdict":"current_profile_missed_actionable_if_laser_annealing_supply_bridge_is_zeroed_out","price_source":"Songdaiki/stock-web","notes":"TheBell reported DIT supplying HBM advanced-process strategic equipment to SK hynix and increasing semiconductor revenue mix."}
{"row_type":"trigger","trigger_id":"C07-R2-L111-110990-Stage2Actionable-2024-03-28","case_id":"C07-R2-L111-110990","symbol":"110990","ticker":"110990","company_name":"디아이티","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_LASER_ANNEALING_CUSTOMER_SUPPLY_BRIDGE","sector":"AI_semiconductor_equipment","primary_archetype":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-28","evidence_available_at_that_date":"TheBell reported DIT supplying HBM advanced-process strategic equipment to SK hynix and increasing semiconductor revenue mix.","evidence_source":"https://m.thebell.co.kr/m/newsview.asp?newskey=202403271355162880106363&svccode=","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility","margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv","profile_path":"atlas/symbol_profiles/110/110990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-28","entry_price":29600,"MFE_30D_pct":29.39,"MFE_90D_pct":68.92,"MFE_180D_pct":74.32,"MAE_30D_pct":-9.46,"MAE_90D_pct":-15.54,"MAE_180D_pct":-28.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":51600,"drawdown_after_peak_pct":-43.61,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"valuation_blowoff","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"laser_annealing_positive_with_high_drawdown_guard","current_profile_verdict":"current_profile_missed_actionable_if_laser_annealing_supply_bridge_is_zeroed_out","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_checked_no_recent_overlap","same_entry_group_id":"C07_110990_Stage2-Actionable_2024-03-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"C07-R2-L111-110990","trigger_id":"C07-R2-L111-110990-Stage2Actionable-2024-03-28","symbol":"110990","company_name":"디아이티","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":36,"margin_bridge_score":34,"revision_score":32,"relative_strength_score":78,"customer_quality_score":62,"valuation_repricing_score":66,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":69.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":46,"margin_bridge_score":42,"revision_score":36,"relative_strength_score":70,"customer_quality_score":68,"valuation_repricing_score":56,"execution_risk_score":62,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_after":76.0,"stage_label_after":"Stage2-Actionable_with_MAE_guard","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow rule rewards verified HBM/advanced-packaging equipment order, tester supply, or revenue conversion; it caps broad relative-strength labels and reroutes premium multiple cases to Stage4B-watch/C09/C10 until non-price bridge appears.","MFE_90D_pct":68.92,"MAE_90D_pct":-15.54,"score_return_alignment_label":"laser_annealing_positive_with_high_drawdown_guard","current_profile_verdict":"current_profile_missed_actionable_if_laser_annealing_supply_bridge_is_zeroed_out"}
{"row_type":"case","case_id":"C07-R2-L111-168360","symbol":"168360","ticker":"168360","company_name":"펨트론","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_INSPECTION_QUALIFICATION_TO_REVENUE_BRIDGE","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"inspection_positive_but_qualification_lag","current_profile_verdict":"current_profile_too_strict_if_HBM_inspection_tool_qualification_has_non_price_customer_signal","price_source":"Songdaiki/stock-web","notes":"Daum/ETNews route reported HBM inspection equipment commercialization or supply testing; this is not yet full Green because qualification and recurring revenue still need confirmation."}
{"row_type":"trigger","trigger_id":"C07-R2-L111-168360-Stage2Actionable-2024-12-03","case_id":"C07-R2-L111-168360","symbol":"168360","ticker":"168360","company_name":"펨트론","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_INSPECTION_QUALIFICATION_TO_REVENUE_BRIDGE","sector":"AI_semiconductor_equipment","primary_archetype":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-02","evidence_available_at_that_date":"Daum/ETNews route reported HBM inspection equipment commercialization or supply testing; this is not yet full Green because qualification and recurring revenue still need confirmation.","evidence_source":"https://www.etnews.com/20240105000153","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","qualification_delay"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/168/168360/2024.csv","profile_path":"atlas/symbol_profiles/168/168360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-03","entry_price":7720,"MFE_30D_pct":10.36,"MFE_90D_pct":34.72,"MFE_180D_pct":82.64,"MAE_30D_pct":-20.08,"MAE_90D_pct":-22.8,"MAE_180D_pct":-25.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-05-29","peak_price":14100,"drawdown_after_peak_pct":-36.88,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"valuation_blowoff;qualification_delay","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"inspection_positive_but_qualification_lag","current_profile_verdict":"current_profile_too_strict_if_HBM_inspection_tool_qualification_has_non_price_customer_signal","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_checked_no_recent_overlap","same_entry_group_id":"C07_168360_Stage2-Actionable_2024-12-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"C07-R2-L111-168360","trigger_id":"C07-R2-L111-168360-Stage2Actionable-2024-12-03","symbol":"168360","company_name":"펨트론","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":36,"margin_bridge_score":34,"revision_score":32,"relative_strength_score":78,"customer_quality_score":62,"valuation_repricing_score":66,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":66.0,"stage_label_before":"Watchlist-only","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":46,"margin_bridge_score":42,"revision_score":36,"relative_strength_score":70,"customer_quality_score":68,"valuation_repricing_score":56,"execution_risk_score":62,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_after":73.5,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow rule rewards verified HBM/advanced-packaging equipment order, tester supply, or revenue conversion; it caps broad relative-strength labels and reroutes premium multiple cases to Stage4B-watch/C09/C10 until non-price bridge appears.","MFE_90D_pct":34.72,"MAE_90D_pct":-22.8,"score_return_alignment_label":"inspection_positive_but_qualification_lag","current_profile_verdict":"current_profile_too_strict_if_HBM_inspection_tool_qualification_has_non_price_customer_signal"}
{"row_type":"case","case_id":"C07-R2-L111-089790","symbol":"089790","ticker":"089790","company_name":"제이티","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_HANDLER_PROXY_WITHOUT_DIRECT_ORDER_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"handler_proxy_failed_rerating","current_profile_verdict":"current_profile_false_positive_if_handler_proxy_unlocks_Yellow_without_order_revenue_bridge","price_source":"Songdaiki/stock-web","notes":"TheInvest described JT as a possible HBM handler beneficiary but also emphasized that the impact was lower and less directly disclosed than Cube Prober routes."}
{"row_type":"trigger","trigger_id":"C07-R2-L111-089790-Stage4B-2024-03-11","case_id":"C07-R2-L111-089790","symbol":"089790","ticker":"089790","company_name":"제이티","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_HANDLER_PROXY_WITHOUT_DIRECT_ORDER_BRIDGE","sector":"AI_semiconductor_equipment","primary_archetype":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-03-08","evidence_available_at_that_date":"TheInvest described JT as a possible HBM handler beneficiary but also emphasized that the impact was lower and less directly disclosed than Cube Prober routes.","evidence_source":"https://www.theinvest.co.kr/article/765","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv","profile_path":"atlas/symbol_profiles/089/089790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-11","entry_price":10950,"MFE_30D_pct":33.79,"MFE_90D_pct":35.16,"MFE_180D_pct":35.16,"MAE_30D_pct":-11.87,"MAE_90D_pct":-33.79,"MAE_180D_pct":-42.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-09","peak_price":14800,"drawdown_after_peak_pct":-57.8,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_local_4B_watch_not_full_4B_without_non_price_thesis_break","four_b_evidence_type":"price_only_local_peak;valuation_blowoff;positioning_overheat","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"handler_proxy_failed_rerating","current_profile_verdict":"current_profile_false_positive_if_handler_proxy_unlocks_Yellow_without_order_revenue_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_checked_no_recent_overlap","same_entry_group_id":"C07_089790_Stage4B_2024-03-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"C07-R2-L111-089790","trigger_id":"C07-R2-L111-089790-Stage4B-2024-03-11","symbol":"089790","company_name":"제이티","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":24,"backlog_visibility_score":20,"margin_bridge_score":12,"revision_score":10,"relative_strength_score":78,"customer_quality_score":36,"valuation_repricing_score":66,"execution_risk_score":82,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":74.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":14,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":42,"customer_quality_score":28,"valuation_repricing_score":34,"execution_risk_score":90,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_after":60.5,"stage_label_after":"Stage4B-Watch","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow rule rewards verified HBM/advanced-packaging equipment order, tester supply, or revenue conversion; it caps broad relative-strength labels and reroutes premium multiple cases to Stage4B-watch/C09/C10 until non-price bridge appears.","MFE_90D_pct":35.16,"MAE_90D_pct":-33.79,"score_return_alignment_label":"handler_proxy_failed_rerating","current_profile_verdict":"current_profile_false_positive_if_handler_proxy_unlocks_Yellow_without_order_revenue_bridge"}
{"row_type":"case","case_id":"C07-R2-L111-098460","symbol":"098460","ticker":"098460","company_name":"고영","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_INSPECTION_METROLOGY_LABEL_WITHOUT_ORDER_REVENUE_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"inspection_label_false_positive","current_profile_verdict":"current_profile_false_positive_if_sector_candidate_label_promotes_without_contract_or_revenue_bridge","price_source":"Songdaiki/stock-web","notes":"Samsung sector update listed HBM inspection equipment candidates, including Goyoung, but the trigger remained a sector candidate label without company-specific order conversion."}
{"row_type":"trigger","trigger_id":"C07-R2-L111-098460-Stage4B-2024-01-24","case_id":"C07-R2-L111-098460","symbol":"098460","ticker":"098460","company_name":"고영","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_INSPECTION_METROLOGY_LABEL_WITHOUT_ORDER_REVENUE_BRIDGE","sector":"AI_semiconductor_equipment","primary_archetype":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-01-24","evidence_available_at_that_date":"Samsung sector update listed HBM inspection equipment candidates, including Goyoung, but the trigger remained a sector candidate label without company-specific order conversion.","evidence_source":"https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2020%2F2024012310041539K_02_05.pdf&inlineYn=Y&saveKey=research.pdf","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098460/2024.csv","profile_path":"atlas/symbol_profiles/098/098460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-24","entry_price":17800,"MFE_30D_pct":22.47,"MFE_90D_pct":28.09,"MFE_180D_pct":28.09,"MAE_30D_pct":-13.2,"MAE_90D_pct":-32.58,"MAE_180D_pct":-42.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-16","peak_price":22800,"drawdown_after_peak_pct":-55.44,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"good_local_4B_watch_not_full_4B_without_non_price_thesis_break","four_b_evidence_type":"price_only_local_peak;valuation_blowoff","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"inspection_label_false_positive","current_profile_verdict":"current_profile_false_positive_if_sector_candidate_label_promotes_without_contract_or_revenue_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_checked_no_recent_overlap","same_entry_group_id":"C07_098460_Stage4B_2024-01-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"C07-R2-L111-098460","trigger_id":"C07-R2-L111-098460-Stage4B-2024-01-24","symbol":"098460","company_name":"고영","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":24,"backlog_visibility_score":20,"margin_bridge_score":12,"revision_score":10,"relative_strength_score":78,"customer_quality_score":36,"valuation_repricing_score":66,"execution_risk_score":82,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":14,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":42,"customer_quality_score":28,"valuation_repricing_score":34,"execution_risk_score":90,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_after":61.0,"stage_label_after":"Stage4B-Watch_or_C09_redirect","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow rule rewards verified HBM/advanced-packaging equipment order, tester supply, or revenue conversion; it caps broad relative-strength labels and reroutes premium multiple cases to Stage4B-watch/C09/C10 until non-price bridge appears.","MFE_90D_pct":28.09,"MAE_90D_pct":-32.58,"score_return_alignment_label":"inspection_label_false_positive","current_profile_verdict":"current_profile_false_positive_if_sector_candidate_label_promotes_without_contract_or_revenue_bridge"}
{"row_type":"case","case_id":"C07-R2-L111-036930","symbol":"036930","ticker":"036930","company_name":"주성엔지니어링","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_PROCESS_EQUIPMENT_EARNINGS_MOMENTUM_WITHOUT_C07_ORDER_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"process_equipment_beta_not_C07_bridge","current_profile_verdict":"current_profile_false_positive_if_broad_semicap_earnings_momentum_counted_as_C07_equipment_order_RS","price_source":"Songdaiki/stock-web","notes":"TheLec 2025 post-earnings article placed Jusung in the semicap profit rebound group; C07 credit should require HBM-specific order/revenue bridge, otherwise this is C10/C09 beta."}
{"row_type":"trigger","trigger_id":"C07-R2-L111-036930-Stage4B-2025-04-04","case_id":"C07-R2-L111-036930","symbol":"036930","ticker":"036930","company_name":"주성엔지니어링","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_PROCESS_EQUIPMENT_EARNINGS_MOMENTUM_WITHOUT_C07_ORDER_BRIDGE","sector":"AI_semiconductor_equipment","primary_archetype":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2025-04-04","evidence_available_at_that_date":"TheLec 2025 post-earnings article placed Jusung in the semicap profit rebound group; C07 credit should require HBM-specific order/revenue bridge, otherwise this is C10/C09 beta.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=34412","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2025.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-04-04","entry_price":38600,"MFE_30D_pct":19.17,"MFE_90D_pct":26.42,"MFE_180D_pct":26.42,"MAE_30D_pct":-8.55,"MAE_90D_pct":-26.17,"MAE_180D_pct":-35.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-05-21","peak_price":48800,"drawdown_after_peak_pct":-49.02,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"good_local_4B_watch_not_full_4B_without_non_price_thesis_break","four_b_evidence_type":"price_only_local_peak;valuation_blowoff;margin_or_backlog_slowdown","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"process_equipment_beta_not_C07_bridge","current_profile_verdict":"current_profile_false_positive_if_broad_semicap_earnings_momentum_counted_as_C07_equipment_order_RS","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_checked_no_recent_overlap","same_entry_group_id":"C07_036930_Stage4B_2025-04-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"C07-R2-L111-036930","trigger_id":"C07-R2-L111-036930-Stage4B-2025-04-04","symbol":"036930","company_name":"주성엔지니어링","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":24,"backlog_visibility_score":20,"margin_bridge_score":12,"revision_score":10,"relative_strength_score":78,"customer_quality_score":36,"valuation_repricing_score":66,"execution_risk_score":82,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":72.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":14,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":42,"customer_quality_score":28,"valuation_repricing_score":34,"execution_risk_score":90,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_after":59.5,"stage_label_after":"Stage4B-Watch_or_C10_redirect","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow rule rewards verified HBM/advanced-packaging equipment order, tester supply, or revenue conversion; it caps broad relative-strength labels and reroutes premium multiple cases to Stage4B-watch/C09/C10 until non-price bridge appears.","MFE_90D_pct":26.42,"MAE_90D_pct":-26.17,"score_return_alignment_label":"process_equipment_beta_not_C07_bridge","current_profile_verdict":"current_profile_false_positive_if_broad_semicap_earnings_momentum_counted_as_C07_equipment_order_RS"}
{"row_type":"aggregate","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_DIRECT_AND_PROXY_EQUIPMENT_ORDER_REVENUE_BRIDGE_VS_RELATIVE_STRENGTH_FADE","calibration_usable_trigger_count":7,"representative_trigger_count":7,"new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"new_trigger_family_count":7,"positive_case_count":4,"counterexample_count":3,"stage4b_case_count":3,"stage4c_case_count":0,"current_profile_error_count":6,"source_proxy_only_count":5,"evidence_url_pending_count":1,"narrative_only_or_rejected_count":0,"auto_selected_coverage_gap":"C07 base index 18 + local loop107 7 + loop108 6 + loop109 7 + loop110 7 + loop111 7 = local-session adjusted about 52; 50-row practical calibration band reached locally","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"new_axis_proposed":"C07_verified_direct_or_proxy_equipment_order_revenue_bridge_required_before_Yellow_or_Green_plus_relative_strength_fade_to_4B_watch_v5","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_weakened":null}
{"row_type":"shadow_weight","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","shadow_rule_candidate_id":"C07_verified_equipment_order_revenue_bridge_before_Yellow_or_Green_v5","target_scope":"canonical_archetype_specific","production_scoring_changed_now":false,"shadow_weight_only":true,"proposed_component_directions":{"contract_score":"increase only for verified equipment supply/order, customer shipment, or tester qualification-to-revenue bridge","backlog_visibility_score":"increase only when delivery or revenue conversion is visible","relative_strength_score":"cap if HBM label is source-proxy-only after local price blowoff","valuation_repricing_score":"cap after local blowoff without margin/revision bridge","execution_risk_score":"increase for MAE90/MAE180 below -20% and no confirmed order bridge"},"implementation_status":"deferred_coding_agent_only"}
{"row_type":"residual_contribution","round":"R2","loop":"111","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C07_direct_order_bridge_missed","C07_source_proxy_label_false_positive","C07_C09_C10_boundary_confusion","post_peak_high_MAE_guard_needed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 9. Aggregate / Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07_HBM_DIRECT_AND_PROXY_EQUIPMENT_ORDER_REVENUE_BRIDGE_VS_RELATIVE_STRENGTH_FADE | 4 | 3 | 3 | 0 | 7 | 0 | 7 | 7 | 6 | true | true | local-session adjusted ≈52; 50-row practical calibration band reached |

```text
avg_MFE_90D_pct = 38.17
avg_MAE_90D_pct = -26.0
avg_MFE_180D_pct = 51.73
avg_MAE_180D_pct = -33.7
positive_counterexample_balance = 4:3
source_proxy_only_count = 5
evidence_url_pending_count = 1
```

## 10. Existing Axis Stress Test

```text
existing_axis_tested = stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened = null
existing_axis_kept = stage3_green_total_min, stage3_green_revision_min
new_axis_proposed = C07_verified_direct_or_proxy_equipment_order_revenue_bridge_required_before_Yellow_or_Green_plus_relative_strength_fade_to_4B_watch_v5
```

The main residual is not that the global bridge rule is wrong. It is that C07 needs a finer bridge definition: direct equipment order/revenue conversion should survive Stage2/Yellow, while source-proxy labels and broad memory beta should be capped or redirected.

## 11. Proposed Shadow Rule Candidate

```json
{
  "row_type": "shadow_rule_candidate",
  "axis": "C07_verified_direct_or_proxy_equipment_order_revenue_bridge_required_before_Yellow_or_Green_plus_relative_strength_fade_to_4B_watch_v5",
  "scope": {
    "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
    "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
  },
  "rule_type": "canonical_archetype_specific_gate",
  "positive_gate": [
    "verified_equipment_order_or_supply",
    "customer_or_tool_shipment_visibility",
    "tester_or_inspection_qualification_to_revenue_bridge",
    "relative_strength_not_price_only",
    "no_C09_premium_multiple_redirect"
  ],
  "watch_or_4B_gate": [
    "HBM_or_advanced_packaging_label_only",
    "source_proxy_only_after_local_blowoff",
    "memory_beta_without_C07_order_bridge",
    "premium_multiple_without_revenue_or_margin_bridge",
    "MAE90_or_MAE180_below_minus_20_pct"
  ],
  "stage3_green_not_loosened": true,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 12. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 13. Residual Contribution Summary

This loop adds 7 new independent cases, 3 counterexamples, and 6 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: C07_direct_order_bridge_missed, C07_source_proxy_label_false_positive, C07_C09_C10_boundary_confusion, post_peak_high_MAE_guard_needed
new_axis_proposed: C07_verified_direct_or_proxy_equipment_order_revenue_bridge_required_before_Yellow_or_Green_plus_relative_strength_fade_to_4B_watch_v5
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 14. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for stock_agent. Do not execute this handoff during the research session that produced this MD.

Input MD:
e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md

Task:
1. Ingest this MD only after normal V12 parser validation.
2. Verify every row_type="trigger" against Songdaiki/stock-web tradable shards.
3. Reject rows whose entry_date/entry_price or MFE/MAE fields do not match atlas recomputation.
4. Treat the proposed C07 rule as shadow-only until enough verified URL rows exist.
5. Do not loosen Stage3-Green. Only test a canonical C07 bridge gate and C07-to-4B/C09/C10 redirection for source-proxy label spikes.
6. Batch this with other V12 residual MD files; do not patch production scoring from this file alone.
```

## 15. Next Research State

```text
completed_round = R2
completed_loop = 111
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C11_BATTERY_ORDERBOOK_RERATING, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
