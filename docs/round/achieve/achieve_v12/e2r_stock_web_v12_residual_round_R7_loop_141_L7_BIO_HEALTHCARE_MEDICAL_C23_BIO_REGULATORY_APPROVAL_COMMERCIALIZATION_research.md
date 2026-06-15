# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R7
selected_loop: 141
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: APPROVAL_TO_COMMERCIAL_ECONOMICS_HOLDOUT_V141_COMMERCIALIZED_DRUG_LAUNCH_LABEL_BINARY_FAILURE_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 326030/2024: reused_from_prior_local_C23_loop_140_commercialized_drug_row
    - 006280/2024: reused_from_prior_local_C23_loop_140_FDA_launch_4B_row
    - 170900/2024: reused_from_prior_local_C23_loop_140_approval_label_cap_row
    - 000100/2024: reused_from_prior_local_C23_loop_140_commercial_bridge_row
    - 195940/2024: reused_from_prior_local_C23_loop_140_commercialized_drug_row
    - 028300/2024: reused_from_prior_local_C23_loop_140_binary_failure_row
    - 145020/2024: reused_from_prior_local_C23_loop_140_post_approval_4B_row
    - 068270/2024: not_recomputed_this_turn_future_biosimilar_commercialization_candidate
    - 196170/2024: not_recomputed_this_turn_future_platform_approval_commercialization_candidate
    - 128940/2024: not_recomputed_this_turn_future_drug_launch_reimbursement_candidate
    - 141080/2024: not_recomputed_this_turn_future_ADC_approval_commercialization_candidate
    - 950160/2024: not_recomputed_this_turn_future_regulatory_approval_commercialization_candidate
    - 003850/2024: not_recomputed_this_turn_future_commercial_drug_candidate
    - 185750/2024: not_recomputed_this_turn_future_bio_commercialization_candidate
    - 214450/2024: not_recomputed_this_turn_C25_medical_device_boundary
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - approval_to_commercial_economics_gate
  - commercialized_drug_positive_escape_hatch
  - FDA_approval_launch_local_4B_guard
  - approval_label_without_listed_company_economics_false_positive_guard
  - binary_regulatory_failure_hard_4C_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` remains a Priority 0 archetype in the no-repeat index. The v12 scheduler maps C23~C25 to `R7 / L7_BIO_HEALTHCARE_MEDICAL`.

This file continues the local C23 sequence after `R7/C23 loop 140`; selected loop is therefore `141`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct fresh C23 approval-to-commercialization candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C23/R13 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

```yaml
loop_141_note:
  independence_status: duplicate_holdout_only
  fresh_reprice_status: not_recomputed_this_execution
  reason: C23 remains under-covered, but this run reuses prior C23/R13 boundary rows and must not create a new weight delta.
