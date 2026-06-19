# E2R v12 residual research — R1 loop 147 — L1 / C03 DEFENSE_EXPORT_FRAMEWORK_BACKLOG

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 147
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C03 direct URL/proxy repair and 4C path repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE
output_filename: e2r_stock_web_v12_residual_round_R1_loop_147_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
```

## 1. Selection rationale

The current No-Repeat ledger says the cumulative v12 corpus already has every C01~C32 archetype above the old 80-row stabilization target, so this run is not a raw row-fill run. It is a quality repair run: direct URL repair, proxy reduction, complete 30/90/180D MFE/MAE rows, and 4B/4C taxonomy repair.

C03 currently has enough rows but still shows a large proxy/URL burden and only a small 4C sample relative to 4B rows. The selected question is therefore not “does K-defense export work?” The useful residual question is narrower:

> When does an export/framework defense headline become executable backlog evidence, and when is it only sector sympathy that should be capped or hard-routed to 4C?

Visible root files already include C03 loop 145 and loop 146. Therefore this run uses R1 loop 147 and avoids the current visible sequence C05 → C01 → C13 → C15 → C10 → C02 → C16 → R13 → C17 → C07 → C06 → C14 → C11 → C12 → C09. The selected C03 path is not a replay of the recent R1 C01/C02/C05 outputs: it tests defense-export framework-to-execution backlog conversion and 4C proxy-failure timing.

## 2. Price atlas / validation basis

- price atlas: `Songdaiki/stock-web`
- upstream: `FinanceData/marcap`
- basis: `tradable_raw`, raw/unadjusted OHLC
- manifest max date: `2026-02-20`
- MFE/MAE calculation: entry close versus max high / min low over 30, 90, and 180 tradable rows from entry date.
- all seven trigger rows have complete `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, and `MAE_180D_pct`.

## 3. Novelty and duplicate-avoidance audit

```yaml
new_independent_case_count: 7
visible_top_symbol_reuse_count: 5
same_archetype_non_top_symbol_count: 2
same_archetype_new_trigger_family_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 4
counterexample_count: 3
stage4b_case_count: 0
stage4c_case_count: 2
source_proxy_only_count: 2
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 3
reused_case_count: 0
```

C03’s visible top symbols already include several major defense exporters, so this run does **not** claim all symbols are new to the full corpus. The novelty claim is case-level and trigger-family-level: Redback Australia execution contract, Saudi MFR component export, Iraq Cheongung prime export, Malaysia FA-50 final contract lag, Altay transmission component export, Victek geopolitical proxy, and Firstec Poland-framework proxy are treated as separate evidence families.

## 4. Case table

| case_id | symbol | name | trigger_type | trigger_date | entry_date | entry_close | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | outcome | source_proxy_only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C03-R1L147-001 | 012450 | Hanwha Aerospace | Stage3-Yellow | 2023-12-08 | 2023-12-11 | 128700.00 | 90.37 | -4.58 | 165.35 | -4.58 | positive_structural_rerating | False |
| C03-R1L147-002 | 272210 | Hanwha Systems | Stage3-Yellow | 2024-07-09 | 2024-07-10 | 18860.00 | 60.13 | -12.35 | 130.12 | -12.35 | positive_component_backlog_rerating | False |
| C03-R1L147-003 | 079550 | LIG Nex1 | Stage3-Yellow | 2024-09-20 | 2024-09-20 | 211000.00 | 28.67 | -20.00 | 194.31 | -20.00 | positive_prime_export_rerating_with_drawdown | False |
| C03-R1L147-004 | 047810 | Korea Aerospace Industries | Stage2-Actionable | 2023-05-23 | 2023-05-24 | 53100.00 | 9.23 | -13.18 | 9.23 | -17.89 | direct_contract_but_no_forward_rerating | False |
| C03-R1L147-005 | 003570 | SNT Dynamics | Stage2-Actionable | 2023-02-05 | 2023-02-06 | 10370.00 | 5.69 | -20.83 | 42.14 | -20.83 | positive_but_high_mae_component_contract | False |
| C03-R1L147-006 | 065450 | Victek | Stage4C | 2022-02-24 | 2022-02-24 | 8000.00 | 1.88 | -40.50 | 1.88 | -42.62 | proxy_false_positive_hard_4c | True |
| C03-R1L147-007 | 010820 | Firstec | Stage4C | 2022-07-28 | 2022-07-29 | 3740.00 | 17.91 | -30.35 | 17.91 | -30.35 | framework_proxy_false_positive_hard_4c | True |


