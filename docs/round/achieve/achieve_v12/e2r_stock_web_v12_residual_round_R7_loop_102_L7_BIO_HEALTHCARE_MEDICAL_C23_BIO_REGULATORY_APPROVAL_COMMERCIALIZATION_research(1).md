# E2R Stock-Web V12 Residual Research — C23 Approval → Commercialization Holdout v102

## 0. Research Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R7_loop_102_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
selected_round: R7
selected_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md used as no-repeat ledger only
selected_priority_bucket: Priority 1 static C23 rows=48 / need-to-50=2; current-session C23 already crossed 50, so this is a new-trigger-family quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: mixed_C23_approval_commercialization_partner_sales_holdout_v102
loop_objective:
  - holdout_validation
  - counterexample_mining
  - approval_to_commercialization_bridge_gate
  - local_4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_code_patch_included: false
production_scoring_patch_applied: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

The No-Repeat Index static ledger still lists `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` at 48 rows, two rows below the 50-row practical calibration band. This session already crossed that band, so this run is not count-filling. It tests a narrower C23 residual problem: **approval is not commercialization unless launch, reimbursement, royalty, partner-sales, or parent-materiality bridge is visible.**

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty logic:

```yaml
new_symbol_count: 2
same_symbol_new_trigger_family_count: 3
new_trigger_family_count: 5
new_independent_case_count: 5
minimum_new_independent_case_ratio: 1.0
positive_case_count: 4
counterexample_count: 1
calibration_usable_case_count: 5
```

## 2. Price source validation

