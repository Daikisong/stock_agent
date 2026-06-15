# E2R v12 residual research — R7 / L7 / C23 bio regulatory approval commercialization — loop 155

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
  "selected_loop": 155,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "selected_priority_bucket": "Priority 1",
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "round_schedule_status": "coverage_index_selected_not_sequential",
  "round_sector_consistency": "pass",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "new_independent_case_count": 7,
  "usable_trigger_row_count": 7,
  "representative_trigger_count": 7,
  "positive_case_count": 3,
  "counterexample_count": 4,
  "stage4b_watch_or_overlay_count": 4,
  "stage4c_or_false4c_count": 2,
  "current_profile_error_count": 5,
  "index_baseline_coverage_before": "C23 rows 48",
  "index_baseline_coverage_after_if_accepted": "C23 rows 55",
  "need_to_50_after_if_accepted": 0,
  "session_aware_note": "loop154 cleared C05 to the 50-row zone; C23 and C27 remained Priority 1 at 48 rows. This run clears C23 first with seven new symbol/trigger-family rows."
}
```

### Selection rationale

- `V12_Research_No_Repeat_Index.md` baseline shows C23 at 48 representative rows, so it is Priority 1 and only 2 rows short of the 50-row practical calibration zone.
- The current session already cleared P0-heavy C02/C09/C14/C10/C06/C07/C11/C01/C28 and then C12/C05. The remaining 48-row tie is C23/C27; C23 is selected first because R7 has fewer recent session passes.
- Top-covered C23 symbols in the baseline include `006280`, `170900`, `326030`, `069620`, `084990`, and `128940`. This run avoids that visible cluster and uses `000100`, `039200`, `145020`, `068270`, `302440`, `206650`, and `195940`.
- The contribution is not another global approval-positive proof. The C23-specific question is whether regulatory approval actually crosses the bridge into **commercial launch, payer/reimbursement access, royalty/milestone visibility, public procurement, or durable product demand**.

## 2. Price atlas validation

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
MFE/MAE formula = max high / min low from entry row through N tradable rows versus entry close
entry_price_rule = next tradable close after trigger_date unless same-day market reaction is explicitly available
```

Window contamination check:

| code | stock-web profile/path check | decision |
|---:|---|---|
| 000100 | profile candidate dates are historical, last visible candidate 2020-04-08 before sample window | usable |
| 039200 | profile candidate dates end at 2022-11-30, before 2024 sample window | usable |
| 145020 | profile candidate dates end in 2020, before 2024 sample window | usable |
| 068270 | 2024-01-12 candidate is before 2024-03-19 entry; no overlap with entry~D180 | usable |
| 302440 | profile has no corporate-action candidate dates | usable |
| 206650 | profile has no corporate-action candidate dates | usable |
| 195940 | profile has no corporate-action candidate dates | usable |

## 3. Case table

| case_id | code | name | trigger | entry | type | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | outcome |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C23-L155-01 | 000100 | 유한양행 | 2024-08-20 | 2024-08-21 @ 94300 | Stage2-Actionable | 69.99/-2.97 | 76.99/-2.97 | 76.99/-2.97 | approval_to_royalty_positive |
| C23-L155-02 | 039200 | 오스코텍 | 2024-08-20 | 2024-08-21 @ 36900 | Stage2 | 24.25/-11.38 | 24.25/-41.46 | 24.25/-41.46 | partner_royalty_derivative_high_mae |
| C23-L155-03 | 145020 | 휴젤 | 2024-03-04 | 2024-03-05 @ 205500 | Stage2-Actionable | 2.68/-16.16 | 27.74/-16.16 | 58.64/-16.16 | approval_to_us_launch_positive |
| C23-L155-04 | 068270 | 셀트리온 | 2024-03-18 | 2024-03-19 @ 184400 | Stage2 | 5.26/-7.97 | 14.43/-7.97 | 14.43/-13.07 | commercial_launch_ramp_too_slow |
| C23-L155-05 | 302440 | SK바이오사이언스 | 2022-06-29 | 2022-06-30 @ 100500 | Stage4B | 55.72/-4.18 | 55.72/-32.94 | 55.72/-35.12 | approval_spike_then_demand_decay_4b |
| C23-L155-06 | 206650 | 유바이오로직스 | 2024-04-15 | 2024-04-16 @ 12930 | Stage2-Actionable | 12.14/-9.2 | 12.14/-27.69 | 45.4/-27.69 | approval_to_public_procurement_positive_with_mae |
| C23-L155-07 | 195940 | HK이노엔 | 2022-04-14 | 2022-04-14 @ 42700 | Stage2 | 22.48/-12.65 | 22.48/-12.65 | 22.48/-26.7 | approval_launch_without_near_term_earnings_bridge |


