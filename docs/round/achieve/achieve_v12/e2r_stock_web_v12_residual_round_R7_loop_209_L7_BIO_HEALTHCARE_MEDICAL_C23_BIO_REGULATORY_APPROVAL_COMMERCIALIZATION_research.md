# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round: R7
selected_loop: 209
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 3/4/5 quality reinforcement after all C01~C32 >= 80 representative rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1
loop_objective: sector_specific_rule_discovery | residual_false_positive_mining | stage2_actionable_bonus_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This file is a standalone v12 post-calibrated historical residual research output. It is not a live stock recommendation, not a current watchlist, and not a production scoring patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus: +2.0
stage3_yellow_total_min: 75.0
stage3_green_total_min: 87.0
stage3_green_revision_min: 55.0
price_only_blowoff_blocks_positive_stage: true
full_4b_requires_non_price_evidence: true
hard_4c_thesis_break_routes_to_4c: true
```

C23 needs a narrower residual gate: in biotech, a regulatory approval is a spark, but revenue conversion is the fire. The same word “FDA approval” can mean a global commercial route with royalties, or a partner-dependent launch that never becomes visible in Korean equity economics.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R7 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION |
| fine_archetype_id | C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1 |
| scope validity | pass |
| R7 hard gate | L7 only; pass |

## 3. Previous Coverage / Duplicate Avoidance Check

The no-repeat index and coverage matrix show a mature corpus, not a raw row shortage: 11,200 representative rows, 962 symbols, and all canonical archetypes covered. C23 has 263 representative rows but only 24 positives and 21 counterexamples, with high evidence URL pending/proxy counts. Therefore this loop selects C23 quality reinforcement rather than simple row filling.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
current loop duplicate check = pass
new_independent_case_count = 6
reused_case_count = 0
new_symbol_count = 6
same_archetype_new_trigger_family_count = 4
```

New trigger families in this loop:

1. FDA approval + named commercial/royalty bridge.
2. FDA-approved product commercial availability / launch conversion.
3. Approval-only or partner-dependent commercialization false positive.
4. Regulatory rejection / CRL hard-4C with reopen clock.
5. Non-U.S. major-regulator approval with demand/cash-conversion gap.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```text
source_name: FinanceData/marcap
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

MFE/MAE calculation follows the v12 rule:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
N = 30 / 90 / 180 trading days
```

## 5. Historical Eligibility Gate

| symbol | shard | profile | corporate action window | profile corporate action dates |
|---|---|---|---|---|
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | atlas/symbol_profiles/145/145020.json | clean_180D_window | 2017-07-31, 2020-07-08, 2020-07-31 |
| 068270 | atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv | atlas/symbol_profiles/068/068270.json | clean_180D_window | 2006-10-13, 2008-06-10, 2008-09-24, 2012-06-29, 2013-03-22, 2024-01-12 |
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | clean_180D_window | 1997-01-03, 1999-08-26, 2020-04-08 |
| 128940 | atlas/ohlcv_tradable_by_symbol_year/128/128940/2022.csv | atlas/symbol_profiles/128/128940.json | clean_180D_window | none |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | clean_180D_window | 1997-01-03, 1998-11-28, 2000-04-10, 2000-04-25, 2000-07-14, 2002-04-02, 2003-10-28, 2003-12-17, 2005-02-22, 2005-06-01, 2007-01-08, 2007-11-29, 2008-12-02, 2009-01-07, 2010-02-23, 2011-01-05, 2021-03-15, 2021-04-01 |
| 302440 | atlas/ohlcv_tradable_by_symbol_year/302/302440/2023.csv | atlas/symbol_profiles/302/302440.json | clean_180D_window | none |

All six usable trigger rows have actual entry OHLCV, at least 180 trading days of forward path in stock-web, and clean 180D corporate-action windows.

## 6. Canonical Archetype Compression Map

| fine/deep subtype | canonical compression | rule implication |
|---|---|---|
| FDA approval + named global commercial partner | C23 | Stage2-Actionable allowed; Yellow only with economics bridge |
| FDA-approved product commercial launch | C23 | Stage2-Actionable allowed; Green needs payer/revenue visibility |
| Approval-only / partner-dependent commercialization | C23 | Stage2 cap; Green blocker |
| Major-regulator approval with demand gap | C23 | Stage2 cap or watch |
| Complete response letter / rejection | C23 | Stage4C allowed, but add reopen clock |

## 7. Case Selection Summary

| symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | role | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| 145020 | Hugel | Stage2-Actionable | 2024-03-04 | 2024-03-04 | 202500 | 29.63 | -14.91 | 60.99 | -14.91 | positive | current_profile_correct |
| 068270 | Celltrion | Stage2-Actionable | 2024-03-18 | 2024-03-18 | 182500 | 12.33 | -7.01 | 15.62 | -12.16 | positive | current_profile_correct |
| 000100 | Yuhan | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94300 | 76.99 | -2.97 | 76.99 | -2.97 | positive | current_profile_too_late |
| 128940 | Hanmi Pharm | Stage2-Actionable | 2022-09-09 | 2022-09-13 | 305000 | 7.05 | -26.72 | 11.31 | -26.72 | counterexample | current_profile_false_positive |
| 028300 | HLB | Stage4C | 2024-05-17 | 2024-05-17 | 67100 | 46.20 | -32.71 | 46.20 | -32.71 | counterexample | current_profile_correct |
| 302440 | SK Bioscience | Stage2 | 2023-05-30 | 2023-05-30 | 81600 | 8.58 | -19.85 | 8.58 | -30.02 | counterexample | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count: 3
counterexample_count: 3
4B_case_count: 0
4C_case_count: 1
current_profile_error_count: 3
minimum_positive_case_count: pass
minimum_counterexample_count: pass
minimum_calibration_usable_case_count: pass
```

Positive controls: Yuhan, Hugel, Celltrion. Counterexamples / guardrails: Hanmi, SK Bioscience, HLB CRL.

## 9. Evidence Source Map

| symbol | company | source family | URL | evidence note |
|---|---|---|---|---|
| 145020 | Hugel | Hugel America press release / Drugs.com FDA Approval History | https://hugel-aesthetics.com/news-press-releases/ ; https://www.drugs.com/history/letybo.html | FDA approval of Letybo for U.S. glabellar-lines market, followed by commercial route/launch planning rather than a pure approval headline. |
| 068270 | Celltrion | Celltrion USA press release | https://www.celltrion.com/en-us/company/media-center/press-release/3128 | ZYMFENTRA, already FDA-approved in 2023, became commercially available in the U.S.; this is an approval-to-launch conversion row rather than a binary approval row. |
| 000100 | Yuhan | FDA approval page / Yuhan USA release | https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer ; https://www.yuhan-usa.com/rybrevant-plus-lazcluze-by-johnson-johnson-got-approved-by-the-u-s-fda-as-a-first-line-chemotherapy-free-treatment-for-patients-with-egfr-mutated-advanced-lung-cancer-lazcl/ | FDA approved lazertinib/Lazcluze in combination with amivantamab/Rybrevant; Yuhan had licensed lazertinib to Janssen, making this a stronger royalty/commercialization bridge than an ordinary domestic approval. |
| 128940 | Hanmi Pharm | Spectrum SEC exhibit / KED Global / Drugs.com approval history | https://www.sec.gov/Archives/edgar/data/831547/000119312522242330/d401699dex991.htm ; https://www.kedglobal.com/bio-pharma/newsView/ked202209130009 ; https://www.drugs.com/history/rolvedon.html | Rolvedon/eflapegrastim received FDA approval through Spectrum, but Hanmi equity rerating required launch traction, economics, and partner execution rather than the approval alone. |
| 028300 | HLB | Korea Times / KED Global / BioWorld | https://www.koreatimes.co.kr/business/companies/20240517/south-korean-drugmaker-hlb-hit-by-us-fdas-rejection-of-rivoceranib-liver-cancer-drug ; https://www.kedglobal.com/bio-pharma/newsView/ked202405170019 ; https://www.bioworld.com/keywords/45665-hlb-co-ltd | FDA complete response letter/rejection for rivoceranib plus camrelizumab HCC approval attempt; listed HLB affiliates hit lower limits, but later rebound requires 4C not to stay sticky after resubmission/recovery evidence. |
| 302440 | SK Bioscience | SK bioscience official release / PRNewswire | https://www.skbioscience.com/en/news/news_01_01?id=212&mode=2 ; https://www.prnewswire.com/news-releases/sk-bioscience-receives-marketing-authorization-of-covid-19-vaccine-from-uk-mhra-301836956.html | UK MHRA marketing authorization for SKYCovion/SKYCovione created regulatory credibility, but COVID-vaccine demand and conversion-to-cash were not visible enough for Actionable/Yellow. |

## 10. Price Data Source Map

The entry-year shards were downloaded from the stock-web tradable shard path pattern. Multi-year forward windows were calculated by concatenating the relevant year files already opened in this session.

| symbol | entry shard | entry OHLCV source status |
|---|---|---|
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | usable |
| 068270 | atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv | usable |
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv + 2025.csv | usable |
| 128940 | atlas/ohlcv_tradable_by_symbol_year/128/128940/2022.csv + 2023.csv | usable |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv + 2025.csv | usable |
| 302440 | atlas/ohlcv_tradable_by_symbol_year/302/302440/2023.csv + 2024.csv | usable |

## 11. Case-by-Case Trigger Grid

### 11.1 Hugel / 145020 — FDA approval with U.S. launch route

- Stage2 evidence: FDA approval, U.S. market access, product commercialization route.
- Stage3 evidence: launch/shipments still required; approval alone is not Green.
- Backtest: MFE180 +60.99%, MAE180 -14.91%.
- Verdict: Stage2-Actionable is justified; Green requires launch economics.

### 11.2 Celltrion / 068270 — ZYMFENTRA commercial availability

- Stage2 evidence: U.S. commercial availability, FDA-approved product, proprietary route.
- Stage3 evidence: payer/PBM/prescription conversion still required.
- Backtest: MFE180 +15.62%, MAE180 -12.16%.
- Verdict: approval-to-launch conversion supports Actionable, not Yellow/Green.

### 11.3 Yuhan / 000100 — Lazcluze approval with licensed global partner bridge

- Stage2 evidence: FDA approval, named J&J/Janssen commercialization route, licensed drug economics.
- Stage3 evidence: stronger than approval-only because royalty/commercial route is explicit.
- Backtest: MFE180 +76.99%, MAE180 -2.97%.
- Verdict: current profile may be too late if it treats this as ordinary biotech optionality.

### 11.4 Hanmi Pharm / 128940 — Rolvedon approval but partner/economics gap

- Stage2 evidence: FDA approval.
- Missing bridge: Korean equity economics, launch traction, partner execution, repeat revenue conversion.
- Backtest: MFE180 +11.31%, MAE180 -26.72%.
- Verdict: approval-only Actionable is false-positive risk; cap below Yellow.

### 11.5 HLB / 028300 — FDA CRL / rejection hard 4C

- 4C evidence: regulatory rejection / CRL, thesis evidence broken.
- Backtest: MAE30 -32.71%, but MFE90/180 +46.20% after later rebound.
- Verdict: hard 4C is valid at rejection date, but must include a reopen clock once resubmission/regulatory path returns.

### 11.6 SK Bioscience / 302440 — MHRA approval without demand conversion

- Stage2 evidence: major-regulator marketing authorization.
- Missing bridge: post-pandemic demand, order/contract visibility, revenue/cash conversion.
- Backtest: MFE180 +8.58%, MAE180 -30.02%.
- Verdict: regulatory approval should remain Stage2 cap unless demand/cash bridge appears.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | actual entry OHLCV | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak date / price | drawdown after peak |
|---|---|---|---|---|---|---|---|---|
| C23_R7_L209_T01 | 145020 | 2024-03-04 | O=199800 H=219000 L=193400 C=202500 V=277773 | 8.15/-14.91 | 29.63/-14.91 | 60.99/-14.91 | 2024-11-07 / 326000 | -22.85 |
| C23_R7_L209_T02 | 068270 | 2024-03-18 | O=180900 H=184400 L=180300 C=182500 V=534945 | 6.36/-7.01 | 12.33/-7.01 | 15.62/-12.16 | 2024-07-30 / 211000 | -24.03 |
| C23_R7_L209_T03 | 000100 | 2024-08-21 | O=103000 H=109700 L=93800 C=94300 V=13922671 | 69.99/-2.97 | 76.99/-2.97 | 76.99/-2.97 | 2024-10-15 / 166900 | -39.84 |
| C23_R7_L209_T04 | 128940 | 2022-09-13 | O=326500 H=326500 L=303000 C=305000 V=162456 | 7.05/-26.72 | 7.05/-26.72 | 11.31/-26.72 | 2023-04-14 / 339500 | -14.43 |
| C23_R7_L209_T05 | 028300 | 2024-05-17 | O=67100 H=67100 L=67100 C=67100 V=617840 | 9.99/-32.71 | 46.20/-32.71 | 46.20/-32.71 | 2024-07-08 / 98100 | -40.06 |
| C23_R7_L209_T06 | 302440 | 2023-05-30 | O=81900 H=83000 L=81300 C=81600 V=291548 | 5.39/-12.25 | 8.58/-19.85 | 8.58/-30.02 | 2023-08-03 / 88600 | -35.55 |

## 13. Current Calibrated Profile Stress Test

| symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90 | MAE90 | current_profile_verdict |
|---|---:|---|---:|---|---:|---:|---|
| 145020 | 76 | Stage2-Actionable | 79 | Stage2-Actionable | 29.63 | -14.91 | current_profile_correct |
| 068270 | 74 | Stage2-Actionable | 76 | Stage2-Actionable | 12.33 | -7.01 | current_profile_correct |
| 000100 | 84 | Stage2-Actionable | 88 | Stage3-Yellow | 76.99 | -2.97 | current_profile_too_late |
| 128940 | 74 | Stage2-Actionable | 62 | Stage2 | 7.05 | -26.72 | current_profile_false_positive |
| 028300 | 38 | Stage4C | 34 | Stage4C | 46.20 | -32.71 | current_profile_correct |
| 302440 | 66 | Stage2 | 55 | Stage2 | 8.58 | -19.85 | current_profile_false_positive |

Stress-test answers:

1. The current profile is directionally correct for direct approval + commercial route, but still too coarse for partner-dependent approval-only rows.
2. Stage2-Actionable bonus is useful for Yuhan/Hugel/Celltrion but too generous for Hanmi/SK Bioscience if no second bridge appears.
3. Yellow threshold 75 is appropriate; it blocks Hanmi/SK Bioscience and keeps Celltrion/Hugel below Green until launch economics appear.
4. Green threshold 87 / revision 55 should not be loosened.
5. Hard 4C routing is correct for HLB CRL, but the path needs a reopen clock.

## 14. Stage2 / Yellow / Green Comparison

| subtype | Stage2 | Stage2-Actionable | Stage3-Yellow | Stage3-Green |
|---|---|---|---|---|
| binary approval only | allowed | usually blocked | blocked | blocked |
| approval + named commercial/royalty route | allowed | allowed | possible after economic bridge | blocked until repeat revenue/revision |
| commercial availability | allowed | allowed | possible after payer/coverage uptake | blocked until revenue conversion |
| CRL/regulatory rejection | not applicable | not applicable | not applicable | not applicable |

Green lateness ratio: not applicable because no confirmed Stage3-Green trigger is used in this file. The positive residual is about preserving Stage2-Actionable on direct commercial bridge rows, not lowering Green.

## 15. 4B Local vs Full-window Timing Audit

No representative Stage4B trigger is emitted in this file. 4B logic is still tested conceptually through Hanmi/SK Bioscience as approval-only watch/cap rows, but all machine-readable rows are Stage2 / Stage2-Actionable / Stage4C.

```text
four_b_local_peak_proximity: not_applicable
four_b_full_window_peak_proximity: not_applicable
four_b_timing_verdict: no_4B_trigger_in_loop
full_4b_requires_non_price_evidence: kept
```

## 16. 4C Protection Audit

HLB is the hard 4C row.

```text
trigger_id: C23_R7_L209_T05
entry_date: 2024-05-17
entry_price: 67,100
MAE_30D_pct: -32.71
MAE_90D_pct: -32.71
MAE_180D_pct: -32.71
MFE_90D_pct: +46.20
four_c_protection_label: hard_4c_success_with_reopen_watch
```

Interpretation: the CRL was a real non-price thesis break and protected against immediate further downside. However, because the stock later rebounded strongly, the C23 4C rule must be a thesis-break state with a reopen condition, not a permanent deletion label.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate: L7_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE
rule_scope: sector_specific
proposal_type: shadow_only
```

