# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
filename = e2r_stock_web_v12_residual_round_R7_loop_128_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
selected_round = R7
selected_loop = 128
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / under_50_rows_static_ledger / C23 rows 48 need_to_50 2 before this local loop
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT
loop_objective = coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds **5** new independent cases, **2** counterexamples, and **2** residual errors for **L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION**.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. The loop does not patch production scoring. It tests whether C23 needs a narrower gate than the global approval/disclosure bridge: regulatory approval must be tied to launch, reimbursement, partner quality, royalty route, or sales conversion. Conversely, a CRL must be severity-split before routing to hard 4C.

## 2. Round / Large Sector / Canonical Archetype Scope

C23 maps to R7 / L7. R13 is not used because this is a sector-specific bio/healthcare canonical study rather than cross-archetype red-team.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index had C23 at 48 representative rows, `need_to_50=2`. This MD uses five symbols and five trigger families not used in the current session's C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05 runs.

Strict duplicate key avoided:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

The 180D windows were computed from downloaded tradable shard CSVs. Corporate action contamination was checked by share-count jumps inside each 180D window; all representative trigger rows below are marked `clean_180D_window`.

## 5. Historical Eligibility Gate

| symbol | company | trigger | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | profile_verdict | role |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 000100 | Yuhan Corporation | Stage3-Green | 2024-08-20 | 2024-08-21 | 94300 | 69.99 | 76.99 | 76.99 | -2.97 | -2.97 | -2.97 | current_profile_correct | P |
| 145020 | Hugel | Stage3-Yellow | 2024-03-04 | 2024-03-05 | 205500 | 2.68 | 27.74 | 58.64 | -16.16 | -16.16 | -16.16 | current_profile_correct | P |
| 068270 | Celltrion | Stage2-Actionable | 2024-03-18 | 2024-03-19 | 184400 | 5.26 | 14.43 | 14.43 | -7.97 | -7.97 | -13.07 | current_profile_correct | P |
| 069620 | Daewoong Pharmaceutical | Stage3-Yellow | 2019-02-07 | 2019-02-08 | 206000 | 2.91 | 2.91 | 2.91 | -13.83 | -29.85 | -33.01 | current_profile_false_positive | C |
| 028300 | HLB | Stage4C | 2024-05-17 | 2024-05-20 | 47000 | 57.02 | 108.72 | 108.72 | -3.94 | -3.94 | -3.94 | current_profile_4C_too_early | C |


All five representative rows have entry date, entry price, 30/90/180D MFE/MAE, at least 180 forward trading days, and a clean 180D corporate-action status.

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT
compresses_to = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

Compression rule:

```text
approval headline -> Stage2/Yellow only unless commercialization bridge exists
approval + partner/royalty/market-access/launch -> Yellow/Green candidate
CRL due to clinical thesis break or rejection of efficacy/safety -> hard 4C
CRL due to fixable GMP/BIMO/inspection with no clinical-data issue -> Stage4B/watch, not automatic hard 4C
```

## 7. Case Selection Summary