```


C23 should not treat `approval` as the finish line.

C23 should reward regulatory success only when it becomes commercial economics for the listed company:

```text
regulatory approval / label expansion / commercialization event
→ launch
→ prescriptions / patient uptake / procedure or order conversion
→ reimbursement / market access
→ royalty / direct sales / partner economics
→ margin / profit / FCF / EPS revision
→ price path validation
```

In bio/pharma, approval is the key. Commercialization is the cash register. A key that does not open the register should not become Stage3-Green.

The recurring false-positive family is:

```text
approval headline
biosimilar approval label
pipeline/regulatory vocabulary
binary regulatory expectation
post-approval peak-zone enthusiasm
commercial-stage label without incremental economics
```

This holdout pass validates six route types:

1. **Approved commercial drug with visible revenue/profit bridge**
   - Keep Stage2 and allow Stage3-Yellow path when sales/profit bridge remains refreshed.

2. **FDA approval to launch bridge**
   - Approval-to-launch can open Stage2.
   - Green waits for quarterly launch revenue, channel uptake, reimbursement and margin cadence.

3. **Approval label without listed-company economics**
   - Block or cap Stage2 when direct sales, royalty, launch timing or margin capture is not visible.

4. **Biosimilar / partner optionality**
   - Explosive MFE is possible, but Green requires launch/reimbursement/channel revenue bridge.

5. **Binary regulatory failure**
   - A pre-event approval expectation should hard-block after regulatory thesis break.

6. **Post-approval peak-zone local 4B**
   - If most of the event is already priced and follow-through fails, route to local 4B rather than Green.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 7
  source_archetypes:
    - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C23 holdout validation
    - approval-to-commercial-economics gate
    - local 4B vs hard 4C split
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

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R7/C23 loop 137
  - R7/C23 loop 138
  - R7/C23 loop 139
  - R7/C23 loop 140
  - R7/C23 loop 99
  - R7/C23 loop 100
  - R13 accounting-trust loop 9
  - R13 Stage2 false-positive loop 8
  - R13 high-MAE guardrail loops 6/14/15
  - R13 4B/4C redteam loops 101/15
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C23 approval-to-commercialization candidate shards were not recomputed in this execution
  - exact duplicate C23 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R7","selected_loop":141,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVED_DRUG_COMMERCIAL_REVENUE_PROFIT_BRIDGE_POSITIVE_CONTROL","symbol":"326030","name":"SK바이오팜","trigger_type":"Stage2-Actionable","entry_date":"2024-08-12","entry_price":98800,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.95,"MAE_30D_pct":-5.87,"MFE_90D_pct":31.58,"MAE_90D_pct":-5.87,"MFE_180D_pct":31.58,"MAE_180D_pct":-5.87,"forward_high_30d":119500,"forward_low_30d":93000,"forward_high_90d":130000,"forward_low_90d":93000,"forward_high_180d":130000,"forward_low_180d":93000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C23|326030|Stage2-Actionable|2024-08-12","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same SK Biopharm commercialized-drug bridge row from C23 loop 138 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":true,"evidence_url_pending":true,"case_role":"commercialized_drug_positive_control","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|326030|Stage2-Actionable|2024-08-12","non_price_bridge":"approved-drug commercialization with visible sales/profit bridge","score_alignment":"keep Stage2-Actionable; allow Stage3-Yellow path when revenue/profit bridge remains refreshed"}
{"row_type":"trigger","selected_round":"R7","selected_loop":141,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_TO_US_LAUNCH_BRIDGE_LOCAL_4B_UNTIL_REVENUE_CADENCE","symbol":"006280","name":"녹십자","trigger_type":"Stage2-Actionable","entry_date":"2024-07-09","entry_price":124900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.71,"MAE_30D_pct":-4.56,"MFE_90D_pct":45.56,"MAE_90D_pct":-4.56,"MFE_180D_pct":45.56,"MAE_180D_pct":-10.49,"forward_high_30d":167000,"forward_low_30d":119200,"forward_high_90d":181800,"forward_low_90d":119200,"forward_high_180d":181800,"forward_low_180d":111800,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C23|006280|Stage2-Actionable|2024-07-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_launch_4B","reuse_reason":"same Green Cross FDA approval-to-launch row from C23 loops 103/137/138 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":true,"evidence_url_pending":true,"case_role":"FDA_approval_launch_local_4B","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|006280|Stage2-Actionable|2024-07-09","non_price_bridge":"FDA approval and US launch path, but launch revenue cadence still needed","score_alignment":"Stage2 opens; block Stage3-Green until quarterly launch revenue, channel uptake and margin evidence confirm"}
{"row_type":"trigger","selected_round":"R7","selected_loop":141,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_APPROVAL_LABEL_WITHOUT_LISTED_COMPANY_ECONOMICS_FALSE_POSITIVE","symbol":"170900","name":"동아에스티","trigger_type":"Stage2-FalsePositive","entry_date":"2024-10-11","entry_price":76400,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.63,"MAE_30D_pct":-20.16,"MFE_90D_pct":5.63,"MAE_90D_pct":-36.32,"MFE_180D_pct":5.63,"MAE_180D_pct":-46.47,"forward_high_30d":80700,"forward_low_30d":61000,"forward_high_90d":80700,"forward_low_90d":48650,"forward_high_180d":80700,"forward_low_180d":40900,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C23|170900|Stage2-FalsePositive|2024-10-11","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_counterexample","reuse_reason":"same Dong-A ST biosimilar approval-label false-positive row from C23 loop 138 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":true,"evidence_url_pending":true,"case_role":"approval_label_false_positive","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|170900|Stage2-FalsePositive|2024-10-11","non_price_bridge":"biosimilar approval label without visible direct sales, royalty, launch timing or listed-company margin bridge","score_alignment":"block Stage2-Actionable; require listed-company economics before reopen"}
{"row_type":"trigger","selected_round":"R7","selected_loop":141,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_GLOBAL_PARTNER_ROYALTY_COMMERCIALIZATION_POSITIVE_CONTROL","symbol":"000100","name":"유한양행","trigger_type":"Stage2-Actionable","entry_date":"2024-08-20","entry_price":94000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":70.53,"MAE_30D_pct":-2.66,"MFE_90D_pct":77.55,"MAE_90D_pct":-2.66,"MFE_180D_pct":77.55,"MAE_180D_pct":-2.66,"forward_high_30d":166900,"forward_low_30d":91500,"forward_high_90d":166900,"forward_low_90d":91500,"forward_high_180d":166900,"forward_low_180d":91500,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C23|000100|Stage2-Actionable|2024-08-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Yuhan FDA approval/global partner commercialization row from prior C23/R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":true,"evidence_url_pending":true,"case_role":"FDA_partner_royalty_positive_control","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|000100|Stage2-Actionable|2024-08-20","non_price_bridge":"FDA approval plus global partner commercialization and royalty/milestone route","score_alignment":"keep Stage2; Stage3 path allowed only with revenue, royalty and margin bridge refresh"}
{"row_type":"trigger","selected_round":"R7","selected_loop":141,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"GI_DRUG_COMMERCIALIZATION_REIMBURSEMENT_CHANNEL_BRIDGE_WATCH","symbol":"195940","name":"HK이노엔","trigger_type":"Stage2-Watch","entry_date":"2024-08-28","entry_price":44100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.91,"MAE_30D_pct":-0.91,"MFE_90D_pct":17.91,"MAE_90D_pct":-0.91,"MFE_180D_pct":17.91,"MAE_180D_pct":-7.48,"forward_high_30d":52000,"forward_low_30d":43700,"forward_high_90d":52000,"forward_low_90d":43700,"forward_high_180d":52000,"forward_low_180d":40800,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C23|195940|Stage2-Watch|2024-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_buffer_watch","reuse_reason":"same HK inno.N GI-drug commercialization/reimbursement row from prior C23 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":true,"evidence_url_pending":true,"case_role":"commercialization_buffer_watch","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|195940|Stage2-Watch|2024-08-28","non_price_bridge":"GI drug commercialization and reimbursement/channel bridge with controlled MAE but moderate MFE","score_alignment":"Stage2-Watch; require channel, prescription and OPM/FCF refresh before Actionable or Green"}
{"row_type":"trigger","selected_round":"R7","selected_loop":141,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BINARY_REGULATORY_APPROVAL_EXPECTATION_FAILURE_HARD_4C","symbol":"028300","name":"HLB","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":95800,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.59,"MAE_30D_pct":-52.87,"MFE_90D_pct":11.59,"MAE_90D_pct":-52.87,"MFE_180D_pct":11.59,"MAE_180D_pct":-52.87,"forward_high_30d":106900,"forward_low_30d":45150,"forward_high_90d":106900,"forward_low_90d":45150,"forward_high_180d":106900,"forward_low_180d":45150,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C23|028300|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_binary_failure","reuse_reason":"same HLB binary regulatory approval expectation failure row from C23/R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":true,"evidence_url_pending":true,"case_role":"binary_regulatory_failure_hard_4C","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|028300|Stage4C|2024-05-16","non_price_bridge":"approval expectation price strength failed before commercialization bridge; regulatory thesis broke","score_alignment":"hard 4C; approval expectation must not be learned as commercialization success"}
{"row_type":"trigger","selected_round":"R7","selected_loop":141,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"POST_APPROVAL_PEAK_ZONE_VALUATION_OVERHEAT_LOCAL_4B","symbol":"145020","name":"휴젤","trigger_type":"Stage4B","entry_date":"2024-11-06","entry_price":321000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.56,"MAE_30D_pct":-26.17,"MFE_90D_pct":1.56,"MAE_90D_pct":-26.17,"MFE_180D_pct":1.56,"MAE_180D_pct":-26.17,"forward_high_30d":326000,"forward_low_30d":237000,"forward_high_90d":326000,"forward_low_90d":237000,"forward_high_180d":326000,"forward_low_180d":237000,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C23|145020|Stage4B|2024-11-06","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_post_approval_4B","reuse_reason":"same Hugel post-approval peak-zone 4B overlay from R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"source_proxy_only":true,"evidence_url_pending":true,"case_role":"post_approval_peak_zone_local_4B","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|145020|Stage4B|2024-11-06","non_price_bridge":"post-approval rerating reached peak zone; launch/valuation enthusiasm without fresh revenue/margin follow-through","score_alignment":"local 4B; do not treat post-approval peak-zone label as new Green"}
```