## 4. Case notes and residual interpretation

### C23-L155-01 — Yuhan: approval plus direct royalty/milestone bridge is C23 positive

The FDA approval of lazertinib with amivantamab was a clean regulatory event, but the investable part was not the medical label alone. Yuhan had a named global partner route, a licensed-out asset, and visible milestone/royalty logic. The stock-web path after the conservative next-trading entry was unusually clean: +76.99% MFE through 90D/180D with only -2.97% MAE. A current profile that waits for several quarters of reported royalties would be too late.

### C23-L155-02 — Oscotec: same drug, different value-capture layer

Oscotec participates in the lazertinib economics, but it sits one layer farther from direct commercialization control. The same FDA event produced +24.25% maximum upside but -41.46% 90D/180D MAE. This is the central C23 compression lesson: **same regulatory event does not mean same listed-company bridge**. A partner-royalty derivative should pass through a high-MAE/positioning guard unless value capture is directly quantified.

### C23-L155-03 — Hugel: FDA approval can work when the market/category bridge is commercial

Letybo's FDA approval opened the U.S. neuromodulator market. The first 30D path was not clean, but the 180D path reached +58.64% MFE. This is a valid positive, but it is not a pure approval row. It works because the U.S. aesthetics category, distributor/launch route, and global toxin market structure gave the label a commercial rail.

### C23-L155-04 — Celltrion: FDA approval plus launch can still be too slow without payer/formulary ramp

ZYMFENTRA's U.S. commercial availability was real and followed a first-in-class FDA-approved subcutaneous infliximab label. Yet the stock-web path was muted: +14.43% MFE and -13.07% MAE through 180D. For C23, launch availability is necessary but not sufficient; payer access, formulary uptake, prescription curve, and sales cadence are the gears that turn the regulatory key.

### C23-L155-05 — SK Bioscience: vaccine approval spike becomes 4B when demand decays

SKYCovione approval created a strong near-term spike, with +55.72% MFE inside 30D. But the post-peak drawdown reached -58.34%, and 90D/180D MAE moved below -30%. The problem was not regulatory failure; it was commercialization demand decay. C23 should allow Stage4B when the approved product's target market evaporates or procurement uptake stalls.

### C23-L155-06 — EuBiologics: WHO PQ is a procurement gate, but timing risk remains

Euvichol-S WHO prequalification has a stronger commercial bridge than a normal medical headline because it unlocks public-supply eligibility through global health procurement channels. The 180D MFE was +45.40%, but MAE hit -27.69%. This is a positive with a guard: public procurement creates a rail, but tender/order timing decides whether Stage2-Actionable is immediate or staged.

### C23-L155-07 — HK inno.N: overseas approval/launch without near-term earnings bridge is not enough

K-CAB China approval and launch planning created a clean C23 headline, and the first 30D MFE reached +22.48%. But the same row had -26.70% 180D MAE. Approval in an overseas market needs a listed-company bridge through royalty rate, shipment timing, local partner economics, or revision. Without that, Stage2 should remain Watch.

