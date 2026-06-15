# E2R Stock-Web V12 Residual Research — R1 C03 Defense Export Framework Backlog

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 112
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: mixed_C03_defense_export_framework_backlog_contract_margin_holdout
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / quality holdout after session-adjusted Priority-0/Priority-1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
output_filename: e2r_stock_web_v12_residual_round_R1_loop_112_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

이번 실행은 일반 R1 순환이 아니라 coverage-index-first 절차로 선택했다. 정적 No-Repeat Index에는 Priority 0/1 부족 canonical이 남아 있지만, 현재 세션에서는 C02, C09, C14, C10, C06, C07, C11, C01, C28, C12 등 핵심 부족 축이 이미 여러 차례 보강되었다. 따라서 이번 파일은 C03의 단순 수량 채우기가 아니라 **방산 수출 framework / named contract / subsystem backlog / delivery-margin bridge**를 재검증하는 quality holdout pass다.

C03의 핵심 질문은 단순하다. **방산 수출 뉴스가 Stage2를 열 수는 있지만, Stage3-Yellow 이상은 named sovereign/customer export contract, framework-to-implementation conversion, backlog delivery timing, revenue recognition, margin bridge가 같이 붙을 때만 열어야 한다.** 반대로 KAI처럼 계약 자체는 크지만 매출 인식이 멀거나, 휴니드처럼 방산 capability는 있지만 named export framework가 약한 경우에는 Stage3를 닫아야 한다.

## 2. Stock-Web price-source validation

- primary_price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- stock_web_manifest_max_date: `2026-02-20`
- selected symbols: `047810, 012450, 272210, 079550, 103140, 003570, 005870`
- selected rows: all entry rows exist in tradable shards.
- 180D forward windows: available for all rows.
- corporate-action window check: no selected row has corporate-action candidate inside entry_date~D+180.

## 3. Case set summary

| role | symbol | trigger | entry | MFE180 | MAE180 | interpretation |
|---|---:|---|---|---:|---:|---|
| counterexample | 047810 한국항공우주 | 2023-05-23 | 2023-05-24 @ 53,100 | 9.2279% | -17.8908% | named_export_contract_without_near_term_delivery_margin_bridge |
| positive_with_4b_watch | 012450 한화에어로스페이스 | 2023-12-04 | 2023-12-05 @ 135,100 | 144.2635% | -9.1044% | local_overheat_after_valid_export_framework_execution |
| positive_with_4b_watch | 272210 한화시스템 | 2024-07-09 | 2024-07-10 @ 18,860 | 130.1166% | -12.3542% | export_subsystem_success_with_post_peak_drawdown |
| positive_with_high_mae_buffer | 079550 LIG넥스원 | 2024-09-20 | 2024-09-20 @ 211,000 | 208.0569% | -20.0000% | valid_framework_export_with_intermediate_MAE_buffer |
| positive_with_local_4b_watch | 103140 풍산 | 2024-03-07 | 2024-03-07 @ 46,100 | 71.1497% | -3.9046% | ammo_export_demand_repricing_with_peak_drawdown |
| missed_structural_positive | 003570 SNT다이내믹스 | 2024-09-09 | 2024-09-09 @ 20,200 | 172.2772% | -19.5050% | defense_subsystem_backlog_under_credit |
| counterexample | 005870 휴니드 | 2022-10-13 | 2022-10-13 @ 5,920 | 32.4324% | -3.3784% | defense_capability_without_named_export_framework_backlog |

### Positive / counterexample balance

```yaml
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_trigger_family_count: 7
positive_case_count: 5
counterexample_count: 2
local_4B_watch_count: 5
hard_4C_case_count: 0
current_profile_error_count: 5
avg_MFE_180D_pct: 109.6463
avg_MAE_180D_pct: -12.3053
rows_MFE_180D_above_50pct: 5
rows_MAE_180D_below_minus_15pct: 3
```

## 4. Interpretation by failure mode

### 4.1 Framework execution should score higher than generic defense capability

Hanwha Aerospace, Hanwha Systems, and LIG Nex1 show the cleanest C03 path: **named sovereign/customer export contract → executable backlog → delivery/revenue visibility → large MFE**. These should not be treated as generic defense theme rows. They deserve Stage3-Yellow and sometimes Stage3-Green treatment, but the local 4B watch must remain active when vertical MFE and post-peak drawdown become severe.

### 4.2 Subsystem backlog can be a real C03 positive

SNT Dynamics and Hanwha Systems show why C03 should not only credit prime contractors. Defense subsystem suppliers can rerate when platform-level export backlog converts into transmission, radar/MFR, electronics, ammunition, or other bottleneck subsystem revenue. The gate should require customer/platform specificity and a revenue or margin bridge; otherwise subsystem beta can become false Stage2.

