# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 39
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = K_ENTERPRISE_SECURITY_AND_BIZ_SW_RECURRING_CONTRACT_RETENTION
output_file = e2r_stock_web_v12_residual_round_R13_loop_39_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration research artifact. It is not a stock recommendation, not a live watchlist, and not a production scoring patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the global calibration. It asks whether L8 / C28 needs a more precise rule for enterprise software/security: the difference between real recurring contract retention and a stock that only wears a software/security costume during a theme wave.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 39
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = K_ENTERPRISE_SECURITY_AND_BIZ_SW_RECURRING_CONTRACT_RETENTION
loop_objective = holdout_validation | residual_false_positive_mining | residual_missed_structural_mining | yellow_threshold_stress_test | green_strictness_stress_test | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill
```

The intended compression is:

```text
C28 = software/security names where the important question is not "is this a SW/security company?"
      but "is there recurring contract retention, installed-base conversion, renewal revenue, or retained-seat proof?"
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact check:

- `reports/e2r_calibration/ingest_summary.md` shows 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows across R1-R13 and loops 1-9.
- The previous artifact universe already covers broad sector loops, so this loop deliberately uses a canonical C28 residual slice rather than replaying generic Stage2-vs-Green or 4B rules.
- This loop contributes 4 new independent symbols/cases for the current v12 residual ledger.

Novelty decision:

```text
required_new_independent_case_ratio = 1.00
new_independent_case_count = 4
reused_case_count = 0
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest fields confirmed for this loop:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
raw_row_count = 15214118
tradable_row_count = 14354401
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema basis:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Important caveat: raw/unadjusted OHLC is used. Corporate-action contaminated windows are blocked from calibration by default. In the four selected windows below, the relevant symbol-profile corporate-action candidate dates do not overlap the 180D windows.

## 5. Historical Eligibility Gate

|symbol|company|profile path|profile window|corporate action candidate dates|180D status|
|---|---|---|---|---|---|
|012510|더존비즈온|atlas/symbol_profiles/012/012510.json|1995-05-02 to 2026-02-20|2002-04-22, 2006-06-28, 2009-12-09|clean for 2019-2020 triggers|
|131370|알서포트|atlas/symbol_profiles/131/131370.json|2011-01-05 to 2026-02-20|2014-01-07|clean for 2020 triggers|
|053800|안랩|atlas/symbol_profiles/053/053800.json|2001-09-13 to 2026-02-20|2005-03-31|clean for 2022 triggers|
|263860|지니언스|atlas/symbol_profiles/263/263860.json|2017-08-02 to 2026-02-20|2018-07-05, 2018-07-24|clean for 2023 triggers|

## 6. Canonical Archetype Compression Map

|canonical_archetype_id|included fine archetypes|compression rationale|
|---|---|---|
|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|C28_ENTERPRISE_ERP_CLOUD_RETENTION; C28_REMOTE_SUPPORT_EVENT_TO_RETENTION_TEST; C28_SECURITY_BRAND_POLITICAL_ASSOCIATION_GUARD; C28_NAC_EDR_ZERO_TRUST_RETENTION|All four are software/security names. The residual discriminator is recurring contract quality, not sector label alone.|

## 7. Case Selection Summary

|case_id|symbol|company|case_type|positive_or_counterexample|current_profile_verdict|best_trigger|
|---|---|---|---|---|---|---|
|R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION|012510|더존비즈온|structural_success|positive|current_profile_too_late|R13L39_C28_012510_STAGE2_20190527|
|R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK|131370|알서포트|high_mae_success|positive_with_4b_caveat|current_profile_4B_too_late|R13L39_C28_131370_STAGE2_20200217|
|R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION|053800|안랩|false_positive_green|counterexample|current_profile_false_positive|R13L39_C28_053800_STAGE2_FALSE_20220311|
|R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR|263860|지니언스|structural_success|positive|current_profile_too_late|R13L39_C28_263860_STAGE2_20230125|


## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
positive_with_4b_caveat = 1
counterexample_or_failed_rerating = 1
4B_or_4C_case = 3
minimum_calibration_usable_case_count = 4
```

Interpretation:

- 더존비즈온 and 지니언스 are the clean C28 structural positives: recurring enterprise/security installed-base logic mattered.
- 알서포트 is a high-MFE positive with a caveat: event demand was real, but retention conversion was not proven enough for unguarded Green.
- 안랩 is the main counterexample: a security-company label plus price/association premium should not be treated as contract-retention evidence.

## 9. Evidence Source Map