## 5. Evidence URL table

| case_id | symbol | evidence_family | primary_url | secondary_url |
| --- | --- | --- | --- | --- |
| C03-R1L147-001 | 012450 | SIGNED_EXPORT_EXECUTION_CONTRACT_REDBACK_AUSTRALIA | https://m.hanwhaaerospace.com/eng/media/newsroom/view.do?seq=379 | https://en.yna.co.kr/view/AEN20231208001300315 |
| C03-R1L147-002 | 272210 | SIGNED_MFR_COMPONENT_EXPORT_SAUDI_CHEONGUNG | https://en.yna.co.kr/view/AEN20240709007700320 | https://www.hanwhasystems.com/en/business/defense/isr/radar01.do |
| C03-R1L147-003 | 079550 | SIGNED_PRIME_EXPORT_CONTRACT_IRAQ_CHEONGUNG | https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/ | https://en.yna.co.kr/view/AEN20240920001800320 |
| C03-R1L147-004 | 047810 | FINAL_CONTRACT_FA50_MALAYSIA_DELIVERY_LAG | https://en.yna.co.kr/view/AEN20230523008800325 | https://www.asiae.co.kr/en/article/2023052314354158390 |
| C03-R1L147-005 | 003570 | SUBCOMPONENT_EXPORT_CONTRACT_ALTAY_TRANSMISSION | https://www.theinvestor.co.kr/article/3054865 | https://www.defensenews.com/industry/2023/02/03/turkey-picks-south-korean-transmission-for-altay-tank/ |
| C03-R1L147-006 | 065450 | GEOPOLITICAL_DEFENSE_PROXY_NO_EXPORT_BACKLOG | https://www.victek.co.kr/eng/01_com/company.html | https://www.victek.co.kr/eng/03_pro/pro_1_4.html |
| C03-R1L147-007 | 010820 | POLAND_FRAMEWORK_SECTOR_SYMPATHY_NO_DIRECT_CONTRACT | https://www.reuters.com/world/with-massive-polish-arms-deal-skorea-steps-closer-ukraine-war-2022-07-28/ | https://eng.firsteccom.co.kr/area/area_01 |


## 6. Stock-Web actual row and forward-window table

| symbol | entry_date | entry_close | peak_180D_date | peak_180D_high | trough_180D_date | trough_180D_low | close_180D_date | close_180D_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 012450 | 2023-12-11 | 128700.00 | 2024-10-04 | 341500.00 | 2023-12-26 | 122800.00 | 2024-10-04 | 162.24 |
| 272210 | 2024-07-10 | 18860.00 | 2025-03-19 | 43400.00 | 2024-09-09 | 16530.00 | 2025-04-08 | 71.26 |
| 079550 | 2024-09-20 | 211000.00 | 2025-06-20 | 621000.00 | 2024-12-10 | 168800.00 | 2025-06-20 | 188.63 |
| 047810 | 2023-05-24 | 53100.00 | 2023-06-19 | 58000.00 | 2023-10-31 | 43600.00 | 2024-02-16 | -3.39 |
| 003570 | 2023-02-06 | 10370.00 | 2023-10-24 | 14740.00 | 2023-03-24 | 8210.00 | 2023-10-30 | 35.00 |
| 065450 | 2022-02-24 | 8000.00 | 2022-02-24 | 8150.00 | 2022-09-28 | 4590.00 | 2022-11-16 | -25.00 |
| 010820 | 2022-07-29 | 3740.00 | 2022-08-02 | 4410.00 | 2022-10-13 | 2605.00 | 2023-04-19 | -0.27 |


## 7. Profile / corporate-action contamination check

