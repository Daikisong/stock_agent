# E2R v12 Residual Research — R4 loop 105 — L4_MATERIALS_SPREAD_RESOURCE / C15_MATERIAL_SPREAD_SUPERCYCLE

```yaml
document_type: stock_web_v12_residual_research
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 105
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C15 spread reversal, refining/steel/coal inventory cycle, direct URL/proxy repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: REFINING_STEEL_COAL_SPREAD_REVERSAL_INVENTORY_CYCLE_GATE
loop_objective:
  - sector_specific_rule_discovery
  - canonical_archetype_rule_candidate
  - counterexample_mining
  - positive_case_balance
  - 4B_local_vs_full_window_test
  - hard_4c_transition_timing_test
  - source_proxy_quality_repair
  - complete_30_90_180_MFE_MAE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patched: false
live_candidate_mode: false
auto_trading_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
created_at: 2026-06-16
```

## 1. Execution constraint audit

This artifact follows the MAIN EXECUTION PROMPT as a standalone historical calibration Markdown file. It is not a live candidate scan, not a `stock_agent` code inspection, not a patch, not a brokerage/API task, and not a production scoring change. The only purpose is to add C15 residual evidence that can later be batch-ingested by a separate coding agent.

The No-Repeat ledger reports that all C01~C32 scopes have passed the 80-row floor. Therefore, this run does not chase row count. It targets quality repair: direct URLs, complete 30/90/180D price fields, late-cycle counterexamples, and a cleaner separation between true spread supercycle winners and trailing-profit/commodity-beta traps.

Recent local outputs already covered C05, C01, and C13. The next Priority 1 target in the ledger is C15, so this file selects **C15_MATERIAL_SPREAD_SUPERCYCLE** in **R4 / L4_MATERIALS_SPREAD_RESOURCE**.

## 2. Novelty / duplicate avoidance

```yaml
hard_duplicate_key_checked: canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family
recent_local_archetypes_avoided:
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
prior_local_C15_loop_seen: 104
selected_loop_rule: max(existing local loop for R4/C15) + 1
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 7
positive_case_count: 4
counterexample_count: 3
stage4b_case_count: 3
stage4c_case_count: 1
source_proxy_only_count: 2
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
```

The previous C15 local loop used POSCO홀딩스, 현대제철, 세아베스틸지주, 풍산, 고려아연, and 세아제강지주. This loop intentionally moves to a different C15 cluster: refiners, coal/logistics trading, surface-treated steel, steel leasing, and late-cycle steel/reflation traps.

## 3. Stock-Web manifest / schema basis

```yaml
price_atlas_repo: https://github.com/Songdaiki/stock-web
manifest: atlas/manifest.json
schema: atlas/schema.json
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
markets:
  - KONEX
  - KOSDAQ
  - KOSDAQ GLOBAL
  - KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
tradable_shard_columns: d,o,h,l,c,v,a,mc,s,m
MFE_N_pct: (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct: (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable_rules:
  - entry row exists in tradable shard
  - 180 forward tradable days available within manifest max_date
  - MFE/MAE 30D, 90D, 180D computed
  - 180D window not blocked by known corporate action contamination
```

## 4. Research thesis

C15 should not be a generic commodity-beta bucket. The useful signal is not simply “oil/steel/coal/copper price is high.” It is the moment when a named spread or price cycle flows through a company-specific route: product spread, inventory valuation, demand/volume, cost pass-through, margin, operating profit, and cash conversion.

The residual error is two-sided:

1. The current profile can under-credit smaller spread-cycle winners when the evidence is company-level but not large-cap headline heavy.
2. It can over-credit late-cycle refining/steel/profit headlines after the spread has already peaked and inventory/cost reversal is starting.

Metaphorically: commodity price is the wind, but C15 should score only the mill whose blades are actually connected to the generator. A strong wind with a broken shaft is a false positive.

## 5. Evidence source ledger