---

## 5. Case analysis

### 5.1 SK Biopharm / 326030 — commercialized-drug positive-control

```yaml
entry_price: 98800
90D_MFE_MAE: +31.58 / -5.87
180D_MFE_MAE: +31.58 / -5.87
route: KeepStage2
```

The approval has already become a commercialized-drug revenue/profit bridge. This is the C23 row that prevents the rule from over-blocking. It is not merely an approval headline; sales/profit traffic is already crossing the bridge.

### 5.2 Green Cross / 006280 — FDA approval-to-launch local 4B

```yaml
entry_price: 124900
90D_MFE_MAE: +45.56 / -4.56
180D_MFE_MAE: +45.56 / -10.49
route: Stage2-Actionable / local 4B until revenue cadence
```

The FDA approval-to-launch bridge is real. But Green requires launch revenue cadence, reimbursement/channel uptake and margin evidence. Approval is the passport; quarterly revenue is the entry stamp.

### 5.3 Dong-A ST / 170900 — approval label false positive

```yaml
entry_price: 76400
90D_MFE_MAE: +5.63 / -36.32
180D_MFE_MAE: +5.63 / -46.47
route: Stage2-FalsePositive
```

The regulatory label may be real, but listed-company economics were not visible. This is the guardrail row: no direct sales, royalty, launch timing or margin bridge means no Actionable C23 credit.