|case|Stage2 evidence|Stage3 evidence|4B evidence|4C evidence|
|---|---|---|---|---|
|더존비즈온|enterprise ERP/tax-accounting installed base, cloud/WEHAGO conversion route, early financial visibility|confirmed revenue/margin visibility and multiple public sources|valuation expansion after cloud rerating|not primary|
|알서포트|COVID remote-work demand, remote support/meeting usage route, relative strength|event-demand financial visibility, multiple public sources|valuation blowoff, positioning overheat, price-only local peak|demand normalization watch|
|안랩|relative strength and security-brand association only|not supported by contract/retention evidence|event/political premium, valuation blowoff, price-only local peak|thesis evidence broken: association premium is not software retention|
|지니언스|NAC/EDR/zero-trust product route, policy optionality, customer quality|confirmed financial visibility and product-route evidence|post-spike overheat after security-theme rerating|not primary|

## 10. Price Data Source Map

|symbol|entry shard examples|profile path|basis|
|---|---|---|---|
|012510|atlas/ohlcv_tradable_by_symbol_year/012/012510/2019.csv; 2020.csv|atlas/symbol_profiles/012/012510.json|tradable_raw|
|131370|atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv|atlas/symbol_profiles/131/131370.json|tradable_raw|
|053800|atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv|atlas/symbol_profiles/053/053800.json|tradable_raw|
|263860|atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv|atlas/symbol_profiles/263/263860.json|tradable_raw|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|outcome|current_profile_verdict|aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L39_C28_012510_STAGE2_20190527|012510|Stage2-Actionable|2019-05-27|63900|16.43|-14.71|61.19|-14.71|structural_success|current_profile_too_late|True|
|R13L39_C28_012510_YELLOW_20191023|012510|Stage3-Yellow|2019-10-23|68000|51.47|-10.44|81.62|-21.32|structural_success|current_profile_correct|False|
|R13L39_C28_012510_GREEN_20200416|012510|Stage3-Green|2020-04-16|90000|37.22|-11.67|37.22|-11.67|late_green_success_but_reduced_upside|current_profile_too_late|False|
|R13L39_C28_131370_STAGE2_20200217|131370|Stage2-Actionable|2020-02-17|3040|188.49|-21.88|677.96|-21.88|high_mae_success|current_profile_4B_too_late|True|
|R13L39_C28_131370_YELLOW_20200330|131370|Stage3-Yellow|2020-03-30|4670|87.79|-7.39|406.42|-7.39|event_demand_success|current_profile_correct|False|
|R13L39_C28_131370_4B_20200828|131370|Stage4B|2020-08-28|19950|18.55|-41.35|18.55|-41.35|4B_overlay_success|current_profile_4B_too_late|False|
|R13L39_C28_053800_STAGE2_FALSE_20220311|053800|Stage2-Actionable|2022-03-11|86500|152.6|-22.77|152.6|-31.68|false_positive_green|current_profile_false_positive|True|
|R13L39_C28_053800_4B_20220324|053800|Stage4B|2022-03-24|145000|50.69|-53.93|50.69|-59.24|4B_overlay_success|current_profile_4B_too_late|False|
|R13L39_C28_053800_4C_20220415|053800|Stage4C|2022-04-15|98500|30.86|-32.18|30.86|-40.0|4C_success|current_profile_4C_too_late|False|
|R13L39_C28_263860_STAGE2_20230125|263860|Stage2-Actionable|2023-01-25|9700|73.2|-4.02|81.86|-4.02|structural_success|current_profile_too_late|True|
|R13L39_C28_263860_YELLOW_20230517|263860|Stage3-Yellow|2023-05-17|11770|49.87|-6.2|49.87|-13.25|structural_success|current_profile_correct|False|
|R13L39_C28_263860_4B_20230612|263860|Stage4B|2023-06-12|16680|5.76|-33.81|5.76|-38.79|4B_overlay_success|current_profile_4B_too_late|False|


## 12. Trigger-Level OHLC Backtest Tables

The table below keeps the representative and comparison triggers together. All prices are raw/unadjusted stock-web `c` entry prices, with high/low windows read from stock-web tradable shards.