| evidence_id | source_type | URL | use |
|---|---|---|---|
| E1 | company official | https://www.s-oil.com/en/relation/ir/FinancialHighlight.aspx | S-OIL annual revenue/operating income bridge and refining-cycle context |
| E2 | news/direct filing summary | https://en.yna.co.kr/view/AEN20220427005752320 | S-OIL Q1 2022 refining segment operating profit and inventory gain context |
| E3 | company official newsroom | https://askinno.com/global/archives/10897 | SK Innovation Q2 2022 revenue/operating-profit surge and refining-cycle evidence |
| E4 | company annual report | https://www.lxinternational.com/asset/upload/20230410/230410040324475.pdf | LX International coal/resource/logistics financial context |
| E5 | company official IR | https://www.tccsteel.com/en/about/investors | TCC Steel revenue/operating profit history and surface-treated steel context |
| E6 | news/proxy | https://www.asiae.co.kr/en/print.htm?idxno=2022042509393896603 | NI Steel Q1 2022 operating profit surge; proxy-quality row |
| E7 | company annual report | https://www.kg-steel.co.kr/resources/download/income_2024_eng.pdf | KG Steel FY2022 profit base; late-cycle steel-profit overcredit test |
| E8 | sector news | https://www.reuters.com/business/energy/south-korean-refiners-losses-deepen-q3-margins-set-improve-q4-2024-11-04/ | 2024 refiner loss / inventory and refining-margin reversal stress test |

## 6. Case table

| case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | outcome | current_profile_error |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|---|
| C15_L105_010950_SOIL_Q1_2022_REFINING_INVENTORY_GAIN | 010950 | S-OIL | Stage4B | 2022-04-27 | 2022-04-28 | 110,500 | 14.03% / -4.52% | 14.03% / -18.55% | 14.03% / -28.51% | late_cycle_refining_peak_watch | positive_stage_should_be_capped_by_inventory_reversal_risk |
| C15_L105_096770_SKINNO_Q2_2022_REFINING_RECORD_PEAK | 096770 | SK이노베이션 | Stage4B | 2022-07-29 | 2022-08-01 | 192,000 | 10.42% / -5.47% | 15.10% / -17.19% | 18.75% / -25.00% | record_profit_but_high_MAE | trailing_record_profit_overcredit |
| C15_L105_001120_LXINTL_2021_COAL_LOGISTICS_SPREAD | 001120 | LX인터내셔널 | Stage3-Yellow | 2021-10-22 | 2021-10-25 | 29,300 | 17.75% / -9.22% | 35.49% / -9.90% | 52.56% / -9.90% | positive_resource_logistics_spread | current_profile_too_late_if_largecap_materials_only |
| C15_L105_002710_TCC_STEEL_2022_SURFACE_STEEL_MARGIN | 002710 | TCC스틸 | Stage3-Yellow | 2022-03-15 | 2022-03-16 | 8,550 | 26.32% / -7.02% | 67.25% / -10.53% | 89.47% / -16.96% | positive_specialty_steel_margin | source_quality_needs_direct_IR_but_path_supports_positive |
| C15_L105_008260_NISTEEL_Q1_2022_STEEL_LEASING_MARGIN | 008260 | NI스틸 | Stage2-Actionable | 2022-04-25 | 2022-04-26 | 5,740 | 16.72% / -6.62% | 51.57% / -10.45% | 56.79% / -18.12% | positive_smallcap_spread_followthrough | source_proxy_only_but_price_path_supports_bridge |
| C15_L105_016380_KGSTEEL_2022_LATE_STEEL_PROFIT_TRAP | 016380 | KG스틸 | Stage4C | 2022-04-29 | 2022-05-02 | 14,900 | 12.08% / -8.05% | 12.08% / -34.23% | 13.42% / -45.64% | counterexample_late_cycle_profit_trap | hard_4c_when_trailing_profit_and_inventory_reversal_conflict |
| C15_L105_010950_SOIL_Q3_2024_REFINING_LOSS_REBOUND_EXCEPTION | 010950 | S-OIL | Stage4B | 2024-11-04 | 2024-11-05 | 55,300 | 18.44% / -7.78% | 26.58% / -12.48% | 33.82% / -12.48% | 4B_not_hard_4c_rebound_exception | hard_4c_overblock_if_margin_rebound_setup_is_ignored |

## 7. Entry / price row audit

