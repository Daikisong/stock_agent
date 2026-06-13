# E2R v12 Residual Research — R1 / C02 Power Grid & Datacenter CAPEX — loop 146

```text
output_file = e2r_stock_web_v12_residual_round_R1_loop_146_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round = R1
selected_loop = 146
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = mixed_c02_fourth_pass_order_capa_revenue_conversion_leaf_set
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still marks C02 as Priority 0 with 10 representative rows, 20 rows short of the 30-row stability threshold. Session-aware prior C02 work already covered the transformer/cable headline cluster (`267260`, `298040`, `024840`, `006340`, `033100`, `103590`, `062040`, `147830`, `017040`, `010120`, `229640`, `001440`, `017510`, `189860`). This loop therefore uses a new C02 leaf set: datacenter backup generator, smart-grid switchgear, distribution automation, indirect Eaton smart-breaker, subsea grid installation, and holding-company look-through rerating.

This loop adds 6 new independent cases, 3 counterexamples, and 5 residual errors for R1/L1/C02.

```text
new_independent_case_count = 6
reused_case_count = 0
new_symbol_count = 6
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
positive_case_count = 3
counterexample_count = 3
current_profile_error_count = 5
diversity_score_summary = C02 fourth pass avoids prior session C02 symbol clusters and fills non-transformer C02 propagation paths: generator, switchgear, automation, subsea cable installation, and holding-company NAV rerating.
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

