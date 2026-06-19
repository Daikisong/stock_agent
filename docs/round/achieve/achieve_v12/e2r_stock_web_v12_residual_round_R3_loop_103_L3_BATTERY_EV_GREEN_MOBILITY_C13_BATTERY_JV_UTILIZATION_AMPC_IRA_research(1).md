# E2R Stock-Web v12 Residual Research — R3 / C13 JV Utilization AMPC IRA

```yaml
schema_version: e2r_stock_web_v12_residual_research
created_at: 2026-06-15
selected_round: R3
selected_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair after C05 and C01 were used in the immediately preceding conversation runs
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: NORTH_AMERICA_JV_AMPC_UTILIZATION_BRIDGE
output_filename: e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row: true
```

## 1. Selection rationale / no-repeat gate

The main execution prompt requires a coverage-index-first scheduler, not a mechanical R1→R13 cycle. The selected canonical drives both round and large-sector metadata. C13 maps to `R3 / L3_BATTERY_EV_GREEN_MOBILITY`. The prompt also requires standard v12 filename format, complete 30D/90D/180D MFE/MAE in every trigger row, canonical stage labels as `trigger_type`, no production scoring change, and a shadow-only rule candidate.

The latest no-repeat ledger is no longer a simple row-count shortage list. All C01~C32 scopes are above 80 representative rows, so this run uses quality/balance repair rather than raw coverage fill. The ledger shows C13 with 189 representative rows, 38 symbols, 24 positive and 43 counterexample rows, 32/19 4B/4C rows, and heavy prior symbol concentration around `373220`, `006400`, `096770`, `051910`, `011790`, and `066970`. Because the immediately preceding generated files in this session used C05 and C01, this run selects C13 and uses verified company/official evidence URLs to repair URL/proxy quality while adding a mixed positive/counterexample pack.

Loop choice follows the prompt rule: `selected_loop = max(existing loop for selected_round and selected_canonical_archetype_id) + 1`. The current root directory snapshot contains C13 R3 loop 100, 101, and 102 files; therefore this output uses R3 loop 103.

### Novelty check

```yaml
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 2
counterexample_count: 4
source_proxy_only_count: 0
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
hard_duplicate_key_avoidance: canonical_archetype_id + symbol + trigger_type + entry_date checked at research-design level
not_counted_as_new_case_rows: 0
```

The run intentionally keeps two LG Energy Solution rows because they represent different regimes and evidence families: 2023 AMPC launch/current shipment bridge versus 2025 profitability/capacity-reallocation bridge. They should not be collapsed as the same case.

## 2. Stock-Web price and profile audit

Stock-Web manifest snapshot used in this run:

```yaml
manifest_url: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Schema basis:

```yaml
schema_url: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
tradable_columns: d/o/h/l/c/v/a/mc/s/m
MFE_N_pct: (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct: (min low from entry_date through N tradable rows / entry_price - 1) * 100
required_windows: 30D, 90D, 180D
calibration_basis: tradable_raw
```

Profile check:

| symbol | profile source | corporate_action_candidate_dates | selected 180D contamination status |
|---:|---|---|---|
| 373220 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/373/373220.json | none | clean |
| 003670 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/003/003670.json | 2015-05-04; 2021-02-03 | clean for 2023 window |
| 006400 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/006/006400.json | 1996-01-03; 1998-11-03; 2014-07-15 | clean for 2023 window |
| 096770 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/096/096770.json | 2024-11-20 | clean for 2023-07-31 to 2024-04-24 180D window |
| 051910 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/051/051910.json | none | clean |

## 3. Evidence basis

Evidence is official/company-source where possible. No source-proxy rows are used.

| symbol | trigger | evidence source | evidence bridge |
|---:|---|---|---|
| 373220 | 2023-04-26 | https://news.lgensol.com/company-news/press-releases/1705/ | Q1 2023 revenue/OP, AMPC inclusion, North America shipment/JV operation |
| 003670 | 2023-06-02 | https://www.poscofuturem.com/en/pr/view.do?num=695 | Ultium CAM JV capacity expansion, pCAM localization, binding CAM supply |
| 006400 | 2023-04-25 | https://www.samsungsdi.com/sdi-now/sdi-news/3162.html?idx=3162&pageIndex=2&pagesize=15 | GM battery-cell JV, >30GWh, mass production aimed for 2026 |
| 096770 | 2023-07-28 | https://askinno.com/global/archives/15259 | Q2 battery revenue growth and AMPC benefit, but consolidated operating loss |
| 051910 | 2024-02-07 | https://www.lgcorp.com/media/release/27326 | KRW 25tn GM cathode supply, 2026-2035 Tennessee/IRA localization |
| 373220 | 2025-04-30 | https://inside.lgensol.com/en/2025/04/lg-energy-solution-releases-2025-first-quarter-financial-results/ | Return to profitability, IRA credit, cost cutting, North America capacity reallocation, GM JV phase-3 acquisition |

## 4. Trigger-level backtest table

| case_id | symbol | trigger_type | trigger_date | entry_date/price | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | label |
|---|---:|---|---:|---|---:|---:|---:|---|
| C13_2023_LGES_Q1_AMPC_NA_JV | 373220 | Stage2 | 2023-04-26 | 2023-04-27 / 587,000 | 4.5997/-9.7104 | 5.6218/-12.6065 | 5.6218/-36.7121 | counterexample_high_mae |
| C13_2023_POSCO_FUTUREM_GM_ULTIUM_CAM_PCAM | 003670 | Stage4B | 2023-06-02 | 2023-06-05 / 380,000 | 10.5263/-9.3421 | 82.6316/-17.5000 | 82.6316/-39.0789 | positive_local_4b_then_high_mae |
| C13_2023_SAMSUNG_SDI_GM_CELL_JV_2026_START | 006400 | Stage2 | 2023-04-25 | 2023-04-26 / 703,000 | 5.9744/-6.8279 | 5.9744/-17.0697 | 5.9744/-47.7240 | counterexample_future_jv_gap |
| C13_2023_SKINNO_Q2_AMPC_LOSS_REDUCTION_BUT_CONSOLIDATED_LOSS | 096770 | Stage2-Actionable | 2023-07-28 | 2023-07-31 / 216,000 | 5.0926/-22.8704 | 5.0926/-44.3981 | 5.0926/-52.5000 | counterexample_actionable_false_positive |
| C13_2024_LGCHEM_GM_CATHODE_2026_2035_IRA_TENNESSEE | 051910 | Stage2 | 2024-02-07 | 2024-02-08 / 470,500 | 10.5207/-8.6079 | 10.5207/-25.6111 | 10.5207/-43.9957 | counterexample_long_dated_supply_gap |
| C13_2025_LGES_Q1_PROFITABILITY_CAPACITY_REALLOCATION_GM_PHASE3 | 373220 | Stage3-Yellow | 2025-04-30 | 2025-05-02 / 320,500 | 2.6521/-17.0047 | 25.7410/-17.0047 | 64.4306/-17.0047 | positive_operational_bridge_after_drawdown |


## 5. Trigger JSONL

Every usable trigger row below includes the six required price fields: `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`.

```jsonl
{"row_type":"trigger","case_id":"C13_2023_LGES_Q1_AMPC_NA_JV","symbol":"373220","name":"LG에너지솔루션","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"NORTH_AMERICA_AMPC_CURRENT_SHIPMENT_BRIDGE","trigger_type":"Stage2","trigger_date":"2023-04-26","entry_date":"2023-04-27","entry_price":587000.0,"entry_rule":"next_tradable_close_due_intraday_timestamp_unknown","evidence_family":"AMPC inception + North America shipment/JV operation + earnings bridge","evidence_url":"https://news.lgensol.com/company-news/press-releases/1705/","evidence_url_verified":true,"source_proxy_only":false,"MFE_30D_pct":4.5997,"MAE_30D_pct":-9.7104,"MFE_90D_pct":5.6218,"MAE_90D_pct":-12.6065,"MFE_180D_pct":5.6218,"MAE_180D_pct":-36.7121,"peak_30D_date":"2023-06-12","peak_30D_high":614000.0,"trough_30D_date":"2023-05-15","trough_30D_low":530000.0,"peak_90D_date":"2023-07-26","peak_90D_high":620000.0,"trough_90D_date":"2023-08-07","trough_90D_low":513000.0,"peak_180D_date":"2023-07-26","peak_180D_high":620000.0,"trough_180D_date":"2024-01-22","trough_180D_low":371500.0,"MFE_1Y_pct":5.6218,"MAE_1Y_pct":-39.0119,"MFE_2Y_pct":5.6218,"MAE_2Y_pct":-54.6848,"calibration_usable":true,"corporate_action_contaminated_180D":false,"representative_for_aggregate":true,"outcome_label":"counterexample_high_mae","current_profile_error":"Stage2 evidence real but AMPC launch alone over-credits durability; needs utilization + customer demand confirmation before Actionable/Green.","proposed_stage":"Stage2","local_4b":false,"full_4b":false,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"C13_2023_POSCO_FUTUREM_GM_ULTIUM_CAM_PCAM","symbol":"003670","name":"포스코퓨처엠","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"NORTH_AMERICA_CAM_PCAM_JV_SUPPLY_CHAIN_LOCALIZATION","trigger_type":"Stage4B","trigger_date":"2023-06-02","entry_date":"2023-06-05","entry_price":380000.0,"entry_rule":"next_tradable_close_due_intraday_timestamp_unknown","evidence_family":"GM/Ultium CAM JV capacity expansion + pCAM localization + binding supply","evidence_url":"https://www.poscofuturem.com/en/pr/view.do?num=695","evidence_url_verified":true,"source_proxy_only":false,"MFE_30D_pct":10.5263,"MAE_30D_pct":-9.3421,"MFE_90D_pct":82.6316,"MAE_90D_pct":-17.5,"MFE_180D_pct":82.6316,"MAE_180D_pct":-39.0789,"peak_30D_date":"2023-07-10","peak_30D_high":420000.0,"trough_30D_date":"2023-06-30","trough_30D_low":344500.0,"peak_90D_date":"2023-07-26","peak_90D_high":694000.0,"trough_90D_date":"2023-10-10","trough_90D_low":313500.0,"peak_180D_date":"2023-07-26","peak_180D_high":694000.0,"trough_180D_date":"2023-11-01","trough_180D_low":231500.0,"MFE_1Y_pct":82.6316,"MAE_1Y_pct":-39.0789,"MFE_2Y_pct":82.6316,"MAE_2Y_pct":-74.0789,"calibration_usable":true,"corporate_action_contaminated_180D":false,"representative_for_aggregate":true,"outcome_label":"positive_local_4b_then_high_mae","current_profile_error":"Price validation was strong, but full-window drawdown says C13 must split local 4B from durable Green unless utilization/cash conversion arrives.","proposed_stage":"Stage4B","local_4b":true,"full_4b":false,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"C13_2023_SAMSUNG_SDI_GM_CELL_JV_2026_START","symbol":"006400","name":"삼성SDI","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"FUTURE_YEAR_US_CELL_JV_CAPEX_NO_NEAR_TERM_UTILIZATION","trigger_type":"Stage2","trigger_date":"2023-04-25","entry_date":"2023-04-26","entry_price":703000.0,"entry_rule":"next_tradable_close_due_intraday_timestamp_unknown","evidence_family":"US battery cell JV capex + future 2026 mass production","evidence_url":"https://www.samsungsdi.com/sdi-now/sdi-news/3162.html?idx=3162&pageIndex=2&pagesize=15","evidence_url_verified":true,"source_proxy_only":false,"MFE_30D_pct":5.9744,"MAE_30D_pct":-6.8279,"MFE_90D_pct":5.9744,"MAE_90D_pct":-17.0697,"MFE_180D_pct":5.9744,"MAE_180D_pct":-47.724,"peak_30D_date":"2023-06-12","peak_30D_high":745000.0,"trough_30D_date":"2023-05-15","trough_30D_low":655000.0,"peak_90D_date":"2023-06-12","peak_90D_high":745000.0,"trough_90D_date":"2023-08-25","trough_90D_low":583000.0,"peak_180D_date":"2023-06-12","peak_180D_high":745000.0,"trough_180D_date":"2024-01-18","trough_180D_low":367500.0,"MFE_1Y_pct":5.9744,"MAE_1Y_pct":-51.3514,"MFE_2Y_pct":5.9744,"MAE_2Y_pct":-77.5676,"calibration_usable":true,"corporate_action_contaminated_180D":false,"representative_for_aggregate":true,"outcome_label":"counterexample_future_jv_gap","current_profile_error":"Long-dated JV headline inflated visibility but lacked current AMPC, utilization, revenue, and margin bridge.","proposed_stage":"Stage2","local_4b":false,"full_4b":false,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"C13_2023_SKINNO_Q2_AMPC_LOSS_REDUCTION_BUT_CONSOLIDATED_LOSS","symbol":"096770","name":"SK이노베이션","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_LOSS_REDUCTION_WITH_CONSOLIDATED_SEGMENT_RISK","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-28","entry_date":"2023-07-31","entry_price":216000.0,"entry_rule":"next_tradable_close_due_intraday_timestamp_unknown","evidence_family":"battery revenue growth + AMPC loss improvement + consolidated operating loss","evidence_url":"https://askinno.com/global/archives/15259","evidence_url_verified":true,"source_proxy_only":false,"MFE_30D_pct":5.0926,"MAE_30D_pct":-22.8704,"MFE_90D_pct":5.0926,"MAE_90D_pct":-44.3981,"MFE_180D_pct":5.0926,"MAE_180D_pct":-52.5,"peak_30D_date":"2023-08-01","peak_30D_high":227000.0,"trough_30D_date":"2023-09-11","trough_30D_low":166600.0,"peak_90D_date":"2023-08-01","peak_90D_high":227000.0,"trough_90D_date":"2023-11-01","trough_90D_low":120100.0,"peak_180D_date":"2023-08-01","peak_180D_high":227000.0,"trough_180D_date":"2024-04-16","trough_180D_low":102600.0,"MFE_1Y_pct":5.0926,"MAE_1Y_pct":-57.5463,"MFE_2Y_pct":5.0926,"MAE_2Y_pct":-62.5926,"calibration_usable":true,"corporate_action_contaminated_180D":false,"representative_for_aggregate":true,"outcome_label":"counterexample_actionable_false_positive","current_profile_error":"Actionable bonus should be blocked when AMPC reduces loss but consolidated/segment loss and non-battery exposure still dominate.","proposed_stage":"Stage2","local_4b":false,"full_4b":false,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"C13_2024_LGCHEM_GM_CATHODE_2026_2035_IRA_TENNESSEE","symbol":"051910","name":"LG화학","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"LONG_TERM_CATHODE_SUPPLY_IRA_LOCALIZATION_NO_NEAR_TERM_UTILIZATION","trigger_type":"Stage2","trigger_date":"2024-02-07","entry_date":"2024-02-08","entry_price":470500.0,"entry_rule":"press_page_displayed_2024_02_08_body_dateline_Feb_7_next_tradable_close_used","evidence_family":"GM cathode supply + Tennessee IRA localization + 2026-2035 delivery window","evidence_url":"https://www.lgcorp.com/media/release/27326","evidence_url_verified":true,"source_proxy_only":false,"MFE_30D_pct":10.5207,"MAE_30D_pct":-8.6079,"MFE_90D_pct":10.5207,"MAE_90D_pct":-25.6111,"MFE_180D_pct":10.5207,"MAE_180D_pct":-43.9957,"peak_30D_date":"2024-02-19","peak_30D_high":520000.0,"trough_30D_date":"2024-03-15","trough_30D_low":430000.0,"peak_90D_date":"2024-02-19","peak_90D_high":520000.0,"trough_90D_date":"2024-05-30","trough_90D_low":350000.0,"peak_180D_date":"2024-02-19","peak_180D_high":520000.0,"trough_180D_date":"2024-08-05","trough_180D_low":263500.0,"MFE_1Y_pct":10.5207,"MAE_1Y_pct":-55.7917,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"calibration_usable":true,"corporate_action_contaminated_180D":false,"representative_for_aggregate":true,"outcome_label":"counterexample_long_dated_supply_gap","current_profile_error":"Long-duration supply agreement and IRA localization are real, but 2026 start and weak EV chain made the bridge too delayed for Actionable/Green.","proposed_stage":"Stage2","local_4b":false,"full_4b":false,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"C13_2025_LGES_Q1_PROFITABILITY_CAPACITY_REALLOCATION_GM_PHASE3","symbol":"373220","name":"LG에너지솔루션","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_PROFITABILITY_UTILIZATION_REALLOCATION_BRIDGE","trigger_type":"Stage3-Yellow","trigger_date":"2025-04-30","entry_date":"2025-05-02","entry_price":320500.0,"entry_rule":"next_tradable_close_due_intraday_timestamp_unknown","evidence_family":"AMPC profitability + cost cutting + North America capacity reallocation + GM JV phase-3 acquisition","evidence_url":"https://inside.lgensol.com/en/2025/04/lg-energy-solution-releases-2025-first-quarter-financial-results/","evidence_url_verified":true,"source_proxy_only":false,"MFE_30D_pct":2.6521,"MAE_30D_pct":-17.0047,"MFE_90D_pct":25.741,"MAE_90D_pct":-17.0047,"MFE_180D_pct":64.4306,"MAE_180D_pct":-17.0047,"peak_30D_date":"2025-05-08","peak_30D_high":329000.0,"trough_30D_date":"2025-05-23","trough_30D_low":266000.0,"peak_90D_date":"2025-07-31","peak_90D_high":403000.0,"trough_90D_date":"2025-05-23","trough_90D_low":266000.0,"peak_180D_date":"2025-10-29","peak_180D_high":527000.0,"trough_180D_date":"2025-05-23","trough_180D_low":266000.0,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"calibration_usable":true,"corporate_action_contaminated_180D":false,"representative_for_aggregate":true,"outcome_label":"positive_operational_bridge_after_drawdown","current_profile_error":"Calibrated profile may be too slow after real operating bridge appears, but Green still needs drawdown-aware confirmation because initial MAE was -17%.","proposed_stage":"Stage3-Yellow","local_4b":false,"full_4b":false,"do_not_count_as_new_case":false}
```

## 6. Score simulation / raw component breakdown

Component labels are the canonical E2R evidence dimensions used for research simulation only. This section is shadow-only and does not patch production scoring.

| case_id | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Risk | Total | proposed stage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C13_2023_LGES_Q1_AMPC_NA_JV | 15 | 17 | 12 | 10 | 7 | 8 | 12 | -7 | 74 | Stage2 |
| C13_2023_POSCO_FUTUREM_GM_ULTIUM_CAM_PCAM | 16 | 21 | 17 | 15 | 8 | 8 | 12 | -13 | 84 | Stage4B |
| C13_2023_SAMSUNG_SDI_GM_CELL_JV_2026_START | 12 | 18 | 11 | 9 | 8 | 8 | 11 | -12 | 65 | Stage2 |
| C13_2023_SKINNO_Q2_AMPC_LOSS_REDUCTION_BUT_CONSOLIDATED_LOSS | 13 | 15 | 10 | 8 | 6 | 7 | 14 | -16 | 57 | Stage2 |
| C13_2024_LGCHEM_GM_CATHODE_2026_2035_IRA_TENNESSEE | 13 | 18 | 12 | 9 | 7 | 8 | 12 | -14 | 65 | Stage2 |
| C13_2025_LGES_Q1_PROFITABILITY_CAPACITY_REALLOCATION_GM_PHASE3 | 18 | 20 | 15 | 13 | 9 | 9 | 14 | -10 | 88 | Stage3-Yellow cap before Green |


Interpretation:

1. **AMPC inception is not the same as AMPC durability.** LGES Q1 2023 had real AMPC and North America evidence, but 180D MFE was only +5.62% while MAE reached -36.71%. The evidence was a key, not yet the lock turning.
2. **Future-year JV capex should be capped before utilization.** Samsung SDI/GM and LG Chem/GM both had credible North America/IRA localization evidence, but production or supply was mostly 2026+; both produced weak MFE and severe 180D drawdown.
3. **AMPC loss reduction can be a false positive if the consolidated body is still bleeding.** SK Innovation's battery segment improved with AMPC, but the consolidated operating loss and non-battery exposure left the entry exposed to -52.50% 180D MAE.
4. **Local 4B and durable Green must be separated.** POSCO Future M validated the price path locally with +82.63% MFE, but the same 180D window showed -39.08% MAE, so it is local 4B evidence rather than a clean full-window Green.
5. **The 2025 LGES case is the clearest positive bridge.** The 2025 setup combined AMPC, profitability, cost cutting, capacity reallocation, and GM JV phase-3 utilization logic; it reached +64.43% 180D MFE, but the -17.00% early MAE argues for Stage3-Yellow before Green.

## 7. Stage transition and residual error summary

| transition issue | affected rows | residual finding | proposed shadow treatment |
|---|---:|---|---|
| Stage2 over-credit for AMPC/JV headline | 373220 2023, 006400 2023, 051910 2024 | policy/JV language appears before operating conversion | cap at Stage2 unless two bridge factors are present |
| Stage2-Actionable false positive | 096770 2023 | AMPC reduces loss but consolidated/segment loss remains dominant | block actionable bonus when loss bridge is incomplete |
| Local 4B vs full 4B | 003670 2023 | large upside but brutal full-window drawdown | mark local 4B, not durable Green |
| Too-late risk after operating bridge | 373220 2025 | AMPC + current operating action finally worked | allow Stage3-Yellow when profitability and utilization bridge are both explicit |

## 8. Residual contribution summary

```yaml
residual_contribution_label: C13_JV_AMPC_UTILIZATION_BRIDGE_CAP
new_axis_proposed: C13_JV_AMPC_UTILIZATION_BRIDGE_CAP
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - earlier_thesis_break_watch
existing_axis_weakened: null
production_scoring_changed: false
shadow_weight_only: true
current_profile_error_count: 5
```

### Candidate sector/canonical rule

For `C13_BATTERY_JV_UTILIZATION_AMPC_IRA`, do not let `AMPC`, `IRA`, `JV`, or `North America localization` vocabulary unlock Stage2-Actionable by itself. Require at least **two** of the following bridge factors:

```yaml
C13_required_bridge_factors:
  - current_period_revenue_or_shipment_growth
  - explicit_utilization_or_yield_improvement
  - AMPC_amount_reflected_in_profit_with_positive_or_improving_operating_profit
  - customer_calloff_or_binding_supply_with_near_term_delivery
  - capacity_reallocation_or_downtime_minimization_showing operating discipline
  - capex-to-production window within 12-18 months, not merely 2026+ promise
```

Blocking factors:

```yaml
C13_actionable_blockers:
  - mass_production_start_more_than_18_months_after_trigger_without_current_revenue_bridge
  - consolidated_operating_loss_dominates_AMPC_improvement
  - segment_loss_still_material_without clear path to EBITDA/OP positivity
  - EV demand slowdown/call-off risk unresolved
  - price-only vertical move without non-price operating bridge
```

Positive unlock:

```yaml
C13_positive_unlock:
  Stage3_Yellow_allowed_when:
    - AMPC/profitability bridge exists
    - current shipments or utilization bridge exists
    - capacity discipline/reallocation is explicit
    - 30D/90D drawdown remains manageable or drawdown is followed by evidence reinforcement
  Stage3_Green_still_requires:
    - earnings revision or cash-margin confirmation
    - durable customer demand visibility
    - no unresolved call-off/underutilization risk
```

## 9. Shadow weight candidate

No global weight relaxation is proposed. This is a C13-only gate and bridge-strengthening proposal.

```yaml
shadow_weight_candidate:
  scope: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  current_runtime_weight_reference: EPS/Vis/Bott/Mis/Val/Cap/Info = 20/18/14/12/10/10/16
  proposed_delta_shadow_only:
    EPS_FCF: 0
    visibility: +1
    bottleneck_pricing: -1
    market_mispricing: -1
    valuation_rerating: -1
    capital_allocation: +1
    information_confidence: +1
  guardrail_overlay:
    C13_AMPC_JV_keyword_only_stage2_actionable_block: true
    C13_future_year_production_without_current_utilization_cap: Stage2
    C13_consolidated_loss_blocks_actionable_bonus: true
    C13_local_4b_requires_full_window_split: true
```

Reason: C13 already has high Info weight in the current runtime profile. The residual error is less “not enough information weight” and more “information is arriving before cash/utilization conversion.” The adjustment should act like a customs gate at the port: the container label says IRA/JV/AMPC, but the gate still needs the invoice, shipment, and unloading record before the goods are booked as revenue.

## 10. Batch ingest self-audit

```yaml
output_file_regex_pass: true
filename_round_matches_metadata: true
filename_loop_matches_metadata: true
round_sector_consistency: pass
canonical_stage_labels_only: true
trigger_rows: 6
trigger_rows_with_complete_30_90_180_mfe_mae: 6
calibration_usable_rows: 6
rows_missing_required_mfe_mae: 0
rows_with_entry_date: 6
rows_with_entry_price: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
corporate_action_contaminated_180D_rows: 0
same_entry_group_dedup_required: false
positive_case_count: 2
counterexample_count: 4
local_4b_case_count: 1
full_4b_case_count: 0
hard_4c_case_count: 0
narrative_only_rows: 0
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding/calibration agent. Do not execute this during the research run.

Input MD:
e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md

Task:
1. Ingest the six trigger JSONL rows if schema validation passes.
2. Verify complete MFE_30D_pct/MFE_90D_pct/MFE_180D_pct and MAE_30D_pct/MAE_90D_pct/MAE_180D_pct fields.
3. Verify no 180D corporate-action contamination for 373220, 003670, 006400, 096770, 051910.
4. Evaluate shadow axis `C13_JV_AMPC_UTILIZATION_BRIDGE_CAP` only as a C13-specific candidate.
5. Do not loosen global Stage3-Green threshold.
6. Do not change production scoring unless batch promotion independently confirms this axis across the cumulative v12 corpus.
7. Consider adding a C13 gate: AMPC/JV/IRA keyword-only evidence cannot unlock Stage2-Actionable unless at least two operating bridge factors are present.
8. Preserve local 4B vs full-window 4B split for POSCO Future M-like vertical moves.
```

## 12. Completed state

```yaml
completed_round: R3
completed_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C13 AMPC/IRA duration, JV utilization, future-production false positives, and URL/proxy repair
next_recommended_archetypes:
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
```
