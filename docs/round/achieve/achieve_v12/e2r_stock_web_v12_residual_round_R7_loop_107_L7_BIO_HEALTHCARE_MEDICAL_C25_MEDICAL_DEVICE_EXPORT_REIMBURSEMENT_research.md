# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R7
selected_loop: 107
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: INSTALLED_BASE_REIMBURSEMENT_RECURRING_REVENUE_HOLDOUT_V107_AESTHETIC_DENTAL_CGM_IMAGING_ROBOT_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  fresh_C25_candidate_shards:
    - direct_raw_web_open: cache_miss_or_not_available_this_turn
    - local_file_library_reused_rows: available
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - medical_device_export_installed_base_recurring_revenue_gate
  - reimbursement_label_vs_commercial_adoption_split
  - dental_device_false_positive_guard
  - CGM_sensor_recurring_revenue_green_block_guard
  - imaging_robot_price_blowoff_4B_4C_split
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` remains a Priority 0 archetype in the no-repeat index. The v12 scheduler maps C23~C25 to `R7 / L7_BIO_HEALTHCARE_MEDICAL`.

This file continues the local C25 sequence after previously observed C25 loop 106, so selected loop is `107`.

This is a **dedupe-aware holdout validation** MD. It does not claim fresh independent stock-web evidence because fresh C25 candidate shards were not recomputed in this execution. The trigger rows below reuse prior current-session / file-library stock-web-derived C25 rows that already contain complete 30D/90D/180D MFE and MAE. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C25 is not a generic healthcare momentum bucket.

C25 should reward device economics only when the device attention becomes adopted, reimbursed, recurring revenue:

```text
medical device export / reimbursement / approval / installed-base attention
→ installation or adoption conversion
→ utilization
→ recurring consumable / sensor / service revenue
→ reimbursement cadence or export reorder
→ gross / OP margin and revision bridge
→ price path validation
```

The false positive is also familiar:

```text
medical device keyword
dental export label
CGM approval / reimbursement label
X-ray detector blowoff
surgical robot theme
diagnostic device spike
```

The machine can be installed before the business is installed. C25 should pay for utilization, reimbursement, recurring revenue and margin, not just a device sitting in the hospital corridor.

This holdout pass validates seven route types:

1. **Aesthetic device installed-base / consumable bridge**
   - Can be positive, but Green requires recurring consumable and margin refresh.

2. **Dental implant / imaging label failure**
   - Dental vocabulary without channel reorder / reimbursement / cash bridge must cap or hard-block.

3. **CGM reimbursement / sensor revenue**
   - A plausible Stage2 route, but no Green until recurring sensor revenue and reimbursement cadence are visible.

4. **Body-composition / optical device installed-base service bridge**
   - Can be positive if installed base, service revenue and margin convert.

5. **Industrial medical imaging / detector blowoff**
   - Price MFE alone routes to local 4B if export order / margin proof is absent.

6. **Surgical robot / procedure volume failure**
   - Device label without procedure volume and installed-base monetization is false-positive.

7. **Digital dentistry / distributor spike**
   - Local 4B only unless distributor inventory, reimbursement, reorder and cash bridge refresh.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 13
  source_archetypes:
    - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C25 holdout validation
    - device export / reimbursement bridge guard
    - local 4B vs hard 4C split
    - recurring revenue and installed-base gate
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local row provenance:

```yaml
reused_price_rows_from_file_library:
  - R7/C25 loop 99
  - R7/C25 loop 102
  - R7/C25 loop 104
  - R7/C25 loop 106
  - R13 C25 guardrail rows