### 5.4 Yuhan / 000100 — FDA approval plus partner commercialization

```yaml
entry_price: 94000
90D_MFE_MAE: +77.55 / -2.66
180D_MFE_MAE: +77.55 / -2.66
route: Stage2-Actionable positive-control
```

This row validates the positive side of C23. Partner commercialization and royalty/milestone route can be learned, but only when the economics are visible enough to monitor.

### 5.5 HK inno.N / 195940 — commercialization buffer watch

```yaml
entry_price: 44100
90D_MFE_MAE: +17.91 / -0.91
180D_MFE_MAE: +17.91 / -7.48
route: Stage2-Watch
```

This is not a hard block. It is a buffer: GI drug commercialization/reimbursement path can be constructive, but channel, prescription and OPM/FCF refresh are needed before promotion.

### 5.6 HLB / 028300 — binary regulatory failure

```yaml
entry_price: 95800
90D_MFE_MAE: +11.59 / -52.87
180D_MFE_MAE: +11.59 / -52.87
route: Stage4C
```

Approval expectation is not approval. After binary regulatory failure, C23 should treat the row as hard 4C and require a new evidence family before reopening.

### 5.7 Hugel / 145020 — post-approval peak-zone 4B

```yaml
entry_price: 321000
90D_MFE_MAE: +1.56 / -26.17
180D_MFE_MAE: +1.56 / -26.17
route: Stage4B
```

