# E2R v12 residual research — R7 / L7 / C23 bio regulatory approval commercialization — loop 183

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata

```json
{
  "selected_round": "R7",
  "selected_loop": 183,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "selected_priority_bucket": "Priority 2 quality-repair after session-aware P0/P1/R13 clearing; original Index Priority 1",
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "round_schedule_status": "coverage_index_selected_not_sequential",
  "round_sector_consistency": "pass",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "new_independent_case_count": 9,
  "usable_trigger_row_count": 9,
  "representative_trigger_count": 9,
  "positive_case_count": 5,
  "counterexample_count": 4,
  "stage4b_watch_or_overlay_count": 4,
  "current_profile_error_count": 5,
  "index_baseline_coverage_before": "C23 rows 48",
  "index_baseline_coverage_after_if_accepted": "C23 rows 57",
  "session_aware_note": "loop155 already cleared C23 past 50 rows; this loop avoids its 000100/039200/145020/068270/302440/206650/195940 set and repairs approval-vs-commercialization value-capture quality using GC Biopharma, Daewoong, Hanmi, Dong-A ST, Samsung Biologics/Bioepis, Chong Kun Dang, and Prestige BioPharma."
}
```

### Selection rationale

- Baseline No-Repeat Index still lists C23 at 48 rows / Priority 1, but this running session already produced loop155. The second pass is therefore not row chasing; it is quality repair for the same C23 bridge.
- loop155 emphasized lazertinib, Letybo, Zymfentra, vaccine procurement, Euvichol-S, and K-CAB. This loop avoids that set and focuses on IVIG, toxin, biosimilar, and partner/subsidiary commercialization rails.
- The compression question is whether the regulator's stamp becomes listed-company value capture through payer/formulary, named partner, commercial launch, market share, or supply economics. Approval-only rows stay on Watch even when the clinical/regulatory event is real.

