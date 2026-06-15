# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R7
selected_loop: 108
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BINARY_TRIAL_DATA_EVENT_QUALITY_FOLLOWTHROUGH_HOLDOUT_V108_PLATFORM_DATA_LICENSE_CRL_LABEL_SPIKE_REROUTE_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 196170/2024: not_recomputed_this_turn_or_reused_from_prior_C24_row
    - 141080/2024: not_recomputed_this_turn_or_reused_from_prior_C24_row
    - 950160/2024: reused_from_prior_local_C24_4B_row
    - 069620/2024: reused_from_prior_local_C24_boundary_row
    - 128940/2024: not_recomputed_this_turn_or_reused_from_prior_C24_4C_row
    - 028300/2024: reused_from_prior_local_C23_C24_failure_row
    - 115180/2024: not_recomputed_this_turn
    - 365270/2024: not_recomputed_this_turn
    - 203400/2024: not_recomputed_this_turn
    - 206650/2024: not_recomputed_this_turn
    - 237690/2024: not_recomputed_this_turn
    - 256840/2024: not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - binary_trial_data_quality_followthrough_gate
  - platform_license_de_risking_positive_control
  - trial_restart_event_cap_4B_guard
  - pipeline_label_false_positive_guard
  - regulatory_failure_hard_4C_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C24_BIO_TRIAL_DATA_EVENT_RISK` remains Priority 0 in the no-repeat index. The v12 scheduler maps C23~C25 to `R7 / L7_BIO_HEALTHCARE_MEDICAL`.

This file continues the local C24 sequence after `R7/C24 loop 107`; selected loop is therefore `108`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct fresh C24 trial-data candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C24/C23/R13 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C24 should not reward every `pipeline`, `approval`, `trial`, or `bio platform` headline equally.

C24 is a binary-event quality gate:

```text
trial / data / license / platform / regulatory event
→ endpoint quality
→ data durability
→ partner or license validation
→ regulatory path
→ milestone / royalty / commercialization option
→ cash runway and dilution guard
→ price path validation
```

The recurring false positive is:

```text
pipeline vocabulary
trial restart headline
approval-adjacent excitement
pre-approval blowoff
post-peak biotech rebound
brand-name pharma label
```

These can create sharp MFE, but C24 only promotes when probability-adjusted value improves. A data event is a drawbridge: the bridge should rise only when the planks line up — endpoint, durability, partner economics, regulatory path, and capital-structure cleanliness. Without those planks, a price spike is a watch signal, not a Green signal.

This holdout pass validates six route types:

1. **Platform/license de-risking positive-control**
   - High MFE can be legitimate when data/license economics improve probability-adjusted value.

2. **ADC / license-platform positive-control**
   - Stage2 can survive when platform data event has follow-through and controlled MAE.

3. **Trial restart / regulatory overhang event cap**
   - Huge later MFE can coexist with early high MAE; keep local 4B, no Green.

4. **Delayed pipeline option**
   - Later MFE can appear after adverse drift; Watch or Stage2 cap, no immediate Green.

5. **Pipeline label false positive**
   - Brand/pipeline vocabulary without new binary data or commercial bridge should hard-cap.

6. **Binary regulatory failure**
   - CRL-like or non-approval thesis break routes to 4C; later MFE must not backfill the failed event.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 6
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C24_BIO_TRIAL_DATA_EVENT_RISK
    - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C24 holdout validation
    - binary event quality gate
    - pipeline-label false-positive guard
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
  - R7/C24 loop 101
  - R7/C24 loop 105
  - R7/C24 loop 106
  - R7/C24 loop 107
  - R7/C23 loop 100
  - R7/C23 loop 103
  - R13 4B/4C and high-MAE guardrail rows
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional C24 candidate shards were not recomputed in this execution
  - exact duplicate C24 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R7","selected_loop":108,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"SC_PLATFORM_LICENSE_DATA_DERISKING_POSITIVE_CONTROL","symbol":"196170","name":"알테오젠","trigger_type":"Stage2-Actionable","entry_date":"2024-02-21","entry_price":93900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":140.15,"MAE_30D_pct":-10.12,"MFE_90D_pct":209.90,"MAE_90D_pct":-10.12,"MFE_180D_pct":287.11,"MAE_180D_pct":-10.12,"forward_high_30d":225500,"forward_low_30d":84400,"forward_high_90d":291000,"forward_low_90d":84400,"forward_high_180d":363500,"forward_low_180d":84400,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C24|196170|Stage2-Actionable|2024-02-21","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same AlTEOGEN SC platform/license data de-risking row from C24 loop 101 / loop 106","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"platform_license_de_risking_positive","novelty_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|196170|Stage2-Actionable|2024-02-21","non_price_bridge":"SC platform biologic delivery data/license option repricing; exact partner/endpoint/royalty evidence still source-proxy-only","score_alignment":"keep Stage2/Yellow path; Green requires repaired endpoint, partner economics, royalty or commercialization bridge"}
{"row_type":"trigger","selected_round":"R7","selected_loop":108,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_LICENSE_PLATFORM_DATA_EVENT_PROBABILITY_RESET_POSITIVE","symbol":"141080","name":"리가켐바이오","trigger_type":"Stage2-Actionable","entry_date":"2024-01-29","entry_price":53500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.60,"MAE_30D_pct":-8.20,"MFE_90D_pct":63.00,"MAE_90D_pct":-11.50,"MFE_180D_pct":94.40,"MAE_180D_pct":-18.10,"forward_high_30d":70900,"forward_low_30d":49100,"forward_high_90d":87200,"forward_low_90d":47300,"forward_high_180d":104000,"forward_low_180d":43800,"corporate_action_window_status":"not_flagged_in_prior_local_validation_batch_reverify_required","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C24|141080|Stage2-Actionable|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same LCB ADC/license platform data-event row from C24 loop 105 / loop 106","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ADC_license_platform_positive","novelty_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|141080|Stage2-Actionable|2024-01-29","non_price_bridge":"license/platform data event probability reset with positive price follow-through, but endpoint and economic evidence remain proxy-only","score_alignment":"Stage2 allowed; Stage3 requires endpoint quality, partner/license economics and cash runway repair"}
{"row_type":"trigger","selected_round":"R7","selected_loop":108,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"TRIAL_RESTART_REGULATORY_OVERHANG_EVENT_CAP_VOLATILITY_LOCAL_4B","symbol":"950160","name":"코오롱티슈진","trigger_type":"Stage4B","entry_date":"2024-01-11","entry_price":11690,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.34,"MAE_30D_pct":-26.35,"MFE_90D_pct":37.13,"MAE_90D_pct":-26.35,"MFE_180D_pct":86.48,"MAE_180D_pct":-26.35,"forward_high_30d":13250,"forward_low_30d":8610,"forward_high_90d":16030,"forward_low_90d":8610,"forward_high_180d":21800,"forward_low_180d":8610,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C24|950160|Stage4B|2024-01-11","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same Kolon TissueGene trial-restart local-4B row from C24 loop 101","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"trial_restart_event_cap_4B","novelty_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|950160|Stage4B|2024-01-11","non_price_bridge":"trial restart / regulatory overhang event-cap volatility; large later MFE but early high MAE","score_alignment":"local 4B only; price-only MFE cannot become positive-stage promotion without endpoint/regulatory/economic bridge"}
{"row_type":"trigger","selected_round":"R7","selected_loop":108,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"PHARMA_PIPELINE_DATA_OPTION_WITH_DELAYED_FOLLOWTHROUGH_STAGE2_CAP","symbol":"069620","name":"대웅제약","trigger_type":"Stage2","entry_date":"2024-03-19","entry_price":123600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MAE_30D_pct":-13.67,"MFE_90D_pct":3.24,"MAE_90D_pct":-19.01,"MFE_180D_pct":21.36,"MAE_180D_pct":-19.01,"forward_high_30d":127600,"forward_low_30d":106700,"forward_high_90d":127600,"forward_low_90d":100100,"forward_high_180d":150000,"forward_low_180d":100100,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C24|069620|Stage2|2024-03-19","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","reuse_reason":"same Daewoong Pharma delayed pipeline-option row from C24 loop 101 / C23 reroute rows","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"delayed_pipeline_option_stage2_cap","novelty_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|069620|Stage2|2024-03-19","non_price_bridge":"pharma pipeline/data option with weak early price confirmation and delayed 180D payoff","score_alignment":"Stage2-Watch/cap; no Green because early follow-through and endpoint/economic bridge were insufficient"}
{"row_type":"trigger","selected_round":"R7","selected_loop":108,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"PIPELINE_LABEL_WITHOUT_FRESH_BINARY_DATA_FALSE_POSITIVE","symbol":"128940","name":"한미약품","trigger_type":"Stage4C","entry_date":"2024-03-25","entry_price":347000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.86,"MAE_30D_pct":-14.70,"MFE_90D_pct":0.86,"MAE_90D_pct":-25.65,"MFE_180D_pct":8.07,"MAE_180D_pct":-29.83,"forward_high_30d":350000,"forward_low_30d":296000,"forward_high_90d":350000,"forward_low_90d":258000,"forward_high_180d":375000,"forward_low_180d":243500,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C24|128940|Stage4C|2024-03-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Hanmi pipeline-label false-positive row from C24 loop 101","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"pipeline_label_false_positive","novelty_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|128940|Stage4C|2024-03-25","non_price_bridge":"brand-name pipeline vocabulary without fresh binary data, endpoint quality improvement, partner economics or commercialization cash bridge","score_alignment":"hard cap / 4C; low MFE and deep 90D/180D MAE reject positive C24 credit"}
{"row_type":"trigger","selected_round":"R7","selected_loop":108,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_REGULATORY_TRIAL_FAILURE_HARD_4C_NO_BACKFILL","symbol":"028300","name":"HLB","trigger_type":"Stage4C","entry_date":"2024-05-17","entry_price":67100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.99,"MAE_30D_pct":-29.96,"MFE_90D_pct":46.20,"MAE_90D_pct":-29.96,"MFE_180D_pct":46.20,"MAE_180D_pct":-29.96,"forward_high_30d":73800,"forward_low_30d":47000,"forward_high_90d":98100,"forward_low_90d":47000,"forward_high_180d":98100,"forward_low_180d":47000,"corporate_action_window_status":"clean_180D_window_after_old_CA","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C24|028300|Stage4C|2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_overlay","reuse_reason":"same HLB CRL/regulatory thesis-break row from R13/C23/C24 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"binary_failure_hard_4C","novelty_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|028300|Stage4C|2024-05-17","non_price_bridge":"binary regulatory/trial failure or CRL-like thesis break; later rebound must not validate the failed event","score_alignment":"hard 4C; do not backfill later MFE into binary failure trigger"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R7","selected_loop":108,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_NEW_TRIAL_DATA_EVENT_REPRICE_TODO","candidate_symbols":["115180","365270","203400","206650","237690","256840"],"candidate_names":["큐리언트","큐라클","에이비온","유바이오로직스","에스티팜","한국비엔씨"],"why_not_trigger_row_now":"fresh C24 symbol-year shards were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C24 evidence; distinguish true data/license de-risking from price-only clinical theme spikes"}
```