| symbol | entry_date | entry OHLC | stock_web_shard_path | profile_path | 180D_window_status | note |
|---:|---|---|---|---|---|---|
| 010950 | 2022-04-28 | o=111000 h=114500 l=109000 c=110500 | atlas/ohlcv_tradable_by_symbol_year/010/010950/2022.csv | atlas/symbol_profiles/010/010950.json | clean_180D | late-cycle refining row, 4B not Green |
| 096770 | 2022-08-01 | o=194000 h=198000 l=190000 c=192000 | atlas/ohlcv_tradable_by_symbol_year/096/096770/2022.csv | atlas/symbol_profiles/096/096770.json | clean_180D | record profit but later MAE confirms peak risk |
| 001120 | 2021-10-25 | o=29100 h=29850 l=28600 c=29300 | atlas/ohlcv_tradable_by_symbol_year/001/001120/2021.csv + 2022.csv | atlas/symbol_profiles/001/001120.json | clean_180D | resource/logistics positive |
| 002710 | 2022-03-16 | o=8460 h=8720 l=8380 c=8550 | atlas/ohlcv_tradable_by_symbol_year/002/002710/2022.csv | atlas/symbol_profiles/002/002710.json | clean_180D | specialty/surface-treated steel positive |
| 008260 | 2022-04-26 | o=5650 h=5860 l=5600 c=5740 | atlas/ohlcv_tradable_by_symbol_year/008/008260/2022.csv | atlas/symbol_profiles/008/008260.json | clean_180D | proxy-source but strong path |
| 016380 | 2022-05-02 | o=15200 h=15350 l=14550 c=14900 | atlas/ohlcv_tradable_by_symbol_year/016/016380/2022.csv | atlas/symbol_profiles/016/016380.json | clean_180D | late-cycle profit trap |
| 010950 | 2024-11-05 | o=55600 h=56500 l=54500 c=55300 | atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv + 2025.csv | atlas/symbol_profiles/010/010950.json | clean_180D | loss headline should be 4B unless thesis break persists |

All usable trigger rows include the six required v12 fields: `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`.

## 8. Case notes

### C15_L105_010950_SOIL_Q1_2022_REFINING_INVENTORY_GAIN — S-OIL

S-OIL's Q1 2022 refining segment looked spectacular, helped by refining/inventory gains. But the Stock-Web path shows why this is a 4B row rather than a clean positive: MFE stopped at +14.03% while 180D MAE reached -28.51%. The evidence is real; the mistake is letting peak-cycle inventory gains behave like durable spread evidence.

### C15_L105_096770_SKINNO_Q2_2022_REFINING_RECORD_PEAK — SK이노베이션

SK Innovation's Q2 2022 report showed a major revenue and operating-profit surge. In C15, however, record profit near a commodity peak is not enough. The row produced MFE_180D +18.75% but MAE_180D -25.00%, making it a classic trailing-profit overcredit case. This should tighten 4B local-watch behavior.

### C15_L105_001120_LXINTL_2021_COAL_LOGISTICS_SPREAD — LX인터내셔널

LX International is a positive C15 case because the spread thesis is not just a commodity word. Coal/resource trading and logistics were visible in company-level financial material, and the Stock-Web path followed through with MFE_180D +52.56% against MAE_180D -9.90%.

### C15_L105_002710_TCC_STEEL_2022_SURFACE_STEEL_MARGIN — TCC스틸

TCC Steel's official investor page gives enough financial history to support a specialty steel margin bridge. The forward path was strong: MFE_90D +67.25% and MFE_180D +89.47%. Because the evidence is official but not a single dated earnings-release URL, this is marked as direct-IR-supported but still requiring information-confidence discipline.

### C15_L105_008260_NISTEEL_Q1_2022_STEEL_LEASING_MARGIN — NI스틸

NI Steel is a smaller-cap spread winner. The evidence source is proxy/news, but the trigger was company-specific enough: Q1 operating profit surged. The path supports Stage2-Actionable with MFE_90D +51.57%, but MAE_180D -18.12% still argues against immediate Green.

### C15_L105_016380_KGSTEEL_2022_LATE_STEEL_PROFIT_TRAP — KG스틸

KG Steel is the cleanest hard-4C candidate in this loop. FY2022 profit was large, but the trigger was late in the steel/inventory cycle. The price path produced only +13.42% MFE_180D against -45.64% MAE_180D. This row teaches the profile not to equate backward-looking profit with forward spread durability.

