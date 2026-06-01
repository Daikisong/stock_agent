# E2R Stock-Web v12 Residual Research — R8 Loop 82 / L8 / C28

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 82,
  "computed_next_round": "R9",
  "computed_next_loop": 82,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "software_security_contract_retention_guardrail",
    "ERP_fintech_IT_outsourcing_contract_retention_margin_bridge",
    "software_theme_fade_boundary",
    "bounded_no_forced4B_guard",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R7 / loop 82.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 82
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
computed_next_round = R9
computed_next_loop = 82
```

R8 was routed to C28 because loop 82 R7 used C25, loop 82 R6 used C22, and loop 81 R8 used C26.  
This file tests software / IT-service contract retention bridges rather than content IP or platform ad leverage.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C28 concentration in:

```text
012510, 053800, 263860, 030520, 131370, 042510
```

This run uses three different symbols:

```text
094280 / 효성ITX / IT outsourcing and managed-service contract-retention candidate
060850 / 영림원소프트랩 / ERP cloud contract-retention theme fade
053580 / 웹케시 / B2B fintech software retention theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected 180D window.
```

## Research thesis

C28 is not “소프트웨어주가 올랐다.”

The mechanism must pass through:

```text
software / security / IT-service headline
→ ARR or recurring contract base
→ renewal, usage and churn control
→ implementation backlog or managed-service continuity
→ revenue conversion and margin bridge
→ durable rerating
```

소프트웨어주는 코드 한 줄보다 반복 청구서가 중요하다.  
C28이 보려는 것은 테마의 불꽃이 실제 갱신, 유지율, 사용량, 반복 매출, 마진으로 서버실에 계속 전원을 넣는지다.

---

## Case 1 — Bounded contract-retention candidate: 094280 / 효성ITX

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is IT outsourcing / contact-center / managed-service contract retention, renewal, recurring revenue and margin bridge evidence.

```text
evidence_family = IT_OUTSOURCING_CONTACT_CENTER_MANAGED_SERVICE_CONTRACT_RETENTION_REVENUE_MARGIN_BRIDGE
case_role = positive_bounded_IT_outsourcing_contract_retention_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 12,180
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/094/094280/2024.csv`:

```text
2024-02-01,12180,12320,12160,12320
2024-02-13,12520,12610,12500,12540
2024-03-29,12700,12910,12660,12830
2024-07-24,13270,13370,13210,13330
2024-08-05,12950,12950,11970,12100
2024-09-03,12810,13340,12700,13340
2024-10-15,12770,15200,12500,12550
2024-10-22,12500,12510,12330,12390
```

### Backtest

```text
MFE_30D  = +3.53%
MAE_30D  = -0.16%
MFE_90D  = +5.99%
MAE_90D  = -1.15%
MFE_180D = +24.79%
MAE_180D = -1.72%
peak_180 = 15,200 on 2024-10-15
trough_180 = 11,970 on 2024-08-05
peak_to_later_drawdown = -18.88%
```

### Interpretation

This is a bounded C28 service-retention candidate.  
It is not an explosive Green, but its MAE is too controlled to force 4B without non-price churn or margin deterioration.

Correct treatment:

```text
verified managed-service contract retention / renewal / recurring revenue / margin bridge → Stage2-Yellow possible
bounded MAE + weak bridge → RiskWatch
no forced 4B without non-price churn, contract loss or margin break
```

---

## Case 2 — Counterexample / local 4B: 060850 / 영림원소프트랩

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests ERP/cloud software theme beta without enough ARR, renewal, churn-control and margin bridge.

```text
evidence_family = ERP_CLOUD_SOFTWARE_CONTRACT_RETENTION_THEME_WITH_WEAK_ARR_RENEWAL_MARGIN_BRIDGE
case_role = counterexample_ERP_cloud_retention_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 9,270
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/060/060850/2024.csv`:

```text
2024-02-01,9270,9290,9000,9250
2024-02-16,8920,9370,8830,8900
2024-04-05,9410,11270,9220,9300
2024-05-16,8750,10250,8700,8840
2024-08-05,8300,8310,7310,7610
2024-09-11,7210,8810,6920,7010
2024-10-17,7030,8360,6910,6940
2024-10-28,6730,6820,6680,6820
```

### Backtest

```text
MFE_30D  = +1.08%
MAE_30D  = -7.77%
MFE_90D  = +21.57%
MAE_90D  = -11.00%
MFE_180D = +21.57%
MAE_180D = -27.94%
peak_180 = 11,270 on 2024-04-05
trough_180 = 6,680 on 2024-10-28
peak_to_later_drawdown = -40.73%
```

### Interpretation

This is a C28 ERP/cloud software theme-fade row.  
The spike did not validate durable ARR/retention economics and later MAE moved into local-4B territory.

Correct treatment:

```text
ERP/cloud software theme beta
→ no verified ARR / renewal / churn-control / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 053580 / 웹케시

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests B2B fintech software retention beta without enough customer retention and usage/revenue bridge.