---

## 6. Case analysis

### 6.1 ALTEOGEN / 196170 — platform/license de-risking positive-control

```yaml
entry_price: 93900
90D_MFE_MAE: +209.90 / -10.12
180D_MFE_MAE: +287.11 / -10.12
route: Stage2-Actionable / Yellow candidate with Green evidence repair
```

This is the clean upside-control. The event path should not be treated as generic biotech binary risk if platform/license economics changed probability-adjusted value. But even this row remains `source_proxy_only`; Green requires endpoint, partner, royalty, exclusivity and cash-bridge repair.

### 6.2 LigaChem Bio / 141080 — ADC license-platform positive

```yaml
entry_price: 53500
90D_MFE_MAE: +63.00 / -11.50
180D_MFE_MAE: +94.40 / -18.10
route: Stage2-Actionable with 4B watch
```

This row validates that C24 should capture license/data de-risking, but the later drawdown profile still argues against unqualified Green.

### 6.3 Kolon TissueGene / 950160 — trial restart local 4B

```yaml
entry_price: 11690
90D_MFE_MAE: +37.13 / -26.35
180D_MFE_MAE: +86.48 / -26.35
route: Stage4B
```

High MFE does not erase early high MAE. This is the event-cap archetype: trial restart plus regulatory overhang can be tradable, but the evidence bridge is not strong enough for positive-stage promotion.

