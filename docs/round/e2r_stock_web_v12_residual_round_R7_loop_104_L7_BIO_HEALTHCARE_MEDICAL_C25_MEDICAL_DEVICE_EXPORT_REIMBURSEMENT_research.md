# stock-web v12 residual research — R7 / loop 104 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT

## 0. Execution metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
```

This file is a standalone historical calibration artifact. It is not a live watchlist, not a current recommendation, and not a production scoring patch.

## 1. Selection

```text
selected_round = R7
selected_loop = 104
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_DEVICE_INSTALLED_BASE_EXPORT_REIMBURSEMENT_RECURRING_REVENUE_BRIDGE_VS_DEVICE_LABEL_HIGH_MAE_FADE
selected_priority_bucket = Priority 1
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
```

C25 remains under the 50-row practical calibration target. The current residual gap is not “find more healthcare winners,” but to separate a real medical-device revenue bridge from device-category labels that can create temporary MFE and then collapse.

Already-used C25 case set avoided in this execution:

```text
- 214150 클래시스
- 145720 덴티움
- 338220 뷰노
```

New case set:

```text
- 065510 휴비츠
- 099190 아이센스
- 228670 레이
```

## 2. Price source verification

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Corporate-action note: the selected windows are outside the corporate-action candidate dates shown in the relevant symbol profiles. Raw/unadjusted caveat remains attached by default.

## 3. Case summary

| case | role | entry | MFE | MAE | interpretation |
|---|---:|---:|---:|---:|---|
| 065510 휴비츠 | positive with 4B watch | 2023-04-12 close 11,160 | +119.53% | -8.78% | ophthalmic/optometry device product bridge can work when price confirms quickly |
| 099190 아이센스 | counterexample | 2023-07-18 close 32,000 | +24.06% | -35.47% | CGM launch/reimbursement label without adoption bridge becomes high-MAE fade |
| 228670 레이 | counterexample | 2023-04-12 close 37,150 | +13.46% | -47.78% | dental digital device/channel label fails without sell-through/order bridge |

## 4. Case details

### 4.1 065510 휴비츠 — ophthalmic device bridge positive, but still 4B watch

Huvitz is an eye-care solution/device company with ophthalmology and optometry products, diagnostic devices, fundus camera, OCT, lens edging solution, and dental device categories. The relevant C25 bridge is not “healthcare” in the abstract; it is install-base, distributor, device revenue and post-sale channel conversion.

```text
symbol = 065510
entry_date = 2023-04-12
entry_price = 11,160
peak_date = 2023-06-29
peak_price = 24,500
trough_date = 2023-04-12
trough_price = 10,180
MFE = +119.53%
MAE = -8.78%
peak_to_later_drawdown_watch = -42.69% from 24,500 to 14,040
classification = positive_with_4b_watch
```

Interpretation: This is the positive control. The C25 score can improve when a device company has a clear product category plus export/install-base logic and the price path confirms with shallow early MAE. Still, the later drawdown shows why Stage3-Green should require sustained order/revenue/revision confirmation rather than just a device-cycle rally.

### 4.2 099190 아이센스 — CGM label high-MFE/high-MAE counterexample

```text
symbol = 099190
entry_date = 2023-07-18
entry_price = 32,000
peak_date = 2023-09-08
peak_price = 39,700
trough_date = 2023-11-13
trough_price = 20,650
MFE = +24.06%
MAE = -35.47%
peak_to_trough_drawdown = -47.98%
classification = counterexample_high_mfe_high_mae
source_status = source_proxy_only_url_repair_required
```

Interpretation: CGM is a real medical-device category, but the stock path shows that launch/reimbursement labels do not automatically become durable rerating. C25 should ask whether the CGM line has adoption, reimbursement coverage, recurring sensor revenue, gross-margin visibility, and churn/retention evidence. Without that bridge, the profile should be capped at 4B/event-watch or moved to 4C on hard fade.

### 4.3 228670 레이 — dental digital device label fade

```text
symbol = 228670
entry_date = 2023-04-12
entry_price = 37,150
peak_date = 2023-06-15
peak_price = 42,150
trough_date = 2023-10-31
trough_price = 19,400
MFE = +13.46%
MAE = -47.78%
peak_to_trough_drawdown = -53.97%
classification = counterexample_low_quality_device_export_label
source_status = company_category_verified_trigger_url_repair_required
```

Interpretation: Digital dentistry/dental device exposure can look like a C25 export/reimbursement theme, especially around China dental volume or digital workflow expectations. But the actual path is a weak MFE followed by a severe high-MAE collapse. C25 must demand channel sell-through, confirmed dental-clinic adoption, receivables quality, China/local distributor quality, and recurring software/material revenue before Stage2-Actionable.

## 5. Residual rule proposal

```text
new_axis_proposed = c25_installed_base_reimbursement_export_recurring_revenue_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C25 medical-device/export/reimbursement-label rallies
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

Rule candidate:

```text
IF canonical_archetype_id == C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
AND trigger evidence is only device category / export label / reimbursement label / launch label
AND no installed-base, reimbursement coverage, recurring consumable/sensor revenue, export order, sell-through, or OPM/revision bridge is verified
THEN cap at Stage2 or 4B-watch.
IF post-entry low breaks below -25% MAE while MFE < +30%
THEN classify as 4C-prone counterexample for calibration.
```

Positive exception:

```text
IF device revenue bridge is supported by product-category evidence plus fast price confirmation, shallow early MAE, and later revision/order confirmation,
THEN allow Stage2-Actionable or Stage3-Yellow.
Stage3-Green still requires non-price bridge persistence.
```

