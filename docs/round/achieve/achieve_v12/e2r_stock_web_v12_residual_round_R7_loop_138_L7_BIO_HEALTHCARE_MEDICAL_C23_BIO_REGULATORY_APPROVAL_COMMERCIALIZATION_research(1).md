# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round: R7
selected_loop: 138
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C23 FDA approval/commercialization bridge, direct URL/proxy repair, approval-event overcredit vs launch/royalty conversion split
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: US_FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE
loop_objective: sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; approval_to_commercialization_timing_test; complete_30_90_180_MFE_MAE
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
```

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_2_rolling_calibrated`. This loop does not repeat global axes. It stress-tests C23-specific residual errors: FDA approval overcredit, partner/manufacturer proxy approval without listed economic bridge, CRL hard-4C timing, launch availability versus actual uptake, and delayed commercialization winners with early drawdown.

## 2. Round / Large Sector / Canonical Archetype Scope

C23 belongs to R7 / L7. Scope is bio/healthcare regulatory approval and commercialization. A regulatory event is not automatically a rerating bridge. The bridge is the road from approval to launch, sales, royalty/milestone recognition, reimbursement, or partner economics. Approval-only evidence is a gate opening; C23 needs proof that patients, payers, distributors, or partners actually walk through it.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot: C23 has 263 representative rows, 38 symbols, positives/counterexamples 24/21, and 4B/4C 21/18. This loop avoids the immediately preceding C21/C22 financial work and uses R7 bio-specific trigger families. Hard duplicate key `canonical_archetype_id + symbol + trigger_type + entry_date` is avoided.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest basis: `tradable_raw`, `raw_unadjusted_marcap`, `atlas/ohlcv_tradable_by_symbol_year`, max_date `2026-02-20`. Every trigger row below has 180 forward tradable rows, required 30D/90D/180D MFE/MAE, and clean 180D corporate-action window by local profile check.

## 5. Historical Eligibility Gate

All seven trigger rows are historical, use stock-web entry close, include 30/90/180D MFE/MAE, and have no D~D+180 corporate-action contamination. 1Y/2Y are intentionally not used in this loop because the prompt's batch-ingest hard gate prioritizes 30/90/180D trigger-level metrics.

## 6. Canonical Archetype Compression Map

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  -> FDA_approval_direct_regulatory
  -> partner_approval_with_listed_economics_gap
  -> commercial_availability_or_first_shipment
  -> sales_royalty_reimbursement_bridge
  -> CRL_GMP_BIMO_clinical_failure_4C
  -> launch_delay_and_high_MAE_4B