## 2. Price atlas validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
manifest_tradable_row_count = 14354401
entry_rule = next tradable date after public trigger date; entry_price = entry_date close
MFE_MAE_rule = max(high) / min(low) over inclusive entry row through 30/90/180 tradable rows
```

Corporate-action window checks used each symbol profile. All trigger rows below are `calibration_usable=true` because no corporate-action candidate overlaps entry_date through D+180.

## 3. Trigger-level price path summary

| ticker | name | trigger | entry | price | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | role |
|---|---|---|---|---:|---:|---:|---:|---|
| 119850 | 지엔씨에너지 | Stage2-Actionable | 2025-04-07 | 13750 | 124.73/-0.15 | 180.00/-0.15 | 240.00/-0.15 | structural_success |
| 388050 | 지투파워 | Stage2 | 2024-05-02 | 9080 | 40.31/-2.20 | 40.31/-38.66 | 40.31/-45.37 | 4B_overlay_success |
| 237750 | 피앤씨테크 | Stage4B | 2024-06-28 | 6130 | 15.17/-27.57 | 15.17/-30.34 | 15.17/-46.49 | failed_rerating |
| 199820 | 제일일렉트릭 | Stage2-Actionable | 2024-09-23 | 9710 | 13.29/-14.21 | 55.72/-19.46 | 55.72/-26.98 | high_mae_success |
| 060370 | LS마린솔루션 | Stage2 | 2024-08-08 | 16800 | 28.27/-6.25 | 28.27/-32.74 | 28.27/-32.74 | 4B_overlay_success |
| 006260 | LS | Stage2-Actionable | 2025-01-17 | 117000 | 16.84/-11.79 | 50.68/-18.46 | 88.03/-18.46 | structural_success |


## 4. Case notes

### 4.1 지엔씨에너지 / 119850 — datacenter generator contract becomes revenue bridge

- **Trigger:** 2025-04-04 data-center emergency generator contract; next tradable entry 2025-04-07.
- **Why C02:** This is not a transformer/cable supplier, but datacenter CAPEX still needs backup generation. C02 should not be too narrow.
- **Path:** MFE180 +240.00%, MAE180 -0.15%.
- **Residual:** current C02 rules may miss this because the bridge is generator EPC rather than grid equipment. Proposed rule should include datacenter power-resilience equipment when named contract and revenue conversion exist.

### 4.2 지투파워 / 388050 — switchgear turnaround works only with exit guard

- **Trigger:** 2024-04-30 report forecasting switchgear-led 2024 turnaround; next tradable entry 2024-05-02.
- **Path:** MFE30 +40.31%, but MAE180 -45.37%.
- **Residual:** Stage2 was not completely wrong, but it became a classic local 4B problem. C02 needs a rule that early MFE without durable revenue/margin follow-through requires exit guard.

### 4.3 피앤씨테크 / 237750 — distribution automation vocabulary without commercial bridge

- **Trigger:** 2024-06-27 power shortage / government support theme; next tradable entry 2024-06-28.
- **Path:** MFE180 only +15.17%, MAE180 -46.49%.
- **Residual:** distribution automation is C02-relevant, but the trigger was vocabulary/policy support rather than order, backlog, or margin conversion. This should be Stage4B watch, not Stage2-Actionable.

### 4.4 제일일렉트릭 / 199820 — global OEM bridge is real, but needs staged entry

- **Trigger:** 2024-09-20 Eaton smart breaker / PCB ASSY growth report; next tradable entry 2024-09-23.
- **Path:** MFE90 +55.72%, MAE180 -26.98%.
- **Residual:** indirect global OEM supply can be a valid C02 bridge, but high MAE says it should not unlock Green without order renewal or actual shipment/margin confirmation.

### 4.5 LS마린솔루션 / 060370 — subsea power-grid capability needs project timing guard

- **Trigger:** 2024-08-07 report on GL2030 / HVDC#3 / subsea power-cable installation capability; next tradable entry 2024-08-08.
- **Path:** MFE30 +28.27%, MAE90 -32.74%.
- **Residual:** capability and LS-group synergy are real, but capital intensity and project timing made early Stage2 too loose. Keep C02 relevance, add 4B exit guard.

### 4.6 LS / 006260 — holding-company look-through rerating can still be C02

- **Trigger:** 2025-01-16 LS report / grid-capex look-through rerating; next tradable entry 2025-01-17.
- **Path:** MFE180 +88.03%, MAE180 -18.46%.
- **Residual:** C02 should allow holding-company look-through if the market is rerating identifiable C02 subsidiaries, but apply a holding-company discount and require NAV/revision linkage.

## 5. Current calibrated profile stress test

| ticker | current calibrated proxy likely action | actual path | residual judgement |
|---|---|---|---|
| 119850 | may under-route to C02 because generator is not classic grid gear | strong clean trend | missed structural if C02 excludes datacenter power-resilience equipment |
| 388050 | Stage2/Actionable if forecast turnover is over-weighted | fast MFE then -45% MAE | needs local 4B exit guard |
| 237750 | Stage2 if policy/grid vocabulary is over-weighted | weak MFE and deep MAE | false positive; block Stage2-Actionable |
| 199820 | Stage2 but perhaps too conservative before signed renewal | strong 90D MFE, later MAE | permit Stage2-Actionable, attach staged-entry guard |
| 060370 | Stage2 if grid-capex capability is enough | short-lived MFE then -32% MAE | project-timing/capital-intensity guard required |
| 006260 | Stage2 or watch because holding-company proxy | strong 180D MFE | allow C02 look-through when subsidiary bridge is explicit |

## 6. Proposed shadow rule candidate

```text
rule_candidate_id = C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4
scope = canonical_archetype_id:C02_POWER_GRID_DATACENTER_CAPEX
new_axis_proposed = c02_order_capa_revenue_conversion_and_4b_exit_gate_v4
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
```

**Rule:** For C02, Stage2-Actionable requires at least one hard commercial bridge and one conversion bridge.

Hard commercial bridge examples:

1. named datacenter/grid customer order,
2. backlog or capacity lock-up,
3. global OEM/customer forecast with line readiness,
4. subsidiary look-through NAV bridge for holdings,
5. project capability tied to identifiable awarded work.

Conversion bridge examples:

1. revenue recognition window,
2. margin or revision bridge,
3. shipment or delivery timing,
4. confirmed earnings conversion,
5. FCF or working-capital improvement.

If the evidence is only policy/theme/product category, or if MFE30 is followed by MAE90 <= -30%, the row should be Stage4B watch or Stage2 with exit guard, not Green.

## 7. Machine-readable trigger rows (JSONL)

```jsonl
{"row_type":"trigger","case_id":"C02_R1_L146_119850_20250407_GNC_DC_GENERATOR_CONTRACT","ticker":"119850","name":"지엔씨에너지","market":"KOSDAQ","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DATACENTER_BACKUP_GENERATOR_CONTRACT_REVENUE_BRIDGE","trigger_type":"Stage2-Actionable","trigger_family":"named_datacenter_generator_contract","case_role":"structural_success","trigger_date":"2025-04-04","entry_date":"2025-04-07","entry_price":13750.0,"entry_price_basis":"entry_date_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":124.73,"MAE_30D_pct":-0.15,"MFE_90D_pct":180.0,"MAE_90D_pct":-0.15,"MFE_180D_pct":240.0,"MAE_180D_pct":-0.15,"peak_30D_date":"2025-05-15","trough_30D_date":"2025-04-07","peak_90D_date":"2025-07-16","trough_90D_date":"2025-04-07","peak_180D_date":"2025-10-29","trough_180D_date":"2025-04-07","window_30D_end":"2025-05-21","window_90D_end":"2025-08-18","window_180D_end":"2025-12-30","forward_window_trading_days":180,"corporate_action_window_status":"clear_no_candidate_in_entry_to_D180_window","calibration_usable":true,"calibration_block_reasons":[],"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|119850|Stage2-Actionable|2025-04-07","same_entry_group_id":"119850|2025-04-07|C02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url":"https://www.newsprime.co.kr/news/article.html?no=682123","secondary_evidence_url":"https://www.electimes.com/news/articleView.html?idxno=354952","evidence_summary":"2025-04-04 데이터센터 비상발전기 265억원 규모 계약이 확인되고, 이후 1Q25 분기 최대 실적으로 매출·영업이익 bridge가 확인됨.","current_profile_expected_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage3-Yellow watch after earnings confirmation","current_profile_error":"too_late_if_generator_not_mapped_to_C02_core","raw_component_score_breakdown":{"eps_fcf":17,"visibility":20,"bottleneck":17,"mispricing":11,"valuation":8,"capital_allocation":2,"information_confidence":5,"total":80}}
{"row_type":"trigger","case_id":"C02_R1_L146_388050_20240502_G2POWER_TURNAROUND_REPORT","ticker":"388050","name":"지투파워","market":"KOSDAQ","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMART_GRID_SWITCHGEAR_TURNAROUND_BUT_EXIT_GUARD","trigger_type":"Stage2","trigger_family":"smart_grid_switchgear_turnaround_forecast","case_role":"4B_overlay_success","trigger_date":"2024-04-30","entry_date":"2024-05-02","entry_price":9080.0,"entry_price_basis":"entry_date_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":40.31,"MAE_30D_pct":-2.2,"MFE_90D_pct":40.31,"MAE_90D_pct":-38.66,"MFE_180D_pct":40.31,"MAE_180D_pct":-45.37,"peak_30D_date":"2024-05-29","trough_30D_date":"2024-05-03","peak_90D_date":"2024-05-29","trough_90D_date":"2024-08-05","peak_180D_date":"2024-05-29","trough_180D_date":"2024-10-04","window_30D_end":"2024-06-17","window_90D_end":"2024-09-10","window_180D_end":"2025-01-31","forward_window_trading_days":180,"corporate_action_window_status":"clear_no_candidate_in_entry_to_D180_window","calibration_usable":true,"calibration_block_reasons":[],"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|388050|Stage2|2024-05-02","same_entry_group_id":"388050|2024-05-02|C02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1714433119383.pdf","secondary_evidence_url":"https://www.electimes.com/news/articleView.html?idxno=350255","evidence_summary":"2024-04-30 report expected 2024 수배전반 중심 매출 605억원·영업이익 흑자전환. 30D MFE는 강했지만 90/180D MAE가 -38%/-45%로 4B exit guard 필요.","current_profile_expected_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage2 with mandatory local_4B_exit_guard","current_profile_error":"false_positive_if_turnaround_forecast_treated_like_signed_backlog","raw_component_score_breakdown":{"eps_fcf":12,"visibility":16,"bottleneck":11,"mispricing":10,"valuation":7,"capital_allocation":2,"information_confidence":4,"total":62}}
{"row_type":"trigger","case_id":"C02_R1_L146_237750_20240628_PNC_GOV_GRID_THEME","ticker":"237750","name":"피앤씨테크","market":"KOSDAQ","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DISTRIBUTION_AUTOMATION_POLICY_THEME_NO_ORDER_BRIDGE","trigger_type":"Stage4B","trigger_family":"policy_support_distribution_automation_theme","case_role":"failed_rerating","trigger_date":"2024-06-27","entry_date":"2024-06-28","entry_price":6130.0,"entry_price_basis":"entry_date_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":15.17,"MAE_30D_pct":-27.57,"MFE_90D_pct":15.17,"MAE_90D_pct":-30.34,"MFE_180D_pct":15.17,"MAE_180D_pct":-46.49,"peak_30D_date":"2024-07-17","trough_30D_date":"2024-08-05","peak_90D_date":"2024-07-17","trough_90D_date":"2024-11-11","peak_180D_date":"2024-07-17","trough_180D_date":"2024-12-09","window_30D_end":"2024-08-08","window_90D_end":"2024-11-11","window_180D_end":"2025-03-27","forward_window_trading_days":180,"corporate_action_window_status":"clear_no_candidate_in_entry_to_D180_window","calibration_usable":true,"calibration_block_reasons":[],"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|237750|Stage4B|2024-06-28","same_entry_group_id":"237750|2024-06-28|C02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url":"https://v.daum.net/v/qh7Em3j43R?f=p","secondary_evidence_url":"https://w4.kirs.or.kr/download/research/250529_%EC%9D%BC%EB%B0%98%EC%A0%84%EA%B8%B0%EC%A0%84%EC%9E%90_%ED%94%BC%EC%95%A4%EC%94%A8%ED%85%8C%ED%81%AC%28237750%29_%EC%A0%84%EB%A0%A5%EB%A7%9D%20%EC%9E%90%EB%8F%99%ED%99%94%EC%97%90%20%ED%95%B5%EC%8B%AC%20%EC%A0%9C%ED%92%88%EC%9D%84%20%EA%B0%9C%EB%B0%9C%20%EB%B0%8F%20%EC%83%81%EC%9A%A9%ED%99%94%ED%95%98%EB%8A%94%20%EC%A0%84%EB%A0%A5%20IT%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_%ED%95%9C%EA%B5%AD%EA%B8%B0%EC%88%A0%EC%8B%A0%EC%9A%A9%ED%8F%89%EA%B0%80%28%EC%A3%BC%29.pdf","evidence_summary":"배전자동화·보호계전기라는 C02 제품 노출은 있었지만 2024-06-27 이벤트는 정부 전력난 지원/테마성 노출 중심. order/backlog/revenue bridge 부재로 Stage4B watch가 맞았음.","current_profile_expected_stage":"Stage2","proposed_shadow_stage":"Stage4B watch / block Stage2-Actionable","current_profile_error":"false_positive_if_policy_grid_vocabulary_overrides_order_bridge_absence","raw_component_score_breakdown":{"eps_fcf":8,"visibility":12,"bottleneck":8,"mispricing":9,"valuation":6,"capital_allocation":1,"information_confidence":4,"total":48}}
{"row_type":"trigger","case_id":"C02_R1_L146_199820_20240923_CHEIL_EATON_SMART_BREAKER","ticker":"199820","name":"제일일렉트릭","market":"KOSDAQ","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"NORTH_AMERICA_SMART_BREAKER_CUSTOMER_FORECAST_HIGH_MAE","trigger_type":"Stage2-Actionable","trigger_family":"global_oem_smart_breaker_customer_forecast","case_role":"high_mae_success","trigger_date":"2024-09-20","entry_date":"2024-09-23","entry_price":9710.0,"entry_price_basis":"entry_date_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":13.29,"MAE_30D_pct":-14.21,"MFE_90D_pct":55.72,"MAE_90D_pct":-19.46,"MFE_180D_pct":55.72,"MAE_180D_pct":-26.98,"peak_30D_date":"2024-09-27","trough_30D_date":"2024-11-04","peak_90D_date":"2025-01-17","trough_90D_date":"2024-12-10","peak_180D_date":"2025-01-17","trough_180D_date":"2025-04-09","window_30D_end":"2024-11-06","window_90D_end":"2025-02-07","window_180D_end":"2025-06-23","forward_window_trading_days":180,"corporate_action_window_status":"clear_candidates_before_entry_only","calibration_usable":true,"calibration_block_reasons":[],"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|199820|Stage2-Actionable|2024-09-23","same_entry_group_id":"199820|2024-09-23|C02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url":"https://file.myasset.com/sitemanager/upload/2024/0918/122343/20240918122343983_0_ko.pdf","secondary_evidence_url":"https://www.kmnanews.com/news/articleView.html?idxno=7805","evidence_summary":"Eaton 스마트브레이커 2.0 신규 매출처와 생산라인/시제품 준비가 확인되며 indirect C02 bridge를 제공. 단 180D MAE -26.98%로 staged entry가 필요.","current_profile_expected_stage":"Stage2","proposed_shadow_stage":"Stage2-Actionable but high-MAE staged-entry guard","current_profile_error":"too_conservative_if_indirect_global_oem_bridge_is_ignored; too_aggressive_if_no_staged_entry_guard","raw_component_score_breakdown":{"eps_fcf":16,"visibility":18,"bottleneck":15,"mispricing":11,"valuation":8,"capital_allocation":2,"information_confidence":5,"total":75}}
{"row_type":"trigger","case_id":"C02_R1_L146_060370_20240808_LS_MARINE_HVDC_INSTALLATION_CAPEX","ticker":"060370","name":"LS마린솔루션","market":"KOSDAQ","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SUBSEA_POWER_GRID_CABLE_INSTALLATION_CAPEX_4B_EXIT","trigger_type":"Stage2","trigger_family":"subsea_power_grid_installation_capacity_report","case_role":"4B_overlay_success","trigger_date":"2024-08-07","entry_date":"2024-08-08","entry_price":16800.0,"entry_price_basis":"entry_date_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.27,"MAE_30D_pct":-6.25,"MFE_90D_pct":28.27,"MAE_90D_pct":-32.74,"MFE_180D_pct":28.27,"MAE_180D_pct":-32.74,"peak_30D_date":"2024-08-19","trough_30D_date":"2024-09-05","peak_90D_date":"2024-08-19","trough_90D_date":"2024-11-21","peak_180D_date":"2024-08-19","trough_180D_date":"2024-11-21","window_30D_end":"2024-09-24","window_90D_end":"2024-12-20","window_180D_end":"2025-05-12","forward_window_trading_days":180,"corporate_action_window_status":"clear_2025_08_28_candidate_after_D180_only","calibration_usable":true,"calibration_block_reasons":[],"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|060370|Stage2|2024-08-08","same_entry_group_id":"060370|2024-08-08|C02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url":"https://w4.kirs.or.kr/download/research/240807_LS%EB%A7%88%EB%A6%B0%EC%86%94%EB%A3%A8%EC%85%98.pdf","secondary_evidence_url":"https://www.thevaluenews.co.kr/news/185476","evidence_summary":"GL2030/HVDC#3/해저 전력케이블 시공 capability는 C02 capex path이나, 선박·유상증자·프로젝트 timing으로 30D 이후 경로가 꺾여 4B exit guard가 필요.","current_profile_expected_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage2 with project timing + capital-intensity 4B guard","current_profile_error":"false_positive_if_grid_capex_capability_is_treated_as_near_term_revenue_backlog","raw_component_score_breakdown":{"eps_fcf":13,"visibility":18,"bottleneck":14,"mispricing":10,"valuation":7,"capital_allocation":3,"information_confidence":5,"total":70}}
{"row_type":"trigger","case_id":"C02_R1_L146_006260_20250117_LS_GRID_CAPEX_HOLDING_RERATING","ticker":"006260","name":"LS","market":"KOSPI","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HOLDING_COMPANY_GRID_CAPEX_SUBSIDIARY_LOOKTHROUGH","trigger_type":"Stage2-Actionable","trigger_family":"holding_company_grid_capex_lookthrough_revaluation","case_role":"structural_success","trigger_date":"2025-01-16","entry_date":"2025-01-17","entry_price":117000.0,"entry_price_basis":"entry_date_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.84,"MAE_30D_pct":-11.79,"MFE_90D_pct":50.68,"MAE_90D_pct":-18.46,"MFE_180D_pct":88.03,"MAE_180D_pct":-18.46,"peak_30D_date":"2025-02-19","trough_30D_date":"2025-03-06","peak_90D_date":"2025-06-04","trough_90D_date":"2025-04-09","peak_180D_date":"2025-07-01","trough_180D_date":"2025-04-09","window_30D_end":"2025-03-06","window_90D_end":"2025-06-04","window_180D_end":"2025-10-17","forward_window_trading_days":180,"corporate_action_window_status":"clear_no_candidate_in_entry_to_D180_window","calibration_usable":true,"calibration_block_reasons":[],"dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|006260|Stage2-Actionable|2025-01-17","same_entry_group_id":"006260|2025-01-17|C02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url":"https://stock.pstatic.net/stock-research/company/16/20250116_company_635918000.pdf","secondary_evidence_url":"https://www.lsholdings.com/","evidence_summary":"LS전선/LS ELECTRIC/LS MnM look-through 재평가가 가능한 지주회사형 C02. 자회사 grid capex와 전력기기 가치가 시총에 전이되는 path가 강했음.","current_profile_expected_stage":"Stage2","proposed_shadow_stage":"Stage2-Actionable with holding-company look-through discount applied","current_profile_error":"missed_structural_if_C02_requires_pure_operating_subsidiary_only","raw_component_score_breakdown":{"eps_fcf":16,"visibility":20,"bottleneck":17,"mispricing":13,"valuation":11,"capital_allocation":5,"information_confidence":4,"total":86}}
```

## 8. Machine-readable score simulations (JSONL)

```jsonl
{"row_type":"score_simulation","case_id":"C02_R1_L146_119850_20250407_GNC_DC_GENERATOR_CONTRACT","ticker":"119850","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4_shadow","rollback_reference_profile_id":"e2r_2_0_baseline_reference","current_profile_expected_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage3-Yellow watch after earnings confirmation","raw_component_score_breakdown":{"eps_fcf":17,"visibility":20,"bottleneck":17,"mispricing":11,"valuation":8,"capital_allocation":2,"information_confidence":5,"total":80},"actual_90D_MFE_pct":180.0,"actual_90D_MAE_pct":-0.15,"actual_180D_MFE_pct":240.0,"actual_180D_MAE_pct":-0.15,"score_return_alignment":"aligned"}
{"row_type":"score_simulation","case_id":"C02_R1_L146_388050_20240502_G2POWER_TURNAROUND_REPORT","ticker":"388050","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4_shadow","rollback_reference_profile_id":"e2r_2_0_baseline_reference","current_profile_expected_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage2 with mandatory local_4B_exit_guard","raw_component_score_breakdown":{"eps_fcf":12,"visibility":16,"bottleneck":11,"mispricing":10,"valuation":7,"capital_allocation":2,"information_confidence":4,"total":62},"actual_90D_MFE_pct":40.31,"actual_90D_MAE_pct":-38.66,"actual_180D_MFE_pct":40.31,"actual_180D_MAE_pct":-45.37,"score_return_alignment":"needs_guard_or_false_positive"}
{"row_type":"score_simulation","case_id":"C02_R1_L146_237750_20240628_PNC_GOV_GRID_THEME","ticker":"237750","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4_shadow","rollback_reference_profile_id":"e2r_2_0_baseline_reference","current_profile_expected_stage":"Stage2","proposed_shadow_stage":"Stage4B watch / block Stage2-Actionable","raw_component_score_breakdown":{"eps_fcf":8,"visibility":12,"bottleneck":8,"mispricing":9,"valuation":6,"capital_allocation":1,"information_confidence":4,"total":48},"actual_90D_MFE_pct":15.17,"actual_90D_MAE_pct":-30.34,"actual_180D_MFE_pct":15.17,"actual_180D_MAE_pct":-46.49,"score_return_alignment":"needs_guard_or_false_positive"}
{"row_type":"score_simulation","case_id":"C02_R1_L146_199820_20240923_CHEIL_EATON_SMART_BREAKER","ticker":"199820","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4_shadow","rollback_reference_profile_id":"e2r_2_0_baseline_reference","current_profile_expected_stage":"Stage2","proposed_shadow_stage":"Stage2-Actionable but high-MAE staged-entry guard","raw_component_score_breakdown":{"eps_fcf":16,"visibility":18,"bottleneck":15,"mispricing":11,"valuation":8,"capital_allocation":2,"information_confidence":5,"total":75},"actual_90D_MFE_pct":55.72,"actual_90D_MAE_pct":-19.46,"actual_180D_MFE_pct":55.72,"actual_180D_MAE_pct":-26.98,"score_return_alignment":"aligned"}
{"row_type":"score_simulation","case_id":"C02_R1_L146_060370_20240808_LS_MARINE_HVDC_INSTALLATION_CAPEX","ticker":"060370","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4_shadow","rollback_reference_profile_id":"e2r_2_0_baseline_reference","current_profile_expected_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage2 with project timing + capital-intensity 4B guard","raw_component_score_breakdown":{"eps_fcf":13,"visibility":18,"bottleneck":14,"mispricing":10,"valuation":7,"capital_allocation":3,"information_confidence":5,"total":70},"actual_90D_MFE_pct":28.27,"actual_90D_MAE_pct":-32.74,"actual_180D_MFE_pct":28.27,"actual_180D_MAE_pct":-32.74,"score_return_alignment":"needs_guard_or_false_positive"}
{"row_type":"score_simulation","case_id":"C02_R1_L146_006260_20250117_LS_GRID_CAPEX_HOLDING_RERATING","ticker":"006260","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4_shadow","rollback_reference_profile_id":"e2r_2_0_baseline_reference","current_profile_expected_stage":"Stage2","proposed_shadow_stage":"Stage2-Actionable with holding-company look-through discount applied","raw_component_score_breakdown":{"eps_fcf":16,"visibility":20,"bottleneck":17,"mispricing":13,"valuation":11,"capital_allocation":5,"information_confidence":4,"total":86},"actual_90D_MFE_pct":50.68,"actual_90D_MAE_pct":-18.46,"actual_180D_MFE_pct":88.03,"actual_180D_MAE_pct":-18.46,"score_return_alignment":"aligned"}
```

## 9. Aggregate row

```json
{
  "row_type": "aggregate",
  "selected_round": "R1",
  "selected_loop": 146,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "calibration_usable_case_count": 6,
  "calibration_usable_trigger_count": 6,
  "representative_trigger_count": 6,
  "positive_case_count": 3,
  "counterexample_count": 3,
  "stage4b_watch_or_overlay_count": 4,
  "stage4c_case_count": 0,
  "current_profile_error_count": 5,
  "new_independent_case_count": 6,
  "reused_case_count": 0,
  "new_symbol_count": 6,
  "same_archetype_new_symbol_count": 6,
  "same_archetype_new_trigger_family_count": 6,
  "coverage_before_index_baseline": 10,
  "coverage_after_if_accepted_index_baseline": 16,
  "session_aware_C02_after_loop125_134_138_146_if_accepted": "about 30 representative rows",
  "do_not_propose_new_weight_delta": false,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 10. Shadow weight row

```json
{
  "row_type": "shadow_weight",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "rule_candidate_id": "C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4",
  "proposal_type": "sector_specific_shadow_rule_candidate",
  "do_not_apply_now": true,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "proposed_rule": "For C02, Stage2-Actionable requires at least one hard commercial bridge (named order, backlog, capacity lock-up, customer/OEM forecast with line readiness, or subsidiary look-through NAV bridge) plus one conversion bridge (revenue recognition, margin/revision, shipment timing, or confirmed earnings). If MFE30 occurs with MAE90 <= -30% or evidence is theme/policy vocabulary only, attach local_4B_exit_guard and block Green.",
  "supports_positive_cases": [
    "119850",
    "199820",
    "006260"
  ],
  "blocks_or_guards_cases": [
    "388050",
    "237750",
    "060370"
  ]
}
```

## 11. Residual contribution row

```json
{
  "row_type": "residual_contribution",
  "completed_round": "R1",
  "completed_loop": 146,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 0",
  "round_schedule_status": "coverage_index_selected_not_sequential",
  "round_sector_consistency": "pass",
  "new_axis_proposed": "c02_order_capa_revenue_conversion_and_4b_exit_gate_v4",
  "existing_axis_strengthened": "price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence",
  "existing_axis_weakened": null,
  "next_recommended_archetypes": [
    "C14_EV_DEMAND_SLOWDOWN_4B_4C",
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C11_BATTERY_ORDERBOOK_RERATING",
    "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
    "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK"
  ]
}
```

## 12. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 13. Deferred Coding Agent Handoff Prompt — do not execute in this research loop

```text
You are a coding agent working on stock_agent after multiple v12 residual research MDs have been committed. Do not re-run live scans. Read this MD together with other V12 result files, ingest only rows with calibration_usable=true and complete 30/90/180D MFE/MAE, then evaluate whether C02_ORDER_CAPA_REVENUE_CONVERSION_AND_4B_EXIT_GATE_V4 should become a scoped archetype rule. Preserve global thresholds unless batch evidence supports a safe scoped patch. Apply only if duplicate keys are absent and representative rows survive validation.
```

## 14. Next research state

```text
completed_round = R1
completed_loop = 146
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C11_BATTERY_ORDERBOOK_RERATING|C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
