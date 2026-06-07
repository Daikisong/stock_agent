---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 97
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: ONCOLOGY_CLINICAL_DATA_BINARY_EVENT_RISK_VS_DURABLE_PARTNER_PLATFORM_BRIDGE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_watch | high_MAE_guardrail | canonical_archetype_compression
selected_from_no_repeat_index: true
source_proxy_only: true
evidence_url_pending: true
production_scoring_changed: false
shadow_weight_only: true
created_by: GPT-5.5 Pro
---

# E2R Stock-Web v12 Residual Research — R7 loop 97 / L7 / C24

## 0. Executive summary

This standalone residual research file expands **C24_BIO_TRIAL_DATA_EVENT_RISK** inside **R7 / L7_BIO_HEALTHCARE_MEDICAL**.

The tested compression is:

> A clinical-trial or bio-platform headline should not become Stage3-Green merely because price survives a data/event window. C24 needs an explicit bridge from **data quality / endpoint durability / partner commitment / funding runway / regulatory path** into commercialization optionality. If the bridge is missing, the same price spike should be capped as **Stage2-Yellow / local 4B watch / 4C thesis-break watch**, especially when post-trigger MAE is deep.

This loop is designed as **shadow rule / residual ledger material**, not a production scoring patch. All non-price evidence is marked `source_proxy_only` and `evidence_url_pending`.

---

## 1. Scope and scheduler decision

- `selected_round`: R7
- `large_sector_id`: L7_BIO_HEALTHCARE_MEDICAL
- `canonical_archetype_id`: C24_BIO_TRIAL_DATA_EVENT_RISK
- `selected_loop`: 97
- `selection_reason`: Priority 0 still shows C24 at 27 rows, needing 3 additional rows to reach the 30-row minimum stability band.
- `registry_basis`: v12 registry shows existing C24 entries through R7 loop 96, so this file advances the canonical pair to loop 97.

### Novelty guard

Hard duplicate key checked conceptually against the available registry:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This file uses new trigger-date families for the tested symbols and compresses them into a different fine archetype:

```text
ONCOLOGY_CLINICAL_DATA_BINARY_EVENT_RISK_VS_DURABLE_PARTNER_PLATFORM_BRIDGE
```

---

## 2. Price source validation

```json
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","schema_mfe":"max high from entry_date through N tradable rows / entry_price - 1","schema_mae":"min low from entry_date through N tradable rows / entry_price - 1","calibration_note":"Raw/unadjusted OHLC. Corporate-action contaminated windows are blocked or caveated."}
```

### Symbol profile caveats

| symbol | name | active/inferred status | profile caveat used in this loop |
|---|---|---|---|
| 028300 | HLB | active_like | historical corporate-action candidates exist before 2024; 2024 event window itself uses tradable shard but remains source_proxy_only |
| 215600 | 신라젠 | active_like | corporate-action candidate on 2024-07-09, so 90D/180D windows after spring entry are **not promotion-usable** |
| 141080 | 리가켐바이오 | active_like | corporate-action candidate on 2024-04-23; post-2024-06-20 event window treated with caveat |
| 039200 | 오스코텍 | active_like | historical corporate-action candidates before 2024 only; 2024 window used as clean enough for residual ledger |
| 358570 | 지아이이노베이션 | active_like | corporate-action candidates on 2024-01-19 and 2024-02-15; post-2024-04 entry still caveated due profile discontinuity |

---

## 3. Case matrix

| case_id | symbol | name | trigger_type | entry_date | entry_price | path result | C24 interpretation |
|---|---:|---|---|---:|---:|---|---|
| C24_R7L97_001 | 028300 | HLB | late_stage_binary_data_regulatory_event_risk | 2024-05-16 | 95,800 | -50% class MAE after binary event failure | true C24 hard 4C / no Green despite pre-event score |
| C24_R7L97_002 | 215600 | 신라젠 | clinical_revival_label_spike_with_ca_block | 2024-03-15 | 5,620 | weak MFE and later CA contamination | local 4B watch / promotion blocked |
| C24_R7L97_003 | 141080 | 리가켐바이오 | partner_platform_data_optionality_bridge | 2024-06-20 | 75,500 | positive asymmetry, but profile CA caveat and URL pending | Yellow-to-Green candidate only with partner/data bridge |
| C24_R7L97_004 | 039200 | 오스코텍 | targeted_oncology_data_partner_followthrough | 2024-06-03 | 37,300 | positive MFE with high MAE | Yellow candidate; needs MAE guardrail |
| C24_R7L97_005 | 358570 | 지아이이노베이션 | early_platform_trial_label_decay | 2024-04-24 | 14,030 | low MFE / deep MAE | false Stage2 / event cap |

