# E2R Stock-Web v12 Residual Research — R5 C18 Consumer Export Channel Reorder / Apparel OEM Reorder Pass
```text
selected_round = R5
selected_loop = 177
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = apparel_oem_restocking_customer_reorder_margin_bridge_leaf_set
loop_objective = counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|holdout_validation
production_scoring_changed = false
shadow_weight_only = true
```
## 1. Selection Rationale

This loop returns to C18 only after the session has generated P0/P1 clearing passes and all four R13 guardrail scopes. The GitHub No-Repeat Index currently lists C18 as a Priority 2 quality-repair scope, not as a raw row-count shortage. Therefore the goal is not to add another food/beauty export narrative. The goal is to isolate an under-specified C18 sub-leaf: apparel OEM export reorder, where customer inventory normalization and buyer restocking can look like a rerating bridge, but only becomes calibration-useful when it turns into visible orders, sales, margin, or working-capital conversion.

The session already produced a C18 loop at 121 and later C20/C19 consumer passes. This file avoids the prior food/beauty-heavy set and uses apparel OEM / global brand reorder cases: 화승엔터프라이즈, 영원무역, TP, 한세실업, and 호전실업.
## 2. Stock-Web Price Atlas Confirmation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
required_forward_window = 180 trading days
entry_price_basis = entry_date close c
```

Profile review note: the selected 2024~2025 entry windows for 111770, 007980, 111110, and 105630 have no detected 180D corporate-action overlap in the downloaded stock-web rows. 241590 has old 2018 corporate-action candidates, outside the 2024~2025 forward windows used here.
## 3. C18 Thesis Under Test

C18 should not treat every “export recovery” sentence as a clean Stage2. Apparel OEM is a conveyor belt: buyer inventory normalization must pull new orders; new orders must become shipment/revenue; revenue must survive fixed-cost and FX/margin conversion. If the belt stops at “recovery expected,” the Stage2 signal is still soft.

Shadow rule hypothesis:

```text
C18_APPAREL_OEM_REORDER_MARGIN_BRIDGE_GATE_V1
IF export-channel or global-brand reorder evidence is present
AND at least one hard buyer/order/shipment/revenue bridge is visible
AND margin or working-capital conversion is not deteriorating
THEN allow Stage2-Actionable or Stage3-Yellow watch.
ELSE keep Stage2-Watch / false-positive guard even if low valuation or one-quarter revenue recovery appears.
```
## 4. Case Summary Table

|#|ticker|name|trigger|entry|MFE30/MAE30|MFE90/MAE90|MFE180/MAE180|label|C18 use|
|---:|---|---|---|---|---:|---:|---:|---|---|
|1|241590|화승엔터프라이즈|Stage2-Actionable / Adidas inventory normalization / technical restocking preview|2024-03-20 @ 7450.0|28.19/-6.04|36.38/-6.04|36.38/-6.98|positive|early_restocking_positive|
|2|241590|화승엔터프라이즈|Stage2-Actionable / Adidas sales growth recovery but single-customer concentration still visible|2024-10-08 @ 8640.0|14.0/-5.21|38.89/-7.18|38.89/-19.21|positive_with_4B_exit_guard|confirmed_recovery_but_customer_concentration_exit_guard|
|3|111770|영원무역|Stage2 / OEM growth offset by SCOTT drag; 3Q24 preview looked weak at consolidated level|2024-10-15 @ 43650.0|2.98/-13.86|8.59/-13.86|50.74/-13.86|delayed_positive|oem_reorder_signal_hidden_by_subsidiary_drag|
|4|111770|영원무역|Stage2-Actionable / OEM dollar-growth surprise; SCOTT inventory burden easing; 2025 profit growth turn|2025-03-04 @ 46850.0|13.98/-10.78|40.45/-10.78|102.77/-10.78|positive|oem_order_growth_inventory_relief_positive|
|5|007980|TP|Stage2-Actionable / Q2 order increase and cost discipline headline but no durable rerating path|2024-08-14 @ 1470.0|1.36/-14.01|4.9/-14.01|5.37/-15.1|counterexample|reported_order_increase_without_rerating_or_reorder_durability|
|6|105630|한세실업|Stage2-Actionable / 2025 order recovery expected but weak and delayed; valuation trap despite low PER|2025-02-25 @ 12460.0|2.09/-22.39|2.09/-22.39|5.22/-27.37|counterexample|weak_order_recovery_forecast_counterexample|
|7|111110|호전실업|Stage2 / Arc’teryx/Lululemon premium OEM new-customer order bridge but still small-cap execution watch|2025-04-21 @ 8120.0|12.44/-3.33|13.18/-16.75|13.18/-16.75|positive_watch|new_customer_reorder_bridge_but_low_alpha_watch|

## 5. Evidence URL / Source Table

|ticker|name|evidence source|URL|
|---|---|---|---|
|241590|화승엔터프라이즈|Meritz Securities, 2024-04-17 1Q24E Preview: Adidas inventory burden easing, technical restocking, HSE inventory down, 2024 turnaround expected|https://home.imeritz.com/include/resource/research/WorkFlow/20240408105225297K_02.pdf|
|241590|화승엔터프라이즈|The Bell, 2024-10-08/15: Adidas sales growth helped rapid performance recovery; dependence on Adidas and profitability still remain tasks|https://m.thebell.co.kr/m/newsview.asp?newskey=202410071721268360108213&svccode=|
|111770|영원무역|SK Securities apparel report, 2024-10-15: OEM sales expected to grow but SCOTT decline drags consolidated revenue/OP|https://www.sks.co.kr/data1/research/qna_file/20241013153402123_0_ko.pdf|
|111770|영원무역|Daishin Securities, 2025-03-04: OEM dollar sales +20%, SCOTT large loss but inventory burden eased, 2025 profit growth expected|https://money2.daishin.com/PDF/Out/intranet_data/Product/ResearchCenter/Report/2025/03/52859_250304_Youngone.F.pdf|
|007980|TP|Daum/TP, 2024-08-14: Q2 sales +9%, OP +35%, early-year order increase and cost cutting supported results|https://v.daum.net/v/yXwvdhYcSB|
|105630|한세실업|BusinessPost/Hana Securities, 2025-02-25 and MK PDF: order recovery not strong, recovery depends on H2 consumer/holiday orders; target lowered|https://www.businesspost.co.kr/BP?command=article_view&num=384721|
|111110|호전실업|Newsprime, 2025-04-21: Arc’teryx OEM started in 2024; already more than $15m orders, annual target $50m; premium functional apparel margin route|https://m.newsprime.co.kr/section_view.html?no=684589|

## 6. Residual Findings

### 6.1 Restocking must pass through order and margin gates

화승엔터프라이즈 shows the cleanest C18 mechanism. The early restocking preview already had customer inventory normalization and operating leverage language, and the later recovery headline still produced positive forward MFE. But it also shows why C18 needs a concentration/exit overlay: a single global customer can pull the whole belt forward, then cap rerating if the buyer growth or vendor mix stalls.

### 6.2 Consolidated drag can hide the export-channel reorder signal

영원무역 is the opposite lesson. In October 2024, consolidated SCOTT drag made the signal look dull at 90D, but the OEM channel later became a strong 180D positive. The March 2025 trigger confirms that when OEM dollar growth and inventory relief are both visible, C18 should not be blocked by a stale consolidated drag penalty.

### 6.3 One-quarter recovery and low valuation are not enough

TP and 한세실업 are the counterweights. TP had Q2 order-increase language and reported profit improvement, but the stock-web path stayed low-alpha with shallow MFE. 한세실업 had low PER and H2 order recovery language, yet the actual 30/90/180D path showed negative MAE dominance. C18 should require repeat order visibility, not just cheap valuation plus recovery vocabulary.

### 6.4 New-customer order bridge can stay Stage2-Watch before scale repeats

호전실업 has a better order-quality story because the new premium customer bridge is specific, but the forward price path remained mild. The correct state is not hard rejection; it is Stage2-Watch until repeat order scale and margin conversion prove the customer bridge can move the consolidated P/L.

## 7. Proposed Shadow Rule Candidate

```text
proposal_id = C18_APPAREL_OEM_REORDER_MARGIN_BRIDGE_GATE_V1
scope = C18_CONSUMER_EXPORT_CHANNEL_REORDER
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
production_scoring_changed = false
shadow_weight_only = true
```

Rule candidate:

```text
IF C18 evidence is apparel OEM / global-brand export reorder
THEN require at least two of:
  1. named buyer / specific brand reorder or customer inventory normalization,
  2. order/shipment/revenue timing bridge,
  3. margin or fixed-cost leverage bridge,
  4. working-capital/inventory conversion not deteriorating.