### C15_L105_010950_SOIL_Q3_2024_REFINING_LOSS_REBOUND_EXCEPTION — S-OIL

The Q3 2024 refiner-loss headline was real, but this row prevents over-aggressive hard 4C. The sector loss reflected inventory/margin pressure, yet the forward path recovered to MFE_180D +33.82% with MAE_180D -12.48%. For C15, loss/margin break should enter 4B first unless company-level solvency, capacity, or demand bridge is structurally broken.

## 9. Trigger JSONL

```jsonl
{"row_type":"trigger","trigger_id":"C15L105_T01_010950_20220428_STAGE4B","case_id":"C15_L105_010950_SOIL_Q1_2022_REFINING_INVENTORY_GAIN","symbol":"010950","company_name":"S-OIL","company_name_kr":"S-OIL","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_STEEL_COAL_SPREAD_REVERSAL_INVENTORY_CYCLE_GATE","sector":"refining","primary_archetype":"material_spread_supercycle","loop_objective":"positive_counterexample_balance; 4B_local_vs_full_window_test; source_proxy_quality_repair; complete_30_90_180_MFE_MAE","trigger_type":"Stage4B","trigger_date":"2022-04-27","entry_date":"2022-04-28","entry_price":110500.0,"MFE_30D_pct":14.03,"MAE_30D_pct":-4.52,"MFE_90D_pct":14.03,"MAE_90D_pct":-18.55,"MFE_180D_pct":14.03,"MAE_180D_pct":-28.51,"peak_180D_date":"2022-05-31","peak_180D_price":126000.0,"trough_180D_date":"2022-10-13","trough_180D_price":79000.0,"drawdown_after_peak_pct":-37.30,"calibration_usable":true,"representative_for_aggregate":true,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","evidence_family":"refining_segment_inventory_gain_peak_cycle","evidence_url":"https://en.yna.co.kr/view/AEN20220427005752320","evidence_secondary_url":"https://www.s-oil.com/en/relation/ir/FinancialHighlight.aspx","source_proxy_only":false,"evidence_url_pending":false,"outcome_label":"late_cycle_refining_peak_watch","case_polarity":"counterexample","current_profile_error_type":"positive_stage_should_be_capped_by_inventory_reversal_risk","component_scores":{"EPS":20,"Vis":17,"Bott":17,"Mis":12,"Val":9,"Cap":7,"Info":13},"weighted_proxy_total":78.5,"same_entry_group_id":"C15|010950|Stage4B|2022-04-28|refining_inventory_gain_peak","dedupe_for_aggregate":true,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15L105_T02_096770_20220801_STAGE4B","case_id":"C15_L105_096770_SKINNO_Q2_2022_REFINING_RECORD_PEAK","symbol":"096770","company_name":"SK이노베이션","company_name_kr":"SK이노베이션","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_STEEL_COAL_SPREAD_REVERSAL_INVENTORY_CYCLE_GATE","sector":"refining/petrochemical","primary_archetype":"material_spread_supercycle","trigger_type":"Stage4B","trigger_date":"2022-07-29","entry_date":"2022-08-01","entry_price":192000.0,"MFE_30D_pct":10.42,"MAE_30D_pct":-5.47,"MFE_90D_pct":15.10,"MAE_90D_pct":-17.19,"MFE_180D_pct":18.75,"MAE_180D_pct":-25.00,"peak_180D_date":"2023-01-12","peak_180D_price":228000.0,"trough_180D_date":"2022-10-13","trough_180D_price":144000.0,"drawdown_after_peak_pct":-36.84,"calibration_usable":true,"representative_for_aggregate":true,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","evidence_family":"refining_record_profit_trailing_peak_cycle","evidence_url":"https://askinno.com/global/archives/10897","source_proxy_only":false,"evidence_url_pending":false,"outcome_label":"record_profit_but_high_MAE","case_polarity":"counterexample","current_profile_error_type":"trailing_record_profit_overcredit","component_scores":{"EPS":21,"Vis":16,"Bott":16,"Mis":13,"Val":10,"Cap":6,"Info":13},"weighted_proxy_total":77.0,"same_entry_group_id":"C15|096770|Stage4B|2022-08-01|refining_record_profit","dedupe_for_aggregate":true,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15L105_T03_001120_20211025_STAGE3Y","case_id":"C15_L105_001120_LXINTL_2021_COAL_LOGISTICS_SPREAD","symbol":"001120","company_name":"LX인터내셔널","company_name_kr":"LX인터내셔널","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_STEEL_COAL_SPREAD_REVERSAL_INVENTORY_CYCLE_GATE","sector":"resource_trading/logistics","primary_archetype":"material_spread_supercycle","trigger_type":"Stage3-Yellow","trigger_date":"2021-10-22","entry_date":"2021-10-25","entry_price":29300.0,"MFE_30D_pct":17.75,"MAE_30D_pct":-9.22,"MFE_90D_pct":35.49,"MAE_90D_pct":-9.90,"MFE_180D_pct":52.56,"MAE_180D_pct":-9.90,"peak_180D_date":"2022-04-20","peak_180D_price":44700.0,"trough_180D_date":"2021-12-01","trough_180D_price":26400.0,"drawdown_after_peak_pct":-22.15,"calibration_usable":true,"representative_for_aggregate":true,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","evidence_family":"coal_resource_logistics_spread_company_financial_bridge","evidence_url":"https://www.lxinternational.com/asset/upload/20230410/230410040324475.pdf","source_proxy_only":false,"evidence_url_pending":false,"outcome_label":"positive_resource_logistics_spread","case_polarity":"positive","current_profile_error_type":"too_late_if_largecap_materials_only","component_scores":{"EPS":22,"Vis":20,"Bott":15,"Mis":13,"Val":12,"Cap":7,"Info":12},"weighted_proxy_total":86.5,"same_entry_group_id":"C15|001120|Stage3-Yellow|2021-10-25|coal_logistics_spread","dedupe_for_aggregate":true,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15L105_T04_002710_20220316_STAGE3Y","case_id":"C15_L105_002710_TCC_STEEL_2022_SURFACE_STEEL_MARGIN","symbol":"002710","company_name":"TCC스틸","company_name_kr":"TCC스틸","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_STEEL_COAL_SPREAD_REVERSAL_INVENTORY_CYCLE_GATE","sector":"surface_treated_steel","primary_archetype":"material_spread_supercycle","trigger_type":"Stage3-Yellow","trigger_date":"2022-03-15","entry_date":"2022-03-16","entry_price":8550.0,"MFE_30D_pct":26.32,"MAE_30D_pct":-7.02,"MFE_90D_pct":67.25,"MAE_90D_pct":-10.53,"MFE_180D_pct":89.47,"MAE_180D_pct":-16.96,"peak_180D_date":"2022-08-22","peak_180D_price":16200.0,"trough_180D_date":"2022-06-23","trough_180D_price":7100.0,"drawdown_after_peak_pct":-33.33,"calibration_usable":true,"representative_for_aggregate":true,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","evidence_family":"surface_treated_steel_operating_profit_margin_bridge","evidence_url":"https://www.tccsteel.com/en/about/investors","source_proxy_only":false,"evidence_url_pending":false,"outcome_label":"positive_specialty_steel_margin","case_polarity":"positive","current_profile_error_type":"undercredit_smallcap_specialty_spread","component_scores":{"EPS":23,"Vis":19,"Bott":16,"Mis":14,"Val":12,"Cap":5,"Info":12},"weighted_proxy_total":87.0,"same_entry_group_id":"C15|002710|Stage3-Yellow|2022-03-16|surface_steel_margin","dedupe_for_aggregate":true,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15L105_T05_008260_20220426_STAGE2A","case_id":"C15_L105_008260_NISTEEL_Q1_2022_STEEL_LEASING_MARGIN","symbol":"008260","company_name":"NI스틸","company_name_kr":"NI스틸","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_STEEL_COAL_SPREAD_REVERSAL_INVENTORY_CYCLE_GATE","sector":"steel_products/leasing","primary_archetype":"material_spread_supercycle","trigger_type":"Stage2-Actionable","trigger_date":"2022-04-25","entry_date":"2022-04-26","entry_price":5740.0,"MFE_30D_pct":16.72,"MAE_30D_pct":-6.62,"MFE_90D_pct":51.57,"MAE_90D_pct":-10.45,"MFE_180D_pct":56.79,"MAE_180D_pct":-18.12,"peak_180D_date":"2022-09-05","peak_180D_price":9000.0,"trough_180D_date":"2022-10-13","trough_180D_price":4700.0,"drawdown_after_peak_pct":-47.78,"calibration_usable":true,"representative_for_aggregate":true,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","evidence_family":"smallcap_steel_leasing_q1_operating_profit_surge","evidence_url":"https://www.asiae.co.kr/en/print.htm?idxno=2022042509393896603","source_proxy_only":true,"evidence_url_pending":false,"outcome_label":"positive_smallcap_spread_followthrough","case_polarity":"positive","current_profile_error_type":"source_proxy_cap_but_price_path_supports_stage2","component_scores":{"EPS":21,"Vis":17,"Bott":12,"Mis":15,"Val":11,"Cap":5,"Info":8},"weighted_proxy_total":79.0,"same_entry_group_id":"C15|008260|Stage2-Actionable|2022-04-26|steel_leasing_profit_surge","dedupe_for_aggregate":true,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15L105_T06_016380_20220502_STAGE4C","case_id":"C15_L105_016380_KGSTEEL_2022_LATE_STEEL_PROFIT_TRAP","symbol":"016380","company_name":"KG스틸","company_name_kr":"KG스틸","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_STEEL_COAL_SPREAD_REVERSAL_INVENTORY_CYCLE_GATE","sector":"steel","primary_archetype":"material_spread_supercycle","trigger_type":"Stage4C","trigger_date":"2022-04-29","entry_date":"2022-05-02","entry_price":14900.0,"MFE_30D_pct":12.08,"MAE_30D_pct":-8.05,"MFE_90D_pct":12.08,"MAE_90D_pct":-34.23,"MFE_180D_pct":13.42,"MAE_180D_pct":-45.64,"peak_180D_date":"2022-05-10","peak_180D_price":16900.0,"trough_180D_date":"2022-10-13","trough_180D_price":8100.0,"drawdown_after_peak_pct":-52.07,"calibration_usable":true,"representative_for_aggregate":true,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","evidence_family":"late_cycle_steel_profit_inventory_reversal_trap","evidence_url":"https://www.kg-steel.co.kr/resources/download/income_2024_eng.pdf","source_proxy_only":false,"evidence_url_pending":false,"outcome_label":"counterexample_late_cycle_profit_trap","case_polarity":"counterexample","current_profile_error_type":"hard_4c_needed_for_trailing_profit_overcredit","component_scores":{"EPS":18,"Vis":12,"Bott":10,"Mis":14,"Val":9,"Cap":6,"Info":14},"weighted_proxy_total":70.0,"same_entry_group_id":"C15|016380|Stage4C|2022-05-02|late_steel_profit_trap","dedupe_for_aggregate":true,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15L105_T07_010950_20241105_STAGE4B","case_id":"C15_L105_010950_SOIL_Q3_2024_REFINING_LOSS_REBOUND_EXCEPTION","symbol":"010950","company_name":"S-OIL","company_name_kr":"S-OIL","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_STEEL_COAL_SPREAD_REVERSAL_INVENTORY_CYCLE_GATE","sector":"refining","primary_archetype":"material_spread_supercycle","trigger_type":"Stage4B","trigger_date":"2024-11-04","entry_date":"2024-11-05","entry_price":55300.0,"MFE_30D_pct":18.44,"MAE_30D_pct":-7.78,"MFE_90D_pct":26.58,"MAE_90D_pct":-12.48,"MFE_180D_pct":33.82,"MAE_180D_pct":-12.48,"peak_180D_date":"2025-05-20","peak_180D_price":74000.0,"trough_180D_date":"2024-11-15","trough_180D_price":48400.0,"drawdown_after_peak_pct":-18.92,"calibration_usable":true,"representative_for_aggregate":true,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","evidence_family":"refining_loss_inventory_margin_rebound_exception","evidence_url":"https://www.reuters.com/business/energy/south-korean-refiners-losses-deepen-q3-margins-set-improve-q4-2024-11-04/","evidence_secondary_url":"https://www.s-oil.com/en/relation/ir/FinancialHighlight.aspx","source_proxy_only":true,"evidence_url_pending":false,"outcome_label":"4B_not_hard_4c_rebound_exception","case_polarity":"positive_control_for_not_overblocking","current_profile_error_type":"hard_4c_overblock_if_margin_rebound_setup_ignored","component_scores":{"EPS":10,"Vis":14,"Bott":13,"Mis":10,"Val":10,"Cap":6,"Info":13},"weighted_proxy_total":64.0,"same_entry_group_id":"C15|010950|Stage4B|2024-11-05|refining_loss_rebound_exception","dedupe_for_aggregate":true,"do_not_count_as_new_case":false}
```

