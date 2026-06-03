# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R13
scheduled_loop = 72
completed_round = R13
completed_loop = 72
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id = CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL
output_file = e2r_stock_web_v12_residual_round_R13_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

One-line contribution: This loop adds 8 new independent cases, 5 counterexamples, and 7 residual errors for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/R13_CROSS_ARCHETYPE_4B_4C_REDTEAM.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

R13 does not re-propose these axes as production changes. It stress-tests their residual edge across C31 policy-event and C32 governance/control-premium event paths. The common mechanism is an event flare: price can run first, but only a conversion bridge keeps the flame from becoming smoke.

## 2. Round / Large Sector / Canonical Archetype Scope

|Field|Value|
|---|---|
|scheduled_round|R13|
|scheduled_loop|72|
|large_sector_id|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|
|canonical_archetype_id|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|
|fine_archetype_id|CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL|
|round_schedule_status|valid|
|round_sector_consistency|pass|
|loop_objective|residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill|

R13 special scope used here:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

This file is not a normal sector research file. It is a cross-archetype checkpoint joining C31 and C32 residuals so that policy-only themes, governance-only events, and legal/tender/control-close paths can be compared under one guardrail lens.

## 3. Previous Coverage / Duplicate Avoidance Check

No `stock_agent` source code was opened or inferred. Duplicate avoidance used local v12 research outputs already present in `/mnt/data` plus the standing hard key:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

The previous completed file was R12/Loop 72/C32, whose next state was R13/Loop 72. R13/Loop 71 already covered HDC, GS, SM, YTN, Korea Zinc, and Hanmi Science. This R13/Loop 72 set avoids those R13 symbols and uses C31/C32 cases not previously used under the R13 special canonical scope.

|R13 case_id|Source case|Source canonical|Symbol|Entry|Duplicate status|Novelty reason|
|---|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|C31_034020_2025_WESTINGHOUSE_REENTRY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|034020|2025-01-17|non-duplicate in R13 scope|new R13 special-scope comparator|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|C31_052690_2025_WESTINGHOUSE_REENTRY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|052690|2025-01-17|non-duplicate in R13 scope|new R13 special-scope comparator|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|006910|2022-03-10|non-duplicate in R13 scope|new R13 special-scope comparator|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|C31_013990_2024_LOW_BIRTH_POLICY_THEME|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|013990|2024-01-03|non-duplicate in R13 scope|new R13 special-scope comparator|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|180640|2020-02-26|non-duplicate in R13 scope|new R13 special-scope comparator|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|011780|2021-01-27|non-duplicate in R13 scope|new R13 special-scope comparator|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|000990|2023-03-31|non-duplicate in R13 scope|new R13 special-scope comparator|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|003920|2021-05-28|non-duplicate in R13 scope|new R13 special-scope comparator|

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest and schema checked from `Songdaiki/stock-web`.

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema check:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

|case_id|symbol|price_shard_path|entry_date|forward window|corporate action status|calibration_usable|
|---|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|034020|atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv|2025-01-17|>=180 trading days|clean_180D_window|True|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|052690|atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv|2025-01-17|>=180 trading days|clean_180D_window|True|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|006910|atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv|2022-03-10|>=180 trading days|clean_180D_window|True|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|013990|atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv|2024-01-03|>=180 trading days|clean_180D_window|True|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|180640|atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv|2020-02-26|>=180 trading days|clean_180D_window|True|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|011780|atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv|2021-01-27|>=180 trading days|clean_180D_window|True|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|000990|atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv|2023-03-31|>=180 trading days|clean_180D_window|True|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|003920|atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv; atlas/ohlcv_tradable_by_symbol_year/003/003920/2022.csv|2021-05-28|>=180 trading days|clean_180D_window|True|

All representative rows use stock-web tradable shards and have 30D/90D/180D MFE/MAE values. Corporate action candidates outside the 180D forward window are not used to block the representative rows. 1Y/2Y fields are retained only when already available from the source residual file; otherwise they remain `null` or narrative-only.

## 6. Canonical Archetype Compression Map

|Source canonical|R13 compression role|Mechanism tested|R13 interpretation|
|---|---|---|---|
|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|policy-event comparator|policy/legal/de-risking vs policy-only headline|company-level conversion bridge determines Stage2/Stage3 validity|
|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|governance/control comparator|tender/control close vs proxy/activist event premium|control-close or tender-price floor determines whether event premium can promote|
|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|cross guardrail|4B/4C overlay timing across both source archetypes|local price spike is not a full 4B unless non-price cap exists; thesis/legal break triggers 4C-watch|

## 7. Case Selection Summary

