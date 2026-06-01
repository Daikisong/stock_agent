# E2R Stock-Web v12 Residual Research — R5 Loop 72 / L5 / C19

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 72,
  "computed_next_round": "R6",
  "computed_next_loop": 72,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY",
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

Previous completed state in this interactive run: R4 / loop 72.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 72
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
computed_next_round = R6
computed_next_loop = 72
```

R5 was routed to C19 because loop 71 already used C20 heavily, while No-Repeat shows C19 still has fewer rows than C18/C20 and has top-symbol concentration.  
This run avoids repeating F&F / Brand X / The Nature Holdings style top-covered rows and instead uses FILA / Youngone / Handsome.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
081660 / 휠라홀딩스 / Stage2-Actionable-InventoryCleanup / 2024-04-11
111770 / 영원무역 / Stage2-FalsePositive / InventoryDestockingWatch / 2024-02-01
020000 / 한섬 / Stage4B-Local-DomesticFashionInventoryMargin / 2024-04-11
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are marked source_proxy_only=true / evidence_url_pending=true.
This file should therefore be treated as a source-repair queue plus stock-web path calibration, not as immediate runtime weight evidence.
```

## Research thesis

C19 is the “warehouse before the shop window” archetype.

A brand can look healthy on sales talk while the back room is still full of stale goods.  
A real C19 positive happens only when the inventory room clears and margin breathes again.

```text
C19 positive:
  inventory cleanup / channel reset / sell-through normalization
  + margin recovery
  + controlled MAE

C19 false positive:
  generic destocking optimism
  + no customer reorder or margin bridge
  + MFE too small to compensate later MAE

C19 local 4B:
  weak demand / discount burden / inventory drag
  + small MFE
  + widening 90D/180D MAE
```

---

## Case 1 — Positive after source repair: 081660 / 휠라홀딩스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is U.S. inventory cleanup, brand reset, and margin recovery.  
The stock-web path is included because it is a clean C19 positive-shaped path with low MAE.

```text
evidence_family = US_INVENTORY_CLEANUP_BRAND_RESET_MARGIN_RECOVERY
case_role = positive
trigger_date = 2024-04-10
entry_date = 2024-04-11
entry_price = 36,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv`:

```text
2024-04-11,36700,38500,36550,38200
2024-08-01,42400,44550,42400,44450
2024-09-25,43350,44950,43300,43550
2024-11-07,36650,37300,36400,37200
```

### Backtest

```text
MFE_30D  = +12.53%
MAE_30D  = -0.41%
MFE_90D  = +21.39%
MAE_90D  = -0.41%
MFE_180D = +22.48%
MAE_180D = -0.82%
peak_180 = 44,950 on 2024-09-25
trough_180 = 36,400 on 2024-11-07
peak_to_later_drawdown = -19.02%
```

### Interpretation

This is the C19 positive shape.  
The return is not explosive, but the path matters: MFE opens without a large MAE hole. That is exactly how inventory cleanup should look in a brand-retail archetype.

The coding-agent should only promote this after verifying non-proxy evidence for inventory cleanup and margin recovery.

---

## Case 2 — Counterexample: 111770 / 영원무역

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row represents global apparel destocking-recovery optimism without enough customer reorder or margin evidence.

```text
evidence_family = GLOBAL_APPAREL_CUSTOMER_DESTOCKING_RECOVERY_BETA_WITH_WEAK_ORDER_BRIDGE
case_role = counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 48,250
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/111/111770/2024.csv`:

```text
2024-02-01,48250,52700,47550,52300
2024-05-29,33250,33250,32100,32900
2024-10-16,43250,44950,42850,43700
```

### Backtest

```text
MFE_30D  = +9.22%
MAE_30D  = -8.81%
MFE_90D  = +9.22%
MAE_90D  = -33.47%
MFE_180D = +9.22%
MAE_180D = -33.47%
peak_180 = 52,700 on 2024-02-01
trough_180 = 32,100 on 2024-05-29
peak_to_later_drawdown = -39.09%
```

### Interpretation

This is the C19 trap.  
The first candle looks like a reorder signal, but the path turns into a drawdown before the margin story can prove itself.

For C19, “destocking is ending” is not enough.  
The rule must require:

```text
customer reorder evidence
or margin recovery
or sell-through/channel evidence
```

Otherwise the row should become local 4B-watch or false Stage2.

