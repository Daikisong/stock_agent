# E2R Stock-Web v12 Residual Research — R6 / C21 Financial ROE-PBR Capital Return

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R6
selected_loop = 136
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C21 direct URL/proxy quality, capital-return execution vs value-up headline split, 4C-thin path repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_HOLDCO_VALUEUP_CET1_ROE_EXECUTION_GATE
output_filename = e2r_stock_web_v12_residual_round_R6_loop_136_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection / no-repeat rationale

The previous conversation run already covered C05, C01, C13, C15, C10, C02, C16, R13 high-MAE, C17, C07, C06, C14, C11, C12, C09, C03, C04, C08, C18, C19, and C20. This run therefore moves to R6 / L6 / C21. C21 is already well-covered by row count, so this is not row-filling. The purpose is quality repair: distinguish real capital-return execution from generic Korea Value-up / low-PBR sympathy, and add a thin 4C-style false-positive path.

Hard duplicate avoidance was applied at the level of `canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family`. The seven rows below use seven symbols and seven trigger families; no reused case is counted as new by convenience.

```text
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 7
calibration_usable_case_count = 7
calibration_usable_trigger_count = 7
positive_case_count = 4
counterexample_count = 3
stage4b_case_count = 2
stage4c_case_count = 1
source_proxy_only_count = 0
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
current_profile_error_count = 6
```

## 2. Price atlas validation basis

All OHLC calculations use Songdaiki/stock-web tradable symbol-year shards. The relevant manifest/schema basis used for this MD:

```text
source_name = FinanceData/marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
forward_windows = 30D, 90D, 180D tradable rows
```

No row below uses current/live prices beyond stock-web availability. All seven rows have at least 180 forward tradable rows and complete MFE/MAE fields.

## 3. Evidence source registry

| source | use |
|---|---|
| FSC Corporate Value-up Plan, 2024-08-01 | policy background only; not symbol-level evidence |
| KB Financial Group Form 6-K, 2024-10-24 | board-finalized sustainable value-up plan, ROE target, CET1 target, shareholder-return formula |
| Shinhan Financial Group 2024 Value-up Plan PDF | direct IR value-up material: ROE/ROTCE, CET1, tangible return, share-count reduction |
| Woori Financial Group Form 6-K / 2024 business report | C21 4C-style test: TSR target, CET1 tiers, later review and execution caveats |
| JB Financial Group EnglishDART value-up disclosure | high-ROE regional-bank positive template |
| KakaoBank IR value-up page + secondary detail | digital bank variant: return-ratio roadmap plus growth bridge |
| Meritz Financial Group shareholder return IR page | execution-heavy buyback/retirement positive template |

## 4. Trigger-level case table

| symbol | company | trigger | entry | trigger_type | entry_c | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | profile note |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 105560 | KB금융 | 2024-10-24 | 2024-10-25 | Stage4B | 101,000 | 2.87 | -15.05 | 2.87 | -24.36 | 20.79 | -31.39 | overpromote_direct_plan_without_drawdown_confirmation |
| 086790 | 하나금융지주 | 2024-10-30 | 2024-10-30 | Stage3-Yellow | 62,600 | 5.75 | -9.9 | 5.75 | -9.9 | 55.11 | -17.73 | too_late_after_capital_return_formula |
| 055550 | 신한지주 | 2024-07-26 | 2024-07-26 | Stage4B | 58,000 | 11.38 | -11.03 | 11.38 | -14.48 | 11.38 | -26.72 | overpromote_valueup_material_at_local_price_peak |
| 316140 | 우리금융지주 | 2024-07-25 | 2024-07-26 | Stage4C | 16,180 | 4.82 | -15.08 | 6.92 | -15.08 | 8.16 | -15.08 | false_positive_TSR_target_without_CET1_execution_visibility |
| 175330 | JB금융지주 | 2024-09-24 | 2024-09-24 | Stage3-Green | 15,560 | 20.24 | -4.76 | 31.75 | -4.76 | 43.32 | -4.76 | Green_late_for_high_ROE_capital_return_execution |
| 323410 | 카카오뱅크 | 2024-11-26 | 2024-11-26 | Stage3-Yellow | 21,750 | 15.4 | -4.14 | 17.01 | -8.97 | 78.16 | -8.97 | undercredit_when_return_policy_pairs_with_growth_bridge |
| 138040 | 메리츠금융지주 | 2024-02-22 | 2024-02-22 | Stage3-Green | 75,600 | 16.8 | -1.72 | 16.8 | -3.97 | 41.8 | -3.97 | Green_late_for_executed_buyback_retirement_structure |


