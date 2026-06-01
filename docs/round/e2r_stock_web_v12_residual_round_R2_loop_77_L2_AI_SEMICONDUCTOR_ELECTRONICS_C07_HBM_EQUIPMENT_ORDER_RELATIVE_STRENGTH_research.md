# E2R Stock-Web v12 Residual Research — R2 Loop 77 / L2 / C07

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 77,
  "computed_next_round": "R3",
  "computed_next_loop": 77,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "HBM_AI_equipment_order_RS_guardrail",
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

Previous completed state in this interactive run: R1 / loop 77.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 77
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
computed_next_round = R3
computed_next_loop = 77
```

R2 was routed to C07 because loop 76 used C10 and visible C07 coverage is concentrated in a small set of well-known HBM equipment names.  
This file tests tester / deposition / metrology equipment relative-strength bridges rather than memory-maker capacity or pure valuation blowoff.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Visible No-Repeat L2 concentration:

```text
C07 top-covered = 042700, 089030, 039030, 058470, 095340
C08 top-covered = 058470, 131290, 리노공업, 티에스이, 095340
C09 top-covered = 039030, 042700, 095340, 이오테크닉스, 한미반도체
```

This run uses three different symbols:

```text
232140 / 와이아이케이·와이씨 / HBM memory tester order relative strength
084370 / 유진테크 / deposition equipment order relative strength
322310 / 오로스테크놀로지 / metrology equipment theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
232140 changed name from 와이아이케이 to 와이씨 on 2024-04-25, after the selected 2024-04-17 entry.
```

## Research thesis

C07 is not “반도체 장비주가 올랐다.”

The mechanism must pass through:

```text
HBM / AI / memory capex
→ named equipment order or customer qualification
→ delivery backlog / tool adoption
→ utilization and margin bridge
→ durable relative-strength rerating
```

장비주는 불이 켜진 공장처럼 보일 수 있다.  
C07이 보려는 것은 조명보다 더 안쪽의 발주서, 납기표, 고객 품질, 마진이다.

---

## Case 1 — Positive with lifecycle 4B: 232140 / 와이아이케이·와이씨

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is HBM/memory tester equipment order, customer capex, delivery backlog and margin bridge evidence.

```text
evidence_family = HBM_MEMORY_TESTER_ORDER_CUSTOMER_CAPEX_DELIVERY_BACKLOG_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-16
entry_date = 2024-04-17
entry_price = 6,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv`:

```text
2024-04-17,6300,7540,6280,7280
2024-04-26,12550,14980,12270,14090
2024-05-31,13930,17910,13800,17910
2024-06-13,19110,22950,18660,21900
2024-08-05,16000,16020,12560,13730
2024-10-23,10690,11720,10640,11480
```

### Backtest

```text
MFE_30D  = +180.32%
MAE_30D  = -0.32%
MFE_90D  = +264.29%
MAE_90D  = -0.32%
MFE_180D = +264.29%
MAE_180D = -0.32%
peak_180 = 22,950 on 2024-06-13
trough_180 = 6,280 on 2024-04-17
peak_to_later_drawdown = -53.64%
```

### Interpretation

This is a strong C07 equipment-RS positive after source repair.  
The entry-basis risk was controlled and MFE expanded extremely fast.

Correct treatment:

```text
verified tester order / customer capex / delivery backlog / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Positive with lifecycle 4B: 084370 / 유진테크

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is deposition equipment order, customer capex, delivery schedule and margin bridge evidence.

```text
evidence_family = MEMORY_HBM_DEPOSITION_EQUIPMENT_CUSTOMER_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-02-19
entry_date = 2024-02-20
entry_price = 34,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv`:

```text
2024-02-20,34500,38150,34500,36700
2024-03-21,37750,41900,37400,41450
2024-04-05,45500,50500,45100,49950
2024-05-28,53800,60000,53600,56500
2024-08-05,43200,43600,37400,38800
2024-10-18,36050,36750,34250,34600
```

### Backtest

```text
MFE_30D  = +29.57%
MAE_30D  = -1.45%
MFE_90D  = +73.91%
MAE_90D  = -1.45%
MFE_180D = +73.91%
MAE_180D = -1.45%
peak_180 = 60,000 on 2024-05-28
trough_180 = 34,000 around 2024-03-14~2024-03-15
peak_to_later_drawdown = -42.92%
```