---

## Case 3 — Risk-positive: 020000 / 한섬

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The row tests domestic premium fashion weak-demand / discount / inventory-margin decay.

```text
evidence_family = DOMESTIC_PREMIUM_FASHION_WEAK_DEMAND_DISCOUNT_INVENTORY_MARGIN_DECAY
case_role = risk_positive
trigger_date = 2024-04-10
entry_date = 2024-04-11
entry_price = 19,230
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/020/020000/2024.csv`:

```text
2024-04-11,19230,19390,18920,19320
2024-05-02,19600,19850,19310,19590
2024-08-05,17100,17180,15640,16290
2024-11-14,14520,14560,14270,14370
```

### Backtest

```text
MFE_30D  = +3.22%
MAE_30D  = -4.47%
MFE_90D  = +3.22%
MAE_90D  = -11.75%
MFE_180D = +3.22%
MAE_180D = -25.79%
peak_180 = 19,850 on 2024-05-02
trough_180 = 14,270 on 2024-11-14
peak_to_later_drawdown = -28.11%
```

### Interpretation

This is a local 4B row.  
The stock never earns enough MFE to compensate for the inventory/demand decay. It is not a hard 4C unless non-price evidence confirms a structural break, but it should not stay Stage2.

The rule candidate:

```text
if C19 brand-retail MFE_90D is small
and MAE_180D <= -25%
and demand/inventory margin evidence is weak
then route to local 4B-watch.
```

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
do_not_raise_generic_C19_weight = true
do_not_treat_destocking_beta_as_Green = true
do_not_convert_weak_fashion_demand_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY
```

This fine archetype covers:

```text
1. inventory cleanup + brand/channel reset + margin recovery → Stage2 possible
2. generic global apparel destocking optimism → false Stage2 / local 4B
3. domestic premium-fashion weak demand + discount burden → local 4B-watch
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R5", "loop": 72, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY", "case_id": "R5L72-C19-081660-FILA-US-INVENTORY-CLEANUP-MARGIN-RECOVERY", "symbol": "081660", "company": "휠라홀딩스", "trigger_type": "Stage2-Actionable-InventoryCleanup", "trigger_date": "2024-04-10", "entry_date": "2024-04-11", "entry_price": 36700.0, "mfe_30_pct": 12.53, "mae_30_pct": -0.41, "mfe_90_pct": 21.39, "mae_90_pct": -0.41, "mfe_180_pct": 22.48, "mae_180_pct": -0.82, "peak_price_180": 44950.0, "peak_date_180": "2024-09-25", "trough_price_180": 36400.0, "trough_date_180": "2024-11-07", "peak_to_later_drawdown_pct": -19.02, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "US_INVENTORY_CLEANUP_BRAND_RESET_MARGIN_RECOVERY", "evidence_url": "source_proxy_manual_verification_required:FILA_HOLDINGS_2024_US_INVENTORY_CLEANUP_AND_BRAND_RESET_MARGIN_RECOVERY", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R5", "loop": 72, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY", "case_id": "R5L72-C19-111770-YOUNGONE-APPAREL-DESTOCKING-FALSE-STAGE2", "symbol": "111770", "company": "영원무역", "trigger_type": "Stage2-FalsePositive / InventoryDestockingWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 48250.0, "mfe_30_pct": 9.22, "mae_30_pct": -8.81, "mfe_90_pct": 9.22, "mae_90_pct": -33.47, "mfe_180_pct": 9.22, "mae_180_pct": -33.47, "peak_price_180": 52700.0, "peak_date_180": "2024-02-01", "trough_price_180": 32100.0, "trough_date_180": "2024-05-29", "peak_to_later_drawdown_pct": -39.09, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "GLOBAL_APPAREL_CUSTOMER_DESTOCKING_RECOVERY_BETA_WITH_WEAK_ORDER_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:YOUNGONE_GLOBAL_APPAREL_DESTOCKING_RECOVERY_WITH_WEAK_REORDER_BRIDGE_2024", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R5", "loop": 72, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY", "case_id": "R5L72-C19-020000-HANSSEM-DOMESTIC-FASHION-DEMAND-INVENTORY-DECAY", "symbol": "020000", "company": "한섬", "trigger_type": "Stage4B-Local-DomesticFashionInventoryMargin", "trigger_date": "2024-04-10", "entry_date": "2024-04-11", "entry_price": 19230.0, "mfe_30_pct": 3.22, "mae_30_pct": -4.47, "mfe_90_pct": 3.22, "mae_90_pct": -11.75, "mfe_180_pct": 3.22, "mae_180_pct": -25.79, "peak_price_180": 19850.0, "peak_date_180": "2024-05-02", "trough_price_180": 14270.0, "trough_date_180": "2024-11-14", "peak_to_later_drawdown_pct": -28.11, "case_role": "risk_positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "DOMESTIC_PREMIUM_FASHION_WEAK_DEMAND_DISCOUNT_INVENTORY_MARGIN_DECAY", "evidence_url": "source_proxy_manual_verification_required:HANSSEM_DOMESTIC_PREMIUM_FASHION_WEAK_DEMAND_INVENTORY_MARGIN_DECAY_2024", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R5L72-C19-081660-FILA-US-INVENTORY-CLEANUP-MARGIN-RECOVERY", "symbol": "081660", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 9, "earnings_visibility": 12, "bottleneck_pricing_power": 4, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["brand_retail_inventory_margin", "inventory_cleanup_or_destocking", "margin_recovery_bridge_present", "stage2_candidate", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable after source repair", "profile_stress_result": "C19 should allow Stage2 only when inventory cleanup or channel reset is tied to margin recovery, not when price is merely bouncing after a discount cycle."}
{"row_type": "score_simulation", "case_id": "R5L72-C19-111770-YOUNGONE-APPAREL-DESTOCKING-FALSE-STAGE2", "symbol": "111770", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 5, "bottleneck_pricing_power": 2, "market_mispricing": 12, "valuation_rerating": 5, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["brand_retail_inventory_margin", "inventory_cleanup_or_destocking", "margin_bridge_weak_or_decaying", "local_4b_watch", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "Global apparel destocking recovery beta can produce a one-week MFE, but without customer reorder and margin evidence it should not become durable Stage2/Green."}
{"row_type": "score_simulation", "case_id": "R5L72-C19-020000-HANSSEM-DOMESTIC-FASHION-DEMAND-INVENTORY-DECAY", "symbol": "020000", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 5, "bottleneck_pricing_power": 2, "market_mispricing": 12, "valuation_rerating": 5, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["brand_retail_inventory_margin", "inventory_cleanup_or_destocking", "margin_bridge_weak_or_decaying", "local_4b_watch", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "Domestic premium fashion with weak sell-through and inventory/discount burden should move to local 4B-watch when MFE remains small and 180D MAE widens."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 72, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "risk_positive_case_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C19 symbols, +3 inventory/margin trigger families, +1 margin-cleanup positive, +2 local-4B/counterexample paths, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 72, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "axis": "apparel_inventory_cleanup_margin_recovery_vs_discount_demand_decay", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C19 should split true inventory cleanup/margin recovery from generic apparel destocking beta. Stage2 requires sell-through, inventory reduction, or margin recovery evidence; local 4B-watch should fire when MFE is small or temporary and MAE/drawdown widens under weak demand or discount burden.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["081660", "111770", "020000"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 72, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C19 should not reward apparel/brand stocks for simple destocking optimism. True positive cases need inventory cleanup or channel reset to become visible in margin recovery and controlled MAE. Weak reorder, domestic fashion demand decay, or discount burden should route to local 4B-watch when MFE remains small and MAE widens."}
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
081660:
  corporate_action_candidate_dates = 2018-05-09
  selected window = 2024-04-11~D+180
  contamination = false

111770:
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

020000:
  corporate_action_candidate_dates = 1997-01-03, 1999-07-26, 2003-07-15, 2008-01-16
  selected window = 2024-04-11~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C19 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and source-repair queue creation,
but coding-agent promotion requires non-proxy company-level evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R5/C19 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
apparel_inventory_cleanup_margin_recovery_vs_discount_demand_decay

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 081660, 111770 and 020000.
4. Keep generic C19 weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - inventory cleanup is explicitly evidenced,
   - sell-through/channel reset or reorder evidence exists,
   - margin recovery is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - MFE_90D is small or only one-candle,
   - MAE_180D <= -25% or post-peak drawdown <= -35%,
   - demand, discount, or inventory burden persists,
   - reorder/margin bridge is weak or stale.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if C19 overblocks verified margin-recovery positives.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 72
next_round = R6
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