|case_id|symbol|company|source canonical|case_type|role|trigger_type|entry_date|entry_price|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|034020|두산에너빌리티|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|structural_success|positive|Stage2-Actionable|2025-01-17|21750|current_profile_correct|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|052690|한전기술|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|high_mae_success|positive|Stage2-Actionable|2025-01-17|64500|current_profile_too_late|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|006910|보성파워텍|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|failed_rerating|counterexample|Stage2-Actionable|2022-03-10|6840|current_profile_false_positive|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|013990|아가방컴퍼니|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|failed_rerating|counterexample|Stage2-Actionable|2024-01-03|5630|current_profile_false_positive|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|180640|한진칼|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|high_mae_success|counterexample|Stage2-Actionable|2020-02-26|60000|current_profile_false_positive|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|011780|금호석유화학|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|false_positive_green|counterexample|Stage2-Actionable|2021-01-27|225000|current_profile_false_positive|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|000990|DB하이텍|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|failed_rerating|counterexample|Stage2-Actionable|2023-03-31|72300|current_profile_false_positive|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|003920|남양유업|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|4C_late|positive|Stage2-Actionable|2021-05-28|570000|current_profile_4C_too_late|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 5
calibration_usable_case_count = 8
minimum_positive_case_count = 1
minimum_counterexample_count = 1
balance_status = pass
```

The positive side is not “price went up.” It is “event + conversion bridge survived long enough for risk-adjusted rerating.” The counterexample side is “event premium ran, but no company-level bridge or closing/legal path existed, so the score should have capped earlier.”

## 9. Evidence Source Map

|case_id|trigger_date|evidence_available_at_that_date|Stage2 fields|Stage3 fields|4B fields|4C fields|
|---|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|2025-01-17|KHNP/KEPCO-Westinghouse settlement removed nuclear export IP overhang|public_event_or_disclosure, policy_or_regulatory_optionality, customer_or_order_quality, legal_or_contract_de_risking|multiple_public_sources, financial_visibility_watch|valuation_blowoff, positioning_overheat||
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|2025-01-17|KHNP/KEPCO-Westinghouse settlement improved Korean reactor export path|public_event_or_disclosure, policy_or_regulatory_optionality, customer_or_order_quality, legal_or_contract_de_risking|multiple_public_sources, financial_visibility_watch|valuation_blowoff, positioning_overheat||
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|2022-03-10|pro-nuclear presidential election result and policy expectation; no company-specific order bridge|public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength||price_only_local_peak|thesis_evidence_broken|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|2024-01-03|low-birth policy theme repricing; no company-specific order/margin bridge|public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength||price_only_local_peak|thesis_evidence_broken|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|2020-02-26|Public proxy fight / control-premium contest became the dominant driver, but no clean tender-price floor or durable operating bridge was available at entry.|public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality|multiple_public_sources|valuation_blowoff, positioning_overheat, explicit_event_cap|thesis_evidence_broken|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|2021-01-27|Public proxy/shareholder-return contest overlapped a powerful chemical spread margin cycle; C32 should not claim the whole rerating without an independent control-close bridge.|public_event_or_disclosure, relative_strength|multiple_public_sources, financial_visibility|valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown|thesis_evidence_broken|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|2023-03-30|Activist-stake/governance pressure generated a short event premium, but no tender price, control close, or earnings revision bridge supported Stage3 promotion.|public_event_or_disclosure, relative_strength|multiple_public_sources|valuation_blowoff, positioning_overheat, explicit_event_cap|thesis_evidence_broken|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|2021-05-27|Signed control-sale agreement created a valid C32 Stage2 event premium, but later legal dispute/closing uncertainty should route to 4C-watch rather than keep a stale positive label.|public_event_or_disclosure, customer_or_order_quality, relative_strength|multiple_public_sources, durable_customer_confirmation|valuation_blowoff, legal_or_regulatory_block, explicit_event_cap|legal_or_regulatory_block, thesis_evidence_broken|

## 10. Price Data Source Map

|case_id|symbol|price_shard_path|profile_path|price_basis|stock_web_manifest_max_date|
|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|034020|atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv|atlas/symbol_profiles/034/034020.json|tradable_raw|2026-02-20|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|052690|atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv|atlas/symbol_profiles/052/052690.json|tradable_raw|2026-02-20|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|006910|atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv|atlas/symbol_profiles/006/006910.json|tradable_raw|2026-02-20|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|013990|atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv|atlas/symbol_profiles/013/013990.json|tradable_raw|2026-02-20|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|180640|atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv|atlas/symbol_profiles/180/180640.json|tradable_raw|2026-02-20|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|011780|atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv|atlas/symbol_profiles/011/011780.json|tradable_raw|2026-02-20|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|000990|atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv|atlas/symbol_profiles/000/000990.json|tradable_raw|2026-02-20|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|003920|atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv; atlas/ohlcv_tradable_by_symbol_year/003/003920/2022.csv|atlas/symbol_profiles/003/003920.json|tradable_raw|2026-02-20|

## 11. Case-by-Case Trigger Grid

|case_id|trigger_id|trigger_type|trigger_date|entry_date|entry_price|dedupe_for_aggregate|aggregate_group_role|same_entry_group_id|
|---|---|---|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|R13L72_TR_C31_034020_20250117_STAGE2A|Stage2-Actionable|2025-01-17|2025-01-17|21750|True|representative|R13L72_C31_034020_20250117|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|R13L72_TR_C31_052690_20250117_STAGE2A|Stage2-Actionable|2025-01-17|2025-01-17|64500|True|representative|R13L72_C31_052690_20250117|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|R13L72_TR_C31_006910_20220310_STAGE2A|Stage2-Actionable|2022-03-10|2022-03-10|6840|True|representative|R13L72_C31_006910_20220310|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|R13L72_TR_C31_013990_20240103_STAGE2A|Stage2-Actionable|2024-01-03|2024-01-03|5630|True|representative|R13L72_C31_013990_20240103|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|Stage2-Actionable|2020-02-26|2020-02-26|60000|True|representative|R13L72_G180640_2020-02-26_60000|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|R13L72_T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|Stage2-Actionable|2021-01-27|2021-01-27|225000|True|representative|R13L72_G011780_2021-01-27_225000|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|R13L72_T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP|Stage2-Actionable|2023-03-30|2023-03-31|72300|True|representative|R13L72_G000990_2023-03-31_72300|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|R13L72_T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|Stage2-Actionable|2021-05-27|2021-05-28|570000|True|representative|R13L72_G003920_2021-05-28_570000|

## 12. Trigger-Level OHLC Backtest Tables

|case_id|symbol|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|034020|2025-01-17|21750|42.07|-2.76|99.77|-8.23|289.43|-8.23|2025-10-16|84700|-5.79|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|052690|2025-01-17|64500|17.67|-1.86|17.67|-22.79|88.68|-22.79|2025-06-25|121700|-31.72|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|006910|2022-03-10|6840|32.31|-6.87|32.31|-26.75|32.31|-44.81|2022-03-25|9050|-58.29|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|013990|2024-01-03|5630|27.53|-10.48|27.53|-20.52|27.53|-29.93|2024-01-18|7180|-45.06|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|180640|2020-02-26|60000|60|-35.17|85|-35.17|85|-35.17|2020-04-20|111000|-39.46|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|011780|2021-01-27|225000|30.44|-11.11|32.67|-11.11|32.67|-21.33|2021-05-06|298500|-40.7|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|000990|2023-03-31|72300|15.63|-24.48|15.63|-25.73|15.63|-34.3|2023-04-04|83600|-43.18|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|003920|2021-05-28|570000|42.63|-5.26|42.63|-29.82|42.63|-34.91|2021-07-01|813000|-54.37|

## 13. Current Calibrated Profile Stress Test

|case_id|source canonical|current verdict|MFE90|MAE90|R13 stress-test explanation|
|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|current_profile_correct|99.77|-8.23|current proxy correctly accepts conversion bridge without needing Green confirmation first|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|current_profile_too_late|17.67|-22.79|current proxy underweights early legal/customer de-risking and waits too long despite later MFE|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|current_profile_false_positive|32.31|-26.75|current proxy can over-score event premium if policy/governance headline is not capped by conversion bridge requirement|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|current_profile_false_positive|27.53|-20.52|current proxy can over-score event premium if policy/governance headline is not capped by conversion bridge requirement|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|current_profile_false_positive|85.0|-35.17|current proxy can over-score event premium if policy/governance headline is not capped by conversion bridge requirement|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|current_profile_false_positive|32.67|-11.11|current proxy can over-score event premium if policy/governance headline is not capped by conversion bridge requirement|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|current_profile_false_positive|15.63|-25.73|current proxy can over-score event premium if policy/governance headline is not capped by conversion bridge requirement|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|current_profile_4C_too_late|42.63|-29.82|current proxy can keep event-positive label after legal/closing thesis breaks|

Stress-test answers:

1. Current calibrated profile is broadly correct for true legal/customer de-risking but still vulnerable to headline-only promotions.
2. The MFE/MAE split shows that policy-only and governance-only rows can generate upside yet still carry unacceptable drawdown and false-positive risk.
3. Stage2 actionable bonus is useful only when conversion evidence exists; otherwise it is too generous.
4. Yellow 75 and Green 87 remain appropriate, but R13 adds a bridge gate before those thresholds matter.
5. Price-only blowoff guard is strengthened.
6. Full 4B non-price requirement is strengthened.
7. Hard 4C routing is kept, but signed event/legal-break rows need earlier 4C-watch.

## 14. Stage2 / Yellow / Green Comparison

|case_id|Stage2 Actionable result|Yellow/Green risk|green_lateness_ratio|R13 verdict|
|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|structural_success|allow Stage2/Actionable; Green only after confirmation|0.52|event bridge gate required|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|high_mae_success|allow Stage2/Actionable; Green only after confirmation|0.69|event bridge gate required|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|failed_rerating|block Yellow/Green unless bridge exists|None|event bridge gate required|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|failed_rerating|block Yellow/Green unless bridge exists|None|event bridge gate required|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|high_mae_event_premium_counterexample|block Yellow/Green unless bridge exists|not_applicable|event bridge gate required|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|confounded_governance_false_attribution|block Yellow/Green unless bridge exists|not_applicable|event bridge gate required|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|activist_stake_event_cap_failed_rerating|block Yellow/Green unless bridge exists|not_applicable|event bridge gate required|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|control_sale_positive_but_legal_4C_needed|allow Stage2/Actionable; Green only after confirmation|not_applicable|event bridge gate required|

## 15. 4B Local vs Full-window Timing Audit

|case_id|4B local proximity|4B full-window proximity|4B evidence type|4B timing verdict|
|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|0.98|0.98|valuation_blowoff, positioning_overheat|good_full_window_4B_timing|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|0.88|0.88|valuation_blowoff, positioning_overheat|good_full_window_4B_timing|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|0.69|0.69|price_only|do_not_treat_as_full_4B_without_non_price_evidence|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|0.33|0.33|price_only|price_only_local_4B_weak|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|0.78|0.7|positioning_overheat, valuation_blowoff, control_premium_or_event_premium|event_cap_watch_required_but_not_positive_stage3|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|0.88|0.88|valuation_blowoff, positioning_overheat, control_premium_or_event_premium|confounded_operating_cycle_requires_non_c32_bridge|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|0.96|0.96|valuation_blowoff, positioning_overheat, control_premium_or_event_premium|activist_headline_local_peak_too_early_for_stage3|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|0.72|0.72|control_premium_or_event_premium, legal_or_regulatory_block, positioning_overheat|positive_control_sale_requires_legal_4C_watch|

## 16. 4C Protection Audit

|case_id|4C protection label|Stage4C fields|R13 4C interpretation|
|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|thesis_break_watch_only||no hard 4C; monitor only|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|thesis_break_watch_only||no hard 4C; monitor only|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|thesis_break_watch_only|thesis_evidence_broken|hard 4C / legal thesis break watch|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|thesis_break_watch_only|thesis_evidence_broken|hard 4C / legal thesis break watch|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|thesis_break_watch_only|thesis_evidence_broken|hard 4C / legal thesis break watch|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|false_break_or_wrong_axis_if_governance_only|thesis_evidence_broken|hard 4C / legal thesis break watch|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|hard_4c_late_if_waiting_for_price_break_only|thesis_evidence_broken|hard 4C / legal thesis break watch|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|hard_4c_late|legal_or_regulatory_block, thesis_evidence_broken|hard 4C / legal thesis break watch|

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R13 is not a normal sector-specific round. It is a cross-archetype checkpoint.
```