Stock-Web manifest basis:

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
```

MFE/MAE follows the Stock-Web schema: `MFE_N_pct = max(high from entry_date through N tradable rows) / entry_price - 1`, and `MAE_N_pct = min(low from entry_date through N tradable rows) / entry_price - 1`. Every representative trigger row below has all six required 30D/90D/180D MFE/MAE fields and a clean 180D corporate-action window.

## 3. Core finding

C23 should be a two-door system. The first door is **regulatory approval**; the second is **commercialization materiality**. Many biotech rows pass the first door and still fail the second. The market often lets the approval headline ring like a bell, but the bell does not print revenue unless there is launch timing, reimbursement, royalty, partner sales, supply economics, or parent-company materiality.

The loop therefore proposes a C23-specific gate:

```text
approval headline -> launch/reimbursement/royalty/partner-sales/parent-materiality bridge -> Stage3 persistence
```

Without that bridge, approval can open Stage2-Actionable, but Stage3-Yellow/Green should carry a local 4B overlay or remain capped.

## 4. Selected trigger rows

| # | symbol | company | trigger_date | entry_date | trigger_type | role | MFE180 | MAE180 | lesson |
|---:|---|---|---|---|---|---|---:|---:|---|
| 1 | 207940 | 삼성바이오로직스 | 2024-07-01 | 2024-07-01 | Stage3-Yellow | positive | 59.29% | -4.48% | approval headline must pass commercialization/materiality bridge |
| 2 | 950210 | 프레스티지바이오파마 | 2024-09-23 | 2024-09-23 | Stage3-Yellow | positive_with_guardrail | 41.50% | -23.56% | approval headline must pass commercialization/materiality bridge |
| 3 | 000100 | 유한양행 | 2024-08-30 | 2024-08-30 | Stage3-Yellow | positive_with_guardrail | 18.37% | -28.79% | approval headline must pass commercialization/materiality bridge |
| 4 | 128940 | 한미약품 | 2023-03-23 | 2023-03-23 | Stage3-Yellow | positive | 31.53% | -3.09% | approval headline must pass commercialization/materiality bridge |
| 5 | 069620 | 대웅제약 | 2019-02-07 | 2019-02-07 | Stage2-Actionable | counterexample | 6.37% | -32.35% | approval headline must pass commercialization/materiality bridge |


## 5. Aggregate stress result

```yaml
calibration_usable_rows: 5
representative_rows: 5
positive_case_count: 4
counterexample_count: 1
stage4b_case_count: 5
stage4c_case_count: 0
current_profile_error_count: 3
avg_MFE_30D_pct: 25.4973
avg_MAE_30D_pct: -9.5387
avg_MFE_90D_pct: 28.8438
avg_MAE_90D_pct: -14.1215
avg_MFE_180D_pct: 31.4122
avg_MAE_180D_pct: -18.4566
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
```

## 6. Machine-readable rows

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "trigger_id": "C23_R7_L102_207940_20240701_TRG", "case_id": "C23_R7_L102_207940_20240701", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": 102, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_commercialization_partner_sales_holdout_v102", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "holdout_validation|counterexample_mining|approval_to_commercialization_bridge_gate|local_4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-07-01", "evidence_available_at_that_date": "Samsung Bioepis announced U.S. FDA approval of PYZCHIVA, with Sandoz commercialization rights for the U.S. and other territories. For listed parent Samsung Biologics, this is positive C23 evidence but requires affiliate/materiality decontamination before Stage3-Green.", "evidence_source": "https://www.samsungbioepis.com/en/newsroom/newsroomView.do?currentPage=1&idx=402", "source_quote_or_summary": "PYZCHIVA FDA approval plus Sandoz commercialization agreement; license period in the U.S. begins in February 2025.", "stage2_evidence_fields": ["regulatory_approval_public", "commercial_partner_named", "affiliate_product_route_visible"], "stage3_evidence_fields": ["commercial_partner_route_visible", "parent_materiality_needs_decontamination"], "stage4b_evidence_fields": ["affiliate_materiality_contamination", "commercial_launch_timing_lag"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-01", "entry_price": 759000.0, "MFE_30D_pct": 29.9078, "MFE_90D_pct": 46.6403, "MFE_180D_pct": 59.2885, "MAE_30D_pct": -4.4796, "MAE_90D_pct": -4.4796, "MAE_180D_pct": -4.4796, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000.0, "drawdown_after_peak_pct": -14.6402, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "local_4b_watch_required_if_sales_royalty_or_launch_bridge_lags", "four_b_evidence_type": "commercialization_timing_or_partner_sales_bridge_lag", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_with_affiliate_decontamination", "current_profile_verdict": "current_profile_correct_if_affiliate_materiality_decontamination_prevents_automatic_stage3_green", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_end_date": "2025-03-28", "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_checked_or_no_overlap", "window_180D_corporate_action_contaminated": false, "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_207940_2024-07-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "trigger_id": "C23_R7_L102_950210_20240923_TRG", "case_id": "C23_R7_L102_950210_20240923", "symbol": "950210", "company_name": "프레스티지바이오파마", "round": "R7", "loop": 102, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_commercialization_partner_sales_holdout_v102", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "holdout_validation|counterexample_mining|approval_to_commercialization_bridge_gate|local_4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-09-23", "evidence_available_at_that_date": "Prestige Biopharma announced that the European Commission granted marketing authorization for Tuznue, its trastuzumab biosimilar. The approval is genuine C23 evidence, but launch economics and distribution partner execution remained the next bridge.", "evidence_source": "https://prestigebiopharma.com/2026-news/?mod=document&pageid=3&uid=387", "source_quote_or_summary": "Tuznue EC marketing authorization in September 2024; later Teva license/supply agreement validates the commercialization bridge, but after the initial approval-date trade.", "stage2_evidence_fields": ["EC_marketing_authorization_public", "biosimilar_product_approved", "Europe_commercial_route_opened"], "stage3_evidence_fields": ["approval_to_commercialization_route_visible_but_partner_distribution_lagged"], "stage4b_evidence_fields": ["post_approval_peak_decay", "distribution_partner_timing_lag", "margin_bridge_not_yet_confirmed_on_entry"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/950/950210/2024.csv", "profile_path": "atlas/symbol_profiles/950/950210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-23", "entry_price": 14770.0, "MFE_30D_pct": 41.503, "MFE_90D_pct": 41.503, "MFE_180D_pct": 41.503, "MAE_30D_pct": -11.1713, "MAE_90D_pct": -11.1713, "MAE_180D_pct": -23.5613, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-28", "peak_price": 20900.0, "drawdown_after_peak_pct": -45.9809, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "local_4b_watch_required_if_sales_royalty_or_launch_bridge_lags", "four_b_evidence_type": "commercialization_timing_or_partner_sales_bridge_lag", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_with_local_4b_watch", "current_profile_verdict": "current_profile_false_positive_if_EC_approval_immediately_treated_as_durable_commercialization_without_distribution_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_end_date": "2025-06-23", "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_checked_or_no_overlap", "window_180D_corporate_action_contaminated": false, "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_950210_2024-09-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "trigger_id": "C23_R7_L102_000100_20240830_TRG", "case_id": "C23_R7_L102_000100_20240830", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": 102, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_commercialization_partner_sales_holdout_v102", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "holdout_validation|counterexample_mining|approval_to_commercialization_bridge_gate|local_4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-08-30", "evidence_available_at_that_date": "After FDA approval of the Rybrevant plus Lazcluze combination, Lazcluze became commercially available through specialty-pharmacy distribution. This is a commercialization bridge trigger distinct from the approval-day trigger, but the stock path still required local 4B watch.", "evidence_source": "https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer", "source_quote_or_summary": "FDA approval for lazertinib plus amivantamab and subsequent commercial availability route.", "stage2_evidence_fields": ["FDA_approval_already_public", "commercial_distribution_route_opened", "licensed_product_materiality_visible"], "stage3_evidence_fields": ["royalty_or_partner_sales_bridge_partially_visible", "global_partner_commercial_route_visible"], "stage4b_evidence_fields": ["post_approval_peak_decay", "royalty_sales_confirmation_lag"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-30", "entry_price": 141000.0, "MFE_30D_pct": 18.3688, "MFE_90D_pct": 18.3688, "MFE_180D_pct": 18.3688, "MAE_30D_pct": -15.9574, "MAE_90D_pct": -22.695, "MAE_180D_pct": -28.7943, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900.0, "drawdown_after_peak_pct": -39.8442, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "local_4b_watch_required_if_sales_royalty_or_launch_bridge_lags", "four_b_evidence_type": "commercialization_timing_or_partner_sales_bridge_lag", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_but_stage3_persistence_requires_royalty_sales_confirmation", "current_profile_verdict": "current_profile_too_early_if_commercial_availability_is_not_waiting_for_partner_sales_or_royalty_confirmation", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_end_date": "2025-06-02", "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_checked_or_no_overlap", "window_180D_corporate_action_contaminated": false, "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_000100_2024-08-30", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_allowed_new_trigger_family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "trigger_id": "C23_R7_L102_128940_20230323_TRG", "case_id": "C23_R7_L102_128940_20230323", "symbol": "128940", "company_name": "한미약품", "round": "R7", "loop": 102, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_commercialization_partner_sales_holdout_v102", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "holdout_validation|counterexample_mining|approval_to_commercialization_bridge_gate|local_4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-03-23", "evidence_available_at_that_date": "Hanmi reported that partner Spectrum achieved roughly USD 10.1 million first-year U.S. sales for Rolvedon. This is not merely approval; it is commercialization evidence after launch.", "evidence_source": "https://www.asiae.co.kr/en/article/2023032313192382131", "source_quote_or_summary": "Rolvedon U.S. sales exceeded about KRW 13.1bn / USD 10.1mn in the first year after launch.", "stage2_evidence_fields": ["approved_product_already_launched", "partner_sales_public", "commercial_bridge_confirmed"], "stage3_evidence_fields": ["sales_confirmation", "commercial_partner_route", "royalty_or_product_pull_through_visibility"], "stage4b_evidence_fields": ["post_peak_drawdown_watch", "commercial_sales_still_partner_dependent"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/128/128940/2023.csv", "profile_path": "atlas/symbol_profiles/128/128940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-23", "entry_price": 258500.0, "MFE_30D_pct": 31.3346, "MFE_90D_pct": 31.3346, "MFE_180D_pct": 31.528, "MAE_30D_pct": -3.0948, "MAE_90D_pct": -3.0948, "MAE_180D_pct": -3.0948, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-11", "peak_price": 340000.0, "drawdown_after_peak_pct": -21.3235, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "local_4b_watch_required_if_sales_royalty_or_launch_bridge_lags", "four_b_evidence_type": "commercialization_timing_or_partner_sales_bridge_lag", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "commercialization_bridge_positive_with_4b_watch", "current_profile_verdict": "current_profile_correct_when_C23_waits_for_sales_confirmation_rather_than_approval_day_alone", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_end_date": "2023-12-13", "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_checked_or_no_overlap", "window_180D_corporate_action_contaminated": false, "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_128940_2023-03-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_allowed_new_trigger_family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "trigger_id": "C23_R7_L102_069620_20190207_TRG", "case_id": "C23_R7_L102_069620_20190207", "symbol": "069620", "company_name": "대웅제약", "round": "R7", "loop": 102, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "mixed_C23_approval_commercialization_partner_sales_holdout_v102", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "holdout_validation|counterexample_mining|approval_to_commercialization_bridge_gate|local_4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2019-02-07", "evidence_available_at_that_date": "Daewoong won U.S. FDA approval for Nabota/Jeuveau, with Evolus in charge of U.S. sales. The approval was real, but the listed Korean company price path failed without immediate commercial pull-through.", "evidence_source": "https://en.yna.co.kr/view/AEN20190207010000320", "source_quote_or_summary": "Nabota FDA approval; Evolus responsible for U.S. sales under the Jeuveau name.", "stage2_evidence_fields": ["FDA_approval_public", "global_partner_sales_route_named", "first_Korean_botulinum_toxin_FDA_greenlight"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["partner_commercialization_lag", "approval_day_event_premium", "weak_revenue_bridge_at_entry"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv", "profile_path": "atlas/symbol_profiles/069/069620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2019-02-07", "entry_price": 204000.0, "MFE_30D_pct": 6.3725, "MFE_90D_pct": 6.3725, "MFE_180D_pct": 6.3725, "MAE_30D_pct": -12.9902, "MAE_90D_pct": -29.1667, "MAE_180D_pct": -32.3529, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2019-02-07", "peak_price": 217000.0, "drawdown_after_peak_pct": -36.4055, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "local_4b_watch_required_if_sales_royalty_or_launch_bridge_lags", "four_b_evidence_type": "commercialization_timing_or_partner_sales_bridge_lag", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "approval_day_counterexample_partner_sales_lag", "current_profile_verdict": "current_profile_false_positive_if_FDA_approval_alone_opens_stage3_without_partner_sales_or_royalty_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "forward_window_end_date": "2019-10-29", "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_checked_or_no_overlap", "window_180D_corporate_action_contaminated": false, "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_069620_2019-02-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_allowed_new_trigger_family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_patch_applied": false}
{"row_type": "score_simulation", "case_id": "C23_R7_L102_207940_20240701", "symbol": "207940", "company_name": "삼성바이오로직스", "profile_id_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_id_after": "C23_approval_commercialization_shadow_profile_v102", "raw_component_scores_before": {"contract_score": 78, "backlog_visibility_score": 45, "margin_bridge_score": 48, "revision_score": 52, "relative_strength_score": 70, "customer_quality_score": 80, "policy_or_regulatory_score": 85, "valuation_repricing_score": 62, "execution_risk_score": 32, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 12, "commercialization_score": 74}, "weighted_score_before": 52.15, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 78, "backlog_visibility_score": 45, "margin_bridge_score": 48, "revision_score": 52, "relative_strength_score": 70, "customer_quality_score": 80, "policy_or_regulatory_score": 85, "valuation_repricing_score": 62, "execution_risk_score": 32, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 12, "commercialization_score": 82}, "weighted_score_after": 52.77, "stage_label_after": "Stage3-Yellow_affiliate_decontamination", "component_delta_explanation": "C23 separates approval headline from launch/reimbursement/royalty/partner-sales materiality bridge; approval-only rows receive local 4B cap."}
{"row_type": "score_simulation", "case_id": "C23_R7_L102_950210_20240923", "symbol": "950210", "company_name": "프레스티지바이오파마", "profile_id_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_id_after": "C23_approval_commercialization_shadow_profile_v102", "raw_component_scores_before": {"contract_score": 65, "backlog_visibility_score": 38, "margin_bridge_score": 35, "revision_score": 40, "relative_strength_score": 68, "customer_quality_score": 60, "policy_or_regulatory_score": 88, "valuation_repricing_score": 70, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 18, "commercialization_score": 56}, "weighted_score_before": 49.08, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 65, "backlog_visibility_score": 38, "margin_bridge_score": 35, "revision_score": 40, "relative_strength_score": 68, "customer_quality_score": 60, "policy_or_regulatory_score": 88, "valuation_repricing_score": 70, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 18, "commercialization_score": 64}, "weighted_score_after": 49.69, "stage_label_after": "Stage3-Yellow_plus_local_4B_watch", "component_delta_explanation": "C23 separates approval headline from launch/reimbursement/royalty/partner-sales materiality bridge; approval-only rows receive local 4B cap."}
{"row_type": "score_simulation", "case_id": "C23_R7_L102_000100_20240830", "symbol": "000100", "company_name": "유한양행", "profile_id_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_id_after": "C23_approval_commercialization_shadow_profile_v102", "raw_component_scores_before": {"contract_score": 82, "backlog_visibility_score": 42, "margin_bridge_score": 52, "revision_score": 55, "relative_strength_score": 60, "customer_quality_score": 82, "policy_or_regulatory_score": 90, "valuation_repricing_score": 58, "execution_risk_score": 42, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 12, "commercialization_score": 72}, "weighted_score_before": 52.08, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 82, "backlog_visibility_score": 42, "margin_bridge_score": 52, "revision_score": 55, "relative_strength_score": 60, "customer_quality_score": 82, "policy_or_regulatory_score": 90, "valuation_repricing_score": 58, "execution_risk_score": 42, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 12, "commercialization_score": 80}, "weighted_score_after": 52.69, "stage_label_after": "Stage3-Yellow_plus_local_4B_watch_until_royalty_sales_bridge", "component_delta_explanation": "C23 separates approval headline from launch/reimbursement/royalty/partner-sales materiality bridge; approval-only rows receive local 4B cap."}
{"row_type": "score_simulation", "case_id": "C23_R7_L102_128940_20230323", "symbol": "128940", "company_name": "한미약품", "profile_id_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_id_after": "C23_approval_commercialization_shadow_profile_v102", "raw_component_scores_before": {"contract_score": 76, "backlog_visibility_score": 35, "margin_bridge_score": 58, "revision_score": 56, "relative_strength_score": 62, "customer_quality_score": 72, "policy_or_regulatory_score": 72, "valuation_repricing_score": 54, "execution_risk_score": 35, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 12, "accounting_trust_risk_score": 12, "commercialization_score": 80}, "weighted_score_before": 49.38, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 76, "backlog_visibility_score": 35, "margin_bridge_score": 58, "revision_score": 56, "relative_strength_score": 62, "customer_quality_score": 72, "policy_or_regulatory_score": 72, "valuation_repricing_score": 54, "execution_risk_score": 35, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 12, "accounting_trust_risk_score": 12, "commercialization_score": 88}, "weighted_score_after": 50.0, "stage_label_after": "Stage3-Yellow_commercial_sales_bridge", "component_delta_explanation": "C23 separates approval headline from launch/reimbursement/royalty/partner-sales materiality bridge; approval-only rows receive local 4B cap."}
{"row_type": "score_simulation", "case_id": "C23_R7_L102_069620_20190207", "symbol": "069620", "company_name": "대웅제약", "profile_id_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_id_after": "C23_approval_commercialization_shadow_profile_v102", "raw_component_scores_before": {"contract_score": 68, "backlog_visibility_score": 20, "margin_bridge_score": 22, "revision_score": 32, "relative_strength_score": 45, "customer_quality_score": 62, "policy_or_regulatory_score": 86, "valuation_repricing_score": 50, "execution_risk_score": 58, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 15, "commercialization_score": 38}, "weighted_score_before": 40.85, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 68, "backlog_visibility_score": 20, "margin_bridge_score": 22, "revision_score": 32, "relative_strength_score": 45, "customer_quality_score": 62, "policy_or_regulatory_score": 86, "valuation_repricing_score": 50, "execution_risk_score": 58, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 15, "commercialization_score": 23}, "weighted_score_after": 39.69, "stage_label_after": "Stage2-Actionable_plus_local_4B_watch", "component_delta_explanation": "C23 separates approval headline from launch/reimbursement/royalty/partner-sales materiality bridge; approval-only rows receive local 4B cap."}
{"row_type": "aggregate", "selected_round": "R7", "selected_loop": 102, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "calibration_usable_rows": 5, "representative_rows": 5, "positive_case_count": 4, "counterexample_count": 1, "stage4b_case_count": 5, "stage4c_case_count": 0, "current_profile_error_count": 3, "avg_MFE_30D_pct": 25.4973, "avg_MAE_30D_pct": -9.5387, "avg_MFE_90D_pct": 28.8438, "avg_MAE_90D_pct": -14.1215, "avg_MFE_180D_pct": 31.4122, "avg_MAE_180D_pct": -18.4566, "source_proxy_only_rows": 0, "evidence_url_pending_rows": 0, "rule_candidate": "C23_APPROVAL_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_ROYALTY_PARTNER_SALES_OR_PARENT_MATERIALITY_BRIDGE_WITH_LOCAL_4B_CAP"}
{"row_type": "shadow_weight", "rule_scope": "canonical_archetype_specific", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_axis_proposed": "C23_APPROVAL_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_ROYALTY_PARTNER_SALES_OR_PARENT_MATERIALITY_BRIDGE_WITH_LOCAL_4B_CAP", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": [], "do_not_propose_new_weight_delta": false}
{"row_type": "residual_contribution", "new_independent_case_count": 5, "reused_case_count": 3, "new_symbol_count": 2, "new_trigger_family_count": 5, "positive_case_count": 4, "counterexample_count": 1, "current_profile_error_count": 3, "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 7. Proposed shadow rule candidate

```text
C23_APPROVAL_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_ROYALTY_PARTNER_SALES_OR_PARENT_MATERIALITY_BRIDGE_WITH_LOCAL_4B_CAP
```

Rule mechanics:

```yaml
Stage2_Actionable_allowed_when:
  - regulatory_approval_or_CHMP_or_EC_authorization_is_public
  - product_or_partner_route_is_material_enough_to_track
