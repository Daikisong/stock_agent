# E2R Stock-Web v12 Residual Research — R11 Loop 78 / L1 / C04

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 78,
  "computed_next_round": "R12",
  "computed_next_loop": 78,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_project_legal_delay_guardrail",
    "4B_non_price_requirement_stress_test",
    "nuclear_policy_project_order_margin_bridge",
    "nuclear_theme_delay_fade_boundary",
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

Previous completed state in this interactive run: R10 / loop 78.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 78
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy/infra linkage
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
computed_next_round = R12
computed_next_loop = 78
```

R11 was routed to L1 because this is policy-infrastructure/nuclear-project linkage, not a generic R13 red-team checkpoint.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C04 is concentrated in:

```text
034020, 051600, 052690, 000720, 083650
```

This run uses three different symbols:

```text
006910 / 보성파워텍 / nuclear equipment project-order lifecycle
032820 / 우리기술 / nuclear I&C/control-system project lifecycle
046120 / 오르비텍 / nuclear inspection/radiation theme delay fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
032820 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C04 is not “원전 정책이 떴다.”

The mechanism must pass through:

```text
nuclear policy / project event
→ named project, order or inspection work
→ regulatory / legal path and delivery schedule
→ revenue recognition
→ margin conversion
→ durable rerating
```

원전 정책 headline은 착공식의 리본이다.  
C04가 보려는 것은 그 리본 뒤에 실제 발주서, 인허가 경로, 납기표, 매출 인식, 마진이 있는지다.

---

## Case 1 — Policy lifecycle candidate: 006910 / 보성파워텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is nuclear equipment project order, delivery schedule, revenue recognition and margin bridge evidence.

```text
evidence_family = NUCLEAR_POLICY_PROJECT_EQUIPMENT_ORDER_DELIVERY_REVENUE_MARGIN_BRIDGE
case_role = positive_policy_lifecycle_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,070
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv`:

```text
2024-02-01,3070,3150,3045,3120
2024-02-22,3240,3430,3200,3275
2024-04-16,2885,2885,2765,2785
2024-05-20,3930,4320,3900,3995
2024-05-29,4550,4655,4050,4050
2024-08-05,3005,3035,2560,2655
2024-09-13,3510,3885,3470,3730
```

### Backtest

```text
MFE_30D  = +11.73%
MAE_30D  = -0.98%
MFE_90D  = +51.63%
MAE_90D  = -9.93%
MFE_180D = +51.63%
MAE_180D = -16.61%
peak_180 = 4,655 on 2024-05-29
trough_180 = 2,560 on 2024-08-05
peak_to_later_drawdown = -45.01%
```

### Interpretation

This is a C04 policy/project lifecycle candidate.  
The MFE was meaningful, but the post-peak drawdown says order/delivery/margin evidence must refresh.

Correct treatment:

```text
verified nuclear project / equipment order / margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Positive with validation: 032820 / 우리기술

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is nuclear I&C/control-system project order, customer/project visibility, delivery/revenue bridge and margin conversion evidence.

```text
evidence_family = NUCLEAR_CONTROL_I_AND_C_PROJECT_POLICY_ORDER_REVENUE_MARGIN_BRIDGE
case_role = positive_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-02-21
entry_date = 2024-02-22
entry_price = 1,294
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv`:

```text
2024-02-22,1294,1338,1289,1314
2024-03-12,1352,1559,1335,1477
2024-04-05,1528,1612,1490,1563
2024-07-31,2350,2485,2340,2380
2024-08-05,2170,2175,1800,1968
2024-09-19,2550,2650,2505,2620
2024-10-02,2200,2210,2145,2155
```

### Backtest

```text
MFE_30D  = +20.48%
MAE_30D  = -0.39%
MFE_90D  = +24.57%
MAE_90D  = -0.39%
MFE_180D = +104.79%
MAE_180D = -0.39%
peak_180 = 2,650 on 2024-09-19
trough_180 = 1,289 on 2024-02-22
peak_to_later_drawdown = -19.06%
```

### Interpretation

This is a C04 project/I&C positive with validation caveat.  
The price path validates a strong nuclear-control-system MFE candidate, but runtime promotion needs share-count validation and source repair.

Correct treatment:

```text
verified project/order/control-system revenue bridge → Stage2 possible
share-count validation first
bridge stale after peak → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 046120 / 오르비텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests nuclear inspection / radiation policy theme beta without enough named project, inspection backlog, regulatory path and margin bridge.

