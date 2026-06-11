# stock-web v12 residual research — R7 loop 106 — C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R7
selected_loop = 106
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_AI_REIMBURSEMENT_AESTHETIC_DEVICE_DENTAL_INSTALLED_BASE_BRIDGE_VS_DENTAL_IMPLANT_LABEL_HIGH_MAE_FADE
output_format = one_standalone_markdown_file
stock_web_price_atlas_access_required = true
stock_agent_code_access_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Scope and no-repeat decision

This run intentionally does **not** access or patch `stock_agent` code. It reads only the execution prompt, the no-repeat / coverage index, and `Songdaiki/stock-web` price atlas rows.

No-repeat exclusions used for C25:

```text
already-used C25 examples avoided:
- Classys / Dentium / VUNO
- Huvitz / i-SENS / Ray
- Seegene / SD Biosensor / Wontech
```

New case set:

```text
case_01 = JLK / 322510 / medical-AI reimbursement route / positive but 4B peak-fade watch
case_02 = Jeisys Medical / 287410 / aesthetic-device installed-base and consumables route / positive with delisting-liquidity caveat
case_03 = Vatech / 043150 / dental imaging export/device installed-base route / positive watch
case_04 = DIO / 039840 / dental implant/digital-dentistry label / high-MAE counterexample
```

## 2. Price source

```text
price_source_repo = Songdaiki/stock-web
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status = raw_unadjusted_marcap
corporate_action_contaminated_windows = blocked_by_default
```

## 3. Research thesis

C25 is not simply “medical device company went up.”

The useful calibration boundary is:

```text
device / reimbursement / installed base / consumable replacement / export distribution
    -> revenue bridge
    -> gross margin / OPM / recurring sales visibility
    -> revision durability
```

The recurring error is that the current profile can over-credit broad labels such as:

```text
medical AI
aesthetic device
dental imaging
dental implant
digital dentistry
```

without verifying whether the signal has a reimbursement route, installed-base expansion, recurring consumables, distributor quality, or margin conversion.

This round therefore separates:

```text
positive-but-watch:
- JLK medical-AI reimbursement route: huge path, but peak-fade and source repair required
- Jeisys aesthetic device route: strong path, but delisted later and company-specific trigger/source repair required
- Vatech dental imaging route: moderate clean path, but not automatic Green

counterexample:
- DIO dental implant/digital-dentistry route: respectable MFE but high MAE, so label-only scoring remains unsafe
```

## 4. Trigger-level cases

### 4.1 JLK — medical AI reimbursement route, positive but full 4B peak-fade watch

```text
symbol = 322510
name = 제이엘케이
trigger_family = medical_ai_reimbursement_market_access
trigger_date = 2023-02-24
entry_date = 2023-02-24
entry_price = 5700
peak_date = 2023-08-11
peak_price = 39050
low_date_for_mae = 2023-04-11
low_price_for_mae = 4820
MFE = +585.09%
MAE = -15.44%
post_peak_low_reference = 2023-10-23 low 16250
peak_to_post_low_drawdown = -58.39%
classification = positive_with_full_4B_peak_fade_watch
source_status = source_proxy_only_url_repair_required
```

Interpretation:

The price path is too strong to ignore. It captures the market’s willingness to rerate a medical-AI / reimbursement / hospital adoption route when investors believe reimbursement unlocks revenue conversion. But the route also has a large peak-to-later drawdown and no repaired firm-specific source spine in this run. Therefore this should not become a raw Stage3-Green shortcut. It is a C25 positive case only when the model can prove: reimbursement or billing route, installed hospital use, paid clinical workflow, and revenue/OPM revision.

### 4.2 Jeisys Medical — aesthetic device installed-base route, positive with delisting/liquidity caveat

```text
symbol = 287410
name = 제이시스메디칼
trigger_family = aesthetic_device_installed_base_consumables_export
trigger_date = 2023-07-05
entry_date = 2023-07-05
entry_price = 10150
peak_date = 2023-08-24
peak_price = 14500
low_date_for_mae = 2023-10-20
low_price_for_mae = 9950
MFE = +42.86%
MAE = -1.97%
classification = positive_with_delisting_liquidity_4B_watch
source_status = source_proxy_only_url_repair_required
```