## 5. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R6_L136_C21_001","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUEUP_CET1_ROE_EXECUTION_GATE","symbol":"105560","company_name":"KB금융","case_id":"C21_KBFG_20241024_SUSTAINABLE_VALUE_UP_HIGH_MAE","trigger_date":"2024-10-24","entry_date":"2024-10-25","entry_timing_rule":"after_close_or_publication_unclear_next_tradable_close","entry_price":101000.0,"entry_ohlcv":{"o":96000.0,"h":103900.0,"l":96000.0,"c":101000.0,"v":2817885},"trigger_type":"Stage4B","current_profile_stage":"Stage3-Yellow","proposed_stage":"Stage4B","evidence_family":"board-finalized value-up plan + ROE target + CET1-linked shareholder return formula","evidence_url":["https://www.sec.gov/Archives/edgar/data/1445930/000119312524242219/d901349d6k.htm"],"evidence_quality":"direct_company_SEC_6K","source_proxy_only":false,"calibration_usable":true,"corporate_action_contaminated_180D":false,"MFE_30D_pct":2.87,"MFE_90D_pct":2.87,"MFE_180D_pct":20.79,"MAE_30D_pct":-15.05,"MAE_90D_pct":-24.36,"MAE_180D_pct":-31.39,"peak_30D_date":"2024-10-25","trough_30D_date":"2024-12-05","peak_90D_date":"2024-10-25","trough_90D_date":"2025-03-05","peak_180D_date":"2025-07-08","trough_180D_date":"2025-04-09","peak_return_180D_pct":20.79,"max_drawdown_180D_pct":-31.39,"score_total_before":84.0,"score_total_after":80.0,"score_revision_after":48.0,"current_profile_error_type":"overpromote_direct_plan_without_drawdown_confirmation","same_entry_group_key":"C21_105560_2024-10-25_valueup_CET1_formula","representative_for_aggregate":true,"not_usable_for_promotion":false,"notes":"Direct policy bridge is real, but 30/90/180D MAE is too large for immediate Green; keep as 4B local risk until execution confirmation."}
{"row_type":"trigger","research_id":"R6_L136_C21_002","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUEUP_CET1_ROE_EXECUTION_GATE","symbol":"086790","company_name":"하나금융지주","case_id":"C21_HANA_20241030_VALUEUP_CET1_ROE_RIGHT_TAIL","trigger_date":"2024-10-30","entry_date":"2024-10-30","entry_timing_rule":"same_day_close_after_value_up_plan_publication","entry_price":62600.0,"entry_ohlcv":{"o":64000.0,"h":64400.0,"l":62400.0,"c":62600.0,"v":1778691},"trigger_type":"Stage3-Yellow","current_profile_stage":"Stage2-Actionable","proposed_stage":"Stage3-Yellow","evidence_family":"value-up plan + ROE/CET1 target + shareholder-return ratio roadmap","evidence_url":["https://www.hanafn.com:8002/eng/pr/ir/announcements.do","https://www.hanafn.com:8002/eng/main.do"],"evidence_quality":"direct_company_IR_with_secondary_crosscheck","source_proxy_only":false,"calibration_usable":true,"corporate_action_contaminated_180D":false,"MFE_30D_pct":5.75,"MFE_90D_pct":5.75,"MFE_180D_pct":55.11,"MAE_30D_pct":-9.9,"MAE_90D_pct":-9.9,"MAE_180D_pct":-17.73,"peak_30D_date":"2024-12-03","trough_30D_date":"2024-12-09","peak_90D_date":"2024-12-03","trough_90D_date":"2024-12-09","peak_180D_date":"2025-07-15","trough_180D_date":"2025-04-09","peak_return_180D_pct":55.11,"max_drawdown_180D_pct":-17.73,"score_total_before":81.5,"score_total_after":85.0,"score_revision_after":52.0,"current_profile_error_type":"too_late_after_capital_return_formula","same_entry_group_key":"C21_086790_2024-10-30_valueup_CET1_ROE","representative_for_aggregate":true,"not_usable_for_promotion":false,"notes":"Initial 30/90D MFE is modest, but 180D right-tail appears once CET1/ROE/shareholder-return bridge is accepted."}
{"row_type":"trigger","research_id":"R6_L136_C21_003","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUEUP_CET1_ROE_EXECUTION_GATE","symbol":"055550","company_name":"신한지주","case_id":"C21_SHINHAN_20240726_VALUEUP_PLAN_LATE_ENTRY_4B","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_timing_rule":"same_day_close_after_value_up_plan_material_publication","entry_price":58000.0,"entry_ohlcv":{"o":54200.0,"h":58400.0,"l":54200.0,"c":58000.0,"v":3558607},"trigger_type":"Stage4B","current_profile_stage":"Stage3-Yellow","proposed_stage":"Stage4B","evidence_family":"ROE/ROTCE improvement + CET1 stability + tangible shareholder return + share-count reduction","evidence_url":["https://shinhangroup.com/resources/publish/jp/resource/2024_Shinhan_Financial_Group_Value-up_Plan.pdf"],"evidence_quality":"direct_company_IR_PDF","source_proxy_only":false,"calibration_usable":true,"corporate_action_contaminated_180D":false,"MFE_30D_pct":11.38,"MFE_90D_pct":11.38,"MFE_180D_pct":11.38,"MAE_30D_pct":-11.03,"MAE_90D_pct":-14.48,"MAE_180D_pct":-26.72,"peak_30D_date":"2024-08-26","trough_30D_date":"2024-08-05","peak_90D_date":"2024-08-26","trough_90D_date":"2024-12-05","peak_180D_date":"2024-08-26","trough_180D_date":"2025-04-09","peak_return_180D_pct":11.38,"max_drawdown_180D_pct":-26.72,"score_total_before":82.0,"score_total_after":77.5,"score_revision_after":47.0,"current_profile_error_type":"overpromote_valueup_material_at_local_price_peak","same_entry_group_key":"C21_055550_2024-07-26_valueup_ROE_sharecount","representative_for_aggregate":true,"not_usable_for_promotion":false,"notes":"The evidence bridge is not fake, but the 180D return profile shows local 4B risk: value-up plan cannot override local price exhaustion."}
{"row_type":"trigger","research_id":"R6_L136_C21_004","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUEUP_CET1_ROE_EXECUTION_GATE","symbol":"316140","company_name":"우리금융지주","case_id":"C21_WOORI_20240725_TSR_TARGET_EXECUTION_GAP_4C","trigger_date":"2024-07-25","entry_date":"2024-07-26","entry_timing_rule":"next_tradable_or_same_session_close_after_CVE_plan_announcement","entry_price":16180.0,"entry_ohlcv":{"o":14810.0,"h":16230.0,"l":14800.0,"c":16180.0,"v":14562584},"trigger_type":"Stage4C","current_profile_stage":"Stage2-Actionable","proposed_stage":"Stage4C","evidence_family":"TSR 50% target + CET1 tiered shareholder return + future buyback/cancellation plan","evidence_url":["https://www.sec.gov/Archives/edgar/data/1264136/000119312525056088/d942209d6k.htm"],"evidence_quality":"direct_company_SEC_6K","source_proxy_only":false,"calibration_usable":true,"corporate_action_contaminated_180D":false,"MFE_30D_pct":4.82,"MFE_90D_pct":6.92,"MFE_180D_pct":8.16,"MAE_30D_pct":-15.08,"MAE_90D_pct":-15.08,"MAE_180D_pct":-15.08,"peak_30D_date":"2024-07-29","trough_30D_date":"2024-08-05","peak_90D_date":"2024-12-03","trough_90D_date":"2024-08-05","peak_180D_date":"2025-02-19","trough_180D_date":"2024-08-05","peak_return_180D_pct":8.16,"max_drawdown_180D_pct":-15.08,"score_total_before":78.0,"score_total_after":70.0,"score_revision_after":42.0,"current_profile_error_type":"false_positive_TSR_target_without_CET1_execution_visibility","same_entry_group_key":"C21_316140_2024-07-26_TSR_CET1_target","representative_for_aggregate":true,"not_usable_for_promotion":false,"notes":"A target TSR statement is insufficient when CET1 execution, asset-quality and integration/capital-allocation uncertainty keep the rerating bridge soft."}
{"row_type":"trigger","research_id":"R6_L136_C21_005","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_HIGH_ROE_VALUEUP_EXECUTION_GATE","symbol":"175330","company_name":"JB금융지주","case_id":"C21_JBFG_20240924_HIGH_ROE_VALUEUP_GREEN","trigger_date":"2024-09-24","entry_date":"2024-09-24","entry_timing_rule":"same_day_close_after_value_up_plan_disclosure","entry_price":15560.0,"entry_ohlcv":{"o":15120.0,"h":15800.0,"l":14950.0,"c":15560.0,"v":1679133},"trigger_type":"Stage3-Green","current_profile_stage":"Stage3-Yellow","proposed_stage":"Stage3-Green","evidence_family":"high ROE target + differentiated shareholder return + buyback/cancellation roadmap","evidence_url":["https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20240924800069"],"evidence_quality":"direct_regulatory_disclosure","source_proxy_only":false,"calibration_usable":true,"corporate_action_contaminated_180D":false,"MFE_30D_pct":20.24,"MFE_90D_pct":31.75,"MFE_180D_pct":43.32,"MAE_30D_pct":-4.76,"MAE_90D_pct":-4.76,"MAE_180D_pct":-4.76,"peak_30D_date":"2024-10-25","trough_30D_date":"2024-10-02","peak_90D_date":"2024-12-03","trough_90D_date":"2024-10-02","peak_180D_date":"2025-06-17","trough_180D_date":"2024-10-02","peak_return_180D_pct":43.32,"max_drawdown_180D_pct":-4.76,"score_total_before":85.0,"score_total_after":89.0,"score_revision_after":57.0,"current_profile_error_type":"Green_late_for_high_ROE_capital_return_execution","same_entry_group_key":"C21_175330_2024-09-24_high_ROE_valueup","representative_for_aggregate":true,"not_usable_for_promotion":false,"notes":"This is the clean C21 positive template: high ROE + explicit return roadmap + shallow MAE."}
{"row_type":"trigger","research_id":"R6_L136_C21_006","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_SHAREHOLDER_RETURN_PROFIT_GROWTH_GATE","symbol":"323410","company_name":"카카오뱅크","case_id":"C21_KAKAOBANK_20241126_SHAREHOLDER_RETURN_PLATFORM_BRIDGE","trigger_date":"2024-11-26","entry_date":"2024-11-26","entry_timing_rule":"same_day_close_after_value_up_plan_announcement","entry_price":21750.0,"entry_ohlcv":{"o":21500.0,"h":21800.0,"l":21500.0,"c":21750.0,"v":385976},"trigger_type":"Stage3-Yellow","current_profile_stage":"Stage2-Actionable","proposed_stage":"Stage3-Yellow","evidence_family":"shareholder return ratio roadmap + digital bank customer/platform revenue growth bridge","evidence_url":["https://www.kakaobank.com/IR/Archive/Valueup?lang=EN","https://www.mk.co.kr/en/economy/11178046"],"evidence_quality":"official_IR_page_plus_secondary_detail","source_proxy_only":false,"calibration_usable":true,"corporate_action_contaminated_180D":false,"MFE_30D_pct":15.4,"MFE_90D_pct":17.01,"MFE_180D_pct":78.16,"MAE_30D_pct":-4.14,"MAE_90D_pct":-8.97,"MAE_180D_pct":-8.97,"peak_30D_date":"2024-12-16","trough_30D_date":"2025-01-02","peak_90D_date":"2025-02-27","trough_90D_date":"2025-04-09","peak_180D_date":"2025-06-24","trough_180D_date":"2025-04-09","peak_return_180D_pct":78.16,"max_drawdown_180D_pct":-8.97,"score_total_before":82.0,"score_total_after":86.0,"score_revision_after":53.0,"current_profile_error_type":"undercredit_when_return_policy_pairs_with_growth_bridge","same_entry_group_key":"C21_323410_2024-11-26_digital_bank_valueup","representative_for_aggregate":true,"not_usable_for_promotion":false,"notes":"Not a classic low-PBR bank, but the return-ratio roadmap plus platform growth bridge keeps it within C21 rather than generic digital-bank beta."}
{"row_type":"trigger","research_id":"R6_L136_C21_007","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"FINANCIAL_HOLDCO_BUYBACK_RETIREMENT_EXECUTION_GATE","symbol":"138040","company_name":"메리츠금융지주","case_id":"C21_MERITZ_20240222_BUYBACK_RETIREMENT_CAPITAL_RETURN_GREEN","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_timing_rule":"same_day_close_after_shareholder_return_disclosure_window","entry_price":75600.0,"entry_ohlcv":{"o":75900.0,"h":76200.0,"l":74300.0,"c":75600.0,"v":272501},"trigger_type":"Stage3-Green","current_profile_stage":"Stage3-Yellow","proposed_stage":"Stage3-Green","evidence_family":"buyback/retirement structure + shareholder return page + financial holding capital allocation","evidence_url":["https://m.meritzgroup.com/mo/en/ir/ir3.do"],"evidence_quality":"direct_company_IR_shareholder_return","source_proxy_only":false,"calibration_usable":true,"corporate_action_contaminated_180D":false,"MFE_30D_pct":16.8,"MFE_90D_pct":16.8,"MFE_180D_pct":41.8,"MAE_30D_pct":-1.72,"MAE_90D_pct":-3.97,"MAE_180D_pct":-3.97,"peak_30D_date":"2024-03-15","trough_30D_date":"2024-02-22","peak_90D_date":"2024-03-15","trough_90D_date":"2024-04-18","peak_180D_date":"2024-10-21","trough_180D_date":"2024-04-18","peak_return_180D_pct":41.8,"max_drawdown_180D_pct":-3.97,"score_total_before":86.0,"score_total_after":90.0,"score_revision_after":58.0,"current_profile_error_type":"Green_late_for_executed_buyback_retirement_structure","same_entry_group_key":"C21_138040_2024-02-22_buyback_retirement","representative_for_aggregate":true,"not_usable_for_promotion":false,"notes":"Clean execution-heavy capital-return positive: shallow MAE and persistent 180D right-tail."}
```

## 6. Current profile stress test

C21 already has a capital-return tilt in the runtime weight table, but this run shows that the current profile can still confuse three different things:

1. **real formulaic capital return**: JB금융지주 and 메리츠금융지주 show strong MFE with shallow MAE when high ROE / buyback / cancellation / shareholder-return execution is explicit.
2. **real plan but local 4B risk**: KB금융 and 신한지주 have direct Value-up evidence, but the entry was too close to a local price peak or followed by deep macro/bank-sector drawdown. These should not be immediate Green.
3. **aspirational TSR / future CET1 execution gap**: 우리금융지주 shows why a TSR target or CET1 tier table alone is not enough when execution is not yet visible in price-return alignment.

### Raw component weight stress test

Current C21 runtime weights from the no-repeat table are `15/20/5/15/25/15/5` in `EPS/Vis/Bott/Mis/Val/Cap/Info` order. Suggested shadow-only repair:

| component | before_weight | after_shadow_weight | reason |
|---|---:|---:|---|
| EPS/FCF | 15 | 14 | bank value-up needs less pure EPS beta and more capital-return execution |
| Visibility | 20 | 21 | CET1/ROE/TSR formulas increase visibility only when board-approved and dated |
| Bottleneck/Pricing | 5 | 5 | not a bottleneck archetype |
| Mispricing | 15 | 13 | low PBR/value-up headline alone overpromotes local peaks |
| Valuation rerating | 25 | 25 | remains core C21 axis, but not sufficient alone |
| Capital allocation | 15 | 17 | buyback/cancellation/dividend formula deserves higher weight |
| Information confidence | 5 | 5 | no broad change; source quality still handled by hard gate |


```text
new_axis_proposed = C21_CAPITAL_RETURN_EXECUTION_CET1_ROE_GATE
suggested_shadow_weight_delta_before = 15/20/5/15/25/15/5
suggested_shadow_weight_delta_after  = 14/21/5/13/25/17/5
suggested_shadow_weight_delta        = -1/+1/0/-2/0/+2/0
```

## 7. Rule candidate

C21 should **not** open Stage3-Green on `Value-up`, `low PBR`, `bank beta`, or `shareholder return target` alone. Require at least two of the following before Stage2-Actionable / Stage3-Yellow, and at least three plus benign drawdown for Stage3-Green:

```text
required_bridge_candidates:
  - sustainable ROE / ROTCE target or recent realized ROE support
  - CET1 already above the stated shareholder-return threshold, not merely targeted
  - board-approved buyback/cancellation or dividend formula with dated execution
  - total share count / TBPS / DPS visibility improving per-share economics
  - asset-quality / provisioning / acquisition / capital-allocation risks not worsening
  - official company or regulatory disclosure, not just policy sympathy
```

Hard 4B / 4C routing:

```text
if evidence == generic_policy_valueup_or_low_PBR_only:
  cap_stage = Stage2 or Watch

if shareholder_return_target_exists and CET1_execution_visibility_missing:
  cap_stage = Stage4B_or_Stage4C_depending_on_forward_price_and_asset_quality

if direct_valueup_plan_exists but MAE_90D <= -20% or MAE_180D <= -25%:
  block_Green_until_execution_confirmation = true

if buyback_cancellation_is_board_approved and ROE/CET1 bridge is present and MAE remains shallow:
  allow_Stage3_Green = true
```

## 8. Residual contribution summary

```text
diversity_score_summary = 7 symbols / 7 trigger families / 4 positives / 3 counterexamples / 2 Stage4B / 1 Stage4C
sector_specific_rule_candidate = L6 financial capital-return rerating requires execution bridge, not just policy beta.
canonical_archetype_rule_candidate = C21 requires ROE-CET1-capital-return execution gate before Green.
loop_contribution_label = C21_capital_return_execution_vs_valueup_headline_quality_repair
existing_axis_strengthened = stage2_required_bridge; local_4b_watch_guard; hard_4c_confirmation; drawdown_aware_confirmation
existing_axis_weakened = generic_mispricing_beta_overcredit
production_scoring_changed = false
shadow_weight_only = true
```

## 9. Validation self-audit

```text
must_use_actual_stock_web_1D_OHLC = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
trigger_rows_missing_required_price_fields_are_forbidden = pass
trigger_type_must_be_canonical_stage_label = pass
source_proxy_only_count = 0
evidence_url_pending_count = 0
same_entry_group_deduped = pass
corporate_action_contamination_checked = no overlap flagged in local Stock-Web tradable windows used here
calibration_usable_rows = 7
not_usable_for_promotion_rows = 0
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research run.

Task: ingest this standalone v12 residual MD together with the full docs/round corpus. Validate filename/metadata consistency, parse trigger JSONL, enforce complete MFE/MAE 30/90/180D fields, dedupe same_entry_group_key, and evaluate a shadow-only C21 rule candidate.

Candidate axis:
  axis_id = C21_CAPITAL_RETURN_EXECUTION_CET1_ROE_GATE
  affected_scope = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL

Patch hypothesis:
  - Do not allow C21 Stage3-Green on generic Korea Value-up / low-PBR / policy beta alone.
  - Require at least two of ROE/ROTCE durability, CET1 above threshold, board-approved buyback/cancellation/dividend formula, per-share metric improvement, and benign asset-quality/capital-allocation risk for Stage2-Actionable.
  - Require at least three plus drawdown-aware confirmation for Stage3-Green.
  - Route target-only shareholder-return plans with weak CET1/execution visibility to Stage4B/Stage4C watch.

Suggested weights:
  before = 15/20/5/15/25/15/5
  after  = 14/21/5/13/25/17/5
  delta  = -1/+1/0/-2/0/+2/0

Do not change production scoring until batch validation confirms positive/counterexample balance and rejects source-proxy-only rows.
```

## 11. Next research state

```text
completed_round = R6
completed_loop = 136
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C21 direct URL/proxy quality, capital-return execution vs value-up headline split, 4C-thin path repair
next_recommended_archetypes = C22_INSURANCE_RATE_CYCLE_RESERVE; C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION; C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE; C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