## 5. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C23-L155-01-T1","case_id":"C23-L155-01","symbol":"000100","company_name":"유한양행","round":"R7","loop":155,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"LAZERTINIB_US_FDA_APPROVAL_ROYALTY","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","evidence_available_at_that_date":true,"evidence_source":"https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer","stage2_evidence_fields":["regulatory_approval","commercialization_route"],"stage3_evidence_fields":["royalty_or_sales_ramp_confirmed"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-21","entry_price":94300,"MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":76.99,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":-2.97,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"approval_to_royalty_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":328,"calibration_block_reasons":[],"corporate_action_window_status":"profile_candidate_dates_do_not_overlap_entry_to_D180_or_no_candidates;share_count_drift_not_treated_as_CA_without_profile_candidate","same_entry_group_id":"000100|2024-08-21|94300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":8,"margin_bridge_score":14,"revision_score":16,"relative_strength_score":20,"customer_quality_score":22,"policy_or_regulatory_score":24,"valuation_repricing_score":16,"execution_risk_score":4,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":20,"royalty_or_reimbursement_score":19},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":8,"margin_bridge_score":14,"revision_score":16,"relative_strength_score":20,"customer_quality_score":22,"policy_or_regulatory_score":24,"valuation_repricing_score":16,"execution_risk_score":4,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":23,"royalty_or_reimbursement_score":19},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow","component_delta_explanation":"C23-specific gate separates regulatory approval headline from commercialization/reimbursement/royalty conversion and adds demand-decay or payer-ramp guard when needed."}
{"row_type":"trigger","trigger_id":"C23-L155-02-T1","case_id":"C23-L155-02","symbol":"039200","company_name":"오스코텍","round":"R7","loop":155,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"PARTNER_ROYALTY_DERIVATIVE_HIGH_BETA","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-08-20","evidence_available_at_that_date":true,"evidence_source":"https://oscotec.com/Lungcancer","stage2_evidence_fields":["regulatory_approval","commercialization_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv","profile_path":"atlas/symbol_profiles/039/039200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-21","entry_price":36900,"MFE_30D_pct":24.25,"MFE_90D_pct":24.25,"MFE_180D_pct":24.25,"MFE_1Y_pct":24.25,"MFE_2Y_pct":null,"MAE_30D_pct":-11.38,"MAE_90D_pct":-41.46,"MAE_180D_pct":-41.46,"MAE_1Y_pct":-41.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-21","peak_price":45850,"drawdown_after_peak_pct":-52.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"requires_pairwise_stage2_anchor","four_b_full_window_peak_proximity":"requires_pairwise_stage2_anchor","four_b_timing_verdict":"approval_headline_local_peak_then_full_window_drawdown","four_b_evidence_type":"positioning_overheat","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"partner_royalty_derivative_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":328,"calibration_block_reasons":[],"corporate_action_window_status":"profile_candidate_dates_do_not_overlap_entry_to_D180_or_no_candidates;share_count_drift_not_treated_as_CA_without_profile_candidate","same_entry_group_id":"039200|2024-08-21|36900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":11,"backlog_visibility_score":5,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":18,"customer_quality_score":15,"policy_or_regulatory_score":24,"valuation_repricing_score":10,"execution_risk_score":11,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2,"commercialization_score":9,"royalty_or_reimbursement_score":13},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":11,"backlog_visibility_score":5,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":18,"customer_quality_score":15,"policy_or_regulatory_score":24,"valuation_repricing_score":10,"execution_risk_score":11,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2,"commercialization_score":5,"royalty_or_reimbursement_score":13},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","component_delta_explanation":"C23-specific gate separates regulatory approval headline from commercialization/reimbursement/royalty conversion and adds demand-decay or payer-ramp guard when needed."}
{"row_type":"trigger","trigger_id":"C23-L155-03-T1","case_id":"C23-L155-03","symbol":"145020","company_name":"휴젤","round":"R7","loop":155,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_FDA_APPROVAL_COMMERCIAL_LAUNCH","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-04","evidence_available_at_that_date":true,"evidence_source":"https://hugel-aesthetics.com/news-press-releases/","stage2_evidence_fields":["regulatory_approval","commercialization_route"],"stage3_evidence_fields":["royalty_or_sales_ramp_confirmed"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-05","entry_price":205500,"MFE_30D_pct":2.68,"MFE_90D_pct":27.74,"MFE_180D_pct":58.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.16,"MAE_90D_pct":-16.16,"MAE_180D_pct":-16.16,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-22.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"approval_to_us_launch_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":201,"calibration_block_reasons":[],"corporate_action_window_status":"profile_candidate_dates_do_not_overlap_entry_to_D180_or_no_candidates;share_count_drift_not_treated_as_CA_without_profile_candidate","same_entry_group_id":"145020|2024-03-05|205500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":6,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":24,"valuation_repricing_score":14,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":18,"royalty_or_reimbursement_score":12},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":6,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":24,"valuation_repricing_score":14,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":21,"royalty_or_reimbursement_score":12},"weighted_score_after":83,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"C23-specific gate separates regulatory approval headline from commercialization/reimbursement/royalty conversion and adds demand-decay or payer-ramp guard when needed."}
{"row_type":"trigger","trigger_id":"C23-L155-04-T1","case_id":"C23-L155-04","symbol":"068270","company_name":"셀트리온","round":"R7","loop":155,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVAL_TO_LAUNCH_PAYER_FORMULARY_RAMP","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-18","evidence_available_at_that_date":true,"evidence_source":"https://www.celltrion.com/en-us/company/media-center/press-release/3128","stage2_evidence_fields":["regulatory_approval","commercialization_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["reimbursement_or_formulary_ramp_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv","profile_path":"atlas/symbol_profiles/068/068270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-19","entry_price":184400,"MFE_30D_pct":5.26,"MFE_90D_pct":14.43,"MFE_180D_pct":14.43,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.97,"MAE_90D_pct":-7.97,"MAE_180D_pct":-13.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":211000,"drawdown_after_peak_pct":-24.03,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"reimbursement_or_formulary_ramp_gap","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"commercial_launch_ramp_too_slow","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":191,"calibration_block_reasons":[],"corporate_action_window_status":"profile_candidate_dates_do_not_overlap_entry_to_D180_or_no_candidates;share_count_drift_not_treated_as_CA_without_profile_candidate","same_entry_group_id":"068270|2024-03-19|184400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":9,"backlog_visibility_score":5,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":10,"customer_quality_score":15,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":12,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"commercialization_score":10,"royalty_or_reimbursement_score":7},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":9,"backlog_visibility_score":5,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":10,"customer_quality_score":15,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":12,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"commercialization_score":6,"royalty_or_reimbursement_score":7},"weighted_score_after":68,"stage_label_after":"Stage2-Watch","component_delta_explanation":"C23-specific gate separates regulatory approval headline from commercialization/reimbursement/royalty conversion and adds demand-decay or payer-ramp guard when needed."}
{"row_type":"trigger","trigger_id":"C23-L155-05-T1","case_id":"C23-L155-05","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":155,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"VACCINE_APPROVAL_DEMAND_DECAY_4B","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2022-06-29","evidence_available_at_that_date":true,"evidence_source":"https://en.yna.co.kr/view/AEN20220629005300320","stage2_evidence_fields":["approval_headline","demand_decay_risk"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["demand_decay_after_approval"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv","profile_path":"atlas/symbol_profiles/302/302440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-06-30","entry_price":100500,"MFE_30D_pct":55.72,"MFE_90D_pct":55.72,"MFE_180D_pct":55.72,"MFE_1Y_pct":55.72,"MFE_2Y_pct":null,"MAE_30D_pct":-4.18,"MAE_90D_pct":-32.94,"MAE_180D_pct":-35.12,"MAE_1Y_pct":-35.12,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-07-13","peak_price":156500,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"requires_pairwise_stage2_anchor","four_b_full_window_peak_proximity":"requires_pairwise_stage2_anchor","four_b_timing_verdict":"approval_headline_local_peak_then_full_window_drawdown","four_b_evidence_type":"demand_decay_after_approval","four_c_protection_label":"hard_4c_success_if_demand_collapse_confirmed","trigger_outcome_label":"approval_spike_then_demand_decay_4b","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":370,"calibration_block_reasons":[],"corporate_action_window_status":"profile_candidate_dates_do_not_overlap_entry_to_D180_or_no_candidates;share_count_drift_not_treated_as_CA_without_profile_candidate","same_entry_group_id":"302440|2022-06-30|100500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":22,"customer_quality_score":11,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":19,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":4,"royalty_or_reimbursement_score":1},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":22,"customer_quality_score":11,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":19,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":0,"royalty_or_reimbursement_score":1},"weighted_score_after":56,"stage_label_after":"Stage4B","component_delta_explanation":"C23-specific gate separates regulatory approval headline from commercialization/reimbursement/royalty conversion and adds demand-decay or payer-ramp guard when needed."}
{"row_type":"trigger","trigger_id":"C23-L155-06-T1","case_id":"C23-L155-06","symbol":"206650","company_name":"유바이오로직스","round":"R7","loop":155,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"WHO_PREQUALIFICATION_PUBLIC_SUPPLY_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-15","evidence_available_at_that_date":true,"evidence_source":"https://www.unicef.org/press-releases/gavi-and-unicef-welcome-approval-new-oral-cholera-vaccine","stage2_evidence_fields":["regulatory_approval","commercialization_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["public_procurement_timing_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/206/206650/2024.csv","profile_path":"atlas/symbol_profiles/206/206650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-16","entry_price":12930,"MFE_30D_pct":12.14,"MFE_90D_pct":12.14,"MFE_180D_pct":45.4,"MFE_1Y_pct":45.4,"MFE_2Y_pct":null,"MAE_30D_pct":-9.2,"MAE_90D_pct":-27.69,"MAE_180D_pct":-27.69,"MAE_1Y_pct":-27.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-06","peak_price":18800,"drawdown_after_peak_pct":-37.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"requires_pairwise_stage2_anchor","four_b_full_window_peak_proximity":"requires_pairwise_stage2_anchor","four_b_timing_verdict":"approval_headline_local_peak_then_full_window_drawdown","four_b_evidence_type":"public_procurement_timing_risk","four_c_protection_label":"not_applicable","trigger_outcome_label":"approval_to_public_procurement_positive_with_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":414,"calibration_block_reasons":[],"corporate_action_window_status":"profile_candidate_dates_do_not_overlap_entry_to_D180_or_no_candidates;share_count_drift_not_treated_as_CA_without_profile_candidate","same_entry_group_id":"206650|2024-04-16|12930","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":11,"revision_score":10,"relative_strength_score":10,"customer_quality_score":20,"policy_or_regulatory_score":23,"valuation_repricing_score":14,"execution_risk_score":10,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":1,"commercialization_score":17,"royalty_or_reimbursement_score":16},"weighted_score_before":74,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":11,"revision_score":10,"relative_strength_score":10,"customer_quality_score":20,"policy_or_regulatory_score":23,"valuation_repricing_score":14,"execution_risk_score":10,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":1,"commercialization_score":20,"royalty_or_reimbursement_score":16},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"C23-specific gate separates regulatory approval headline from commercialization/reimbursement/royalty conversion and adds demand-decay or payer-ramp guard when needed."}
{"row_type":"trigger","trigger_id":"C23-L155-07-T1","case_id":"C23-L155-07","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":155,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CHINA_APPROVAL_LAUNCH_MARGIN_RAMP_GAP","sector":"bio_healthcare_medical","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2022-04-14","evidence_available_at_that_date":true,"evidence_source":"https://pulse.mk.co.kr/news/english/10289876","stage2_evidence_fields":["regulatory_approval","commercialization_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["commercialization_ramp_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/195/195940/2022.csv","profile_path":"atlas/symbol_profiles/195/195940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-04-14","entry_price":42700,"MFE_30D_pct":22.48,"MFE_90D_pct":22.48,"MFE_180D_pct":22.48,"MFE_1Y_pct":22.48,"MFE_2Y_pct":22.48,"MAE_30D_pct":-12.65,"MAE_90D_pct":-12.65,"MAE_180D_pct":-26.7,"MAE_1Y_pct":-26.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-05-23","peak_price":52300,"drawdown_after_peak_pct":-40.15,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"requires_pairwise_stage2_anchor","four_b_full_window_peak_proximity":"requires_pairwise_stage2_anchor","four_b_timing_verdict":"approval_headline_local_peak_then_full_window_drawdown","four_b_evidence_type":"commercialization_ramp_gap","four_c_protection_label":"false_break","trigger_outcome_label":"approval_launch_without_near_term_earnings_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":908,"calibration_block_reasons":[],"corporate_action_window_status":"profile_candidate_dates_do_not_overlap_entry_to_D180_or_no_candidates;share_count_drift_not_treated_as_CA_without_profile_candidate","same_entry_group_id":"195940|2022-04-14|42700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"none","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":4,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":13,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":8,"royalty_or_reimbursement_score":5},"weighted_score_before":73,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":4,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":13,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":4,"royalty_or_reimbursement_score":5},"weighted_score_after":62,"stage_label_after":"Stage2-Watch","component_delta_explanation":"C23-specific gate separates regulatory approval headline from commercialization/reimbursement/royalty conversion and adds demand-decay or payer-ramp guard when needed."}
```

## 6. Score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C23-L155-01","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_canonical_candidate","weighted_score_before":82,"stage_label_before":"Stage2-Actionable","weighted_score_after":88,"stage_label_after":"Stage3-Yellow","score_return_alignment_verdict":"current_profile_too_late","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":8,"margin_bridge_score":14,"revision_score":16,"relative_strength_score":20,"customer_quality_score":22,"policy_or_regulatory_score":24,"valuation_repricing_score":16,"execution_risk_score":4,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":20,"royalty_or_reimbursement_score":19},"component_delta_explanation":"C23 approval headline is repriced by commercialization_score, royalty_or_reimbursement_score, and demand-decay/payer-ramp risk."}
{"row_type":"score_simulation","case_id":"C23-L155-02","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_canonical_candidate","weighted_score_before":78,"stage_label_before":"Stage2-Actionable","weighted_score_after":64,"stage_label_after":"Stage2-Watch","score_return_alignment_verdict":"current_profile_false_positive","raw_component_scores_before":{"contract_score":11,"backlog_visibility_score":5,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":18,"customer_quality_score":15,"policy_or_regulatory_score":24,"valuation_repricing_score":10,"execution_risk_score":11,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2,"commercialization_score":9,"royalty_or_reimbursement_score":13},"component_delta_explanation":"C23 approval headline is repriced by commercialization_score, royalty_or_reimbursement_score, and demand-decay/payer-ramp risk."}
{"row_type":"score_simulation","case_id":"C23-L155-03","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_canonical_candidate","weighted_score_before":76,"stage_label_before":"Stage2-Actionable","weighted_score_after":83,"stage_label_after":"Stage2-Actionable","score_return_alignment_verdict":"current_profile_correct","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":6,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":24,"valuation_repricing_score":14,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":18,"royalty_or_reimbursement_score":12},"component_delta_explanation":"C23 approval headline is repriced by commercialization_score, royalty_or_reimbursement_score, and demand-decay/payer-ramp risk."}
{"row_type":"score_simulation","case_id":"C23-L155-04","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_canonical_candidate","weighted_score_before":77,"stage_label_before":"Stage2-Actionable","weighted_score_after":68,"stage_label_after":"Stage2-Watch","score_return_alignment_verdict":"current_profile_false_positive","raw_component_scores_before":{"contract_score":9,"backlog_visibility_score":5,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":10,"customer_quality_score":15,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":12,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"commercialization_score":10,"royalty_or_reimbursement_score":7},"component_delta_explanation":"C23 approval headline is repriced by commercialization_score, royalty_or_reimbursement_score, and demand-decay/payer-ramp risk."}
{"row_type":"score_simulation","case_id":"C23-L155-05","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_canonical_candidate","weighted_score_before":80,"stage_label_before":"Stage2-Actionable","weighted_score_after":56,"stage_label_after":"Stage4B","score_return_alignment_verdict":"current_profile_4B_too_late","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":22,"customer_quality_score":11,"policy_or_regulatory_score":22,"valuation_repricing_score":12,"execution_risk_score":19,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":4,"royalty_or_reimbursement_score":1},"component_delta_explanation":"C23 approval headline is repriced by commercialization_score, royalty_or_reimbursement_score, and demand-decay/payer-ramp risk."}
{"row_type":"score_simulation","case_id":"C23-L155-06","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_canonical_candidate","weighted_score_before":74,"stage_label_before":"Stage2","weighted_score_after":79,"stage_label_after":"Stage2-Actionable","score_return_alignment_verdict":"current_profile_correct","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":11,"revision_score":10,"relative_strength_score":10,"customer_quality_score":20,"policy_or_regulatory_score":23,"valuation_repricing_score":14,"execution_risk_score":10,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":2,"accounting_trust_risk_score":1,"commercialization_score":17,"royalty_or_reimbursement_score":16},"component_delta_explanation":"C23 approval headline is repriced by commercialization_score, royalty_or_reimbursement_score, and demand-decay/payer-ramp risk."}
{"row_type":"score_simulation","case_id":"C23-L155-07","profile_before":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_after":"P2_C23_canonical_candidate","weighted_score_before":73,"stage_label_before":"Stage2","weighted_score_after":62,"stage_label_after":"Stage2-Watch","score_return_alignment_verdict":"current_profile_false_positive","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":4,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":13,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"commercialization_score":8,"royalty_or_reimbursement_score":5},"component_delta_explanation":"C23 approval headline is repriced by commercialization_score, royalty_or_reimbursement_score, and demand-decay/payer-ramp risk."}
```

## 7. Aggregate score-return alignment

```json
{
  "aggregate_id": "R7_L155_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "usable_trigger_rows": 7,
  "representative_trigger_rows": 7,
  "positive_rows": ["C23-L155-01", "C23-L155-03", "C23-L155-06"],
  "counterexample_rows": ["C23-L155-02", "C23-L155-04", "C23-L155-05", "C23-L155-07"],
  "mean_MFE_90D_pct": 33.39,
  "mean_MAE_90D_pct": -20.26,
  "mean_MFE_180D_pct": 42.56,
  "mean_MAE_180D_pct": -23.31,
  "positive_mean_MFE_180D_pct": 60.34,
  "positive_mean_MAE_180D_pct": -15.61,
  "current_profile_error_count": 5,
  "main_residual_error": "C23 approval headlines are overaccepted when commercialization value capture is indirect, payer/formulary ramp is slow, or end-market demand decays. The opposite error is waiting too long when the approval comes with a named global partner, quantified milestone/royalty path, or procurement unlock."
}
```

## 8. Score simulation profile comparison

| profile_id | eligible | selected entry policy | avg MFE90/MAE90 | avg MFE180/MAE180 | false positive rate | verdict |
|---|---:|---|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 7 | all approval/commercial launch rows | 33.39/-20.26 | 42.56/-23.31 | 0.57 | mixed; overaccepts approval-only and partner-derivative rows |
| P0b_e2r_2_0_baseline_reference | 5 | late confirmation only | 34.3/-18.1 | 39.2/-20.4 | 0.45 | too late for Yuhan/Hugel, still weak on demand decay |
| P1_L7_sector_candidate | 5 | approval plus commercialization route | 38.96/-15.61 | 60.34/-15.61 | 0.20 | better alignment; still needs MAE guard for public-procurement and launch timing |
| P2_C23_canonical_candidate | 3 | Yuhan/Hugel/EuBiologics only | 38.96/-15.61 | 60.34/-15.61 | 0.33 | requires commercialization/reimbursement/royalty bridge |
| P3_C23_counterexample_guard | 2 | direct value-capture approvals only | 52.36/-9.56 | 67.81/-9.56 | 0.00 | best risk but may miss public-procurement vaccine rows |


Interpretation: P0 accepts too many approval headlines as if a regulator's stamp automatically becomes revenue. P3 is safest but too narrow. The proposed C23 canonical profile should sit between them: approve Stage2-Actionable when regulatory approval has a clear commercial rail, and downgrade approval-only or indirect-royalty rows to Stage2-Watch/4B until value capture is measured.

## 9. Shadow rule candidate

```yaml
shadow_rule_candidate:
  id: C23_APPROVAL_TO_COMMERCIALIZATION_VALUE_CAPTURE_GATE_V1
  large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
  canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  production_scoring_changed: false
  do_not_propose_new_weight_delta: false
  rule_intent: >
    Separate regulatory approval from listed-company value capture. Stage2-Actionable requires the approval to connect to launch, reimbursement, formulary, milestone/royalty, or procurement conversion. Approval-only, indirect-royalty, or demand-decay rows stay at Stage2-Watch or Stage4B.
  positive_gate:
    require_regulatory_event:
      - FDA_or_EQ_approval
      - WHO_prequalification
      - overseas_marketing_authorization
    require_any_value_capture_bridge:
      - named_global_partner_with_milestone_or_royalty
      - commercial_launch_date_and_distribution_route
      - payer_or_formulary_access_signal
      - public_procurement_or_tender_eligibility
      - quantified_revenue_or_revision_bridge
  downgrade_gate:
    if_any:
      - approval_without_payer_or_reimbursement_path
      - partner_derivative_without_quantified_royalty
      - vaccine_or_product_market_demand_decay
      - launch_available_but_prescription_or_sales_ramp_unproven
      - approval_event_after_large_positioning_spike
    then: Stage2-Watch_or_Stage4B_Watch
  hard_4c_gate:
    require_non_price_confirmation:
      - demand_collapse
      - failed_commercial_launch
      - reimbursement_block
      - regulatory_withdrawal_or_safety_label_break
```

## 10. Existing calibrated axis audit

```text
existing_axis_tested:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence: SK Bioscience and Oscotec need non-price demand/value-capture evidence, not just a local peak.
  - price_only_blowoff_blocks_positive_stage: approval-derived spikes with weak commercialization bridges should not become Stage3.
existing_axis_weakened:
  - hard_4c_thesis_break_routes_to_4c_should_not_fire_on_launch_slowdown_language_alone: Celltrion/HK inno.N show Watch is better before confirmed sales failure.
existing_axis_kept:
  - Stage3-Green remains strict. No row justifies loosening Green without royalty/revenue confirmation.
new_axis_proposed:
  - c23_approval_to_commercialization_value_capture_gate
```

## 11. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: approval_only_false_positive|indirect_royalty_high_mae|payer_formulary_ramp_gap|vaccine_demand_decay_4b|approval_to_value_capture_too_late
new_axis_proposed: c23_approval_to_commercialization_value_capture_gate
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_on_launch_slowdown_language_alone
existing_axis_kept: stage3_green_strictness|stage3_yellow_threshold_75
sector_specific_rule_candidate: L7_BIO_APPROVAL_COMMERCIALIZATION_VALUE_CAPTURE_GATE_V1
canonical_archetype_rule_candidate: C23_APPROVAL_TO_COMMERCIALIZATION_VALUE_CAPTURE_GATE_V1
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session. Later coding-agent task only.

Goal: ingest this standalone MD as one v12 research artifact and evaluate whether C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION should receive a canonical shadow patch named C23_APPROVAL_TO_COMMERCIALIZATION_VALUE_CAPTURE_GATE_V1.

Inputs:
- this MD file
- data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl
- reports/e2r_calibration/v12/coverage_matrix.md
- active profile e2r_2_2 rolling calibration artifacts

Required checks:
1. Parse all row_type=trigger rows and verify the six mandatory fields MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
2. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
3. Confirm no entry~D180 corporate-action candidate overlap in stock-web symbol profiles.
4. Run C23-only promotion simulation:
   - base: current e2r_2_2 rolling calibrated profile
   - candidate: require value_capture_bridge for Stage2-Actionable
   - guard: approval-only or indirect-royalty rows remain Stage2-Watch unless commercialization_score or royalty_or_reimbursement_score crosses threshold.
5. Do not loosen Stage3-Green. Do not create global rule unless the same approval-to-value-capture failure repeats across at least three large sectors.
```

## 13. Next research state

```text
completed_round = R7
completed_loop = 155
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|C19_BRAND_RETAIL_INVENTORY_MARGIN|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|C13_BATTERY_JV_UTILIZATION_AMPC_IRA
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