### 4.3 Big export contract without near-term delivery bridge should be capped

KAI's Malaysia FA-50 final contract was real, but the 180D path was weak because delivery/revenue recognition was too far away. C03 Stage3 should not open from contract size alone. It needs a near-term delivery/margin bridge or revision confirmation.

### 4.4 Capability reports without named export framework are Stage2 watch, not Stage3

Huneed had defense communications and export-adjacent capability, but no sufficiently explicit named export framework/backlog bridge in the trigger. This is a good guardrail row: capability can open monitoring, but not Stage3 C03 rerating.

## 5. Proposed shadow rule candidate

```text
C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP
```

Rule logic:

```text
If canonical_archetype_id == C03:
  Stage2 allowed when:
    - defense export capability, program participation, or sector demand is public and dated
  Stage2-Actionable allowed when at least one of:
    - named customer / sovereign program
    - export framework agreement
    - visible platform-level backlog linkage
    - credible subsystem demand from export platform
  Stage3-Yellow allowed only when at least two are present:
    - named export or framework-to-implementation contract
    - delivery / revenue-recognition timing
    - order backlog with customer or platform specificity
    - margin or revision bridge
    - repeat/export package-sales evidence
  Stage3-Green allowed only when:
    - Stage3-Yellow conditions hold
    - revision or margin bridge is confirmed
    - red-team risk is low
  Apply local 4B overlay when:
    - MFE_90D or MFE_180D is extreme and drawdown_after_peak is severe
    - valuation/pricing is primarily price-only without new contract/margin evidence
  Block Stage3 when:
    - evidence is only generic defense capability
    - contract delivery/revenue is multi-year delayed without revision bridge
    - no named export framework, customer, platform, or margin bridge exists
```

## 6. Machine-readable rows