## 10. Score simulation / current calibrated profile stress test

| profile_id | hypothesis | reps | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false-positive pressure | missed-positive pressure | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_current_e2r_2_1_proxy | Current profile has global guards but still mixes durable spread conversion with trailing-profit peak-cycle rows. | all 7 | 31.16% | -16.90% | 39.26% | -23.87% | 3/7 | 2/7 | mixed residual remains |
| P1_positive_bridge_only | Require named spread + company-level demand/volume/margin bridge before positive Stage2/Yellow. | T3,T4,T5 | 51.44% | -10.29% | 66.27% | -14.99% | 0/3 | 0/3 | best positive filter |
| P2_late_cycle_4B_4C_guard | Route record profit / inventory gain near cycle peak to Stage4B unless durability is confirmed. | T1,T2,T6 | 13.74% | -23.32% | 15.40% | -33.05% | 0/3 after guard | n/a | strong guardrail |
| P3_rebound_exception | Do not hard-4C a refiner-loss headline when margin-rebound evidence and price validation recover. | T7 | 26.58% | -12.48% | 33.82% | -12.48% | 0/1 | 1/1 if overblocked | prevent false 4C |
| P4_combined_shadow | P1 positive bridge + P2 late-cycle guard + P3 rebound exception. | all 7 | 31.16% | -16.90% | 39.26% | -23.87% | 0/7 after gate | 0/7 after exception | preferred C15 rule |