reason:
  - all reused rows already contain complete 30D/90D/180D MFE and MAE
  - fresh raw GitHub shard access returned cache miss or was not recomputable in this execution
  - exact duplicate C25 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_CONSUMABLE_POSITIVE_WITH_GREEN_BLOCK","symbol":"214150","name":"클래시스","trigger_type":"Stage3-Yellow","entry_date":"2024-05-09","entry_price":48500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.32,"MAE_30D_pct":-5.88,"MFE_90D_pct":19.38,"MAE_90D_pct":-15.36,"MFE_180D_pct":29.69,"MAE_180D_pct":-15.36,"peak_180D_price":62900,"calibration_usable":true,"same_entry_group_id":"C25|214150|Stage3-Yellow|2024-05-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Classys C25 row from prior loop 102 / 103 / R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"aesthetic_device_positive_green_block","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214150|Stage3-Yellow|2024-05-09","non_price_bridge":"aesthetic device export, installed base and consumable reorder bridge","score_alignment":"Stage3-Yellow can survive; Green requires installed-base utilization, consumable repeat revenue and margin refresh"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_REIMBURSEMENT_LABEL_WITHOUT_CHANNEL_BRIDGE_HARD_4C","symbol":"145720","name":"덴티움","trigger_type":"Stage3-Yellow","entry_date":"2024-02-29","entry_price":144200,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.98,"MAE_30D_pct":-13.11,"MFE_90D_pct":2.98,"MAE_90D_pct":-28.50,"MFE_180D_pct":2.98,"MAE_180D_pct":-62.55,"peak_180D_price":148500,"calibration_usable":true,"same_entry_group_id":"C25|145720|Stage3-Yellow|2024-02-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Dentium C25 counterexample row from prior loop 102 / 103","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"dental_implant_label_hard_4C","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|145720|Stage3-Yellow|2024-02-29","non_price_bridge":"dental implant export/reimbursement label without channel demand, procedure volume, reimbursement or margin bridge","score_alignment":"hard 4C / false-positive block; low MFE and severe MAE reject Stage3"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMAGING_EXPORT_CAPEX_LABEL_WITHOUT_REORDER_BRIDGE_HARD_4C","symbol":"043150","name":"바텍","trigger_type":"Stage2-Actionable","entry_date":"2024-04-01","entry_price":31300,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.12,"MAE_30D_pct":-7.19,"MFE_90D_pct":1.12,"MAE_90D_pct":-21.73,"MFE_180D_pct":1.12,"MAE_180D_pct":-37.19,"peak_180D_price":31650,"calibration_usable":true,"same_entry_group_id":"C25|043150|Stage2-Actionable|2024-04-01","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Vatech C25 counterexample row from prior loop 102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"dental_imaging_false_positive","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|043150|Stage2-Actionable|2024-04-01","non_price_bridge":"dental imaging export/capex replacement-cycle label without reorder, reimbursement or margin bridge","score_alignment":"hard block if no replacement-cycle acceleration, reimbursement channel or installed-base utilization proof"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DIGITAL_DENTISTRY_DISTRIBUTOR_SPIKE_LOCAL_4B_THEN_FAIL","symbol":"228670","name":"레이","trigger_type":"Stage4B","entry_date":"2024-06-10","entry_price":11120,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":24.10,"MAE_30D_pct":-1.71,"MFE_90D_pct":24.10,"MAE_90D_pct":-31.65,"MFE_180D_pct":24.10,"MAE_180D_pct":-48.65,"peak_180D_price":13800,"calibration_usable":true,"same_entry_group_id":"C25|228670|Stage4B|2024-06-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B_to_fail","reuse_reason":"same Ray local 4B row from prior loop 102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"digital_dentistry_4B_to_fail","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|228670|Stage4B|2024-06-10","non_price_bridge":"digital dentistry distributor spike without durable reimbursement, order or cash bridge","score_alignment":"local 4B only; block Green and require cash/reimbursement/channel refresh"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_EVENT_CAP_POSITIVE_WITH_4B_WATCH","symbol":"335890","name":"비올","trigger_type":"Stage2-Actionable","entry_date":"2024-03-13","entry_price":8480,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":41.86,"MAE_30D_pct":-13.92,"MFE_90D_pct":41.86,"MAE_90D_pct":-13.92,"MFE_180D_pct":41.86,"MAE_180D_pct":-21.82,"peak_180D_price":12030,"calibration_usable":true,"same_entry_group_id":"C25|335890|Stage2-Actionable|2024-03-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_4B_watch","reuse_reason":"same ViOL C25 row from prior loop 99","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"aesthetic_device_positive_with_4B_watch","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|335890|Stage2-Actionable|2024-03-13","non_price_bridge":"aesthetic device export / installed-base vocabulary produced strong early MFE but required margin/consumable continuation","score_alignment":"Stage2 can survive; 180D MAE requires 4B watch unless margin and consumable revenue persist"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_MATERIAL_EXPORT_REORDER_MARGIN_POSITIVE","symbol":"059210","name":"메타바이오메드","trigger_type":"Stage2-Actionable","entry_date":"2024-06-17","entry_price":4100,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":31.00,"MAE_30D_pct":-7.60,"MFE_90D_pct":53.40,"MAE_90D_pct":-12.70,"MFE_180D_pct":61.20,"MAE_180D_pct":-15.40,"peak_180D_price":6610,"calibration_usable":true,"same_entry_group_id":"C25|059210|Stage2-Actionable|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Meta Biomed C25 row from prior loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"dental_material_export_positive","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|059210|Stage2-Actionable|2024-06-17","non_price_bridge":"dental material export repeat order and margin revision bridge","score_alignment":"Stage2-Actionable can survive; Green requires margin/revision refresh"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"BODY_COMPOSITION_INSTALLED_BASE_SERVICE_REVENUE_POSITIVE","symbol":"041830","name":"인바디","trigger_type":"Stage3-Yellow","entry_date":"2024-05-22","entry_price":24600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.70,"MAE_30D_pct":-5.50,"MFE_90D_pct":32.90,"MAE_90D_pct":-10.40,"MFE_180D_pct":45.80,"MAE_180D_pct":-12.30,"peak_180D_price":35870,"calibration_usable":true,"same_entry_group_id":"C25|041830|Stage3-Yellow|2024-05-22","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same InBody C25 row from prior loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"installed_base_service_revenue_positive","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|041830|Stage3-Yellow|2024-05-22","non_price_bridge":"installed-base service revenue and body-composition device export bridge","score_alignment":"Stage3-Yellow can survive if installed-base service revenue and margin bridge are confirmed"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"INDUSTRIAL_MEDICAL_IMAGING_ORDER_MARGIN_FOLLOWTHROUGH_LOCAL_4B","symbol":"100120","name":"뷰웍스","trigger_type":"Stage2-Actionable","entry_date":"2024-06-12","entry_price":28750,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":18.10,"MAE_30D_pct":-8.00,"MFE_90D_pct":26.40,"MAE_90D_pct":-18.20,"MFE_180D_pct":26.40,"MAE_180D_pct":-27.90,"peak_180D_price":36340,"calibration_usable":true,"same_entry_group_id":"C25|100120|Stage2-Actionable|2024-06-12","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_mixed_positive_4B","reuse_reason":"same Vieworks C25 row from prior loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"medical_imaging_local_4B","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|100120|Stage2-Actionable|2024-06-12","non_price_bridge":"industrial medical imaging export/order margin bridge needing follow-through","score_alignment":"Stage2 can open; 180D MAE blocks Green until order and margin bridge refresh"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"OPTICAL_DEVICE_EXPORT_REORDER_MARGIN_CONFIRMATION_POSITIVE","symbol":"065510","name":"휴비츠","trigger_type":"Stage2-Actionable","entry_date":"2024-04-29","entry_price":15320,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":11.10,"MAE_30D_pct":-6.80,"MFE_90D_pct":38.20,"MAE_90D_pct":-14.50,"MFE_180D_pct":38.20,"MAE_180D_pct":-18.00,"peak_180D_price":21170,"calibration_usable":true,"same_entry_group_id":"C25|065510|Stage2-Actionable|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Huvitz C25 row from prior loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"optical_device_export_positive","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|065510|Stage2-Actionable|2024-04-29","non_price_bridge":"optical/ophthalmic device export reorder and margin confirmation bridge","score_alignment":"Stage2 can survive; Green requires export reorder and margin confirmation"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_REIMBURSEMENT_SENSOR_RECURRING_REVENUE_MIXED_POSITIVE","symbol":"099190","name":"아이센스","trigger_type":"Stage2-Actionable","entry_date":"2024-02-01","entry_price":21950,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":22.80,"MAE_30D_pct":-7.10,"MFE_90D_pct":34.60,"MAE_90D_pct":-16.20,"MFE_180D_pct":42.10,"MAE_180D_pct":-19.40,"peak_180D_price":31190,"calibration_usable":true,"same_entry_group_id":"C25|099190|Stage2-Actionable|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_mixed_positive","reuse_reason":"same i-SENS C25 row from prior loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"CGM_reimbursement_mixed_positive","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|099190|Stage2-Actionable|2024-02-01","non_price_bridge":"CGM reimbursement and recurring sensor revenue bridge needing commercial confirmation","score_alignment":"Stage2 can survive; no Green without reimbursement cadence and recurring sensor revenue proof"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"XRAY_DETECTOR_PRICE_BLOWOFF_EXPORT_MARGIN_LOCAL_4B","symbol":"214680","name":"디알텍","trigger_type":"Stage4B","entry_date":"2024-02-26","entry_price":4860,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":58.60,"MAE_30D_pct":-9.70,"MFE_90D_pct":72.40,"MAE_90D_pct":-24.50,"MFE_180D_pct":72.40,"MAE_180D_pct":-46.30,"peak_180D_price":8380,"calibration_usable":true,"same_entry_group_id":"C25|214680|Stage4B|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_price_blowoff_4B","reuse_reason":"same DRTech C25 row from prior loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"xray_detector_blowoff_4B","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214680|Stage4B|2024-02-26","non_price_bridge":"X-ray detector price blowoff needing export order and margin bridge","score_alignment":"local 4B only; block Green until export order and margin evidence appears"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"SURGICAL_ROBOT_LABEL_WITHOUT_PROCEDURE_VOLUME_HARD_4C","symbol":"060280","name":"큐렉소","trigger_type":"Stage2","entry_date":"2024-03-25","entry_price":15460,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.80,"MAE_30D_pct":-12.20,"MFE_90D_pct":9.40,"MAE_90D_pct":-28.00,"MFE_180D_pct":9.40,"MAE_180D_pct":-41.60,"peak_180D_price":16910,"calibration_usable":true,"same_entry_group_id":"C25|060280|Stage2|2024-03-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same CUREXO C25 row from prior loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"surgical_robot_label_hard_4C","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|060280|Stage2|2024-03-25","non_price_bridge":"surgical robot label without installed-base procedure volume and service revenue bridge","score_alignment":"hard 4C / false-positive block; low MFE and severe MAE reject device-theme Stage2"}
{"row_type":"trigger","selected_round":"R7","selected_loop":107,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_KEYWORD_WITHOUT_REIMBURSEMENT_REPEAT_SALES_HARD_4C","symbol":"302550","name":"리메드","trigger_type":"Stage2","entry_date":"2024-03-21","entry_price":8200,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.90,"MAE_30D_pct":-16.50,"MFE_90D_pct":15.60,"MAE_90D_pct":-30.00,"MFE_180D_pct":15.60,"MAE_180D_pct":-44.90,"peak_180D_price":9480,"calibration_usable":true,"same_entry_group_id":"C25|302550|Stage2|2024-03-21","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Remed C25 row from prior loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"device_keyword_hard_4C","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|302550|Stage2|2024-03-21","non_price_bridge":"medical-device keyword without reimbursement, repeat sales or margin bridge","score_alignment":"hard 4C; device keyword and weak MFE with deep MAE fail C25"}
```

---

## 5. Case analysis

### 5.1 Positive or constructive bridge rows

```yaml
positive_or_constructive:
  - 214150: aesthetic device export / installed base / consumable bridge.
  - 335890: aesthetic device export event with strong MFE but 4B watch.
  - 059210: dental material export repeat order / margin revision.
  - 041830: installed-base service revenue bridge.
  - 065510: optical device export reorder bridge.
  - 099190: CGM reimbursement / recurring sensor revenue, but no Green without recurring proof.