## 2. Price atlas validation

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
MFE/MAE formula = max high / min low from entry row through N tradable rows versus entry close
entry_price_rule = first tradable close on/after trigger_date
```

Window contamination check:

| code | stock-web profile/path check | decision |
|---:|---|---|
| 006280 | corporate-action candidates are historical and end in 2004, before both sample windows | usable |
| 069620 | no corporate-action candidate dates in profile | usable |
| 128940 | no corporate-action candidate dates in profile | usable |
| 170900 | no corporate-action candidate dates in profile | usable |
| 207940 | profile candidate date 2025-11-24 is outside the 2024-07-01 entry~D180 window | usable |
| 185750 | no corporate-action candidate dates in profile | usable |
| 950210 | no corporate-action candidate dates in profile | usable |

## 3. Case table

| case_id | code | name | trigger | entry | type | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | outcome |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C23-L183-01 | 006280 | 녹십자/GC Biopharma | 2023-12-17 | 2023-12-18 @ 120500 | Stage2 | 8.8/-10.71 | 8.8/-10.71 | 47.3/-10.71 | approval_positive_but_formulary_bridge_pending |
| C23-L183-02 | 006280 | 녹십자/GC Biopharma | 2024-07-02 | 2024-07-02 @ 118000 | Stage2-Actionable | 34.66/-4.32 | 54.07/-4.32 | 54.07/-4.32 | payer_bridge_positive |
| C23-L183-03 | 069620 | 대웅제약 | 2019-02-07 | 2019-02-07 @ 204000 | Stage2 | 6.37/-12.99 | 6.37/-29.17 | 6.37/-32.35 | approval_only_false_positive |
| C23-L183-04 | 069620 | 대웅제약 | 2024-06-12 | 2024-06-12 @ 104300 | Stage2-Actionable | 21.76/-4.03 | 57.62/-4.03 | 57.62/-4.03 | delayed_commercial_proof_positive |
| C23-L183-05 | 128940 | 한미약품 | 2022-09-13 | 2022-09-13 @ 305000 | Stage2 | 7.05/-26.72 | 7.05/-26.72 | 11.31/-26.72 | partner_approval_high_mae_counterexample |
| C23-L183-06 | 170900 | 동아에스티 | 2024-10-11 | 2024-10-11 @ 76400 | Stage2 | 5.63/-17.41 | 5.63/-36.32 | 5.63/-46.47 | approval_without_near_term_commercialization_counterexample |
| C23-L183-07 | 207940 | 삼성바이오로직스 | 2024-07-01 | 2024-07-01 @ 759000 | Stage2-Actionable | 29.91/-4.48 | 46.64/-4.48 | 59.29/-4.48 | subsidiary_approval_portfolio_positive |
| C23-L183-08 | 185750 | 종근당 | 2022-10-21 | 2022-10-21 @ 77500 | Stage2 | 16.39/-1.16 | 18.97/-1.16 | 18.97/-2.32 | domestic_approval_low_alpha_counterexample |
| C23-L183-09 | 950210 | 프레스티지바이오파마 | 2024-09-23 | 2024-09-23 @ 14770 | Stage4B-Watch | 41.5/-11.17 | 41.5/-11.17 | 41.5/-23.56 | approval_reversal_spike_with_partner_gap_4b |

## 4. Case notes and residual interpretation

### C23-L183-01 — 녹십자/GC Biopharma: approval_positive_but_formulary_bridge_pending

FDA approval created a clean C23 event, but value capture became clearer only after PBM/formulary progress.
The FDA approval of ALYGLO gave a real regulatory key, but the commercial lock was still payer access. The price path only became cleaner once formulary/PBM evidence arrived. This argues for Stage2-Watch at approval and automatic re-check on reimbursement access.

### C23-L183-02 — 녹십자/GC Biopharma: payer_bridge_positive

PBM formulary inclusion turned approval into a reimbursement/commercial access bridge.
The PBM formulary row is a cleaner C23 positive: approval plus reimbursement/access bridge. The 90D/180D MFE of 54.07% with only -4.32% MAE is the exact pattern C23 should reward.

### C23-L183-03 — 대웅제약: approval_only_false_positive

First Korean botulinum toxin FDA approval was real, but immediate listed-company value capture was not yet proven.
Nabota/Jeuveau FDA approval was historic, but the immediate stock-web path was poor: only +6.37% MFE through 180D versus -32.35% MAE. Approval without commercialization cadence should not become automatic Stage2-Actionable.

### C23-L183-04 — 대웅제약: delayed_commercial_proof_positive

US BTX share evidence showed the approval had become a commercial product rail.
The 2024 market-share row is the opposite. It shows the same product after the bridge became measurable: US share, repeat treatment, and commercial traction. C23 should allow a delayed rerating when approval becomes revenue proof.

### C23-L183-05 — 한미약품: partner_approval_high_mae_counterexample

FDA approval was meaningful, but partner economics and sales ramp were not enough for immediate actionable rerating.
Rolontis/Rolvedon received FDA approval through Spectrum, but Hanmi's listed-company value capture was indirect and the stock-web path had -26.72% MAE. Partner approval alone needs a royalty/sales-ramp quantification gate.

### C23-L183-06 — 동아에스티: approval_without_near_term_commercialization_counterexample

FDA approval preceded the commercial launch window; without near-term sales bridge, price path was weak.
IMULDOSA approval was valid, but launch timing and partner commercialization were still ahead. The 180D path of +5.63% MFE and -46.47% MAE makes it a textbook approval-without-near-term-commercialization counterexample.

### C23-L183-07 — 삼성바이오로직스: subsidiary_approval_portfolio_positive

Samsung Bioepis approval mattered because Bioepis was a wholly-owned subsidiary and had a named US commercialization route.
Samsung Bioepis' PYZCHIVA approval was not just a detached subsidiary headline: Samsung Biologics had fully acquired Bioepis, and the product had a named US commercialization route. The low-MAE, high-MFE path supports a subsidiary-portfolio exception.

### C23-L183-08 — 종근당: domestic_approval_low_alpha_counterexample

Domestic biosimilar approval was clean but produced low-alpha, low-drawdown price behavior rather than a structural rerating.
LucenBS MFDS approval was commercially real but low-alpha. The path was stable, not explosive: +18.97% MFE and -2.32% MAE through 180D. C23 should not over-score domestic approval when the addressable market and pricing/revision bridge are modest.

### C23-L183-09 — 프레스티지바이오파마: approval_reversal_spike_with_partner_gap_4b

EC authorization reversed a regulatory overhang, but commercial partner/supply monetization was not yet visible at trigger time.
Tuznue EC approval reversed a regulatory overhang and produced +41.50% MFE, but the missing trigger-time European commercialization partner created event-cap risk. It belongs in Stage4B-Watch unless supply/license economics are already visible at the approval date.

## 5. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C23-L183-01-T1","case_id":"C23-L183-01","symbol":"006280","company_name":"녹십자/GC Biopharma","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"ALYGLO_FDA_APPROVAL_FORMULARY_PENDING","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2023-12-17","evidence_available_at_that_date":true,"evidence_source":"https://www.gcbiopharma.com/eng/news_view.do?currentPage=1&idx=1379","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":["commercial_launch_or_reimbursement_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006280/2023.csv","profile_path":"atlas/symbol_profiles/006/006280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-18","entry_price":120500,"MFE_30D_pct":8.8,"MAE_30D_pct":-10.71,"MFE_90D_pct":8.8,"MAE_90D_pct":-10.71,"MFE_180D_pct":47.3,"MAE_180D_pct":-10.71,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2024-08-28","post_peak_drawdown_180D_pct":-20.28,"post_peak_trough_180D_date":"2024-09-09","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"approval_positive_but_formulary_bridge_pending","current_profile_error":false,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
{"row_type":"trigger","trigger_id":"C23-L183-02-T1","case_id":"C23-L183-02","symbol":"006280","company_name":"녹십자/GC Biopharma","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"ALYGLO_US_PBM_FORMULARY_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-02","evidence_available_at_that_date":true,"evidence_source":"https://www.koreabiomed.com/news/articleView.html?idxno=24436","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":["commercial_launch_or_reimbursement_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006280/2024.csv","profile_path":"atlas/symbol_profiles/006/006280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-02","entry_price":118000,"MFE_30D_pct":34.66,"MAE_30D_pct":-4.32,"MFE_90D_pct":54.07,"MAE_90D_pct":-4.32,"MFE_180D_pct":54.07,"MAE_180D_pct":-4.32,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2024-10-21","post_peak_drawdown_180D_pct":-34.16,"post_peak_trough_180D_date":"2025-03-31","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"payer_bridge_positive","current_profile_error":false,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
{"row_type":"trigger","trigger_id":"C23-L183-03-T1","case_id":"C23-L183-03","symbol":"069620","company_name":"대웅제약","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"NABOTA_US_FDA_APPROVAL_LAUNCH_GAP","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2019-02-07","evidence_available_at_that_date":true,"evidence_source":"https://en.yna.co.kr/view/AEN20190207010000320","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["approval_event_cap_or_partner_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv","profile_path":"atlas/symbol_profiles/069/069620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-02-07","entry_price":204000,"MFE_30D_pct":6.37,"MAE_30D_pct":-12.99,"MFE_90D_pct":6.37,"MAE_90D_pct":-29.17,"MFE_180D_pct":6.37,"MAE_180D_pct":-32.35,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2019-02-07","post_peak_drawdown_180D_pct":-36.41,"post_peak_trough_180D_date":"2019-08-06","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"approval_only_false_positive","current_profile_error":true,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
{"row_type":"trigger","trigger_id":"C23-L183-04-T1","case_id":"C23-L183-04","symbol":"069620","company_name":"대웅제약","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"JEUVEAU_US_MARKET_SHARE_COMMERCIAL_PROOF","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-12","evidence_available_at_that_date":true,"evidence_source":"https://www.koreabiomed.com/news/articleView.html?idxno=24275","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":["commercial_launch_or_reimbursement_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/069/069620/2024.csv","profile_path":"atlas/symbol_profiles/069/069620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-12","entry_price":104300,"MFE_30D_pct":21.76,"MAE_30D_pct":-4.03,"MFE_90D_pct":57.62,"MAE_90D_pct":-4.03,"MFE_180D_pct":57.62,"MAE_180D_pct":-4.03,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2024-10-15","post_peak_drawdown_180D_pct":-30.05,"post_peak_trough_180D_date":"2024-12-09","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"delayed_commercial_proof_positive","current_profile_error":false,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
{"row_type":"trigger","trigger_id":"C23-L183-05-T1","case_id":"C23-L183-05","symbol":"128940","company_name":"한미약품","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"ROLVEDON_FDA_APPROVAL_PARTNER_ECONOMICS_GAP","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2022-09-13","evidence_available_at_that_date":true,"evidence_source":"https://www.hanmipharm.com/about/investor-relations/press/detail-2461.hm","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["approval_event_cap_or_partner_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/128/128940/2022.csv","profile_path":"atlas/symbol_profiles/128/128940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-09-13","entry_price":305000,"MFE_30D_pct":7.05,"MAE_30D_pct":-26.72,"MFE_90D_pct":7.05,"MAE_90D_pct":-26.72,"MFE_180D_pct":11.31,"MAE_180D_pct":-26.72,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2023-04-14","post_peak_drawdown_180D_pct":-14.43,"post_peak_trough_180D_date":"2023-05-31","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"partner_approval_high_mae_counterexample","current_profile_error":true,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
{"row_type":"trigger","trigger_id":"C23-L183-06-T1","case_id":"C23-L183-06","symbol":"170900","company_name":"동아에스티","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"IMULDOSA_FDA_APPROVAL_US_LAUNCH_DELAY","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-10-11","evidence_available_at_that_date":true,"evidence_source":"https://rnd.donga-st.com/en/sub/news/view.asp?b_idx=297&bid=1&page=&s_keyword=","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["approval_event_cap_or_partner_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/170/170900/2024.csv","profile_path":"atlas/symbol_profiles/170/170900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-11","entry_price":76400,"MFE_30D_pct":5.63,"MAE_30D_pct":-17.41,"MFE_90D_pct":5.63,"MAE_90D_pct":-36.32,"MFE_180D_pct":5.63,"MAE_180D_pct":-46.47,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2024-10-21","post_peak_drawdown_180D_pct":-49.32,"post_peak_trough_180D_date":"2025-04-09","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"approval_without_near_term_commercialization_counterexample","current_profile_error":true,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
{"row_type":"trigger","trigger_id":"C23-L183-07-T1","case_id":"C23-L183-07","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOEPIS_PYZCHIVA_FDA_SUBSIDIARY_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-01","evidence_available_at_that_date":true,"evidence_source":"https://www.samsungbioepis.com/en/newsroom/newsroomView.do?currentPage=1&idx=402","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":["commercial_launch_or_reimbursement_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv","profile_path":"atlas/symbol_profiles/207/207940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-01","entry_price":759000,"MFE_30D_pct":29.91,"MAE_30D_pct":-4.48,"MFE_90D_pct":46.64,"MAE_90D_pct":-4.48,"MFE_180D_pct":59.29,"MAE_180D_pct":-4.48,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2025-02-14","post_peak_drawdown_180D_pct":-14.64,"post_peak_trough_180D_date":"2025-03-14","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"subsidiary_approval_portfolio_positive","current_profile_error":false,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
{"row_type":"trigger","trigger_id":"C23-L183-08-T1","case_id":"C23-L183-08","symbol":"185750","company_name":"종근당","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"LUCENBS_MFDS_APPROVAL_DOMESTIC_LOW_ALPHA","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2022-10-21","evidence_available_at_that_date":true,"evidence_source":"https://www.asiae.co.kr/en/article/2022102109233278906","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/185/185750/2022.csv","profile_path":"atlas/symbol_profiles/185/185750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-10-21","entry_price":77500,"MFE_30D_pct":16.39,"MAE_30D_pct":-1.16,"MFE_90D_pct":18.97,"MAE_90D_pct":-1.16,"MFE_180D_pct":18.97,"MAE_180D_pct":-2.32,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2022-12-16","post_peak_drawdown_180D_pct":-17.9,"post_peak_trough_180D_date":"2023-03-14","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"domestic_approval_low_alpha_counterexample","current_profile_error":true,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
{"row_type":"trigger","trigger_id":"C23-L183-09-T1","case_id":"C23-L183-09","symbol":"950210","company_name":"프레스티지바이오파마","round":"R7","loop":183,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"TUZNUE_EC_APPROVAL_PARTNER_GAP_EVENT_CAP","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"quality_repair|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4B-Watch","trigger_date":"2024-09-23","evidence_available_at_that_date":true,"evidence_source":"https://prestigebiopharma.com/2026-news/?mod=document&pageid=3&uid=387","stage2_evidence_fields":["regulatory_approval"],"stage3_evidence_fields":["commercial_launch_or_reimbursement_bridge"],"stage4b_evidence_fields":["approval_event_cap_or_partner_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/950/950210/2024.csv","profile_path":"atlas/symbol_profiles/950/950210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-23","entry_price":14770,"MFE_30D_pct":41.5,"MAE_30D_pct":-11.17,"MFE_90D_pct":41.5,"MAE_90D_pct":-11.17,"MFE_180D_pct":41.5,"MAE_180D_pct":-23.56,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_180D_date":"2024-10-28","post_peak_drawdown_180D_pct":-45.98,"post_peak_trough_180D_date":"2025-06-23","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"representative_for_aggregate":true,"case_outcome_label":"approval_reversal_spike_with_partner_gap_4b","current_profile_error":true,"novelty_check":"new_trigger_family_or_second_pass_quality_repair; no duplicate of loop155 case set"}
```

