# E2R Stock-Web v12 Residual Research — R3 Loop 81 / L3 / C13

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 81,
  "computed_next_round": "R4",
  "computed_next_loop": 81,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "battery_JV_utilization_AMPC_IRA_guardrail",
    "copperfoil_cathode_AMPC_IRA_utilization_margin_bridge",
    "policy_theme_and_nonbattery_event_separation",
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

Previous completed state in this interactive run: R2 / loop 81.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 81
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
computed_next_round = R4
computed_next_loop = 81
```

R3 was routed to C13 because loop 80 R3 used C12 and loop 79 R3 used C14.  
This file tests copper-foil / cathode / AMPC-IRA utilization bridges rather than battery orderbook or EV slowdown 4B/4C.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C13 concentration in:

```text
006400, 373220, 096770
```

This run uses three different symbols:

```text
011790 / SKC / copper-foil AMPC-IRA utilization bridge with non-battery event separation
020150 / 롯데에너지머티리얼즈 / copper-foil utilization recovery bridge
051910 / LG화학 / cathode AMPC-IRA policy theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
011790 requires event-separation validation before any runtime promotion.
```

## Research thesis

C13 is not “IRA/AMPC 정책이 좋다.”

The mechanism must pass through:

```text
IRA / AMPC / battery JV headline
→ customer or JV volume
→ US capacity and utilization
→ subsidy economics and revenue recognition
→ margin bridge
→ durable rerating
```

AMPC는 보조금이라는 바람이다.  
C13이 보려는 것은 바람 그 자체가 아니라 그 바람이 실제 가동률, 출하, 매출, 마진의 풍차를 돌리는지다.

---

## Case 1 — Copper-foil / AMPC candidate with event separation: 011790 / SKC

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
event_separation_required = true
source_repair_required = true
```

The source-repair task is copper-foil customer/JV volume, US capacity, AMPC/IRA economics, utilization, revenue and margin bridge evidence.  
Non-battery event/theme components must be separated before runtime promotion.

```text
evidence_family = BATTERY_COPPERFOIL_AMPC_IRA_US_CAPA_UTILIZATION_MARGIN_BRIDGE_WITH_NONBATTERY_EVENT_SEPARATION
case_role = positive_copperfoil_AMPC_IRA_candidate_with_event_separation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 76,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv`:

```text
2024-02-01,76100,77200,74400,76900
2024-02-20,86000,92700,84000,92600
2024-03-18,116200,121800,116200,121800
2024-04-08,144700,147500,132800,145300
2024-06-13,169500,184000,167000,183700
2024-06-18,189100,200000,172900,182000
2024-08-05,123100,125000,107600,114100
2024-09-09,105000,111800,104300,111000
```

### Backtest

```text
MFE_30D  = +60.05%
MAE_30D  = -2.23%
MFE_90D  = +141.79%
MAE_90D  = -2.23%
MFE_180D = +162.81%
MAE_180D = -2.23%
peak_180 = 200,000 on 2024-06-18
trough_180 = 74,400 on 2024-02-01
peak_to_later_drawdown = -47.85%
```

### Interpretation

This is a powerful MFE candidate, but C13 must not blindly attribute the whole move to battery AMPC/IRA economics.  
The coding-agent promotion task is to separate battery copper-foil utilization proof from non-battery event/theme contamination.

Correct treatment:

```text
verified customer/JV volume + AMPC/IRA utilization + margin bridge → Stage2-Yellow possible
non-battery event separation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Copper-foil utilization recovery candidate: 020150 / 롯데에너지머티리얼즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is copper-foil customer volume, utilization, IRA/AMPC economics, revenue conversion and margin bridge evidence.

```text
evidence_family = BATTERY_COPPERFOIL_CUSTOMER_VOLUME_UTILIZATION_AMPC_IRA_MARGIN_RECOVERY_BRIDGE
case_role = positive_copperfoil_utilization_recovery_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 31,250
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv`:

```text
2024-02-01,31250,32850,31000,32700
2024-02-22,38000,39700,37500,37500
2024-03-21,43000,49200,42850,47050
2024-03-25,48900,51500,48450,50700
2024-07-24,38500,39650,38150,38350
2024-08-05,36100,36750,30500,32200
2024-09-05,40050,45650,40050,43000
2024-10-25,36700,37800,36300,37150
```

### Backtest

```text
MFE_30D  = +27.04%
MAE_30D  = -0.80%
MFE_90D  = +64.80%
MAE_90D  = -0.80%
MFE_180D = +64.80%
MAE_180D = -2.40%
peak_180 = 51,500 on 2024-03-25
trough_180 = 30,500 on 2024-08-05
peak_to_later_drawdown = -40.78%
```

### Interpretation

This is a C13 copper-foil utilization recovery candidate.  
The entry-basis MAE was shallow, but the post-peak drawdown means the utilization and margin bridge must refresh.

Correct treatment:

```text
verified customer volume / utilization / AMPC economics / margin bridge → Stage2-Yellow possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 051910 / LG화학

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests cathode / IRA / AMPC policy beta without enough utilization, customer volume, revenue and margin bridge.

