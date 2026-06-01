# E2R Stock-Web v12 Residual Research — R8 Loop 75 / L8 / C28

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 75,
  "computed_next_round": "R9",
  "computed_next_loop": 75,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "software_security_contract_retention_guardrail",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R7 / loop 75.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 75
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
computed_next_round = R9
computed_next_loop = 75
```

R8 was routed to C28 because loop 74 used C27 and prior loop work already touched C26.  
This file tests software/security contract-retention, not generic platform ad revenue or content monetization.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C28 is concentrated in:

```text
012510, 053800, 263860, 131370, 030520
```

This run uses three different symbols:

```text
058970 / 엠로 / procurement SaaS AI contract-retention bridge
047560 / 이스트소프트 / AI software/avatar theme-spike fade
067920 / 이글루 / cybersecurity SIEM/SOC theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
058970 and 047560 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C28 is not “software stock went up.”

The mechanism must pass through:

```text
software / security product
→ enterprise contract or managed-service renewal
→ ARR / license / paid-seat / customer expansion
→ margin conversion
→ durable rerating
```

A software demo is a spark.  
Contract retention is the furnace that keeps heat in the building.

---

## Case 1 — Delayed positive: 058970 / 엠로

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is procurement SaaS / AI supply-chain contract retention, customer expansion, recurring license and margin bridge evidence.

```text
evidence_family = PROCUREMENT_SAAS_AI_SUPPLY_CHAIN_CONTRACT_RETENTION_CUSTOMER_EXPANSION_MARGIN_BRIDGE
case_role = delayed_positive_with_sharecount_validation
trigger_date = 2024-08-12
entry_date = 2024-08-13
entry_price = 43,050
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/058/058970/2024.csv`:

```text
2024-08-13,43050,44700,41000,42600
2024-09-26,54000,54600,53500,54400
2024-11-18,68800,72600,66900,67800
2024-11-27,66500,72300,65500,71400
2024-12-20,61100,62400,59000,61100
```

### Backtest

```text
MFE_30D  = +26.83%
MAE_30D  = -4.76%
MFE_90D  = +68.64%
MAE_90D  = -4.76%
MFE_180D = +68.64%
MAE_180D = -4.76%
peak_180 = 72,600 on 2024-11-18
trough_180 = 41,000 on 2024-08-13
peak_to_later_drawdown = -18.73%
```

### Interpretation

This is the C28 positive side.  
The price path was not only a one-day software spike. It had controlled MAE and multi-month follow-through.

But runtime promotion still requires source repair and share-count validation:

```text
enterprise contract retention
ARR/license bridge
customer expansion
margin conversion
```

---

## Case 2 — Counterexample / local 4B: 047560 / 이스트소프트

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests AI software/avatar theme MFE without enough enterprise contract retention or paid-seat bridge.

```text
evidence_family = AI_AVATAR_SOFTWARE_THEME_SPIKE_WITH_WEAK_ENTERPRISE_CONTRACT_RETENTION_MARGIN_BRIDGE
case_role = counterexample_theme_spike_local4b_with_sharecount_validation
trigger_date = 2024-01-04
entry_date = 2024-01-05
entry_price = 15,230
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv`:

```text
2024-01-05,15230,19740,15230,19740
2024-01-19,31300,39100,30300,39100
2024-01-29,46100,49800,36500,41300
2024-08-05,14000,14010,11220,11900
2024-09-25,13210,15990,13100,14380
```

### Backtest

```text
MFE_30D  = +227.00%
MAE_30D  = +0.00%
MFE_90D  = +227.00%
MAE_90D  = +0.00%
MFE_180D = +227.00%
MAE_180D = -26.33%
peak_180 = 49,800 on 2024-01-29
trough_180 = 11,220 on 2024-08-05
peak_to_later_drawdown = -77.47%
```

### Interpretation

This is the dangerous C28 false-positive shape.  
A huge MFE can make a model think the signal was durable. But without contract retention, paid-seat expansion, ARR/license and margin bridge, this is not Green.

Correct treatment:

```text
theme-spike MFE
→ source repair required
→ local 4B-watch after bridge fade
```

---

## Case 3 — Counterexample / local 4B: 067920 / 이글루

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests cybersecurity/SIEM/SOC theme beta without recurring contract-retention or managed-service backlog evidence.

```text
evidence_family = CYBERSECURITY_SIEM_SOC_THEME_SPIKE_WITH_WEAK_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE
case_role = counterexample_security_theme_local4b
trigger_date = 2024-01-12
entry_date = 2024-01-15
entry_price = 6,660
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/067/067920/2024.csv`:

```text
2024-01-15,6660,7680,6560,6750
2024-01-23,7350,8080,7190,7930
2024-01-29,7980,8680,7100,7180
2024-03-19,6220,6300,6170,6260
2024-08-05,5400,5400,4925,4925
```

### Backtest

```text
MFE_30D  = +30.33%
MAE_30D  = -5.56%
MFE_90D  = +30.33%
MAE_90D  = -7.36%
MFE_180D = +30.33%
MAE_180D = -26.05%
peak_180 = 8,680 on 2024-01-29
trough_180 = 4,925 on 2024-08-05
peak_to_later_drawdown = -43.26%
```

### Interpretation

This is the security-theme version of local 4B.  
The early move was tradable, but recurring retention and margin bridge did not hold.

C28 should not convert this kind of cybersecurity beta into durable Stage2 unless renewal rate, ARR/MRR, managed-security backlog or margin bridge is verified.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C28_software_security_weight = true
do_not_treat_all_AI_or_security_MFE_as_Green = true
do_not_convert_software_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE
```

This fine archetype covers:

```text
1. procurement SaaS / AI supply-chain contract retention → delayed Stage2 possible after source repair
2. AI avatar/software theme spike without ARR/paid-seat bridge → false Stage2 / local 4B
3. cybersecurity/SIEM theme spike without recurring retention bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE", "symbol": "058970", "company_name": "엠로", "round": "R8", "loop": "75", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "delayed_positive", "best_trigger": "Stage2-DelayedPositive-ProcurementSaaSContractRetentionBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should allow a delayed Stage2 when procurement SaaS / supply-chain AI demand connects to actual enterprise contract retention, customer expansion, recurring license or margin bridge. EMRO produced controlled-MAE follow-through after the August reset, but the price shard shows share-count changes, so runtime promotion needs validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ARR/license, contract renewal, retention, paid-seat, customer expansion, managed security and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE", "symbol": "047560", "company_name": "이스트소프트", "round": "R8", "loop": "75", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AISoftwareThemeSpikeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should not treat AI software/avatar headline MFE as durable Stage2 unless enterprise contract retention, paid seat expansion, ARR/license revenue or margin bridge is visible. ESTsoft produced an enormous MFE, but later drawdown shows that theme-spike winners need lifecycle local 4B when bridge evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ARR/license, contract renewal, retention, paid-seat, customer expansion, managed security and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE", "symbol": "067920", "company_name": "이글루", "round": "R8", "loop": "75", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CybersecurityContractRetentionBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should not treat cybersecurity/SIEM/SOC theme spikes as durable Stage2 unless recurring contract retention, renewal rate, managed security service backlog or margin bridge is visible. IGLOO had a strong early MFE but then faded into high MAE and post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ARR/license, contract renewal, retention, paid-seat, customer expansion, managed security and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE", "case_id": "R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE", "symbol": "058970", "company_name": "엠로", "round": "R8", "loop": "75", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "Stage2-DelayedPositive-ProcurementSaaSContractRetentionBridge", "trigger_date": "2024-08-12", "entry_date": "2024-08-13", "entry_price": 43050.0, "evidence_available_at_that_date": "PROCUREMENT_SAAS_AI_SUPPLY_CHAIN_CONTRACT_RETENTION_CUSTOMER_EXPANSION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:EMRO_2024_PROCUREMENT_SAAS_AI_SUPPLY_CHAIN_ENTERPRISE_CONTRACT_RETENTION_MARGIN_BRIDGE", "stage2_evidence_fields": ["software_or_security_contract_candidate", "retention_or_renewal_candidate", "ARR_license_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_expansion_or_paid_seat_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "theme_spike", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058970/2024.csv", "profile_path": "atlas/symbol_profiles/058/058970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.83, "MFE_90D_pct": 68.64, "MFE_180D_pct": 68.64, "MAE_30D_pct": -4.76, "MAE_90D_pct": -4.76, "MAE_180D_pct": -4.76, "peak_date": "2024-11-18", "peak_price": 72600.0, "drawdown_after_peak_pct": -18.73, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_software_or_security_peak_if_contract_retention_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_loss_retention_collapse_customer_churn_or_margin_break", "trigger_outcome_label": "delayed_positive_with_sharecount_validation", "current_profile_verdict": "C28 should allow a delayed Stage2 when procurement SaaS / supply-chain AI demand connects to actual enterprise contract retention, customer expansion, recurring license or margin bridge. EMRO produced controlled-MAE follow-through after the August reset, but the price shard shows share-count changes, so runtime promotion needs validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C28_SW_SECURITY_RETENTION_058970_2024-08-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE", "case_id": "R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE", "symbol": "047560", "company_name": "이스트소프트", "round": "R8", "loop": "75", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "Stage2-FalsePositive / AISoftwareThemeSpikeFade", "trigger_date": "2024-01-04", "entry_date": "2024-01-05", "entry_price": 15230.0, "evidence_available_at_that_date": "AI_AVATAR_SOFTWARE_THEME_SPIKE_WITH_WEAK_ENTERPRISE_CONTRACT_RETENTION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ESTSOFT_2024_AI_AVATAR_SOFTWARE_ENTERPRISE_CONTRACT_RETENTION_PAID_SEAT_MARGIN_BRIDGE", "stage2_evidence_fields": ["software_or_security_contract_candidate", "retention_or_renewal_candidate", "ARR_license_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_expansion_or_paid_seat_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "theme_spike", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv", "profile_path": "atlas/symbol_profiles/047/047560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 227.0, "MFE_90D_pct": 227.0, "MFE_180D_pct": 227.0, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -26.33, "peak_date": "2024-01-29", "peak_price": 49800.0, "drawdown_after_peak_pct": -77.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_software_or_security_peak_if_contract_retention_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_loss_retention_collapse_customer_churn_or_margin_break", "trigger_outcome_label": "counterexample_theme_spike_local4b_with_sharecount_validation", "current_profile_verdict": "C28 should not treat AI software/avatar headline MFE as durable Stage2 unless enterprise contract retention, paid seat expansion, ARR/license revenue or margin bridge is visible. ESTsoft produced an enormous MFE, but later drawdown shows that theme-spike winners need lifecycle local 4B when bridge evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C28_SW_SECURITY_RETENTION_047560_2024-01-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE", "case_id": "R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE", "symbol": "067920", "company_name": "이글루", "round": "R8", "loop": "75", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "Stage2-FalsePositive / CybersecurityContractRetentionBetaFade", "trigger_date": "2024-01-12", "entry_date": "2024-01-15", "entry_price": 6660.0, "evidence_available_at_that_date": "CYBERSECURITY_SIEM_SOC_THEME_SPIKE_WITH_WEAK_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:IGLOO_2024_CYBERSECURITY_SIEM_SOC_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE", "stage2_evidence_fields": ["software_or_security_contract_candidate", "retention_or_renewal_candidate", "ARR_license_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_expansion_or_paid_seat_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "theme_spike", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067920/2024.csv", "profile_path": "atlas/symbol_profiles/067/067920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 30.33, "MFE_90D_pct": 30.33, "MFE_180D_pct": 30.33, "MAE_30D_pct": -5.56, "MAE_90D_pct": -7.36, "MAE_180D_pct": -26.05, "peak_date": "2024-01-29", "peak_price": 8680.0, "drawdown_after_peak_pct": -43.26, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_software_or_security_peak_if_contract_retention_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_loss_retention_collapse_customer_churn_or_margin_break", "trigger_outcome_label": "counterexample_security_theme_local4b", "current_profile_verdict": "C28 should not treat cybersecurity/SIEM/SOC theme spikes as durable Stage2 unless recurring contract retention, renewal rate, managed security service backlog or margin bridge is visible. IGLOO had a strong early MFE but then faded into high MAE and post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C28_SW_SECURITY_RETENTION_067920_2024-01-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE", "trigger_id": "TRG_R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE", "symbol": "058970", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 14, "ARR_or_license_score": 13, "customer_expansion_score": 12, "margin_bridge_score": 12, "relative_strength_score": 13, "execution_risk_score": 6, "theme_spike_risk_score": 7, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Delayed Stage2 candidate after source repair", "raw_component_scores_after": {"contract_retention_score": 16, "ARR_or_license_score": 15, "customer_expansion_score": 14, "margin_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 7, "theme_spike_risk_score": 8, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 87, "stage_label_after": "Delayed Stage2/Yellow candidate after source repair + share-count validation", "changed_components": ["contract_retention_score", "ARR_or_license_score", "margin_bridge_score", "execution_risk_score", "theme_spike_risk_score"], "component_delta_explanation": "Reward only verified software/security contract retention, ARR/license, renewal, paid-seat/customer expansion and margin bridge; cap AI/security theme spikes when retention evidence is absent.", "MFE_90D_pct": 68.64, "MAE_90D_pct": -4.76, "score_return_alignment_label": "delayed_positive_contract_retention_bridge", "current_profile_verdict": "C28 should allow a delayed Stage2 when procurement SaaS / supply-chain AI demand connects to actual enterprise contract retention, customer expansion, recurring license or margin bridge. EMRO produced controlled-MAE follow-through after the August reset, but the price shard shows share-count changes, so runtime promotion needs validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE", "trigger_id": "TRG_R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE", "symbol": "047560", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 4, "ARR_or_license_score": 3, "customer_expansion_score": 4, "margin_bridge_score": 2, "relative_strength_score": 14, "execution_risk_score": 18, "theme_spike_risk_score": 19, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 53, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_retention_score": 2, "ARR_or_license_score": 1, "customer_expansion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 20, "theme_spike_risk_score": 22, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["contract_retention_score", "ARR_or_license_score", "margin_bridge_score", "execution_risk_score", "theme_spike_risk_score"], "component_delta_explanation": "Reward only verified software/security contract retention, ARR/license, renewal, paid-seat/customer expansion and margin bridge; cap AI/security theme spikes when retention evidence is absent.", "MFE_90D_pct": 227.0, "MAE_90D_pct": 0.0, "score_return_alignment_label": "false_positive_theme_spike_retention_bridge_gap", "current_profile_verdict": "C28 should not treat AI software/avatar headline MFE as durable Stage2 unless enterprise contract retention, paid seat expansion, ARR/license revenue or margin bridge is visible. ESTsoft produced an enormous MFE, but later drawdown shows that theme-spike winners need lifecycle local 4B when bridge evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE", "trigger_id": "TRG_R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE", "symbol": "067920", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 4, "ARR_or_license_score": 3, "customer_expansion_score": 4, "margin_bridge_score": 2, "relative_strength_score": 14, "execution_risk_score": 18, "theme_spike_risk_score": 19, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 53, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_retention_score": 2, "ARR_or_license_score": 1, "customer_expansion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 20, "theme_spike_risk_score": 22, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["contract_retention_score", "ARR_or_license_score", "margin_bridge_score", "execution_risk_score", "theme_spike_risk_score"], "component_delta_explanation": "Reward only verified software/security contract retention, ARR/license, renewal, paid-seat/customer expansion and margin bridge; cap AI/security theme spikes when retention evidence is absent.", "MFE_90D_pct": 30.33, "MAE_90D_pct": -7.36, "score_return_alignment_label": "false_positive_theme_spike_retention_bridge_gap", "current_profile_verdict": "C28 should not treat cybersecurity/SIEM/SOC theme spikes as durable Stage2 unless recurring contract retention, renewal rate, managed security service backlog or margin bridge is visible. IGLOO had a strong early MFE but then faded into high MAE and post-peak drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 75, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C28 software/security symbols outside top-covered set, +3 procurement SaaS/AI avatar/cybersecurity trigger families, +1 delayed contract-retention positive, +2 AI/security theme-spike local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 75, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "axis": "procurement_saas_ai_software_security_contract_retention_vs_theme_spike_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C28 should split verified SaaS/security contract-retention rerating from AI/software/security theme spikes. Stage2 requires ARR/license, contract renewal, paid-seat expansion, customer expansion, managed security backlog or margin bridge. If MFE fades and MAE/post-peak drawdown opens without retention evidence, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["058970", "047560", "067920"], "share_count_validation_required": ["058970", "047560"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 75, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C28 needs contract-retention proof. EMRO shows a procurement SaaS delayed positive after source repair; ESTsoft and IGLOO show AI/software/security theme MFE fading into local 4B when ARR, renewal, contract retention or margin bridge is absent."}
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
058970:
  corporate_action_candidate_dates = 2022-01-17, 2022-02-09
  selected window = 2024-08-13~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