IF evidence is only low valuation, H2 recovery expectation, or one-quarter order effect
THEN cap at Stage2-Watch and mark current_profile_false_positive risk.

IF consolidated drag hides a confirmed OEM order recovery
THEN allow staged Stage2 even before the consolidated segment fully turns.
```

## 8. Current Calibrated Profile Stress Test

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C18_apparel_oem_reorder_bridge_gate
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

|question|answer|
|---|---|
|Stage2 bonus too high?|Too high for low-PER or single-quarter recovery language without repeat order bridge.|
|Stage2 too late?|Too late when consolidated drag masks confirmed OEM dollar growth and inventory relief.|
|Yellow 75 too loose/tight?|Mostly correct, but C18 needs buyer/order/margin bridge before Yellow.|
|Green 87/revision 55 too loose/tight?|Correctly strict. None of the apparel OEM cases should skip to Green without repeated revenue and margin confirmation.|
|price-only blowoff guard|Strengthened for late recovery headlines after the reorder cycle is already priced.|
|4B non-price requirement|Use customer concentration, weak buyer growth, or working-capital deterioration as non-price 4B watch evidence.|

## 9. Machine-readable JSONL

```jsonl
{"row_type": "case", "case_id": "C18_L177_01_241590_2024-03-20", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "241590", "company_name": "화승엔터프라이즈", "trigger_date": "2024-03-20", "event_summary": "Adidas inventory normalization / technical restocking preview", "evidence_url": "https://home.imeritz.com/include/resource/research/WorkFlow/20240408105225297K_02.pdf", "evidence_family": "apparel_oem_reorder_inventory_normalization_margin_bridge", "case_result_label": "positive", "calibration_usable": true, "novelty_check": "new_trigger_family_in_session_or_new_symbol_for_C18_apparel_oem_leaf"}
{"row_type": "trigger", "case_id": "C18_L177_01_241590_2024-03-20", "trigger_id": "TR_C18_L177_01_241590_Stage2Actionable_2024-03-20", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "241590", "company_name": "화승엔터프라이즈", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 7450.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 28.19, "MAE_30D_pct": -6.04, "MFE_90D_pct": 36.38, "MAE_90D_pct": -6.04, "MFE_180D_pct": 36.38, "MAE_180D_pct": -6.98, "calibration_usable": true, "corporate_action_contamination_180D": false, "score_return_alignment_label": "current_profile_too_conservative_if_restocking_bridge_requires_reported_full_quarter_confirmation", "representative_for_aggregate": true, "evidence_url": "https://home.imeritz.com/include/resource/research/WorkFlow/20240408105225297K_02.pdf"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_L177_01_241590_2024-03-20", "trigger_id": "TR_C18_L177_01_241590_Stage2Actionable_2024-03-20", "symbol": "241590", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"eps_fcf": 15, "visibility": 18, "bottleneck": 10, "mispricing": 14, "valuation": 12, "capital_allocation": 5, "information_confidence": 16}, "weighted_score_before": 90, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"eps_fcf": 17, "visibility": 23, "bottleneck": 12, "mispricing": 15, "valuation": 12, "capital_allocation": 5, "information_confidence": 19}, "weighted_score_after": 103, "stage_label_after": "Stage2-Actionable", "changed_components": ["visibility", "information_confidence", "eps_fcf", "valuation"], "component_delta_explanation": "C18 apparel OEM pass requires named buyer/order/revenue/margin bridge before positive stage; weak H2 recovery language and one-quarter order effect are capped.", "MFE_90D_pct": 36.38, "MAE_90D_pct": -6.04, "score_return_alignment_label": "current_profile_too_conservative_if_restocking_bridge_requires_reported_full_quarter_confirmation", "current_profile_verdict": "current_profile_too_conservative_if_restocking_bridge_requires_reported_full_quarter_confirmation"}
{"row_type": "case", "case_id": "C18_L177_02_241590_2024-10-08", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "241590", "company_name": "화승엔터프라이즈", "trigger_date": "2024-10-08", "event_summary": "Adidas sales growth recovery but single-customer concentration still visible", "evidence_url": "https://m.thebell.co.kr/m/newsview.asp?newskey=202410071721268360108213&svccode=", "evidence_family": "apparel_oem_reorder_inventory_normalization_margin_bridge", "case_result_label": "positive_with_4B_exit_guard", "calibration_usable": true, "novelty_check": "new_trigger_family_in_session_or_new_symbol_for_C18_apparel_oem_leaf"}
{"row_type": "trigger", "case_id": "C18_L177_02_241590_2024-10-08", "trigger_id": "TR_C18_L177_02_241590_Stage2Actionable_2024-10-08", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "241590", "company_name": "화승엔터프라이즈", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-10-08", "entry_date": "2024-10-08", "entry_price": 8640.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 14.0, "MAE_30D_pct": -5.21, "MFE_90D_pct": 38.89, "MAE_90D_pct": -7.18, "MFE_180D_pct": 38.89, "MAE_180D_pct": -19.21, "calibration_usable": true, "corporate_action_contamination_180D": false, "score_return_alignment_label": "current_profile_good_stage2_but_needs_customer_concentration_4b_exit_guard", "representative_for_aggregate": true, "evidence_url": "https://m.thebell.co.kr/m/newsview.asp?newskey=202410071721268360108213&svccode="}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_L177_02_241590_2024-10-08", "trigger_id": "TR_C18_L177_02_241590_Stage2Actionable_2024-10-08", "symbol": "241590", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"eps_fcf": 16, "visibility": 20, "bottleneck": 10, "mispricing": 16, "valuation": 14, "capital_allocation": 5, "information_confidence": 17}, "weighted_score_before": 98, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"eps_fcf": 18, "visibility": 24, "bottleneck": 11, "mispricing": 17, "valuation": 14, "capital_allocation": 5, "information_confidence": 20}, "weighted_score_after": 109, "stage_label_after": "Stage2-Actionable", "changed_components": ["visibility", "information_confidence", "eps_fcf", "valuation"], "component_delta_explanation": "C18 apparel OEM pass requires named buyer/order/revenue/margin bridge before positive stage; weak H2 recovery language and one-quarter order effect are capped.", "MFE_90D_pct": 38.89, "MAE_90D_pct": -7.18, "score_return_alignment_label": "current_profile_good_stage2_but_needs_customer_concentration_4b_exit_guard", "current_profile_verdict": "current_profile_good_stage2_but_needs_customer_concentration_4b_exit_guard"}
{"row_type": "case", "case_id": "C18_L177_03_111770_2024-10-15", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "111770", "company_name": "영원무역", "trigger_date": "2024-10-15", "event_summary": "OEM growth offset by SCOTT drag; 3Q24 preview looked weak at consolidated level", "evidence_url": "https://www.sks.co.kr/data1/research/qna_file/20241013153402123_0_ko.pdf", "evidence_family": "apparel_oem_reorder_inventory_normalization_margin_bridge", "case_result_label": "delayed_positive", "calibration_usable": true, "novelty_check": "new_trigger_family_in_session_or_new_symbol_for_C18_apparel_oem_leaf"}
{"row_type": "trigger", "case_id": "C18_L177_03_111770_2024-10-15", "trigger_id": "TR_C18_L177_03_111770_Stage2_2024-10-15", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "111770", "company_name": "영원무역", "trigger_type": "Stage2", "trigger_date": "2024-10-15", "entry_date": "2024-10-15", "entry_price": 43650.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 2.98, "MAE_30D_pct": -13.86, "MFE_90D_pct": 8.59, "MAE_90D_pct": -13.86, "MFE_180D_pct": 50.74, "MAE_180D_pct": -13.86, "calibration_usable": true, "corporate_action_contamination_180D": false, "score_return_alignment_label": "current_profile_too_late_if_consolidated_drag_blocks_oem_reorder_signal_until_after_price_moves", "representative_for_aggregate": true, "evidence_url": "https://www.sks.co.kr/data1/research/qna_file/20241013153402123_0_ko.pdf"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_L177_03_111770_2024-10-15", "trigger_id": "TR_C18_L177_03_111770_Stage2_2024-10-15", "symbol": "111770", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"eps_fcf": 10, "visibility": 15, "bottleneck": 8, "mispricing": 14, "valuation": 15, "capital_allocation": 5, "information_confidence": 15}, "weighted_score_before": 82, "stage_label_before": "Stage2", "raw_component_scores_after": {"eps_fcf": 13, "visibility": 20, "bottleneck": 9, "mispricing": 15, "valuation": 16, "capital_allocation": 5, "information_confidence": 18}, "weighted_score_after": 96, "stage_label_after": "Stage2-Actionable", "changed_components": ["visibility", "information_confidence", "eps_fcf", "valuation"], "component_delta_explanation": "C18 apparel OEM pass requires named buyer/order/revenue/margin bridge before positive stage; weak H2 recovery language and one-quarter order effect are capped.", "MFE_90D_pct": 8.59, "MAE_90D_pct": -13.86, "score_return_alignment_label": "current_profile_too_late_if_consolidated_drag_blocks_oem_reorder_signal_until_after_price_moves", "current_profile_verdict": "current_profile_too_late_if_consolidated_drag_blocks_oem_reorder_signal_until_after_price_moves"}
{"row_type": "case", "case_id": "C18_L177_04_111770_2025-03-04", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "111770", "company_name": "영원무역", "trigger_date": "2025-03-04", "event_summary": "OEM dollar-growth surprise; SCOTT inventory burden easing; 2025 profit growth turn", "evidence_url": "https://money2.daishin.com/PDF/Out/intranet_data/Product/ResearchCenter/Report/2025/03/52859_250304_Youngone.F.pdf", "evidence_family": "apparel_oem_reorder_inventory_normalization_margin_bridge", "case_result_label": "positive", "calibration_usable": true, "novelty_check": "new_trigger_family_in_session_or_new_symbol_for_C18_apparel_oem_leaf"}
{"row_type": "trigger", "case_id": "C18_L177_04_111770_2025-03-04", "trigger_id": "TR_C18_L177_04_111770_Stage2Actionable_2025-03-04", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "111770", "company_name": "영원무역", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-03-04", "entry_date": "2025-03-04", "entry_price": 46850.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 13.98, "MAE_30D_pct": -10.78, "MFE_90D_pct": 40.45, "MAE_90D_pct": -10.78, "MFE_180D_pct": 102.77, "MAE_180D_pct": -10.78, "calibration_usable": true, "corporate_action_contamination_180D": false, "score_return_alignment_label": "current_profile_good_stage2_if_oem_growth_and_inventory_relief_bridge_are_combined", "representative_for_aggregate": true, "evidence_url": "https://money2.daishin.com/PDF/Out/intranet_data/Product/ResearchCenter/Report/2025/03/52859_250304_Youngone.F.pdf"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_L177_04_111770_2025-03-04", "trigger_id": "TR_C18_L177_04_111770_Stage2Actionable_2025-03-04", "symbol": "111770", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"eps_fcf": 17, "visibility": 20, "bottleneck": 11, "mispricing": 16, "valuation": 18, "capital_allocation": 6, "information_confidence": 19}, "weighted_score_before": 107, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"eps_fcf": 20, "visibility": 25, "bottleneck": 12, "mispricing": 18, "valuation": 18, "capital_allocation": 6, "information_confidence": 22}, "weighted_score_after": 121, "stage_label_after": "Stage2-Actionable", "changed_components": ["visibility", "information_confidence", "eps_fcf", "valuation"], "component_delta_explanation": "C18 apparel OEM pass requires named buyer/order/revenue/margin bridge before positive stage; weak H2 recovery language and one-quarter order effect are capped.", "MFE_90D_pct": 40.45, "MAE_90D_pct": -10.78, "score_return_alignment_label": "current_profile_good_stage2_if_oem_growth_and_inventory_relief_bridge_are_combined", "current_profile_verdict": "current_profile_good_stage2_if_oem_growth_and_inventory_relief_bridge_are_combined"}
{"row_type": "case", "case_id": "C18_L177_05_007980_2024-08-14", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "007980", "company_name": "TP", "trigger_date": "2024-08-14", "event_summary": "Q2 order increase and cost discipline headline but no durable rerating path", "evidence_url": "https://v.daum.net/v/yXwvdhYcSB", "evidence_family": "apparel_oem_reorder_inventory_normalization_margin_bridge", "case_result_label": "counterexample", "calibration_usable": true, "novelty_check": "new_trigger_family_in_session_or_new_symbol_for_C18_apparel_oem_leaf"}
{"row_type": "trigger", "case_id": "C18_L177_05_007980_2024-08-14", "trigger_id": "TR_C18_L177_05_007980_Stage2Actionable_2024-08-14", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "007980", "company_name": "TP", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-14", "entry_date": "2024-08-14", "entry_price": 1470.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 1.36, "MAE_30D_pct": -14.01, "MFE_90D_pct": 4.9, "MAE_90D_pct": -14.01, "MFE_180D_pct": 5.37, "MAE_180D_pct": -15.1, "calibration_usable": true, "corporate_action_contamination_180D": false, "score_return_alignment_label": "current_profile_false_positive_if_one_quarter_order_effect_is_treated_as_channel_reorder_cycle", "representative_for_aggregate": true, "evidence_url": "https://v.daum.net/v/yXwvdhYcSB"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_L177_05_007980_2024-08-14", "trigger_id": "TR_C18_L177_05_007980_Stage2Actionable_2024-08-14", "symbol": "007980", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"eps_fcf": 15, "visibility": 18, "bottleneck": 8, "mispricing": 15, "valuation": 13, "capital_allocation": 5, "information_confidence": 17}, "weighted_score_before": 91, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"eps_fcf": 12, "visibility": 14, "bottleneck": 6, "mispricing": 12, "valuation": 12, "capital_allocation": 5, "information_confidence": 16}, "weighted_score_after": 77, "stage_label_after": "Stage2-Watch", "changed_components": ["visibility", "information_confidence", "eps_fcf", "valuation"], "component_delta_explanation": "C18 apparel OEM pass requires named buyer/order/revenue/margin bridge before positive stage; weak H2 recovery language and one-quarter order effect are capped.", "MFE_90D_pct": 4.9, "MAE_90D_pct": -14.01, "score_return_alignment_label": "current_profile_false_positive_if_one_quarter_order_effect_is_treated_as_channel_reorder_cycle", "current_profile_verdict": "current_profile_false_positive_if_one_quarter_order_effect_is_treated_as_channel_reorder_cycle"}
{"row_type": "case", "case_id": "C18_L177_06_105630_2025-02-25", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "105630", "company_name": "한세실업", "trigger_date": "2025-02-25", "event_summary": "2025 order recovery expected but weak and delayed; valuation trap despite low PER", "evidence_url": "https://www.businesspost.co.kr/BP?command=article_view&num=384721", "evidence_family": "apparel_oem_reorder_inventory_normalization_margin_bridge", "case_result_label": "counterexample", "calibration_usable": true, "novelty_check": "new_trigger_family_in_session_or_new_symbol_for_C18_apparel_oem_leaf"}
{"row_type": "trigger", "case_id": "C18_L177_06_105630_2025-02-25", "trigger_id": "TR_C18_L177_06_105630_Stage2Actionable_2025-02-25", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "105630", "company_name": "한세실업", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-25", "entry_date": "2025-02-25", "entry_price": 12460.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 2.09, "MAE_30D_pct": -22.39, "MFE_90D_pct": 2.09, "MAE_90D_pct": -22.39, "MFE_180D_pct": 5.22, "MAE_180D_pct": -27.37, "calibration_usable": true, "corporate_action_contamination_180D": false, "score_return_alignment_label": "current_profile_false_positive_if_low_per_and_h2_order_recovery_language_lack_actual_reorder_confirmation", "representative_for_aggregate": true, "evidence_url": "https://www.businesspost.co.kr/BP?command=article_view&num=384721"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_L177_06_105630_2025-02-25", "trigger_id": "TR_C18_L177_06_105630_Stage2Actionable_2025-02-25", "symbol": "105630", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"eps_fcf": 14, "visibility": 17, "bottleneck": 7, "mispricing": 16, "valuation": 18, "capital_allocation": 5, "information_confidence": 16}, "weighted_score_before": 93, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"eps_fcf": 10, "visibility": 13, "bottleneck": 6, "mispricing": 12, "valuation": 16, "capital_allocation": 5, "information_confidence": 15}, "weighted_score_after": 77, "stage_label_after": "Stage2-Watch", "changed_components": ["visibility", "information_confidence", "eps_fcf", "valuation"], "component_delta_explanation": "C18 apparel OEM pass requires named buyer/order/revenue/margin bridge before positive stage; weak H2 recovery language and one-quarter order effect are capped.", "MFE_90D_pct": 2.09, "MAE_90D_pct": -22.39, "score_return_alignment_label": "current_profile_false_positive_if_low_per_and_h2_order_recovery_language_lack_actual_reorder_confirmation", "current_profile_verdict": "current_profile_false_positive_if_low_per_and_h2_order_recovery_language_lack_actual_reorder_confirmation"}
{"row_type": "case", "case_id": "C18_L177_07_111110_2025-04-21", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "111110", "company_name": "호전실업", "trigger_date": "2025-04-21", "event_summary": "Arc’teryx/Lululemon premium OEM new-customer order bridge but still small-cap execution watch", "evidence_url": "https://m.newsprime.co.kr/section_view.html?no=684589", "evidence_family": "apparel_oem_reorder_inventory_normalization_margin_bridge", "case_result_label": "positive_watch", "calibration_usable": true, "novelty_check": "new_trigger_family_in_session_or_new_symbol_for_C18_apparel_oem_leaf"}
{"row_type": "trigger", "case_id": "C18_L177_07_111110_2025-04-21", "trigger_id": "TR_C18_L177_07_111110_Stage2_2025-04-21", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "symbol": "111110", "company_name": "호전실업", "trigger_type": "Stage2", "trigger_date": "2025-04-21", "entry_date": "2025-04-21", "entry_price": 8120.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 12.44, "MAE_30D_pct": -3.33, "MFE_90D_pct": 13.18, "MAE_90D_pct": -16.75, "MFE_180D_pct": 13.18, "MAE_180D_pct": -16.75, "calibration_usable": true, "corporate_action_contamination_180D": false, "score_return_alignment_label": "current_profile_stage2_watch_correct_until_new_customer_order_scale_repeats_or_margin_bridge_confirms", "representative_for_aggregate": true, "evidence_url": "https://m.newsprime.co.kr/section_view.html?no=684589"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_L177_07_111110_2025-04-21", "trigger_id": "TR_C18_L177_07_111110_Stage2_2025-04-21", "symbol": "111110", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"eps_fcf": 13, "visibility": 17, "bottleneck": 9, "mispricing": 16, "valuation": 18, "capital_allocation": 8, "information_confidence": 17}, "weighted_score_before": 98, "stage_label_before": "Stage2", "raw_component_scores_after": {"eps_fcf": 15, "visibility": 21, "bottleneck": 10, "mispricing": 17, "valuation": 18, "capital_allocation": 8, "information_confidence": 20}, "weighted_score_after": 109, "stage_label_after": "Stage2-Watch", "changed_components": ["visibility", "information_confidence", "eps_fcf", "valuation"], "component_delta_explanation": "C18 apparel OEM pass requires named buyer/order/revenue/margin bridge before positive stage; weak H2 recovery language and one-quarter order effect are capped.", "MFE_90D_pct": 13.18, "MAE_90D_pct": -16.75, "score_return_alignment_label": "current_profile_stage2_watch_correct_until_new_customer_order_scale_repeats_or_margin_bridge_confirms", "current_profile_verdict": "current_profile_stage2_watch_correct_until_new_customer_order_scale_repeats_or_margin_bridge_confirms"}
{"row_type": "aggregate", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "apparel_oem_restocking_customer_reorder_margin_bridge", "new_independent_case_count": 7, "reused_case_count": 0, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 7, "calibration_usable_trigger_count": 7, "representative_trigger_count": 7, "positive_case_count": 5, "counterexample_count": 2, "stage4b_watch_or_overlay_count": 3, "current_profile_error_count": 4, "loop_contribution_label": "canonical_archetype_rule_candidate|quality_repair", "do_not_propose_new_weight_delta": false, "rule_candidate": "C18_APPAREL_OEM_REORDER_MARGIN_BRIDGE_GATE_V1"}
{"row_type": "shadow_weight", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "proposal_id": "C18_APPAREL_OEM_REORDER_MARGIN_BRIDGE_GATE_V1", "production_scoring_changed": false, "shadow_weight_only": true, "suggested_rule_text": "For apparel OEM export reorder, require named buyer/order/shipment or revenue timing plus margin/working-capital bridge. Cap low-valuation/H2 recovery/one-quarter order effect at Stage2-Watch. Allow staged Stage2 when consolidated drag hides confirmed OEM order recovery.", "tested_existing_axes": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_strengthened": ["stage2_required_bridge", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": ["do_not_block_confirmed_oem_order_recovery_solely_because_consolidated_subsidiary_drag_remains"], "max_delta_scope": "C18_apparel_oem_subleaf_only"}
{"row_type": "residual_contribution", "round": "R5", "loop": "177", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 7, "counterexample_count": 2, "current_profile_error_count": 4, "residual_error_types_found": ["one_quarter_order_effect_false_positive", "low_per_h2_recovery_language_false_positive", "consolidated_drag_hides_oem_reorder_signal", "single_customer_concentration_needs_4b_exit_guard", "new_customer_order_bridge_needs_repeat_scale_confirmation"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 10. Batch Ingest Self-Audit

```text
expected_v12_result_file = true
filename_pattern_pass = true
metadata_filename_consistency = pass
jsonl_trigger_row_count = 7
calibration_usable_trigger_count = 7
representative_trigger_count = 7
new_weight_evidence_candidate_count = 7
rows_missing_required_mfe_mae = 0
rows_missing_entry_price_or_date = 0
rows_with_noncanonical_trigger_type = 0
corporate_action_contaminated_180D_rows = 0
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 11. Deferred Coding Agent Handoff Prompt — Do Not Execute In This Research Loop

```text
Read this MD as a candidate v12 residual research artifact only. Do not treat it as an immediate production patch. Validate JSONL rows, deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date, confirm stock-web MFE/MAE fields, and only then consider a scoped C18 apparel_oem_reorder bridge rule. Preserve active profile rollback and keep all changes as safe patch specs unless enough cross-case evidence supports promotion.
```

## 12. Next Research State

```text
completed_round = R5
completed_loop = 177
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|C18_CONSUMER_EXPORT_CHANNEL_REORDER|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