## 11. Raw component score breakdown before/after shadow gate

| case_id | before EPS/Vis/Bott/Mis/Val/Cap/Info | before label | after EPS/Vis/Bott/Mis/Val/Cap/Info | after label | reason |
|---|---|---|---|---|---|
| T1 S-OIL 2022 | 20/17/17/12/9/7/13 | Stage2-Actionable risk | 16/14/15/10/7/7/16 | Stage4B | inventory gain and peak-cycle evidence cap Green |
| T2 SK Innovation 2022 | 21/16/16/13/10/6/13 | Stage2-Actionable risk | 16/13/14/10/8/6/17 | Stage4B | record profit is trailing, not durability |
| T3 LX International | 22/20/15/13/12/7/12 | Stage3-Yellow | 22/22/15/12/11/7/13 | Stage3-Yellow | resource/logistics bridge validated |
| T4 TCC Steel | 23/19/16/14/12/5/12 | Stage3-Yellow | 22/22/16/12/11/5/13 | Stage3-Yellow | official IR + strong path validates specialty spread |
| T5 NI Steel | 21/17/12/15/11/5/8 | Stage2-Actionable | 20/18/11/13/10/5/9 | Stage2-Actionable | proxy-source cap prevents Green |
| T6 KG Steel | 18/12/10/14/9/6/14 | Stage2 risk | 12/10/8/10/6/6/20 | Stage4C | late-cycle profit + -45% MAE requires thesis-break route |
| T7 S-OIL 2024 | 10/14/13/10/10/6/13 | Stage4C risk | 11/16/13/9/9/6/15 | Stage4B | loss headline not structural break when rebound path validates |