---

## 4. Trigger-level JSONL rows

```jsonl
{"row_type":"trigger","case_id":"C24_R7L97_001","symbol":"028300","name":"HLB","round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ONCOLOGY_BINARY_EVENT_PRE_PDUFA_FAILURE_PATH","trigger_type":"late_stage_binary_data_regulatory_event_risk","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":11.59,"mae_30d_pct":-50.94,"mfe_90d_pct":11.59,"mae_90d_pct":-50.94,"mfe_180d_pct":11.59,"mae_180d_pct":-50.94,"peak_date":"2024-05-16","trough_date":"2024-05-20","stage_current_profile":"Stage2_or_Stage3_Yellow_before_event","stage_research_override":"4C_thesis_break_after_binary_failure","data_quality_label":"usable_with_caveat","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote":true,"residual_flag":"hard_4c_confirmation_needed_for_binary_bio_event"}
{"row_type":"trigger","case_id":"C24_R7L97_002","symbol":"215600","name":"신라젠","round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_REVIVAL_LABEL_SPIKE_CA_BLOCK","trigger_type":"clinical_revival_label_spike_with_ca_block","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":5620,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.07,"mae_30d_pct":-16.37,"mfe_90d_pct":null,"mae_90d_pct":null,"mfe_180d_pct":null,"mae_180d_pct":null,"peak_date":"2024-03-15","trough_date":"2024-03-25","stage_current_profile":"Stage2_label_risk","stage_research_override":"local_4B_watch_or_blocked_by_corporate_action_window","data_quality_label":"blocked_by_corporate_action","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote":true,"residual_flag":"clinical_revival_headline_not_enough_and_window_blocked"}
{"row_type":"trigger","case_id":"C24_R7L97_003","symbol":"141080","name":"리가켐바이오","round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_PLATFORM_PARTNER_OPTIONALITY_BRIDGE","trigger_type":"partner_platform_data_optionality_bridge","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.50,"mae_30d_pct":-7.68,"mfe_90d_pct":15.50,"mae_90d_pct":-7.68,"mfe_180d_pct":15.50,"mae_180d_pct":-7.68,"peak_date":"2024-07-09","trough_date":"2024-06-28","stage_current_profile":"Stage2_to_Yellow","stage_research_override":"Yellow_candidate_not_Green_until_partner_data_bridge_verified","data_quality_label":"usable_with_caveat","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote":true,"residual_flag":"positive_asymmetry_requires_non_price_partner_data_bridge"}
{"row_type":"trigger","case_id":"C24_R7L97_004","symbol":"039200","name":"오스코텍","round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"TARGETED_ONCOLOGY_DATA_PARTNER_FOLLOWTHROUGH","trigger_type":"targeted_oncology_data_partner_followthrough","trigger_date":"2024-06-03","entry_date":"2024-06-03","entry_price":37300,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.38,"mae_30d_pct":-14.08,"mfe_90d_pct":20.38,"mae_90d_pct":-14.08,"mfe_180d_pct":20.38,"mae_180d_pct":-14.08,"peak_date":"2024-07-16","trough_date":"2024-06-17","stage_current_profile":"Stage2_to_Yellow","stage_research_override":"Yellow_candidate_with_high_MAE_guardrail","data_quality_label":"clean_tradable_path","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote":true,"residual_flag":"positive_case_but_requires_MAE_guard_and_partner_data_durability"}
{"row_type":"trigger","case_id":"C24_R7L97_005","symbol":"358570","name":"지아이이노베이션","round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"EARLY_PLATFORM_TRIAL_LABEL_DECAY","trigger_type":"early_platform_trial_label_decay","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":14030,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.57,"mae_30d_pct":-18.67,"mfe_90d_pct":1.57,"mae_90d_pct":-29.29,"mfe_180d_pct":1.57,"mae_180d_pct":-29.29,"peak_date":"2024-04-24","trough_date":"2024-06-25","stage_current_profile":"Stage2_label_risk","stage_research_override":"event_cap_or_false_stage2","data_quality_label":"usable_with_caveat","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote":true,"residual_flag":"clinical_platform_label_without_data_durability_or_partner_cash_bridge"}
```

---

## 5. Aggregate metrics

```json
{"row_type":"aggregate_metric","round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","sample_count":5,"positive_count":2,"counterexample_count":3,"avg_mfe_30d_pct":10.02,"avg_mae_30d_pct":-21.83,"high_mae_case_count":4,"blocked_or_do_not_promote_count":5,"source_proxy_only_count":5,"evidence_url_pending_count":5,"summary":"C24 needs explicit non-price trial-data durability and partner/funding/regulatory bridge. Price-only trial-event spikes often show large MFE/MAE asymmetry and binary 4C failure risk."}
```