No L5/L6/L7/L8 sector rule is proposed from R13. The rule is deliberately kept in the R13 cross-archetype guardrail bucket.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = R13_cross_archetype_checkpoint
new_axis_proposed = R13_event_premium_conversion_bridge_required
```

Candidate rule:

```text
If the trigger is a policy, governance, tender, control-premium, or legal headline event, do not allow Stage3-Yellow/Green promotion unless at least one non-price conversion bridge exists: signed/closing-visible contract, customer identity, legal/IP de-risking, tender-price floor, control-close visibility, financial revision, or cash-flow/margin bridge.
```

Counterexample guard:

```text
Policy-only themes, activist stake headlines, and proxy fights without a conversion bridge can remain Stage2-Watch or Stage2-Actionable only; their local peaks are 4B overlay candidates, not positive Stage3 evidence.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|late_green|alignment|
|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|8|44.15|-22.52|76.73|-28.93|0.62|1|1|mixed; policy/legal de-risking worked, policy-only and governance-only headlines over-promoted|
|P0b_e2r_2_0_baseline_reference|rollback_reference|8|44.15|-22.52|76.73|-28.93|0.74|2|2|worse; less separation between event headline and conversion bridge|
|P1_R13_event_premium_conversion_bridge_guard|cross_archetype_guard|8|44.15|-22.52|76.73|-28.93|0.25|0|0|best; keeps nuclear legal-settlement positives and caps policy/governance-only blowoffs|
|P2_R13_nonprice_4B_overlay_split|cross_archetype_4B|8|44.15|-22.52|76.73|-28.93|0.25|0|0|improves 4B/4C risk timing without changing production scoring|
|P3_R13_counterexample_guard_profile|counterexample_guard|8|38.63|-23.86|38.63|-33.11|0.0|0|0|guardrail profile only; not global production|