A post-approval rerating can reach the peak zone before fresh revenue/margin proof appears. That is 4B inspection territory, not a new Green.

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 7
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 3
counterexample_count: 4
local_4B_watch_count: 3
hard_4C_or_false_positive_count: 2
current_profile_error_count: 5
source_proxy_only_count: 7
evidence_url_pending_count: 7
diversity_score_summary: "commercialized-drug positive, FDA launch bridge, approval-label false positive, partner-commercialization positive, commercialization buffer watch, binary failure, and post-approval peak-zone 4B covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C23 lesson |
|---|---:|---:|---:|---|
| 326030 | commercialized-drug positive | +31.58 / -5.87 | +31.58 / -5.87 | revenue/profit bridge validates |
| 006280 | launch bridge 4B | +45.56 / -4.56 | +45.56 / -10.49 | launch revenue cadence needed |
| 170900 | approval-label false positive | +5.63 / -36.32 | +5.63 / -46.47 | label lacks listed-company economics |
| 000100 | partner commercialization positive | +77.55 / -2.66 | +77.55 / -2.66 | approval plus partner economics works |
| 195940 | commercialization buffer watch | +17.91 / -0.91 | +17.91 / -7.48 | channel/OPM refresh required |
| 028300 | binary failure 4C | +11.59 / -52.87 | +11.59 / -52.87 | expectation failed before bridge |
| 145020 | post-approval 4B | +1.56 / -26.17 | +1.56 / -26.17 | peak-zone enthusiasm needs proof |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"326030","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_regulatory_event":3,"raw_commercial_revenue_bridge":5,"raw_reimbursement_market_access":3,"raw_royalty_or_direct_sales":4,"raw_margin_profit_bridge":4,"raw_validation":4,"raw_label_only_risk":0,"event_binary_risk_penalty":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control","MFE_90D_pct":31.58,"MAE_90D_pct":-5.87,"score_return_alignment_label":"commercialized_drug_revenue_profit_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"006280","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_regulatory_event":5,"raw_commercial_revenue_bridge":3,"raw_reimbursement_market_access":3,"raw_royalty_or_direct_sales":3,"raw_margin_profit_bridge":2,"raw_validation":4,"raw_label_only_risk":1,"event_binary_risk_penalty":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-local-4B-watch","MFE_90D_pct":45.56,"MAE_90D_pct":-4.56,"score_return_alignment_label":"FDA_approval_launch_bridge_local_4B","current_profile_verdict":"current_profile_correct_if_Green_blocked_until_revenue"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"170900","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_regulatory_event":4,"raw_commercial_revenue_bridge":1,"raw_reimbursement_market_access":1,"raw_royalty_or_direct_sales":1,"raw_margin_profit_bridge":1,"raw_validation":0,"raw_label_only_risk":4,"event_binary_risk_penalty":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-approval-label","MFE_90D_pct":5.63,"MAE_90D_pct":-36.32,"score_return_alignment_label":"approval_label_without_listed_company_economics","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_regulatory_event":5,"raw_commercial_revenue_bridge":5,"raw_reimbursement_market_access":4,"raw_royalty_or_direct_sales":5,"raw_margin_profit_bridge":4,"raw_validation":5,"raw_label_only_risk":0,"event_binary_risk_penalty":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-partner-commercialization-positive","MFE_90D_pct":77.55,"MAE_90D_pct":-2.66,"score_return_alignment_label":"FDA_partner_royalty_positive_control","current_profile_verdict":"current_profile_correct_if_economics_refresh"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"195940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_regulatory_event":3,"raw_commercial_revenue_bridge":3,"raw_reimbursement_market_access":3,"raw_royalty_or_direct_sales":2,"raw_margin_profit_bridge":2,"raw_validation":2,"raw_label_only_risk":1,"event_binary_risk_penalty":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2-Watch-commercialization-buffer","MFE_90D_pct":17.91,"MAE_90D_pct":-0.91,"score_return_alignment_label":"commercialization_buffer_watch","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_regulatory_event":0,"raw_commercial_revenue_bridge":0,"raw_reimbursement_market_access":0,"raw_royalty_or_direct_sales":0,"raw_margin_profit_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"event_binary_risk_penalty":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage4C_binary_regulatory_failure","MFE_90D_pct":11.59,"MAE_90D_pct":-52.87,"score_return_alignment_label":"binary_regulatory_failure_hard_4C","current_profile_verdict":"current_profile_false_positive_if_approval_expectation_scored"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_regulatory_event":4,"raw_commercial_revenue_bridge":2,"raw_reimbursement_market_access":2,"raw_royalty_or_direct_sales":2,"raw_margin_profit_bridge":1,"raw_validation":0,"raw_label_only_risk":3,"event_binary_risk_penalty":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.5,"simulated_route":"Stage4B_post_approval_peak_zone","MFE_90D_pct":1.56,"MAE_90D_pct":-26.17,"score_return_alignment_label":"post_approval_peak_zone_4B","current_profile_verdict":"current_profile_4B_too_late_if_peak_zone_not_capped"}
```

---

## 8. Current calibrated profile stress test

The C23 approval-to-commercial-economics gate held again:

```text
commercialized drug revenue/profit bridge
→ keep Stage2

FDA approval-to-launch bridge
→ keep Stage2, local 4B until launch revenue cadence

