# E2R Stock-Web v12 Residual Research — R2 Loop 73 / L2 / C08

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 73,
  "computed_next_round": "R3",
  "computed_next_loop": 73,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
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
```

## Round / scope resolution

Previous completed state in this interactive run: R1 / loop 73.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 73
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
computed_next_round = R3
computed_next_loop = 73
```

R2 was routed to C08 because No-Repeat already shows C08 coverage is concentrated in a small symbol set, while loop 72 had filled C10.  
This run avoids repeating the heaviest C08 symbols and tests a broader customer-quality boundary: tester, consumable, and OSAT/package beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
092870 / 엑시콘 / Stage2-Actionable-TesterAdoptionBridgeAfterCA / 2024-09-06
064760 / 티씨케이 / Stage2-FalsePositive / ConsumableCustomerQualityLocal4B / 2024-06-12
067310 / 하나마이크론 / Stage2-FalsePositive / OSATPackagingBetaWeakUtilization / 2024-04-11
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
092870 has a corporate-action candidate on 2024-07-31, but this artifact uses a post-CA entry date, 2024-09-06, so the selected 180D window is not blocked by that candidate.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C08 is not “semiconductor subcomponent went up.”

The true mechanism is:

```text
test / socket / consumable / packaging function
→ customer-quality evidence
→ adoption, reorder, utilization, or margin conversion
→ durable rerating
```

A tester with real adoption is a sensor plugged into the fab.  
A packaging or consumable beta without utilization proof is just a blinking light on the dashboard.

The residual split is:

```text
C08 positive:
  verified customer adoption/reorder/utilization/margin bridge
  + controlled MAE

C08 false positive:
  HBM/package/consumable beta
  + no customer-quality bridge
  + high MAE or post-peak drawdown

C08 local 4B:
  initial MFE fades before adoption/utilization bridge refreshes
```

---

## Case 1 — Positive after source repair: 092870 / 엑시콘

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is memory/HBM tester customer adoption, reorder, and margin conversion.  
The selected entry is after the 2024-07-31 corporate-action candidate.

```text
evidence_family = MEMORY_HBM_TESTER_CUSTOMER_ADOPTION_REORDER_BRIDGE_POST_CORPORATE_ACTION
case_role = positive_after_source_repair
trigger_date = 2024-09-05
entry_date = 2024-09-06
entry_price = 10,720
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv` and `2025.csv`:

```text
2024-09-06,10720,10900,10300,10400
2024-09-26,12420,14660,12110,13810
2025-02-14,14730,15760,13510,14030
2025-04-07,10550,10550,9790,9800
```

### Backtest

```text
MFE_30D  = +36.75%
MAE_30D  = -6.72%
MFE_90D  = +36.75%
MAE_90D  = -6.72%
MFE_180D = +47.01%
MAE_180D = -8.68%
peak_180 = 15,760 on 2025-02-14
trough_180 = 9,790 on 2025-04-07
peak_to_later_drawdown = -37.88%
```

### Interpretation

This is the cleanest positive path in this R2 file.  
It still needs source repair, but the price path says a tester adoption/reorder bridge could justify Stage2. The later post-peak drawdown means the lifecycle should still allow local 4B-watch if the bridge stops refreshing.

---

## Case 2 — Counterexample / local 4B: 064760 / 티씨케이

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The row tests whether high-quality semiconductor consumables can be treated as Green without near-term customer utilization or margin bridge.

```text
evidence_family = SIC_RING_CONSUMABLE_CUSTOMER_QUALITY_WITH_WEAK_NEAR_TERM_MARGIN_UTILIZATION_BRIDGE
case_role = counterexample
trigger_date = 2024-06-11
entry_date = 2024-06-12
entry_price = 123,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv` and `2025.csv`:

```text
2024-06-12,123500,135000,123100,133200
2024-06-14,129800,149900,129300,141400
2024-09-10,89800,91600,87100,88500
2025-01-15,71900,72500,68400,69900
```

### Backtest

```text
MFE_30D  = +21.38%
MAE_30D  = -6.88%
MFE_90D  = +21.38%
MAE_90D  = -29.47%
MFE_180D = +21.38%
MAE_180D = -44.62%
peak_180 = 149,900 on 2024-06-14
trough_180 = 68,400 on 2025-01-15
peak_to_later_drawdown = -54.37%
```

### Interpretation

This is a C08 quality-name trap.  
A good part category is not enough if utilization and margin conversion do not show up.

The correct label is:

```text
false Stage2 / local 4B-watch
```

not durable Green.

---

## Case 3 — Counterexample: 067310 / 하나마이크론

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests OSAT/HBM packaging beta without verified utilization, customer-quality, package-mix, or margin bridge.

```text
evidence_family = OSAT_PACKAGING_HBM_BETA_WITH_WEAK_UTILIZATION_AND_MARGIN_BRIDGE
case_role = counterexample
trigger_date = 2024-04-10
entry_date = 2024-04-11
entry_price = 29,850
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv` and `2025.csv`:

```text
2024-04-11,29850,31950,29800,31500
2024-05-31,21500,21650,21100,21150
2024-08-05,18610,18880,15400,15950
2025-01-02,9240,9310,9030,9250
```

### Backtest

```text
MFE_30D  = +7.04%
MAE_30D  = -29.31%
MFE_90D  = +7.04%
MAE_90D  = -48.41%
MFE_180D = +7.04%
MAE_180D = -69.75%
peak_180 = 31,950 on 2024-04-11
trough_180 = 9,030 on 2025-01-02
peak_to_later_drawdown = -71.74%
```

### Interpretation

This is the hard false-positive path in this C08 set.  
The stock did not give the model time to be right. A one-day high was followed by a long utilization/margin bridge failure.

For C08, OSAT/HBM package beta should remain capped unless there is explicit customer-quality or margin conversion evidence.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C08_weight = true
do_not_treat_all_HBM_package_or_consumable_beta_as_Green = true
do_not_convert_local_4B_test_socket_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION
```

This fine archetype covers:

```text
1. post-CA tester adoption/reorder bridge → Stage2 possible after source repair
2. high-quality consumable without utilization/margin refresh → false Stage2 / local 4B
3. OSAT/HBM packaging beta without customer-quality proof → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE", "symbol": "092870", "company_name": "엑시콘", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-TesterAdoptionBridgeAfterCA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 can permit Stage2 when tester demand is tied to verified customer adoption/reorder and the entry window is after corporate-action contamination. Exicon's post-CA path had strong MFE with controlled MAE, but source repair is required before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer adoption/utilization/margin evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B", "symbol": "064760", "company_name": "티씨케이", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ConsumableCustomerQualityLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 should not treat high-quality semi consumables as Green when near-term customer utilization or margin bridge is absent. TCK had an initial MFE but later opened large MAE and drawdown, requiring local 4B-watch rather than durable Stage2.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer adoption/utilization/margin evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION", "symbol": "067310", "company_name": "하나마이크론", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / OSATPackagingBetaWeakUtilization", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 must not allow OSAT/HBM packaging beta to become durable Stage2 without utilization, customer quality, margin, or package mix evidence. Hana Micron generated only small MFE and then severe MAE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer adoption/utilization/margin evidence must be attached before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE", "case_id": "R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE", "symbol": "092870", "company_name": "엑시콘", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-TesterAdoptionBridgeAfterCA", "trigger_date": "2024-09-05", "entry_date": "2024-09-06", "entry_price": 10720.0, "evidence_available_at_that_date": "MEMORY_HBM_TESTER_CUSTOMER_ADOPTION_REORDER_BRIDGE_POST_CORPORATE_ACTION", "evidence_source": "source_proxy_manual_verification_required:EXICON_2024_HBM_MEMORY_TESTER_CUSTOMER_ADOPTION_REORDER_BRIDGE_AFTER_20240731_CA", "stage2_evidence_fields": ["semi_customer_quality", "test_or_consumable_or_packaging_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_reorder_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv", "profile_path": "atlas/symbol_profiles/092/092870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.75, "MFE_90D_pct": 36.75, "MFE_180D_pct": 47.01, "MAE_30D_pct": -6.72, "MAE_90D_pct": -6.72, "MAE_180D_pct": -8.68, "peak_date": "2025-02-14", "peak_price": 15760.0, "drawdown_after_peak_pct": -37.88, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_customer_bridge_fails_or_peak_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_break", "trigger_outcome_label": "positive_after_source_repair", "current_profile_verdict": "C08 can permit Stage2 when tester demand is tied to verified customer adoption/reorder and the entry window is after corporate-action contamination. Exicon's post-CA path had strong MFE with controlled MAE, but source repair is required before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_092870_2024-09-06", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B", "case_id": "R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B", "symbol": "064760", "company_name": "티씨케이", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / ConsumableCustomerQualityLocal4B", "trigger_date": "2024-06-11", "entry_date": "2024-06-12", "entry_price": 123500.0, "evidence_available_at_that_date": "SIC_RING_CONSUMABLE_CUSTOMER_QUALITY_WITH_WEAK_NEAR_TERM_MARGIN_UTILIZATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TCK_2024_SIC_RING_CONSUMABLE_CUSTOMER_QUALITY_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["semi_customer_quality", "test_or_consumable_or_packaging_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_reorder_candidate"], "stage4b_evidence_fields": ["bridge_absent_or_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv", "profile_path": "atlas/symbol_profiles/064/064760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.38, "MFE_90D_pct": 21.38, "MFE_180D_pct": 21.38, "MAE_30D_pct": -6.88, "MAE_90D_pct": -29.47, "MAE_180D_pct": -44.62, "peak_date": "2024-06-14", "peak_price": 149900.0, "drawdown_after_peak_pct": -54.37, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_customer_bridge_fails_or_peak_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C08 should not treat high-quality semi consumables as Green when near-term customer utilization or margin bridge is absent. TCK had an initial MFE but later opened large MAE and drawdown, requiring local 4B-watch rather than durable Stage2.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_064760_2024-06-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION", "case_id": "R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION", "symbol": "067310", "company_name": "하나마이크론", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / OSATPackagingBetaWeakUtilization", "trigger_date": "2024-04-10", "entry_date": "2024-04-11", "entry_price": 29850.0, "evidence_available_at_that_date": "OSAT_PACKAGING_HBM_BETA_WITH_WEAK_UTILIZATION_AND_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANAMICRON_2024_OSAT_PACKAGING_HBM_BETA_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["semi_customer_quality", "test_or_consumable_or_packaging_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_reorder_candidate"], "stage4b_evidence_fields": ["bridge_absent_or_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv", "profile_path": "atlas/symbol_profiles/067/067310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.04, "MFE_90D_pct": 7.04, "MFE_180D_pct": 7.04, "MAE_30D_pct": -29.31, "MAE_90D_pct": -48.41, "MAE_180D_pct": -69.75, "peak_date": "2024-04-11", "peak_price": 31950.0, "drawdown_after_peak_pct": -71.74, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_customer_bridge_fails_or_peak_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C08 must not allow OSAT/HBM packaging beta to become durable Stage2 without utilization, customer quality, margin, or package mix evidence. Hana Micron generated only small MFE and then severe MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_067310_2024-04-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE", "trigger_id": "TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE", "symbol": "092870", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 13, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 10, "revision_score": 9, "relative_strength_score": 13, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer-quality/adoption/reorder evidence; cap HBM/package/consumable beta when utilization or margin bridge is stale.", "MFE_90D_pct": 36.75, "MAE_90D_pct": -6.72, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "C08 can permit Stage2 when tester demand is tied to verified customer adoption/reorder and the entry window is after corporate-action contamination. Exicon's post-CA path had strong MFE with controlled MAE, but source repair is required before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B", "trigger_id": "TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B", "symbol": "064760", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer-quality/adoption/reorder evidence; cap HBM/package/consumable beta when utilization or margin bridge is stale.", "MFE_90D_pct": 21.38, "MAE_90D_pct": -29.47, "score_return_alignment_label": "false_positive_bridge_gap", "current_profile_verdict": "C08 should not treat high-quality semi consumables as Green when near-term customer utilization or margin bridge is absent. TCK had an initial MFE but later opened large MAE and drawdown, requiring local 4B-watch rather than durable Stage2."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION", "trigger_id": "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION", "symbol": "067310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer-quality/adoption/reorder evidence; cap HBM/package/consumable beta when utilization or margin bridge is stale.", "MFE_90D_pct": 7.04, "MAE_90D_pct": -48.41, "score_return_alignment_label": "false_positive_bridge_gap", "current_profile_verdict": "C08 must not allow OSAT/HBM packaging beta to become durable Stage2 without utilization, customer quality, margin, or package mix evidence. Hana Micron generated only small MFE and then severe MAE."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 73, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused/new C08 symbols, +3 test/socket/consumable/customer-quality trigger families, +1 post-CA tester positive, +2 HBM/consumable beta counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 73, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "axis": "test_socket_consumable_customer_quality_vs_hbm_packaging_beta_with_weak_utilization", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C08 should split verified test/socket/customer-quality adoption and reorder bridges from generic HBM packaging or consumable beta. Stage2 requires adoption, utilization, reorder, customer quality or margin conversion evidence. If MAE widens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["092870", "064760", "067310"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 73, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C08 needs customer-quality proof. A tester post-CA rebound can be Stage2 if adoption/reorder is verified; high-quality consumables and OSAT/HBM packaging beta should be capped when utilization or margin bridge is absent and MAE widens."}
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
092870:
  corporate_action_candidate_dates = 2015-10-22, 2024-07-31
  selected window = 2024-09-06~D+180
  contamination = false because entry is after 2024-07-31

064760:
  corporate_action_candidate_dates = none
  selected window = 2024-06-12~D+180
  contamination = false

067310:
  corporate_action_candidate_dates = 2009-11-10, 2021-12-29
  selected window = 2024-04-11~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C08 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C08 rule-shape discovery,
but coding-agent promotion requires non-proxy customer adoption, utilization, reorder and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C08 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
test_socket_consumable_customer_quality_vs_hbm_packaging_beta_with_weak_utilization

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 092870, 064760 and 067310.
4. Keep generic C08 positive weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - customer adoption, reorder or utilization evidence is explicit,
   - test/socket/consumable/package exposure has customer-quality proof,
   - margin conversion is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is HBM/package/consumable beta only,
   - utilization or margin bridge is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if verified customer-quality positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 73
next_round = R3
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