## 20. Score-Return Alignment Matrix

|case_id|source canonical|score_before|label_before|score_after|label_after|MFE90|MAE90|alignment|current_verdict|
|---|---|---|---|---|---|---|---|---|---|
|R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|78|Stage2-Actionable|84|Stage2-Actionable_YellowWatch|99.77|-8.23|aligned_positive|current_profile_correct|
|R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|74|Stage2-Watch|82|Stage2-Actionable|17.67|-22.79|aligned_but_high_MAE|current_profile_too_late|
|R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|76|Stage2-Actionable_false_positive_risk|63|Stage2-Watch_themeRisk|32.31|-26.75|false_positive_blocked|current_profile_false_positive|
|R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|75|Stage2-Actionable_false_positive_risk|61|Stage2-Watch_themeRisk|27.53|-20.52|false_positive_blocked|current_profile_false_positive|
|R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|76|Stage3-Yellow proxy-fight false promotion risk|63|Stage2-watch + C32 4B event-cap overlay|85.0|-35.17|high_mae_event_premium_counterexample|current_profile_false_positive|
|R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|80|Stage3-Yellow if governance and margin cycle are blended|66|C32 event-watch; positive attribution must move to C17 if margin bridge exists|32.67|-11.11|confounded_governance_false_attribution|current_profile_false_positive|
|R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|75|Stage3-Yellow false promotion risk|58|Stage2-watch / event-cap block|15.63|-25.73|activist_stake_event_cap_failed_rerating|current_profile_false_positive|
|R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|83|Stage3-Yellow control-sale success but legal-risk underweighted|74|Stage2-Actionable + C32 legal 4C watch|42.63|-29.82|control_sale_positive_but_legal_4C_needed|current_profile_4C_too_late|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL|3|5|8|6|8|0|8|8|7|False|True|R13 C31/C32 event-premium guardrail coverage improved; still needs bio/platform/financial event-cap holdouts in later loops|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus | stage3_yellow_total_min | stage3_green_total_min | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
residual_error_types_found: current_profile_4C_too_late, current_profile_false_positive, current_profile_too_late, policy_theme_without_company_bridge, governance_event_without_control_close, signed_control_sale_legal_4C_late, legal_de_risking_positive_high_MAE
new_axis_proposed: R13_event_premium_conversion_bridge_required
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min | stage3_green_total_min | stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Uses stock-web tradable_raw 1D OHLC rows already represented in R11/R12 research artifacts and checked against stock-web manifest/schema/profile paths.
- Uses calibration_usable representative rows only for aggregate metrics.
- Tests event-premium conversion bridge across C31 and C32 source archetypes.
- Splits local-vs-full-window 4B proximity where available.
```

Non-validation scope:

```text
- No live candidate scan.
- No current stock recommendation.
- No stock_agent source-code access.
- No production scoring change.
- No brokerage/API/autotrading path.
- No new price-route discovery.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_event_premium_conversion_bridge_required,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,absent,present,+1,Policy/governance event premium must show contract/customer/legal-close/financial conversion bridge before Stage3 promotion.,Caps policy-only and governance-only false positives while retaining nuclear legal-de-risking positives,R13L72_TR_C31_034020_20250117_STAGE2A|R13L72_TR_C31_052690_20250117_STAGE2A|R13L72_T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|R13L72_TR_C31_006910_20220310_STAGE2A|R13L72_TR_C31_013990_20240103_STAGE2A|R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|R13L72_T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|R13L72_T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP,8,8,5,medium,cross_archetype_shadow_only,not production; R13 checkpoint
shadow_weight,R13_policy_theme_without_company_bridge_stage_cap,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,weak,strong,+1,Policy-only theme spikes have MFE but large MAE unless company-level bridge appears.,Reduces C31 policy-only false positives without weakening legal-settlement positives,R13L72_TR_C31_006910_20220310_STAGE2A|R13L72_TR_C31_013990_20240103_STAGE2A,2,2,2,medium,guard_shadow_only,not production; C31 subset
shadow_weight,R13_governance_without_control_close_stage_cap,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,weak,strong,+1,Proxy fights and activist stakes without tender/control close should remain Stage2-watch plus 4B overlay.,Blocks C32 event-premium false Yellow/Green promotions,R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|R13L72_T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|R13L72_T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP,3,3,3,medium,guard_shadow_only,not production; C32 subset
shadow_weight,R13_nonprice_4B_and_legal_4C_overlay_required,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,kept,strengthened,+1,Full 4B needs non-price cap and signed event disputes should route to hard 4C-watch earlier.,Improves risk timing around Namyang and governance/policy event caps,R13L72_T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|R13L72_TR_C31_006910_20220310_STAGE2A,8,8,5,medium_low,4B_4C_shadow_only,not production; strengthens existing global axes only as R13 residual evidence
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR_C31_034020_20250117_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "legal_de_risking_plus_export_path_aligned_with_180D_MFE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "legal/IP settlement re-entry; strong 180D MFE | R13 cross-archetype comparator sourced from C31_POLICY_SUBSIDY_LEGISLATION_EVENT.", "source_case_id": "C31_034020_2025_WESTINGHOUSE_REENTRY", "source_round_reference": "R11", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY", "symbol": "052690", "company_name": "한전기술", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TR_C31_052690_20250117_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "legal_de_risking_reentry_worked_but_90D_MAE_was_high", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "engineering leverage to settlement; high MAE before 180D rerating | R13 cross-archetype comparator sourced from C31_POLICY_SUBSIDY_LEGISLATION_EVENT.", "source_case_id": "C31_052690_2025_WESTINGHOUSE_REENTRY", "source_round_reference": "R11", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME", "symbol": "006910", "company_name": "보성파워텍", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR_C31_006910_20220310_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_only_theme_initial_MFE_followed_by_large_drawdown", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "policy-only nuclear theme; no company-level contract bridge | R13 cross-archetype comparator sourced from C31_POLICY_SUBSIDY_LEGISLATION_EVENT.", "source_case_id": "C31_006910_2022_YOON_NUCLEAR_POLICY_THEME", "source_round_reference": "R11", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME", "symbol": "013990", "company_name": "아가방컴퍼니", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR_C31_013990_20240103_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "demographic_policy_theme_failed_to_convert_to_financial_visibility", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "policy theme without company-specific conversion | R13 cross-archetype comparator sourced from C31_POLICY_SUBSIDY_LEGISLATION_EVENT.", "source_case_id": "C31_013990_2024_LOW_BIRTH_POLICY_THEME", "source_round_reference": "R11", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "symbol": "180640", "company_name": "한진칼", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mae_event_premium_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Public proxy fight / control-premium contest became the dominant driver, but no clean tender-price floor or durable operating bridge was available at entry. | R13 cross-archetype comparator sourced from C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.", "source_case_id": "C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "source_round_reference": "R12", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "symbol": "011780", "company_name": "금호석유화학", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "confounded_governance_false_attribution", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Public proxy/shareholder-return contest overlapped a powerful chemical spread margin cycle; C32 should not claim the whole rerating without an independent control-close bridge. | R13 cross-archetype comparator sourced from C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.", "source_case_id": "C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "source_round_reference": "R12", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "symbol": "000990", "company_name": "DB하이텍", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "activist_stake_event_cap_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Activist-stake/governance pressure generated a short event premium, but no tender price, control close, or earnings revision bridge supported Stage3 promotion. | R13 cross-archetype comparator sourced from C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.", "source_case_id": "C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "source_round_reference": "R12", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "symbol": "003920", "company_name": "남양유업", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "case_type": "4C_late", "positive_or_counterexample": "positive", "best_trigger": "T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "control_sale_positive_but_legal_4C_needed", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Signed control-sale agreement created a valid C32 Stage2 event premium, but later legal dispute/closing uncertainty should route to 4C-watch rather than keep a stale positive label. | R13 cross-archetype comparator sourced from C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.", "source_case_id": "C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "source_round_reference": "R12", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "do_not_count_as_new_case": false}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R13L72_TR_C31_034020_20250117_STAGE2A", "case_id": "R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "sector": "policy_event_nuclear_export", "primary_archetype": "policy_legal_de_risking", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-17", "evidence_available_at_that_date": "KHNP/KEPCO-Westinghouse settlement removed nuclear export IP overhang", "evidence_source": "Reuters 2025-01-17; stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality", "legal_or_contract_de_risking"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility_watch"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-17", "entry_price": 21750, "MFE_30D_pct": 42.07, "MFE_90D_pct": 99.77, "MFE_180D_pct": 289.43, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.76, "MAE_90D_pct": -8.23, "MAE_180D_pct": -8.23, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-10-16", "peak_price": 84700, "drawdown_after_peak_pct": -5.79, "green_lateness_ratio": 0.52, "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L72_C31_034020_20250117", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_case_id": "C31_034020_2025_WESTINGHOUSE_REENTRY", "source_trigger_id": "TR_C31_034020_20250117_STAGE2A", "source_round_reference": "R11", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type": "trigger", "trigger_id": "R13L72_TR_C31_052690_20250117_STAGE2A", "case_id": "R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY", "symbol": "052690", "company_name": "한전기술", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "sector": "policy_event_nuclear_export", "primary_archetype": "policy_legal_de_risking", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-17", "evidence_available_at_that_date": "KHNP/KEPCO-Westinghouse settlement improved Korean reactor export path", "evidence_source": "Reuters 2025-01-17; stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality", "legal_or_contract_de_risking"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility_watch"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-17", "entry_price": 64500, "MFE_30D_pct": 17.67, "MFE_90D_pct": 17.67, "MFE_180D_pct": 88.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.86, "MAE_90D_pct": -22.79, "MAE_180D_pct": -22.79, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-25", "peak_price": 121700, "drawdown_after_peak_pct": -31.72, "green_lateness_ratio": 0.69, "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L72_C31_052690_20250117", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_case_id": "C31_052690_2025_WESTINGHOUSE_REENTRY", "source_trigger_id": "TR_C31_052690_20250117_STAGE2A", "source_round_reference": "R11", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type": "trigger", "trigger_id": "R13L72_TR_C31_006910_20220310_STAGE2A", "case_id": "R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME", "symbol": "006910", "company_name": "보성파워텍", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "sector": "policy_event_nuclear_theme", "primary_archetype": "policy_theme_false_positive", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-03-10", "evidence_available_at_that_date": "pro-nuclear presidential election result and policy expectation; no company-specific order bridge", "evidence_source": "public election result; stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv", "profile_path": "atlas/symbol_profiles/006/006910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-10", "entry_price": 6840, "MFE_30D_pct": 32.31, "MFE_90D_pct": 32.31, "MFE_180D_pct": 32.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.87, "MAE_90D_pct": -26.75, "MAE_180D_pct": -44.81, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-25", "peak_price": 9050, "drawdown_after_peak_pct": -58.29, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.69, "four_b_full_window_peak_proximity": 0.69, "four_b_timing_verdict": "do_not_treat_as_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L72_C31_006910_20220310", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_case_id": "C31_006910_2022_YOON_NUCLEAR_POLICY_THEME", "source_trigger_id": "TR_C31_006910_20220310_STAGE2A", "source_round_reference": "R11", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type": "trigger", "trigger_id": "R13L72_TR_C31_013990_20240103_STAGE2A", "case_id": "R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME", "symbol": "013990", "company_name": "아가방컴퍼니", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "sector": "policy_event_demographic_theme", "primary_archetype": "policy_theme_false_positive", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-03", "evidence_available_at_that_date": "low-birth policy theme repricing; no company-specific order/margin bridge", "evidence_source": "Reuters fertility-policy context; stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv", "profile_path": "atlas/symbol_profiles/013/013990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-03", "entry_price": 5630, "MFE_30D_pct": 27.53, "MFE_90D_pct": 27.53, "MFE_180D_pct": 27.53, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.48, "MAE_90D_pct": -20.52, "MAE_180D_pct": -29.93, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 7180, "drawdown_after_peak_pct": -45.06, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.33, "four_b_full_window_peak_proximity": 0.33, "four_b_timing_verdict": "price_only_local_4B_weak", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L72_C31_013990_20240103", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_case_id": "C31_013990_2024_LOW_BIRTH_POLICY_THEME", "source_trigger_id": "TR_C31_013990_20240103_STAGE2A", "source_round_reference": "R11", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type": "trigger", "trigger_id": "R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF", "case_id": "R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "symbol": "180640", "company_name": "한진칼", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "sector": "holding_company_airline_group", "primary_archetype": "proxy_fight_without_control_close", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-02-26", "evidence_available_at_that_date": "Public proxy fight / control-premium contest became the dominant driver, but no clean tender-price floor or durable operating bridge was available at entry.", "evidence_source": "Public historical disclosure/news narrative; stock-web 1D OHLC shards and symbol profile verified for the historical price path. This row is not a live recommendation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv", "profile_path": "atlas/symbol_profiles/180/180640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-02-26", "entry_price": 60000, "MFE_30D_pct": 60.0, "MFE_90D_pct": 85.0, "MFE_180D_pct": 85.0, "MFE_1Y_pct": 85.0, "MFE_2Y_pct": null, "MAE_30D_pct": -35.17, "MAE_90D_pct": -35.17, "MAE_180D_pct": -35.17, "MAE_1Y_pct": -35.17, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-04-20", "peak_price": 111000, "drawdown_after_peak_pct": -39.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "event_cap_watch_required_but_not_positive_stage3", "four_b_evidence_type": ["positioning_overheat", "valuation_blowoff", "control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_event_premium_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L72_G180640_2020-02-26_60000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_case_id": "C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "source_trigger_id": "T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF", "source_round_reference": "R12", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
{"row_type": "trigger", "trigger_id": "R13L72_T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "case_id": "R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "symbol": "011780", "company_name": "금호석유화학", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "sector": "chemical_family_control_proxy_fight", "primary_archetype": "proxy_fight_confounded_by_operating_cycle", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-27", "evidence_available_at_that_date": "Public proxy/shareholder-return contest overlapped a powerful chemical spread margin cycle; C32 should not claim the whole rerating without an independent control-close bridge.", "evidence_source": "Public historical disclosure/news narrative; stock-web 1D OHLC shards and symbol profile verified for the historical price path. This row is not a live recommendation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-27", "entry_price": 225000, "MFE_30D_pct": 30.44, "MFE_90D_pct": 32.67, "MFE_180D_pct": 32.67, "MFE_1Y_pct": 32.67, "MFE_2Y_pct": null, "MAE_30D_pct": -11.11, "MAE_90D_pct": -11.11, "MAE_180D_pct": -21.33, "MAE_1Y_pct": -31.85, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -40.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "confounded_operating_cycle_requires_non_c32_bridge", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "false_break_or_wrong_axis_if_governance_only", "trigger_outcome_label": "confounded_governance_false_attribution", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L72_G011780_2021-01-27_225000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_case_id": "C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "source_trigger_id": "T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "source_round_reference": "R12", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
{"row_type": "trigger", "trigger_id": "R13L72_T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP", "case_id": "R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "symbol": "000990", "company_name": "DB하이텍", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "sector": "semiconductor_foundry_governance", "primary_archetype": "activist_stake_without_tender_floor", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-30", "evidence_available_at_that_date": "Activist-stake/governance pressure generated a short event premium, but no tender price, control close, or earnings revision bridge supported Stage3 promotion.", "evidence_source": "Public historical disclosure/news narrative; stock-web 1D OHLC shards and symbol profile verified for the historical price path. This row is not a live recommendation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv", "profile_path": "atlas/symbol_profiles/000/000990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-31", "entry_price": 72300, "MFE_30D_pct": 15.63, "MFE_90D_pct": 15.63, "MFE_180D_pct": 15.63, "MFE_1Y_pct": 15.63, "MFE_2Y_pct": null, "MAE_30D_pct": -24.48, "MAE_90D_pct": -25.73, "MAE_180D_pct": -34.3, "MAE_1Y_pct": -34.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-04", "peak_price": 83600, "drawdown_after_peak_pct": -43.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "activist_headline_local_peak_too_early_for_stage3", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_late_if_waiting_for_price_break_only", "trigger_outcome_label": "activist_stake_event_cap_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L72_G000990_2023-03-31_72300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_case_id": "C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "source_trigger_id": "T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP", "source_round_reference": "R12", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
{"row_type": "trigger", "trigger_id": "R13L72_T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "case_id": "R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "symbol": "003920", "company_name": "남양유업", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "CROSS_ARCHETYPE_EVENT_PREMIUM_POLICY_THEME_CONTROL_CLOSE_GUARDRAIL", "sector": "consumer_control_sale", "primary_archetype": "signed_control_sale_agreement_then_legal_dispute", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | counterexample_mining | holdout_validation | canonical_archetype_compression | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-05-27", "evidence_available_at_that_date": "Signed control-sale agreement created a valid C32 Stage2 event premium, but later legal dispute/closing uncertainty should route to 4C-watch rather than keep a stale positive label.", "evidence_source": "Public historical disclosure/news narrative; stock-web 1D OHLC shards and symbol profile verified for the historical price path. This row is not a live recommendation.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv; atlas/ohlcv_tradable_by_symbol_year/003/003920/2022.csv", "profile_path": "atlas/symbol_profiles/003/003920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-28", "entry_price": 570000, "MFE_30D_pct": 42.63, "MFE_90D_pct": 42.63, "MFE_180D_pct": 42.63, "MFE_1Y_pct": 42.63, "MFE_2Y_pct": null, "MAE_30D_pct": -5.26, "MAE_90D_pct": -29.82, "MAE_180D_pct": -34.91, "MAE_1Y_pct": -34.91, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-01", "peak_price": 813000, "drawdown_after_peak_pct": -54.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.72, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "positive_control_sale_requires_legal_4C_watch", "four_b_evidence_type": ["control_premium_or_event_premium", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "control_sale_positive_but_legal_4C_needed", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L72_G003920_2021-05-28_570000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_case_id": "C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "source_trigger_id": "T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "source_round_reference": "R12", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L72_C31_034020_2025_WESTINGHOUSE_REENTRY", "trigger_id": "R13L72_TR_C31_034020_20250117_STAGE2A", "symbol": "034020", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 6, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -1, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -1, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable_YellowWatch", "changed_components": ["legal_or_contract_risk_score", "customer_quality_score", "backlog_visibility_score"], "component_delta_explanation": "C31 settlement de-risks export path without waiting for full revisions. R13 overlay: event premium must be separated from company-specific conversion bridge; price-only local peaks remain 4B overlay, not positive promotion.", "MFE_90D_pct": 99.77, "MAE_90D_pct": -8.23, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct", "source_case_id": "C31_034020_2025_WESTINGHOUSE_REENTRY", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L72_C31_052690_2025_WESTINGHOUSE_REENTRY", "trigger_id": "R13L72_TR_C31_052690_20250117_STAGE2A", "symbol": "052690", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["legal_or_contract_risk_score", "customer_quality_score"], "component_delta_explanation": "Legal/IP settlement is an early C31 re-entry bridge; Green still requires later confirmation. R13 overlay: event premium must be separated from company-specific conversion bridge; price-only local peaks remain 4B overlay, not positive promotion.", "MFE_90D_pct": 17.67, "MAE_90D_pct": -22.79, "score_return_alignment_label": "aligned_but_high_MAE", "current_profile_verdict": "current_profile_too_late", "source_case_id": "C31_052690_2025_WESTINGHOUSE_REENTRY", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L72_C31_006910_2022_YOON_NUCLEAR_POLICY_THEME", "trigger_id": "R13L72_TR_C31_006910_20220310_STAGE2A", "symbol": "006910", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 3, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch_themeRisk", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Policy-only theme is capped because no company-level contract or margin bridge exists. R13 overlay: event premium must be separated from company-specific conversion bridge; price-only local peaks remain 4B overlay, not positive promotion.", "MFE_90D_pct": 32.31, "MAE_90D_pct": -26.75, "score_return_alignment_label": "false_positive_blocked", "current_profile_verdict": "current_profile_false_positive", "source_case_id": "C31_006910_2022_YOON_NUCLEAR_POLICY_THEME", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L72_C31_013990_2024_LOW_BIRTH_POLICY_THEME", "trigger_id": "R13L72_TR_C31_013990_20240103_STAGE2A", "symbol": "013990", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 4, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage2-Actionable_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 2, "execution_risk_score": -7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage2-Watch_themeRisk", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Demographic policy theme lacks company-level conversion and should be capped. R13 overlay: event premium must be separated from company-specific conversion bridge; price-only local peaks remain 4B overlay, not positive promotion.", "MFE_90D_pct": 27.53, "MAE_90D_pct": -20.52, "score_return_alignment_label": "false_positive_blocked", "current_profile_verdict": "current_profile_false_positive", "source_case_id": "C31_013990_2024_LOW_BIRTH_POLICY_THEME", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L72_C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "trigger_id": "R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF", "symbol": "180640", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 16, "execution_risk_score": 12, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow proxy-fight false promotion risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 10, "execution_risk_score": 18, "legal_or_contract_risk_score": 14, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-watch + C32 4B event-cap overlay", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "contract_score", "margin_bridge_score"], "component_delta_explanation": "C32 shadow profile rewards explicit signed control-sale/tender-price bridge, but caps proxy-only, activist-stake, and operating-cycle-confounded event premiums. Legal/closing dispute raises 4C-watch risk. R13 overlay: event premium must be separated from company-specific conversion bridge; price-only local peaks remain 4B overlay, not positive promotion.", "MFE_90D_pct": 85.0, "MAE_90D_pct": -35.17, "score_return_alignment_label": "high_mae_event_premium_counterexample", "current_profile_verdict": "current_profile_false_positive", "source_case_id": "C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L72_C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "trigger_id": "R13L72_T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "symbol": "011780", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 13, "execution_risk_score": 8, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow if governance and margin cycle are blended", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 11, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 9, "execution_risk_score": 13, "legal_or_contract_risk_score": 11, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "C32 event-watch; positive attribution must move to C17 if margin bridge exists", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "contract_score", "margin_bridge_score"], "component_delta_explanation": "C32 shadow profile rewards explicit signed control-sale/tender-price bridge, but caps proxy-only, activist-stake, and operating-cycle-confounded event premiums. Legal/closing dispute raises 4C-watch risk. R13 overlay: event premium must be separated from company-specific conversion bridge; price-only local peaks remain 4B overlay, not positive promotion.", "MFE_90D_pct": 32.67, "MAE_90D_pct": -11.11, "score_return_alignment_label": "confounded_governance_false_attribution", "current_profile_verdict": "current_profile_false_positive", "source_case_id": "C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L72_C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "trigger_id": "R13L72_T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP", "symbol": "000990", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 14, "execution_risk_score": 10, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow false promotion risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 16, "legal_or_contract_risk_score": 11, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-watch / event-cap block", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "contract_score", "margin_bridge_score"], "component_delta_explanation": "C32 shadow profile rewards explicit signed control-sale/tender-price bridge, but caps proxy-only, activist-stake, and operating-cycle-confounded event premiums. Legal/closing dispute raises 4C-watch risk. R13 overlay: event premium must be separated from company-specific conversion bridge; price-only local peaks remain 4B overlay, not positive promotion.", "MFE_90D_pct": 15.63, "MAE_90D_pct": -25.73, "score_return_alignment_label": "activist_stake_event_cap_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "source_case_id": "C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L72_C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "trigger_id": "R13L72_T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "symbol": "003920", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 14, "execution_risk_score": 7, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83, "stage_label_before": "Stage3-Yellow control-sale success but legal-risk underweighted", "raw_component_scores_after": {"contract_score": 18, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 2, "policy_or_regulatory_score": 3, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + C32 legal 4C watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "contract_score", "margin_bridge_score"], "component_delta_explanation": "C32 shadow profile rewards explicit signed control-sale/tender-price bridge, but caps proxy-only, activist-stake, and operating-cycle-confounded event premiums. Legal/closing dispute raises 4C-watch risk. R13 overlay: event premium must be separated from company-specific conversion bridge; price-only local peaks remain 4B overlay, not positive promotion.", "MFE_90D_pct": 42.63, "MAE_90D_pct": -29.82, "score_return_alignment_label": "control_sale_positive_but_legal_4C_needed", "current_profile_verdict": "current_profile_4C_too_late", "source_case_id": "C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_event_premium_conversion_bridge_required,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,absent,present,+1,Policy/governance event premium must show contract/customer/legal-close/financial conversion bridge before Stage3 promotion.,Caps policy-only and governance-only false positives while retaining nuclear legal-de-risking positives,R13L72_TR_C31_034020_20250117_STAGE2A|R13L72_TR_C31_052690_20250117_STAGE2A|R13L72_T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|R13L72_TR_C31_006910_20220310_STAGE2A|R13L72_TR_C31_013990_20240103_STAGE2A|R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|R13L72_T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|R13L72_T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP,8,8,5,medium,cross_archetype_shadow_only,not production; R13 checkpoint
shadow_weight,R13_policy_theme_without_company_bridge_stage_cap,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,weak,strong,+1,Policy-only theme spikes have MFE but large MAE unless company-level bridge appears.,Reduces C31 policy-only false positives without weakening legal-settlement positives,R13L72_TR_C31_006910_20220310_STAGE2A|R13L72_TR_C31_013990_20240103_STAGE2A,2,2,2,medium,guard_shadow_only,not production; C31 subset
shadow_weight,R13_governance_without_control_close_stage_cap,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,weak,strong,+1,Proxy fights and activist stakes without tender/control close should remain Stage2-watch plus 4B overlay.,Blocks C32 event-premium false Yellow/Green promotions,R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|R13L72_T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|R13L72_T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP,3,3,3,medium,guard_shadow_only,not production; C32 subset
shadow_weight,R13_nonprice_4B_and_legal_4C_overlay_required,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,kept,strengthened,+1,Full 4B needs non-price cap and signed event disputes should route to hard 4C-watch earlier.,Improves risk timing around Namyang and governance/policy event caps,R13L72_T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|R13L72_T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|R13L72_TR_C31_006910_20220310_STAGE2A,8,8,5,medium_low,4B_4C_shadow_only,not production; strengthens existing global axes only as R13 residual evidence
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "new_independent_case_count": 8, "reused_case_count": 0, "new_symbol_count": 8, "same_archetype_new_symbol_count": 8, "same_archetype_new_trigger_family_count": 8, "new_trigger_family_count": 8, "positive_case_count": 3, "counterexample_count": 5, "current_profile_error_count": 7, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_4C_too_late", "current_profile_false_positive", "current_profile_too_late", "policy_theme_without_company_bridge", "governance_event_without_control_close", "signed_control_sale_legal_4C_late", "legal_de_risking_positive_high_MAE"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":"none","reason":"all selected representative rows are calibration_usable; no narrative-only row used for weighting","usage":"not_applicable"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R13
completed_loop = 72
next_round = R1
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
primary_price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_checked = atlas/manifest.json
stock_web_schema_checked = atlas/schema.json
source_research_artifacts_used = e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md | e2r_stock_web_v12_residual_round_R12_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
source_code_accessed = false
production_scoring_changed = false
investment_recommendation_language = none
```

Profile paths referenced by machine-readable rows:

```text
atlas/symbol_profiles/000/000990.json
atlas/symbol_profiles/003/003920.json
atlas/symbol_profiles/006/006910.json
atlas/symbol_profiles/011/011780.json
atlas/symbol_profiles/013/013990.json
atlas/symbol_profiles/034/034020.json
atlas/symbol_profiles/052/052690.json
atlas/symbol_profiles/180/180640.json
```

Price shard paths referenced by machine-readable rows:

```text
atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv
atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv; atlas/ohlcv_tradable_by_symbol_year/003/003920/2022.csv
atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv
atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv
atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv
atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv
atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv
atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv
```