## 12. Shadow rule candidate

```yaml
new_axis_proposed: C15_SPREAD_DURABILITY_INVENTORY_REVERSAL_GATE
axis_type: canonical_archetype_specific
production_scoring_changed: false
shadow_weight_only: true
rule_summary: >
  C15 positive stage should require a named spread cycle plus at least two of company-level demand/volume, product exposure,
  inventory/cost durability, margin/OP conversion, or cash/revision bridge. Trailing record profit, inventory gain, or generic
  commodity beta near a cycle peak should be capped at Stage4B watch. Escalate to hard 4C only when spread reversal is paired
  with company-level sustained margin collapse, inventory/cash break, or severe validated MAE without rebound evidence.
positive_gate:
  require_at_least_two:
    - named_spread_or_commodity_cycle
    - company_level_product_exposure
    - demand_or_volume_bridge
    - margin_or_operating_profit_conversion
    - inventory_or_cost_durability
    - cashflow_or_revision_bridge
4b_gate:
  trigger_when_any:
    - trailing_record_profit_without_forward_spread_durability
    - inventory_gain_dominated_result_near_cycle_peak
    - commodity_beta_or_sector_headline_without_company_bridge
    - local_peak_followed_by_deep_MAE
4c_gate:
  trigger_when_at_least_two:
    - sustained_margin_or_operating_profit_collapse
    - inventory_or_cost_reversal_confirmed
    - balance_sheet_or_cash_quality_break
    - forward_MAE90_or_MAE180_breaches_minus_25_pct
    - no_rebound_exception_or_policy_demand_offset
rebound_exception:
  keep_as_4B_not_4C_when:
    - loss_headline_is_inventory_or_margin_cycle_related
    - sector_margin_rebound_setup_exists
    - price_path_recovers_without_structural cash or solvency break
suggested_shadow_weight_delta:
  before: EPS/Vis/Bott/Mis/Val/Cap/Info = 20/12/20/10/10/8/20
  after:  EPS/Vis/Bott/Mis/Val/Cap/Info = 19/15/18/8/8/8/24
  delta:  -1/+3/-2/-2/-2/0/+4
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
  - information_confidence_gate
existing_axis_weakened: null
```