1. `000100` Yuhan: Lazcluze approval with explicit Yuhan/Janssen route produced strong MFE and small MAE.
2. `145020` Hugel: Letybo FDA approval had a slower early path but converted by 180D.
3. `068270` Celltrion: Zymfentra commercial availability was an actual approval-to-launch bridge, but the path argues against automatic Green.
4. `069620` Daewoong: Nabota approval headline failed to convert into durable 180D price path.
5. `028300` HLB: May 2024 CRL was a regulatory shock, but later disclosure indicates fixable GMP/BIMO issues rather than clinical-data break; hard 4C was too blunt.

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
stage4b_or_4c_case_count = 1
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
```

The positive cases show that C23 can work when approval unlocks a visible commercial route. The counterexamples show that approval alone can be a trap and that CRL severity must be split.

## 9. Evidence Source Map

| case_id | evidence source | date anchor | role |
|---|---|---:|---|
| C23_000100_LAZCLUZE_FDA_202408 | FDA approval notice; Yuhan USA news | 2024-08-19 / 2024-08-20 | approval + Yuhan license/commercial route |
| C23_145020_LETYBO_FDA_202403 | Hugel / PRNewswire release | 2024-03-04 | FDA approval + planned U.S. launch |
| C23_068270_ZYMFENTRA_COMM_202403 | Celltrion press release | 2024-03-18 | U.S. commercial availability after FDA approval |
| C23_069620_NABOTA_FDA_201902 | Yonhap | 2019-02-07 | FDA approval + partner sales route, but weak conversion |
| C23_028300_RIVOCERANIB_CRL_202405 | Elevar Therapeutics | 2024-09-23 retrospective CRL explanation | May CRL severity split; no clinical-data issue indicated |

## 10. Price Data Source Map

| symbol | entry shard | profile path | 180D corporate-action status |
|---|---|---|---|
| 000100 | `atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv` | `atlas/symbol_profiles/000/000100.json` | clean_180D_window |
| 145020 | `atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv` | `atlas/symbol_profiles/145/145020.json` | clean_180D_window |
| 068270 | `atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv` | `atlas/symbol_profiles/068/068270.json` | clean_180D_window |
| 069620 | `atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv` | `atlas/symbol_profiles/069/069620.json` | clean_180D_window |
| 028300 | `atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv` | `atlas/symbol_profiles/028/028300.json` | clean_180D_window |


## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | case_type | positive_or_counterexample | stage2_fields | stage3_fields | stage4b_fields | stage4c_fields |
|---|---|---|---|---|---|---|---|---|
| C23_000100_LAZCLUZE_FDA_202408 | 000100 | Stage3-Green | structural_success | positive | public_event_or_disclosure,customer_or_order_quality,policy_or_regulatory_optionality | multiple_public_sources,durable_customer_confirmation,commercialization_or_royalty_route,low_red_team_risk |  |  |
| C23_145020_LETYBO_FDA_202403 | 145020 | Stage3-Yellow | structural_success | positive | public_event_or_disclosure,policy_or_regulatory_optionality,customer_or_order_quality | multiple_public_sources,commercial_launch_visibility,financial_visibility_partial | commercial_ramp_delay_risk |  |
| C23_068270_ZYMFENTRA_COMM_202403 | 068270 | Stage2-Actionable | stage2_promote_candidate | positive | public_event_or_disclosure,commercial_availability,policy_or_regulatory_optionality | financial_visibility_partial,repeat_order_or_conversion_unknown | reimbursement_ramp_risk |  |
| C23_069620_NABOTA_FDA_201902 | 069620 | Stage3-Yellow | false_positive_green | counterexample | public_event_or_disclosure,policy_or_regulatory_optionality,partner_distribution_route | multiple_public_sources | market_competition,commercialization_overhang,litigation_or_partner_risk |  |
| C23_028300_RIVOCERANIB_CRL_202405 | 028300 | Stage4C | 4C_too_early | counterexample |  |  | regulatory_delay,inspection_or_cmc_issue,resubmission_path_possible | complete_response_letter |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C23_000100_LAZCLUZE_FDA_202408_T1 | 2024-08-21 | 94300 | 69.99 | 76.99 | 76.99 | -2.97 | -2.97 | -2.97 | 2024-10-15 | 166900 | -39.84 |
| C23_145020_LETYBO_FDA_202403_T1 | 2024-03-05 | 205500 | 2.68 | 27.74 | 58.64 | -16.16 | -16.16 | -16.16 | 2024-11-07 | 326000 | -22.85 |
| C23_068270_ZYMFENTRA_COMM_202403_T1 | 2024-03-19 | 184400 | 5.26 | 14.43 | 14.43 | -7.97 | -7.97 | -13.07 | 2024-07-30 | 211000 | -24.03 |
| C23_069620_NABOTA_FDA_201902_T1 | 2019-02-08 | 206000 | 2.91 | 2.91 | 2.91 | -13.83 | -29.85 | -33.01 | 2019-02-08 | 212000 | -34.91 |
| C23_028300_RIVOCERANIB_CRL_202405_T1 | 2024-05-20 | 47000 | 57.02 | 108.72 | 108.72 | -3.94 | -3.94 | -3.94 | 2024-07-08 | 98100 | -40.06 |


## 13. Current Calibrated Profile Stress Test

| symbol | expected current profile behavior | actual path | verdict |
|---|---|---|---|
| 000100 | Green allowed when FDA approval has named partner/commercial route | +76.99% 180D MFE / -2.97% MAE | current_profile_correct |
| 145020 | Yellow before Green because commercial launch timing still needed | +58.64% 180D MFE / -16.16% MAE | current_profile_correct |
| 068270 | Actionable/Yellow but not Green because ramp/reimbursement still uncertain | +14.43% 180D MFE / -13.07% MAE | current_profile_correct |
| 069620 | Approval headline should not be Green without durable sales bridge | +2.91% 180D MFE / -33.01% MAE | current_profile_false_positive |
| 028300 | CRL should be severity-split before hard 4C | +108.72% 180D MFE / -3.94% MAE | current_profile_4C_too_early |

## 14. Stage2 / Yellow / Green Comparison

C23 Green works only where approval is coupled to a credible commercialization route. Yuhan had partner route and strong price alignment. Hugel had approval and launch plan but early drawdown, so Yellow was safer than immediate Green. Celltrion had commercial availability but moderate MFE; it is a Stage2-Actionable/Yellow bridge case, not a Green proof. Daewoong shows approval headline can be a false-positive Green when commercial conversion is thin.

## 15. 4B Local vs Full-window Timing Audit

No price-only 4B row is used as a positive promotion trigger. HLB is treated as a 4C severity-split audit: the CRL was bad regulatory news, but the later path and non-clinical nature argue that this should have been a Stage4B/watch until clinical thesis break was confirmed.

## 16. 4C Protection Audit

```text
HLB / 028300:
trigger_type = Stage4C
four_c_protection_label = false_break_fixable_crl
observed_180D_MFE = +108.72%
observed_180D_MAE = -3.94%
verdict = hard_4c_too_early_when_crl_is_fixable_cmc_bimo_without_clinical_data_break
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L7_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_GATE
```

For L7, regulatory approval is not enough by itself. Promotion strength should rise only when approval is tied to launch date, market-access/reimbursement, named commercial partner, royalty economics, or confirmed early sales conversion.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C23_APPROVAL_NEEDS_COMMERCIALIZATION_ROUTE_AND_CRL_SEVERITY_SPLIT
```