```

These rows show that C25 can work. The score should not blanket-block medical devices. The positive path needs a bridge that turns installed machines into recurring revenue.

### 5.2 Local 4B rows

```yaml
local_4B_rows:
  - 228670: digital dentistry distributor spike.
  - 100120: industrial medical imaging, order/margin follow-through required.
  - 214680: X-ray detector blowoff.
```

These are inspection-bay rows. They can show price MFE, but 90D/180D MAE says they should not become Green without export order, installed-base, reimbursement, procedure volume or margin refresh.

### 5.3 Hard failure / false positive rows

```yaml
hard_4C_or_false_positive:
  - 145720: dental implant export/reimbursement label without channel bridge.
  - 043150: dental imaging export/capex label without reorder bridge.
  - 060280: surgical robot label without procedure volume.
  - 302550: medical-device keyword without reimbursement or repeat sales.
```

These rows are not just “late.” The bridge itself was missing.

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 13
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 13
calibration_usable_trigger_count: 13
positive_case_count: 6
counterexample_count: 7
local_4B_watch_count: 4
hard_4C_or_false_positive_count: 4
current_profile_error_count: 9
source_proxy_only_count: 13
evidence_url_pending_count: 13
batch_reverification_required_count: 13
diversity_score_summary: "aesthetic device, dental implant, dental imaging, digital dentistry, body composition, industrial imaging, optical devices, CGM, X-ray detector, surgical robot, and device keyword rows covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C25 lesson |
|---|---:|---:|---:|---|
| 214150 | aesthetic positive | +19.38 / -15.36 | +29.69 / -15.36 | installed-base/consumable bridge |
| 145720 | dental hard 4C | +2.98 / -28.50 | +2.98 / -62.55 | channel bridge missing |
| 043150 | dental imaging hard 4C | +1.12 / -21.73 | +1.12 / -37.19 | capex label fails |
| 228670 | digital dentistry 4B | +24.10 / -31.65 | +24.10 / -48.65 | distributor spike fails without cash bridge |
| 335890 | aesthetic 4B watch | +41.86 / -13.92 | +41.86 / -21.82 | MFE works but margin refresh needed |
| 059210 | dental material positive | +53.40 / -12.70 | +61.20 / -15.40 | repeat order / margin bridge |
| 041830 | installed-base positive | +32.90 / -10.40 | +45.80 / -12.30 | service revenue bridge |
| 100120 | imaging mixed 4B | +26.40 / -18.20 | +26.40 / -27.90 | order/margin follow-through required |
| 065510 | optical device positive | +38.20 / -14.50 | +38.20 / -18.00 | reorder/margin bridge |
| 099190 | CGM mixed positive | +34.60 / -16.20 | +42.10 / -19.40 | recurring sensor revenue needed |
| 214680 | detector 4B | +72.40 / -24.50 | +72.40 / -46.30 | price blowoff without export order proof |
| 060280 | robot hard 4C | +9.40 / -28.00 | +9.40 / -41.60 | procedure volume absent |
| 302550 | keyword hard 4C | +15.60 / -30.00 | +15.60 / -44.90 | repeat sales absent |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"214150","raw_device_export":5,"raw_installed_base":5,"raw_reimbursement_or_consumable":4,"raw_margin_revision":3,"raw_price_validation":3,"raw_MAE_risk":2,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage3Yellow_GreenBlocked"}
{"row_type":"score_simulation","symbol":"145720","raw_device_export":3,"raw_installed_base":1,"raw_reimbursement_or_consumable":0,"raw_margin_revision":0,"raw_price_validation":0,"raw_MAE_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_DentalLabelNoBridge"}
{"row_type":"score_simulation","symbol":"043150","raw_device_export":2,"raw_installed_base":1,"raw_reimbursement_or_consumable":0,"raw_margin_revision":0,"raw_price_validation":0,"raw_MAE_risk":4,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_DentalImagingNoReorder"}
{"row_type":"score_simulation","symbol":"228670","raw_device_export":2,"raw_installed_base":1,"raw_reimbursement_or_consumable":0,"raw_margin_revision":0,"raw_price_validation":1,"raw_MAE_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Local4BThenFail"}
{"row_type":"score_simulation","symbol":"335890","raw_device_export":4,"raw_installed_base":3,"raw_reimbursement_or_consumable":2,"raw_margin_revision":2,"raw_price_validation":4,"raw_MAE_risk":3,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2With4BWatch"}
{"row_type":"score_simulation","symbol":"059210","raw_device_export":4,"raw_installed_base":3,"raw_reimbursement_or_consumable":3,"raw_margin_revision":4,"raw_price_validation":4,"raw_MAE_risk":2,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_DentalMaterialExport"}
{"row_type":"score_simulation","symbol":"041830","raw_device_export":3,"raw_installed_base":5,"raw_reimbursement_or_consumable":3,"raw_margin_revision":4,"raw_price_validation":4,"raw_MAE_risk":2,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage3Yellow_InstalledBaseServiceRevenue"}
{"row_type":"score_simulation","symbol":"100120","raw_device_export":3,"raw_installed_base":2,"raw_reimbursement_or_consumable":1,"raw_margin_revision":2,"raw_price_validation":3,"raw_MAE_risk":4,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_OrderMarginRefresh"}
{"row_type":"score_simulation","symbol":"065510","raw_device_export":4,"raw_installed_base":3,"raw_reimbursement_or_consumable":2,"raw_margin_revision":3,"raw_price_validation":4,"raw_MAE_risk":2,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OpticalDeviceExport"}
{"row_type":"score_simulation","symbol":"099190","raw_device_export":3,"raw_installed_base":3,"raw_reimbursement_or_consumable":4,"raw_margin_revision":2,"raw_price_validation":4,"raw_MAE_risk":3,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2_CGMRevenueRefresh"}
{"row_type":"score_simulation","symbol":"214680","raw_device_export":2,"raw_installed_base":1,"raw_reimbursement_or_consumable":0,"raw_margin_revision":1,"raw_price_validation":3,"raw_MAE_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Local4B_PriceBlowoff"}
{"row_type":"score_simulation","symbol":"060280","raw_device_export":1,"raw_installed_base":0,"raw_reimbursement_or_consumable":0,"raw_margin_revision":0,"raw_price_validation":0,"raw_MAE_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_SurgicalRobotLabel"}
{"row_type":"score_simulation","symbol":"302550","raw_device_export":1,"raw_installed_base":0,"raw_reimbursement_or_consumable":0,"raw_margin_revision":0,"raw_price_validation":0,"raw_MAE_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_DeviceKeywordNoBridge"}
```