|trigger_id|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|MFE_1Y|MAE_1Y|MFE_2Y|MAE_2Y|peak_date|peak_price|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L39_C28_012510_STAGE2_20190527|13.3|-5.48|16.43|-14.71|61.19|-14.71|87.79|-16.28|93.27|-16.28|2020-02-18|103000|
|R13L39_C28_012510_YELLOW_20191023|20.0|-10.44|51.47|-10.44|81.62|-21.32|81.62|-21.32|81.62|-21.32|2020-06-02|123500|
|R13L39_C28_012510_GREEN_20200416|27.78|-11.67|37.22|-11.67|37.22|-11.67|37.22|-11.67|37.22|-11.67|2020-06-02|123500|
|R13L39_C28_131370_STAGE2_20200217|53.62|-21.88|188.49|-21.88|677.96|-21.88|677.96|-21.88|677.96|-21.88|2020-08-28|23650|
|R13L39_C28_131370_YELLOW_20200330|66.38|-7.39|87.79|-7.39|406.42|-7.39|406.42|-7.39|406.42|-7.39|2020-08-28|23650|
|R13L39_C28_131370_4B_20200828|18.55|-27.32|18.55|-41.35|18.55|-41.35|18.55|-41.35|18.55|-41.35|2020-11-11|23650|
|R13L39_C28_053800_STAGE2_FALSE_20220311|152.6|-14.22|152.6|-22.77|152.6|-31.68|152.6|-31.68|152.6|-31.68|2022-03-24|218500|
|R13L39_C28_053800_4B_20220324|50.69|-35.17|50.69|-53.93|50.69|-59.24|50.69|-59.24|50.69|-59.24|2022-10-13|218500|
|R13L39_C28_053800_4C_20220415|30.86|-4.57|30.86|-32.18|30.86|-40.0|30.86|-40.0|30.86|-40.0|2022-12-13|128900|
|R13L39_C28_263860_STAGE2_20230125|19.9|-4.02|73.2|-4.02|81.86|-4.02|81.86|-4.02|85.36|-4.02|2023-06-13|17640|
|R13L39_C28_263860_YELLOW_20230517|49.53|-4.59|49.87|-6.2|49.87|-13.25|49.87|-13.25|52.76|-13.25|2023-06-13|17640|
|R13L39_C28_263860_4B_20230612|5.76|-33.81|5.76|-33.81|5.76|-38.79|5.76|-38.79|7.79|-38.79|2023-11-29|17640|


Important price rows audited in stock-web:

```text
012510 2019-05-27 close=63900; 2019-08-13 high=74400; 2020-02-18 high=103000; 2020-05-29 high=120000.
131370 2020-02-17 close=3040; 2020-03-19 low=2375; 2020-08-28 high=23650 close=19950; 2020-11-11 low=11700.
053800 2022-03-11 close=86500; 2022-03-24 high=218500 close=145000; 2022-10-13 low=59100.
263860 2023-01-25 close=9700; 2023-06-13 high=17640; 2023-11-29 low=10210.
```

## 13. Current Calibrated Profile Stress Test

|case|current profile result|actual alignment|verdict|
|---|---|---|---|
|더존비즈온|would wait for stronger revision/Green confirmation|Stage2 installed-base evidence captured a large part of forward rerating; Green was late|current_profile_too_late|
|알서포트|would allow event-demand Stage2 but may wait too long for a non-price 4B|early MFE was huge, but 4B risk rose before durable retention evidence appeared|current_profile_4B_too_late|
|안랩|may over-score security label + relative strength if no association guard exists|high MFE came with event premium and severe post-peak drawdown; no contract retention proof|current_profile_false_positive|
|지니언스|may require too much revision confirmation before recognizing security product-route repricing|Stage2 product/policy/customer evidence had strong 90D/180D alignment|current_profile_too_late|

Answers to the required stress-test questions:

```text
1. current calibrated profile often works globally, but C28 still has a sector-specific residual:
   it needs to distinguish recurring contract retention from security/SW label association.

2. Actual MFE/MAE alignment:
   - positive installed-base cases: early evidence worked.
   - event/association cases: price moved, but durable alignment was weak or risky.

3. Stage2 bonus:
   - sufficient for Douzone/Genians only if contract-retention fields are explicit.
   - too generous for AhnLab if relative strength/security label is treated as evidence.

4. Yellow 75:
   - okay for confirmed SW/security revenue visibility.
   - too low for event-only demand without retained-seat proof.

5. Green 87 / revision 55:
   - too strict/late for installed-base enterprise SW when customer stickiness is already visible.
   - not strict enough for association-only security themes unless blocked by guard.

6. price-only blowoff guard:
   - strengthened.

7. full 4B non-price requirement:
   - kept, but C28 needs a watch-level event-demand cap before full 4B.

8. hard 4C routing:
   - strengthened for association premium and post-event thesis break.
```

## 14. Stage2 / Yellow / Green Comparison

|case|Stage2 entry|later confirmation|green_lateness_ratio|interpretation|
|---|---:|---:|---:|---|
|더존비즈온|63,900|90,000|0.44|Green came after a meaningful part of the 63,900 to 123,500 move had already occurred.|
|알서포트|3,040|4,670|0.08|Yellow did not miss much upside, but the case is event-demand, not durable retention.|
|안랩|86,500|not supported|not_applicable|No confirmed contract-retention Green should exist.|
|지니언스|9,700|11,770|0.26|Yellow confirmation was still reasonably timed, but late 4B chasing was costly.|

## 15. 4B Local vs Full-window Timing Audit