```text
evidence_family = BATTERY_CATHODE_AMPC_IRA_US_JV_POLICY_THEME_WITH_WEAK_UTILIZATION_REVENUE_MARGIN_BRIDGE
case_role = counterexample_cathode_AMPC_IRA_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 426,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv`:

```text
2024-02-01,426500,433000,417000,430000
2024-02-16,489000,515000,488000,504000
2024-02-19,508000,520000,504000,508000
2024-04-08,395500,399000,384000,394000
2024-08-05,302500,304500,263500,272500
2024-09-27,360000,368500,353500,357500
2024-10-22,328000,329000,317000,318000
2024-10-31,317000,320000,313500,313500
```

### Backtest

```text
MFE_30D  = +21.92%
MAE_30D  = -2.23%
MFE_90D  = +21.92%
MAE_90D  = -9.96%
MFE_180D = +21.92%
MAE_180D = -38.22%
peak_180 = 520,000 on 2024-02-19
trough_180 = 263,500 on 2024-08-05
peak_to_later_drawdown = -49.33%
```

### Interpretation

This is a C13 false-positive / local-4B boundary.  
The early policy MFE did not validate durable cathode/JV utilization rerating.

Correct treatment:

```text
cathode / IRA / AMPC policy beta
→ no verified utilization / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
JV_utilization_AMPC_IRA_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
event_separation_guard = strengthen
full_4b_or_4c_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C13_battery_policy_weight = true
do_not_treat_all_AMPC_IRA_MFE_as_Green = true
do_not_ingest_event_contaminated_battery_rows_without_separation = true
do_not_convert_battery_policy_drawdown_to_hard_4C_without_non_price_JV_customer_volume_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE
```

This fine archetype covers:

```text
1. copper-foil AMPC/IRA + utilization bridge → Stage2-Yellow possible after source repair
2. copper-foil recovery with bounded entry MAE → lifecycle Stage2 candidate after source repair
3. cathode/IRA policy beta without utilization and margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L81-C13-011790-SKC-COPPERFOIL-AMPC-IRA-EVENT-SEPARATION", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE", "case_type": "battery_JV_utilization_AMPC_IRA", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-CopperfoilAMPCIRAUtilizationBridgeWithNonBatteryEventSeparation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C13 should not blindly credit a whole SKC rally to battery JV/AMPC economics. A valid positive needs copper-foil customer/JV visibility, US capacity, utilization, IRA/AMPC economics, revenue and margin bridge; non-battery event/theme components must be separated.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy JV/customer volume, AMPC/IRA economics, utilization, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L81-C13-020150-LOTTE-ENERGY-MATERIALS-COPPERFOIL-UTILIZATION-RECOVERY", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE", "case_type": "battery_JV_utilization_AMPC_IRA", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-CopperfoilUtilizationAMPCIRAMarginBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C13 can preserve copper-foil recovery positives when customer volume, utilization, IRA/AMPC economics and margin bridge are visible. Lotte Energy Materials had tradable MFE with bounded entry-basis MAE, but post-peak drawdown means bridge refresh is required.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy JV/customer volume, AMPC/IRA economics, utilization, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L81-C13-051910-LG-CHEM-CATHODE-AMPC-IRA-THEME-FADE", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE", "case_type": "battery_JV_utilization_AMPC_IRA", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CathodeAMPCIRAThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C13 should not treat cathode/IRA/AMPC policy beta as durable Stage2 unless JV utilization, customer volume, subsidy economics, revenue conversion and margin bridge are visible. LG Chem had an early MFE but then a severe high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy JV/customer volume, AMPC/IRA economics, utilization, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L81-C13-011790-SKC-COPPERFOIL-AMPC-IRA-EVENT-SEPARATION", "case_id": "R3L81-C13-011790-SKC-COPPERFOIL-AMPC-IRA-EVENT-SEPARATION", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_JV_utilization_AMPC_IRA_guardrail", "trigger_type": "Stage2-Lifecycle-CopperfoilAMPCIRAUtilizationBridgeWithNonBatteryEventSeparation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 76100.0, "evidence_available_at_that_date": "BATTERY_COPPERFOIL_AMPC_IRA_US_CAPA_UTILIZATION_MARGIN_BRIDGE_WITH_NONBATTERY_EVENT_SEPARATION", "evidence_source": "source_proxy_manual_verification_required:SKC_2024_COPPERFOIL_AMPC_IRA_US_CAPA_UTILIZATION_MARGIN_AND_NONBATTERY_EVENT_SEPARATION", "stage2_evidence_fields": ["JV_or_AMPC_IRA_candidate", "customer_volume_or_utilization_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "US_CAPA_or_subsidy_economics_candidate"], "stage4b_evidence_fields": ["battery_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv", "profile_path": "atlas/symbol_profiles/011/011790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 60.05, "MFE_90D_pct": 141.79, "MFE_180D_pct": 162.81, "MAE_30D_pct": -2.23, "MAE_90D_pct": -2.23, "MAE_180D_pct": -2.23, "peak_date": "2024-06-18", "peak_price": 200000.0, "drawdown_after_peak_pct": -47.85, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_JV_AMPC_IRA_peak_if_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_JV_delay_customer_volume_loss_subsidy_rule_change_margin_or_financing_break", "trigger_outcome_label": "positive_copperfoil_AMPC_IRA_candidate_with_event_separation_and_later_4b_watch", "current_profile_verdict": "C13 should not blindly credit a whole SKC rally to battery JV/AMPC economics. A valid positive needs copper-foil customer/JV visibility, US capacity, utilization, IRA/AMPC economics, revenue and margin bridge; non-battery event/theme components must be separated.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_event_separation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C13_BATTERY_AMPC_IRA_011790_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L81-C13-020150-LOTTE-ENERGY-MATERIALS-COPPERFOIL-UTILIZATION-RECOVERY", "case_id": "R3L81-C13-020150-LOTTE-ENERGY-MATERIALS-COPPERFOIL-UTILIZATION-RECOVERY", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_JV_utilization_AMPC_IRA_guardrail", "trigger_type": "Stage2-Lifecycle-CopperfoilUtilizationAMPCIRAMarginBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 31250.0, "evidence_available_at_that_date": "BATTERY_COPPERFOIL_CUSTOMER_VOLUME_UTILIZATION_AMPC_IRA_MARGIN_RECOVERY_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_ENERGY_MATERIALS_2024_COPPERFOIL_CUSTOMER_VOLUME_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE", "stage2_evidence_fields": ["JV_or_AMPC_IRA_candidate", "customer_volume_or_utilization_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "US_CAPA_or_subsidy_economics_candidate"], "stage4b_evidence_fields": ["battery_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.04, "MFE_90D_pct": 64.8, "MFE_180D_pct": 64.8, "MAE_30D_pct": -0.8, "MAE_90D_pct": -0.8, "MAE_180D_pct": -2.4, "peak_date": "2024-03-25", "peak_price": 51500.0, "drawdown_after_peak_pct": -40.78, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_JV_AMPC_IRA_peak_if_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_JV_delay_customer_volume_loss_subsidy_rule_change_margin_or_financing_break", "trigger_outcome_label": "positive_copperfoil_utilization_recovery_with_later_4b_watch", "current_profile_verdict": "C13 can preserve copper-foil recovery positives when customer volume, utilization, IRA/AMPC economics and margin bridge are visible. Lotte Energy Materials had tradable MFE with bounded entry-basis MAE, but post-peak drawdown means bridge refresh is required.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_event_separation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C13_BATTERY_AMPC_IRA_020150_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L81-C13-051910-LG-CHEM-CATHODE-AMPC-IRA-THEME-FADE", "case_id": "R3L81-C13-051910-LG-CHEM-CATHODE-AMPC-IRA-THEME-FADE", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_JV_utilization_AMPC_IRA_guardrail", "trigger_type": "Stage2-FalsePositive / CathodeAMPCIRAThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 426500.0, "evidence_available_at_that_date": "BATTERY_CATHODE_AMPC_IRA_US_JV_POLICY_THEME_WITH_WEAK_UTILIZATION_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LG_CHEM_2024_CATHODE_US_JV_AMPC_IRA_UTILIZATION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["JV_or_AMPC_IRA_candidate", "customer_volume_or_utilization_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "US_CAPA_or_subsidy_economics_candidate"], "stage4b_evidence_fields": ["battery_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv", "profile_path": "atlas/symbol_profiles/051/051910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.92, "MFE_90D_pct": 21.92, "MFE_180D_pct": 21.92, "MAE_30D_pct": -2.23, "MAE_90D_pct": -9.96, "MAE_180D_pct": -38.22, "peak_date": "2024-02-19", "peak_price": 520000.0, "drawdown_after_peak_pct": -49.33, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_JV_AMPC_IRA_peak_if_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_JV_delay_customer_volume_loss_subsidy_rule_change_margin_or_financing_break", "trigger_outcome_label": "counterexample_cathode_AMPC_IRA_theme_local4b", "current_profile_verdict": "C13 should not treat cathode/IRA/AMPC policy beta as durable Stage2 unless JV utilization, customer volume, subsidy economics, revenue conversion and margin bridge are visible. LG Chem had an early MFE but then a severe high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_event_separation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C13_BATTERY_AMPC_IRA_051910_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L81-C13-011790-SKC-COPPERFOIL-AMPC-IRA-EVENT-SEPARATION", "trigger_id": "TRG_R3L81-C13-011790-SKC-COPPERFOIL-AMPC-IRA-EVENT-SEPARATION", "symbol": "011790", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"JV_or_AMPC_score": 14, "IRA_policy_score": 13, "customer_volume_score": 13, "utilization_score": 12, "revenue_margin_bridge_score": 13, "relative_strength_score": 12, "event_separation_risk": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"JV_or_AMPC_score": 16, "IRA_policy_score": 15, "customer_volume_score": 15, "utilization_score": 14, "revenue_margin_bridge_score": 15, "relative_strength_score": 11, "event_separation_risk": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["JV_or_AMPC_score", "IRA_policy_score", "customer_volume_score", "utilization_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified JV/customer volume, AMPC/IRA subsidy economics, utilization, revenue and margin bridge; cap battery policy beta or non-battery event contamination when bridge fails to refresh.", "MFE_90D_pct": 141.79, "MAE_90D_pct": -2.23, "score_return_alignment_label": "battery_AMPC_IRA_positive_with_lifecycle_4b", "current_profile_verdict": "C13 should not blindly credit a whole SKC rally to battery JV/AMPC economics. A valid positive needs copper-foil customer/JV visibility, US capacity, utilization, IRA/AMPC economics, revenue and margin bridge; non-battery event/theme components must be separated."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L81-C13-020150-LOTTE-ENERGY-MATERIALS-COPPERFOIL-UTILIZATION-RECOVERY", "trigger_id": "TRG_R3L81-C13-020150-LOTTE-ENERGY-MATERIALS-COPPERFOIL-UTILIZATION-RECOVERY", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"JV_or_AMPC_score": 14, "IRA_policy_score": 13, "customer_volume_score": 13, "utilization_score": 12, "revenue_margin_bridge_score": 13, "relative_strength_score": 12, "event_separation_risk": 0, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"JV_or_AMPC_score": 16, "IRA_policy_score": 15, "customer_volume_score": 15, "utilization_score": 14, "revenue_margin_bridge_score": 15, "relative_strength_score": 11, "event_separation_risk": 0, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["JV_or_AMPC_score", "IRA_policy_score", "customer_volume_score", "utilization_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified JV/customer volume, AMPC/IRA subsidy economics, utilization, revenue and margin bridge; cap battery policy beta or non-battery event contamination when bridge fails to refresh.", "MFE_90D_pct": 64.8, "MAE_90D_pct": -0.8, "score_return_alignment_label": "battery_AMPC_IRA_positive_with_lifecycle_4b", "current_profile_verdict": "C13 can preserve copper-foil recovery positives when customer volume, utilization, IRA/AMPC economics and margin bridge are visible. Lotte Energy Materials had tradable MFE with bounded entry-basis MAE, but post-peak drawdown means bridge refresh is required."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L81-C13-051910-LG-CHEM-CATHODE-AMPC-IRA-THEME-FADE", "trigger_id": "TRG_R3L81-C13-051910-LG-CHEM-CATHODE-AMPC-IRA-THEME-FADE", "symbol": "051910", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"JV_or_AMPC_score": 5, "IRA_policy_score": 5, "customer_volume_score": 3, "utilization_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 5, "event_separation_risk": 0, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 43, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"JV_or_AMPC_score": 3, "IRA_policy_score": 3, "customer_volume_score": 1, "utilization_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "event_separation_risk": 0, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["JV_or_AMPC_score", "IRA_policy_score", "customer_volume_score", "utilization_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified JV/customer volume, AMPC/IRA subsidy economics, utilization, revenue and margin bridge; cap battery policy beta or non-battery event contamination when bridge fails to refresh.", "MFE_90D_pct": 21.92, "MAE_90D_pct": -9.96, "score_return_alignment_label": "false_positive_battery_policy_bridge_gap", "current_profile_verdict": "C13 should not treat cathode/IRA/AMPC policy beta as durable Stage2 unless JV utilization, customer volume, subsidy economics, revenue conversion and margin bridge are visible. LG Chem had an early MFE but then a severe high-MAE drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 81, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "COPPERFOIL_CATHODE_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_POLICY_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "event_separation_required_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C13 battery/copperfoil/cathode symbols outside top-covered 006400/373220/096770 set, +3 SKC/Lotte/LG Chem trigger families, +2 AMPC/IRA utilization positives, +1 cathode policy-theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_event_separation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 81, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "axis": "copperfoil_cathode_AMPC_IRA_utilization_margin_bridge_vs_battery_policy_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C13 should split verified battery JV/AMPC/IRA utilization and margin rerating from generic battery policy beta or non-battery event contamination. Stage2 requires customer/JV volume, US capacity, utilization, subsidy economics, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["011790", "020150", "051910"], "event_separation_required": ["011790"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 81, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "existing_axis_strengthened": ["stage2_required_bridge", "JV_utilization_AMPC_IRA_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "event_separation_guard", "full_4b_or_4c_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C13 needs JV/customer volume, US capacity, AMPC/IRA economics, utilization and margin proof. SKC and Lotte Energy Materials show copper-foil/AMPC recovery candidates after source repair, with SKC needing non-battery event separation; LG Chem shows cathode/IRA policy beta fading into local 4B when utilization and margin bridge are weak."}
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
011790:
  name = SKC from 1997-08-04
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
  event_separation_required = true

020150:
  name = 롯데에너지머티리얼즈 from 2023-03-30, 일진머티리얼즈 before that
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

051910:
  name = LG화학
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C13 rows are source_proxy_only / evidence_url_pending.
011790 also requires non-battery event separation before runtime promotion.
This MD is useful for stock-web path calibration and C13 rule-shape discovery,
but coding-agent promotion requires non-proxy JV/customer volume, AMPC/IRA economics, utilization, revenue conversion and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C13 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 011790 needs event separation.

Candidate axis:
copperfoil_cathode_AMPC_IRA_utilization_margin_bridge_vs_battery_policy_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 011790, 020150 and 051910.
4. Validate 011790 event separation so non-battery theme/event MFE is not counted as C13 battery AMPC/IRA evidence.
5. Keep generic C13 AMPC/IRA policy weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - IRA/AMPC/JV premise is explicit,
   - customer or JV volume is visible,
   - US capacity and utilization are visible,
   - subsidy economics and revenue recognition are credible,
   - margin bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is battery policy/AMPC theme beta only,
   - JV/customer volume/utilization/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price JV delay, customer volume loss, subsidy-rule change, financing or margin break.
9. Emit before/after diagnostics and reject if verified copper-foil/AMPC positives are overblocked.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 81
next_round = R4
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