### Interpretation

This is a cleaner controlled-MAE C07 row.  
It should be protected after source repair, but not left as permanent Green if capex/order/margin evidence fades.

Correct treatment:

```text
Stage2 possible after source repair
lifecycle local 4B if equipment order/margin bridge decays
```

---

## Case 3 — Counterexample / local 4B: 322310 / 오로스테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests metrology / overlay equipment theme beta without enough customer order and margin bridge.

```text
evidence_family = METROLOGY_OVERLAY_EQUIPMENT_HBM_THEME_WITH_WEAK_ORDER_MARGIN_BRIDGE
case_role = counterexample_equipment_theme_local4b
trigger_date = 2024-01-23
entry_date = 2024-01-24
entry_price = 31,050
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv`:

```text
2024-01-24,31050,36600,30800,34650
2024-01-25,37550,38550,34200,34450
2024-02-27,36100,40750,34050,37200
2024-05-24,24850,25600,24150,24550
2024-08-05,19950,19980,16300,16860
2024-09-09,15300,15950,15130,15730
```

### Backtest

```text
MFE_30D  = +31.24%
MAE_30D  = -14.01%
MFE_90D  = +31.24%
MAE_90D  = -22.22%
MFE_180D = +31.24%
MAE_180D = -51.27%
peak_180 = 40,750 on 2024-02-27
trough_180 = 15,130 on 2024-09-09
peak_to_later_drawdown = -62.87%
```

### Interpretation

This is the dangerous C07 false-positive shape.  
The early MFE was real, but it did not prove durable equipment order rerating.

Correct treatment:

```text
metrology / equipment theme beta
→ no verified order / tool adoption / margin bridge
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
```

### What this does not justify

```text
do_not_raise_generic_C07_equipment_RS_weight = true
do_not_treat_all_HBM_equipment_MFE_as_Green = true
do_not_convert_equipment_drawdown_to_hard_4C_without_non_price_customer_order_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE
```

This fine archetype covers:

```text
1. HBM/memory tester order relative strength → Stage2 possible after source repair
2. deposition equipment capex/order relative strength → Stage2 possible, lifecycle-managed
3. metrology equipment theme beta without order/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE", "symbol": "232140", "company_name": "와이아이케이/와이씨", "round": "R2", "loop": "77", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "case_type": "HBM_equipment_order_relative_strength", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-HBMTesterOrderRelativeStrengthBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 should allow HBM/AI tester equipment winners when relative strength connects to customer capex, tester order, delivery backlog and margin bridge. YC/YIK produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown requires lifecycle local 4B if order/backlog/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer capex, equipment order, delivery/backlog, tool adoption and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "77", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "case_type": "HBM_equipment_order_relative_strength", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-DepositionEquipmentOrderRSBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 should preserve equipment relative-strength rows when customer capex, deposition equipment orders, delivery schedule and margin bridge are visible. Eugene Technology had a controlled-MAE rerating path; later drawdown should be lifecycle-managed, not treated as hard 4C without order or margin break.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer capex, equipment order, delivery/backlog, tool adoption and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": "77", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "case_type": "HBM_equipment_order_relative_strength", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / MetrologyEquipmentThemeBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 should not treat metrology/overlay equipment beta as durable Stage2 unless customer order, delivery, tool adoption and margin bridge are visible. Auros Technology had a tradable early MFE, but then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer capex, equipment order, delivery/backlog, tool adoption and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE", "case_id": "R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE", "symbol": "232140", "company_name": "와이아이케이/와이씨", "round": "R2", "loop": "77", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_AI_equipment_order_RS_guardrail", "trigger_type": "Stage2-Actionable-HBMTesterOrderRelativeStrengthBridgeWithLifecycle4B", "trigger_date": "2024-04-16", "entry_date": "2024-04-17", "entry_price": 6300.0, "evidence_available_at_that_date": "HBM_MEMORY_TESTER_ORDER_CUSTOMER_CAPEX_DELIVERY_BACKLOG_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:YC_YIK_2024_HBM_MEMORY_TESTER_ORDER_CUSTOMER_CAPEX_DELIVERY_BACKLOG_MARGIN_BRIDGE", "stage2_evidence_fields": ["HBM_or_AI_customer_capex_candidate", "equipment_order_or_delivery_backlog_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_tool_adoption_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "profile_path": "atlas/symbol_profiles/232/232140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 180.32, "MFE_90D_pct": 264.29, "MFE_180D_pct": 264.29, "MAE_30D_pct": -0.32, "MAE_90D_pct": -0.32, "MAE_180D_pct": -0.32, "peak_date": "2024-06-13", "peak_price": 22950.0, "drawdown_after_peak_pct": -53.64, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_RS_peak_if_order_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_capex_delivery_margin_or_tool_adoption_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C07 should allow HBM/AI tester equipment winners when relative strength connects to customer capex, tester order, delivery backlog and margin bridge. YC/YIK produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown requires lifecycle local 4B if order/backlog/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C07_EQUIPMENT_RS_232140_2024-04-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "case_id": "R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "77", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_AI_equipment_order_RS_guardrail", "trigger_type": "Stage2-Actionable-DepositionEquipmentOrderRSBridgeWithLifecycle4B", "trigger_date": "2024-02-19", "entry_date": "2024-02-20", "entry_price": 34500.0, "evidence_available_at_that_date": "MEMORY_HBM_DEPOSITION_EQUIPMENT_CUSTOMER_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:EUGENE_TECH_2024_MEMORY_HBM_DEPOSITION_EQUIPMENT_ORDER_CUSTOMER_CAPEX_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["HBM_or_AI_customer_capex_candidate", "equipment_order_or_delivery_backlog_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_tool_adoption_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv", "profile_path": "atlas/symbol_profiles/084/084370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.57, "MFE_90D_pct": 73.91, "MFE_180D_pct": 73.91, "MAE_30D_pct": -1.45, "MAE_90D_pct": -1.45, "MAE_180D_pct": -1.45, "peak_date": "2024-05-28", "peak_price": 60000.0, "drawdown_after_peak_pct": -42.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_RS_peak_if_order_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_capex_delivery_margin_or_tool_adoption_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C07 should preserve equipment relative-strength rows when customer capex, deposition equipment orders, delivery schedule and margin bridge are visible. Eugene Technology had a controlled-MAE rerating path; later drawdown should be lifecycle-managed, not treated as hard 4C without order or margin break.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C07_EQUIPMENT_RS_084370_2024-02-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE", "case_id": "R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": "77", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_AI_equipment_order_RS_guardrail", "trigger_type": "Stage2-FalsePositive / MetrologyEquipmentThemeBetaFade", "trigger_date": "2024-01-23", "entry_date": "2024-01-24", "entry_price": 31050.0, "evidence_available_at_that_date": "METROLOGY_OVERLAY_EQUIPMENT_HBM_THEME_WITH_WEAK_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:AUROS_TECHNOLOGY_2024_METROLOGY_OVERLAY_EQUIPMENT_ORDER_TOOL_ADOPTION_MARGIN_BRIDGE", "stage2_evidence_fields": ["HBM_or_AI_customer_capex_candidate", "equipment_order_or_delivery_backlog_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_tool_adoption_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv", "profile_path": "atlas/symbol_profiles/322/322310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.24, "MFE_90D_pct": 31.24, "MFE_180D_pct": 31.24, "MAE_30D_pct": -14.01, "MAE_90D_pct": -22.22, "MAE_180D_pct": -51.27, "peak_date": "2024-02-27", "peak_price": 40750.0, "drawdown_after_peak_pct": -62.87, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_RS_peak_if_order_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_capex_delivery_margin_or_tool_adoption_break", "trigger_outcome_label": "counterexample_equipment_theme_local4b", "current_profile_verdict": "C07 should not treat metrology/overlay equipment beta as durable Stage2 unless customer order, delivery, tool adoption and margin bridge are visible. Auros Technology had a tradable early MFE, but then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C07_EQUIPMENT_RS_322310_2024-01-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE", "trigger_id": "TRG_R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE", "symbol": "232140", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"HBM_AI_capex_score": 13, "equipment_order_score": 14, "customer_quality_score": 13, "delivery_backlog_score": 12, "margin_bridge_score": 12, "relative_strength_score": 16, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"HBM_AI_capex_score": 12, "equipment_order_score": 16, "customer_quality_score": 15, "delivery_backlog_score": 14, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["equipment_order_score", "customer_quality_score", "delivery_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified equipment orders, customer capex, delivery/backlog, tool adoption and margin bridge; cap equipment theme beta when evidence fails to refresh.", "MFE_90D_pct": 264.29, "MAE_90D_pct": -0.32, "score_return_alignment_label": "equipment_order_RS_positive_with_lifecycle_4b", "current_profile_verdict": "C07 should allow HBM/AI tester equipment winners when relative strength connects to customer capex, tester order, delivery backlog and margin bridge. YC/YIK produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown requires lifecycle local 4B if order/backlog/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "trigger_id": "TRG_R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "symbol": "084370", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"HBM_AI_capex_score": 13, "equipment_order_score": 14, "customer_quality_score": 13, "delivery_backlog_score": 12, "margin_bridge_score": 12, "relative_strength_score": 16, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"HBM_AI_capex_score": 12, "equipment_order_score": 16, "customer_quality_score": 15, "delivery_backlog_score": 14, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["equipment_order_score", "customer_quality_score", "delivery_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified equipment orders, customer capex, delivery/backlog, tool adoption and margin bridge; cap equipment theme beta when evidence fails to refresh.", "MFE_90D_pct": 73.91, "MAE_90D_pct": -1.45, "score_return_alignment_label": "equipment_order_RS_positive_with_lifecycle_4b", "current_profile_verdict": "C07 should preserve equipment relative-strength rows when customer capex, deposition equipment orders, delivery schedule and margin bridge are visible. Eugene Technology had a controlled-MAE rerating path; later drawdown should be lifecycle-managed, not treated as hard 4C without order or margin break."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE", "trigger_id": "TRG_R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE", "symbol": "322310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"HBM_AI_capex_score": 6, "equipment_order_score": 4, "customer_quality_score": 4, "delivery_backlog_score": 3, "margin_bridge_score": 2, "relative_strength_score": 8, "execution_risk_score": 19, "source_confidence_score": 2}, "weighted_score_before": 51, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"HBM_AI_capex_score": 4, "equipment_order_score": 2, "customer_quality_score": 2, "delivery_backlog_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 38, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["equipment_order_score", "customer_quality_score", "delivery_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified equipment orders, customer capex, delivery/backlog, tool adoption and margin bridge; cap equipment theme beta when evidence fails to refresh.", "MFE_90D_pct": 31.24, "MAE_90D_pct": -22.22, "score_return_alignment_label": "false_positive_equipment_theme_bridge_gap", "current_profile_verdict": "C07 should not treat metrology/overlay equipment beta as durable Stage2 unless customer order, delivery, tool adoption and margin bridge are visible. Auros Technology had a tradable early MFE, but then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 77, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C07 equipment symbols outside visible top-covered 042700/089030 concentration, +3 tester/deposition/metrology trigger families, +2 controlled-MAE equipment RS positives, +1 metrology theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 77, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "axis": "HBM_tester_deposition_metrology_equipment_order_RS_bridge_vs_equipment_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C07 should split verified HBM/AI equipment order relative strength from generic equipment beta. Stage2 requires customer capex, equipment order, delivery/backlog, tool adoption and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["232140", "084370", "322310"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 77, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C07 needs equipment order and customer-quality proof. YC/YIK and Eugene Technology show HBM/tester/deposition equipment RS positives after source repair; Auros Technology shows metrology equipment beta fading into local 4B when customer order and margin bridge are absent."}
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
232140:
  name = 와이아이케이 until 2024-04-24, 와이씨 from 2024-04-25
  corporate_action_candidate_dates = 2017-04-05
  selected window = 2024-04-17~D+180
  contamination = false

084370:
  corporate_action_candidate_dates = 2007-05-17, 2010-01-22, 2012-06-07
  selected window = 2024-02-20~D+180
  contamination = false

322310:
  corporate_action_candidate_dates = none
  selected window = 2024-01-24~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C07 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C07 rule-shape discovery,
but coding-agent promotion requires non-proxy customer capex, equipment order, delivery/backlog, tool adoption and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C07 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
HBM_tester_deposition_metrology_equipment_order_RS_bridge_vs_equipment_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 232140, 084370 and 322310.
4. Keep generic C07 equipment-RS weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - HBM/AI/memory capex demand is explicit,
   - equipment order or customer qualification is visible,
   - delivery backlog or tool adoption bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is equipment/metrology theme beta only,
   - order/delivery/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer order cut, capex cancellation, delivery delay, utilization collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified tester/deposition equipment positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 77
next_round = R3
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