### 6.4 Daewoong Pharma / 069620 — delayed pipeline option

```yaml
entry_price: 123600
90D_MFE_MAE: +3.24 / -19.01
180D_MFE_MAE: +21.36 / -19.01
route: Stage2 cap / Watch
```

This is neither hard 4C nor Green. It is the middle case that argues for Watch until delayed option value is confirmed by evidence rather than price alone.

### 6.5 Hanmi Pharm / 128940 — pipeline label false positive

```yaml
entry_price: 347000
90D_MFE_MAE: +0.86 / -25.65
180D_MFE_MAE: +8.07 / -29.83
route: Stage4C
```

Pipeline vocabulary inflated information confidence, but the price path rejected it. This should not be Stage2-Actionable.

### 6.6 HLB / 028300 — binary regulatory failure hard 4C

```yaml
entry_price: 67100
90D_MFE_MAE: +46.20 / -29.96
180D_MFE_MAE: +46.20 / -29.96
route: Stage4C
```

The later rebound cannot validate the failed event. C24 needs a no-backfill guard for binary regulatory failures.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 6
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 2
mixed_positive_count: 2
counterexample_count: 2
local_4B_watch_count: 3
hard_4C_count: 2
current_profile_error_count: 5
diversity_score_summary: "platform/license positives, trial-restart 4B, delayed pipeline option, pipeline-label hard 4C, binary failure hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C24 lesson |
|---|---:|---:|---:|---|
| 196170 | platform/license positive | +209.90 / -10.12 | +287.11 / -10.12 | de-risking can be real; Green needs exact source repair |
| 141080 | ADC license positive | +63.00 / -11.50 | +94.40 / -18.10 | positive, but 4B watch remains |
| 950160 | trial restart 4B | +37.13 / -26.35 | +86.48 / -26.35 | price MFE cannot override event-cap risk |
| 069620 | delayed option | +3.24 / -19.01 | +21.36 / -19.01 | Watch/cap, no Green |
| 128940 | pipeline false positive | +0.86 / -25.65 | +8.07 / -29.83 | label-only pipeline fails |
| 028300 | binary failure 4C | +46.20 / -29.96 | +46.20 / -29.96 | no-backfill after regulatory failure |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"data_event_quality":24,"endpoint_relevance":20,"partner_license_validation":22,"commercial_cash_bridge":8,"price_confirmation":24,"capital_structure_cleanliness":9,"high_MAE_penalty":-4},"weighted_score_before":86,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"data_event_quality":25,"endpoint_relevance":22,"partner_license_validation":24,"commercial_cash_bridge":10,"price_confirmation":24,"capital_structure_cleanliness":9,"high_MAE_penalty":-4},"weighted_score_after":90,"stage_label_after":"Stage3-Yellow_candidate_Green_source_repair_required","changed_components":["data_event_quality","endpoint_relevance","partner_license_validation","commercial_cash_bridge"],"component_delta_explanation":"Platform/license de-risking produced extreme MFE with controlled MAE, but source repair is required before Green.","MFE_90D_pct":209.90,"MAE_90D_pct":-10.12,"score_return_alignment_label":"platform_license_de_risking_positive","current_profile_verdict":"current_profile_underweights_if_all_trial_events_treated_as_binary_risk"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"141080","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"data_event_quality":22,"endpoint_relevance":17,"partner_license_validation":18,"commercial_cash_bridge":6,"price_confirmation":16,"capital_structure_cleanliness":8,"high_MAE_penalty":-4},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"data_event_quality":22,"endpoint_relevance":18,"partner_license_validation":19,"commercial_cash_bridge":7,"price_confirmation":16,"capital_structure_cleanliness":8,"high_MAE_penalty":-4},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":["endpoint_relevance","partner_license_validation","commercial_cash_bridge"],"component_delta_explanation":"ADC/license data event follow-through validates Stage2, but later drawdown and proxy evidence block Green.","MFE_90D_pct":63.00,"MAE_90D_pct":-11.50,"score_return_alignment_label":"ADC_license_platform_positive_with_4B_watch","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"950160","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"data_event_quality":10,"endpoint_relevance":8,"partner_license_validation":3,"commercial_cash_bridge":1,"price_confirmation":14,"capital_structure_cleanliness":5,"high_MAE_penalty":-16},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"data_event_quality":8,"endpoint_relevance":7,"partner_license_validation":2,"commercial_cash_bridge":0,"price_confirmation":8,"capital_structure_cleanliness":4,"high_MAE_penalty":-18},"weighted_score_after":38,"stage_label_after":"Stage4B_event_cap","changed_components":["data_event_quality","endpoint_relevance","partner_license_validation","commercial_cash_bridge","price_confirmation","capital_structure_cleanliness","high_MAE_penalty"],"component_delta_explanation":"Trial-restart event produced later MFE but early MAE was high and non-price bridge was unresolved.","MFE_90D_pct":37.13,"MAE_90D_pct":-26.35,"score_return_alignment_label":"trial_restart_event_cap_local_4B","current_profile_verdict":"current_profile_false_positive_if_price_MFE_used_alone"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"069620","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"data_event_quality":12,"endpoint_relevance":9,"partner_license_validation":5,"commercial_cash_bridge":4,"price_confirmation":5,"capital_structure_cleanliness":6,"high_MAE_penalty":-8},"weighted_score_before":62,"stage_label_before":"Stage2","raw_component_scores_after":{"data_event_quality":11,"endpoint_relevance":8,"partner_license_validation":4,"commercial_cash_bridge":4,"price_confirmation":5,"capital_structure_cleanliness":6,"high_MAE_penalty":-8},"weighted_score_after":58,"stage_label_after":"Stage2_Watch_or_Cap","changed_components":["data_event_quality","endpoint_relevance","partner_license_validation"],"component_delta_explanation":"Delayed option value appeared only after adverse drift; Watch is safer than Green or hard block.","MFE_90D_pct":3.24,"MAE_90D_pct":-19.01,"score_return_alignment_label":"delayed_pipeline_option_watch","current_profile_verdict":"current_profile_too_binary_if_rejects_or_promotes_immediately"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"128940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"data_event_quality":8,"endpoint_relevance":7,"partner_license_validation":2,"commercial_cash_bridge":2,"price_confirmation":1,"capital_structure_cleanliness":6,"high_MAE_penalty":-16},"weighted_score_before":54,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"data_event_quality":4,"endpoint_relevance":4,"partner_license_validation":0,"commercial_cash_bridge":0,"price_confirmation":0,"capital_structure_cleanliness":5,"high_MAE_penalty":-20},"weighted_score_after":28,"stage_label_after":"Stage4C","changed_components":["data_event_quality","endpoint_relevance","partner_license_validation","commercial_cash_bridge","price_confirmation","capital_structure_cleanliness","high_MAE_penalty"],"component_delta_explanation":"Pipeline label without fresh binary data or economic bridge produced low MFE and deep MAE.","MFE_90D_pct":0.86,"MAE_90D_pct":-25.65,"score_return_alignment_label":"pipeline_label_false_positive","current_profile_verdict":"current_profile_false_positive_if_information_confidence_overcredits_label"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"data_event_quality":5,"endpoint_relevance":3,"partner_license_validation":0,"commercial_cash_bridge":0,"price_confirmation":6,"capital_structure_cleanliness":2,"high_MAE_penalty":-22},"weighted_score_before":36,"stage_label_before":"Stage4C","raw_component_scores_after":{"data_event_quality":0,"endpoint_relevance":0,"partner_license_validation":0,"commercial_cash_bridge":0,"price_confirmation":0,"capital_structure_cleanliness":1,"high_MAE_penalty":-25},"weighted_score_after":8,"stage_label_after":"Stage4C_no_backfill","changed_components":["data_event_quality","endpoint_relevance","price_confirmation","capital_structure_cleanliness","high_MAE_penalty"],"component_delta_explanation":"Binary regulatory/trial failure breaks the thesis; later rebound cannot repair the original failed event.","MFE_90D_pct":46.20,"MAE_90D_pct":-29.96,"score_return_alignment_label":"binary_regulatory_failure_hard_4C","current_profile_verdict":"current_profile_correct_only_if_no_backfill_guard_applied"}
```

---

## 9. Current calibrated profile stress test

The C24 binary-event quality gate held:

```text
platform/license/data de-risking with huge MFE
→ keep Stage2/Yellow, but Green requires source repair