```text
evidence_family = NUCLEAR_INSPECTION_RADIATION_POLICY_THEME_WITH_WEAK_PROJECT_ORDER_MARGIN_BRIDGE
case_role = counterexample_nuclear_inspection_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,290
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv`:

```text
2024-02-01,3290,3340,3245,3335
2024-02-16,3380,3525,3370,3515
2024-03-14,3405,3555,3375,3495
2024-04-11,3105,3180,2970,3175
2024-08-05,2495,2585,2040,2175
2024-09-09,2115,2200,2090,2200
2024-10-31,2300,2300,2165,2180
```

### Backtest

```text
MFE_30D  = +7.14%
MAE_30D  = -1.37%
MFE_90D  = +8.05%
MAE_90D  = -13.22%
MFE_180D = +8.05%
MAE_180D = -37.99%
peak_180 = 3,555 on 2024-03-14
trough_180 = 2,040 on 2024-08-05
peak_to_later_drawdown = -42.62%
```

### Interpretation

This is a C04 false-positive boundary.  
Nuclear/radiation theme exposure did not validate durable project-order economics.

Correct treatment:

```text
nuclear inspection / radiation theme beta
→ no verified project / order / regulatory / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C04_nuclear_theme_weight = true
do_not_treat_all_nuclear_policy_MFE_as_Green = true
do_not_convert_nuclear_theme_drawdown_to_hard_4C_without_non_price_project_order_legal_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE
```

This fine archetype covers:

```text
1. nuclear equipment/project order bridge → Stage2 possible after source repair
2. nuclear I&C/control-system project bridge → Stage2 possible, share-count validated
3. nuclear inspection/radiation theme without project/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L78-C04-006910-BOSEONG-POWERTEC-NUCLEAR-POLICY-EQUIPMENT-LIFECYCLE", "symbol": "006910", "company_name": "보성파워텍", "round": "R11", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "positive", "best_trigger": "Stage2-PolicyLifecycle-NuclearEquipmentProjectOrderBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should allow nuclear-policy/project equipment rows only when policy headline maps to named project, equipment order, delivery schedule, revenue recognition and margin bridge. Boseong Powertec produced a meaningful MFE, then a post-peak drawdown, so it should be lifecycle-managed rather than permanent Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy nuclear policy/project, named order, delivery or inspection work, regulatory/legal path, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L78-C04-032820-WOORI-TECH-NUCLEAR-IANDC-PROJECT-LIFECYCLE", "symbol": "032820", "company_name": "우리기술", "round": "R11", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-NuclearIandCProjectBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should protect nuclear control/I&C positives when project-policy demand maps to control-system order, customer/project visibility, delivery/revenue bridge and margin conversion. Woori Technology produced a strong MFE with almost no entry-basis MAE, but share-count movement requires validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy nuclear policy/project, named order, delivery or inspection work, regulatory/legal path, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L78-C04-046120-ORBITEC-NUCLEAR-INSPECTION-THEME-DELAY-FADE", "symbol": "046120", "company_name": "오르비텍", "round": "R11", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / NuclearInspectionThemeDelayFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should not treat nuclear-inspection/radiation policy beta as durable Stage2 unless inspection work, named project, regulatory path, order backlog and margin bridge are visible. Orbitec had limited MFE and then a deep drawdown, making it local 4B-watch rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy nuclear policy/project, named order, delivery or inspection work, regulatory/legal path, revenue recognition and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L78-C04-006910-BOSEONG-POWERTEC-NUCLEAR-POLICY-EQUIPMENT-LIFECYCLE", "case_id": "R11L78-C04-006910-BOSEONG-POWERTEC-NUCLEAR-POLICY-EQUIPMENT-LIFECYCLE", "symbol": "006910", "company_name": "보성파워텍", "round": "R11", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_project_legal_delay_guardrail", "trigger_type": "Stage2-PolicyLifecycle-NuclearEquipmentProjectOrderBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3070.0, "evidence_available_at_that_date": "NUCLEAR_POLICY_PROJECT_EQUIPMENT_ORDER_DELIVERY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:BOSEONG_POWERTEC_2024_NUCLEAR_POLICY_PROJECT_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_or_project_candidate", "named_order_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "regulatory_legal_path_or_project_progress_candidate"], "stage4b_evidence_fields": ["nuclear_policy_theme_beta", "project_delay_or_bridge_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv", "profile_path": "atlas/symbol_profiles/006/006910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.73, "MFE_90D_pct": 51.63, "MFE_180D_pct": 51.63, "MAE_30D_pct": -0.98, "MAE_90D_pct": -9.93, "MAE_180D_pct": -16.61, "peak_date": "2024-05-29", "peak_price": 4655.0, "drawdown_after_peak_pct": -45.01, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_peak_if_project_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_legal_delay_regulatory_setback_order_loss_margin_or_financing_break", "trigger_outcome_label": "positive_policy_lifecycle_with_later_4b_watch", "current_profile_verdict": "C04 should allow nuclear-policy/project equipment rows only when policy headline maps to named project, equipment order, delivery schedule, revenue recognition and margin bridge. Boseong Powertec produced a meaningful MFE, then a post-peak drawdown, so it should be lifecycle-managed rather than permanent Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C04_NUCLEAR_PROJECT_006910_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L78-C04-032820-WOORI-TECH-NUCLEAR-IANDC-PROJECT-LIFECYCLE", "case_id": "R11L78-C04-032820-WOORI-TECH-NUCLEAR-IANDC-PROJECT-LIFECYCLE", "symbol": "032820", "company_name": "우리기술", "round": "R11", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_project_legal_delay_guardrail", "trigger_type": "Stage2-Actionable-NuclearIandCProjectBridgeWithSharecountValidation", "trigger_date": "2024-02-21", "entry_date": "2024-02-22", "entry_price": 1294.0, "evidence_available_at_that_date": "NUCLEAR_CONTROL_I_AND_C_PROJECT_POLICY_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WOORI_TECH_2024_NUCLEAR_CONTROL_IANDC_PROJECT_ORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_or_project_candidate", "named_order_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "regulatory_legal_path_or_project_progress_candidate"], "stage4b_evidence_fields": ["nuclear_policy_theme_beta", "project_delay_or_bridge_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv", "profile_path": "atlas/symbol_profiles/032/032820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.48, "MFE_90D_pct": 24.57, "MFE_180D_pct": 104.79, "MAE_30D_pct": -0.39, "MAE_90D_pct": -0.39, "MAE_180D_pct": -0.39, "peak_date": "2024-09-19", "peak_price": 2650.0, "drawdown_after_peak_pct": -19.06, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_peak_if_project_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_legal_delay_regulatory_setback_order_loss_margin_or_financing_break", "trigger_outcome_label": "positive_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C04 should protect nuclear control/I&C positives when project-policy demand maps to control-system order, customer/project visibility, delivery/revenue bridge and margin conversion. Woori Technology produced a strong MFE with almost no entry-basis MAE, but share-count movement requires validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C04_NUCLEAR_PROJECT_032820_2024-02-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L78-C04-046120-ORBITEC-NUCLEAR-INSPECTION-THEME-DELAY-FADE", "case_id": "R11L78-C04-046120-ORBITEC-NUCLEAR-INSPECTION-THEME-DELAY-FADE", "symbol": "046120", "company_name": "오르비텍", "round": "R11", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_project_legal_delay_guardrail", "trigger_type": "Stage2-FalsePositive / NuclearInspectionThemeDelayFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3290.0, "evidence_available_at_that_date": "NUCLEAR_INSPECTION_RADIATION_POLICY_THEME_WITH_WEAK_PROJECT_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ORBITEC_2024_NUCLEAR_INSPECTION_RADIATION_POLICY_PROJECT_ORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_or_project_candidate", "named_order_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "regulatory_legal_path_or_project_progress_candidate"], "stage4b_evidence_fields": ["nuclear_policy_theme_beta", "project_delay_or_bridge_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv", "profile_path": "atlas/symbol_profiles/046/046120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.14, "MFE_90D_pct": 8.05, "MFE_180D_pct": 8.05, "MAE_30D_pct": -1.37, "MAE_90D_pct": -13.22, "MAE_180D_pct": -37.99, "peak_date": "2024-03-14", "peak_price": 3555.0, "drawdown_after_peak_pct": -42.62, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_peak_if_project_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_legal_delay_regulatory_setback_order_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_nuclear_inspection_theme_local4b", "current_profile_verdict": "C04 should not treat nuclear-inspection/radiation policy beta as durable Stage2 unless inspection work, named project, regulatory path, order backlog and margin bridge are visible. Orbitec had limited MFE and then a deep drawdown, making it local 4B-watch rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C04_NUCLEAR_PROJECT_046120_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L78-C04-006910-BOSEONG-POWERTEC-NUCLEAR-POLICY-EQUIPMENT-LIFECYCLE", "trigger_id": "TRG_R11L78-C04-006910-BOSEONG-POWERTEC-NUCLEAR-POLICY-EQUIPMENT-LIFECYCLE", "symbol": "006910", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_project_score": 14, "named_order_score": 13, "delivery_or_inspection_work_score": 12, "regulatory_legal_path_score": 12, "margin_bridge_score": 12, "relative_strength_score": 13, "execution_risk_score": 10, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"policy_project_score": 15, "named_order_score": 15, "delivery_or_inspection_work_score": 14, "regulatory_legal_path_score": 14, "margin_bridge_score": 14, "relative_strength_score": 12, "execution_risk_score": 11, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["policy_project_score", "named_order_score", "delivery_or_inspection_work_score", "regulatory_legal_path_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear policy/project, named order, delivery/inspection work, regulatory path and margin bridge; cap nuclear theme beta when evidence fails to refresh or project/legal delay appears.", "MFE_90D_pct": 51.63, "MAE_90D_pct": -9.93, "score_return_alignment_label": "nuclear_project_positive_with_lifecycle_4b", "current_profile_verdict": "C04 should allow nuclear-policy/project equipment rows only when policy headline maps to named project, equipment order, delivery schedule, revenue recognition and margin bridge. Boseong Powertec produced a meaningful MFE, then a post-peak drawdown, so it should be lifecycle-managed rather than permanent Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L78-C04-032820-WOORI-TECH-NUCLEAR-IANDC-PROJECT-LIFECYCLE", "trigger_id": "TRG_R11L78-C04-032820-WOORI-TECH-NUCLEAR-IANDC-PROJECT-LIFECYCLE", "symbol": "032820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_project_score": 14, "named_order_score": 13, "delivery_or_inspection_work_score": 12, "regulatory_legal_path_score": 12, "margin_bridge_score": 12, "relative_strength_score": 13, "execution_risk_score": 10, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"policy_project_score": 15, "named_order_score": 15, "delivery_or_inspection_work_score": 14, "regulatory_legal_path_score": 14, "margin_bridge_score": 14, "relative_strength_score": 12, "execution_risk_score": 11, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["policy_project_score", "named_order_score", "delivery_or_inspection_work_score", "regulatory_legal_path_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear policy/project, named order, delivery/inspection work, regulatory path and margin bridge; cap nuclear theme beta when evidence fails to refresh or project/legal delay appears.", "MFE_90D_pct": 24.57, "MAE_90D_pct": -0.39, "score_return_alignment_label": "nuclear_project_positive_with_lifecycle_4b", "current_profile_verdict": "C04 should protect nuclear control/I&C positives when project-policy demand maps to control-system order, customer/project visibility, delivery/revenue bridge and margin conversion. Woori Technology produced a strong MFE with almost no entry-basis MAE, but share-count movement requires validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L78-C04-046120-ORBITEC-NUCLEAR-INSPECTION-THEME-DELAY-FADE", "trigger_id": "TRG_R11L78-C04-046120-ORBITEC-NUCLEAR-INSPECTION-THEME-DELAY-FADE", "symbol": "046120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"policy_project_score": 6, "named_order_score": 3, "delivery_or_inspection_work_score": 3, "regulatory_legal_path_score": 3, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 21, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_project_score": 4, "named_order_score": 1, "delivery_or_inspection_work_score": 1, "regulatory_legal_path_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_project_score", "named_order_score", "delivery_or_inspection_work_score", "regulatory_legal_path_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear policy/project, named order, delivery/inspection work, regulatory path and margin bridge; cap nuclear theme beta when evidence fails to refresh or project/legal delay appears.", "MFE_90D_pct": 8.05, "MAE_90D_pct": -13.22, "score_return_alignment_label": "false_positive_nuclear_theme_bridge_gap", "current_profile_verdict": "C04 should not treat nuclear-inspection/radiation policy beta as durable Stage2 unless inspection work, named project, regulatory path, order backlog and margin bridge are visible. Orbitec had limited MFE and then a deep drawdown, making it local 4B-watch rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 78, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_ORDER_I_AND_C_INSPECTION_BRIDGE_VS_NUCLEAR_THEME_DELAY_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C04 nuclear-policy symbols outside top-covered 034020/051600/052690/000720/083650 set, +3 equipment/I&C/inspection trigger families, +2 nuclear project-policy MFE candidates, +1 nuclear inspection theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 78, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "axis": "nuclear_policy_project_order_I_and_C_inspection_bridge_vs_nuclear_theme_delay_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C04 should split verified nuclear policy/project order bridge from generic nuclear theme beta. Stage2 requires policy/project visibility, named order or delivery/inspection work, regulatory/legal path, revenue recognition and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, or project/legal delay evidence appears, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["006910", "032820", "046120"], "share_count_validation_required": ["032820"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 78, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C04 needs nuclear project/order/regulatory/margin proof. Boseong Powertec and Woori Technology show nuclear policy/project MFE candidates after source repair; Orbitec shows nuclear inspection/radiation theme beta fading into local 4B when project/order and margin bridge are absent or stale."}
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
006910:
  name = 보성파워텍
  corporate_action_candidate_dates = 1996-09-30, 1998-04-14, 1999-09-29, 1999-10-18, 2000-05-10, 2005-12-29, 2010-05-19, 2016-08-29
  selected window = 2024-02-01~D+180
  contamination = false

032820:
  name = 우리기술
  corporate_action_candidate_dates = 2003-10-28, 2005-06-07, 2007-07-03, 2007-07-31, 2009-07-29
  selected window = 2024-02-22~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

046120:
  name = 오르비텍 from 2013-04-12, 케이엔디티 before that
  corporate_action_candidate_dates = 2017-06-30
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C04 rows are source_proxy_only / evidence_url_pending.
032820 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C04 rule-shape discovery,
but coding-agent promotion requires non-proxy nuclear policy/project, named order, delivery or inspection work, regulatory/legal path, revenue recognition and margin bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C04 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 032820 needs share-count validation.

Candidate axis:
nuclear_policy_project_order_I_and_C_inspection_bridge_vs_nuclear_theme_delay_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 006910, 032820 and 046120.
4. Validate 032820 share-count changes inside the selected window.
5. Keep generic C04 nuclear-policy weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - nuclear policy/project event is explicit,
   - named project, order or inspection work is visible,
   - regulatory/legal path and delivery schedule are visible,
   - revenue recognition and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is nuclear policy/theme beta only,
   - project/order/legal/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price project cancellation, legal delay, regulatory setback, order loss, financing or margin break.
9. Emit before/after diagnostics and reject if verified nuclear project/order positives are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 78
next_round = R12
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