Interpretation:

This case supports the C25 thesis that aesthetic devices can work when the route implies installed-base growth, overseas channels, and recurring consumables or service revenue. However, the stock later becomes inactive/delisted-like in the atlas profile. That does not invalidate the 2023 calibration path, but it means full-window extrapolation and production scoring should treat it as a local historical case only.

### 4.3 Vatech — dental imaging device export route, moderate clean positive watch

```text
symbol = 043150
name = 바텍
trigger_family = dental_imaging_export_installed_base
trigger_date = 2023-03-29
entry_date = 2023-03-29
entry_price = 32100
peak_date = 2023-07-12
peak_price = 43100
low_date_for_mae = 2023-10-04
low_price_for_mae = 30800
MFE = +34.27%
MAE = -4.05%
classification = moderate_positive_stage2_watch
source_status = source_proxy_only_url_repair_required
```

Interpretation:

Vatech is a cleaner device/export-installed-base route than many label-only dental names. The path has moderate MFE and contained MAE. But C25 should still demand evidence of order quality, regional distributor strength, installed base, maintenance/software revenue, and gross-margin durability before assigning Green. This case supports Stage2/Stage2-Actionable only after evidence repair.

### 4.4 DIO — dental implant / digital dentistry label, high-MAE counterexample

```text
symbol = 039840
name = 디오
trigger_family = dental_implant_digital_dentistry_label
trigger_date = 2023-04-11
entry_date = 2023-04-11
entry_price = 30250
peak_date = 2023-07-24
peak_price = 37100
low_date_for_mae = 2023-11-17
low_price_for_mae = 20550
MFE = +22.64%
MAE = -32.07%
classification = counterexample_high_MAE_label_fade
source_status = source_proxy_only_url_repair_required
```

Interpretation:

DIO demonstrates the residual error: a plausible dental implant / digital dentistry label can produce a positive local MFE, yet still deliver a large adverse excursion. This is exactly where C25 must distinguish label exposure from durable revenue conversion. The model should penalize names where the signal is only “dental implant/digital dentistry” without evidence of new order flow, international adoption, consumable attach, reimbursement support, or margin revision.

## 5. Machine-readable rows

### 5.1 case_rows.jsonl

```jsonl
{"row_type":"case","case_id":"C25_R7_L106_322510_JLK_2023_02_24","round":"R7","loop":106,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_AESTHETIC_DEVICE_DENTAL_INSTALLED_BASE_BRIDGE_VS_DENTAL_IMPLANT_LABEL_HIGH_MAE_FADE","symbol":"322510","name":"제이엘케이","trigger_date":"2023-02-24","entry_date":"2023-02-24","entry_price":5700,"peak_date":"2023-08-11","peak_price":39050,"low_date_for_mae":"2023-04-11","low_price_for_mae":4820,"mfe_pct":585.09,"mae_pct":-15.44,"classification":"positive_with_full_4B_peak_fade_watch","source_status":"source_proxy_only_url_repair_required","calibration_usable":true}
{"row_type":"case","case_id":"C25_R7_L106_287410_JEISYS_2023_07_05","round":"R7","loop":106,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_AESTHETIC_DEVICE_DENTAL_INSTALLED_BASE_BRIDGE_VS_DENTAL_IMPLANT_LABEL_HIGH_MAE_FADE","symbol":"287410","name":"제이시스메디칼","trigger_date":"2023-07-05","entry_date":"2023-07-05","entry_price":10150,"peak_date":"2023-08-24","peak_price":14500,"low_date_for_mae":"2023-10-20","low_price_for_mae":9950,"mfe_pct":42.86,"mae_pct":-1.97,"classification":"positive_with_delisting_liquidity_4B_watch","source_status":"source_proxy_only_url_repair_required","calibration_usable":true}
{"row_type":"case","case_id":"C25_R7_L106_043150_VATECH_2023_03_29","round":"R7","loop":106,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_AESTHETIC_DEVICE_DENTAL_INSTALLED_BASE_BRIDGE_VS_DENTAL_IMPLANT_LABEL_HIGH_MAE_FADE","symbol":"043150","name":"바텍","trigger_date":"2023-03-29","entry_date":"2023-03-29","entry_price":32100,"peak_date":"2023-07-12","peak_price":43100,"low_date_for_mae":"2023-10-04","low_price_for_mae":30800,"mfe_pct":34.27,"mae_pct":-4.05,"classification":"moderate_positive_stage2_watch","source_status":"source_proxy_only_url_repair_required","calibration_usable":true}
{"row_type":"case","case_id":"C25_R7_L106_039840_DIO_2023_04_11","round":"R7","loop":106,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_AESTHETIC_DEVICE_DENTAL_INSTALLED_BASE_BRIDGE_VS_DENTAL_IMPLANT_LABEL_HIGH_MAE_FADE","symbol":"039840","name":"디오","trigger_date":"2023-04-11","entry_date":"2023-04-11","entry_price":30250,"peak_date":"2023-07-24","peak_price":37100,"low_date_for_mae":"2023-11-17","low_price_for_mae":20550,"mfe_pct":22.64,"mae_pct":-32.07,"classification":"counterexample_high_MAE_label_fade","source_status":"source_proxy_only_url_repair_required","calibration_usable":true}
```