ADC/license platform event
→ Stage2-Actionable with 4B watch

trial restart or event-cap volatility
→ local 4B, not Green

delayed pipeline option
→ Watch/cap

pipeline label without fresh data
→ hard 4C / false-positive block

binary regulatory failure
→ hard 4C and no-backfill
```

### Rule candidate retained, not newly proposed

```text
C24_BINARY_EVENT_QUALITY_FOLLOWTHROUGH_GATE_V108_HELD_OUT

if C24
and trial_pipeline_platform_or_data_event_label == true
and endpoint_quality_partner_license_regulatory_path_cash_runway_or_economic_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C24
and endpoint_quality_partner_license_or_platform_de_risking_bridge == true
and MFE_90D_pct >= +40
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
    block_stage3_green_until_source_repair = true
```

```text
if C24
and price_MFE_event_spike == true
and MAE_90D_pct <= -20
and endpoint_or_partner_bridge == false:
    route = local_4B_watch_or_Stage2_FalsePositive_Block
```

```text
if C24
and pipeline_label_only == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C24
and binary_regulatory_or_trial_failure == true:
    route = Stage4C
    do_not_backfill_later_MFE = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 6
    avg_MFE_90D_pct: 60.89
    avg_MAE_90D_pct: -20.43
    false_positive_risk: high_if_price_MFE_or_pipeline_label_is_overcredited
    verdict: adequate_only_with_C24_binary_event_quality_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for biotech information confidence and event vocabulary
    eligible_trigger_count: 6
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L7 bio rows require event quality, endpoint relevance and economic bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C24 requires trial/data event quality rather than pipeline label
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: binary regulatory failures and label-only pipeline rows route hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | BINARY_TRIAL_DATA_EVENT_QUALITY_FOLLOWTHROUGH_HOLDOUT_V108 | 2 | 2 | 3 | 2 | 0 | 6 | 6 | 0 | 5 | false | false | 17 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 6
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 6
reused_case_ids:
  - C24|196170|Stage2-Actionable|2024-02-21
  - C24|141080|Stage2-Actionable|2024-01-29
  - C24|950160|Stage4B|2024-01-11
  - C24|069620|Stage2|2024-03-19
  - C24|128940|Stage4C|2024-03-25
  - C24|028300|Stage4C|2024-05-17
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C24_binary_event_quality_followthrough_gate
  - no_backfill_later_evidence