| symbol | profile_path | profile_check | calibration_usable |
| --- | --- | --- | --- |
| 012450 | atlas/symbol_profiles/012/012450.json | corporate_action_candidate_count=5; dates=[1996-01-03,1997-01-03,1999-04-08,1999-07-06,2009-02-20]; no overlap with 2023-12-11~2024-10-04 180D window. | true |
| 272210 | atlas/symbol_profiles/272/272210.json | corporate_action_candidate_count=1; dates=[2021-06-23]; no overlap with 2024-07-10~2025-03-19 180D window. | true |
| 079550 | atlas/symbol_profiles/079/079550.json | corporate_action_candidate_count=0; no overlap. | true |
| 047810 | atlas/symbol_profiles/047/047810.json | corporate_action_candidate_count=0; no overlap. | true |
| 003570 | atlas/symbol_profiles/003/003570.json | corporate_action_candidate_count=5; dates=[1998-12-22,2000-04-28,2000-07-03,2003-03-31,2006-04-05]; no overlap with 2023 window. | true |
| 065450 | atlas/symbol_profiles/065/065450.json | corporate_action_candidate_count=3; dates=[2004-10-28,2008-08-25,2009-11-24]; no overlap with 2022 window. | true |
| 010820 | atlas/symbol_profiles/010/010820.json | corporate_action_candidate_count=4; dates=[1999-11-05,2002-02-19,2003-07-16,2006-12-22]; no overlap with 2022-2023 window. | true |


All 180D forward windows are inside the Stock-Web manifest max date. No selected trigger has a corporate-action candidate date overlapping its entry date through 180-tradable-row calibration window.

## 8. Raw component score simulation

C03 runtime weights in the No-Repeat summary are `EPS/Vis/Bott/Mis/Val/Cap/Info = 20/24/17/14/14/6/5`. The table below is a shadow simulation, not a production patch.

| case_id | symbol | trigger_type | total | EPS/FCF | Vis | Bott | Mis | Val | Cap | Info | decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C03-R1L147-001 | 012450 | Stage3-Yellow | 85 | 16 | 23 | 16 | 10 | 11 | 4 | 5 | Direct signed export contract plus named end customer/product gives enough visibility for Yellow, but Green still needs delivery/margin/revision bridge. |
| C03-R1L147-002 | 272210 | Stage3-Yellow | 76 | 13 | 22 | 15 | 9 | 9 | 3 | 5 | Component supplier is not the prime contractor, but named radar contract and product role convert framework into executable backlog evidence. |
| C03-R1L147-003 | 079550 | Stage3-Yellow | 84 | 16 | 24 | 15 | 10 | 10 | 4 | 5 | Prime export and backlog quality support Yellow; confidentiality and MAE argue against automatic Green at trigger. |
| C03-R1L147-004 | 047810 | Stage2-Actionable | 68 | 11 | 19 | 12 | 9 | 8 | 4 | 5 | Direct signed contract deserves Stage2-Actionable, but not Yellow without incremental revision/margin bridge after prior LOA. |
| C03-R1L147-005 | 003570 | Stage2-Actionable | 66 | 10 | 20 | 10 | 8 | 8 | 5 | 5 | Good for Stage2-Actionable, not Yellow/Green, because subcomponent economics and margin/revision visibility are thin. |
| C03-R1L147-006 | 065450 | Stage4C | 31 | 3 | 6 | 4 | 8 | 4 | 1 | 5 | C03 requires export framework/backlog, not only defense theme exposure; large MAE confirms 4C/proxy block. |
| C03-R1L147-007 | 010820 | Stage4C | 39 | 4 | 8 | 6 | 9 | 5 | 2 | 5 | Framework agreement at national level is not symbol-level backlog. Treat as 4C unless direct executable contract appears. |


## 9. Trigger JSONL

