# E2R Stock-Web V12 Residual Research — R13 Accounting / Trust / Price Validation

```text
MD filename: e2r_stock_web_v12_residual_round_R13_loop_152_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md
selected_round: R13
selected_loop: 152
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: R13 special scope / cross-archetype accounting trust price validation after repeated Priority-0/1 sector follow-ups
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE
loop_objective: holdout_validation | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

This loop intentionally uses the R13 special scope rather than another sector-specific C02/C09/C14 follow-up. The remote No-Repeat Index still shows large source-quality debt: `source_proxy_only_count=1340`, `evidence_url_pending_count=1506`, and `current_profile_false_positive_count=598`. The prior local sequence already added many Priority 0/1 follow-ups, so this checkpoint tests whether selected rows should be treated as normal trigger rows, hard 4C, soft 4B, official-source positive controls, or narrative-only price-validation blocks.

R13 is valid here because the target is not a new C01~C32 sector positive. It is a cross-archetype audit of accounting/trust events, allegation-only events, fixable regulatory CRLs, official filings, trading halts, and stock-web raw price-row eligibility.

## 2. Stock-Web price source validation

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_data_repo: https://github.com/Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

All usable trigger rows below use entry-date close `c` from stock-web tradable shards and include the required 30D/90D/180D MFE·MAE fields. Osstem Implant is deliberately written as `narrative_only`, because its immediate event date was a trading suspension and the next tradable row cannot represent a normal next-trading-day entry.

## 3. Trigger summary table

|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|current_profile_verdict|case_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|006360|GS건설|Stage4C|2023-08-28|2023-08-28|14480.0|3.38|20.17|20.17|-12.5|-12.5|-12.5|current_profile_4C_too_late|trust_break_hard_4c|
|294870|HDC현대산업개발|Stage4C|2022-01-17|2022-01-17|18750.0|5.6|5.6|5.6|-28.0|-29.87|-45.33|current_profile_correct|trust_break_hard_4c|
|035720|카카오|Stage4B|2024-07-23|2024-07-23|38850.0|6.69|21.24|21.24|-9.01|-16.22|-16.22|current_profile_4C_too_early|governance_regulatory_overhang_severity_split|
|028300|HLB|Stage4B|2024-05-17|2024-05-17|67100.0|9.99|46.2|46.2|-32.71|-32.71|-32.71|current_profile_4C_too_early|regulatory_crl_severity_split|
|005930|삼성전자|Stage4B|2024-05-24|2024-05-24|75900.0|14.76|17.0|17.0|-3.16|-21.61|-34.26|current_profile_correct|source_conflict_and_scope_validation|
|105560|KB금융|Stage2-Actionable|2024-02-07|2024-02-07|64700.0|21.48|28.9|60.59|-7.73|-7.73|-7.73|current_profile_correct|official_filing_positive_validation_control|
|086790|하나금융지주|Stage2-Actionable|2024-10-29|2024-10-29|65000.0|3.85|3.85|49.38|-13.23|-13.23|-20.77|current_profile_too_late|official_valueup_positive_validation_control|


## 4. Case findings

### 4.1 Hard trust-break controls: C30 construction safety/trust breaks

GS E&C and HDC Hyundai Development show why R13 needs a separate trust gate. A construction safety/trust break is not merely a low-PBR or sector-beta drawdown. It damages the evidence substrate itself: project quality, regulatory eligibility, future orders, cost provisions, and brand trust. HDC's row is the cleaner hard-4C control because the 180D path has only 5.6% MFE and -45.33% MAE. GS E&C is more subtle: the later MFE recovered to 19.83%, so the correct rule is not automatic permanent sell, but earlier hard trust watch with evidence-based 4C routing.

### 4.2 Allegation-only / disputed-source severity split

Kakao and Samsung Electronics prove that source trust is not binary. Kakao founder arrest and Samsung HBM qualification reports were high-quality public evidence, but the right route is Stage4B unless the non-price thesis break becomes final and durable. Kakao later had meaningful 90D/180D MFE from the entry date, and Samsung's HBM article was explicitly disputed by the company. These rows strengthen the rule: **accusation, report, denial, or incomplete qualification cannot be treated as hard 4C unless the business thesis is actually broken.**

### 4.3 Fixable regulatory CRL split

HLB's FDA CRL is a strong binary risk row, but not all CRLs are equal. If the CRL points to fixable CMC/BIMO/site-inspection issues rather than clinical efficacy collapse, R13 should route it as Stage4B or severity-split 4C, not as an irreversible hard 4C. The stock path validates risk because MAE_30D is -32.71%, but the later 90D/180D MFE of 46.20% warns against permanent thesis-break labeling without the clinical thesis being broken.

### 4.4 Official filing positive controls

KB Financial and Hana Financial are positive controls for source validation. Official filing / official Value-Up Plan evidence can support Stage2-Actionable when it contains board-approved buyback/cancellation, capital-return route, or CET1/TSR mechanics. Their price paths also validate that official capital-return evidence is not merely a policy headline: KB's 180D MFE was 60.59%, and Hana's 180D MFE was 49.38% after the official plan date. The guardrail is that both still need staged entry and local 4B/profit-lock overlays after fast reprice.

### 4.5 Trading-halt and delisting route block

Osstem Implant is intentionally not emitted as a trigger row. The W188B embezzlement event led to trading suspension, and the first next tradable row came months later. That later row mixes trust break, suspension review, rescue expectations, and eventual tender/delisting dynamics. R13 should teach the batch ingest not to force an ordinary MFE/MAE trigger row through a trading-halt gap.

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R13_152_01","case_id":"R13_ATPV_001","symbol":"006360","company_name":"GS건설","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4C","trigger_date":"2023-08-28","evidence_available_at_that_date":true,"evidence_source":"Yonhap, 2023-08-27, land ministry seeks 10-month business suspension for GS E&C over Geomdan parking garage collapse; BusinessKorea, 2023-05-10, missing rebars reported","evidence_source_url":"https://en.yna.co.kr/view/AEN20230827002451320","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal/regulatory business suspension risk","quality trust break"],"stage4c_evidence_fields":["safety/quality trust break","business suspension proposal","rebar omission/collapse"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-28","entry_price":14480.0,"MFE_30D_pct":3.38,"MFE_90D_pct":20.17,"MFE_180D_pct":20.17,"MFE_1Y_pct":50.21,"MFE_2Y_pct":null,"MAE_30D_pct":-12.5,"MAE_90D_pct":-12.5,"MAE_180D_pct":-12.5,"MAE_1Y_pct":-12.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-23","peak_price":17400.0,"drawdown_after_peak_pct":-20.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"computed_qualitatively","four_b_full_window_peak_proximity":"computed_qualitatively","four_b_timing_verdict":"hard_4C_or_trust_break_guard","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"hard_4C","trigger_outcome_label":"geomdan_missing_rebar_business_suspension_trust_break","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|006360|2023-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"trust_break_hard_4c","price_note":"Entry uses next tradable date after Sunday ministry announcement."}
{"row_type":"trigger","trigger_id":"R13_152_02","case_id":"R13_ATPV_002","symbol":"294870","company_name":"HDC현대산업개발","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4C","trigger_date":"2022-01-17","evidence_available_at_that_date":true,"evidence_source":"Reuters, 2022-01-17, HDC chairman steps down after apartment complex collapse","evidence_source_url":"https://www.reuters.com/world/asia-pacific/skorea-builder-hdcs-chairman-steps-down-after-apartment-complex-collapse-2022-01-17/","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["safety incident overhang","licence/regulatory risk"],"stage4c_evidence_fields":["fatal construction-site collapse","management accountability","repeated safety trust break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-17","entry_price":18750.0,"MFE_30D_pct":5.6,"MFE_90D_pct":5.6,"MFE_180D_pct":5.6,"MFE_1Y_pct":5.6,"MFE_2Y_pct":null,"MAE_30D_pct":-28.0,"MAE_90D_pct":-29.87,"MAE_180D_pct":-45.33,"MAE_1Y_pct":-50.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-17","peak_price":19800.0,"drawdown_after_peak_pct":-48.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"computed_qualitatively","four_b_full_window_peak_proximity":"computed_qualitatively","four_b_timing_verdict":"hard_4C_or_trust_break_guard","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"hard_4C","trigger_outcome_label":"gwangju_apartment_collapse_management_resignation_trust_break","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|294870|2022-01-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"trust_break_hard_4c","price_note":"Clean 180D window; peak already on entry day."}
{"row_type":"trigger","trigger_id":"R13_152_03","case_id":"R13_ATPV_003","symbol":"035720","company_name":"카카오","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4B","trigger_date":"2024-07-23","evidence_available_at_that_date":true,"evidence_source":"Reuters, 2024-07-23, Kakao founder arrested for suspected stock manipulation; later legal outcomes require severity split","evidence_source_url":"https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["founder arrest","regulatory scrutiny","governance overhang"],"stage4c_evidence_fields":["only if conviction/control loss/regulatory forced business break is confirmed"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-23","entry_price":38850.0,"MFE_30D_pct":6.69,"MFE_90D_pct":21.24,"MFE_180D_pct":21.24,"MFE_1Y_pct":84.3,"MFE_2Y_pct":null,"MAE_30D_pct":-9.01,"MAE_90D_pct":-16.22,"MAE_180D_pct":-16.22,"MAE_1Y_pct":-16.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-04","peak_price":47100.0,"drawdown_after_peak_pct":-24.2,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"computed_qualitatively","four_b_full_window_peak_proximity":"computed_qualitatively","four_b_timing_verdict":"4B_watch_or_profit_lock_required","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"4C_severity_split_do_not_overkill","trigger_outcome_label":"founder_arrest_stock_manipulation_allegation_but_hard4c_overkill","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"minor_share_count_change; profile corporate_action_candidates are outside 180D trigger window","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|035720|2024-07-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"governance_regulatory_overhang_severity_split","price_note":"Stage4B watch row: price later had MFE, so hard 4C purely on allegation would overkill."}
{"row_type":"trigger","trigger_id":"R13_152_04","case_id":"R13_ATPV_004","symbol":"028300","company_name":"HLB","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION / C24_BIO_TRIAL_DATA_EVENT_RISK","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4B","trigger_date":"2024-05-17","evidence_available_at_that_date":true,"evidence_source":"Korea Times/KED/BioWorld, 2024-05-17, FDA CRL/rejection for rivoceranib+camrelizumab; issue framed around CMC/inspection rather than pure clinical failure","evidence_source_url":"https://www.koreatimes.co.kr/business/companies/20240517/south-korean-drugmaker-hlb-hit-by-us-fdas-rejection-of-rivoceranib-liver-cancer-drug","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["FDA CRL","binary regulatory event","manufacturing/inspection gap"],"stage4c_evidence_fields":["only if clinical efficacy or repeated unfixable regulatory thesis break is confirmed"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100.0,"MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":46.2,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":-32.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100.0,"drawdown_after_peak_pct":-40.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"computed_qualitatively","four_b_full_window_peak_proximity":"computed_qualitatively","four_b_timing_verdict":"4B_watch_or_profit_lock_required","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"4C_severity_split_do_not_overkill","trigger_outcome_label":"fda_crl_fixable_cmc_bimo_vs_clinical_thesis_break_split","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"minor_share_count_change; profile corporate_action_candidates are outside 180D trigger window","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|028300|2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"regulatory_crl_severity_split","price_note":"Large MAE validates risk, but MFE recovery means immediate permanent 4C is too coarse."}
{"row_type":"trigger","trigger_id":"R13_152_05","case_id":"R13_ATPV_005","symbol":"005930","company_name":"삼성전자","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage4B","trigger_date":"2024-05-24","evidence_available_at_that_date":true,"evidence_source":"Reuters, 2024-05-23/24, Samsung HBM chips reportedly failing Nvidia tests; Samsung disputed heat/power claims","evidence_source_url":"https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["customer qualification uncertainty","source-conflict risk","HBM share-lag risk"],"stage4c_evidence_fields":["only if named-customer qualification failure becomes persistent confirmed thesis break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-24","entry_price":75900.0,"MFE_30D_pct":14.76,"MFE_90D_pct":17.0,"MFE_180D_pct":17.0,"MFE_1Y_pct":17.0,"MFE_2Y_pct":null,"MAE_30D_pct":-3.16,"MAE_90D_pct":-21.61,"MAE_180D_pct":-34.26,"MAE_1Y_pct":-34.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800.0,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"computed_qualitatively","four_b_full_window_peak_proximity":"computed_qualitatively","four_b_timing_verdict":"4B_watch_or_profit_lock_required","four_b_evidence_type":"non_price_evidence","four_c_protection_label":"4C_severity_split_do_not_overkill","trigger_outcome_label":"hbm_nvidia_qualification_report_denial_stage4b_not_hard4c","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"profile_clean_or_no_profile_candidate_overlap_180D","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005930|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"source_conflict_and_scope_validation","price_note":"Clean price row; Stage4B is the right severity because evidence was disputed and broader memory business remained."}
{"row_type":"trigger","trigger_id":"R13_152_06","case_id":"R13_ATPV_006","symbol":"105560","company_name":"KB금융","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","evidence_available_at_that_date":true,"evidence_source":"SEC 6-K filed 2024-05-16 states Feb. 7, 2024 board resolved W320B treasury share acquisition/cancellation","evidence_source_url":"https://www.sec.gov/Archives/edgar/data/1445930/000119312524139928/d830917d6k.htm","stage2_evidence_fields":["official filing","board-approved buyback/cancellation","capital return bridge"],"stage3_evidence_fields":["CET1/shareholder return visibility","subsequent price alignment"],"stage4b_evidence_fields":["fast low-PBR/value-up reprice later needs local 4B"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-07","entry_price":64700.0,"MFE_30D_pct":21.48,"MFE_90D_pct":28.9,"MFE_180D_pct":60.59,"MFE_1Y_pct":60.59,"MFE_2Y_pct":null,"MAE_30D_pct":-7.73,"MAE_90D_pct":-7.73,"MAE_180D_pct":-7.73,"MAE_1Y_pct":-7.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900.0,"drawdown_after_peak_pct":-14.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"computed_qualitatively","four_b_full_window_peak_proximity":"computed_qualitatively","four_b_timing_verdict":"4B_watch_or_profit_lock_required","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"kb_financial_sec_6k_buyback_cancellation_official_source_positive_control","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"shares_changed_due_to_buyback_execution_not_price_adjustment; profile_overlap_not_used_as_block","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|105560|2024-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"official_filing_positive_validation_control","price_note":"Share-count decline is expected capital-return execution, not an OHLC adjustment contamination."}
{"row_type":"trigger","trigger_id":"R13_152_07","case_id":"R13_ATPV_007","symbol":"086790","company_name":"하나금융지주","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE","sector":"cross_archetype_accounting_trust_price_validation","primary_archetype":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","loop_objective":["holdout_validation","source_proxy_replacement","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","canonical_archetype_compression"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-10-29","evidence_available_at_that_date":true,"evidence_source":"Hana Financial official Value Up Plan page, 2024-10-29 plan; later W400B buyback/cancellation confirms execution route","evidence_source_url":"https://www.hanafn.com/en/hfm/mnu/ir/valueupplan.do","stage2_evidence_fields":["official value-up plan","capital return framework","CET1/TSR route"],"stage3_evidence_fields":["later buyback/cancellation execution","record earnings support"],"stage4b_evidence_fields":["early MAE/staged entry needed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-29","entry_price":65000.0,"MFE_30D_pct":3.85,"MFE_90D_pct":3.85,"MFE_180D_pct":49.38,"MFE_1Y_pct":55.54,"MFE_2Y_pct":null,"MAE_30D_pct":-13.23,"MAE_90D_pct":-13.23,"MAE_180D_pct":-20.77,"MAE_1Y_pct":-20.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-15","peak_price":97100.0,"drawdown_after_peak_pct":-7.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"computed_qualitatively","four_b_full_window_peak_proximity":"computed_qualitatively","four_b_timing_verdict":"4B_watch_or_profit_lock_required","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"hana_valueup_plan_official_source_stage2_actionable_control","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"minor_share_count_change; no raw OHLC discontinuity in 180D window","same_entry_group_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|086790|2024-10-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_role":"official_valueup_positive_validation_control","price_note":"Official source validates Stage2, but first 90D path had drawdown; staged entry is required."}
```