approval label without direct listed-company economics
→ Stage2 false-positive block

partner commercialization / royalty route
→ positive only while economics are visible

binary regulatory failure
→ hard 4C, no backfill

post-approval peak-zone enthusiasm
→ local 4B, not Green
```

### Rule candidate retained, not newly proposed

```text
C23_APPROVAL_TO_COMMERCIAL_ECONOMICS_REQUIREMENT_V141_HELD_OUT

if C23
and regulatory_approval_or_label_expansion == true
and listed_company_launch_revenue_reimbursement_royalty_or_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C23
and approved_drug_commercialization_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C23
and FDA_approval_to_launch_bridge == true
and MFE_30D_pct >= +30
and quarterly_launch_revenue_cadence == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C23
and approval_label_only == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
    require_new_evidence_family_before_reopen = true
```

```text
if C23
and binary_regulatory_failure_or_CRL_like_thesis_break == true:
    route = Stage4C
    do_not_backfill_later_MFE = true
```

```text
if C23
and post_approval_peak_zone == true
and MFE_90D_pct < +5
and MAE_90D_pct <= -20:
    route = local_4B_or_Stage2_FalsePositive_Block
```

---

## 9. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 7
    avg_MFE_90D_pct: 27.13
    avg_MAE_90D_pct: -19.29
    false_positive_risk: high_if_approval_labels_are_left_actionable
    verdict: adequate_only_with_C23_commercial_economics_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for approval/regulatory labels
    eligible_trigger_count: 7
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L7 bio names require launch/reimbursement/revenue/royalty/margin economics
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C23 requires commercial economics, not approval label
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: approval-label-only, binary failure and post-peak rows route to block/4B
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 10. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | APPROVAL_TO_COMMERCIAL_ECONOMICS_HOLDOUT_V141 | 3 | 4 | 3 | 1 | 0 | 7 | 7 | 0 | 5 | false | false | 18 |

---

## 11. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 7
source_proxy_only_count: 7
evidence_url_pending_count: 7
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
reused_case_count: 7
reused_case_ids:
  - C23|326030|Stage2-Actionable|2024-08-12
  - C23|006280|Stage2-Actionable|2024-07-09
  - C23|170900|Stage2-FalsePositive|2024-10-11
  - C23|000100|Stage2-Actionable|2024-08-20
  - C23|195940|Stage2-Watch|2024-08-28
  - C23|028300|Stage4C|2024-05-16
  - C23|145020|Stage4B|2024-11-06
new_symbol_count: 0
new_trigger_family_count: 0
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C23_approval_to_commercial_economics_gate
  - no_backfill_later_evidence
residual_error_types_found:
  - approval_label_without_listed_company_economics
  - FDA_approval_launch_bridge_green_too_early
  - binary_regulatory_failure
  - post_approval_peak_zone_enthusiasm
  - commercialization_buffer_requires_channel_OPM_refresh
new_axis_proposed: null
existing_axis_strengthened:
  - C23_APPROVAL_TO_COMMERCIAL_ECONOMICS_REQUIREMENT_V141_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C23 approval-to-commercialization candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"141","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":0,"reused_case_count":7,"new_symbol_count":0,"new_trigger_family_count":0,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C23_approval_to_commercial_economics_gate","no_backfill_later_evidence"],"residual_error_types_found":["approval_label_without_listed_company_economics","FDA_approval_launch_bridge_green_too_early","binary_regulatory_failure","post_approval_peak_zone_enthusiasm","commercialization_buffer_requires_channel_OPM_refresh"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R7/C23 loop 141 as holdout validation only. Batch it with C23 loops 99/100/103/137/138/139/140 and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C23 approval-to-commercial-economics gate, FDA approval-to-launch local 4B guard, approval-label false-positive block, binary regulatory failure hard 4C guard, and post-approval peak-zone 4B guard. Do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice 셀트리온(068270), 알테오젠(196170), 한미약품(128940), 리가켐바이오(141080), 코오롱티슈진(950160), 유한양행(000100), 보령(003850), 종근당(185750), SK바이오팜(326030), 녹십자(006280) and other approval-to-commercialization cases when stock-web shards are accessible.
```

---

## 14. Next research state

```yaml
completed_round: R7
completed_loop: 141
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```
