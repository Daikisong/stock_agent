# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R11
selected_loop = 219
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy/MFE-MAE repair + Priority 2 C31 direct policy cashflow conversion compression
round_schedule_status = coverage_index_selected; prior C31 loop 218 exists, so C31 advances to loop 219; recent C10 loop 214 repeated archetype avoided
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD
loop_objective = direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

One-line contribution: this loop turns C31 from a broad policy-headline bucket into a policy-cashflow finality ladder. The same public-money headline behaves like a traffic light only after we know whether the money is preliminary, final, conditional, already recognized, or actually convertible into issuer cashflow.

## 1. Current Calibrated Profile Assumption

Current proxy remains `e2r_2_1_stock_web_calibrated_proxy` for this MD handoff. The already-applied global axes are treated as prior machinery, not as new discoveries: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`.

This run stress-tests a narrower C31 question: when policy money has a named issuer route, does it behave like cashflow, or only like weather over the sector?

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R11`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`
- fine_archetype_id: `C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD`
- valid mapping: C31 -> R11 / L10 policy-event cross-redteam miscellaneous.

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` shows the cumulative corpus is already large, with 2,081 v12 result MDs, 12,410 validated rows, 11,200 representative rows, and no representative rows missing required MFE/MAE fields. It also shows high source-proxy and evidence-url-pending counts, so this run targets direct source repair rather than simple row filling.

Local duplicate avoidance checked prior C31 tariff-oriented files, especially C31 loop 214 and C31 loop 218. This run avoids repeating the KEPCO/KOGAS tariff rows and instead uses U.S. industrial-policy subsidies and loans with direct issuer/JV routes.

Minimum novelty gates:

```text
new_independent_case_count = 8
minimum_new_symbol_count = 2 -> observed 6
minimum_counterexample_count = 1 -> observed 4
minimum_positive_case_count = 1 -> observed 4
minimum_new_trigger_family_count = observed 8
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```json
{"source_name":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap","min_date":"1995-05-02","max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","schema_path":"atlas/schema.json"}
```

Schema interpretation used: `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE are computed from entry-date close and forward max high / min low over 30, 90, and 180 tradable rows.

## 5. Historical Eligibility Gate

All representative trigger rows satisfy:

- historical trigger date before Stock-Web manifest max date,
- entry row present in tradable shard mirror,
- at least 180 forward tradable rows available,
- 30D/90D/180D MFE and MAE computed,
- no `s`-ratio corporate-action jump >=20% detected in the local 180D loaded windows,
- trigger rows use canonical stage labels only.

## 6. Canonical Archetype Compression Map

| raw event shape | C31 compressed interpretation | promotion/cap rule |
|---|---|---|
| Preliminary CHIPS PMT | named but not final policy route | Stage2 watch/actionable; cap if after rerating |
| Final awarded CHIPS funding | finality + named issuer route | Stage2-Actionable / Yellow; Green only with margin/order bridge |
| Recognized AMPC in operating profit | cash recognized but can be result-only | cap below Green unless ex-credit margin/demand persist |
| Conditional ATVM loan to JV | large financing but conditional and often not parent cashflow | Stage2 watch until parent cashflow/offtake/utilization visible |
| Event after local premium | direct policy but bad phase | local Stage4B-watch, not full 4B without non-price risk |

## 7. Case Selection Summary

|case_id|symbol|name|trigger_date|entry_date|trigger_type|family|polarity|MFE90|MAE90|MFE180|MAE180|profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C31_L219_01_SAMSUNG_PMT_AFTER_MEMORY_RERATING|005930|삼성전자|2024-04-15|2024-04-16|Stage4B|chips_pmt_after_local_memory_rerating|counterexample|11.00|-12.25|11.00|-37.62|current_profile_false_positive|
|C31_L219_02_SAMSUNG_FINAL_AWARD_AFTER_RESET|005930|삼성전자|2024-12-20|2024-12-23|Stage3-Yellow|chips_final_award_after_due_diligence_and_price_reset|positive|15.89|-5.05|50.47|-5.05|current_profile_too_late|
|C31_L219_03_SKHYNIX_PMT_HBM_PACKAGING_ROUTE|000660|SK하이닉스|2024-08-06|2024-08-07|Stage2-Actionable|chips_pmt_named_hbm_packaging_and_rd_route|positive|21.68|-14.53|34.08|-14.53|current_profile_correct|
|C31_L219_04_SKHYNIX_FINAL_AWARD_DUE_DILIGENCE|000660|SK하이닉스|2024-12-19|2024-12-20|Stage3-Yellow|chips_final_award_named_hbm_route|positive|34.72|-3.44|110.09|-3.44|current_profile_too_late|
|C31_L219_05_SKC_ABSOLICS_FINAL_AWARD|011790|SKC|2024-12-05|2024-12-06|Stage2-Actionable|chips_final_award_advanced_packaging_material_affiliate|positive|85.64|-11.59|85.64|-11.90|current_profile_missed_structural|
|C31_L219_06_LGES_Q1_AMPC_RESULT_ONLY_TRAP|373220|LG에너지솔루션|2023-04-26|2023-04-27|Stage3-Yellow|ira_ampc_recognized_in_operating_profit_ex_credit_guard|counterexample|5.62|-12.61|5.62|-36.71|current_profile_false_positive|
|C31_L219_07_SKINNOVATION_BLUEOVAL_CONDITIONAL_LOAN|096770|SK이노베이션|2023-06-22|2023-06-23|Stage2-Actionable|atvm_conditional_loan_to_jv_parent_cashflow_uncertain|counterexample|25.68|-34.23|25.68|-41.13|current_profile_false_positive|
|C31_L219_08_SAMSUNGSDI_STARPLUS_CONDITIONAL_LOAN|006400|삼성SDI|2024-12-02|2024-12-03|Stage2|atvm_conditional_loan_to_jv_without_near_term_conversion|counterexample|2.68|-34.87|2.68|-39.58|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

- positive_case_count: 4
- counterexample_count: 4
- 4B/watch rows: 2
- 4C rows: 0 hard 4C. The observed failure mode is usually conditionality, parent-cashflow gap, or result-only subsidy trap, not complete thesis death.

Positive side: final awarded CHIPS funding with a named issuer route and price reset showed strong 180D upside in Samsung, SK hynix, and SKC/Absolics.

Counterexample side: preliminary terms after rerating, AMPC result-only recognition, and conditional JV loans produced large drawdowns or weak 180D MFE. Policy money can be a bridge, but only when it actually lands on the issuer’s income statement or balance-sheet path.

## 9. Evidence Source Map

|case_id|evidence_key|summary|url|
|---|---|---|---|
|C31_L219_01_SAMSUNG_PMT_AFTER_MEMORY_RERATING|samsung_pmt|NIST / U.S. Department of Commerce, 2024-04-15, preliminary memorandum for up to $6.4B direct funding to Samsung Electronics under CHIPS Act;|https://www.nist.gov/news-events/news/2024/04/biden-harris-administration-announces-preliminary-terms-samsung-electronics|
|C31_L219_02_SAMSUNG_FINAL_AWARD_AFTER_RESET|samsung_final|NIST / U.S. Department of Commerce, 2024-12-20, final CHIPS award to Samsung Electronics up to $4.745B;|https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-award-samsung|
|C31_L219_03_SKHYNIX_PMT_HBM_PACKAGING_ROUTE|skhynix_pmt|NIST / U.S. Department of Commerce, 2024-08-06, preliminary terms with SK hynix for up to $450M direct funding plus up to $500M loans;|https://www.nist.gov/news-events/news/2024/08/us-department-commerce-announces-preliminary-terms-sk-hynix-advance-us-ai-0|
|C31_L219_04_SKHYNIX_FINAL_AWARD_DUE_DILIGENCE|skhynix_final|NIST / U.S. Department of Commerce, 2024-12-19, final CHIPS award to SK hynix up to $458M direct funding;|https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-award-sk-hynix|
|C31_L219_05_SKC_ABSOLICS_FINAL_AWARD|skc_absolics_final|NIST / U.S. Department of Commerce, 2024-12-05, final CHIPS award to Absolics, an affiliate of Korea-based SKC, up to $75M;|https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-awards-absolics-and|
|C31_L219_06_LGES_Q1_AMPC_RESULT_ONLY_TRAP|lges_ampc|LG Energy Solution press release, 2023-04-26, Q1 operating profit included KRW100.3B estimated AMPC under IRA Section 45X;|https://news.lgensol.com/company-news/press-releases/1705/|
|C31_L219_07_SKINNOVATION_BLUEOVAL_CONDITIONAL_LOAN|blueoval_conditional|U.S. DOE LPO bulletin, 2023-06-22, conditional commitment up to $9.2B loan to BlueOval SK LLC;|https://content.govdelivery.com/accounts/USDOELPO/bulletins/3614c1e|
|C31_L219_08_SAMSUNGSDI_STARPLUS_CONDITIONAL_LOAN|starplus_conditional|U.S. DOE LPO, 2024-12-02, conditional commitment up to $7.54B loan to StarPlus Energy LLC;|https://www.energy.gov/edf/articles/lpo-announces-conditional-commitment-starplus-energy-construct-lithium-ion-battery|

## 10. Price Data Source Map

|symbol|price_shard_path|profile_path|local_files_used|
|---|---|---|---|
|005930|atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv|atlas/symbol_profiles/005/005930.json|/mnt/data/e2r_run/005930_2024.csv;/mnt/data/e2r_run/005930_2025.csv|
|005930|atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv|atlas/symbol_profiles/005/005930.json|/mnt/data/e2r_run/005930_2024.csv;/mnt/data/e2r_run/005930_2025.csv|
|000660|atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv|atlas/symbol_profiles/000/000660.json|/mnt/data/e2r_run/000660_2024.csv;/mnt/data/e2r_run/000660_2025.csv|
|000660|atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv|atlas/symbol_profiles/000/000660.json|/mnt/data/e2r_run/000660_2024.csv;/mnt/data/e2r_run/000660_2025.csv|
|011790|atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv|atlas/symbol_profiles/011/011790.json|/mnt/data/011790_2023.csv;/mnt/data/011790_2024.csv;/mnt/data/011790_2025.csv|
|373220|atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv|atlas/symbol_profiles/373/373220.json|/mnt/data/373220_2022.csv;/mnt/data/e2r_c13_l211/price/373220_2023.csv;/mnt/data/e2r_c13_l211/price/373220_2024.csv;/mnt/data/e2r_c13_l211/price/373220_2025.csv;/mnt/data/e2r_c13_l211/price/373220_2026.csv|
|096770|atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv|atlas/symbol_profiles/096/096770.json|/mnt/data/e2r_c13_l211/price/096770_2023.csv;/mnt/data/e2r_c13_l211/price/096770_2024.csv;/mnt/data/e2r_c13_l211/price/096770_2025.csv;/mnt/data/e2r_c13_l211/price/096770_2026.csv|
|006400|atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv|atlas/symbol_profiles/006/006400.json|/mnt/data/e2r_c13_l211/price/006400_2024.csv;/mnt/data/e2r_c13_l211/price/006400_2025.csv;/mnt/data/e2r_c13_l211/price/006400_2026.csv|

## 11. Case-by-Case Trigger Grid

### C31_L219_01 — Samsung preliminary PMT after memory rerating

The April 2024 CHIPS PMT was a named and large subsidy route, but it arrived after Samsung had already rerated on memory/HBM-cycle expectations. The 180D path showed MFE +11.00% versus MAE -37.62%. Current profile would likely over-credit direct policy evidence. Shadow rule caps preliminary PMT rows when price phase is already crowded.

### C31_L219_02 — Samsung final award after price reset

The December 2024 final award had legal/funding finality and came after price reset. The same issuer and same policy family flipped from a poor April entry to a much better December entry: MFE180 +50.47% with MAE180 -5.05%. The mechanism is not “Samsung + CHIPS = good”; the mechanism is finality plus phase reset.

### C31_L219_03 / 04 — SK hynix PMT and final award

SK hynix PMT already had a named HBM advanced-packaging route; final award later turned policy route into stronger finality. The December final row had MFE180 +110.09% and MAE180 -3.44%. This is the cleanest positive row in the set, but C31 still should not promote policy alone to Green without issuer-specific order/margin bridge.

### C31_L219_05 — SKC / Absolics final award

SKC was a smaller direct beneficiary through Absolics. MFE90 and MFE180 were both +85.64%, but post-peak drawdown was -52.54%. This is a positive Stage2-Actionable row with an embedded 4B overlay after the policy-option spike.

### C31_L219_06 — LG Energy Solution AMPC recognition

LGES actually recognized KRW100.3B AMPC in Q1 operating profit. Yet forward MFE180 was only +5.62% while MAE180 reached -36.71%. Recognized subsidy is stronger than a headline, but result-only subsidy can still fail if ex-credit demand/margin bridge weakens.

### C31_L219_07 / 08 — BlueOval SK and StarPlus conditional ATVM loans

The loan sizes were huge, but the borrower route was a JV and conversion to parent equity cashflow was conditional and delayed. SK Innovation and Samsung SDI both produced poor 180D asymmetry. For C31, conditional financing is a pipe; issuer cashflow is water actually moving through it.

## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|005930|2024-04-16|80000.00|1.88|-8.13|11.00|-12.25|11.00|-37.62|2024-07-11|88800.00|-43.81|
|005930|2024-12-23|53500.00|7.85|-5.05|15.89|-5.05|50.47|-5.05|2025-09-18|80500.00|-2.36|
|000660|2024-08-07|169300.00|19.61|-14.53|21.68|-14.53|34.08|-14.53|2025-01-22|227000.00|-28.33|
|000660|2024-12-20|168500.00|34.72|-0.83|34.72|-3.44|110.09|-3.44|2025-09-16|354000.00|-6.36|
|011790|2024-12-06|97500.00|85.64|-7.38|85.64|-11.59|85.64|-11.90|2025-01-20|181000.00|-52.54|
|373220|2023-04-27|587000.00|4.60|-9.71|5.62|-12.61|5.62|-36.71|2023-07-26|620000.00|-40.08|
|096770|2023-06-23|182600.00|25.68|-13.58|25.68|-34.23|25.68|-41.13|2023-07-26|229500.00|-53.16|
|006400|2024-12-03|261000.00|2.68|-12.07|2.68|-34.87|2.68|-39.58|2024-12-03|268000.00|-41.16|

## 13. Current Calibrated Profile Stress Test

|case_id|symbol|before|stage_before|after|stage_after|MFE90|MAE90|verdict|
|---|---|---|---|---|---|---|---|---|
|C31_L219_01_SAMSUNG_PMT_AFTER_MEMORY_RERATING|005930|78|Stage3-Yellow|58|Stage4B|11.00|-12.25|current_profile_false_positive|
|C31_L219_02_SAMSUNG_FINAL_AWARD_AFTER_RESET|005930|70|Stage2-Actionable|80|Stage3-Yellow|15.89|-5.05|current_profile_too_late|
|C31_L219_03_SKHYNIX_PMT_HBM_PACKAGING_ROUTE|000660|76|Stage2-Actionable|79|Stage2-Actionable|21.68|-14.53|current_profile_correct|
|C31_L219_04_SKHYNIX_FINAL_AWARD_DUE_DILIGENCE|000660|80|Stage3-Yellow|88|Stage3-Green|34.72|-3.44|current_profile_too_late|
|C31_L219_05_SKC_ABSOLICS_FINAL_AWARD|011790|58|Stage2|76|Stage2-Actionable|85.64|-11.59|current_profile_missed_structural|
|C31_L219_06_LGES_Q1_AMPC_RESULT_ONLY_TRAP|373220|84|Stage3-Yellow|66|Stage2-Actionable|5.62|-12.61|current_profile_false_positive|
|C31_L219_07_SKINNOVATION_BLUEOVAL_CONDITIONAL_LOAN|096770|74|Stage2-Actionable|55|Stage2|25.68|-34.23|current_profile_false_positive|
|C31_L219_08_SAMSUNGSDI_STARPLUS_CONDITIONAL_LOAN|006400|72|Stage2-Actionable|54|Stage2|2.68|-34.87|current_profile_false_positive|

Stress-test answers:

1. Current calibrated profile would correctly require non-price evidence, but it can still over-credit direct policy route when finality or issuer cashflow is absent.
2. It is correct on SK hynix PMT, too late on some final awards, and false-positive on conditional-loan or result-only rows.
3. Stage2-Actionable bonus is too generous for conditional JV loans and too conservative for final awarded cash after price reset.
4. Yellow threshold 75 is not the issue; the evidence ladder feeding the score is the issue.
5. Green threshold 87 / revision 55 remains appropriate, but Green should require cashflow finality, not merely subsidy finality.
6. Price-only blowoff guard is appropriate, but event-premium phase must be added to C31 even when the event itself is non-price.
7. Full 4B non-price requirement is appropriate. Most weak rows here are local 4B-watch, not full 4B.
8. Hard 4C routing should not fire merely because AMPC/loan rows draw down; thesis death requires project cancellation, repeal, customer-route death, or parent cashflow impairment.

## 14. Stage2 / Yellow / Green Comparison

| ladder step | representative rows | observed result | implication |
|---|---|---|---|
| Stage2 watch | conditional JV loans | weak or high-MAE | keep below Actionable without parent cashflow bridge |
| Stage2-Actionable | named PMT with issuer route | mixed; depends on phase | allow only if price phase not crowded |
| Stage3-Yellow | final award or recognized subsidy | positive when finality + reset; weak when result-only | Yellow needs finality plus cashflow sufficiency |
| Stage3-Green | final award + issuer order/margin bridge | SK hynix final is closest | Green should require non-policy business confirmation |

`green_lateness_ratio = not_applicable` for this run because the goal is not a same-case Stage2-to-Green chronological promotion ladder; it is policy-finality compression across comparable C31 rows.

## 15. 4B Local vs Full-window Timing Audit

Local 4B-watch is useful when a policy event arrives after price premium. Samsung April PMT had full 180D peak only +11.00% above entry and subsequent drawdown after peak -43.81%. SKC December award had huge MFE but then post-peak drawdown -52.54%, making it a positive row that needs 4B overlay after spike.

| case_id | local 4B issue | full-window verdict |
|---|---|---|
| C31_L219_01 | policy PMT after prior memory rerating | local Stage4B-watch was needed; not hard 4C |
| C31_L219_05 | direct final award caused option-like spike | positive entry, but 4B overlay needed after fast MFE |
| C31_L219_07 | large conditional loan before conversion | no full 4B; instead Stage2 cap and conversion watch |
| C31_L219_08 | conditional loan in weak EV tape | no full 4B; Stage2-watch until utilization/customer call-off |

## 16. 4C Protection Audit

No row is assigned hard Stage4C as the representative trigger. Large drawdown alone is not thesis death. 4C would require one of the following:

- subsidy/loan cancellation or legal block,
- final award materially reversed,
- JV customer/offtake route broken,
- parent unable to capture economics,
- repeated ex-credit loss despite recognized subsidies.

Protection label for this MD: `thesis_break_watch_only`.

## 17. Sector-Specific Rule Candidate

`L10 policy/event evidence should split public program existence, named issuer route, legal/funding finality, cashflow sufficiency, and price phase. A government program opens a door; C31 promotion requires evidence that the listed issuer can walk through it and keep the cash.`

## 18. Canonical-Archetype Rule Candidate

`C31 should use a five-step policy-to-cashflow finality ladder: preliminary terms -> final awarded funding -> named issuer/JV route -> recognized cash or financing sufficiency -> durable issuer-level conversion. Preliminary PMT and conditional JV loans are capped; result-only subsidy is capped unless ex-credit/parent cashflow survives; final awards after price reset can promote.`

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|6|16.90|-18.65|31.52|-28.84|0.67|0|1|improves_alignment_vs_policy_headline_only|
|P0b_e2r_2_0_baseline_reference|rollback_reference|2|20.17|-8.03|57.86|-20.07|0.50|0|1|improves_alignment_vs_policy_headline_only|
|P1_L10_policy_cashflow_candidate|sector_specific|4|39.48|-8.65|70.07|-8.73|0.00|1|2|improves_alignment_vs_policy_headline_only|
|P2_C31_policy_to_cashflow_candidate|canonical_archetype_specific|4|39.48|-8.65|70.07|-8.73|0.00|1|2|improves_alignment_vs_policy_headline_only|
|P3_C31_counterexample_guard|counterexample_guard|3|45.42|-6.69|82.07|-6.80|0.00|1|2|improves_alignment_vs_policy_headline_only|

## 20. Score-Return Alignment Matrix

The candidate ladder improves alignment because it removes three types of false equivalence:

1. PMT vs final award: the legal state is different.
2. Direct issuer award vs JV conditional loan: the cashflow recipient is different.
3. Subsidy recognized in operating profit vs durable ex-credit earnings: the quality of earnings is different.

Average all-case MFE90/MAE90 = 25.36 / -16.07. The positive-only candidate profile retains the high-MFE rows while excluding the AMPC/conditional-loan traps.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD | 4 | 4 | 2 | 0 | 8 | 0 | 8 | 8 | 7 | yes | yes | C31 direct-source subsidy rows improved; remaining gap is direct awarded cashflow outside semis/batteries |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: policy_headline_false_positive; preliminary_terms_after_rerating_4B_watch; conditional_loan_parent_cashflow_gap; recognized_subsidy_result_only_green_trap; final_award_after_reset_missed_structural
new_axis_proposed: c31_awarded_policy_cashflow_finality_ladder; c31_pmt_vs_final_award_phase_guard; c31_conditional_loan_parent_cashflow_discount; c31_result_only_subsidy_green_trap_cap
existing_axis_strengthened: stage2_required_bridge; local_4b_watch_guard; stage3_green_revision_min_by_cashflow_finality
existing_axis_weakened: none in production; shadow-only weakening of policy headline directness for PMT/conditional-loan rows
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L10 policy/event evidence should split public program existence, named issuer route, legal/funding finality, cashflow sufficiency, and price phase.
canonical_archetype_rule_candidate: C31 should separate preliminary terms, final award, recognized subsidy, conditional JV loan, and issuer-level cashflow conversion.
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web tradable raw OHLC path for the listed symbols and entry dates.
- 30D/90D/180D MFE and MAE using max high / min low forward windows.
- direct source URLs for historical policy/subsidy events.
- duplicate avoidance against recent local C31 tariff rows.

Not validated:

- production code behavior in `stock_agent`.
- live recommendations or current candidates.
- actual receipt timing of every subsidy tranche.
- revised or post-2026-02-20 price history.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_policy_finality_ladder,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"split PMT/final/recognized/conditional funding","keeps high-MFE final award rows while filtering PMT/conditional false positives","TRG_C31_L219_01|TRG_C31_L219_02|TRG_C31_L219_03|TRG_C31_L219_04|TRG_C31_L219_05|TRG_C31_L219_06|TRG_C31_L219_07|TRG_C31_L219_08",8,8,4,medium,canonical_shadow_only,"not production; batch implementation later"
shadow_weight,c31_conditional_loan_parent_cashflow_discount,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"large JV loans are not automatically listed-parent cashflow","096770 and 006400 high-MAE rows capped below Yellow","TRG_C31_L219_07|TRG_C31_L219_08",2,2,2,medium,canonical_shadow_only,"requires parent cashflow/offtake bridge"
shadow_weight,c31_result_only_subsidy_green_trap_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"recognized subsidy without ex-credit durability failed in LGES row","caps result-only AMPC rows below Green","TRG_C31_L219_06",1,1,1,medium,canonical_shadow_only,"not a global anti-AMPC rule"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C31_L219_01_SAMSUNG_PMT_AFTER_MEMORY_RERATING","symbol":"005930","company_name":"삼성전자","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","case_type":"policy_pmt_after_rerating_4b_watch","positive_or_counterexample":"counterexample","best_trigger":"TRG_C31_L219_01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"policy_subsidy_pmt_direct_but_price_phase_bad"}
{"row_type":"case","case_id":"C31_L219_02_SAMSUNG_FINAL_AWARD_AFTER_RESET","symbol":"005930","company_name":"삼성전자","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","case_type":"direct_award_after_price_reset","positive_or_counterexample":"positive","best_trigger":"TRG_C31_L219_02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_final_award_after_preliminary_pmt","independent_evidence_weight":0.5,"score_price_alignment":"current_profile_too_late","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"final_award_plus_reset_positive"}
{"row_type":"case","case_id":"C31_L219_03_SKHYNIX_PMT_HBM_PACKAGING_ROUTE","symbol":"000660","company_name":"SK하이닉스","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","case_type":"direct_award_named_ai_packaging_route","positive_or_counterexample":"positive","best_trigger":"TRG_C31_L219_03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"issuer_specific_subsidy_with_customer_route_positive"}
{"row_type":"case","case_id":"C31_L219_04_SKHYNIX_FINAL_AWARD_DUE_DILIGENCE","symbol":"000660","company_name":"SK하이닉스","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","case_type":"final_award_with_hbm_route","positive_or_counterexample":"positive","best_trigger":"TRG_C31_L219_04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_final_award_after_preliminary_pmt","independent_evidence_weight":0.5,"score_price_alignment":"current_profile_too_late","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"final_award_direct_cash_route_strong_positive"}
{"row_type":"case","case_id":"C31_L219_05_SKC_ABSOLICS_FINAL_AWARD","symbol":"011790","company_name":"SKC","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","case_type":"small_direct_chips_award_with_project_option","positive_or_counterexample":"positive","best_trigger":"TRG_C31_L219_05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_missed_structural","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"small_direct_subsidy_positive_but_4b_after_spike"}
{"row_type":"case","case_id":"C31_L219_06_LGES_Q1_AMPC_RESULT_ONLY_TRAP","symbol":"373220","company_name":"LG에너지솔루션","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","case_type":"recognized_subsidy_but_ex_credit_demand_risk","positive_or_counterexample":"counterexample","best_trigger":"TRG_C31_L219_06","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"recognized_ampc_result_only_not_durable_conversion"}
{"row_type":"case","case_id":"C31_L219_07_SKINNOVATION_BLUEOVAL_CONDITIONAL_LOAN","symbol":"096770","company_name":"SK이노베이션","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","case_type":"conditional_loan_not_parent_cashflow","positive_or_counterexample":"counterexample","best_trigger":"TRG_C31_L219_07","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"huge_policy_financing_not_parent_cashflow"}
{"row_type":"case","case_id":"C31_L219_08_SAMSUNGSDI_STARPLUS_CONDITIONAL_LOAN","symbol":"006400","company_name":"삼성SDI","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","case_type":"conditional_loan_with_ev_demand_and_policy_reversal_risk","positive_or_counterexample":"counterexample","best_trigger":"TRG_C31_L219_08","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"conditional_loan_direct_but_no_near_term_equity_conversion"}
{"row_type":"trigger","trigger_id":"TRG_C31_L219_01","case_id":"C31_L219_01_SAMSUNG_PMT_AFTER_MEMORY_RERATING","symbol":"005930","company_name":"삼성전자","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-04-15","evidence_available_at_that_date":"NIST / U.S. Department of Commerce, 2024-04-15, preliminary memorandum for up to $6.4B direct funding to Samsung Electronics under CHIPS Act; URL: https://www.nist.gov/news-events/news/2024/04/biden-harris-administration-announces-preliminary-terms-samsung-electronics","evidence_source":"https://www.nist.gov/news-events/news/2024/04/biden-harris-administration-announces-preliminary-terms-samsung-electronics","stage2_evidence_fields":["named_policy_or_subsidy_event","issuer_or_jv_route_visible","chips_pmt_after_local_memory_rerating"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_after_local_rerating","price_phase_or_execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-16","entry_price":80000.0,"MFE_30D_pct":1.88,"MFE_90D_pct":11.0,"MFE_180D_pct":11.0,"MFE_1Y_pct":11.0,"MFE_2Y_pct":null,"MAE_30D_pct":-8.13,"MAE_90D_pct":-12.25,"MAE_180D_pct":-37.62,"MAE_1Y_pct":-37.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800.0,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.22,"four_b_timing_verdict":"local_4b_watch_not_full_exit","four_b_evidence_type":["valuation_blowoff","positioning_overheat","execution_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_subsidy_pmt_direct_but_price_phase_bad","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_s_ratio_check","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005930|2024-04-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C31_L219_02","case_id":"C31_L219_02_SAMSUNG_FINAL_AWARD_AFTER_RESET","symbol":"005930","company_name":"삼성전자","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2024-12-20","evidence_available_at_that_date":"NIST / U.S. Department of Commerce, 2024-12-20, final CHIPS award to Samsung Electronics up to $4.745B; URL: https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-award-samsung","evidence_source":"https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-award-samsung","stage2_evidence_fields":["named_policy_or_subsidy_event","issuer_or_jv_route_visible","chips_final_award_after_due_diligence_and_price_reset"],"stage3_evidence_fields":["final_award_or_cash_recognition"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-23","entry_price":53500.0,"MFE_30D_pct":7.85,"MFE_90D_pct":15.89,"MFE_180D_pct":50.47,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.05,"MAE_90D_pct":-5.05,"MAE_180D_pct":-5.05,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-09-18","peak_price":80500.0,"drawdown_after_peak_pct":-2.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"final_award_plus_reset_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_s_ratio_check","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005930|2024-12-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_final_award_after_preliminary_pmt","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C31_L219_03","case_id":"C31_L219_03_SKHYNIX_PMT_HBM_PACKAGING_ROUTE","symbol":"000660","company_name":"SK하이닉스","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-06","evidence_available_at_that_date":"NIST / U.S. Department of Commerce, 2024-08-06, preliminary terms with SK hynix for up to $450M direct funding plus up to $500M loans; URL: https://www.nist.gov/news-events/news/2024/08/us-department-commerce-announces-preliminary-terms-sk-hynix-advance-us-ai-0","evidence_source":"https://www.nist.gov/news-events/news/2024/08/us-department-commerce-announces-preliminary-terms-sk-hynix-advance-us-ai-0","stage2_evidence_fields":["named_policy_or_subsidy_event","issuer_or_jv_route_visible","chips_pmt_named_hbm_packaging_and_rd_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-07","entry_price":169300.0,"MFE_30D_pct":19.61,"MFE_90D_pct":21.68,"MFE_180D_pct":34.08,"MFE_1Y_pct":81.04,"MFE_2Y_pct":null,"MAE_30D_pct":-14.53,"MAE_90D_pct":-14.53,"MAE_180D_pct":-14.53,"MAE_1Y_pct":-14.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-22","peak_price":227000.0,"drawdown_after_peak_pct":-28.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"issuer_specific_subsidy_with_customer_route_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_s_ratio_check","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|000660|2024-08-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C31_L219_04","case_id":"C31_L219_04_SKHYNIX_FINAL_AWARD_DUE_DILIGENCE","symbol":"000660","company_name":"SK하이닉스","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2024-12-19","evidence_available_at_that_date":"NIST / U.S. Department of Commerce, 2024-12-19, final CHIPS award to SK hynix up to $458M direct funding; URL: https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-award-sk-hynix","evidence_source":"https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-award-sk-hynix","stage2_evidence_fields":["named_policy_or_subsidy_event","issuer_or_jv_route_visible","chips_final_award_named_hbm_route"],"stage3_evidence_fields":["final_award_or_cash_recognition"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-20","entry_price":168500.0,"MFE_30D_pct":34.72,"MFE_90D_pct":34.72,"MFE_180D_pct":110.09,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.83,"MAE_90D_pct":-3.44,"MAE_180D_pct":-3.44,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2025-09-16","peak_price":354000.0,"drawdown_after_peak_pct":-6.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"final_award_direct_cash_route_strong_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_s_ratio_check","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|000660|2024-12-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_final_award_after_preliminary_pmt","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C31_L219_05","case_id":"C31_L219_05_SKC_ABSOLICS_FINAL_AWARD","symbol":"011790","company_name":"SKC","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-05","evidence_available_at_that_date":"NIST / U.S. Department of Commerce, 2024-12-05, final CHIPS award to Absolics, an affiliate of Korea-based SKC, up to $75M; URL: https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-awards-absolics-and","evidence_source":"https://www.nist.gov/news-events/news/2024/12/biden-harris-administration-announces-chips-incentives-awards-absolics-and","stage2_evidence_fields":["named_policy_or_subsidy_event","issuer_or_jv_route_visible","chips_final_award_advanced_packaging_material_affiliate"],"stage3_evidence_fields":["final_award_or_cash_recognition"],"stage4b_evidence_fields":["event_after_local_rerating","price_phase_or_execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-06","entry_price":97500.0,"MFE_30D_pct":85.64,"MFE_90D_pct":85.64,"MFE_180D_pct":85.64,"MFE_1Y_pct":85.64,"MFE_2Y_pct":null,"MAE_30D_pct":-7.38,"MAE_90D_pct":-11.59,"MAE_180D_pct":-11.9,"MAE_1Y_pct":-11.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-20","peak_price":181000.0,"drawdown_after_peak_pct":-52.54,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_not_full_exit","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"small_direct_subsidy_positive_but_4b_after_spike","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_s_ratio_check","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|011790|2024-12-06","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C31_L219_06","case_id":"C31_L219_06_LGES_Q1_AMPC_RESULT_ONLY_TRAP","symbol":"373220","company_name":"LG에너지솔루션","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2023-04-26","evidence_available_at_that_date":"LG Energy Solution press release, 2023-04-26, Q1 operating profit included KRW100.3B estimated AMPC under IRA Section 45X; URL: https://news.lgensol.com/company-news/press-releases/1705/","evidence_source":"https://news.lgensol.com/company-news/press-releases/1705/","stage2_evidence_fields":["named_policy_or_subsidy_event","issuer_or_jv_route_visible","ira_ampc_recognized_in_operating_profit_ex_credit_guard"],"stage3_evidence_fields":["final_award_or_cash_recognition"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-27","entry_price":587000.0,"MFE_30D_pct":4.6,"MFE_90D_pct":5.62,"MFE_180D_pct":5.62,"MFE_1Y_pct":5.62,"MFE_2Y_pct":5.62,"MAE_30D_pct":-9.71,"MAE_90D_pct":-12.61,"MAE_180D_pct":-36.71,"MAE_1Y_pct":-39.01,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":620000.0,"drawdown_after_peak_pct":-40.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"recognized_ampc_result_only_not_durable_conversion","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_s_ratio_check","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|373220|2023-04-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C31_L219_07","case_id":"C31_L219_07_SKINNOVATION_BLUEOVAL_CONDITIONAL_LOAN","symbol":"096770","company_name":"SK이노베이션","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-22","evidence_available_at_that_date":"U.S. DOE LPO bulletin, 2023-06-22, conditional commitment up to $9.2B loan to BlueOval SK LLC; URL: https://content.govdelivery.com/accounts/USDOELPO/bulletins/3614c1e","evidence_source":"https://content.govdelivery.com/accounts/USDOELPO/bulletins/3614c1e","stage2_evidence_fields":["named_policy_or_subsidy_event","issuer_or_jv_route_visible","atvm_conditional_loan_to_jv_parent_cashflow_uncertain"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv","profile_path":"atlas/symbol_profiles/096/096770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-23","entry_price":182600.0,"MFE_30D_pct":25.68,"MFE_90D_pct":25.68,"MFE_180D_pct":25.68,"MFE_1Y_pct":25.68,"MFE_2Y_pct":25.68,"MAE_30D_pct":-13.58,"MAE_90D_pct":-34.23,"MAE_180D_pct":-41.13,"MAE_1Y_pct":-45.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":229500.0,"drawdown_after_peak_pct":-53.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"huge_policy_financing_not_parent_cashflow","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_s_ratio_check","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|096770|2023-06-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C31_L219_08","case_id":"C31_L219_08_SAMSUNGSDI_STARPLUS_CONDITIONAL_LOAN","symbol":"006400","company_name":"삼성SDI","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-12-02","evidence_available_at_that_date":"U.S. DOE LPO, 2024-12-02, conditional commitment up to $7.54B loan to StarPlus Energy LLC; URL: https://www.energy.gov/edf/articles/lpo-announces-conditional-commitment-starplus-energy-construct-lithium-ion-battery","evidence_source":"https://www.energy.gov/edf/articles/lpo-announces-conditional-commitment-starplus-energy-construct-lithium-ion-battery","stage2_evidence_fields":["named_policy_or_subsidy_event","issuer_or_jv_route_visible","atvm_conditional_loan_to_jv_without_near_term_conversion"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-03","entry_price":261000.0,"MFE_30D_pct":2.68,"MFE_90D_pct":2.68,"MFE_180D_pct":2.68,"MFE_1Y_pct":35.82,"MFE_2Y_pct":null,"MAE_30D_pct":-12.07,"MAE_90D_pct":-34.87,"MAE_180D_pct":-39.58,"MAE_1Y_pct":-39.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":268000.0,"drawdown_after_peak_pct":-41.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"conditional_loan_direct_but_no_near_term_equity_conversion","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_s_ratio_check","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|006400|2024-12-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_L219_01_SAMSUNG_PMT_AFTER_MEMORY_RERATING","trigger_id":"TRG_C31_L219_01","symbol":"005930","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":13,"valuation_repricing_score":2,"execution_risk_score":11,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":2,"execution_risk_score":13,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_components":["policy_cashflow_specificity_gate","final_award_vs_pmt_split","conditional_loan_parent_cashflow_discount","result_only_ex_credit_guard"],"component_delta_explanation":"Shadow profile separates policy existence from issuer-level cashflow conversion; final awards and recognized cash bridge are upgraded only when price phase and ex-credit/parent-cashflow route are not broken.","MFE_90D_pct":11.0,"MAE_90D_pct":-12.25,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_L219_02_SAMSUNG_FINAL_AWARD_AFTER_RESET","trigger_id":"TRG_C31_L219_02","symbol":"005930","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":9,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":15,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":2},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":9,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":15,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":2},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["policy_cashflow_specificity_gate","final_award_vs_pmt_split","conditional_loan_parent_cashflow_discount","result_only_ex_credit_guard"],"component_delta_explanation":"Shadow profile separates policy existence from issuer-level cashflow conversion; final awards and recognized cash bridge are upgraded only when price phase and ex-credit/parent-cashflow route are not broken.","MFE_90D_pct":15.89,"MAE_90D_pct":-5.05,"score_return_alignment_label":"current_profile_too_late","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_L219_03_SKHYNIX_PMT_HBM_PACKAGING_ROUTE","trigger_id":"TRG_C31_L219_03","symbol":"000660","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":7,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":13,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":2},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":7,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":13,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":2},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","changed_components":["policy_cashflow_specificity_gate","final_award_vs_pmt_split","conditional_loan_parent_cashflow_discount","result_only_ex_credit_guard"],"component_delta_explanation":"Shadow profile separates policy existence from issuer-level cashflow conversion; final awards and recognized cash bridge are upgraded only when price phase and ex-credit/parent-cashflow route are not broken.","MFE_90D_pct":21.68,"MAE_90D_pct":-14.53,"score_return_alignment_label":"current_profile_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_L219_04_SKHYNIX_FINAL_AWARD_DUE_DILIGENCE","trigger_id":"TRG_C31_L219_04","symbol":"000660","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":9,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":15,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":2},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":9,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":15,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":2},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["policy_cashflow_specificity_gate","final_award_vs_pmt_split","conditional_loan_parent_cashflow_discount","result_only_ex_credit_guard"],"component_delta_explanation":"Shadow profile separates policy existence from issuer-level cashflow conversion; final awards and recognized cash bridge are upgraded only when price phase and ex-credit/parent-cashflow route are not broken.","MFE_90D_pct":34.72,"MAE_90D_pct":-3.44,"score_return_alignment_label":"current_profile_too_late","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_L219_05_SKC_ABSOLICS_FINAL_AWARD","trigger_id":"TRG_C31_L219_05","symbol":"011790","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":9,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":15,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":2},"weighted_score_before":58,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":9,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":15,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":2},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["policy_cashflow_specificity_gate","final_award_vs_pmt_split","conditional_loan_parent_cashflow_discount","result_only_ex_credit_guard"],"component_delta_explanation":"Shadow profile separates policy existence from issuer-level cashflow conversion; final awards and recognized cash bridge are upgraded only when price phase and ex-credit/parent-cashflow route are not broken.","MFE_90D_pct":85.64,"MAE_90D_pct":-11.59,"score_return_alignment_label":"current_profile_missed_structural","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_L219_06_LGES_Q1_AMPC_RESULT_ONLY_TRAP","trigger_id":"TRG_C31_L219_06","symbol":"373220","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":13,"valuation_repricing_score":4,"execution_risk_score":10,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":4,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_after":66,"stage_label_after":"Stage2-Actionable","changed_components":["policy_cashflow_specificity_gate","final_award_vs_pmt_split","conditional_loan_parent_cashflow_discount","result_only_ex_credit_guard"],"component_delta_explanation":"Shadow profile separates policy existence from issuer-level cashflow conversion; final awards and recognized cash bridge are upgraded only when price phase and ex-credit/parent-cashflow route are not broken.","MFE_90D_pct":5.62,"MAE_90D_pct":-12.61,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_L219_07_SKINNOVATION_BLUEOVAL_CONDITIONAL_LOAN","trigger_id":"TRG_C31_L219_07","symbol":"096770","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":3,"customer_quality_score":6,"policy_or_regulatory_score":13,"valuation_repricing_score":4,"execution_risk_score":11,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":3,"customer_quality_score":6,"policy_or_regulatory_score":10,"valuation_repricing_score":4,"execution_risk_score":13,"legal_or_contract_risk_score":9,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_after":55,"stage_label_after":"Stage2","changed_components":["policy_cashflow_specificity_gate","final_award_vs_pmt_split","conditional_loan_parent_cashflow_discount","result_only_ex_credit_guard"],"component_delta_explanation":"Shadow profile separates policy existence from issuer-level cashflow conversion; final awards and recognized cash bridge are upgraded only when price phase and ex-credit/parent-cashflow route are not broken.","MFE_90D_pct":25.68,"MAE_90D_pct":-34.23,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_L219_08_SAMSUNGSDI_STARPLUS_CONDITIONAL_LOAN","trigger_id":"TRG_C31_L219_08","symbol":"006400","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":3,"customer_quality_score":6,"policy_or_regulatory_score":13,"valuation_repricing_score":4,"execution_risk_score":11,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":3,"customer_quality_score":6,"policy_or_regulatory_score":10,"valuation_repricing_score":4,"execution_risk_score":13,"legal_or_contract_risk_score":9,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_after":54,"stage_label_after":"Stage2","changed_components":["policy_cashflow_specificity_gate","final_award_vs_pmt_split","conditional_loan_parent_cashflow_discount","result_only_ex_credit_guard"],"component_delta_explanation":"Shadow profile separates policy existence from issuer-level cashflow conversion; final awards and recognized cash bridge are upgraded only when price phase and ex-credit/parent-cashflow route are not broken.","MFE_90D_pct":2.68,"MAE_90D_pct":-34.87,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"aggregate","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_US_INDUSTRIAL_POLICY_SUBSIDY_TO_CASHFLOW_CONVERSION_GUARD","calibration_usable_case_count":8,"calibration_usable_trigger_count":8,"new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":6,"same_archetype_new_symbol_count":6,"new_trigger_family_count":8,"same_archetype_new_trigger_family_count":8,"positive_case_count":4,"counterexample_count":4,"stage4b_case_count":2,"stage4c_case_count":0,"current_profile_error_count":7,"avg_MFE_90D_pct":25.36,"avg_MAE_90D_pct":-16.07,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"production_scoring_changed":false}
{"row_type":"residual_contribution","round":"R11","loop":"219","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_headline_false_positive","preliminary_terms_after_rerating_4B_watch","conditional_loan_parent_cashflow_gap","recognized_subsidy_result_only_green_trap","final_award_after_reset_missed_structural"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"sector_specific_rule_candidate":"L10 policy/event evidence should split public program existence, named issuer route, legal/funding finality, cashflow sufficiency, and price phase.","canonical_archetype_rule_candidate":"C31 should separate preliminary policy terms, final awarded funding, recognized subsidy in operating profit, conditional JV loans, and issuer-level cashflow conversion. Finality and cashflow route are promotion gates; conditional financing or result-only subsidy is capped unless ex-credit/parent conversion is visible.","new_axis_proposed":"c31_awarded_policy_cashflow_finality_ladder; c31_pmt_vs_final_award_phase_guard; c31_conditional_loan_parent_cashflow_discount; c31_result_only_subsidy_green_trap_cap","existing_axis_strengthened":"stage2_required_bridge; local_4b_watch_guard; stage3_green_revision_min_by_cashflow_finality","existing_axis_weakened":"none in production; shadow-only weakening of policy headline directness for PMT/conditional-loan rows"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R11
completed_loop = 219
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy/MFE-MAE repair + Priority 2 C31 direct policy cashflow conversion compression
next_recommended_archetypes = C31 only for non-semi/battery direct awarded cashflow rows; otherwise rotate to C15 spread freshness, C01/C05 direct FCF conversion, C13 utilization/ex-credit rows, or R13 only for non-duplicate taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt used: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat index used only as duplicate/coverage ledger: `docs/core/V12_Research_No_Repeat_Index.md`.
- Stock-Web manifest/schema used for price basis and MFE/MAE rules.
- Evidence URLs are included in section 9 and the JSONL rows.