## 6. Narrative-only / blocked row JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R13_ATPV_008","symbol":"048260","company_name":"오스템임플란트","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CROSS_ARCHETYPE_SOURCE_TRUST_ACCOUNTING_EVENT_AND_PRICE_ROW_VALIDATION_GATE","primary_archetype":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / R13_PRICE_VALIDATION","trigger_type":"Stage4C","trigger_date":"2022-01-03","evidence_source":"Yonhap/Korea JoongAng/Korea Times, Jan. 2022, W188B embezzlement and trading suspension/delisting review","evidence_source_url":"https://en.yna.co.kr/view/AEN20220105006051320","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","would_be_next_tradable_entry_date":"2022-04-28","would_be_entry_price":112000.0,"calibration_usable":false,"calibration_block_reasons":["evidence-date trading halt: next tradable row occurs after long suspension, so immediate event impact cannot be represented as normal next-day entry","profile latest tradable date 2023-08-11 after tender/delisting route; representative trigger would mix trust break, suspension, and deal-premium paths"],"profile_path":"atlas/symbol_profiles/048/048260.json","profile_status":"inactive_or_delisted_like","corporate_action_window_status":"trading_suspension_and_later_delisting/tender_path; narrative_only","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"reuse_reason":"none","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"trigger_outcome_label":"osstem_embezzlement_trading_halt_price_validation_block","current_profile_verdict":"current_profile_data_insufficient"}
```

## 7. Aggregate / shadow / residual rows JSONL

```jsonl
{"row_type":"aggregate","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","usable_trigger_count":7,"representative_trigger_count":7,"narrative_only_or_rejected_count":1,"positive_case_count":2,"counterexample_count":5,"stage4b_case_count":3,"stage4c_case_count":2,"current_profile_error_count":5,"avg_MFE_90D_pct":20.42,"avg_MAE_90D_pct":-19.12,"rule_candidate":"R13_SOURCE_TRUST_PRICE_ROW_GATE_WITH_TRADING_HALT_AND_SEVERITY_SPLIT"}
{"row_type":"shadow_weight","round":"R13","loop":152,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","new_axis_proposed":"R13_SOURCE_TRUST_PRICE_ROW_GATE_WITH_TRADING_HALT_AND_SEVERITY_SPLIT","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c"],"existing_axis_weakened":["hard_4c should not fire on allegation-only or fixable CRL without confirmed permanent thesis break"],"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","round":"R13","loop":152,"loop_contribution_label":"residual_error_found","residual_summary":"Adds source trust and price-row validation gate: official filing positive controls, safety/trust hard 4C controls, allegation-only/CRL severity split, and trading-halt narrative-only blocking.","new_independent_case_count":7,"reused_case_count":0,"do_not_propose_new_weight_delta":false}
```

## 8. Current calibrated profile stress test

```text
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
```

| test item | result |
|---|---|
| Stage2 actionable bonus | Correct for official filing / official value-up controls; unsafe for allegation-only or source-proxy rows. |
| Yellow threshold 75 | Not the main problem here; source/trust validity dominates threshold tuning. |
| Green threshold 87 / revision 55 | Should remain strict; none of the soft allegation/CRL rows should become Green from price recovery alone. |
| price-only blowoff guard | Kept. This loop adds a source/trust companion guard. |
| full 4B non-price requirement | Strengthened. Stage4B must identify the non-price overhang class: allegation, qualification uncertainty, CRL, trading halt, trust break. |
| hard 4C routing | Strengthened for safety/trust breaks; weakened for allegation-only and fixable CRL rows. |

## 9. Proposed R13 shadow rule

```text
new_axis_proposed:
R13_SOURCE_TRUST_PRICE_ROW_GATE_WITH_TRADING_HALT_AND_SEVERITY_SPLIT
```

Rule draft:

```text
1. If evidence is an official filing, board resolution, regulator/FDA notice, or exchange filing and price rows are clean, source_trust_score may support Stage2-Actionable.
2. If evidence is allegation-only, investigative arrest, disputed qualification report, or source-conflicted press item, cap at Stage4B unless a durable non-price thesis break is confirmed.
3. If evidence is a safety/accounting/trust break with regulatory/business suspension or repeated quality failure, hard 4C is allowed even if price later bounces.
4. If evidence date is a trading halt and the next tradable row is months later, do not emit a trigger row; emit narrative_only or blocked validation row.
5. If a CRL or regulatory rejection is fixable CMC/BIMO/site-inspection rather than clinical/efficacy failure, use 4B severity split or decay/reopen watch; do not force permanent hard 4C.
```

## 10. Residual contribution summary

```text
This loop adds 7 new independent usable trigger cases, 5 counterexample/guardrail cases, and 5 residual errors for R13/L10/R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION.
loop_contribution_label: residual_error_found
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: R13_SOURCE_TRUST_PRICE_ROW_GATE_WITH_TRADING_HALT_AND_SEVERITY_SPLIT
do_not_propose_new_weight_delta: false
```

The residual error is not that the global profile lacks a generic 4B/4C rule. The residual error is that evidence trust level and price-row eligibility are still too easy to flatten. A verified official filing, a safety trust break, a disputed press report, a fixable FDA CRL, and a trading halt all need different routing even if their price charts look similarly violent.

## 11. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research loop.

When batch-applying this MD later, ingest the trigger rows only if filename, round, loop, large_sector_id, canonical_archetype_id, entry_date, entry_price, trigger_type, and all six required MFE/MAE fields pass validation. Add or test an R13-only shadow gate named R13_SOURCE_TRUST_PRICE_ROW_GATE_WITH_TRADING_HALT_AND_SEVERITY_SPLIT. The gate should not alter production scoring immediately. It should classify official filing positive controls, allegation-only Stage4B rows, hard safety/accounting trust 4C rows, fixable CRL severity-split rows, and trading-halt narrative-only rows. Do not convert the Osstem narrative-only row into a representative trigger unless a separate trading-halt methodology is implemented.
```

## 13. Next research state

```text
completed_round = R13
completed_loop = 152
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = R13 special scope / accounting trust price validation
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes =
  - C02_POWER_GRID_DATACENTER_CAPEX_followup_new_symbols_only
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_followup_after_shard_recheck
  - C14_EV_DEMAND_SLOWDOWN_4B_4C_followup_utilization_regime
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_followup_new_symbols_only
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_if_source_proxy_debt_persists
```