047560:
  corporate_action_candidate_dates = 2015-05-06, 2015-05-27
  selected window = 2024-01-05~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

067920:
  corporate_action_candidate_dates = 2014-04-24
  selected window = 2024-01-15~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C28 rows are source_proxy_only / evidence_url_pending.
058970 and 047560 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C28 rule-shape discovery,
but coding-agent promotion requires non-proxy ARR/license, contract renewal, retention, paid-seat, customer expansion, managed security and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C28 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and two rows need share-count validation.

Candidate axis:
procurement_saas_ai_software_security_contract_retention_vs_theme_spike_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 058970, 047560 and 067920.
4. Validate 058970 and 047560 share-count changes inside the selected window.
5. Keep generic C28 software/security weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - enterprise contract or managed security contract is explicit,
   - ARR/license/paid-seat/customer expansion bridge is visible,
   - renewal/retention or backlog is credible,
   - margin conversion exists,
   - MAE remains controlled or the signal is deliberately delayed after early reset.
7. Consider local 4B-watch when:
   - the trigger is AI/software/security theme spike only,
   - retention/ARR/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price contract loss, churn spike, renewal failure, ARR decline, customer loss, security project cancellation, financing or margin break.
9. Emit before/after diagnostics and reject if verified SaaS/security contract-retention positives are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 75
next_round = R9
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