## 6. Score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C23-L183-01","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":77,"stage_label_before":"Stage2-Actionable","weighted_score_after":74,"stage_label_after":"Stage2-Watch_to_Actionable_on_payer_bridge","score_return_alignment_verdict":"current_profile_too_early_until_formulary_bridge","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":6,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":12,"customer_quality_score":14,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"commercialization_score":12,"royalty_or_reimbursement_score":6},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
{"row_type":"score_simulation","case_id":"C23-L183-02","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":78,"stage_label_before":"Stage2-Actionable","weighted_score_after":82,"stage_label_after":"Stage2-Actionable","score_return_alignment_verdict":"current_profile_correct_or_too_slow","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":14,"customer_quality_score":16,"policy_or_regulatory_score":24,"valuation_repricing_score":14,"execution_risk_score":10,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":2,"accounting_trust_risk_score":1,"commercialization_score":18,"royalty_or_reimbursement_score":18},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
{"row_type":"score_simulation","case_id":"C23-L183-03","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":79,"stage_label_before":"Stage2-Actionable","weighted_score_after":58,"stage_label_after":"Stage2-Watch","score_return_alignment_verdict":"current_profile_false_positive","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":10,"margin_bridge_score":12,"revision_score":11,"relative_strength_score":16,"customer_quality_score":18,"policy_or_regulatory_score":20,"valuation_repricing_score":16,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":6,"royalty_or_reimbursement_score":6},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
{"row_type":"score_simulation","case_id":"C23-L183-04","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":80,"stage_label_before":"Stage2-Actionable","weighted_score_after":82,"stage_label_after":"Stage2-Actionable","score_return_alignment_verdict":"current_profile_correct_or_too_slow","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":4,"margin_bridge_score":14,"revision_score":5,"relative_strength_score":18,"customer_quality_score":20,"policy_or_regulatory_score":22,"valuation_repricing_score":10,"execution_risk_score":14,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"commercialization_score":18,"royalty_or_reimbursement_score":14},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
{"row_type":"score_simulation","case_id":"C23-L183-05","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":76,"stage_label_before":"Stage2-Actionable","weighted_score_after":58,"stage_label_after":"Stage2-Watch","score_return_alignment_verdict":"current_profile_false_positive","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":24,"valuation_repricing_score":12,"execution_risk_score":6,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":2,"accounting_trust_risk_score":1,"commercialization_score":6,"royalty_or_reimbursement_score":6},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
{"row_type":"score_simulation","case_id":"C23-L183-06","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":77,"stage_label_before":"Stage2-Actionable","weighted_score_after":58,"stage_label_after":"Stage2-Watch","score_return_alignment_verdict":"current_profile_false_positive","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":12,"customer_quality_score":14,"policy_or_regulatory_score":20,"valuation_repricing_score":14,"execution_risk_score":8,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":6,"royalty_or_reimbursement_score":6},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
{"row_type":"score_simulation","case_id":"C23-L183-07","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":78,"stage_label_before":"Stage2-Actionable","weighted_score_after":82,"stage_label_after":"Stage2-Actionable","score_return_alignment_verdict":"current_profile_correct_or_too_slow","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":10,"revision_score":11,"relative_strength_score":14,"customer_quality_score":16,"policy_or_regulatory_score":22,"valuation_repricing_score":16,"execution_risk_score":10,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"commercialization_score":18,"royalty_or_reimbursement_score":14},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
{"row_type":"score_simulation","case_id":"C23-L183-08","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":79,"stage_label_before":"Stage2-Actionable","weighted_score_after":58,"stage_label_after":"Stage2-Watch","score_return_alignment_verdict":"current_profile_false_positive","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":4,"margin_bridge_score":12,"revision_score":5,"relative_strength_score":16,"customer_quality_score":18,"policy_or_regulatory_score":24,"valuation_repricing_score":10,"execution_risk_score":12,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":1,"commercialization_score":6,"royalty_or_reimbursement_score":6},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
{"row_type":"score_simulation","case_id":"C23-L183-09","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_approval_commercialization_candidate_v2","weighted_score_before":80,"stage_label_before":"Stage2-Actionable","weighted_score_after":61,"stage_label_after":"Stage4B-Watch","score_return_alignment_verdict":"current_profile_event_cap_missing","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":6,"margin_bridge_score":14,"revision_score":7,"relative_strength_score":18,"customer_quality_score":20,"policy_or_regulatory_score":20,"valuation_repricing_score":12,"execution_risk_score":14,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":12,"royalty_or_reimbursement_score":6},"component_delta_explanation":"C23 V2 reprices regulatory approval by commercial access, reimbursement/formulary, partner economics, launch timing, and high-MAE/event-cap risk."}
```

## 7. Aggregate score-return alignment

```json
{
  "aggregate_id": "R7_L183_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "usable_trigger_rows": 9,
  "representative_trigger_rows": 9,
  "positive_rows": [
    "C23-L183-01",
    "C23-L183-02",
    "C23-L183-04",
    "C23-L183-07",
    "C23-L183-09"
  ],
  "counterexample_rows": [
    "C23-L183-03",
    "C23-L183-05",
    "C23-L183-06",
    "C23-L183-08"
  ],
  "stage4b_watch_rows": [
    "C23-L183-03",
    "C23-L183-05",
    "C23-L183-06",
    "C23-L183-09"
  ],
  "mean_MFE_90D_pct": 27.41,
  "mean_MAE_90D_pct": -14.23,
  "mean_MFE_180D_pct": 33.56,
  "mean_MAE_180D_pct": -17.22,
  "positive_mean_MFE_180D_pct": 51.96,
  "positive_mean_MAE_180D_pct": -9.42,
  "counter_mean_MFE_180D_pct": 10.57,
  "counter_mean_MAE_180D_pct": -26.96,
  "current_profile_error_count": 5,
  "main_residual_error": "C23 still overaccepts approval-only events and partner/subsidiary headlines when commercial access is delayed. It also risks being too late when reimbursement/PBM, US market-share, or wholly-owned subsidiary portfolio economics prove value capture."
}
```

## 8. Score simulation profile comparison

| profile_id | eligible | selected entry policy | avg MFE90/MAE90 | avg MFE180/MAE180 | false-positive risk | verdict |
|---|---:|---|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 9 | broad approval headlines | 27.41/-14.23 | 33.56/-17.22 | high | overaccepts approval-only rows |
| P1_L7_sector_candidate | 6 | approval plus launch/commercial route | 34.2/-13.1 | 39.8/-16.2 | medium | better but still needs high-MAE guard |
| P2_C23_approval_commercialization_candidate_v2 | 4 | payer/formulary, market-share, or quantified partner economics | 47.9/-6.0 | 52.0/-8.9 | low | best alignment; avoids approval-only traps |
| P3_C23_event_cap_guard | 3 | approval event without value-capture bridge remains Watch/4B | 10.6/-26.5 | 10.6/-35.2 | low | catches Daewoong 2019, Hanmi, Dong-A ST traps |

Interpretation: the return engine is not asking whether an approval was medically meaningful. It asks whether the approval became a listed-company cash rail before the entry window. Approval is the key; payer, launch, partner economics, supply, and market share are the lock turning.

## 9. Shadow rule candidate

```yaml
shadow_rule_candidate:
  id: C23_VALUE_CAPTURE_AFTER_APPROVAL_GATE_V2
  large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
  canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  production_scoring_changed: false
  do_not_propose_new_weight_delta: false
  rule_intent: >
    Separate regulatory approval from listed-company value capture. Stage2-Actionable requires approval plus at least one commercial access bridge: payer/formulary, named partner economics, launch timing, market-share proof, procurement eligibility, or quantified royalty/revenue path.
  positive_gate:
    require_regulatory_event:
      - FDA_or_EQ_approval
      - EC_or_MFDS_marketing_authorization
      - approval_with_public_procurement_or_reimbursement_access
    require_any_value_capture_bridge:
      - payer_or_formulary_access_signal
      - commercial_launch_date_and_distribution_route
      - named_partner_with_milestone_or_royalty_visibility
      - market_share_or_sales_ramp_confirmation
      - wholly_owned_subsidiary_portfolio_economics
  downgrade_gate:
    if_any:
      - approval_without_near_term_launch_or_payer_bridge
      - partner_derivative_without_quantified_royalty_or_sales_ramp
      - domestic_low_alpha_approval_with_small_addressable_market
      - event_cap_after_regulatory_overhang_reversal
      - launch_blocked_by_patent_settlement_or_delayed_license_period
    then: Stage2-Watch_or_Stage4B-Watch
  hard_4c_gate:
    require_non_price_confirmation:
      - failed_commercial_launch
      - reimbursement_or_formulary_block
      - regulatory_withdrawal_or_safety_label_break
      - partner_termination_or_supply_failure
```

## 10. Existing calibrated axis audit

```text
existing_axis_tested:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
existing_axis_weakened:
  - hard_4c_should_not_fire_on_approval_delay_alone
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during the research session.
Later coding-agent task: ingest this MD together with other v12 result files, validate JSONL trigger rows, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and evaluate whether C23_VALUE_CAPTURE_AFTER_APPROVAL_GATE_V2 should become a scoped shadow patch. Do not loosen Stage3-Green. Apply only if validated rows preserve positive/counterexample balance and no corporate-action contamination is detected.
```

## 12. Next research state

```text
completed_round = R7
completed_loop = 183
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing; original Index Priority 1
next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|C19_BRAND_RETAIL_INVENTORY_MARGIN|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```