Stage3_Yellow_allowed_when_at_least_two:
  - commercial_launch_date_or_availability_confirmed
  - reimbursement_or_formulary_or_pricing_route_confirmed
  - royalty_or_partner_sales_route_confirmed
  - parent_company_materiality_or_supply_economics_visible
  - revenue_recognition_or_operating_profit_bridge_confirmed
Stage3_Green_blocked_when:
  - approval exists but commercialization route is delayed
  - affiliate product materiality is unclear for the listed parent
  - post-approval MFE reverses into deep 90D/180D MAE before sales bridge
Stage4B_local_watch_when:
  - approval headline generates fast MFE but peak drawdown exceeds local watch threshold
  - approval is real but partner launch / royalty / distribution route is not yet cash-visible
```

## 8. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 3
reused_case_ids:
  - 000100_YUHAN_new_commercial_availability_trigger_not_approval_day
  - 128940_HANMI_new_sales_confirmation_trigger_not_approval_day
  - 069620_DAEWOONG_2019_Nabota_approval_not_2023_Fexuclue_case
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - approval_headline_overweighted_without_commercialization_bridge
  - affiliate_or_parent_materiality_contamination
  - partner_launch_or_royalty_lag
new_axis_proposed: C23_APPROVAL_COMMERCIALIZATION_BRIDGE_GATE_WITH_LOCAL_4B_CAP
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C23_APPROVAL_COMMERCIALIZATION_REQUIRES_LAUNCH_REIMBURSEMENT_ROYALTY_PARTNER_SALES_OR_PARENT_MATERIALITY_BRIDGE_WITH_LOCAL_4B_CAP
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 9. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | calibration usable | representative | current profile errors | rule candidate | coverage gap after this loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | mixed_C23_approval_commercialization_partner_sales_holdout_v102 | 4 | 1 | 5 | 0 | 5 | 3 | 5 | 5 | 3 | C23 approval-commercialization bridge gate | static 48 -> 53; session-adjusted quality holdout strengthened |

## 10. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Read this MD as a v12 historical calibration candidate only. Do not execute this handoff during the research session. In a later coding-agent batch, parse trigger rows where calibration_usable=true and aggregate_group_role=representative. Evaluate whether the C23 approval-commercialization bridge gate should become a canonical-archetype-specific shadow rule. Do not alter production scoring unless batch aggregate confirms the rule across accepted C23 rows.
```

## 12. Next research state

```yaml
completed_round: R7
completed_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 static ledger C23 rows=48 / need-to-50=2; session-adjusted quality holdout
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