---

## 8. Current calibrated profile stress test

The C25 installed-base / reimbursement / recurring-revenue gate held:

```text
installed base + consumable / service / recurring revenue bridge
→ Stage2 or Stage3-Yellow can survive

high MFE but high 180D MAE
→ local 4B watch, no Green

dental label without channel/reimbursement bridge
→ hard 4C / false-positive block

CGM approval/reimbursement label
→ Stage2 only until recurring sensor revenue and reimbursement cadence confirm

X-ray / imaging / robot device keyword
→ 4B or 4C depending on order/procedure/margin bridge

source_proxy_only row
→ dedupe / holdout only, no new weight delta
```

### Rule candidate retained, not newly proposed

```text
C25_INSTALLED_BASE_REIMBURSEMENT_RECURRING_REVENUE_GATE_V107_HELD_OUT

if C25
and medical_device_export_reimbursement_or_approval_label == true
and installed_base_utilization_recurring_revenue_reimbursement_channel_or_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C25
and installed_base_or_recurring_revenue_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -20:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_margin_or_recurring_revenue_refresh = true
```

```text
if C25
and device_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C25
and MFE_90D_pct >= +20
and MAE_90D_pct <= -25
and recurring_revenue_or_reimbursement_bridge == false:
    route = local_4B_watch_or_Stage2_false_positive_block
```