```jsonl
{"row_type":"trigger","case_id":"C03-R1L147-001","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE","symbol":"012450","name":"Hanwha Aerospace","trigger_type":"Stage3-Yellow","trigger_date":"2023-12-08","entry_date":"2023-12-11","entry_price":128700.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.16,"MFE_90D_pct":90.37,"MFE_180D_pct":165.35,"MAE_30D_pct":-4.58,"MAE_90D_pct":-4.58,"MAE_180D_pct":-4.58,"peak_180D_date":"2024-10-04","peak_180D_high":341500.0,"trough_180D_date":"2023-12-26","trough_180D_low":122800.0,"close_180D_date":"2024-10-04","close_180D_return_pct":162.24,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"source_proxy_only":false,"evidence_url_pending":false,"is_positive_case":true,"is_counterexample":false,"current_profile_error":false,"evidence_family":"SIGNED_EXPORT_EXECUTION_CONTRACT_REDBACK_AUSTRALIA","same_entry_group_id":"C03-R1L147-001","representative_for_aggregate":true,"do_not_count_as_new_case":false,"component_scores":{"eps_fcf_explosion":16,"earnings_visibility":23,"bottleneck_pricing":16,"market_mispricing":10,"valuation_rerating":11,"capital_allocation":4,"information_confidence":5},"component_total_score":85,"primary_evidence_url":"https://m.hanwhaaerospace.com/eng/media/newsroom/view.do?seq=379","secondary_evidence_url":"https://en.yna.co.kr/view/AEN20231208001300315"}
{"row_type":"trigger","case_id":"C03-R1L147-002","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE","symbol":"272210","name":"Hanwha Systems","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-09","entry_date":"2024-07-10","entry_price":18860.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":24.07,"MFE_90D_pct":60.13,"MFE_180D_pct":130.12,"MAE_30D_pct":-9.38,"MAE_90D_pct":-12.35,"MAE_180D_pct":-12.35,"peak_180D_date":"2025-03-19","peak_180D_high":43400.0,"trough_180D_date":"2024-09-09","trough_180D_low":16530.0,"close_180D_date":"2025-04-08","close_180D_return_pct":71.26,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"source_proxy_only":false,"evidence_url_pending":false,"is_positive_case":true,"is_counterexample":false,"current_profile_error":false,"evidence_family":"SIGNED_MFR_COMPONENT_EXPORT_SAUDI_CHEONGUNG","same_entry_group_id":"C03-R1L147-002","representative_for_aggregate":true,"do_not_count_as_new_case":false,"component_scores":{"eps_fcf_explosion":13,"earnings_visibility":22,"bottleneck_pricing":15,"market_mispricing":9,"valuation_rerating":9,"capital_allocation":3,"information_confidence":5},"component_total_score":76,"primary_evidence_url":"https://en.yna.co.kr/view/AEN20240709007700320","secondary_evidence_url":"https://www.hanwhasystems.com/en/business/defense/isr/radar01.do"}
{"row_type":"trigger","case_id":"C03-R1L147-003","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE","symbol":"079550","name":"LIG Nex1","trigger_type":"Stage3-Yellow","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":211000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":25.59,"MFE_90D_pct":28.67,"MFE_180D_pct":194.31,"MAE_30D_pct":-1.42,"MAE_90D_pct":-20.0,"MAE_180D_pct":-20.0,"peak_180D_date":"2025-06-20","peak_180D_high":621000.0,"trough_180D_date":"2024-12-10","trough_180D_low":168800.0,"close_180D_date":"2025-06-20","close_180D_return_pct":188.63,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"source_proxy_only":false,"evidence_url_pending":false,"is_positive_case":true,"is_counterexample":false,"current_profile_error":false,"evidence_family":"SIGNED_PRIME_EXPORT_CONTRACT_IRAQ_CHEONGUNG","same_entry_group_id":"C03-R1L147-003","representative_for_aggregate":true,"do_not_count_as_new_case":false,"component_scores":{"eps_fcf_explosion":16,"earnings_visibility":24,"bottleneck_pricing":15,"market_mispricing":10,"valuation_rerating":10,"capital_allocation":4,"information_confidence":5},"component_total_score":84,"primary_evidence_url":"https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/","secondary_evidence_url":"https://en.yna.co.kr/view/AEN20240920001800320"}
{"row_type":"trigger","case_id":"C03-R1L147-004","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE","symbol":"047810","name":"Korea Aerospace Industries","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-23","entry_date":"2023-05-24","entry_price":53100.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.23,"MFE_90D_pct":9.23,"MFE_180D_pct":9.23,"MAE_30D_pct":-4.71,"MAE_90D_pct":-13.18,"MAE_180D_pct":-17.89,"peak_180D_date":"2023-06-19","peak_180D_high":58000.0,"trough_180D_date":"2023-10-31","trough_180D_low":43600.0,"close_180D_date":"2024-02-16","close_180D_return_pct":-3.39,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"source_proxy_only":false,"evidence_url_pending":false,"is_positive_case":false,"is_counterexample":true,"current_profile_error":true,"evidence_family":"FINAL_CONTRACT_FA50_MALAYSIA_DELIVERY_LAG","same_entry_group_id":"C03-R1L147-004","representative_for_aggregate":true,"do_not_count_as_new_case":false,"component_scores":{"eps_fcf_explosion":11,"earnings_visibility":19,"bottleneck_pricing":12,"market_mispricing":9,"valuation_rerating":8,"capital_allocation":4,"information_confidence":5},"component_total_score":68,"primary_evidence_url":"https://en.yna.co.kr/view/AEN20230523008800325","secondary_evidence_url":"https://www.asiae.co.kr/en/article/2023052314354158390"}
{"row_type":"trigger","case_id":"C03-R1L147-005","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE","symbol":"003570","name":"SNT Dynamics","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-05","entry_date":"2023-02-06","entry_price":10370.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.69,"MFE_90D_pct":5.69,"MFE_180D_pct":42.14,"MAE_30D_pct":-15.33,"MAE_90D_pct":-20.83,"MAE_180D_pct":-20.83,"peak_180D_date":"2023-10-24","peak_180D_high":14740.0,"trough_180D_date":"2023-03-24","trough_180D_low":8210.0,"close_180D_date":"2023-10-30","close_180D_return_pct":35.0,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"source_proxy_only":false,"evidence_url_pending":false,"is_positive_case":true,"is_counterexample":false,"current_profile_error":false,"evidence_family":"SUBCOMPONENT_EXPORT_CONTRACT_ALTAY_TRANSMISSION","same_entry_group_id":"C03-R1L147-005","representative_for_aggregate":true,"do_not_count_as_new_case":false,"component_scores":{"eps_fcf_explosion":10,"earnings_visibility":20,"bottleneck_pricing":10,"market_mispricing":8,"valuation_rerating":8,"capital_allocation":5,"information_confidence":5},"component_total_score":66,"primary_evidence_url":"https://www.theinvestor.co.kr/article/3054865","secondary_evidence_url":"https://www.defensenews.com/industry/2023/02/03/turkey-picks-south-korean-transmission-for-altay-tank/"}
{"row_type":"trigger","case_id":"C03-R1L147-006","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE","symbol":"065450","name":"Victek","trigger_type":"Stage4C","trigger_date":"2022-02-24","entry_date":"2022-02-24","entry_price":8000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.88,"MFE_90D_pct":1.88,"MFE_180D_pct":1.88,"MAE_30D_pct":-23.0,"MAE_90D_pct":-40.5,"MAE_180D_pct":-42.62,"peak_180D_date":"2022-02-24","peak_180D_high":8150.0,"trough_180D_date":"2022-09-28","trough_180D_low":4590.0,"close_180D_date":"2022-11-16","close_180D_return_pct":-25.0,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false,"is_positive_case":false,"is_counterexample":true,"current_profile_error":true,"evidence_family":"GEOPOLITICAL_DEFENSE_PROXY_NO_EXPORT_BACKLOG","same_entry_group_id":"C03-R1L147-006","representative_for_aggregate":true,"do_not_count_as_new_case":false,"component_scores":{"eps_fcf_explosion":3,"earnings_visibility":6,"bottleneck_pricing":4,"market_mispricing":8,"valuation_rerating":4,"capital_allocation":1,"information_confidence":5},"component_total_score":31,"primary_evidence_url":"https://www.victek.co.kr/eng/01_com/company.html","secondary_evidence_url":"https://www.victek.co.kr/eng/03_pro/pro_1_4.html"}
{"row_type":"trigger","case_id":"C03-R1L147-007","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE","symbol":"010820","name":"Firstec","trigger_type":"Stage4C","trigger_date":"2022-07-28","entry_date":"2022-07-29","entry_price":3740.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.91,"MFE_90D_pct":17.91,"MFE_180D_pct":17.91,"MAE_30D_pct":-8.82,"MAE_90D_pct":-30.35,"MAE_180D_pct":-30.35,"peak_180D_date":"2022-08-02","peak_180D_high":4410.0,"trough_180D_date":"2022-10-13","trough_180D_low":2605.0,"close_180D_date":"2023-04-19","close_180D_return_pct":-0.27,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false,"is_positive_case":false,"is_counterexample":true,"current_profile_error":true,"evidence_family":"POLAND_FRAMEWORK_SECTOR_SYMPATHY_NO_DIRECT_CONTRACT","same_entry_group_id":"C03-R1L147-007","representative_for_aggregate":true,"do_not_count_as_new_case":false,"component_scores":{"eps_fcf_explosion":4,"earnings_visibility":8,"bottleneck_pricing":6,"market_mispricing":9,"valuation_rerating":5,"capital_allocation":2,"information_confidence":5},"component_total_score":39,"primary_evidence_url":"https://www.reuters.com/world/with-massive-polish-arms-deal-skorea-steps-closer-ukraine-war-2022-07-28/","secondary_evidence_url":"https://eng.firsteccom.co.kr/area/area_01"}
```

