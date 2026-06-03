# E2R Stock-Web v12 Residual Research — R4 Loop 81 / L4 / C16

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 81,
  "computed_next_round": "R5",
  "computed_next_loop": 81,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "strategic_resource_policy_supply_guardrail",
    "lithium_cobalt_aluminum_foil_supply_volume_margin_bridge",
    "resource_policy_theme_fade_boundary",
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

Previous completed state in this interactive run: R3 / loop 81.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 81
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
computed_next_round = R5
computed_next_loop = 81
```

R4 was routed to C16 because loop 80 R4 used C15 and loop 79 R4 used C17.  
This file tests lithium/cobalt/aluminum-foil strategic resource supply bridges rather than material spread or chemical commodity margin spread.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C16 concentration in:

```text
005290, 027580, 047400, 093370
```

This run uses three different symbols:

```text
005420 / 코스모화학 / cobalt-lithium-nickel recycling supply lifecycle
001570 / 금양 / lithium resource policy theme fade
006110 / 삼아알미늄 / aluminum battery-foil strategic supply theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected 180D window.
001570 has a profile status caveat for longer-horizon ingestion because tradable last_date and raw_last_date differ.
```

## Research thesis

C16 is not “전략자원 테마가 올랐다.”

The mechanism must pass through:

```text
strategic resource / policy / supply-chain headline
→ material availability or mine/recycling supply
→ customer/offtake or volume visibility
→ financing, permitting or utilization
→ revenue conversion and margin bridge
→ durable rerating
```

전략자원 정책은 지도 위의 광산 표시다.  
C16이 보려는 것은 그 표시가 실제 채굴, 재활용, 고객계약, 자금조달, 출하, 마진으로 땅을 파고 들어가는지다.

---

## Case 1 — Resource recovery lifecycle candidate: 005420 / 코스모화학

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is cobalt/lithium/nickel recycling or material-supply economics, customer volume, utilization, revenue conversion and margin bridge evidence.

```text
evidence_family = COBALT_LITHIUM_NICKEL_RECYCLING_STRATEGIC_RESOURCE_SUPPLY_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE
case_role = positive_resource_recovery_candidate_with_later_high_MAE_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 28,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005420/2024.csv`:

```text
2024-02-01,28400,29250,27900,29050
2024-02-21,34000,39250,33550,37900
2024-03-26,38400,41900,38300,39050
2024-05-24,28150,28550,27700,27700
2024-07-16,25150,25150,23600,24150
2024-08-05,20250,20300,16500,17220
2024-09-27,24300,25600,23550,25100
2024-10-25,22550,22850,21200,21250
```

### Backtest

```text
MFE_30D  = +38.20%
MAE_30D  = -1.76%
MFE_90D  = +47.54%
MAE_90D  = -2.46%
MFE_180D = +47.54%
MAE_180D = -41.90%
peak_180 = 41,900 on 2024-03-26
trough_180 = 16,500 on 2024-08-05
peak_to_later_drawdown = -60.62%
```

### Interpretation

This is a C16 lifecycle candidate, not durable Green.  
The early MFE was tradable, but the later high-MAE drawdown says resource supply and margin evidence must refresh.

Correct treatment:

```text
verified cobalt/lithium/nickel supply or recycling volume / utilization / margin bridge → Stage2-Yellow possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 001570 / 금양

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
longer_horizon_status_validation_recommended = true
source_repair_required = true
```

This row tests lithium/resource policy beta without enough mine supply, customer offtake, financing and revenue bridge.

```text
evidence_family = LITHIUM_RESOURCE_BATTERY_POLICY_THEME_WITH_WEAK_MINE_SUPPLY_CUSTOMER_REVENUE_MARGIN_BRIDGE
case_role = counterexample_lithium_resource_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 77,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv`:

```text
2024-02-01,77200,80000,75100,78900
2024-02-15,85200,99000,85100,94800
2024-03-05,110100,129500,110000,125300
2024-03-06,130500,134100,116000,118800
2024-08-05,64800,65000,51000,56100
2024-09-09,40200,44200,40150,43300
2024-10-25,43000,44750,42400,43250
2024-10-30,35300,41050,35100,38250
```

### Backtest

```text
MFE_30D  = +26.94%
MAE_30D  = -2.72%
MFE_90D  = +73.70%
MAE_90D  = -2.72%
MFE_180D = +73.70%
MAE_180D = -54.53%
peak_180 = 134,100 on 2024-03-06
trough_180 = 35,100 on 2024-10-30
peak_to_later_drawdown = -73.83%
```

### Interpretation

This is a C16 lithium-resource theme-fade row.  
The early resource MFE did not become durable mine/offtake/revenue economics.

Correct treatment:

```text
lithium/resource policy beta
→ no verified mine supply / offtake / financing / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 006110 / 삼아알미늄

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests aluminum battery-foil strategic supply beta without enough customer volume and margin bridge.