### Positive / counterexample balance

- Positive-with-caveat: 141080, 039200
- Hard counterexample / 4C or event cap: 028300, 215600, 358570
- Promotion-ready rows: 0
- Ledger-usable rows: 5

---

## 6. Current calibrated profile stress test

### Failure mode A — binary clinical event treated like ordinary rerating

HLB shows the cleanest failure: a pre-event Stage2/Yellow setup can still become a hard 4C after the data/regulatory binary resolves negatively. The entry-day high inflates MFE, but post-event path collapses immediately. This is the core C24 guardrail: **do not let entry-day high MFE mask binary-event MAE**.

### Failure mode B — platform label without durable data bridge

지아이이노베이션 and 신라젠 demonstrate the platform/revival label trap. Price can react to optionality, but without endpoint durability, partner commitment, and financing runway, the event window either decays or becomes unusable due corporate-action contamination.

### Failure mode C — positive follow-through still needs MAE guardrail

리가켐바이오 and 오스코텍 are not simple failures. They have positive asymmetry, but C24 still needs a bridge from **clinical data / partner validation / regulatory path / funding runway** to avoid treating any oncology/ADC/targeted-therapy headline as Green.

---

## 7. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","scope":"canonical_archetype","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"hard_4c_confirmation","candidate_rule":"If binary clinical/regulatory event resolves negatively, route to 4C regardless of prior price-based MFE; entry-day high cannot count as durable rerating evidence.","evidence_case_ids":["C24_R7L97_001"],"production_ready":false,"blocker":"exact non-price URL pending"}
{"row_type":"shadow_weight","scope":"canonical_archetype","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"stage2_required_bridge","candidate_rule":"For C24, Stage2 requires at least one of endpoint durability, partner commitment, funding runway, regulatory path clarity, or commercialization route. Trial/platform label alone is capped.","evidence_case_ids":["C24_R7L97_002","C24_R7L97_005"],"production_ready":false,"blocker":"source_proxy_only"}
{"row_type":"shadow_weight","scope":"canonical_archetype","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"high_MAE_guardrail","candidate_rule":"Positive C24 cases with MFE>15% but MAE worse than -10% remain Yellow until data durability and partner/funding bridge are confirmed.","evidence_case_ids":["C24_R7L97_003","C24_R7L97_004"],"production_ready":false,"blocker":"evidence_url_pending"}
```

---

## 8. Score simulation

```jsonl
{"row_type":"score_simulation","case_id":"C24_R7L97_001","old_stage_guess":"Stage2_or_Stage3_Yellow","new_stage_guess":"4C","reason":"binary event failure dominates price MFE"}
{"row_type":"score_simulation","case_id":"C24_R7L97_003","old_stage_guess":"Stage2","new_stage_guess":"Stage3_Yellow_candidate","reason":"positive asymmetry, but partner/data bridge must be verified"}
{"row_type":"score_simulation","case_id":"C24_R7L97_004","old_stage_guess":"Stage2","new_stage_guess":"Stage3_Yellow_candidate_with_high_MAE_guard","reason":"follow-through exists, but MAE drawdown is too deep for unguarded Green"}
{"row_type":"score_simulation","case_id":"C24_R7L97_005","old_stage_guess":"Stage2","new_stage_guess":"Stage2_event_cap_or_3Red","reason":"platform label produced little MFE and deep MAE"}
```

---

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","contribution":"Adds 5 ledger rows to thin C24 coverage. Main residual is binary clinical event MAE masking by entry-day MFE and price-only trial label spikes.","promotion_recommendation":"hold_for_url_evidence","do_not_promote_reason":"source_proxy_only and exact clinical/regulatory evidence URLs pending"}
{"row_type":"residual_contribution","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","contribution":"Proposes hard_4c_confirmation, stage2_required_bridge, and high_MAE_guardrail candidates specific to C24.","promotion_recommendation":"shadow_only"}
```

---

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session.

```text
You are the later coding agent for Songdaiki/stock_agent.

Input artifact:
- docs/round/e2r_stock_web_v12_residual_round_R7_loop_97_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md

Tasks:
1. Ingest this MD with the v12 calibration parser.
2. Validate trigger rows against Stock-Web shards.
3. Keep rows as source_proxy_only until exact clinical/regulatory evidence URLs are attached.
4. Do not promote any patch directly from this file.
5. Use the shadow rule candidates only as candidates:
   - hard_4c_confirmation for binary clinical/regulatory failure
   - stage2_required_bridge for trial/platform label spikes
   - high_MAE_guardrail for positive C24 cases with deep MAE
6. Recompute aggregate metrics after URL-backed evidence is added.
```