## 10. Stage2 / Yellow / Green / 4B / 4C residual interpretation

### Positive path

C03 works when the headline has already crossed from vague export framework into executable backlog: a named foreign customer, a named weapon system or component, a signed contract or binding order, and a delivery/backlog path. Hanwha Aerospace’s Redback contract, Hanwha Systems’ Saudi MFR contract, LIG Nex1’s Iraq Cheongung-II contract, and SNT Dynamics’ Altay transmission contract all clear some form of that bridge. These are not just flags planted on a map; they are roads, cargo, and an address.

### Weak direct-contract path

KAI’s Malaysia FA-50 final contract is a useful counterexample because it is a real direct contract, yet 180D MFE was only 9.23% and MAE reached -17.89%. The reason is not that the contract is fake; the issue is that final signing after prior LOA can be already digested, and the market still needs revision, margin, delivery timing, or cash-conversion proof before Yellow/Green.

### Proxy false-positive path

Victek and Firstec show the opposite failure. Their defense exposure is real at a business-description level, and the sector events were real, but C03 is not “defense exposure.” C03 is export framework plus backlog conversion. Without a symbol-level dated contract/customer/backlog bridge, geopolitical shocks and national framework deals should be treated as watch/4C, not Stage2-Actionable.

## 11. Residual contribution summary