residual_error_types_found:
  - price_MFE_event_cap_without_endpoint_bridge
  - pipeline_label_false_positive
  - binary_regulatory_failure_no_backfill
  - platform_license_de_risking_needs_source_repair
new_axis_proposed: null
existing_axis_strengthened:
  - C24_BINARY_EVENT_QUALITY_FOLLOWTHROUGH_GATE_V108_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C24 trial-data candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"108","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":0,"reused_case_count":6,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C24_binary_event_quality_followthrough_gate","no_backfill_later_evidence"],"residual_error_types_found":["price_MFE_event_cap_without_endpoint_bridge","pipeline_label_false_positive","binary_regulatory_failure_no_backfill","platform_license_de_risking_needs_source_repair"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R7/C24 loop 108 as holdout validation only. Batch it with C24 loops 90~107, C23 commercialization reroute rows, and R13 high-MAE / Stage2 false-positive / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C24 binary-event-quality follow-through gate and the no-backfill rule for binary regulatory failures, but do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice 큐리언트(115180), 큐라클(365270), 에이비온(203400), 유바이오로직스(206650), 에스티팜(237690), 한국비엔씨(256840), 알테오젠(196170), 리가켐바이오(141080) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R7
completed_loop: 108
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C19_BRAND_RETAIL_INVENTORY_MARGIN
```
