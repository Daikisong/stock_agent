# E2R Stock-Web v12 Residual Research — R7 / L7_BIO_HEALTHCARE_MEDICAL / C24_BIO_TRIAL_DATA_EVENT_RISK

```text
selected_round: R7
selected_loop: 211
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 URL/proxy quality repair + R7 C24 endpoint/safety balance reinforcement
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection Rationale

The current No-Repeat Index shows that all C01~C32 canonical archetypes are above the 80-row floor, so this loop is not a raw row-fill. L7 already received fresh C23 approval/commercialization and C25 medical-device commercialization repairs in adjacent loops. C24 remains the missing R7 middle layer: endpoint, safety, ODAC, futility, and trial-data interpretation risk. C24 has 239 representative rows, 63 symbols, positives/counterexamples 36/41, and 4B/4C 28/28, so the useful residual work is no longer count expansion; it is direct-source quality and endpoint-vs-commercial-bridge taxonomy.

Loop objective: `trial_endpoint_event_risk`, `hard_4c_thesis_break_timing_test`, `stage2_actionable_bonus_stress_test`, `green_strictness_stress_test`, `source_proxy_replacement`.

## 2. Stock-Web Price Atlas Validation

```text
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_columns: d,o,h,l,c,v,a,mc,s,m
MFE/MAE formula: max high / min low from entry_date through N trading days vs entry close
```

All seven usable rows have actual entry OHLCV, complete 30D/90D/180D MFE·MAE, at least 180 forward tradable rows, and no 180D corporate-action contamination under the local Stock-Web shard check. The LigaChem LCB84 case is retained as a narrative-only taxonomy row because its 180D window includes a share-change corporate-action candidate and is therefore excluded from weight evidence.

## 3. Human-readable Trigger Table

| symbol | company | trigger | trigger_date | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak_date | post-peak DD | role | current_profile_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 000100 | Yuhan Corporation | Stage2-Actionable | 2023-10-23 | 2023-10-23 | 62000 | 3.55 / -11.45 | 15.48 / -11.45 | 61.94 / -11.45 | 2024-07-16 | -45.32 | positive_control | current_profile_correct_but_green_blocked |
| 039200 | Oscotec | Stage2-Actionable | 2023-10-23 | 2023-10-23 | 21850 | 2.06 / -17.62 | 13.27 / -17.62 | 105.49 / -17.62 | 2024-07-16 | -59.91 | positive_high_MAE_control | current_profile_too_late_if_actionable_blocked |
| 084990 | Helixmith | Stage4C | 2024-01-03 | 2024-01-03 | 4250 | 75.06 / -23.53 | 75.06 / -23.53 | 75.06 / -23.53 | 2024-02-06 | -56.32 | endpoint_failure_control | current_profile_correct_4c_but_not_sticky_green_blocker |
| 215600 | SillaJen | Stage4C | 2019-08-02 | 2019-08-05 | 21850 | 0.00 / -58.81 | 2.29 / -64.21 | 2.29 / -64.21 | 2019-10-24 | -65.01 | terminal_trial_failure_control | current_profile_correct |
| 028300 | HLB | Stage4B | 2024-05-17 | 2024-05-17 | 67100 | 9.99 / -32.71 | 46.20 / -32.71 | 46.20 / -32.71 | 2024-07-08 | -53.98 | regulatory_offset_case | current_profile_false_positive_if_hard_4c_sticky |
| 128940 | Hanmi Pharm | Stage4C | 2022-09-23 | 2022-09-23 | 237000 | 11.39 / -5.70 | 29.96 / -5.70 | 43.25 / -5.70 | 2023-04-14 | -34.17 | program_thesis_break_with_issuer_offset | current_profile_false_positive_if_issuer_level_4c |
| 298380 | ABL Bio | Stage2 | 2022-01-12 | 2022-01-12 | 26150 | 33.08 / -8.99 | 33.08 / -26.58 | 33.08 / -27.92 | 2022-01-21 | -45.83 | stage2_false_positive_guard | current_profile_false_positive_if_actionable |

## 4. Case Notes

### C24_211_YUHAN_MARIPOSA_PHASE3_POSITIVE — 000100 Yuhan Corporation
- Trigger: `Stage2-Actionable` on `2023-10-23`, entry `2023-10-23` close `62000`.
- Actual Stock-Web entry OHLCV: `2023-10-23 o=62500 h=63400 l=61300 c=62000 v=664563`.
- Evidence: Annals of Oncology MARIPOSA primary results / ESMO 2023; J&J/Yuhan lazertinib program context.
- Source: https://www.annalsofoncology.org/article/S0923-7534(23)04206-0/fulltext ; https://www.rybrevanthcp.com/clinical-data/mariposa/
- Result: 30D MFE/MAE `3.55% / -11.45%`; 90D `15.48% / -11.45%`; 180D `61.94% / -11.45%`, peak `2024-07-16` at `100400`, post-peak drawdown `-45.32%`.
- Residual: `positive_phase3_pfs_data_with_partnered_route_but_no_immediate_revenue_bridge`; proposed after-stage `Stage2-Actionable`; verdict `current_profile_correct_but_green_blocked`.

### C24_211_OSCOTEC_MARIPOSA_ROYALTY_OPTION — 039200 Oscotec
- Trigger: `Stage2-Actionable` on `2023-10-23`, entry `2023-10-23` close `21850`.
- Actual Stock-Web entry OHLCV: `2023-10-23 o=22100 h=22300 l=20700 c=21850 v=622220`.
- Evidence: MARIPOSA Phase 3 primary results; Oscotec lazertinib linkage.
- Source: https://www.annalsofoncology.org/article/S0923-7534(23)04206-0/fulltext ; https://oscotec.com/?document_srl=739&listStyle=viewer&mid=PressReleases
- Result: 30D MFE/MAE `2.06% / -17.62%`; 90D `13.27% / -17.62%`; 180D `105.49% / -17.62%`, peak `2024-07-16` at `44900`, post-peak drawdown `-59.91%`.
- Residual: `partnered_phase3_success_can_be_stage2_actionable_but_royalty_revenue_timing_blocks_green`; proposed after-stage `Stage2-Actionable`; verdict `current_profile_too_late_if_actionable_blocked`.

### C24_211_HELIXMITH_VM202_DPN_PRIMARY_ENDPOINT_FAIL — 084990 Helixmith
- Trigger: `Stage4C` on `2024-01-03`, entry `2024-01-03` close `4250`.
- Actual Stock-Web entry OHLCV: `2024-01-03 o=4250 h=4450 l=4250 c=4250 v=3868841`.
- Evidence: Engensis/VM202 U.S. Phase 3 DPN primary endpoint failure.
- Source: https://www.asiae.co.kr/en/print.htm?idxno=2024010307510936034 ; https://www.yna.co.kr/view/AKR20240104037200002
- Result: 30D MFE/MAE `75.06% / -23.53%`; 90D `75.06% / -23.53%`; 180D `75.06% / -23.53%`, peak `2024-02-06` at `7440`, post-peak drawdown `-56.32%`.
- Residual: `confirmed_primary_endpoint_failure_is_4c_but_later_bounce_warns_against_price_only_stickiness`; proposed after-stage `Stage4C`; verdict `current_profile_correct_4c_but_not_sticky_green_blocker`.

### C24_211_SILLAJEN_PHOCUS_FUTILITY_TERMINATION — 215600 SillaJen
- Trigger: `Stage4C` on `2019-08-02`, entry `2019-08-05` close `21850`.
- Actual Stock-Web entry OHLCV: `2019-08-05 o=21850 h=21850 l=21850 c=21850 v=235177`.
- Evidence: PHOCUS DMC futility analysis and early termination for Pexa-Vec.
- Source: https://www.prnewswire.com/news-releases/sillajen-announces-conclusions-from-interim-futility-analysis-of-phase-3-phocus-trial-in-hcc-300895539.html ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11095598/
- Result: 30D MFE/MAE `0.00% / -58.81%`; 90D `2.29% / -64.21%`; 180D `2.29% / -64.21%`, peak `2019-10-24` at `22350`, post-peak drawdown `-65.01%`.
- Residual: `terminal_phase3_futility_has_no_second_bridge_and_supports_hard_4c`; proposed after-stage `Stage4C`; verdict `current_profile_correct`.

### C24_211_HLB_CRL_CLINICAL_DATA_INTACT_REGULATORY_OFFSET — 028300 HLB
- Trigger: `Stage4B` on `2024-05-17`, entry `2024-05-17` close `67100`.
- Actual Stock-Web entry OHLCV: `2024-05-17 o=67100 h=67100 l=67100 c=67100 v=617840`.
- Evidence: FDA CRL for rivoceranib/camrelizumab; company later said deficiencies were GMP/BIMO not efficacy/safety data.
- Source: https://www.bioworld.com/articles/708761-fda-issues-crl-on-rivoceranib-camrelizumab-combo-in-liver-cancer ; https://elevartx.com/2024/09/23/elevar-therapeutics-resubmits-new-drug-application/
- Result: 30D MFE/MAE `9.99% / -32.71%`; 90D `46.20% / -32.71%`; 180D `46.20% / -32.71%`, peak `2024-07-08` at `98100`, post-peak drawdown `-53.98%`.
- Residual: `CRL_without_clinical_data_deficiency_routes_to_4b_watch_not_sticky_hard_4c`; proposed after-stage `Stage4B`; verdict `current_profile_false_positive_if_hard_4c_sticky`.

### C24_211_HANMI_POZIOTINIB_ODAC_RISK_BENEFIT_FAIL — 128940 Hanmi Pharm
- Trigger: `Stage4C` on `2022-09-23`, entry `2022-09-23` close `237000`.
- Actual Stock-Web entry OHLCV: `2022-09-23 o=236000 h=241500 l=231500 c=237000 v=63953`.
- Evidence: FDA ODAC voted benefits did not outweigh risks; later CRL required additional data.
- Source: https://www.businesswire.com/news/home/20220922005870/en/Spectrum-Pharmaceuticals-Provides-Update-on-Poziotinib-Following-FDA-Oncologic-Drugs-Advisory-Committee-Meeting ; https://www.onclive.com/view/fda-issues-complete-response-letter-to-poziotinib-for-metastatic-nsclc-harboring-her2-exon-20-mutations
- Result: 30D MFE/MAE `11.39% / -5.70%`; 90D `29.96% / -5.70%`; 180D `43.25% / -5.70%`, peak `2023-04-14` at `339500`, post-peak drawdown `-34.17%`.
- Residual: `program_level_4c_should_not_be_issuer_level_sticky_when_diversified_ops_offset`; proposed after-stage `Stage4C`; verdict `current_profile_false_positive_if_issuer_level_4c`.

### C24_211_ABL_SANOFI_PRECLINICAL_LICENSE_NOT_ENDPOINT_DATA — 298380 ABL Bio
- Trigger: `Stage2` on `2022-01-12`, entry `2022-01-12` close `26150`.
- Actual Stock-Web entry OHLCV: `2022-01-12 o=24950 h=26150 l=24650 c=26150 v=4098067`.
- Evidence: Sanofi collaboration for preclinical ABL301; Phase 1 handoff but no human endpoint at trigger date.
- Source: https://www.ablbio.com/en/company/news_view/438?keyword= ; https://www.prnewswire.com/news-releases/abl-bio-enters-global-collaboration-and-license-agreement-with-sanofi-to-advance-abl301-for-the-treatment-of-parkinsons-disease-301458951.html
- Result: 30D MFE/MAE `33.08% / -8.99%`; 90D `33.08% / -26.58%`; 180D `33.08% / -27.92%`, peak `2022-01-21` at `34800`, post-peak drawdown `-45.83%`.
- Residual: `large_license_upfront_is_not_trial_data_actionable_without_endpoint_or_safety_readout`; proposed after-stage `Stage2`; verdict `current_profile_false_positive_if_actionable`.

### C24_211_LIGACHEM_LCB84_JANSSEN_CORP_ACTION_BLOCKED — 141080 LigaChem Biosciences — narrative-only blocked
- Trigger: `Stage2` on `2023-12-26`, entry `2023-12-26` close `57400`.
- Evidence: LCB84 Janssen license; Phase 1/2 initiated, preclinical safety/efficacy data, but 180D price window has stock/share discontinuity.
- Source: https://www.legochembio.com/media/press_view.php?lang=e&sc_seq=594 ; https://jnjinnovation.com/news/press-releases/legochem-biosciences-announces-license-agreement-for-lcb84-trop2targeted-adc
- Price note: 180D MFE/MAE would be `86.24% / -19.25%`, but the 180D window has a Stock-Web corporate-action candidate from share-count discontinuity; therefore calibration_usable=false.
- Residual: `valid_taxonomy_note_but_not_weight_usable_due_corporate_action_window`.

## 5. Current Calibrated Profile Stress Test

The current calibrated profile is directionally right: Stage3-Green must stay blocked for trial-event rows unless clinical data are paired with a second bridge. This batch still shows two residual problems. First, a positive Phase 3 endpoint can be under-credited when it has a named global partner and a clear future regulatory/commercial route. Second, negative trial or regulatory events can be over-stuck as issuer-level hard 4C when the failure is program-specific, inspection/GMP-specific, or offset by a broader operating franchise.

```text
existing_axis_tested: stage2_actionable_evidence_bonus, hard_4c_thesis_break_routes_to_4c, stage3_green_not_loosened, high_MAE_green_blocker
existing_axis_strengthened: stage2_required_bridge, hard_4c_confirmation, stage3_green_not_loosened
existing_axis_refined: endpoint_failure_vs_regulatory_offset_split, issuer_level_offset_check
existing_axis_weakened: none
new_axis_proposed: no_global_axis; canonical C24 endpoint/safety/CRL second-bridge gate only
```

## 6. Score Simulation Profiles

```jsonl
{"profile_id":"P0_e2r_2_2_current_proxy","profile_scope":"current_proxy","profile_hypothesis":"Existing calibrated profile with strong Information Confidence weight in C24; may still confuse endpoint event with issuer-level thesis break","changed_axes":[],"eligible_trigger_count":7,"avg_MFE_90D_pct":30.76,"avg_MAE_90D_pct":-25.97,"current_profile_error_count":4,"score_return_alignment_verdict":"mixed_endpoint_quality_cluster"}
{"profile_id":"P1_C24_endpoint_second_bridge_candidate","profile_scope":"canonical_archetype_specific","profile_hypothesis":"Stage2-Actionable in C24 requires positive endpoint/safety data plus partner/regulatory/commercial route; Green requires revenue or approval conversion","changed_axes":["C24_endpoint_second_bridge_required","C24_green_blocker_without_commercialization"],"eligible_trigger_count":7,"avg_MFE_90D_pct":30.76,"avg_MAE_90D_pct":-25.97,"score_return_alignment_verdict":"better_positive_vs_false_positive_split"}
{"profile_id":"P2_C24_hard4c_offset_candidate","profile_scope":"canonical_archetype_specific","profile_hypothesis":"Hard 4C requires confirmed endpoint/safety/risk-benefit failure with weak offset quality; CRL due GMP/BIMO or diversified issuer offset routes first to 4B/watch","changed_axes":["C24_hard4c_requires_clinical_thesis_break","issuer_level_offset_check"],"eligible_trigger_count":7,"avg_MFE_180D_pct":52.47,"avg_MAE_180D_pct":-26.16,"score_return_alignment_verdict":"reduces_sticky_4c_false_positive"}
```

## 7. Machine-readable Trigger Rows

```jsonl
{"row_type": "trigger", "schema_version": "v12_residual_research", "case_id": "C24_211_YUHAN_MARIPOSA_PHASE3_POSITIVE", "symbol": "000100", "company": "Yuhan Corporation", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-23", "entry_date": "2023-10-23", "entry_price": 62000.0, "actual_entry_ohlcv": {"d": "2023-10-23", "o": 62500.0, "h": 63400.0, "l": 61300.0, "c": 62000.0, "v": 664563, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30D_pct": 3.55, "mae_30D_pct": -11.45, "mfe_90D_pct": 15.48, "mae_90D_pct": -11.45, "mfe_180D_pct": 61.94, "mae_180D_pct": -11.45, "peak_180D_date": "2024-07-16", "post_peak_drawdown_180D_pct": -45.32, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "role": "positive_control", "current_profile_verdict": "current_profile_correct_but_green_blocked", "evidence_family": "phase3_endpoint_positive_partnered_commercial_option", "source_urls": ["https://www.annalsofoncology.org/article/S0923-7534(23)04206-0/fulltext", "https://www.rybrevanthcp.com/clinical-data/mariposa/"], "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 20, "bottleneck_pricing": 4, "market_mispricing": 9, "valuation_rerating": 10, "capital_allocation": 4, "information_confidence": 18}, "score_total_proxy": 75, "residual_label": "positive_phase3_pfs_data_with_partnered_route_but_no_immediate_revenue_bridge", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "case_id": "C24_211_OSCOTEC_MARIPOSA_ROYALTY_OPTION", "symbol": "039200", "company": "Oscotec", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-23", "entry_date": "2023-10-23", "entry_price": 21850.0, "actual_entry_ohlcv": {"d": "2023-10-23", "o": 22100.0, "h": 22300.0, "l": 20700.0, "c": 21850.0, "v": 622220, "m": "KOSDAQ"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30D_pct": 2.06, "mae_30D_pct": -17.62, "mfe_90D_pct": 13.27, "mae_90D_pct": -17.62, "mfe_180D_pct": 105.49, "mae_180D_pct": -17.62, "peak_180D_date": "2024-07-16", "post_peak_drawdown_180D_pct": -59.91, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "role": "positive_high_MAE_control", "current_profile_verdict": "current_profile_too_late_if_actionable_blocked", "evidence_family": "phase3_endpoint_positive_royalty_option", "source_urls": ["https://www.annalsofoncology.org/article/S0923-7534(23)04206-0/fulltext", "https://oscotec.com/?document_srl=739&listStyle=viewer&mid=PressReleases"], "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 18, "bottleneck_pricing": 4, "market_mispricing": 12, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 18}, "score_total_proxy": 70, "residual_label": "partnered_phase3_success_can_be_stage2_actionable_but_royalty_revenue_timing_blocks_green", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "case_id": "C24_211_HELIXMITH_VM202_DPN_PRIMARY_ENDPOINT_FAIL", "symbol": "084990", "company": "Helixmith", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1", "trigger_type": "Stage4C", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 4250.0, "actual_entry_ohlcv": {"d": "2024-01-03", "o": 4250.0, "h": 4450.0, "l": 4250.0, "c": 4250.0, "v": 3868841, "m": "KOSDAQ"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30D_pct": 75.06, "mae_30D_pct": -23.53, "mfe_90D_pct": 75.06, "mae_90D_pct": -23.53, "mfe_180D_pct": 75.06, "mae_180D_pct": -23.53, "peak_180D_date": "2024-02-06", "post_peak_drawdown_180D_pct": -56.32, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "role": "endpoint_failure_control", "current_profile_verdict": "current_profile_correct_4c_but_not_sticky_green_blocker", "evidence_family": "phase3_primary_endpoint_failure", "source_urls": ["https://www.asiae.co.kr/en/print.htm?idxno=2024010307510936034", "https://www.yna.co.kr/view/AKR20240104037200002"], "raw_component_score_breakdown": {"eps_fcf_explosion": 0, "earnings_visibility": 2, "bottleneck_pricing": 0, "market_mispricing": 4, "valuation_rerating": 0, "capital_allocation": 2, "information_confidence": 40}, "score_total_proxy": 48, "residual_label": "confirmed_primary_endpoint_failure_is_4c_but_later_bounce_warns_against_price_only_stickiness", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "case_id": "C24_211_SILLAJEN_PHOCUS_FUTILITY_TERMINATION", "symbol": "215600", "company": "SillaJen", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1", "trigger_type": "Stage4C", "trigger_date": "2019-08-02", "entry_date": "2019-08-05", "entry_price": 21850.0, "actual_entry_ohlcv": {"d": "2019-08-05", "o": 21850.0, "h": 21850.0, "l": 21850.0, "c": 21850.0, "v": 235177, "m": "KOSDAQ"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30D_pct": 0.0, "mae_30D_pct": -58.81, "mfe_90D_pct": 2.29, "mae_90D_pct": -64.21, "mfe_180D_pct": 2.29, "mae_180D_pct": -64.21, "peak_180D_date": "2019-10-24", "post_peak_drawdown_180D_pct": -65.01, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "role": "terminal_trial_failure_control", "current_profile_verdict": "current_profile_correct", "evidence_family": "phase3_futility_early_termination", "source_urls": ["https://www.prnewswire.com/news-releases/sillajen-announces-conclusions-from-interim-futility-analysis-of-phase-3-phocus-trial-in-hcc-300895539.html", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11095598/"], "raw_component_score_breakdown": {"eps_fcf_explosion": 0, "earnings_visibility": 2, "bottleneck_pricing": 0, "market_mispricing": 4, "valuation_rerating": 0, "capital_allocation": 2, "information_confidence": 40}, "score_total_proxy": 48, "residual_label": "terminal_phase3_futility_has_no_second_bridge_and_supports_hard_4c", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "case_id": "C24_211_HLB_CRL_CLINICAL_DATA_INTACT_REGULATORY_OFFSET", "symbol": "028300", "company": "HLB", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1", "trigger_type": "Stage4B", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 67100.0, "actual_entry_ohlcv": {"d": "2024-05-17", "o": 67100.0, "h": 67100.0, "l": 67100.0, "c": 67100.0, "v": 617840, "m": "KOSDAQ"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30D_pct": 9.99, "mae_30D_pct": -32.71, "mfe_90D_pct": 46.2, "mae_90D_pct": -32.71, "mfe_180D_pct": 46.2, "mae_180D_pct": -32.71, "peak_180D_date": "2024-07-08", "post_peak_drawdown_180D_pct": -53.98, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "role": "regulatory_offset_case", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_sticky", "evidence_family": "regulatory_crl_with_nonclinical_offset", "source_urls": ["https://www.bioworld.com/articles/708761-fda-issues-crl-on-rivoceranib-camrelizumab-combo-in-liver-cancer", "https://elevartx.com/2024/09/23/elevar-therapeutics-resubmits-new-drug-application/"], "raw_component_score_breakdown": {"eps_fcf_explosion": 2, "earnings_visibility": 8, "bottleneck_pricing": 2, "market_mispricing": 8, "valuation_rerating": 4, "capital_allocation": 3, "information_confidence": 24}, "score_total_proxy": 51, "residual_label": "CRL_without_clinical_data_deficiency_routes_to_4b_watch_not_sticky_hard_4c", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "case_id": "C24_211_HANMI_POZIOTINIB_ODAC_RISK_BENEFIT_FAIL", "symbol": "128940", "company": "Hanmi Pharm", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1", "trigger_type": "Stage4C", "trigger_date": "2022-09-23", "entry_date": "2022-09-23", "entry_price": 237000.0, "actual_entry_ohlcv": {"d": "2022-09-23", "o": 236000.0, "h": 241500.0, "l": 231500.0, "c": 237000.0, "v": 63953, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30D_pct": 11.39, "mae_30D_pct": -5.7, "mfe_90D_pct": 29.96, "mae_90D_pct": -5.7, "mfe_180D_pct": 43.25, "mae_180D_pct": -5.7, "peak_180D_date": "2023-04-14", "post_peak_drawdown_180D_pct": -34.17, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "role": "program_thesis_break_with_issuer_offset", "current_profile_verdict": "current_profile_false_positive_if_issuer_level_4c", "evidence_family": "odac_negative_risk_benefit_vote", "source_urls": ["https://www.businesswire.com/news/home/20220922005870/en/Spectrum-Pharmaceuticals-Provides-Update-on-Poziotinib-Following-FDA-Oncologic-Drugs-Advisory-Committee-Meeting", "https://www.onclive.com/view/fda-issues-complete-response-letter-to-poziotinib-for-metastatic-nsclc-harboring-her2-exon-20-mutations"], "raw_component_score_breakdown": {"eps_fcf_explosion": 0, "earnings_visibility": 2, "bottleneck_pricing": 0, "market_mispricing": 4, "valuation_rerating": 0, "capital_allocation": 2, "information_confidence": 40}, "score_total_proxy": 48, "residual_label": "program_level_4c_should_not_be_issuer_level_sticky_when_diversified_ops_offset", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "case_id": "C24_211_ABL_SANOFI_PRECLINICAL_LICENSE_NOT_ENDPOINT_DATA", "symbol": "298380", "company": "ABL Bio", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1", "trigger_type": "Stage2", "trigger_date": "2022-01-12", "entry_date": "2022-01-12", "entry_price": 26150.0, "actual_entry_ohlcv": {"d": "2022-01-12", "o": 24950.0, "h": 26150.0, "l": 24650.0, "c": 26150.0, "v": 4098067, "m": "KOSDAQ"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30D_pct": 33.08, "mae_30D_pct": -8.99, "mfe_90D_pct": 33.08, "mae_90D_pct": -26.58, "mfe_180D_pct": 33.08, "mae_180D_pct": -27.92, "peak_180D_date": "2022-01-21", "post_peak_drawdown_180D_pct": -45.83, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "role": "stage2_false_positive_guard", "current_profile_verdict": "current_profile_false_positive_if_actionable", "evidence_family": "preclinical_license_without_human_endpoint", "source_urls": ["https://www.ablbio.com/en/company/news_view/438?keyword=", "https://www.prnewswire.com/news-releases/abl-bio-enters-global-collaboration-and-license-agreement-with-sanofi-to-advance-abl301-for-the-treatment-of-parkinsons-disease-301458951.html"], "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 8, "bottleneck_pricing": 3, "market_mispricing": 12, "valuation_rerating": 7, "capital_allocation": 4, "information_confidence": 16}, "score_total_proxy": 53, "residual_label": "large_license_upfront_is_not_trial_data_actionable_without_endpoint_or_safety_readout", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "narrative_only", "case_id": "C24_211_LIGACHEM_LCB84_JANSSEN_CORP_ACTION_BLOCKED", "symbol": "141080", "company": "LigaChem Biosciences", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "trigger_type": "Stage2", "trigger_date": "2023-12-26", "entry_date": "2023-12-26", "entry_price": 57400.0, "calibration_usable": false, "blocked_reason": "corporate_action_contaminated_180D_window", "mfe_180D_pct": 86.24, "mae_180D_pct": -19.25, "source_urls": ["https://www.legochembio.com/media/press_view.php?lang=e&sc_seq=594", "https://jnjinnovation.com/news/press-releases/legochem-biosciences-announces-license-agreement-for-lcb84-trop2targeted-adc"], "residual_label": "valid_taxonomy_note_but_not_weight_usable_due_corporate_action_window", "note": "kept for taxonomy only; not counted in aggregate or weight evidence because 180D window has share-change corporate-action candidate"}
```

## 8. Aggregate / Shadow Weight Candidate

```jsonl
{"row_type":"aggregate","selected_round":"R7","selected_loop":211,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1","usable_trigger_count":7,"positive_case_count":2,"counterexample_or_guardrail_case_count":5,"stage_counts":{"Stage2": 1, "Stage2-Actionable": 2, "Stage3-Yellow": 0, "Stage3-Green": 0, "Stage4B": 1, "Stage4C": 3},"avg_MFE_30D_pct":19.3,"avg_MAE_30D_pct":-22.69,"avg_MFE_90D_pct":30.76,"avg_MAE_90D_pct":-25.97,"avg_MFE_180D_pct":52.47,"avg_MAE_180D_pct":-26.16,"production_scoring_changed":false,"shadow_weight_only":true,"ready_for_batch_ingest":true}
{"row_type":"shadow_weight","scope":"canonical_archetype","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","rule_candidate":"C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1","before_weight_proxy":"5/15/5/10/5/5/55","after_weight_candidate":"5/16/5/9/5/5/55","delta_rationale":"Do not loosen Green. Slightly emphasize visibility only when endpoint/safety data are paired with partner/regulatory/commercial bridge; slightly reduce mispricing credit on data-only rallies.","apply_now":false,"production_scoring_changed":false}
{"row_type":"residual_contribution","loop_contribution_label":"C24_endpoint_safety_CRL_second_bridge_quality_repair","new_axis_proposed":"no_global_axis","existing_axis_strengthened":["stage2_required_bridge","hard_4c_confirmation","stage3_green_not_loosened"],"existing_axis_refined":["issuer_level_offset_check","CRL_clinical_vs_nonclinical_deficiency_split"],"existing_axis_weakened":[],"do_not_propose_new_weight_delta":false}
```

## 9. Rule Candidate

```text
canonical_rule_candidate:
C24_ENDPOINT_SAFETY_CRL_AND_SECOND_BRIDGE_GATE_V1

core residual:
- Positive Phase 3 endpoint, safety, or OS/PFS data can support Stage2-Actionable only when paired with a second bridge:
  named partner route, royalty economics, regulatory filing/approval path, launch timing, reimbursement/commercial route, or explicit revenue conversion.
- Trial-data headline alone remains Stage2 cap. Preclinical license/upfront money is not endpoint data.
- Hard Stage4C is valid when endpoint failure, futility stop, ODAC risk-benefit rejection, CRL requiring new clinical data, or program discontinuation confirms a clinical thesis break.
- CRL or delay caused by GMP/BIMO/inspection deficiency, with no clinical efficacy/safety deficiency, routes first to Stage4B/watch rather than sticky hard 4C.
- Program-level hard 4C should not automatically become issuer-level hard 4C when the issuer has diversified operating or pipeline offset.
- Stage3-Green remains blocked until endpoint success turns into approval, revenue, royalty, reimbursement, or durable commercial economics.
```

## 10. Batch Ingest Self-Audit

```text
new_independent_case_count: 7
new_independent_trigger_count: 7
unique_symbol_count: 7

stage2_count: 1
stage2_actionable_count: 2
stage4b_count: 1
stage4c_count: 3

positive_case_count: 2
counterexample_or_guardrail_case_count: 5
current_profile_error_count: 4

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count_for_usable_rows: 0
insufficient_forward_window_180D_count: 0
narrative_only_blocked_count: 1

production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research run.

When batch-applying v12 residual research, parse this MD as a C24 canonical-archetype candidate only.
Use only calibration_usable=true trigger rows for aggregate/weight evidence.
Keep the LigaChem row as narrative-only taxonomy because corporate-action contamination blocks 180D calibration.
Evaluate whether C24 should add a second-bridge gate separating:
1. endpoint/safety/OS/PFS data + partner/regulatory/commercial route -> Stage2-Actionable possible,
2. preclinical license or trial-data headline alone -> Stage2 cap,
3. endpoint/futility/ODAC/clinical-data CRL failure -> hard 4C only when offset quality is weak,
4. GMP/BIMO/inspection CRL or diversified issuer offset -> Stage4B/watch before sticky 4C.
Do not loosen Stage3-Green. Do not make production scoring changes without batch validation across all C24 representative rows.
```

## 12. Next Research State

```text
completed_round: R7
completed_loop: 211
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 URL/proxy quality repair + R7 C24 endpoint/safety balance reinforcement
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