### 5.2 trigger_rows_representative.jsonl

```jsonl
{"row_type":"trigger","trigger_id":"C25_MEDICAL_AI_REIMBURSEMENT_322510_2023_02_24","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"322510","trigger_type":"medical_ai_reimbursement_market_access","entry_date":"2023-02-24","entry_price":5700,"mfe_pct":585.09,"mae_pct":-15.44,"stage_hint":"Stage2_Actionable_if_reimbursement_hospital_revenue_bridge_verified_else_4B_watch"}
{"row_type":"trigger","trigger_id":"C25_AESTHETIC_INSTALLED_BASE_287410_2023_07_05","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"287410","trigger_type":"aesthetic_device_installed_base_consumables_export","entry_date":"2023-07-05","entry_price":10150,"mfe_pct":42.86,"mae_pct":-1.97,"stage_hint":"Stage2_watch_with_delisting_liquidity_caveat"}
{"row_type":"trigger","trigger_id":"C25_DENTAL_IMAGING_EXPORT_043150_2023_03_29","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"043150","trigger_type":"dental_imaging_export_installed_base","entry_date":"2023-03-29","entry_price":32100,"mfe_pct":34.27,"mae_pct":-4.05,"stage_hint":"Stage2_watch_not_Green_without_order_margin_bridge"}
{"row_type":"trigger","trigger_id":"C25_DENTAL_IMPLANT_LABEL_039840_2023_04_11","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"039840","trigger_type":"dental_implant_digital_dentistry_label","entry_date":"2023-04-11","entry_price":30250,"mfe_pct":22.64,"mae_pct":-32.07,"stage_hint":"4B_or_4C_watch_if_no_export_consumable_margin_bridge"}
```

### 5.3 score_simulation_rows.jsonl

```jsonl
{"row_type":"score_simulation","rule_id":"c25_reimbursement_installed_base_recurring_revenue_bridge_required","symbol":"322510","without_rule_stage":"Stage3_Yellow_or_Green_possible_by_price_strength","with_rule_stage":"Stage2_Actionable_or_4B_watch","reason":"large MFE but source repair and peak-fade require reimbursement plus revenue bridge"}
{"row_type":"score_simulation","rule_id":"c25_reimbursement_installed_base_recurring_revenue_bridge_required","symbol":"287410","without_rule_stage":"Stage3_Yellow_possible_by_clean_MFE_MAE","with_rule_stage":"Stage2_watch","reason":"aesthetic-device path worked but inactive/delisted-like profile requires full-window caution"}
{"row_type":"score_simulation","rule_id":"c25_dental_label_penalty_without_order_margin_bridge","symbol":"043150","without_rule_stage":"Stage3_Yellow_possible_by_device_export_label","with_rule_stage":"Stage2_watch","reason":"moderate clean path but evidence must show dental imaging order/export/installed-base conversion"}
{"row_type":"score_simulation","rule_id":"c25_dental_label_penalty_without_order_margin_bridge","symbol":"039840","without_rule_stage":"Stage2_or_Yellow_possible_by_dental_implant_label","with_rule_stage":"4B_watch_or_4C","reason":"MFE positive but MAE -32.07 shows label-only residual error"}
```