|trigger|four_b_local_peak_proximity|four_b_full_window_peak_proximity|verdict|
|---|---:|---:|---|
|R13L39_C28_131370_4B_20200828|0.97|0.97|good_full_window_4B_timing|
|R13L39_C28_053800_4B_20220324|0.45|0.45|good_full_window_4B_timing as risk overlay, not positive evidence|
|R13L39_C28_263860_4B_20230612|0.87|0.87|price-only local 4B too early for full thesis break, but valid as valuation/overheat cap|

C28-specific 4B interpretation:

```text
- Event-demand software spikes can deserve Stage2, but retained-seat conversion is needed before Green.
- Association/political premium in a security stock should be blocked from Stage2/3 promotion.
- Price-only local peaks are watch overlays; full 4B needs non-price weakening or obvious valuation/event premium.
```

## 16. 4C Protection Audit

|case|4C route|protection label|
|---|---|---|
|안랩|association premium decays; no contract-retention thesis confirmation|hard_4c_success|
|알서포트|remote-work demand normalized, but underlying business still existed|thesis_break_watch_only|
|지니언스|post-spike overheat, not hard thesis break|false_break_watch_only|
|더존비즈온|no hard 4C in this loop|not_applicable|

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
candidate = L8_SW_SECURITY_RETENTION_QUALITY_GATE
```

Rule candidate:

```text
In L8, software/security names need an explicit retention-quality field:
- enterprise installed base,
- recurring maintenance/license/SaaS seat expansion,
- public-sector or enterprise security deployment continuity,
- repeatable product module conversion,
- renewal or recurring revenue evidence.

If evidence is only:
- price momentum,
- security/SW label,
- political/personality association,
- event-demand usage spike,
then Stage2 can be allowed only as watch/actionable depending on evidence,
but Stage3-Green should be blocked or capped until retention conversion is shown.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
candidate = C28_RECURRING_CONTRACT_AND_ASSOCIATION_GUARD
```

Proposed C28 shadow axes:

```text
new_axis_proposed:
- c28_recurring_contract_retention_bonus: +2 when installed-base/renewal/repeat-contract evidence exists.
- c28_event_demand_retention_cap: cap event-only demand at Stage2/Yellow unless retained-seat or repeat-contract evidence appears.
- c28_association_only_green_block: block positive Stage2/3 when the move is driven by association/political/personality premium rather than software/security contract evidence.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|changed_axes|eligible_triggers|avg_MFE_90D|avg_MAE_90D|avg_MFE_180D|avg_MAE_180D|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|global_current_proxy|e2r_2_1 calibrated; no C28-specific retention/association guard|none|4|107.68|-15.84|243.4|-18.07|25%|1|2|0.47|mixed|
|P0b|rollback_reference|E2R 2.0 rollback; looser Green and price sensitivity|rollback only|4|107.68|-15.84|243.4|-18.07|50%|0|3|0.61|over-promotes AhnLab/RSUPPORT price action|
|P1|sector_specific_candidate|L8 rewards recurring contract evidence and caps event-only demand|L8 retention + event cap|4|92.71|-13.54|273.67|-13.54|0%|0|1|0.32|better|
|P2|canonical_archetype_candidate|C28 installed-base/renewal evidence adds +2; association-only blocks positive stage|C28 contract-retention guard|4|44.81|-9.37|71.53|-9.37|0%|0|0|0.21|best for structural C28|
|P3|counterexample_guard|Security brand/political association and event-only remote-work spikes cannot become Green without retention conversion|guard profile|4|107.68|-15.84|243.4|-18.07|0%|1|1|0.40|best risk filter|


## 20. Score-Return Alignment Matrix

|bucket|symbols|alignment|
|---|---|---|
|recurring installed-base SW/security|012510, 263860|Early Stage2/Yellow evidence aligned with positive MFE and tolerable MAE.|
|event-demand SW|131370|Stage2 worked, but Green requires retention conversion; 4B overlay needed after blowoff.|
|association-only security theme|053800|High MFE did not equal valid Stage2/3; guard is required.|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L8_PLATFORM_CONTENT_SW_SECURITY|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|K_ENTERPRISE_SECURITY_AND_BIZ_SW_RECURRING_CONTRACT_RETENTION|3|1|3|1|4|0|12|4|4|true|true|C28 now has recurring-contract positive cases plus association/event-demand counterexamples|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- stage3_cross_evidence_green_buffer
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- green_strictness_too_late_for_installed_base_SW
- event_demand_without_retention_can_overpromote
- security_brand_political_association_false_positive
- late_price_chase_MAE_in_security_spike