```

## 7. Case Selection Summary

| case_id | symbol | company | trigger | type | pos/counter | entry | MFE90 | MAE90 | verdict |
|---|---|---|---|---|---|---|---|---|---|
| C23_R7L138_001_YUHAN_20240820_LAZERTINIB_FDA_APPROVAL | 000100 | 유한양행 | 2024-08-20 Stage3-Yellow | structural_success | positive | 2024-08-21 94300 | 76.99 | -2.97 | current_profile_too_slow_without_approval_bridge |
| C23_R7L138_002_HLB_20240517_RIVOCERANIB_CRL_BIMO_GMP | 028300 | HLB | 2024-05-17 Stage4C | regulatory_break_counterexample | counterexample | 2024-05-17 67100 | 46.2 | -32.71 | current_profile_4c_needed_but_reentry_rule_required |
| C23_R7L138_003_HUGEL_20240304_LETYBO_FDA_APPROVAL | 145020 | 휴젤 | 2024-03-04 Stage3-Yellow | approval_to_commercialization_success | positive | 2024-03-04 202500 | 29.63 | -14.91 | current_profile_correct_but_green_requires_launch_bridge |
| C23_R7L138_004_CELLTRION_20240318_ZYMFENTRA_US_AVAILABILITY | 068270 | 셀트리온 | 2024-03-18 Stage2-Actionable | commercialization_positive_but_modest_mfe | positive | 2024-03-18 182500 | 12.33 | -7.01 | current_profile_green_too_early_without_sales_uptake |
| C23_R7L138_005_GCBIO_20231218_ALYGLO_FDA_APPROVAL | 006280 | 녹십자 | 2023-12-18 Stage2-Actionable | delayed_commercialization_positive | positive | 2023-12-18 120500 | 8.8 | -10.71 | current_profile_needs_drawdown_aware_confirmation |
| C23_R7L138_006_DAEWOONG_20190207_JEUVEAU_FDA_APPROVAL_PARTNER | 069620 | 대웅제약 | 2019-02-01 Stage4B | approval_event_overcredit_counterexample | counterexample | 2019-02-07 204000 | 6.37 | -29.17 | current_profile_false_positive_if_approval_only |
| C23_R7L138_007_HANMI_20220913_ROLVEDON_FDA_APPROVAL_PARTNER | 128940 | 한미약품 | 2022-09-09 Stage4B | approval_event_overcredit_counterexample | counterexample | 2022-09-13 305000 | 7.05 | -26.72 | current_profile_false_positive_without_royalty_sales_bridge |


## 8. Positive vs Counterexample Balance

```text
positive_case_count: 4
counterexample_count: 3
4B_case_count: 2
4C_case_count: 1
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 7
source_proxy_only_count: 2
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 5
```

## 9. Evidence Source Map

| case | evidence family | source |
|---|---|---|
| T01 유한양행 | FDA approval plus partner commercialization / royalty bridge | https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer |
| T02 HLB | CRL / GMP / BIMO inspection break | https://elevartx.com/2024/09/23/elevar-therapeutics-resubmits-new-drug-application/ |
| T03 휴젤 | FDA approval of Letybo for glabellar lines | https://hugel-aesthetics.com/news-press-releases/ |
| T04 셀트리온 | ZYMFENTRA U.S. commercial availability | https://www.celltrion.com/en-us/company/media-center/press-release/3128 |
| T05 녹십자 | FDA approval for ALYGLO | https://www.gcbiopharma.com/eng/news_view.do?currentPage=1&idx=1379 |
| T06 대웅제약 | Evolus Jeuveau approval, Daewoong-manufactured partner product | https://www.globenewswire.com/news-release/2019/02/01/1709411/0/en/evolus-receives-fda-approval-for-jeuveau-prabotulinumtoxina-xvfs-for-injection.html |
| T07 한미약품 | Spectrum ROLVEDON FDA approval, Hanmi collaboration economics | https://www.sec.gov/Archives/edgar/data/831547/000119312522242330/d401699dex991.htm |

## 10. Price Data Source Map

| symbol | shard |
|---:|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/{2024,2025}.csv |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/{2024,2025}.csv |
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/{2024,2025}.csv |
| 068270 | atlas/ohlcv_tradable_by_symbol_year/068/068270/{2024,2025}.csv |
| 006280 | atlas/ohlcv_tradable_by_symbol_year/006/006280/{2023,2024}.csv |
| 069620 | atlas/ohlcv_tradable_by_symbol_year/069/069620/{2019,2020}.csv |
| 128940 | atlas/ohlcv_tradable_by_symbol_year/128/128940/{2022,2023}.csv |

## 11. Case-by-Case Trigger Grid

The central split is this: a C23 regulatory headline is only the first tollgate. Stage2-Actionable can recognize a direct FDA approval, but Green should require at least one additional economic bridge: commercial availability, first shipment, reimbursement, launch cadence, sales uptake, royalty/milestone recognition, or a named partner economic path. Conversely, a CRL or major inspection/manufacturing issue should route to 4C only while the defect remains unresolved; if the sponsor later resubmits or clears the issue, C23 needs a re-entry rule.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | o | h | l | c | v | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 000100 | 2024-08-21 | 103000 | 109700 | 93800 | 94300 | 13922671 | 69.99 | 76.99 | 76.99 | -2.97 | -2.97 | -2.97 | 2024-10-15 | 166900 | -39.84 |
| 028300 | 2024-05-17 | 67100 | 67100 | 67100 | 67100 | 617840 | 9.99 | 46.2 | 46.2 | -32.71 | -32.71 | -32.71 | 2024-07-08 | 98100 | -40.06 |
| 145020 | 2024-03-04 | 199800 | 219000 | 193400 | 202500 | 277773 | 8.15 | 29.63 | 60.99 | -14.91 | -14.91 | -14.91 | 2024-11-07 | 326000 | -22.85 |
| 068270 | 2024-03-18 | 180900 | 184400 | 180300 | 182500 | 534945 | 6.36 | 12.33 | 15.62 | -7.01 | -7.01 | -12.16 | 2024-07-30 | 211000 | -24.03 |
| 006280 | 2023-12-18 | 128200 | 131100 | 119600 | 120500 | 212283 | 8.8 | 8.8 | 47.3 | -10.71 | -10.71 | -10.71 | 2024-08-28 | 177500 | -20.28 |
| 069620 | 2019-02-07 | 210000 | 217000 | 196000 | 204000 | 401670 | 6.37 | 6.37 | 6.37 | -12.99 | -29.17 | -32.35 | 2019-02-07 | 217000 | -36.41 |
| 128940 | 2022-09-13 | 326500 | 326500 | 303000 | 305000 | 162456 | 7.05 | 7.05 | 11.31 | -26.72 | -26.72 | -26.72 | 2023-04-14 | 339500 | -14.43 |


## 13. Current Calibrated Profile Stress Test

| trigger | likely current judgment | actual path | residual verdict |
|---|---|---|---|
| T01 유한양행 Lazcluze | Stage2/Yellow if approval recognized | MFE180 +76.99 / MAE180 -2.97 | profile should not wait for domestic sales once global partner FDA approval exists |
| T02 HLB CRL | 4C | MAE30 -32.71 but MFE180 +46.20 after resubmission optionality | 4C correct initially, but re-entry after defect cure is required |
| T03 휴젤 Letybo | Yellow | MFE180 +60.99 / MAE180 -14.91 | correct, but Green needs launch/sales bridge because early MAE was real |
| T04 셀트리온 ZYMFENTRA | Stage2-Actionable | MFE180 +15.62 / MAE180 -12.16 | commercial availability is actionable, but uptake proof required for Green |
| T05 녹십자 ALYGLO | Stage2-Actionable | MFE180 +47.30 / MAE180 -10.71 | delayed winner; drawdown-aware confirmation needed |
| T06 대웅제약 Jeuveau | Stage2 if approval-only overcredited | MFE180 +6.37 / MAE180 -32.35 | partner approval/manufacturer bridge insufficient; 4B cap needed |
| T07 한미약품 ROLVEDON | Stage2 if partner approval-only overcredited | MFE180 +11.31 / MAE180 -26.72 | launch-ready language did not protect price; royalty/sales bridge required |

## 14. Component Score Simulation

```text
component_order: event/regulatory_status, economic_bridge, clinical_quality, market_mispricing, 4b_risk, accounting_confidence, commercial_execution
current_C23_shadow_weights: 12 / 24 / 5 / 12 / 10 / 7 / 30
suggested_shadow_weights:     11 / 26 / 5 / 10 / 11 / 7 / 30
delta:                         -1 / +2 / 0 / -2 / +1 / 0 / 0
production_scoring_changed: false
shadow_weight_only: true
```

The proposed shift does not create a new global axis. It strengthens the C23-specific bridge from approval to commercial economics and adds a little more penalty for approval-only / partner-proxy high-MAE cases.

## 15. Stage2 / Yellow / Green / 4B / 4C Rule Candidate

```text
canonical_archetype_rule_candidate: C23_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE_GATE