## 13. Residual contribution summary

```yaml
loop_contribution_label: C15_refining_steel_coal_spread_durability_quality_repair
residual_error_families:
  - trailing_record_profit_overcredit
  - inventory_gain_peak_cycle_false_positive
  - smallcap_specialty_spread_undercredit
  - refiner_loss_hard_4c_overblock
new_positive_patterns:
  - resource/logistics spread with company financial bridge
  - surface-treated steel margin bridge
  - small-cap steel leasing profit bridge with source-quality cap
new_counterexample_patterns:
  - refining inventory gain at cycle peak
  - record refining profit followed by high MAE
  - late steel profit/inventory reversal trap
batch_ingest_expected_use:
  - canonical_archetype_rule_candidate
  - C15 weight support
  - 4B/4C timing support
  - source_proxy repair queue
```

## 14. Batch Ingest Self-Audit

```yaml
filename_matches_required_regex: true
filename_round_matches_metadata_round: true
filename_loop_matches_metadata_loop: true
canonical_archetype_valid: true
large_sector_id_valid: true
round_sector_consistency: pass
trigger_type_values_are_canonical_stage_labels: true
all_trigger_rows_have_MFE_30D_pct: true
all_trigger_rows_have_MFE_90D_pct: true
all_trigger_rows_have_MFE_180D_pct: true
all_trigger_rows_have_MAE_30D_pct: true
all_trigger_rows_have_MAE_90D_pct: true
all_trigger_rows_have_MAE_180D_pct: true
rows_missing_required_mfe_mae: 0
source_proxy_only_count: 2
evidence_url_pending_count: 0
calibration_usable_trigger_count: 7
representative_trigger_candidate_count: 7
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 15. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not use this handoff as a standalone patch request. First run the v12 calibration ingest with --include-archive and include this MD. Parse all trigger JSONL rows, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family, and verify the six required MFE/MAE fields.

If the row set passes validation, evaluate the shadow rule candidate:
C15_SPREAD_DURABILITY_INVENTORY_REVERSAL_GATE.

Only implement if aggregate evidence across representative rows supports it. Keep production scoring conservative. Do not loosen Stage3-Green. Prefer a canonical-archetype runtime adjustment or guardrail note over a global rule.

Expected implementation intent:
- Increase C15 information-confidence / visibility importance when company-level spread-to-margin conversion is direct.
- Reduce valuation/mispricing credit for late-cycle record profit or generic commodity beta.
- Preserve hard 4C for confirmed inventory/cost/margin/cash break.
- Add 4B-not-4C exception for inventory-cycle loss headlines that rebound with evidence.
```

## 16. Next research state

```yaml
completed_round: R4
completed_loop: 105
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C15 spread reversal, refining/steel/coal inventory cycle, direct URL/proxy repair
next_recommended_archetypes:
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