```yaml
residual_contribution_label: C03_export_framework_to_execution_backlog_bridge_quality_repair
new_axis_proposed: C03_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
do_not_propose_green_threshold_loosening: true
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed C03-specific shadow rule

For `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG`, do not grant Stage2-Actionable from a generic “K-defense export / geopolitical shock / national framework / sector sympathy” headline alone. Require at least two of the following before Stage2-Actionable:

1. signed execution contract or regulatory filing with amount;
2. named foreign government/customer or prime contractor;
3. named system/component with direct symbol-level role;
4. delivery period, backlog, or revenue-recognition path;
5. non-price earnings/margin/revision evidence;
6. financing or execution-risk clarity.

If only one item is present, cap at `Stage2` or narrative watch. If none are present and the price already ran, route to `Stage4C` when subsequent price path confirms high MAE or no forward MFE.

## 12. Same-entry dedupe and aggregate logic

Each trigger row has a unique `same_entry_group_id`, so aggregate counting can use all seven rows. If a later parser finds older rows with the same `canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family`, keep the older representative row and demote this row to `not_representative_for_aggregate`; otherwise, all seven are representative.

## 13. Batch-ingest self-audit

```yaml
standard_v12_filename: pass
filename_round_loop_metadata_match: pass
round_sector_consistency: pass
canonical_stage_label_only: pass
actual_stock_web_1d_ohlc_used: pass
complete_30_90_180_mfe_mae_every_trigger: pass
trigger_rows_missing_required_price_fields: 0
manifest_max_date_respected: pass
corporate_action_180D_overlap: 0
source_proxy_only_rows: 2
evidence_url_pending_rows: 0
production_scoring_changed: false
handoff_prompt_executed_now: false
```

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

When batch-applying v12 residual research, ingest this file as a standard v12 result MD. Parse all JSONL rows with row_type=trigger. Preserve production_scoring_changed=false and shadow_weight_only=true.

Candidate patch axis:
  C03_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE_GATE

Scope:
  large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG

Implementation intent:
  Add or strengthen a C03-specific bridge gate so that generic defense/geopolitical/framework headlines do not open Stage2-Actionable unless they contain at least two executable-backlog proof items: signed order amount, named foreign customer, named product/component role, delivery/backlog path, non-price revision/margin evidence, or financing/execution clarity.

Expected behavior:
  - Direct prime export contract with named customer/system can reach Stage3-Yellow if visibility is strong.
  - Direct component contract can reach Stage2-Actionable and sometimes Yellow when component role and amount are explicit.
  - Prior-LOA/final-contract lag without fresh revision/margin bridge remains Stage2-Actionable or lower.
  - Sector sympathy/proxy names without direct contract/backlog route to Stage4C if high MAE/no MFE confirms failure.

Do not loosen Stage3-Green threshold.
Do not change global production profile from a single MD.
```

## 15. Final state

```yaml
completed: true
selected_round: R1
selected_loop: 147
selected_priority_bucket: Priority 0/1 quality repair — C03 direct URL/proxy repair and 4C path repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTION_BACKLOG_BRIDGE
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