Stage2-Actionable:
  direct approval, approval-letter, commercial availability, or first shipment evidence is present.

Stage3-Yellow:
  Stage2 evidence plus at least one economic bridge: partner economics, reimbursement, first shipment, launch readiness, distributor coverage, or explicit milestone/royalty relevance.

Stage3-Green:
  approval/availability plus two economic bridges: actual sales uptake, reimbursement/coverage, named partner commercial traction, royalty/milestone recognition, or guidance/revision bridge.

Stage4B:
  approval is real but listed-company economics are weak, partner/manufacturer-only bridge is thin, launch timing is delayed, or 30D/90D MAE exceeds tolerable drawdown without sales uptake proof.

Stage4C:
  CRL, clinical failure, unresolved GMP/BIMO/manufacturing deficiency, approval rejection, or commercialization thesis break. Re-entry allowed only after defect cure/resubmission/approval update.
```

## 16. Residual Contribution Summary

```text
loop_contribution_label: C23_FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_QUALITY_REPAIR
new_axis_proposed: C23_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
```

C23 winners are not simply the companies that receive regulatory approval. The winners are the companies whose approval becomes a working distribution pipe: product label, launch, patient access, partner economics, and eventual revenue/royalty. Approval without that pipe is a beautiful key with no door attached.

## 17. Coverage Matrix Update

```text
selected_canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
selected_large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
selected_round: R7
new_independent_case_count: 7
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 7
positive_case_count: 4
counterexample_count: 3
4B_case_count: 2
4C_case_count: 1
source_proxy_only_count: 2
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
```

## 18. Machine-Readable JSONL Rows

```jsonl
{"row_type":"price_source_validation","price_source":"Songdaiki/stock-web","basis":"tradable_raw/raw_unadjusted_marcap","manifest_max_date":"2026-02-20","mfe_mae_definition":"entry close vs forward N tradable rows max high/min low","corporate_action_window_check":"clean_by_local_profile_check_no_D_to_D+180_overlap"}
{"row_type":"trigger","case_id":"C23_R7L138_001_YUHAN_20240820_LAZERTINIB_FDA_APPROVAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","selected_round":"R7","selected_loop":138,"symbol":"000100","company":"유한양행","trigger_date":"2024-08-20","entry_date":"2024-08-21","trigger_type":"Stage3-Yellow","evidence_family":"FDA_APPROVAL_PLUS_GLOBAL_PARTNER_COMMERCIALIZATION_ROYALTY_BRIDGE","source_quality":"direct_regulatory_and_partner","source_url":"https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer","row_status":"calibration_usable","pos_counter":"positive","case_role":"structural_success","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"actual_ohlc_row":{"d":"2024-08-21","o":103000.0,"h":109700.0,"l":93800.0,"c":94300.0,"v":13922671,"m":"KOSPI"},"MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"peak_180D_date":"2024-10-15","trough_180D_date":"2024-08-22","drawdown_after_peak_180D_pct":-39.84,"current_profile_verdict":"current_profile_too_slow_without_approval_bridge","evidence_summary":"FDA approval of lazertinib/Lazcluze with amivantamab/Rybrevant for first-line EGFR-mutated NSCLC; Korean listed economics depend on partner commercialization and royalty/milestone realization."}
{"row_type":"trigger","case_id":"C23_R7L138_002_HLB_20240517_RIVOCERANIB_CRL_BIMO_GMP","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","selected_round":"R7","selected_loop":138,"symbol":"028300","company":"HLB","trigger_date":"2024-05-17","entry_date":"2024-05-17","trigger_type":"Stage4C","evidence_family":"FDA_COMPLETE_RESPONSE_LETTER_GMP_BIMO_NOT_CLINICAL_DATA","source_quality":"direct_subsidiary_regulatory","source_url":"https://elevartx.com/2024/09/23/elevar-therapeutics-resubmits-new-drug-application/","row_status":"calibration_usable","pos_counter":"counterexample","case_role":"regulatory_break_counterexample","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"actual_ohlc_row":{"d":"2024-05-17","o":67100.0,"h":67100.0,"l":67100.0,"c":67100.0,"v":617840,"m":"KOSDAQ"},"MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"peak_180D_date":"2024-07-08","trough_180D_date":"2024-05-21","drawdown_after_peak_180D_pct":-40.06,"current_profile_verdict":"current_profile_4c_needed_but_reentry_rule_required","evidence_summary":"FDA CRL for rivoceranib/camrelizumab NDA cited GMP deficiencies at camrelizumab manufacturing site and incomplete BIMO inspections, while not indicating clinical-data issues; immediate drawdown was severe but later resubmission optionality produced rebound."}
{"row_type":"trigger","case_id":"C23_R7L138_003_HUGEL_20240304_LETYBO_FDA_APPROVAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","selected_round":"R7","selected_loop":138,"symbol":"145020","company":"휴젤","trigger_date":"2024-03-04","entry_date":"2024-03-04","trigger_type":"Stage3-Yellow","evidence_family":"FDA_APPROVAL_AESTHETIC_TOXIN_US_LAUNCH_PENDING","source_quality":"direct_company_regulatory","source_url":"https://hugel-aesthetics.com/news-press-releases/","row_status":"calibration_usable","pos_counter":"positive","case_role":"approval_to_commercialization_success","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"actual_ohlc_row":{"d":"2024-03-04","o":199800.0,"h":219000.0,"l":193400.0,"c":202500.0,"v":277773,"m":"KOSDAQ GLOBAL"},"MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"peak_180D_date":"2024-11-07","trough_180D_date":"2024-03-21","drawdown_after_peak_180D_pct":-22.85,"current_profile_verdict":"current_profile_correct_but_green_requires_launch_bridge","evidence_summary":"Hugel America announced FDA approval of Letybo for moderate-to-severe glabellar lines; the direct approval was real but the E2R bridge still needed US shipment/launch and distributor economics confirmation."}
{"row_type":"trigger","case_id":"C23_R7L138_004_CELLTRION_20240318_ZYMFENTRA_US_AVAILABILITY","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","selected_round":"R7","selected_loop":138,"symbol":"068270","company":"셀트리온","trigger_date":"2024-03-18","entry_date":"2024-03-18","trigger_type":"Stage2-Actionable","evidence_family":"FDA_APPROVED_PRODUCT_US_COMMERCIAL_AVAILABILITY","source_quality":"direct_company_commercialization","source_url":"https://www.celltrion.com/en-us/company/media-center/press-release/3128","row_status":"calibration_usable","pos_counter":"positive","case_role":"commercialization_positive_but_modest_mfe","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"actual_ohlc_row":{"d":"2024-03-18","o":180900.0,"h":184400.0,"l":180300.0,"c":182500.0,"v":534945,"m":"KOSPI"},"MFE_30D_pct":6.36,"MFE_90D_pct":12.33,"MFE_180D_pct":15.62,"MAE_30D_pct":-7.01,"MAE_90D_pct":-7.01,"MAE_180D_pct":-12.16,"peak_180D_date":"2024-07-30","trough_180D_date":"2024-11-15","drawdown_after_peak_180D_pct":-24.03,"current_profile_verdict":"current_profile_green_too_early_without_sales_uptake","evidence_summary":"Celltrion USA announced ZYMFENTRA commercial availability across the U.S.; this is stronger than approval-only evidence but price path showed modest MFE and later MAE, so Green should wait for uptake/sales confirmation."}
{"row_type":"trigger","case_id":"C23_R7L138_005_GCBIO_20231218_ALYGLO_FDA_APPROVAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","selected_round":"R7","selected_loop":138,"symbol":"006280","company":"녹십자","trigger_date":"2023-12-18","entry_date":"2023-12-18","trigger_type":"Stage2-Actionable","evidence_family":"FDA_APPROVAL_IVIG_US_MARKET_ENTRY_BRIDGE","source_quality":"direct_company_regulatory","source_url":"https://www.gcbiopharma.com/eng/news_view.do?currentPage=1&idx=1379","row_status":"calibration_usable","pos_counter":"positive","case_role":"delayed_commercialization_positive","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"actual_ohlc_row":{"d":"2023-12-18","o":128200.0,"h":131100.0,"l":119600.0,"c":120500.0,"v":212283,"m":"KOSPI"},"MFE_30D_pct":8.8,"MFE_90D_pct":8.8,"MFE_180D_pct":47.3,"MAE_30D_pct":-10.71,"MAE_90D_pct":-10.71,"MAE_180D_pct":-10.71,"peak_180D_date":"2024-08-28","trough_180D_date":"2024-01-31","drawdown_after_peak_180D_pct":-20.28,"current_profile_verdict":"current_profile_needs_drawdown_aware_confirmation","evidence_summary":"GC Biopharma announced FDA approval for ALYGLO in adult primary humoral immunodeficiency; early MAE appeared before delayed right-tail as launch/commercialization became clearer."}
{"row_type":"trigger","case_id":"C23_R7L138_006_DAEWOONG_20190207_JEUVEAU_FDA_APPROVAL_PARTNER","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","selected_round":"R7","selected_loop":138,"symbol":"069620","company":"대웅제약","trigger_date":"2019-02-01","entry_date":"2019-02-07","trigger_type":"Stage4B","evidence_family":"PARTNER_FDA_APPROVAL_MANUFACTURER_ECONOMICS_UNCLEAR","source_quality":"partner_proxy_but_manufacturer_named","source_url":"https://www.globenewswire.com/news-release/2019/02/01/1709411/0/en/evolus-receives-fda-approval-for-jeuveau-prabotulinumtoxina-xvfs-for-injection.html","row_status":"calibration_usable","pos_counter":"counterexample","case_role":"approval_event_overcredit_counterexample","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"actual_ohlc_row":{"d":"2019-02-07","o":210000.0,"h":217000.0,"l":196000.0,"c":204000.0,"v":401670,"m":"KOSPI"},"MFE_30D_pct":6.37,"MFE_90D_pct":6.37,"MFE_180D_pct":6.37,"MAE_30D_pct":-12.99,"MAE_90D_pct":-29.17,"MAE_180D_pct":-32.35,"peak_180D_date":"2019-02-07","trough_180D_date":"2019-08-06","drawdown_after_peak_180D_pct":-36.41,"current_profile_verdict":"current_profile_false_positive_if_approval_only","evidence_summary":"Evolus announced FDA approval of Jeuveau, manufactured by Daewoong, with spring launch planned; for Daewoong listed economics the bridge from partner approval to revenue/margin was insufficient at entry."}
{"row_type":"trigger","case_id":"C23_R7L138_007_HANMI_20220913_ROLVEDON_FDA_APPROVAL_PARTNER","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","selected_round":"R7","selected_loop":138,"symbol":"128940","company":"한미약품","trigger_date":"2022-09-09","entry_date":"2022-09-13","trigger_type":"Stage4B","evidence_family":"PARTNER_FDA_APPROVAL_LAUNCH_READY_BUT_ROYALTY_PROOF_WEAK","source_quality":"partner_proxy_with_collaboration_disclosure","source_url":"https://www.sec.gov/Archives/edgar/data/831547/000119312522242330/d401699dex991.htm","row_status":"calibration_usable","pos_counter":"counterexample","case_role":"approval_event_overcredit_counterexample","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"actual_ohlc_row":{"d":"2022-09-13","o":326500.0,"h":326500.0,"l":303000.0,"c":305000.0,"v":162456,"m":"KOSPI"},"MFE_30D_pct":7.05,"MFE_90D_pct":7.05,"MFE_180D_pct":11.31,"MAE_30D_pct":-26.72,"MAE_90D_pct":-26.72,"MAE_180D_pct":-26.72,"peak_180D_date":"2023-04-14","trough_180D_date":"2022-09-26","drawdown_after_peak_180D_pct":-14.43,"current_profile_verdict":"current_profile_false_positive_without_royalty_sales_bridge","evidence_summary":"Spectrum announced FDA approval of ROLVEDON, developed with Hanmi LAPSCOVERY technology, and commercial launch readiness; listed-stock price path showed approval-only evidence did not protect from deep MAE."}
{"row_type":"score_simulation","profile":"current_e2r_2_2_proxy","axis":"C23 approval/commercialization","stage2_required_bridge":"approval or availability evidence plus economic bridge","green_guard":"approval-only cannot open Green without launch/sales/royalty uptake","4b_guard":"partner/manufacturer approval without listed economic bridge or high-MAE after approval","4c_guard":"CRL/inspection/manufacturing deficiency or clinical failure; allow re-entry after resubmission/clearance evidence"}
{"row_type":"shadow_weight_delta","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","component_order":"event/regulatory_status,economic_bridge,clinical_quality,market_mispricing,4b_risk,accounting_confidence,commercial_execution","before":[12,24,5,12,10,7,30],"after":[11,26,5,10,11,7,30],"delta":[-1,2,0,-2,1,0,0],"production_scoring_changed":false,"shadow_weight_only":true}
```

## 19. Batch Ingest Self-Audit

```text
filename_pattern_valid: true
metadata_round_loop_match_filename: true
round_sector_consistency: pass
canonical_archetype_id_valid: true
fine_archetype_maps_to_canonical: true
all_trigger_rows_use_canonical_stage_label: true
all_trigger_rows_have_MFE_30D_pct: true
all_trigger_rows_have_MFE_90D_pct: true
all_trigger_rows_have_MFE_180D_pct: true
all_trigger_rows_have_MAE_30D_pct: true
all_trigger_rows_have_MAE_90D_pct: true
all_trigger_rows_have_MAE_180D_pct: true
actual_stock_web_ohlc_row_included: true
same_entry_group_deduped: true
corporate_action_contamination_D_to_Dplus180: false
price_source_is_stock_web: true
production_scoring_changed: false
shadow_weight_only: true
```

## 20. Deferred Coding Agent Handoff Prompt

```text
Read this MD as one v12 residual calibration input.
Do not patch production scoring directly.
Parse JSONL trigger rows and validate required 30/90/180D MFE/MAE fields.
Add C23_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE_GATE to the candidate archetype-specific shadow ledger only.
Recommended validation:
  1. Confirm C23 direct FDA approval cases are not capped too harshly when global partner economics are explicit.
  2. Confirm partner/manufacturer approval-only events require commercial economics before Green.
  3. Add CRL re-entry rule after resubmission/defect-cure evidence.
  4. Test high-MAE approval cases for drawdown-aware Green delay rather than hard exclusion.
```

## 21. Completed Research State

```text
completed: true
selected_round: R7
selected_loop: 138
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selected_priority_bucket: Priority 0/1 quality repair
next_recommended_archetypes:
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C27_CONTENT_IP_GLOBAL_MONETIZATION
```