C23 should split:

```text
approval_with_partner_or_launch_route -> Stage2-Actionable / Stage3-Yellow / Stage3-Green depending on margin and revenue bridge
approval_without_commercialization_bridge -> Stage2-watch or Yellow ceiling
fixable_CMC_BIMO_CRL -> Stage4B/watch unless clinical thesis breaks
clinical_efficacy_or_safety_rejection -> hard Stage4C
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | selected triggers | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1 proxy | current generic approval bridge | 5 | 46.16 | -12.18 | 52.34 | -13.83 | mixed; false positive and premature 4C remain |
| P1 sector L7 | approval requires commercial bridge | 5 | 39.72 | -9.03 | 50.02 | -10.73 | improves promotion precision |
| P2 canonical C23 | CRL severity split | 5 | n/a | n/a | n/a | n/a | avoids misrouting fixable CRL to hard 4C |
| P3 guard | cap approval headline without launch route | 2 counterexamples | 55.81 | -16.89 | 55.81 | -18.47 | catches opposite failure modes |

## 20. Score-Return Alignment Matrix

Score proxy rows are emitted in JSONL. The main alignment result is that approval events with commercialization route aligned with MFE, while approval-only or blunt CRL routing produced residual error.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT | 3 | 2 | 1 | 1 | 5 | 0 | 5 | 5 | 2 | L7_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_GATE | C23_APPROVAL_NEEDS_COMMERCIALIZATION_ROUTE_AND_CRL_SEVERITY_SPLIT | C23 static rows 48 + 5 local usable rows = 53; need_to_50 becomes 0 after commit |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_required_bridge | hard_4c_thesis_break_routes_to_4c | price_only_blowoff_blocks_positive_stage
residual_error_types_found: approval_headline_false_positive | fixable_crl_misrouted_to_hard_4c
new_axis_proposed: C23_APPROVAL_NEEDS_COMMERCIALIZATION_ROUTE_AND_CRL_SEVERITY_SPLIT
existing_axis_strengthened: stage2_required_bridge
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c only for fixable CMC/BIMO CRL without clinical thesis break
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L7_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_GATE
canonical_archetype_rule_candidate: C23_APPROVAL_NEEDS_COMMERCIALIZATION_ROUTE_AND_CRL_SEVERITY_SPLIT
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web tradable shard entry rows, 30/90/180D MFE/MAE, clean 180D share-count continuity, evidence date anchors, canonical trigger labels.

Not validated: production scoring code, live candidate scan, current investment suitability, exact royalty economics, revised 2026 price data beyond stock-web manifest max date.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_APPROVAL_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Approval credit requires market-access/partner/royalty or launch bridge; fixable CMC/BIMO CRL is 4B watch unless clinical thesis breaks.","Improves false positive control on 069620 and reduces premature hard 4C on 028300 while preserving 000100/145020 upside.","C23_000100_LAZCLUZE_FDA_202408_T1|C23_145020_LETYBO_FDA_202403_T1|C23_068270_ZYMFENTRA_COMM_202403_T1|C23_069620_NABOTA_FDA_201902_T1|C23_028300_RIVOCERANIB_CRL_202405_T1",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C23_000100_LAZCLUZE_FDA_202408","symbol":"000100","company_name":"Yuhan Corporation","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"FDA approval + Yuhan/Janssen license route","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"approval with named global commercial partner and royalty-style monetization route"}
{"row_type":"case","case_id":"C23_145020_LETYBO_FDA_202403","symbol":"145020","company_name":"Hugel","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"FDA approval + planned U.S. launch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"approval positive but early high MAE argues for Yellow before Green"}
{"row_type":"case","case_id":"C23_068270_ZYMFENTRA_COMM_202403","symbol":"068270","company_name":"Celltrion","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"U.S. commercial availability after FDA approval","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"commercialization bridge existed but MFE/MAE argues against automatic Green"}
{"row_type":"case","case_id":"C23_069620_NABOTA_FDA_201902","symbol":"069620","company_name":"Daewoong Pharmaceutical","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"FDA approval headline but weak durable commercialization bridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"approval headline did not translate into durable 180D price path"}
{"row_type":"case","case_id":"C23_028300_RIVOCERANIB_CRL_202405","symbol":"028300","company_name":"HLB","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","case_type":"4C_too_early","positive_or_counterexample":"counterexample","best_trigger":"FDA CRL severity split: CMC/BIMO not clinical-data break","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"CRL was not a clean clinical thesis break; hard 4C routing was too blunt"}
{"row_type":"trigger","trigger_id":"C23_000100_LAZCLUZE_FDA_202408_T1","case_id":"C23_000100_LAZCLUZE_FDA_202408","symbol":"000100","company_name":"Yuhan Corporation","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage3-Green","trigger_date":"2024-08-20","entry_date":"2024-08-21","entry_price":94300.0,"evidence_available_at_that_date":"FDA approved lazertinib with amivantamab on 2024-08-19; Yuhan USA noted Lazcluze was developed by Yuhan and licensed to Janssen.","evidence_source":"FDA approval notice; Yuhan USA approval note","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","commercialization_or_royalty_route","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":76.99,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":-2.97,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-15","peak_price":166900.0,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"lazcluze_fda_approval_royalty_commercial_route_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":328,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_000100_20240821","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C23_145020_LETYBO_FDA_202403_T1","case_id":"C23_145020_LETYBO_FDA_202403","symbol":"145020","company_name":"Hugel","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-04","entry_date":"2024-03-05","entry_price":205500.0,"evidence_available_at_that_date":"Hugel announced FDA approval for Letybo and planned U.S. launch in the back half of 2024.","evidence_source":"Hugel/PRNewswire Letybo FDA approval release","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources","commercial_launch_visibility","financial_visibility_partial"],"stage4b_evidence_fields":["commercial_ramp_delay_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.68,"MFE_90D_pct":27.74,"MFE_180D_pct":58.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.16,"MAE_90D_pct":-16.16,"MAE_180D_pct":-16.16,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000.0,"drawdown_after_peak_pct":-22.85,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"commercial_ramp_delay_risk","four_c_protection_label":null,"trigger_outcome_label":"letybo_fda_approval_with_h2_launch_conversion_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":201,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_145020_20240305","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C23_068270_ZYMFENTRA_COMM_202403_T1","case_id":"C23_068270_ZYMFENTRA_COMM_202403","symbol":"068270","company_name":"Celltrion","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-18","entry_date":"2024-03-19","entry_price":184400.0,"evidence_available_at_that_date":"Celltrion announced Zymfentra was commercially available across the U.S. on 2024-03-15 after FDA approval in 2023.","evidence_source":"Celltrion Zymfentra U.S. availability press release","stage2_evidence_fields":["public_event_or_disclosure","commercial_availability","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility_partial","repeat_order_or_conversion_unknown"],"stage4b_evidence_fields":["reimbursement_ramp_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv","profile_path":"atlas/symbol_profiles/068/068270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.26,"MFE_90D_pct":14.43,"MFE_180D_pct":14.43,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.97,"MAE_90D_pct":-7.97,"MAE_180D_pct":-13.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":211000.0,"drawdown_after_peak_pct":-24.03,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"reimbursement_ramp_risk","four_c_protection_label":null,"trigger_outcome_label":"zymfentra_us_availability_approval_to_commercialization_mild_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":191,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_068270_20240319","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C23_069620_NABOTA_FDA_201902_T1","case_id":"C23_069620_NABOTA_FDA_201902","symbol":"069620","company_name":"Daewoong Pharmaceutical","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2019-02-07","entry_date":"2019-02-08","entry_price":206000.0,"evidence_available_at_that_date":"Yonhap reported FDA approval and U.S. partner Evolus commercialization route after market close on 2019-02-07.","evidence_source":"Yonhap Nabota FDA approval article","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","partner_distribution_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["market_competition","commercialization_overhang","litigation_or_partner_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv","profile_path":"atlas/symbol_profiles/069/069620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.91,"MFE_90D_pct":2.91,"MFE_180D_pct":2.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.83,"MAE_90D_pct":-29.85,"MAE_180D_pct":-33.01,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-02-08","peak_price":212000.0,"drawdown_after_peak_pct":-34.91,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"market_competition|commercialization_overhang|litigation_or_partner_risk","four_c_protection_label":null,"trigger_outcome_label":"nabota_fda_approval_without_durable_commercialization_bridge_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":221,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_069620_20190208","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C23_028300_RIVOCERANIB_CRL_202405_T1","case_id":"C23_028300_RIVOCERANIB_CRL_202405","symbol":"028300","company_name":"HLB","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_AND_CRL_SEVERITY_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-05-17","entry_date":"2024-05-20","entry_price":47000.0,"evidence_available_at_that_date":"The May 2024 CRL became public; later Elevar specified GMP/BIMO inspection issues and no clinical-data issue, explaining why hard 4C needed severity split.","evidence_source":"Elevar resubmission release explaining May 2024 CRL","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["regulatory_delay","inspection_or_cmc_issue","resubmission_path_possible"],"stage4c_evidence_fields":["complete_response_letter"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":57.02,"MFE_90D_pct":108.72,"MFE_180D_pct":108.72,"MFE_1Y_pct":108.72,"MFE_2Y_pct":null,"MAE_30D_pct":-3.94,"MAE_90D_pct":-3.94,"MAE_180D_pct":-3.94,"MAE_1Y_pct":-3.94,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-08","peak_price":98100.0,"drawdown_after_peak_pct":-40.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"do_not_treat_fixable_cmc_bimo_crl_as_full_4c_without_thesis_break","four_b_evidence_type":"regulatory_delay|inspection_or_cmc_issue|resubmission_path_possible","four_c_protection_label":"false_break_fixable_crl","trigger_outcome_label":"rivoceranib_camrelizumab_crl_fixable_cmc_bimo_false_break","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":393,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_028300_20240520","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_000100_LAZCLUZE_FDA_202408","trigger_id":"C23_000100_LAZCLUZE_FDA_202408_T1","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":0,"customer_quality_score":9,"policy_or_regulatory_score":10,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":0,"customer_quality_score":10,"policy_or_regulatory_score":10,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C23 shadow profile separates mere regulatory approval from commercialization bridge and separates fixable CMC/BIMO CRL from clinical thesis break.","MFE_90D_pct":76.99,"MAE_90D_pct":-2.97,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_145020_LETYBO_FDA_202403","trigger_id":"C23_145020_LETYBO_FDA_202403_T1","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":0,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":0,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C23 shadow profile separates mere regulatory approval from commercialization bridge and separates fixable CMC/BIMO CRL from clinical thesis break.","MFE_90D_pct":27.74,"MAE_90D_pct":-16.16,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_068270_ZYMFENTRA_COMM_202403","trigger_id":"C23_068270_ZYMFENTRA_COMM_202403_T1","symbol":"068270","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":0,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":0,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C23 shadow profile separates mere regulatory approval from commercialization bridge and separates fixable CMC/BIMO CRL from clinical thesis break.","MFE_90D_pct":14.43,"MAE_90D_pct":-7.97,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_069620_NABOTA_FDA_201902","trigger_id":"C23_069620_NABOTA_FDA_201902_T1","symbol":"069620","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":0,"customer_quality_score":6,"policy_or_regulatory_score":9,"valuation_repricing_score":0,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":0,"customer_quality_score":6,"policy_or_regulatory_score":9,"valuation_repricing_score":0,"execution_risk_score":8,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C23 shadow profile separates mere regulatory approval from commercialization bridge and separates fixable CMC/BIMO CRL from clinical thesis break.","MFE_90D_pct":2.91,"MAE_90D_pct":-29.85,"score_return_alignment_label":"counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_028300_RIVOCERANIB_CRL_202405","trigger_id":"C23_028300_RIVOCERANIB_CRL_202405_T1","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":0,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":0,"execution_risk_score":8,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":42,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":0,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":0,"execution_risk_score":6,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_components":["margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C23 shadow profile separates mere regulatory approval from commercialization bridge and separates fixable CMC/BIMO CRL from clinical thesis break.","MFE_90D_pct":108.72,"MAE_90D_pct":-3.94,"score_return_alignment_label":"counterexample","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"residual_contribution","round":"R7","loop":"128","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["approval_headline_false_positive","fixable_crl_misrouted_to_hard_4c"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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
completed_round = R7
completed_loop = 128
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / C23 rows 48 need_to_50 2 before this loop
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_quality_repair | C19_BRAND_RETAIL_INVENTORY_MARGIN_quality_repair | C31_POLICY_SUBSIDY_LEGISLATION_EVENT_URL_repair | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_if_guardrail_needed
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

Next execution should read the latest `V12_Research_No_Repeat_Index.md` again. If this file is committed, C23 should clear 50 rows, making C27 the remaining Priority 1 under-50 canonical from the static ledger.

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- FDA lazertinib approval: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer
- Yuhan USA Lazcluze/Rybrevant approval note: https://www.yuhan-usa.com/rybrevant-plus-lazcluze-by-johnson-johnson-got-approved-by-the-u-s-fda-as-a-first-line-chemotherapy-free-treatment-for-patients-with-egfr-mutated-advanced-lung-cancer-lazcl/
- Hugel Letybo FDA approval release: https://www.prnewswire.com/news-releases/hugel-receives-fda-approval-in-the-united-states-of-letybo-letibotulinumtoxina-wlbg-for-injection-for-the-treatment-of-glabellar-lines-302078434.html
- Celltrion Zymfentra U.S. availability: https://www.celltrion.com/en-us/company/media-center/press-release/3128
- Yonhap Nabota FDA approval: https://en.yna.co.kr/view/AEN20190207010000320
- Elevar CRL/resubmission explanation: https://elevartx.com/2024/09/23/elevar-therapeutics-resubmits-new-drug-application/

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