```text
evidence_family = ALUMINUM_BATTERY_FOIL_STRATEGIC_SUPPLY_THEME_WITH_WEAK_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE
case_role = counterexample_aluminum_foil_strategic_supply_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 86,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv`:

```text
2024-02-01,86500,88000,84800,86500
2024-02-16,95000,102400,93700,99500
2024-02-21,110600,116400,110000,110700
2024-04-08,76400,79900,73800,78900
2024-08-05,48100,49000,39600,42000
2024-09-27,53900,55000,51800,54000
2024-10-10,60000,61200,57700,58700
2024-10-25,49700,51000,48850,49150
```

### Backtest

```text
MFE_30D  = +34.57%
MAE_30D  = -7.28%
MFE_90D  = +34.57%
MAE_90D  = -14.68%
MFE_180D = +34.57%
MAE_180D = -54.22%
peak_180 = 116,400 on 2024-02-21
trough_180 = 39,600 on 2024-08-05
peak_to_later_drawdown = -65.98%
```

### Interpretation

This is the aluminum-foil strategic supply theme-fade row.  
The early MFE was tradable, but it did not validate durable customer-volume and margin rerating.

Correct treatment:

```text
aluminum / battery-foil supply theme beta
→ no verified customer volume / utilization / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
strategic_resource_supply_bridge_required = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C16_resource_policy_weight = true
do_not_treat_all_lithium_cobalt_aluminum_MFE_as_Green = true
do_not_convert_resource_policy_drawdown_to_hard_4C_without_non_price_supply_offtake_financing_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE
```

This fine archetype covers:

```text
1. cobalt/lithium/nickel recycling or supply recovery → Stage2-Yellow possible after source repair
2. lithium resource policy beta without mine/offtake economics → false Stage2 / local 4B
3. aluminum battery-foil supply beta without customer-volume/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L81-C16-005420-COSMO-CHEMICAL-COBALT-LITHIUM-RECOVERY-LIFECYCLE", "symbol": "005420", "company_name": "코스모화학", "round": "R4", "loop": "81", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-CobaltLithiumRecyclingStrategicSupplyBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 should allow strategic-resource recovery positives only when cobalt/lithium/nickel or recycling supply maps to customer volume, utilization, policy support, revenue and margin bridge. Cosmo Chemical produced a large early MFE, but the later high-MAE path requires lifecycle 4B if the bridge fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy strategic resource policy, mine/supply availability, customer/offtake, financing/permitting, utilization, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L81-C16-001570-KUMYANG-LITHIUM-RESOURCE-POLICY-THEME-FADE", "symbol": "001570", "company_name": "금양", "round": "R4", "loop": "81", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LithiumResourcePolicyThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 should not treat lithium/resource policy beta as durable Stage2 unless mine/supply availability, customer offtake, financing, permitting, revenue conversion and margin bridge are visible. Kumyang had a strong early spike, then a severe high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy strategic resource policy, mine/supply availability, customer/offtake, financing/permitting, utilization, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L81-C16-006110-SAMA-ALUMINUM-FOIL-STRATEGIC-SUPPLY-FADE", "symbol": "006110", "company_name": "삼아알미늄", "round": "R4", "loop": "81", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AluminumFoilStrategicSupplyThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 should not treat aluminum/battery-foil supply theme beta as durable Stage2 unless customer volume, utilization, orderbook, pricing and margin bridge are visible. Sam-A Aluminum had an early MFE, then a severe drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy strategic resource policy, mine/supply availability, customer/offtake, financing/permitting, utilization, revenue and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L81-C16-005420-COSMO-CHEMICAL-COBALT-LITHIUM-RECOVERY-LIFECYCLE", "case_id": "R4L81-C16-005420-COSMO-CHEMICAL-COBALT-LITHIUM-RECOVERY-LIFECYCLE", "symbol": "005420", "company_name": "코스모화학", "round": "R4", "loop": "81", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-Lifecycle-CobaltLithiumRecyclingStrategicSupplyBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 28400.0, "evidence_available_at_that_date": "COBALT_LITHIUM_NICKEL_RECYCLING_STRATEGIC_RESOURCE_SUPPLY_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:COSMO_CHEMICAL_2024_COBALT_LITHIUM_NICKEL_RECYCLING_STRATEGIC_RESOURCE_SUPPLY_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["strategic_resource_policy_candidate", "supply_or_offtake_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_volume_financing_or_utilization_candidate"], "stage4b_evidence_fields": ["resource_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005420/2024.csv", "profile_path": "atlas/symbol_profiles/005/005420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 38.2, "MFE_90D_pct": 47.54, "MFE_180D_pct": 47.54, "MAE_30D_pct": -1.76, "MAE_90D_pct": -2.46, "MAE_180D_pct": -41.9, "peak_date": "2024-03-26", "peak_price": 41900.0, "drawdown_after_peak_pct": -60.62, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_strategic_resource_peak_if_supply_offtake_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_permitting_failure_customer_loss_financing_or_margin_break", "trigger_outcome_label": "positive_resource_recovery_candidate_with_later_high_MAE_4b_watch", "current_profile_verdict": "C16 should allow strategic-resource recovery positives only when cobalt/lithium/nickel or recycling supply maps to customer volume, utilization, policy support, revenue and margin bridge. Cosmo Chemical produced a large early MFE, but the later high-MAE path requires lifecycle 4B if the bridge fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C16_STRATEGIC_RESOURCE_005420_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L81-C16-001570-KUMYANG-LITHIUM-RESOURCE-POLICY-THEME-FADE", "case_id": "R4L81-C16-001570-KUMYANG-LITHIUM-RESOURCE-POLICY-THEME-FADE", "symbol": "001570", "company_name": "금양", "round": "R4", "loop": "81", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-FalsePositive / LithiumResourcePolicyThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 77200.0, "evidence_available_at_that_date": "LITHIUM_RESOURCE_BATTERY_POLICY_THEME_WITH_WEAK_MINE_SUPPLY_CUSTOMER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KUMYANG_2024_LITHIUM_RESOURCE_POLICY_MINE_SUPPLY_OFFTAKE_FINANCING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["strategic_resource_policy_candidate", "supply_or_offtake_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_volume_financing_or_utilization_candidate"], "stage4b_evidence_fields": ["resource_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv", "profile_path": "atlas/symbol_profiles/001/001570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.94, "MFE_90D_pct": 73.7, "MFE_180D_pct": 73.7, "MAE_30D_pct": -2.72, "MAE_90D_pct": -2.72, "MAE_180D_pct": -54.53, "peak_date": "2024-03-06", "peak_price": 134100.0, "drawdown_after_peak_pct": -73.83, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_strategic_resource_peak_if_supply_offtake_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_permitting_failure_customer_loss_financing_or_margin_break", "trigger_outcome_label": "counterexample_lithium_resource_theme_local4b", "current_profile_verdict": "C16 should not treat lithium/resource policy beta as durable Stage2 unless mine/supply availability, customer offtake, financing, permitting, revenue conversion and margin bridge are visible. Kumyang had a strong early spike, then a severe high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C16_STRATEGIC_RESOURCE_001570_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L81-C16-006110-SAMA-ALUMINUM-FOIL-STRATEGIC-SUPPLY-FADE", "case_id": "R4L81-C16-006110-SAMA-ALUMINUM-FOIL-STRATEGIC-SUPPLY-FADE", "symbol": "006110", "company_name": "삼아알미늄", "round": "R4", "loop": "81", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-FalsePositive / AluminumFoilStrategicSupplyThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 86500.0, "evidence_available_at_that_date": "ALUMINUM_BATTERY_FOIL_STRATEGIC_SUPPLY_THEME_WITH_WEAK_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SAMA_ALUMINUM_2024_ALUMINUM_BATTERY_FOIL_STRATEGIC_SUPPLY_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["strategic_resource_policy_candidate", "supply_or_offtake_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_volume_financing_or_utilization_candidate"], "stage4b_evidence_fields": ["resource_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv", "profile_path": "atlas/symbol_profiles/006/006110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.57, "MFE_90D_pct": 34.57, "MFE_180D_pct": 34.57, "MAE_30D_pct": -7.28, "MAE_90D_pct": -14.68, "MAE_180D_pct": -54.22, "peak_date": "2024-02-21", "peak_price": 116400.0, "drawdown_after_peak_pct": -65.98, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_strategic_resource_peak_if_supply_offtake_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_permitting_failure_customer_loss_financing_or_margin_break", "trigger_outcome_label": "counterexample_aluminum_foil_strategic_supply_local4b", "current_profile_verdict": "C16 should not treat aluminum/battery-foil supply theme beta as durable Stage2 unless customer volume, utilization, orderbook, pricing and margin bridge are visible. Sam-A Aluminum had an early MFE, then a severe drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C16_STRATEGIC_RESOURCE_006110_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L81-C16-005420-COSMO-CHEMICAL-COBALT-LITHIUM-RECOVERY-LIFECYCLE", "trigger_id": "TRG_R4L81-C16-005420-COSMO-CHEMICAL-COBALT-LITHIUM-RECOVERY-LIFECYCLE", "symbol": "005420", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_supply_score": 14, "resource_availability_score": 13, "offtake_customer_score": 12, "financing_permitting_score": 10, "utilization_revenue_score": 12, "margin_bridge_score": 12, "relative_strength_score": 10, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 74, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"policy_supply_score": 16, "resource_availability_score": 15, "offtake_customer_score": 14, "financing_permitting_score": 12, "utilization_revenue_score": 14, "margin_bridge_score": 14, "relative_strength_score": 9, "execution_risk_score": 13, "source_confidence_score": 2}, "weighted_score_after": 80, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["policy_supply_score", "resource_availability_score", "offtake_customer_score", "financing_permitting_score", "utilization_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified strategic-resource supply, customer/offtake, financing/permitting, utilization, revenue and margin bridge; cap resource policy theme beta when bridge fails to refresh.", "MFE_90D_pct": 47.54, "MAE_90D_pct": -2.46, "score_return_alignment_label": "strategic_resource_supply_positive_with_lifecycle_4b", "current_profile_verdict": "C16 should allow strategic-resource recovery positives only when cobalt/lithium/nickel or recycling supply maps to customer volume, utilization, policy support, revenue and margin bridge. Cosmo Chemical produced a large early MFE, but the later high-MAE path requires lifecycle 4B if the bridge fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L81-C16-001570-KUMYANG-LITHIUM-RESOURCE-POLICY-THEME-FADE", "trigger_id": "TRG_R4L81-C16-001570-KUMYANG-LITHIUM-RESOURCE-POLICY-THEME-FADE", "symbol": "001570", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_supply_score": 5, "resource_availability_score": 3, "offtake_customer_score": 2, "financing_permitting_score": 2, "utilization_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 10, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_supply_score": 3, "resource_availability_score": 1, "offtake_customer_score": 1, "financing_permitting_score": 1, "utilization_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_supply_score", "resource_availability_score", "offtake_customer_score", "financing_permitting_score", "utilization_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified strategic-resource supply, customer/offtake, financing/permitting, utilization, revenue and margin bridge; cap resource policy theme beta when bridge fails to refresh.", "MFE_90D_pct": 73.7, "MAE_90D_pct": -2.72, "score_return_alignment_label": "false_positive_resource_policy_bridge_gap", "current_profile_verdict": "C16 should not treat lithium/resource policy beta as durable Stage2 unless mine/supply availability, customer offtake, financing, permitting, revenue conversion and margin bridge are visible. Kumyang had a strong early spike, then a severe high-MAE fade."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L81-C16-006110-SAMA-ALUMINUM-FOIL-STRATEGIC-SUPPLY-FADE", "trigger_id": "TRG_R4L81-C16-006110-SAMA-ALUMINUM-FOIL-STRATEGIC-SUPPLY-FADE", "symbol": "006110", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_supply_score": 5, "resource_availability_score": 3, "offtake_customer_score": 2, "financing_permitting_score": 2, "utilization_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_supply_score": 3, "resource_availability_score": 1, "offtake_customer_score": 1, "financing_permitting_score": 1, "utilization_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_supply_score", "resource_availability_score", "offtake_customer_score", "financing_permitting_score", "utilization_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified strategic-resource supply, customer/offtake, financing/permitting, utilization, revenue and margin bridge; cap resource policy theme beta when bridge fails to refresh.", "MFE_90D_pct": 34.57, "MAE_90D_pct": -14.68, "score_return_alignment_label": "false_positive_resource_policy_bridge_gap", "current_profile_verdict": "C16 should not treat aluminum/battery-foil supply theme beta as durable Stage2 unless customer volume, utilization, orderbook, pricing and margin bridge are visible. Sam-A Aluminum had an early MFE, then a severe drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 81, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_COBALT_ALUMINUM_FOIL_STRATEGIC_RESOURCE_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C16 strategic-resource symbols outside top-covered 005290/027580/047400/093370 set, +3 cobalt-lithium/lithium-resource/aluminum-foil trigger families, +1 resource recovery lifecycle candidate, +2 resource policy theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 81, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "axis": "lithium_cobalt_aluminum_foil_strategic_resource_supply_bridge_vs_resource_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C16 should split verified strategic-resource supply/recycling/offtake rerating from generic lithium/cobalt/aluminum-foil policy theme beta. Stage2 requires policy/supply premise, mine or material availability, customer/offtake, financing/permitting, utilization, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["005420", "001570", "006110"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 81, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "existing_axis_strengthened": ["stage2_required_bridge", "strategic_resource_supply_bridge_required", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C16 needs strategic resource policy to map into resource availability, customer/offtake, financing/permitting, utilization, revenue and margin proof. Cosmo Chemical is a lifecycle candidate after source repair; Kumyang and Sam-A Aluminum show resource-policy theme beta fading into local 4B when supply and margin bridge are absent or stale."}
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
005420:
  name = 코스모화학 from 2003-07-08, 한국티타늄 before that
  corporate_action_candidate_dates = 1998-12-21, 2000-04-11, 2000-08-14, 2001-09-28, 2003-06-18, 2004-05-06, 2019-12-24
  selected window = 2024-02-01~D+180
  contamination = false

001570:
  name = 금양
  corporate_action_candidate_dates = 1998-12-01, 2000-04-17, 2001-11-29, 2003-08-01, 2007-10-23
  selected window = 2024-02-01~D+180
  contamination = false
  longer-horizon status validation recommended

006110:
  name = 삼아알미늄
  corporate_action_candidate_dates = 2000-10-16, 2000-11-14, 2007-05-04, 2011-04-26, 2023-02-09
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C16 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C16 rule-shape discovery,
but coding-agent promotion requires non-proxy strategic resource policy, mine/supply availability, customer/offtake, financing/permitting, utilization, revenue and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R4/C16 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
lithium_cobalt_aluminum_foil_strategic_resource_supply_bridge_vs_resource_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 005420, 001570 and 006110.
4. Validate 001570 long-horizon listing/status continuity before any extended-window ingestion.
5. Keep generic C16 strategic-resource policy weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - strategic-resource policy or supply-chain premise is explicit,
   - material availability, mine/recycling supply or foil capacity is visible,
   - customer/offtake or volume visibility exists,
   - financing/permitting/utilization is credible,
   - revenue conversion and margin bridge exist,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is lithium/cobalt/aluminum/resource theme beta only,
   - supply/offtake/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price policy reversal, permitting failure, customer loss, financing break, supply failure or margin break.
9. Emit before/after diagnostics and reject if verified strategic-resource supply positives are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 81
next_round = R5
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