```jsonl
{"row_type":"price_source_validation","price_source":"Songdaiki/stock-web","source_basis":"FinanceData/marcap transformed into assistant-readable symbol-year CSV shards","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","schema_path":"atlas/schema.json","MFE_MAE_rule":"MFE/MAE computed from entry_date through 30/90/180 tradable rows using high/low relative to entry_price","corporate_action_window_policy":"block if corporate_action_candidate_dates overlap entry_date through D+180","symbols_checked":["047810","012450","272210","079550","103140","003570","005870"],"profile_corporate_action_status":"no selected row has profile corporate-action candidate inside the 180D calibration window"}
{"row_type":"case","case_id":"C03_047810_STAGE2_ACTIONABLE_2023-05-24_KAI_MALAYSIA_FA50_DELIVERY_DELAY","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AIRCRAFT_EXPORT_FINAL_CONTRACT_DELIVERY_DELAY_CAP","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","selected_round":"R1","selected_loop":112,"symbol":"047810","company_name":"한국항공우주","market":"KOSPI","case_role":"counterexample","trigger_date":"2023-05-23","entry_date":"2023-05-24","novelty_check":"new trigger family in current session; hard duplicate key avoided","exact_duplicate_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|047810|Stage2-Actionable|2023-05-24","source_urls":["https://en.yna.co.kr/view/AEN20230523006800320","https://www.koreatimes.co.kr/www/nation/2026/06/113_346007.html","https://www.edrmagazine.eu/kai-officially-signs-malaysian-fa-50-export-contract"],"thesis_summary":"Malaysia FA-50 final contract is real export evidence, but deliveries begin from 2026 and the 180D path did not validate immediate Stage3 rerating."}
{"row_type":"case","case_id":"C03_012450_STAGE3_YELLOW_2023-12-05_HANWHA_AEROSPACE_POLAND_K9_SECOND_EXECUTION","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_GROUND_DEFENSE_EXPORT_FRAMEWORK_IMPLEMENTATION_CONTRACT","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","selected_round":"R1","selected_loop":112,"symbol":"012450","company_name":"한화에어로스페이스","market":"KOSPI","case_role":"positive_with_4b_watch","trigger_date":"2023-12-04","entry_date":"2023-12-05","novelty_check":"new trigger family in current session; hard duplicate key avoided","exact_duplicate_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|Stage3-Yellow|2023-12-05","source_urls":["https://en.yna.co.kr/view/AEN20231204009400320"],"thesis_summary":"The Poland K9 follow-on implementation contract turned framework backlog into named export execution and validated C03 positive treatment, while later peak drawdown still requires local 4B watch."}
{"row_type":"case","case_id":"C03_272210_STAGE3_YELLOW_2024-07-10_HANWHA_SYSTEMS_SAUDI_CHEONGUNG_MFR","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AIR_DEFENSE_MFR_EXPORT_SUBSYSTEM_CONTRACT","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","selected_round":"R1","selected_loop":112,"symbol":"272210","company_name":"한화시스템","market":"KOSPI","case_role":"positive_with_4b_watch","trigger_date":"2024-07-09","entry_date":"2024-07-10","novelty_check":"new trigger family in current session; hard duplicate key avoided","exact_duplicate_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|272210|Stage3-Yellow|2024-07-10","source_urls":["https://en.yna.co.kr/view/AEN20240709006700320","https://eng.hanwhasystems.com/en/mediaCenter/newsView.do?seq=3187"],"thesis_summary":"Saudi Cheongung-II MFR supply converted subsystem capability into named export backlog; price path strongly validated Stage3-Yellow, but post-peak drawdown confirms local 4B overlay."}
{"row_type":"case","case_id":"C03_079550_STAGE3_YELLOW_2024-09-20_LIG_NEX1_IRAQ_CHEONGUNG_II","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AIR_DEFENSE_EXPORT_CONTRACT_BACKLOG","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","selected_round":"R1","selected_loop":112,"symbol":"079550","company_name":"LIG넥스원","market":"KOSPI","case_role":"positive_with_high_mae_buffer","trigger_date":"2024-09-20","entry_date":"2024-09-20","novelty_check":"new trigger family in current session; hard duplicate key avoided","exact_duplicate_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|079550|Stage3-Yellow|2024-09-20","source_urls":["https://en.yna.co.kr/view/AEN20240920005300320"],"thesis_summary":"Iraq Cheongung-II contract created named large export backlog and validated C03 Stage3-Yellow despite intermediate drawdown; hard 4B would have been too early."}
{"row_type":"case","case_id":"C03_103140_STAGE2_ACTIONABLE_2024-03-07_POONGSAN_AMMO_EXPORT_DEMAND","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AMMUNITION_EXPORT_DEMAND_BACKLOG_MARGIN_BRIDGE","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","selected_round":"R1","selected_loop":112,"symbol":"103140","company_name":"풍산","market":"KOSPI","case_role":"positive_with_local_4b_watch","trigger_date":"2024-03-07","entry_date":"2024-03-07","novelty_check":"new trigger family in current session; hard duplicate key avoided","exact_duplicate_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|103140|Stage2-Actionable|2024-03-07","source_urls":["https://ssl.pstatic.net/imgstock/upload/research/company/1709778599516.pdf"],"thesis_summary":"Ammunition export demand and package-sales linkage to Korean ground-defense exports validated C03-like rerating, but the drawdown after the May 2024 peak requires local 4B protection."}
{"row_type":"case","case_id":"C03_003570_STAGE2_ACTIONABLE_2024-09-09_SNT_DYNAMICS_TRANSMISSION_BACKLOG","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_DEFENSE_SUBSYSTEM_TRANSMISSION_EXPORT_BACKLOG","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","selected_round":"R1","selected_loop":112,"symbol":"003570","company_name":"SNT다이내믹스","market":"KOSPI","case_role":"missed_structural_positive","trigger_date":"2024-09-09","entry_date":"2024-09-09","novelty_check":"new trigger family in current session; hard duplicate key avoided","exact_duplicate_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|003570|Stage2-Actionable|2024-09-09","source_urls":["https://www.hanaw.com/download/research/FileServer/WEB/industry/company/2024/09/09/SNTDynamics_240909.pdf"],"thesis_summary":"Subsystem transmission exposure to K9/K10/Cheonma/Biho platforms can be a valid C03 backlog bridge; the 180D path indicates the current profile may under-credit subsystem backlog when not a prime export contractor."}
{"row_type":"case","case_id":"C03_005870_STAGE2_2022-10-13_HUNEED_DEFENSE_COMMUNICATION_EXPORT_CAPABILITY","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_DEFENSE_COMMUNICATION_CAPABILITY_NOT_EXPORT_FRAMEWORK","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","selected_round":"R1","selected_loop":112,"symbol":"005870","company_name":"휴니드","market":"KOSPI","case_role":"counterexample","trigger_date":"2022-10-13","entry_date":"2022-10-13","novelty_check":"new trigger family in current session; hard duplicate key avoided","exact_duplicate_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|005870|Stage2|2022-10-13","source_urls":["https://ssl.pstatic.net/imgstock/upload/research/company/1665628986482.pdf"],"thesis_summary":"Defense communication/system capability and export-adjacent avionics work can justify Stage2 watch, but absent a named export framework or backlog-to-margin bridge it should not unlock Stage3 C03."}
{"row_type":"trigger","case_id":"C03_047810_STAGE2_ACTIONABLE_2023-05-24_KAI_MALAYSIA_FA50_DELIVERY_DELAY","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AIRCRAFT_EXPORT_FINAL_CONTRACT_DELIVERY_DELAY_CAP","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","round":"R1","loop":112,"symbol":"047810","company_name":"한국항공우주","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-23","entry_date":"2023-05-24","entry_price":53100.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047810/2023.csv","forward_price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/047/047810/2023.csv","atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv"],"MFE_30D_pct":9.2279,"MAE_30D_pct":-4.7081,"MFE_90D_pct":9.2279,"MAE_90D_pct":-13.1827,"MFE_180D_pct":9.2279,"MAE_180D_pct":-17.8908,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_180D_date":"2023-06-19","peak_price_180D":58000.0,"drawdown_after_peak_180D_pct":-24.8276,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"stage2_evidence":"Malaysia FA-50 final contract / 18 aircraft / about USD 920M, but delivery schedule and revenue recognition were too delayed for immediate Stage3.","stage3_evidence":"not enough; delivery/revenue/margin bridge delayed or absent","stage4b_evidence":"local 4B watch if MFE is fast or drawdown_after_peak is below -20pct","stage4c_evidence":"none; no confirmed export cancellation or thesis break in selected window","price_source_validation":"actual Stock-Web tradable shard used; entry row present; >=180 forward tradable rows available","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative":true,"dedupe_for_aggregate":true,"calibration_block_reasons":[],"case_role":"counterexample","failure_mode":"named_export_contract_without_near_term_delivery_margin_bridge","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","case_id":"C03_012450_STAGE3_YELLOW_2023-12-05_HANWHA_AEROSPACE_POLAND_K9_SECOND_EXECUTION","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_GROUND_DEFENSE_EXPORT_FRAMEWORK_IMPLEMENTATION_CONTRACT","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","round":"R1","loop":112,"symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage3-Yellow","trigger_date":"2023-12-04","entry_date":"2023-12-05","entry_price":135100.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","forward_price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv"],"MFE_30D_pct":10.6588,"MAE_30D_pct":-9.1044,"MFE_90D_pct":81.3472,"MAE_90D_pct":-9.1044,"MFE_180D_pct":144.2635,"MAE_180D_pct":-9.1044,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_180D_date":"2024-07-30","peak_price_180D":330000.0,"drawdown_after_peak_180D_pct":-25.1515,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"stage2_evidence":"Poland K9 second export / implementation contract following large K9-K239 framework; named contract converted prior framework into executable backlog.","stage3_evidence":"named export/framework/backlog plus delivery/revenue/margin bridge present","stage4b_evidence":"local 4B watch if MFE is fast or drawdown_after_peak is below -20pct","stage4c_evidence":"none; no confirmed export cancellation or thesis break in selected window","price_source_validation":"actual Stock-Web tradable shard used; entry row present; >=180 forward tradable rows available","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative":true,"dedupe_for_aggregate":true,"calibration_block_reasons":[],"case_role":"positive_with_4b_watch","failure_mode":"local_overheat_after_valid_export_framework_execution","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","case_id":"C03_272210_STAGE3_YELLOW_2024-07-10_HANWHA_SYSTEMS_SAUDI_CHEONGUNG_MFR","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AIR_DEFENSE_MFR_EXPORT_SUBSYSTEM_CONTRACT","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","round":"R1","loop":112,"symbol":"272210","company_name":"한화시스템","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-09","entry_date":"2024-07-10","entry_price":18860.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv","forward_price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv","atlas/ohlcv_tradable_by_symbol_year/272/272210/2025.csv"],"MFE_30D_pct":24.0721,"MAE_30D_pct":-9.3849,"MFE_90D_pct":60.1273,"MAE_90D_pct":-12.3542,"MFE_180D_pct":130.1166,"MAE_180D_pct":-12.3542,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_180D_date":"2025-03-19","peak_price_180D":43400.0,"drawdown_after_peak_180D_pct":-30.6452,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"stage2_evidence":"Saudi Cheongung-II MFR supply contract; repeat trillion-won export route after UAE; subsystem supplier exposure rather than prime missile export only.","stage3_evidence":"named export/framework/backlog plus delivery/revenue/margin bridge present","stage4b_evidence":"local 4B watch if MFE is fast or drawdown_after_peak is below -20pct","stage4c_evidence":"none; no confirmed export cancellation or thesis break in selected window","price_source_validation":"actual Stock-Web tradable shard used; entry row present; >=180 forward tradable rows available","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative":true,"dedupe_for_aggregate":true,"calibration_block_reasons":[],"case_role":"positive_with_4b_watch","failure_mode":"export_subsystem_success_with_post_peak_drawdown","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","case_id":"C03_079550_STAGE3_YELLOW_2024-09-20_LIG_NEX1_IRAQ_CHEONGUNG_II","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AIR_DEFENSE_EXPORT_CONTRACT_BACKLOG","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","round":"R1","loop":112,"symbol":"079550","company_name":"LIG넥스원","trigger_type":"Stage3-Yellow","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":211000.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","forward_price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","atlas/ohlcv_tradable_by_symbol_year/079/079550/2025.csv"],"MFE_30D_pct":27.7251,"MAE_30D_pct":-1.4218,"MFE_90D_pct":28.673,"MAE_90D_pct":-20.0,"MFE_180D_pct":208.0569,"MAE_180D_pct":-20.0,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_180D_date":"2025-06-23","peak_price_180D":650000.0,"drawdown_after_peak_180D_pct":-4.3077,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"stage2_evidence":"Iraq Cheongung-II export contract worth about KRW 3.7T; named sovereign customer and major air-defense export framework execution.","stage3_evidence":"named export/framework/backlog plus delivery/revenue/margin bridge present","stage4b_evidence":"local 4B watch if MFE is fast or drawdown_after_peak is below -20pct","stage4c_evidence":"none; no confirmed export cancellation or thesis break in selected window","price_source_validation":"actual Stock-Web tradable shard used; entry row present; >=180 forward tradable rows available","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative":true,"dedupe_for_aggregate":true,"calibration_block_reasons":[],"case_role":"positive_with_high_mae_buffer","failure_mode":"valid_framework_export_with_intermediate_MAE_buffer","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","case_id":"C03_103140_STAGE2_ACTIONABLE_2024-03-07_POONGSAN_AMMO_EXPORT_DEMAND","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AMMUNITION_EXPORT_DEMAND_BACKLOG_MARGIN_BRIDGE","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","round":"R1","loop":112,"symbol":"103140","company_name":"풍산","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":46100.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","forward_price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","atlas/ohlcv_tradable_by_symbol_year/103/103140/2025.csv"],"MFE_30D_pct":46.4208,"MAE_30D_pct":-3.9046,"MFE_90D_pct":71.1497,"MAE_90D_pct":-3.9046,"MFE_180D_pct":71.1497,"MAE_180D_pct":-3.9046,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_180D_date":"2024-05-14","peak_price_180D":78900.0,"drawdown_after_peak_180D_pct":-40.4309,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"stage2_evidence":"Defense sales split domestic/export ammo; Europe ammo demand and package sales linked to Korean ground-defense exports; 2024 defense growth expected.","stage3_evidence":"named export/framework/backlog plus delivery/revenue/margin bridge present","stage4b_evidence":"local 4B watch if MFE is fast or drawdown_after_peak is below -20pct","stage4c_evidence":"none; no confirmed export cancellation or thesis break in selected window","price_source_validation":"actual Stock-Web tradable shard used; entry row present; >=180 forward tradable rows available","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative":true,"dedupe_for_aggregate":true,"calibration_block_reasons":[],"case_role":"positive_with_local_4b_watch","failure_mode":"ammo_export_demand_repricing_with_peak_drawdown","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","case_id":"C03_003570_STAGE2_ACTIONABLE_2024-09-09_SNT_DYNAMICS_TRANSMISSION_BACKLOG","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_DEFENSE_SUBSYSTEM_TRANSMISSION_EXPORT_BACKLOG","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","round":"R1","loop":112,"symbol":"003570","company_name":"SNT다이내믹스","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-09","entry_date":"2024-09-09","entry_price":20200.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv","forward_price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv","atlas/ohlcv_tradable_by_symbol_year/003/003570/2025.csv"],"MFE_30D_pct":39.604,"MAE_30D_pct":-4.2079,"MFE_90D_pct":39.604,"MAE_90D_pct":-19.505,"MFE_180D_pct":172.2772,"MAE_180D_pct":-19.505,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_180D_date":"2025-06-13","peak_price_180D":55000.0,"drawdown_after_peak_180D_pct":-8.9091,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"stage2_evidence":"Defense transmission specialist with platform exposure and transport-equipment revenue mix; subsystem backlog route rather than prime export announcement.","stage3_evidence":"named export/framework/backlog plus delivery/revenue/margin bridge present","stage4b_evidence":"local 4B watch if MFE is fast or drawdown_after_peak is below -20pct","stage4c_evidence":"none; no confirmed export cancellation or thesis break in selected window","price_source_validation":"actual Stock-Web tradable shard used; entry row present; >=180 forward tradable rows available","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative":true,"dedupe_for_aggregate":true,"calibration_block_reasons":[],"case_role":"missed_structural_positive","failure_mode":"defense_subsystem_backlog_under_credit","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","case_id":"C03_005870_STAGE2_2022-10-13_HUNEED_DEFENSE_COMMUNICATION_EXPORT_CAPABILITY","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_DEFENSE_COMMUNICATION_CAPABILITY_NOT_EXPORT_FRAMEWORK","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","round":"R1","loop":112,"symbol":"005870","company_name":"휴니드","trigger_type":"Stage2","trigger_date":"2022-10-13","entry_date":"2022-10-13","entry_price":5920.0,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005870/2022.csv","forward_price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/005/005870/2022.csv","atlas/ohlcv_tradable_by_symbol_year/005/005870/2023.csv"],"MFE_30D_pct":16.723,"MAE_30D_pct":2.3649,"MFE_90D_pct":16.723,"MAE_90D_pct":-3.0405,"MFE_180D_pct":32.4324,"MAE_180D_pct":-3.3784,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_180D_date":"2023-04-20","peak_price_180D":7840.0,"drawdown_after_peak_180D_pct":-24.1071,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"stage2_evidence":"Military tactical communication/system/IFF and avionics/wiring harness capability, but not a named sovereign export framework or clear backlog margin bridge.","stage3_evidence":"not enough; delivery/revenue/margin bridge delayed or absent","stage4b_evidence":"local 4B watch if MFE is fast or drawdown_after_peak is below -20pct","stage4c_evidence":"none; no confirmed export cancellation or thesis break in selected window","price_source_validation":"actual Stock-Web tradable shard used; entry row present; >=180 forward tradable rows available","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative":true,"dedupe_for_aggregate":true,"calibration_block_reasons":[],"case_role":"counterexample","failure_mode":"defense_capability_without_named_export_framework_backlog","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","case_id":"C03_047810_STAGE2_ACTIONABLE_2023-05-24_KAI_MALAYSIA_FA50_DELIVERY_DELAY","symbol":"047810","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","current_profile_proxy":"e2r_2_2_rolling_calibrated","shadow_rule_candidate":"C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP","stage_before_shadow":"Stage3-Yellow","stage_after_shadow":"Stage2-Actionable","total_score_before_shadow":76.0,"total_score_after_shadow":68.0,"raw_component_scores_before":{"eps_fcf_explosion":4.0,"earnings_visibility":6.5,"bottleneck_pricing":6.5,"market_mispricing":7.0,"valuation_rerating":6.5,"capital_allocation":4.0,"information_confidence":8.0},"raw_component_scores_after":{"eps_fcf_explosion":3.0,"earnings_visibility":4.5,"bottleneck_pricing":6.0,"market_mispricing":6.5,"valuation_rerating":5.0,"capital_allocation":4.0,"information_confidence":8.0},"residual_error":"current profile can over-credit signed aircraft export when delivery/revenue bridge is multi-year delayed","suggested_action":"cap at Stage2-Actionable until delivery schedule and margin/revenue recognition bridge are near-term"}
{"row_type":"score_simulation","case_id":"C03_012450_STAGE3_YELLOW_2023-12-05_HANWHA_AEROSPACE_POLAND_K9_SECOND_EXECUTION","symbol":"012450","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","current_profile_proxy":"e2r_2_2_rolling_calibrated","shadow_rule_candidate":"C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP","stage_before_shadow":"Stage3-Yellow","stage_after_shadow":"Stage3-Green_with_local_4B_watch","total_score_before_shadow":83.0,"total_score_after_shadow":88.0,"raw_component_scores_before":{"eps_fcf_explosion":7.5,"earnings_visibility":8.0,"bottleneck_pricing":8.0,"market_mispricing":7.0,"valuation_rerating":7.0,"capital_allocation":5.5,"information_confidence":8.5},"raw_component_scores_after":{"eps_fcf_explosion":8.0,"earnings_visibility":9.0,"bottleneck_pricing":8.5,"market_mispricing":7.0,"valuation_rerating":7.5,"capital_allocation":5.5,"information_confidence":9.0},"residual_error":"positive scoring works but local 4B overlay should activate after vertical MFE and peak drawdown risk","suggested_action":"allow Stage3-Green only with export execution plus margin bridge; overlay local 4B if MFE180 is extreme"}
{"row_type":"score_simulation","case_id":"C03_272210_STAGE3_YELLOW_2024-07-10_HANWHA_SYSTEMS_SAUDI_CHEONGUNG_MFR","symbol":"272210","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","current_profile_proxy":"e2r_2_2_rolling_calibrated","shadow_rule_candidate":"C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP","stage_before_shadow":"Stage3-Yellow","stage_after_shadow":"Stage3-Green_with_local_4B_watch","total_score_before_shadow":80.0,"total_score_after_shadow":86.0,"raw_component_scores_before":{"eps_fcf_explosion":6.5,"earnings_visibility":7.5,"bottleneck_pricing":8.0,"market_mispricing":7.0,"valuation_rerating":7.5,"capital_allocation":4.5,"information_confidence":8.5},"raw_component_scores_after":{"eps_fcf_explosion":7.5,"earnings_visibility":8.5,"bottleneck_pricing":8.5,"market_mispricing":7.0,"valuation_rerating":8.0,"capital_allocation":4.5,"information_confidence":9.0},"residual_error":"subsystem exports can be under-recognized if C03 requires prime-system backlog only","suggested_action":"credit named export subsystem contracts when customer/framework and revenue conversion are visible; add 4B watch after large MFE"}
{"row_type":"score_simulation","case_id":"C03_079550_STAGE3_YELLOW_2024-09-20_LIG_NEX1_IRAQ_CHEONGUNG_II","symbol":"079550","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","current_profile_proxy":"e2r_2_2_rolling_calibrated","shadow_rule_candidate":"C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP","stage_before_shadow":"Stage3-Yellow","stage_after_shadow":"Stage3-Green_with_high_MAE_buffer","total_score_before_shadow":84.0,"total_score_after_shadow":89.0,"raw_component_scores_before":{"eps_fcf_explosion":7.5,"earnings_visibility":8.5,"bottleneck_pricing":8.5,"market_mispricing":7.0,"valuation_rerating":7.5,"capital_allocation":4.5,"information_confidence":9.0},"raw_component_scores_after":{"eps_fcf_explosion":8.5,"earnings_visibility":9.0,"bottleneck_pricing":9.0,"market_mispricing":7.0,"valuation_rerating":8.0,"capital_allocation":4.5,"information_confidence":9.0},"residual_error":"high-MAE guard must not overkill a valid named sovereign export contract","suggested_action":"buffer 4B when contract/backlog quality is very strong and thesis is intact"}
{"row_type":"score_simulation","case_id":"C03_103140_STAGE2_ACTIONABLE_2024-03-07_POONGSAN_AMMO_EXPORT_DEMAND","symbol":"103140","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","current_profile_proxy":"e2r_2_2_rolling_calibrated","shadow_rule_candidate":"C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP","stage_before_shadow":"Stage2-Actionable","stage_after_shadow":"Stage3-Yellow_with_local_4B_watch","total_score_before_shadow":74.0,"total_score_after_shadow":80.0,"raw_component_scores_before":{"eps_fcf_explosion":6.5,"earnings_visibility":7.0,"bottleneck_pricing":7.0,"market_mispricing":6.5,"valuation_rerating":6.5,"capital_allocation":4.0,"information_confidence":7.0},"raw_component_scores_after":{"eps_fcf_explosion":7.5,"earnings_visibility":8.0,"bottleneck_pricing":8.0,"market_mispricing":6.5,"valuation_rerating":7.0,"capital_allocation":4.0,"information_confidence":7.5},"residual_error":"ammo export demand can be missed if C03 only credits prime system contracts; but price-only blowoff must be capped","suggested_action":"allow ammo export demand as C03 Stage2/Yellow when recurring export/margin evidence exists; local 4B after fast rerating"}
{"row_type":"score_simulation","case_id":"C03_003570_STAGE2_ACTIONABLE_2024-09-09_SNT_DYNAMICS_TRANSMISSION_BACKLOG","symbol":"003570","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","current_profile_proxy":"e2r_2_2_rolling_calibrated","shadow_rule_candidate":"C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP","stage_before_shadow":"Stage2","stage_after_shadow":"Stage3-Yellow_with_MAE_buffer","total_score_before_shadow":69.0,"total_score_after_shadow":79.0,"raw_component_scores_before":{"eps_fcf_explosion":5.0,"earnings_visibility":6.0,"bottleneck_pricing":6.5,"market_mispricing":6.0,"valuation_rerating":6.0,"capital_allocation":4.0,"information_confidence":6.5},"raw_component_scores_after":{"eps_fcf_explosion":7.0,"earnings_visibility":7.5,"bottleneck_pricing":8.0,"market_mispricing":6.5,"valuation_rerating":7.0,"capital_allocation":4.0,"information_confidence":7.5},"residual_error":"subsystem backlog can be a real C03 positive but lacks a dedicated gate in current canonical treatment","suggested_action":"credit subsystem backlog if platform/customer and revenue bridge are explicit; keep MAE buffer"}
{"row_type":"score_simulation","case_id":"C03_005870_STAGE2_2022-10-13_HUNEED_DEFENSE_COMMUNICATION_EXPORT_CAPABILITY","symbol":"005870","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","current_profile_proxy":"e2r_2_2_rolling_calibrated","shadow_rule_candidate":"C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP","stage_before_shadow":"Stage2-Actionable","stage_after_shadow":"Stage2-Watch","total_score_before_shadow":66.0,"total_score_after_shadow":61.0,"raw_component_scores_before":{"eps_fcf_explosion":4.0,"earnings_visibility":5.5,"bottleneck_pricing":5.5,"market_mispricing":6.0,"valuation_rerating":6.0,"capital_allocation":3.5,"information_confidence":6.5},"raw_component_scores_after":{"eps_fcf_explosion":3.5,"earnings_visibility":4.5,"bottleneck_pricing":5.0,"market_mispricing":5.5,"valuation_rerating":5.0,"capital_allocation":3.5,"information_confidence":6.0},"residual_error":"defense capability reports can become false C03 positives if named export/backlog gate is absent","suggested_action":"block Stage3 unless named sovereign/export framework, backlog, delivery and margin bridge are present"}
{"row_type":"residual_contribution","selected_round":"R1","selected_loop":112,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","rule_candidate":"C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP","positive_case_count":5,"counterexample_count":2,"local_4B_watch_count":5,"hard_4C_count":0,"current_profile_error_count":5,"calibration_usable_rows":7,"representative_rows":7,"avg_MFE_180D_pct":109.6463,"avg_MAE_180D_pct":-12.3053,"rows_MFE_180D_above_50pct":5,"rows_MAE_180D_below_minus_15pct":3,"shadow_weight_only":true,"production_scoring_changed":false}
{"row_type":"shadow_weight","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_axis":"named_export_or_framework_backlog_delivery_margin_bridge","increase_components":["earnings_visibility","information_confidence","bottleneck_pricing"],"cap_components":["valuation_rerating","market_mispricing"],"guardrail":"local_4B_watch_guard when fast MFE or post-peak drawdown is severe","implementation_scope":"deferred_coding_agent_only","apply_now":false}
```