new_axis_proposed:
- c28_recurring_contract_retention_bonus
- c28_event_demand_retention_cap
- c28_association_only_green_block

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- stage3_cross_evidence_green_buffer

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema basis
- selected symbol profiles
- actual stock-web tradable entry rows
- 30D/90D/180D MFE/MAE proxy calculations
- current profile residual stress test
- positive/counterexample balance
- same-entry dedupe fields
```

Not validated in this loop:

```text
- production scoring code
- live runner
- current 2026 watchlist
- investment recommendation
- broker/API integration
- exact production score implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_recurring_contract_retention_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,2,+2,"installed-base + renewal/maintenance/enterprise SaaS conversion evidence","improves Douzone/Genians timing without promoting AhnLab","R13L39_C28_012510_STAGE2_20190527|R13L39_C28_263860_STAGE2_20230125",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_event_demand_retention_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"event demand can be Stage2 but Green needs retained-seat or repeat-contract proof","keeps RSUPPORT as Stage2 success but adds 4B cap","R13L39_C28_131370_STAGE2_20200217|R13L39_C28_131370_4B_20200828",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_association_only_green_block,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,false,true,+1,"security-company label plus political/personality association is not contract retention evidence","blocks AhnLab false positive despite high MFE","R13L39_C28_053800_STAGE2_FALSE_20220311|R13L39_C28_053800_4B_20220324",4,4,1,high,guard_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION","symbol":"012510","company_name":"더존비즈온","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_ENTERPRISE_ERP_CLOUD_RETENTION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L39_C28_012510_STAGE2_20190527","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 with recurring installed-base evidence aligned better than late Green.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"ERP/tax-accounting installed base plus WEHAGO/cloud conversion created a recurring software repricing route; strict Green confirmation appeared after meaningful upside had already accrued."}
{"row_type":"case","case_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK","symbol":"131370","company_name":"알서포트","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_REMOTE_SUPPORT_EVENT_TO_RETENTION_TEST","case_type":"high_mae_success","positive_or_counterexample":"positive_with_4b_caveat","best_trigger":"R13L39_C28_131370_STAGE2_20200217","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 captured event demand; Green should require retained-seat evidence, not merely remote-work traffic.","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"COVID remote-work demand created extraordinary MFE, but the case requires a retention-conversion cap and early 4B overlay after local overheat."}
{"row_type":"case","case_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION","symbol":"053800","company_name":"안랩","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_BRAND_POLITICAL_ASSOCIATION_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13L39_C28_053800_STAGE2_FALSE_20220311","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Price-only/security-label signal produced high MFE but poor durable alignment and large post-peak drawdown.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Security-company label and relative strength were not enough; move behaved like association/political premium rather than recurring security contract repricing."}
{"row_type":"case","case_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR","symbol":"263860","company_name":"지니언스","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_NAC_EDR_ZERO_TRUST_RETENTION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L39_C28_263860_STAGE2_20230125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Early product-route evidence worked; late chasing after 2023-06 spike had unfavorable MAE.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"NAC/EDR installed-base security vendor with zero-trust policy optionality; price path rewarded early evidence but punished post-spike chasing."}
{"row_type":"trigger","trigger_id":"R13L39_C28_012510_STAGE2_20190527","case_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION","symbol":"012510","company_name":"더존비즈온","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_ENTERPRISE_ERP_CLOUD_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"enterprise cloud ERP / tax-accounting software retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2019-05-27","evidence_available_at_that_date":"recurring cloud ERP installed-base evidence before strict Green confirmation","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2019.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-05-27","entry_price":63900,"MFE_30D_pct":13.3,"MAE_30D_pct":-5.48,"MFE_90D_pct":16.43,"MAE_90D_pct":-14.71,"MFE_180D_pct":61.19,"MAE_180D_pct":-14.71,"MFE_1Y_pct":87.79,"MAE_1Y_pct":-16.28,"MFE_2Y_pct":93.27,"MAE_2Y_pct":-16.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-02-18","peak_price":103000,"drawdown_after_peak_pct":-14.71,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION:2019-05-27:63900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L39_C28_012510_YELLOW_20191023","case_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION","symbol":"012510","company_name":"더존비즈온","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_ENTERPRISE_ERP_CLOUD_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"enterprise cloud ERP / tax-accounting software retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Yellow","trigger_date":"2019-10-23","evidence_available_at_that_date":"post-Stage2 revision confirmation","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":["customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2019.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-10-23","entry_price":68000,"MFE_30D_pct":20.0,"MAE_30D_pct":-10.44,"MFE_90D_pct":51.47,"MAE_90D_pct":-10.44,"MFE_180D_pct":81.62,"MAE_180D_pct":-21.32,"MFE_1Y_pct":81.62,"MAE_1Y_pct":-21.32,"MFE_2Y_pct":81.62,"MAE_2Y_pct":-21.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-06-02","peak_price":123500,"drawdown_after_peak_pct":-21.32,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION:2019-10-23:68000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L39_C28_012510_GREEN_20200416","case_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION","symbol":"012510","company_name":"더존비즈온","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_ENTERPRISE_ERP_CLOUD_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"enterprise cloud ERP / tax-accounting software retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Green","trigger_date":"2020-04-16","evidence_available_at_that_date":"strict Green arrived after much of the 2019-to-2020 repricing","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":["customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","durable_customer_confirmation","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-04-16","entry_price":90000,"MFE_30D_pct":27.78,"MAE_30D_pct":-11.67,"MFE_90D_pct":37.22,"MAE_90D_pct":-11.67,"MFE_180D_pct":37.22,"MAE_180D_pct":-11.67,"MFE_1Y_pct":37.22,"MAE_1Y_pct":-11.67,"MFE_2Y_pct":37.22,"MAE_2Y_pct":-11.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-06-02","peak_price":123500,"drawdown_after_peak_pct":-11.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_success_but_reduced_upside","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION:2020-04-16:90000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L39_C28_131370_STAGE2_20200217","case_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK","symbol":"131370","company_name":"알서포트","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_REMOTE_SUPPORT_EVENT_TO_RETENTION_TEST","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"remote support SaaS / temporary demand shock vs retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2020-02-17","evidence_available_at_that_date":"remote-work software demand shock should be Stage2, not automatic Green","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv","profile_path":"atlas/symbol_profiles/131/131370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-02-17","entry_price":3040,"MFE_30D_pct":53.62,"MAE_30D_pct":-21.88,"MFE_90D_pct":188.49,"MAE_90D_pct":-21.88,"MFE_180D_pct":677.96,"MAE_180D_pct":-21.88,"MFE_1Y_pct":677.96,"MAE_1Y_pct":-21.88,"MFE_2Y_pct":677.96,"MAE_2Y_pct":-21.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-28","peak_price":23650,"drawdown_after_peak_pct":-21.88,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK:2020-02-17:3040","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L39_C28_131370_YELLOW_20200330","case_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK","symbol":"131370","company_name":"알서포트","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_REMOTE_SUPPORT_EVENT_TO_RETENTION_TEST","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"remote support SaaS / temporary demand shock vs retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Yellow","trigger_date":"2020-03-30","evidence_available_at_that_date":"strong event demand confirmed, but retention evidence remains incomplete","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv","profile_path":"atlas/symbol_profiles/131/131370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-03-30","entry_price":4670,"MFE_30D_pct":66.38,"MAE_30D_pct":-7.39,"MFE_90D_pct":87.79,"MAE_90D_pct":-7.39,"MFE_180D_pct":406.42,"MAE_180D_pct":-7.39,"MFE_1Y_pct":406.42,"MAE_1Y_pct":-7.39,"MFE_2Y_pct":406.42,"MAE_2Y_pct":-7.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-28","peak_price":23650,"drawdown_after_peak_pct":-7.39,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"event_demand_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK:2020-03-30:4670","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L39_C28_131370_4B_20200828","case_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK","symbol":"131370","company_name":"알서포트","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_REMOTE_SUPPORT_EVENT_TO_RETENTION_TEST","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"remote support SaaS / temporary demand shock vs retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B","trigger_date":"2020-08-28","evidence_available_at_that_date":"full-window proximity high; without retained-seat evidence this should cap promotion and add risk overlay","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv","profile_path":"atlas/symbol_profiles/131/131370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-08-28","entry_price":19950,"MFE_30D_pct":18.55,"MAE_30D_pct":-27.32,"MFE_90D_pct":18.55,"MAE_90D_pct":-41.35,"MFE_180D_pct":18.55,"MAE_180D_pct":-41.35,"MFE_1Y_pct":18.55,"MAE_1Y_pct":-41.35,"MFE_2Y_pct":18.55,"MAE_2Y_pct":-41.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-11-11","peak_price":23650,"drawdown_after_peak_pct":-41.35,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK:2020-08-28:19950","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L39_C28_053800_STAGE2_FALSE_20220311","case_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION","symbol":"053800","company_name":"안랩","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_BRAND_POLITICAL_ASSOCIATION_GUARD","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"cybersecurity brand plus political/personality association","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-11","evidence_available_at_that_date":"security label plus political/personality association; no contract retention evidence","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-11","entry_price":86500,"MFE_30D_pct":152.6,"MAE_30D_pct":-14.22,"MFE_90D_pct":152.6,"MAE_90D_pct":-22.77,"MFE_180D_pct":152.6,"MAE_180D_pct":-31.68,"MFE_1Y_pct":152.6,"MAE_1Y_pct":-31.68,"MFE_2Y_pct":152.6,"MAE_2Y_pct":-31.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-31.68,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION:2022-03-11:86500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L39_C28_053800_4B_20220324","case_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION","symbol":"053800","company_name":"안랩","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_BRAND_POLITICAL_ASSOCIATION_GUARD","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"cybersecurity brand plus political/personality association","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B","trigger_date":"2022-03-24","evidence_available_at_that_date":"non-contract event premium and blowoff should be risk overlay, not positive Green","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak","control_premium_or_event_premium"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-24","entry_price":145000,"MFE_30D_pct":50.69,"MAE_30D_pct":-35.17,"MFE_90D_pct":50.69,"MAE_90D_pct":-53.93,"MFE_180D_pct":50.69,"MAE_180D_pct":-59.24,"MFE_1Y_pct":50.69,"MAE_1Y_pct":-59.24,"MFE_2Y_pct":50.69,"MAE_2Y_pct":-59.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-10-13","peak_price":218500,"drawdown_after_peak_pct":-59.24,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.44,"four_b_full_window_peak_proximity":0.44,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak","control_premium_or_event_premium"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION:2022-03-24:145000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L39_C28_053800_4C_20220415","case_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION","symbol":"053800","company_name":"안랩","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_BRAND_POLITICAL_ASSOCIATION_GUARD","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"cybersecurity brand plus political/personality association","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4C","trigger_date":"2022-04-15","evidence_available_at_that_date":"post-event thesis break route protects from confusing security brand with contract retention","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_premium_decay"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-04-15","entry_price":98500,"MFE_30D_pct":30.86,"MAE_30D_pct":-4.57,"MFE_90D_pct":30.86,"MAE_90D_pct":-32.18,"MFE_180D_pct":30.86,"MAE_180D_pct":-40.0,"MFE_1Y_pct":30.86,"MAE_1Y_pct":-40.0,"MFE_2Y_pct":30.86,"MAE_2Y_pct":-40.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-12-13","peak_price":128900,"drawdown_after_peak_pct":-40.0,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["event_premium_decay"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION:2022-04-15:98500","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L39_C28_263860_STAGE2_20230125","case_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR","symbol":"263860","company_name":"지니언스","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_NAC_EDR_ZERO_TRUST_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"NAC / EDR / zero-trust security contract retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-25","evidence_available_at_that_date":"zero-trust/NAC/EDR product route with public-sector optionality should not wait for late price confirmation","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-25","entry_price":9700,"MFE_30D_pct":19.9,"MAE_30D_pct":-4.02,"MFE_90D_pct":73.2,"MAE_90D_pct":-4.02,"MFE_180D_pct":81.86,"MAE_180D_pct":-4.02,"MFE_1Y_pct":81.86,"MAE_1Y_pct":-4.02,"MFE_2Y_pct":85.36,"MAE_2Y_pct":-4.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-13","peak_price":17640,"drawdown_after_peak_pct":-4.02,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR:2023-01-25:9700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L39_C28_263860_YELLOW_20230517","case_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR","symbol":"263860","company_name":"지니언스","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_NAC_EDR_ZERO_TRUST_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"NAC / EDR / zero-trust security contract retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Yellow","trigger_date":"2023-05-17","evidence_available_at_that_date":"confirmation was useful but still earlier than strict Green","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-17","entry_price":11770,"MFE_30D_pct":49.53,"MAE_30D_pct":-4.59,"MFE_90D_pct":49.87,"MAE_90D_pct":-6.2,"MFE_180D_pct":49.87,"MAE_180D_pct":-13.25,"MFE_1Y_pct":49.87,"MAE_1Y_pct":-13.25,"MFE_2Y_pct":52.76,"MAE_2Y_pct":-13.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-13","peak_price":17640,"drawdown_after_peak_pct":-13.25,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR:2023-05-17:11770","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13L39_C28_263860_4B_20230612","case_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR","symbol":"263860","company_name":"지니언스","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_NAC_EDR_ZERO_TRUST_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"NAC / EDR / zero-trust security contract retention","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B","trigger_date":"2023-06-12","evidence_available_at_that_date":"post-spike MAE shows the need to separate Stage2 product route from late-chase valuation overlay","evidence_source":"historical public disclosure/news/industry evidence; price rows from Songdaiki/stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-12","entry_price":16680,"MFE_30D_pct":5.76,"MAE_30D_pct":-33.81,"MFE_90D_pct":5.76,"MAE_90D_pct":-33.81,"MFE_180D_pct":5.76,"MAE_180D_pct":-38.79,"MFE_1Y_pct":5.76,"MAE_1Y_pct":-38.79,"MFE_2Y_pct":7.79,"MAE_2Y_pct":-38.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-29","peak_price":17640,"drawdown_after_peak_pct":-38.79,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["positioning_overheat","price_only_local_peak","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR:2023-06-12:16680","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION","trigger_id":"R13L39_C28_012510_STAGE2_20190527","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":10,"margin_bridge_score":11,"revision_score":13,"relative_strength_score":8,"customer_quality_score":13,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":17,"backlog_visibility_score":12,"margin_bridge_score":11,"revision_score":13,"relative_strength_score":8,"customer_quality_score":15,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score","valuation_repricing_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":16.43,"MAE_90D_pct":-14.71,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION","trigger_id":"R13L39_C28_012510_YELLOW_20191023","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":10,"margin_bridge_score":11,"revision_score":13,"relative_strength_score":8,"customer_quality_score":13,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":17,"backlog_visibility_score":12,"margin_bridge_score":11,"revision_score":13,"relative_strength_score":8,"customer_quality_score":15,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score","valuation_repricing_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":51.47,"MAE_90D_pct":-10.44,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION","trigger_id":"R13L39_C28_012510_GREEN_20200416","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":10,"margin_bridge_score":11,"revision_score":13,"relative_strength_score":8,"customer_quality_score":13,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":17,"backlog_visibility_score":12,"margin_bridge_score":11,"revision_score":13,"relative_strength_score":8,"customer_quality_score":15,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score","valuation_repricing_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":37.22,"MAE_90D_pct":-11.67,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK","trigger_id":"R13L39_C28_131370_STAGE2_20200217","symbol":"131370","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":10,"valuation_repricing_score":11,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":52,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":10,"valuation_repricing_score":9,"execution_risk_score":-11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":188.49,"MAE_90D_pct":-21.88,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK","trigger_id":"R13L39_C28_131370_YELLOW_20200330","symbol":"131370","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":10,"valuation_repricing_score":11,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":52,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":10,"valuation_repricing_score":9,"execution_risk_score":-11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":87.79,"MAE_90D_pct":-7.39,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK","trigger_id":"R13L39_C28_131370_4B_20200828","symbol":"131370","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":10,"valuation_repricing_score":11,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":52,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":10,"valuation_repricing_score":9,"execution_risk_score":-11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"Stage4B","changed_components":["contract_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":18.55,"MAE_90D_pct":-41.35,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION","trigger_id":"R13L39_C28_053800_STAGE2_FALSE_20220311","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":19,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":-12,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":29,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-18,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":1,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":152.6,"MAE_90D_pct":-22.77,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION","trigger_id":"R13L39_C28_053800_4B_20220324","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":19,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":-12,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":29,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-18,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":1,"stage_label_after":"Stage4B","changed_components":["contract_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":50.69,"MAE_90D_pct":-53.93,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION","trigger_id":"R13L39_C28_053800_4C_20220415","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":19,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":-12,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":29,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-18,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":1,"stage_label_after":"Stage4C","changed_components":["contract_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":30.86,"MAE_90D_pct":-32.18,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR","trigger_id":"R13L39_C28_263860_STAGE2_20230125","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":10,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":12,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":73.2,"MAE_90D_pct":-4.02,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR","trigger_id":"R13L39_C28_263860_YELLOW_20230517","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":10,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":12,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":49.87,"MAE_90D_pct":-6.2,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR","trigger_id":"R13L39_C28_263860_4B_20230612","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":10,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":12,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage4B","changed_components":["contract_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards recurring contract/installed-base evidence and penalizes association-only or event-only demand without retention conversion.","MFE_90D_pct":5.76,"MAE_90D_pct":-33.81,"score_return_alignment_label":"misaligned_or_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R13","loop":"39","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["green_strictness_too_late_for_installed_base_SW","event_demand_without_retention_can_overpromote","security_brand_political_association_false_positive","late_price_chase_MAE_in_security_spike"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = R13_loop_40
next_large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
next_canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
next_objective = residual_counterexample_and_channel_reorder_retention
```

## 28. Source Notes

```text
Primary price atlas:
- Songdaiki/stock-web
- manifest = atlas/manifest.json
- schema = atlas/schema.json
- universe = atlas/universe/all_symbols.csv
- price_basis = tradable_raw
- price_adjustment_status = raw_unadjusted_marcap

Stock-web files consulted:
- atlas/manifest.json
- atlas/schema.json
- atlas/symbol_profiles/012/012510.json
- atlas/symbol_profiles/131/131370.json
- atlas/symbol_profiles/053/053800.json
- atlas/symbol_profiles/263/263860.json
- atlas/ohlcv_tradable_by_symbol_year/012/012510/2019.csv
- atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv
- atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv

stock_agent research artifact consulted for duplicate/coverage context:
- reports/e2r_calibration/ingest_summary.md
```