## 6. JSONL rows

```jsonl
{"row_type": "case", "case_id": "C25_HUVITZ_OPHTHALMIC_EYECARE_EXPORT_DEVICE_BRIDGE_20230412", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "symbol": "065510", "name": "휴비츠", "trigger_date": "2023-04-12", "entry_date": "2023-04-12", "entry_price": 11160, "peak_date": "2023-06-29", "peak_price": 24500, "trough_date": "2023-04-12", "trough_price": 10180, "mfe_pct": 119.53, "mae_pct": -8.78, "classification": "positive_with_4b_watch", "calibration_usable": true, "source_status": "verified_company_category_plus_stock_web_ohlc", "rule_hint": "C25 positive only when device product category is tied to export/install-base/order bridge, not generic healthcare keyword."}
{"row_type": "case", "case_id": "C25_ISENS_CGM_LAUNCH_REIMBURSEMENT_LABEL_HIGH_MAE_20230718", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "symbol": "099190", "name": "아이센스", "trigger_date": "2023-07-18", "entry_date": "2023-07-18", "entry_price": 32000, "peak_date": "2023-09-08", "peak_price": 39700, "trough_date": "2023-11-13", "trough_price": 20650, "mfe_pct": 24.06, "mae_pct": -35.47, "classification": "counterexample_high_mfe_high_mae", "calibration_usable": true, "source_status": "source_proxy_only_url_repair_required", "rule_hint": "C25 should not treat CGM launch/reimbursement label as Green without adoption/reimbursement/recurring-sensor revenue bridge."}
{"row_type": "case", "case_id": "C25_RAY_DENTAL_DIGITAL_DEVICE_EXPORT_CHINA_VBP_FADE_20230412", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "symbol": "228670", "name": "레이", "trigger_date": "2023-04-12", "entry_date": "2023-04-12", "entry_price": 37150, "peak_date": "2023-06-15", "peak_price": 42150, "trough_date": "2023-10-31", "trough_price": 19400, "mfe_pct": 13.46, "mae_pct": -47.78, "classification": "counterexample_low_quality_device_export_label", "calibration_usable": true, "source_status": "company_category_verified_trigger_url_repair_required", "rule_hint": "C25 dental-device/digital-dentistry label needs sell-through/order/China channel evidence; otherwise price path is 4C-prone."}
{"row_type": "trigger", "trigger_id": "TRG_C25_HUVITZ_20230412", "case_id": "C25_HUVITZ_OPHTHALMIC_EYECARE_EXPORT_DEVICE_BRIDGE_20230412", "trigger_type": "ophthalmic_optometry_device_export_install_base_bridge", "entry_date": "2023-04-12", "entry_price": 11160, "mfe_pct": 119.53, "mae_pct": -8.78}
{"row_type": "trigger", "trigger_id": "TRG_C25_ISENS_20230718", "case_id": "C25_ISENS_CGM_LAUNCH_REIMBURSEMENT_LABEL_HIGH_MAE_20230718", "trigger_type": "cgm_launch_reimbursement_label_without_adoption_bridge", "entry_date": "2023-07-18", "entry_price": 32000, "mfe_pct": 24.06, "mae_pct": -35.47}
{"row_type": "trigger", "trigger_id": "TRG_C25_RAY_20230412", "case_id": "C25_RAY_DENTAL_DIGITAL_DEVICE_EXPORT_CHINA_VBP_FADE_20230412", "trigger_type": "dental_digital_device_export_channel_label_fade", "entry_date": "2023-04-12", "entry_price": 37150, "mfe_pct": 13.46, "mae_pct": -47.78}
{"row_type": "aggregate", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "case_count": 3, "positive_case_count": 1, "counterexample_count": 2, "new_independent_case_count": 3, "reused_case_count": 0, "coverage_gap_basis": "V12 No-Repeat Index Priority 1: C25 rows 33, need 17 to 50", "residual_rule_candidate": "C25 requires installed-base/export/reimbursement/recurring-revenue bridge before Stage2-Actionable; device category label alone stays 4B/4C watch."}
{"row_type": "shadow_weight", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "shadow_weight_only": true, "new_axis_proposed": "c25_installed_base_reimbursement_export_recurring_revenue_bridge_required_for_stage2_actionable_shadow_only", "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to C25 medical-device/export/reimbursement-label rallies", "production_scoring_changed": false}
{"row_type": "residual_contribution", "loop": "104", "round": "R7", "label": "canonical_archetype_rule_candidate", "contribution": "Separates true device installed-base/export bridge from CGM/dental device label rallies that fade into high-MAE paths."}
```

## 7. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

You are a coding agent working on Songdaiki/stock_agent after a batch of v12 residual research MD files has been collected.

Task:
1. Read this MD as one historical calibration artifact.
2. Extract the JSONL rows from section 6.
3. Validate that this artifact does not duplicate existing canonical_archetype_id + symbol + trigger_type + entry_date keys.
4. Add only shadow-weight / calibration-data artifacts, not production scoring changes.
5. Do not change live scan behavior.
6. Use this artifact to test whether C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT should require installed-base / reimbursement / export / recurring-revenue bridge before Stage2-Actionable.
7. Preserve source_status flags, especially source_proxy_only_url_repair_required.
```

## 8. Final run summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 3
verified_url_repair_needed_count = 2

diversity_score_summary = C25 Priority 1 보강 + Huvitz ophthalmic/device positive + i-SENS CGM label high-MAE counterexample + Ray dental digital device high-MAE counterexample
loop_contribution_label = canonical_archetype_rule_candidate
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C22_INSURANCE_RATE_CYCLE_RESERVE, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```