```text
if C25
and source_proxy_only == true:
    do_not_create_new_weight_delta = true
    require_batch_reverification = true
```

---

## 9. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 13
    avg_MFE_90D_pct: 27.35
    avg_MAE_90D_pct: -22.63
    false_positive_risk: high_if_device_labels_are_left_actionable
    verdict: adequate_only_with_C25_recurring_revenue_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for medical-device labels and reimbursement keywords
    eligible_trigger_count: 13
    false_positive_rate: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L7 medical-device rows require installed-base, utilization, reimbursement and margin bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C25 requires recurring revenue or export/reimbursement bridge, not device keyword
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: dental/robot/device-keyword rows without bridge route to 4C or local 4B
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 10. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | INSTALLED_BASE_REIMBURSEMENT_RECURRING_REVENUE_HOLDOUT_V107 | 6 | 7 | 4 | 4 | 0 | 13 | 13 | 0 | 9 | false | false | 24 |

---

## 11. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 13
calibration_usable_trigger_count: 13
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 13
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 12. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 13
new_symbol_count: 0
new_trigger_family_count: 0
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C25_installed_base_reimbursement_recurring_revenue_gate
  - source_proxy_batch_reverification_gate
residual_error_types_found:
  - dental_device_label_without_channel_bridge
  - medical_device_keyword_without_repeat_sales
  - high_MFE_price_blowoff_without_export_order_margin
  - CGM_reimbursement_without_recurring_sensor_revenue_refresh
  - imaging_robot_keyword_without_procedure_volume