```text
evidence_family = B2B_FINTECH_SOFTWARE_CONTRACT_RETENTION_THEME_WITH_WEAK_CUSTOMER_RENEWAL_REVENUE_MARGIN_BRIDGE
case_role = counterexample_fintech_software_retention_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 9,370
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/053/053580/2024.csv`:

```text
2024-02-01,9370,9480,9270,9370
2024-02-22,9980,10690,9910,10200
2024-03-18,10500,10700,10140,10230
2024-04-08,9250,9300,9000,9000
2024-08-05,7770,7770,6760,6970
2024-09-09,6800,7120,6760,7120
2024-10-17,7220,8960,7220,7330
2024-10-31,7100,7170,7060,7160
```

### Backtest

```text
MFE_30D  = +14.09%
MAE_30D  = -1.07%
MFE_90D  = +14.19%
MAE_90D  = -5.44%
MFE_180D = +14.19%
MAE_180D = -27.85%
peak_180 = 10,700 on 2024-03-18
trough_180 = 6,760 on 2024-08-05~2024-09-09
peak_to_later_drawdown = -36.82%
```

### Interpretation

This is a C28 B2B fintech software retention-fade row.  
The MFE was modest, and the later MAE suggests the retention/revenue bridge failed to refresh.

Correct treatment:

```text
B2B fintech software retention theme beta
→ no verified retention / usage / renewal / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
software_contract_retention_bridge_required = strengthen
ARR_renewal_churn_margin_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C28_software_theme_weight = true
do_not_treat_all_software_MFE_as_Green = true
do_not_force_4B_on_bounded_service_retention_rows_without_non_price_churn_or_margin_break = true
do_not_convert_software_drawdown_to_hard_4C_without_non_price_contract_churn_customer_loss_security_incident_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE
```

This fine archetype covers:

```text
1. IT outsourcing / managed-service retention with bounded MAE → Stage2-Yellow possible after source repair
2. ERP/cloud software theme beta without ARR/renewal bridge → false Stage2 / local 4B
3. B2B fintech software retention beta without customer usage/revenue bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L82-C28-094280-HYOSUNG-ITX-ITOUTSOURCING-CONTRACT-RETENTION-BOUNDED", "symbol": "094280", "company_name": "효성ITX", "round": "R8", "loop": "82", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "positive", "best_trigger": "RiskWatch-PositiveITOutsourcingContractRetentionNoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should allow software/IT service positives only when recurring contract retention, renewal, managed-service orderbook, revenue conversion and margin bridge are visible. Hyosung ITX had bounded MAE and later MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair rather than a forced 4B row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ARR, contract retention, renewal/churn, usage, implementation backlog, recurring revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L82-C28-060850-YOUNGLIMWON-ERP-CONTRACT-RETENTION-FADE", "symbol": "060850", "company_name": "영림원소프트랩", "round": "R8", "loop": "82", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ERPCloudContractRetentionThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should not treat ERP/cloud software theme beta as durable Stage2 unless ARR/subscription, renewal, churn control, implementation backlog, revenue conversion and margin bridge are visible. YoungLimWon had a theme spike and then high MAE, so it is local-4B unless retention economics are source-repaired.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ARR, contract retention, renewal/churn, usage, implementation backlog, recurring revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L82-C28-053580-WEBCASH-FINTECH-SOFTWARE-RETENTION-FADE", "symbol": "053580", "company_name": "웹케시", "round": "R8", "loop": "82", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / FintechSoftwareContractRetentionFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should not treat B2B fintech software retention theme beta as durable Stage2 unless customer retention, paid conversion, renewal, usage, revenue and margin bridge are visible. WebCash had modest MFE and then high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ARR, contract retention, renewal/churn, usage, implementation backlog, recurring revenue and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L82-C28-094280-HYOSUNG-ITX-ITOUTSOURCING-CONTRACT-RETENTION-BOUNDED", "case_id": "R8L82-C28-094280-HYOSUNG-ITX-ITOUTSOURCING-CONTRACT-RETENTION-BOUNDED", "symbol": "094280", "company_name": "효성ITX", "round": "R8", "loop": "82", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "RiskWatch-PositiveITOutsourcingContractRetentionNoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 12180.0, "evidence_available_at_that_date": "IT_OUTSOURCING_CONTACT_CENTER_MANAGED_SERVICE_CONTRACT_RETENTION_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYOSUNG_ITX_2024_IT_OUTSOURCING_CONTACT_CENTER_CONTRACT_RETENTION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["contract_retention_or_ARR_candidate", "renewal_churn_or_usage_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "implementation_backlog_or_customer_quality_candidate"], "stage4b_evidence_fields": ["software_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094280/2024.csv", "profile_path": "atlas/symbol_profiles/094/094280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.53, "MFE_90D_pct": 5.99, "MFE_180D_pct": 24.79, "MAE_30D_pct": -0.16, "MAE_90D_pct": -1.15, "MAE_180D_pct": -1.72, "peak_date": "2024-10-15", "peak_price": 15200.0, "drawdown_after_peak_pct": -18.88, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_software_contract_peak_if_ARR_retention_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_churn_customer_loss_margin_or_security_incident_break", "trigger_outcome_label": "positive_bounded_IT_outsourcing_contract_retention_no_forced4b", "current_profile_verdict": "C28 should allow software/IT service positives only when recurring contract retention, renewal, managed-service orderbook, revenue conversion and margin bridge are visible. Hyosung ITX had bounded MAE and later MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair rather than a forced 4B row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C28_SOFTWARE_RETENTION_094280_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L82-C28-060850-YOUNGLIMWON-ERP-CONTRACT-RETENTION-FADE", "case_id": "R8L82-C28-060850-YOUNGLIMWON-ERP-CONTRACT-RETENTION-FADE", "symbol": "060850", "company_name": "영림원소프트랩", "round": "R8", "loop": "82", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "Stage2-FalsePositive / ERPCloudContractRetentionThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 9270.0, "evidence_available_at_that_date": "ERP_CLOUD_SOFTWARE_CONTRACT_RETENTION_THEME_WITH_WEAK_ARR_RENEWAL_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:YOUNGLIMWON_SOFTLAB_2024_ERP_CLOUD_ARR_RENEWAL_CHURN_IMPLEMENTATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["contract_retention_or_ARR_candidate", "renewal_churn_or_usage_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "implementation_backlog_or_customer_quality_candidate"], "stage4b_evidence_fields": ["software_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/060/060850/2024.csv", "profile_path": "atlas/symbol_profiles/060/060850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.08, "MFE_90D_pct": 21.57, "MFE_180D_pct": 21.57, "MAE_30D_pct": -7.77, "MAE_90D_pct": -11.0, "MAE_180D_pct": -27.94, "peak_date": "2024-04-05", "peak_price": 11270.0, "drawdown_after_peak_pct": -40.73, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_software_contract_peak_if_ARR_retention_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_churn_customer_loss_margin_or_security_incident_break", "trigger_outcome_label": "counterexample_ERP_cloud_retention_theme_local4b", "current_profile_verdict": "C28 should not treat ERP/cloud software theme beta as durable Stage2 unless ARR/subscription, renewal, churn control, implementation backlog, revenue conversion and margin bridge are visible. YoungLimWon had a theme spike and then high MAE, so it is local-4B unless retention economics are source-repaired.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C28_SOFTWARE_RETENTION_060850_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L82-C28-053580-WEBCASH-FINTECH-SOFTWARE-RETENTION-FADE", "case_id": "R8L82-C28-053580-WEBCASH-FINTECH-SOFTWARE-RETENTION-FADE", "symbol": "053580", "company_name": "웹케시", "round": "R8", "loop": "82", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "Stage2-FalsePositive / FintechSoftwareContractRetentionFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 9370.0, "evidence_available_at_that_date": "B2B_FINTECH_SOFTWARE_CONTRACT_RETENTION_THEME_WITH_WEAK_CUSTOMER_RENEWAL_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WEBCASH_2024_B2B_FINTECH_SOFTWARE_CUSTOMER_RETENTION_USAGE_RENEWAL_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["contract_retention_or_ARR_candidate", "renewal_churn_or_usage_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "implementation_backlog_or_customer_quality_candidate"], "stage4b_evidence_fields": ["software_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053580/2024.csv", "profile_path": "atlas/symbol_profiles/053/053580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.09, "MFE_90D_pct": 14.19, "MFE_180D_pct": 14.19, "MAE_30D_pct": -1.07, "MAE_90D_pct": -5.44, "MAE_180D_pct": -27.85, "peak_date": "2024-03-18", "peak_price": 10700.0, "drawdown_after_peak_pct": -36.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_software_contract_peak_if_ARR_retention_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_churn_customer_loss_margin_or_security_incident_break", "trigger_outcome_label": "counterexample_fintech_software_retention_theme_local4b", "current_profile_verdict": "C28 should not treat B2B fintech software retention theme beta as durable Stage2 unless customer retention, paid conversion, renewal, usage, revenue and margin bridge are visible. WebCash had modest MFE and then high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C28_SOFTWARE_RETENTION_053580_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L82-C28-094280-HYOSUNG-ITX-ITOUTSOURCING-CONTRACT-RETENTION-BOUNDED", "trigger_id": "TRG_R8L82-C28-094280-HYOSUNG-ITX-ITOUTSOURCING-CONTRACT-RETENTION-BOUNDED", "symbol": "094280", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"ARR_contract_retention_score": 13, "renewal_churn_score": 12, "customer_usage_score": 12, "implementation_backlog_score": 11, "revenue_margin_bridge_score": 12, "relative_strength_score": 8, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_before": 70, "stage_label_before": "RiskWatch / Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"ARR_contract_retention_score": 15, "renewal_churn_score": 14, "customer_usage_score": 14, "implementation_backlog_score": 13, "revenue_margin_bridge_score": 14, "relative_strength_score": 7, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_after": 76, "stage_label_after": "Stage2-Yellow only after source repair / no forced 4B", "changed_components": ["ARR_contract_retention_score", "renewal_churn_score", "customer_usage_score", "implementation_backlog_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ARR/contract retention, renewal/churn control, customer usage, implementation backlog, recurring revenue and margin bridge; cap software theme beta when retention evidence is weak or stale.", "MFE_90D_pct": 5.99, "MAE_90D_pct": -1.15, "score_return_alignment_label": "software_contract_retention_bounded_candidate", "current_profile_verdict": "C28 should allow software/IT service positives only when recurring contract retention, renewal, managed-service orderbook, revenue conversion and margin bridge are visible. Hyosung ITX had bounded MAE and later MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair rather than a forced 4B row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L82-C28-060850-YOUNGLIMWON-ERP-CONTRACT-RETENTION-FADE", "trigger_id": "TRG_R8L82-C28-060850-YOUNGLIMWON-ERP-CONTRACT-RETENTION-FADE", "symbol": "060850", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"ARR_contract_retention_score": 4, "renewal_churn_score": 3, "customer_usage_score": 2, "implementation_backlog_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 8, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"ARR_contract_retention_score": 2, "renewal_churn_score": 1, "customer_usage_score": 1, "implementation_backlog_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["ARR_contract_retention_score", "renewal_churn_score", "customer_usage_score", "implementation_backlog_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ARR/contract retention, renewal/churn control, customer usage, implementation backlog, recurring revenue and margin bridge; cap software theme beta when retention evidence is weak or stale.", "MFE_90D_pct": 21.57, "MAE_90D_pct": -11.0, "score_return_alignment_label": "software_contract_retention_theme_false_positive", "current_profile_verdict": "C28 should not treat ERP/cloud software theme beta as durable Stage2 unless ARR/subscription, renewal, churn control, implementation backlog, revenue conversion and margin bridge are visible. YoungLimWon had a theme spike and then high MAE, so it is local-4B unless retention economics are source-repaired."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L82-C28-053580-WEBCASH-FINTECH-SOFTWARE-RETENTION-FADE", "trigger_id": "TRG_R8L82-C28-053580-WEBCASH-FINTECH-SOFTWARE-RETENTION-FADE", "symbol": "053580", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"ARR_contract_retention_score": 4, "renewal_churn_score": 3, "customer_usage_score": 2, "implementation_backlog_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"ARR_contract_retention_score": 2, "renewal_churn_score": 1, "customer_usage_score": 1, "implementation_backlog_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["ARR_contract_retention_score", "renewal_churn_score", "customer_usage_score", "implementation_backlog_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ARR/contract retention, renewal/churn control, customer usage, implementation backlog, recurring revenue and margin bridge; cap software theme beta when retention evidence is weak or stale.", "MFE_90D_pct": 14.19, "MAE_90D_pct": -5.44, "score_return_alignment_label": "software_contract_retention_theme_false_positive", "current_profile_verdict": "C28 should not treat B2B fintech software retention theme beta as durable Stage2 unless customer retention, paid conversion, renewal, usage, revenue and margin bridge are visible. WebCash had modest MFE and then high-MAE fade."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 82, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_FINTECH_ITOUTSOURCING_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C28 software/contract-retention symbols outside top-covered 012510/053800/263860/030520/131370/042510 set, +3 IT-outsourcing/ERP/B2B-fintech trigger families, +1 bounded contract-retention candidate, +2 software theme-retention local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 82, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "axis": "ERP_fintech_IToutsourcing_contract_retention_margin_bridge_vs_software_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C28 should split verified ARR/contract-retention and recurring-margin rerating from generic software theme beta. Stage2 requires contract retention or ARR, renewal/churn control, customer usage, implementation backlog, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Bounded service rows should not be forced into 4B without non-price churn or margin break evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["094280", "060850", "053580"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 82, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "existing_axis_strengthened": ["stage2_required_bridge", "software_contract_retention_bridge_required", "ARR_renewal_churn_margin_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_MAE_no_forced_4B_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C28 needs software/service MFE to map into ARR, retention, renewal, churn control, implementation backlog, recurring revenue and margin proof. Hyosung ITX is a bounded service-retention candidate after source repair; YoungLimWon and WebCash show ERP/B2B-fintech software theme beta fading into local 4B when retention economics are absent or stale."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
094280:
  name = 효성ITX
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

060850:
  name = 영림원소프트랩
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

053580:
  name = 웹케시
  corporate_action_candidate_dates = 2021-05-04, 2021-06-03
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C28 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C28 software/contract-retention rule-shape discovery,
but coding-agent promotion requires non-proxy ARR, contract retention, renewal/churn, usage, implementation backlog, recurring revenue and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C28 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
ERP_fintech_IToutsourcing_contract_retention_margin_bridge_vs_software_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 094280, 060850 and 053580.
4. Keep generic C28 software/security/contract-retention weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - ARR or recurring contract base is explicit,
   - renewal/churn control is visible,
   - customer usage and implementation backlog are visible,
   - revenue conversion and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is software theme beta only,
   - ARR / renewal / usage / revenue / margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not force local 4B when bounded service-retention rows have controlled MAE and no confirmed non-price churn or margin break.
8. Do not convert local 4B-watch into full 4B/4C without non-price contract churn, customer loss, security incident, financing or margin break.
9. Emit before/after diagnostics and reject if verified ARR/retention positives or bounded service rows are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 82
next_round = R9
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