## 7. Source map

- `047810 한국항공우주`: https://en.yna.co.kr/view/AEN20230523006800320; https://www.koreatimes.co.kr/www/nation/2026/06/113_346007.html; https://www.edrmagazine.eu/kai-officially-signs-malaysian-fa-50-export-contract
- `012450 한화에어로스페이스`: https://en.yna.co.kr/view/AEN20231204009400320
- `272210 한화시스템`: https://en.yna.co.kr/view/AEN20240709006700320; https://eng.hanwhasystems.com/en/mediaCenter/newsView.do?seq=3187
- `079550 LIG넥스원`: https://en.yna.co.kr/view/AEN20240920005300320
- `103140 풍산`: https://ssl.pstatic.net/imgstock/upload/research/company/1709778599516.pdf
- `003570 SNT다이내믹스`: https://www.hanaw.com/download/research/FileServer/WEB/industry/company/2024/09/09/SNTDynamics_240909.pdf
- `005870 휴니드`: https://ssl.pstatic.net/imgstock/upload/research/company/1665628986482.pdf

## 8. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 7
calibration_usable_rows: 7
representative_rows: 7
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for Songdaiki/stock_agent. Do not re-run web research. Use this standalone MD as one V12 calibration research artifact.

Task:
1. Validate the filename and metadata against the V12 result filename regex.
2. Parse the machine-readable JSONL rows in section 6.
3. Validate every trigger row has entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
4. Confirm trigger_type is one of Stage2, Stage2-Actionable, Stage3-Yellow, Stage3-Green, Stage4B, Stage4C.
5. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
6. Treat this as shadow-rule evidence only; do not directly change production scoring from a single MD.
7. Candidate rule to evaluate in batch: C03_DEFENSE_EXPORT_REQUIRES_NAMED_EXPORT_OR_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_WITH_SUBSYSTEM_4B_CAP.
8. Compare against existing C03 rows, especially whether prime-contractor-only logic under-credits subsystem backlog while generic defense capability over-credits Stage3.
```

## 10. Next research state

```text
completed_round = R1
completed_loop = 112
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / quality holdout after session-adjusted Priority-0/Priority-1 fills
next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_quality_holdout | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_quality_holdout | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