new_axis_proposed: null
existing_axis_strengthened:
  - C25_INSTALLED_BASE_REIMBURSEMENT_RECURRING_REVENUE_GATE_V107_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after fresh C25 shards were unavailable in this execution
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"107","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":0,"reused_case_count":13,"new_symbol_count":0,"new_trigger_family_count":0,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C25_installed_base_reimbursement_recurring_revenue_gate","source_proxy_batch_reverification_gate"],"residual_error_types_found":["dental_device_label_without_channel_bridge","medical_device_keyword_without_repeat_sales","high_MFE_price_blowoff_without_export_order_margin","CGM_reimbursement_without_recurring_sensor_revenue_refresh","imaging_robot_keyword_without_procedure_volume"],"loop_contribution_label":"duplicate_low_value_loop","do_not_propose_new_weight_delta":true}
```

---

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R7/C25 loop 107 as holdout validation only. Batch it with C25 loops 99~106 and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C25 installed-base / reimbursement / recurring-revenue bridge gate and source-proxy batch reverification guard. Do not create a new weight delta from this loop because no new independent case was added. Future research should reprice fresh candidates directly from stock-web shards when raw access is available rather than reusing this holdout set.
```

---

## 14. Next research state

```yaml
completed_round: R7
completed_loop: 107
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C24_BIO_TRIAL_DATA_EVENT_RISK
```