### 5.4 aggregate_rows.jsonl

```jsonl
{"row_type":"aggregate","round":"R7","loop":106,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":4,"reused_case_count":0,"positive_case_count":3,"counterexample_count":1,"full_4B_watch_count":3,"current_profile_error_count":4,"verified_url_repair_needed_count":4}
```

### 5.5 shadow_weight_rows.jsonl

```jsonl
{"row_type":"shadow_weight","rule_id":"c25_reimbursement_installed_base_recurring_revenue_bridge_required_v2","target_scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","proposed_change_type":"shadow_only_feature_gate","production_scoring_changed":false,"positive_condition":"reimbursement/billing route OR installed-base/consumable/export order bridge AND revenue/margin visibility","negative_condition":"device/dental/AI label without company-specific adoption/revenue/OPM bridge","expected_effect":"reduce false Stage3 for label-only dental/AI/device rallies while retaining true positive C25 routes"}
```

### 5.6 residual_contribution_rows.jsonl

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","contribution_label":"canonical_archetype_rule_candidate","new_axis":"c25_reimbursement_installed_base_recurring_revenue_bridge_required_v2","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C25 medical-AI/aesthetic/dental-device rallies","existing_axis_weakened":null}
```

## 6. Proposed shadow rule

```text
rule_id = c25_reimbursement_installed_base_recurring_revenue_bridge_required_v2
scope = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
status = shadow_only
production_scoring_changed = false

If a C25 trigger is based on medical AI, aesthetic device, dental imaging, dental implant, or medical-device export label,
do not allow Stage3-Green unless at least one of the following is verified:

1. reimbursement / billing route:
   - insured or reimbursed clinical workflow
   - non-insured but paid hospital workflow with clear pricing
   - government/medical society adoption route

2. installed-base / recurring bridge:
   - installed device base is expanding
   - consumables, probes, cartridges, software, maintenance, or repeat procedures attach to the device

3. export/distributor quality:
   - named region or distributor
   - repeated orders or customer expansion
   - regulatory clearance tied to revenue opportunity

4. margin/revision bridge:
   - ASP, gross margin, OPM, or analyst revision evidence

Otherwise:
- keep as Stage2 watch at most if MFE is positive and MAE is contained
- move to 4B/4C watch if MAE is high or source spine is unrepaired
```

## 7. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this MD as an immediate production-scoring patch request.
Batch this MD with other v12 residual calibration MDs.

Input artifact:
- e2r_stock_web_v12_residual_round_R7_loop_106_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md

Task:
1. Parse the machine-readable JSONL rows in sections 5.1~5.6.
2. Add the cases to the research registry only if no canonical_archetype_id + symbol + trigger_type + entry_date duplicate exists.
3. Implement only shadow rules or diagnostic flags unless a later consolidated batch explicitly approves production scoring changes.
4. Candidate shadow rule:
   - c25_reimbursement_installed_base_recurring_revenue_bridge_required_v2
5. Ensure C25 medical-AI/aesthetic/dental-device labels cannot auto-upgrade to Stage3-Green without:
   - reimbursement/billing route, OR
   - installed-base/consumable bridge, OR
   - export/distributor/order bridge, AND
   - margin/revision support.
6. Keep all changes behind shadow_weight_only=true.
```

## 8. Final summary

```text
selected_round: R7
selected_loop: 106
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: MEDICAL_AI_REIMBURSEMENT_AESTHETIC_DEVICE_DENTAL_INSTALLED_BASE_BRIDGE_VS_DENTAL_IMPLANT_LABEL_HIGH_MAE_FADE

new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 4
verified_url_repair_needed_count: 4

new_axis_proposed: c25_reimbursement_installed_base_recurring_revenue_bridge_required_v2
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C25 medical-AI/aesthetic/dental-device rallies
existing_axis_weakened: null
next_recommended_archetypes: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C22_INSURANCE_RATE_CYCLE_RESERVE, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```