Rule:

```text
In L7, regulatory approval alone may create Stage2, but Stage2-Actionable requires at least one second bridge:
- named commercial partner / royalty route,
- launch / first shipment / commercial availability,
- payer or prescription route,
- revenue or margin conversion,
- repeat approval-to-sales evidence.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: C23_REGULATORY_APPROVAL_TO_REVENUE_CONVERSION_GATE_V1
rule_scope: canonical_archetype_specific
proposal_type: shadow_only
```

Rule:

```text
C23 should split approval events into three buckets:
1. approval_only_cap: Stage2 only, Green blocked.
2. approval_plus_commercial_route: Stage2-Actionable allowed.
3. approval_plus_realized economics: Yellow candidate, Green still requires durable revision/revenue.
CRL/rejection routes to Stage4C, but a resubmission/reinspection/approval path can reopen to Stage4B/watch or Stage2.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Existing calibrated profile; approval evidence may still be too coarse inside C23. | none | 6 | 30.13 | -17.36 | 36.62 | -19.91 | 0.33 | 1 | mixed: positive controls exist but approval-only false positives remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Older baseline likely over-promotes binary FDA/MHRA events without launch economics. | none | 6 | 30.13 | -17.36 | 36.62 | -19.91 | 0.50 | 1 | worse false-positive control |
| P1_L7_sector_candidate | sector_specific | Require approval-to-commercialization second bridge for L7 regulatory rows. | commercialization_second_bridge_required | 6 | 30.13 | -17.36 | 36.62 | -19.91 | 0.17 | 0 | better risk separation |
| P2_C23_archetype_candidate | canonical_archetype_specific | Reward FDA approval plus named commercial/royalty route; cap approval-only rows. | approval_only_cap + launch_economics_bonus | 6 | 30.13 | -17.36 | 36.62 | -19.91 | 0.17 | 0 | best explanatory fit |
| P3_counterexample_guard | canonical_guard | Stage2 allowed, but Yellow/Green blocked unless payer, launch, royalty, or revenue bridge appears. | green_blocker_strengthened | 6 | 30.13 | -17.36 | 36.62 | -19.91 | 0.17 | 0 | conservative but robust |


## 20. Score-Return Alignment Matrix

| verdict | cases | price alignment |
|---|---:|---|
| current_profile_correct | 3 | Hugel/Celltrion/HLB were broadly handled correctly if Green stays blocked and HLB gets 4C reopen watch. |
| current_profile_too_late | 1 | Yuhan had an unusually clean licensed-partner approval bridge and very strong forward path. |
| current_profile_false_positive | 2 | Hanmi/SK Bioscience show approval-only or demand-gap rows with low MFE and deep MAE. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1 | 3 | 3 | 0 | 1 | 6 | 0 | 6 | 6 | 3 | L7_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE | C23_REGULATORY_APPROVAL_TO_REVENUE_CONVERSION_GATE_V1 | C23 approval-only vs commercialization bridge quality improved |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - approval_only_false_positive
  - commercialization_second_bridge_missing
  - licensed_partner_positive_control
  - hard_4c_reopen_clock_needed
new_axis_proposed: no_global_axis
existing_axis_strengthened:
  - stage2_required_bridge
  - stage3_green_not_loosened
existing_axis_weakened: none
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L7_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE
canonical_archetype_rule_candidate: C23_REGULATORY_APPROVAL_TO_REVENUE_CONVERSION_GATE_V1
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical trigger-level backtest only.
- Actual stock-web tradable OHLCV rows.
- 30D / 90D / 180D MFE and MAE for all trigger rows.
- C23 regulatory approval and commercialization evidence.

Non-validation scope:

- No live candidate discovery.
- No current stock recommendation.
- No production scoring patch.
- No medical or investment advice.
- No use of future price in runtime scoring.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,approval_to_commercialization_second_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"FDA/MHRA approval alone did not separate Yuhan/Hugel/Celltrion from Hanmi/SK Bioscience; commercialization or royalty/launch bridge did.","false positives reduced while Yuhan positive retained",C23_R7_L209_T01|C23_R7_L209_T02|C23_R7_L209_T03|C23_R7_L209_T04|C23_R7_L209_T06,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,hard_4c_reopen_clock,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"CRL/rejection protects downside, but HLB rebound shows hard 4C should reopen if resubmission or regulatory path becomes credible.","keeps 4C protection without permanent thesis deletion",C23_R7_L209_T05,1,1,1,low,guardrail_shadow_only,"4C overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","notes":"manifest max_date and raw_unadjusted calibration-safe shard roots verified from stock-web manifest."}
{"row_type":"case","case_id":"C23_145020_2024_03_04_FDA_APPROVAL_US_LAUNCH_BRIDGE","symbol":"145020","company_name":"Hugel","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_with_commercial_route_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Approval was meaningful, but Green should still wait for shipment/revenue evidence. Price path supports Stage2-Actionable but not automatic Green."}
{"row_type":"trigger","trigger_id":"C23_R7_L209_T01","case_id":"C23_145020_2024_03_04_FDA_APPROVAL_US_LAUNCH_BRIDGE","symbol":"145020","company_name":"Hugel","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","sector":"Bio/Healthcare/Medical","primary_archetype":"bio_regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|residual_false_positive_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-04","evidence_available_at_that_date":"FDA approval of Letybo for U.S. glabellar-lines market, followed by commercial route/launch planning rather than a pure approval headline.","evidence_source":"Hugel America press release / Drugs.com FDA Approval History | https://hugel-aesthetics.com/news-press-releases/ ; https://www.drugs.com/history/letybo.html","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["commercialization_route","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-04","entry_price":202500.0,"MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":70.86,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":-14.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000.0,"drawdown_after_peak_pct":-22.85,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"approval_with_commercial_route_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|145020|2024-03-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_145020_2024_03_04_FDA_APPROVAL_US_LAUNCH_BRIDGE","trigger_id":"C23_R7_L209_T01","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":10,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C23-specific second-bridge gate rewards approval+commercial route and caps approval-only or partner-dependent rows until launch economics appear.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"approval_with_commercial_route_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C23_068270_2024_03_18_ZYMFENTRA_COMMERCIAL_AVAILABILITY","symbol":"068270","company_name":"Celltrion","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"commercial_availability_moderate_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Commercial availability supports Stage2-Actionable. Moderate MFE and later drawdown argue against Stage3-Green without payer coverage / prescription conversion."}
{"row_type":"trigger","trigger_id":"C23_R7_L209_T02","case_id":"C23_068270_2024_03_18_ZYMFENTRA_COMMERCIAL_AVAILABILITY","symbol":"068270","company_name":"Celltrion","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","sector":"Bio/Healthcare/Medical","primary_archetype":"bio_regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|residual_false_positive_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-18","evidence_available_at_that_date":"ZYMFENTRA, already FDA-approved in 2023, became commercially available in the U.S.; this is an approval-to-launch conversion row rather than a binary approval row.","evidence_source":"Celltrion USA press release | https://www.celltrion.com/en-us/company/media-center/press-release/3128","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","commercialization_route"],"stage3_evidence_fields":["commercial_availability","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv","profile_path":"atlas/symbol_profiles/068/068270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-18","entry_price":182500.0,"MFE_30D_pct":6.36,"MFE_90D_pct":12.33,"MFE_180D_pct":15.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.01,"MAE_90D_pct":-7.01,"MAE_180D_pct":-12.16,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":211000.0,"drawdown_after_peak_pct":-24.03,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"commercial_availability_moderate_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|068270|2024-03-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_068270_2024_03_18_ZYMFENTRA_COMMERCIAL_AVAILABILITY","trigger_id":"C23_R7_L209_T02","symbol":"068270","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":8,"policy_or_regulatory_score":10,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":4,"customer_quality_score":9,"policy_or_regulatory_score":10,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C23-specific second-bridge gate rewards approval+commercial route and caps approval-only or partner-dependent rows until launch economics appear.","MFE_90D_pct":12.33,"MAE_90D_pct":-7.01,"score_return_alignment_label":"commercial_availability_moderate_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C23_000100_2024_08_21_LAZCLUZE_FDA_APPROVAL","symbol":"000100","company_name":"Yuhan","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"licensed_drug_fda_approval_structural_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"This is the cleanest positive control: direct FDA approval plus named global commercial partner/royalty route. The current profile can become too conservative if it treats this like approval-only biotech optionality."}
{"row_type":"trigger","trigger_id":"C23_R7_L209_T03","case_id":"C23_000100_2024_08_21_LAZCLUZE_FDA_APPROVAL","symbol":"000100","company_name":"Yuhan","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","sector":"Bio/Healthcare/Medical","primary_archetype":"bio_regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|residual_false_positive_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","evidence_available_at_that_date":"FDA approved lazertinib/Lazcluze in combination with amivantamab/Rybrevant; Yuhan had licensed lazertinib to Janssen, making this a stronger royalty/commercialization bridge than an ordinary domestic approval.","evidence_source":"FDA approval page / Yuhan USA release | https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer ; https://www.yuhan-usa.com/rybrevant-plus-lazcluze-by-johnson-johnson-got-approved-by-the-u-s-fda-as-a-first-line-chemotherapy-free-treatment-for-patients-with-egfr-mutated-advanced-lung-cancer-lazcl/","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["commercialization_route","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-21","entry_price":94300.0,"MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":76.99,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":-2.97,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-15","peak_price":166900.0,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"licensed_drug_fda_approval_structural_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|000100|2024-08-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_000100_2024_08_21_LAZCLUZE_FDA_APPROVAL","trigger_id":"C23_R7_L209_T03","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":9,"customer_quality_score":10,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":2,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":9,"customer_quality_score":11,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C23-specific second-bridge gate rewards approval+commercial route and caps approval-only or partner-dependent rows until launch economics appear.","MFE_90D_pct":76.99,"MAE_90D_pct":-2.97,"score_return_alignment_label":"licensed_drug_fda_approval_structural_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C23_128940_2022_09_13_ROLVEDON_APPROVAL_COUNTEREXAMPLE","symbol":"128940","company_name":"Hanmi Pharm","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_without_visible_korea_equity_economics_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Approval-only and partner-dependent commercialization produced deep MAE and small MFE; should be capped below Yellow until launch/economic conversion appears."}
{"row_type":"trigger","trigger_id":"C23_R7_L209_T04","case_id":"C23_128940_2022_09_13_ROLVEDON_APPROVAL_COUNTEREXAMPLE","symbol":"128940","company_name":"Hanmi Pharm","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","sector":"Bio/Healthcare/Medical","primary_archetype":"bio_regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|residual_false_positive_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-09-09","evidence_available_at_that_date":"Rolvedon/eflapegrastim received FDA approval through Spectrum, but Hanmi equity rerating required launch traction, economics, and partner execution rather than the approval alone.","evidence_source":"Spectrum SEC exhibit / KED Global / Drugs.com approval history | https://www.sec.gov/Archives/edgar/data/831547/000119312522242330/d401699dex991.htm ; https://www.kedglobal.com/bio-pharma/newsView/ked202209130009 ; https://www.drugs.com/history/rolvedon.html","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["execution_risk","commercialization_partner_dependency"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/128/128940/2022.csv","profile_path":"atlas/symbol_profiles/128/128940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-09-13","entry_price":305000.0,"MFE_30D_pct":7.05,"MFE_90D_pct":7.05,"MFE_180D_pct":11.31,"MFE_1Y_pct":11.48,"MFE_2Y_pct":null,"MAE_30D_pct":-26.72,"MAE_90D_pct":-26.72,"MAE_180D_pct":-26.72,"MAE_1Y_pct":-26.72,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-14","peak_price":339500.0,"drawdown_after_peak_pct":-14.43,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_4B_trigger","four_b_evidence_type":["execution_risk","commercialization_partner_dependency"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"approval_without_visible_korea_equity_economics_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|128940|2022-09-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_128940_2022_09_13_ROLVEDON_APPROVAL_COUNTEREXAMPLE","trigger_id":"C23_R7_L209_T04","symbol":"128940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":8,"valuation_repricing_score":2,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C23-specific second-bridge gate rewards approval+commercial route and caps approval-only or partner-dependent rows until launch economics appear.","MFE_90D_pct":7.05,"MAE_90D_pct":-26.72,"score_return_alignment_label":"approval_without_visible_korea_equity_economics_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C23_028300_2024_05_17_RIVOCERANIB_CRL_4C","symbol":"028300","company_name":"HLB","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"regulatory_rejection_hard_4c_with_reopen_watch","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Hard 4C is justified at CRL, yet the large rebound means the rule should include a reopen clock if resubmission/regulatory path is restored."}
{"row_type":"trigger","trigger_id":"C23_R7_L209_T05","case_id":"C23_028300_2024_05_17_RIVOCERANIB_CRL_4C","symbol":"028300","company_name":"HLB","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","sector":"Bio/Healthcare/Medical","primary_archetype":"bio_regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|residual_false_positive_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage4C","trigger_date":"2024-05-17","evidence_available_at_that_date":"FDA complete response letter/rejection for rivoceranib plus camrelizumab HCC approval attempt; listed HLB affiliates hit lower limits, but later rebound requires 4C not to stay sticky after resubmission/recovery evidence.","evidence_source":"Korea Times / KED Global / BioWorld | https://www.koreatimes.co.kr/business/companies/20240517/south-korean-drugmaker-hlb-hit-by-us-fdas-rejection-of-rivoceranib-liver-cancer-drug ; https://www.kedglobal.com/bio-pharma/newsView/ked202405170019 ; https://www.bioworld.com/keywords/45665-hlb-co-ltd","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100.0,"MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":46.2,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":-32.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100.0,"drawdown_after_peak_pct":-40.06,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_4B_trigger","four_b_evidence_type":["legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_success_with_reopen_watch","trigger_outcome_label":"regulatory_rejection_hard_4c_with_reopen_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|028300|2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_028300_2024_05_17_RIVOCERANIB_CRL_4C","trigger_id":"C23_R7_L209_T05","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":-8,"valuation_repricing_score":0,"execution_risk_score":10,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":38,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":-8,"valuation_repricing_score":0,"execution_risk_score":10,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":34,"stage_label_after":"Stage4C","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C23-specific second-bridge gate rewards approval+commercial route and caps approval-only or partner-dependent rows until launch economics appear.","MFE_90D_pct":46.2,"MAE_90D_pct":-32.71,"score_return_alignment_label":"regulatory_rejection_hard_4c_with_reopen_watch","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C23_302440_2023_05_30_MHRA_APPROVAL_COMMERCIAL_GAP","symbol":"302440","company_name":"SK Bioscience","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_without_demand_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A regulatory approval without demand/cash conversion should remain Stage2 and may deserve 4B/watch if demand regime is already deteriorating."}
{"row_type":"trigger","trigger_id":"C23_R7_L209_T06","case_id":"C23_302440_2023_05_30_MHRA_APPROVAL_COMMERCIAL_GAP","symbol":"302440","company_name":"SK Bioscience","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_TO_COMMERCIALIZATION_SECOND_BRIDGE_GATE_V1","sector":"Bio/Healthcare/Medical","primary_archetype":"bio_regulatory_approval_to_commercialization","loop_objective":"sector_specific_rule_discovery|residual_false_positive_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2","trigger_date":"2023-05-30","evidence_available_at_that_date":"UK MHRA marketing authorization for SKYCovion/SKYCovione created regulatory credibility, but COVID-vaccine demand and conversion-to-cash were not visible enough for Actionable/Yellow.","evidence_source":"SK bioscience official release / PRNewswire | https://www.skbioscience.com/en/news/news_01_01?id=212&mode=2 ; https://www.prnewswire.com/news-releases/sk-bioscience-receives-marketing-authorization-of-covid-19-vaccine-from-uk-mhra-301836956.html","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["execution_risk","commercialization_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/302/302440/2023.csv","profile_path":"atlas/symbol_profiles/302/302440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-30","entry_price":81600.0,"MFE_30D_pct":5.39,"MFE_90D_pct":8.58,"MFE_180D_pct":8.58,"MFE_1Y_pct":8.58,"MFE_2Y_pct":null,"MAE_30D_pct":-12.25,"MAE_90D_pct":-19.85,"MAE_180D_pct":-30.02,"MAE_1Y_pct":-36.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-03","peak_price":88600.0,"drawdown_after_peak_pct":-35.55,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_4B_trigger","four_b_evidence_type":["execution_risk","commercialization_gap"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"approval_without_demand_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|302440|2023-05-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_302440_2023_05_30_MHRA_APPROVAL_COMMERCIAL_GAP","trigger_id":"C23_R7_L209_T06","symbol":"302440","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":8,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":6,"valuation_repricing_score":1,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage2","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C23-specific second-bridge gate rewards approval+commercial route and caps approval-only or partner-dependent rows until launch economics appear.","MFE_90D_pct":8.58,"MAE_90D_pct":-19.85,"score_return_alignment_label":"approval_without_demand_conversion_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"209","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_not_loosened","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["approval_only_false_positive","commercialization_second_bridge_missing","licensed_partner_positive_control","4C_reopen_clock_needed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

### Rules

1. Use only calibration_usable=true rows for quantitative calibration.
2. Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
3. Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
4. Do not apply global deltas unless multiple large_sector_id values support the same direction.
5. Prefer sector_specific or canonical_archetype_specific shadow profiles.
6. Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
7. 4B rows are overlay/risk calibration only.
8. 4C rows are thesis-break/protection calibration only.
9. price-only rows cannot promote Stage2/Stage3.
10. If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
11. Production scoring must not change unless the user explicitly asks for another promotion batch.

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
completed_round: R7
completed_loop: 209
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 3/4/5 quality reinforcement after all C01~C32 >= 80 representative rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_COMMERCIAL_REVENUE_DIRECT_ROW_REPAIR
  - C24_BIO_TRIAL_DATA_EVENT_RISK_ENDPOINT_SAFETY_4C_DIRECT_REPAIR
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REIMBURSEMENT_TO_PROCEDURE_VOLUME_REPAIR
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Coverage matrix: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/reports/e2r_calibration/v12/coverage_matrix.md
- Stock-web manifest: https://github.com/Songdaiki/stock-web/blob/main/atlas/manifest.json
- Stock-web schema: https://github.com/Songdaiki/stock-web/blob/main/atlas/schema.json
- Stock-web price shards: https://github.com/Songdaiki/stock-web/tree/main/atlas/ohlcv_tradable_by_symbol_year

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
