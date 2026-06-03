# E2R Stock-Web v12 Residual Research — R1 Loop 72 / L1 / C02

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 72,
  "computed_next_round": "R2",
  "computed_next_loop": 72,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF",
  "loop_objective": [
    "coverage_gap_fill",
    "residual_missed_structural_mining",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression"
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

Previous completed state in this interactive run: R13 / loop 71.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 72
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
computed_next_round = R2
computed_next_loop = 72
```

R1 was routed to C02 because the no-repeat coverage table effectively starts at C03 and does not yet show C01/C02/C05 representative coverage.  
This run therefore fills a genuine R1 coverage gap rather than rematerializing a previously crowded R1 defense or nuclear set.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
267260 / HD현대일렉트릭 / Stage2-Actionable / 2024-04-23
010120 / LS ELECTRIC / Stage4B-Local-PriceOnly-GridEquipmentBlowoff / 2024-07-01
298040 / 효성중공업 / Stage2-Actionable / 2024-04-29
```

Data-quality note:

```text
267260 and 298040 are calibration-usable on stock-web OHLC,
but evidence rows are marked source_proxy_only=true / evidence_url_pending=true.
They should be treated as source-repair candidates before any runtime weight change.
```

## Research thesis

C02 is not just “AI needs electricity.”

The correct mechanism is a bridge:

```text
data center / renewable / grid capex demand
→ transformer and high-voltage equipment shortage
→ order backlog / delivery slots / export pricing
→ margin conversion
→ durable rerating
```

A power-equipment chart can look like a transformer itself: it hums with load, but the question is whether current is actually flowing through copper, or whether the meter is only reacting to a nearby storm.

The residual split is:

```text
C02 positive:
  transformer/datacenter capex thesis + backlog or capacity evidence + margin conversion

C02 local 4B watch:
  grid-equipment/AI-power theme MFE + valuation blowoff + high MAE/drawdown + stale or weak bridge evidence
```

---

## Case 1 — Positive bridge: 267260 / HD현대일렉트릭

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family is the 2024 transformer shortage / North America export / backlog-to-margin bridge.  
The stock-web path is included because C02 itself is a missing coverage gap, but non-proxy evidence should be repaired before coding-agent promotion.

```text
evidence_family = US_TRANSFORMER_SHORTAGE_BACKLOG_MARGIN_BRIDGE
case_role = positive
trigger_date = 2024-04-22
entry_date = 2024-04-23
entry_price = 229,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv` and `2025.csv`:

```text
2024-04-23,229000,251500,210000,240000
2024-07-24,351000,374500,345500,365500
2025-01-09,401500,417500,398000,414000
```

### Backtest

```text
MFE_30D  = +37.12%
MAE_30D  = -8.30%
MFE_90D  = +63.54%
MAE_90D  = -8.30%
MFE_180D = +82.31%
MAE_180D = -8.30%
peak_180 = 417,500 on 2025-01-09
trough_180 = 210,000 on 2024-04-23
peak_to_later_drawdown = -12.46%
```

### Interpretation

This is the clean C02 positive shape.  
The price path moved with relatively contained MAE, and the later peak was not just a one-day theme candle. The mechanism to test in future rows is not price momentum; it is whether backlog/margin evidence appears before the rerating.

---

## Case 2 — Counterexample / local 4B: 010120 / LS ELECTRIC

### Evidence

MarketWatch reported a Daiwa view that LS Electric could benefit from U.S. business growth, with U.S. revenue potentially rising materially as data-center construction, renewable-energy projects, and EV value-chain investment increased. That is a valid C02 thesis, but the post-trigger price path shows why bridge quality and valuation temperature must be separated.

```text
evidence_family = US_BUSINESS_GROWTH_DATACENTER_RENEWABLE_CAPEX_ANALYST_RERATING
case_role = counterexample
trigger_date = 2024-07-01
entry_date = 2024-07-01
entry_price = 218,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv` and `2025.csv`:

```text
2024-07-01,218000,220000,203000,204500
2024-09-09,130200,137300,126200,136800
2025-02-19,290500,303500,280500,286500
```

### Backtest

```text
MFE_30D  = +25.92%
MAE_30D  = -33.49%
MFE_90D  = +25.92%
MAE_90D  = -42.11%
MFE_180D = +39.22%
MAE_180D = -42.11%
peak_180 = 303,500 on 2025-02-19
trough_180 = 126,200 on 2024-09-09
peak_to_later_drawdown = -42.50%
```

### Interpretation

This is not a failed theme.  
It is a timing failure.

The C02 story eventually worked again, but the July 2024 entry carried severe MAE before the later high. A Stage2/Green model that only sees “U.S. data-center growth” would be too generous. The right label is:

```text
C02 local 4B-watch / no durable Green at the July valuation temperature
```

The bridge existed as a thesis, but the tradeable entry needed a drawdown/valuation guard.

---

## Case 3 — Positive bridge: 298040 / 효성중공업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row is used as a clean OHLC positive anchor because the stock-web profile has no corporate-action candidate dates.  
The evidence family is U.S. transformer manufacturing / Hyosung HICO / transformer shortage visibility, but non-proxy evidence must be repaired before runtime promotion.

```text
evidence_family = TRANSFORMER_SHORTAGE_US_MANUFACTURING_HICO_ORDER_VISIBILITY
case_role = positive
trigger_date = 2024-04-26
entry_date = 2024-04-29
entry_price = 289,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv` and `2025.csv`:

```text
2024-04-29,289000,318500,284000,312000
2024-05-28,430000,469000,423000,449500
2025-01-20,482000,490000,447500,456500
```

### Backtest

```text
MFE_30D  = +62.28%
MAE_30D  = -1.73%
MFE_90D  = +62.28%
MAE_90D  = -17.30%
MFE_180D = +69.55%
MAE_180D = -17.30%
peak_180 = 490,000 on 2025-01-20
trough_180 = 239,000 on 2024-09-09
peak_to_later_drawdown = -14.29%
```

### Interpretation

This is the second C02 positive anchor.  
Unlike the LS Electric July row, the early entry had very low 30D MAE and strong MFE. Later volatility existed, but the path did not become a collapse from the entry basis.

This supports a scoped C02 rule:

```text
when transformer shortage evidence is tied to manufacturing capacity or order visibility,
Stage2 may need to arrive before the full price breakout.
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
do_not_raise_generic_C02_weight_yet = true
do_not_treat_all_AI_power_grid_names_as_Green = true
do_not_relax_full_4B_non_price_evidence = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF
```

This fine archetype covers:

```text
1. transformer/datacenter capex + backlog/margin bridge → Stage2-Actionable possible
2. U.S. growth / analyst rerating + severe MAE → local 4B-watch
3. transformer manufacturing capacity + order visibility → Stage2-Actionable possible
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R1", "loop": 72, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF", "case_id": "R1L72-C02-267260-HDHE-US-TRANSFORMER-BACKLOG-MARGIN-BRIDGE", "symbol": "267260", "company": "HD현대일렉트릭", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-22", "entry_date": "2024-04-23", "entry_price": 229000.0, "mfe_30_pct": 37.12, "mae_30_pct": -8.3, "mfe_90_pct": 63.54, "mae_90_pct": -8.3, "mfe_180_pct": 82.31, "mae_180_pct": -8.3, "peak_price_180": 417500.0, "peak_date_180": "2025-01-09", "trough_price_180": 210000.0, "trough_date_180": "2024-04-23", "peak_to_later_drawdown_pct": -12.46, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "US_TRANSFORMER_SHORTAGE_BACKLOG_MARGIN_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:HD_HYUNDAI_ELECTRIC_Q1_2024_US_TRANSFORMER_ORDER_BACKLOG_MARGIN_BRIDGE", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R1", "loop": 72, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF", "case_id": "R1L72-C02-010120-LS-ELECTRIC-US-DATACENTER-GROWTH-PRICE-ONLY-4B", "symbol": "010120", "company": "LS ELECTRIC", "trigger_type": "Stage4B-Local-PriceOnly-GridEquipmentBlowoff", "trigger_date": "2024-07-01", "entry_date": "2024-07-01", "entry_price": 218000.0, "mfe_30_pct": 25.92, "mae_30_pct": -33.49, "mfe_90_pct": 25.92, "mae_90_pct": -42.11, "mfe_180_pct": 39.22, "mae_180_pct": -42.11, "peak_price_180": 303500.0, "peak_date_180": "2025-02-19", "trough_price_180": 126200.0, "trough_date_180": "2024-09-09", "peak_to_later_drawdown_pct": -42.5, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "US_BUSINESS_GROWTH_DATACENTER_RENEWABLE_CAPEX_ANALYST_RERATING", "evidence_url": "https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067", "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "round": "R1", "loop": 72, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF", "case_id": "R1L72-C02-298040-HYOSUNG-US-TRANSFORMER-HICO-BRIDGE", "symbol": "298040", "company": "효성중공업", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-26", "entry_date": "2024-04-29", "entry_price": 289000.0, "mfe_30_pct": 62.28, "mae_30_pct": -1.73, "mfe_90_pct": 62.28, "mae_90_pct": -17.3, "mfe_180_pct": 69.55, "mae_180_pct": -17.3, "peak_price_180": 490000.0, "peak_date_180": "2025-01-20", "trough_price_180": 239000.0, "trough_date_180": "2024-09-09", "peak_to_later_drawdown_pct": -14.29, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "TRANSFORMER_SHORTAGE_US_MANUFACTURING_HICO_ORDER_VISIBILITY", "evidence_url": "source_proxy_manual_verification_required:HYOSUNG_HEAVY_TRANSFORMER_US_HICO_BACKLOG_CAPACITY_BRIDGE_2024", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R1L72-C02-267260-HDHE-US-TRANSFORMER-BACKLOG-MARGIN-BRIDGE", "symbol": "267260", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 14, "earnings_visibility": 15, "bottleneck_pricing_power": 18, "market_mispricing": 12, "valuation_rerating": 12, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["power_grid_datacenter_capex", "transformer_shortage", "non_price_bridge_present", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable", "profile_stress_result": "C02 should allow early Stage2 when transformer/datacenter demand is tied to order backlog, export pricing, and margin conversion rather than generic AI/power-grid beta."}
{"row_type": "score_simulation", "case_id": "R1L72-C02-010120-LS-ELECTRIC-US-DATACENTER-GROWTH-PRICE-ONLY-4B", "symbol": "010120", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 11, "bottleneck_pricing_power": 13, "market_mispricing": 14, "valuation_rerating": 15, "capital_allocation": 2, "information_confidence": 4}, "diagnostic_flags": ["power_grid_datacenter_capex", "transformer_shortage", "valuation_blowoff_after_grid_theme", "verified_external_evidence"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "US/datacenter revenue-growth narrative produced further MFE later, but the 180D path had severe MAE and post-peak drawdown. C02 needs local 4B-watch when order visibility is not enough to absorb valuation blowoff."}
{"row_type": "score_simulation", "case_id": "R1L72-C02-298040-HYOSUNG-US-TRANSFORMER-HICO-BRIDGE", "symbol": "298040", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 14, "earnings_visibility": 15, "bottleneck_pricing_power": 18, "market_mispricing": 12, "valuation_rerating": 12, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["power_grid_datacenter_capex", "transformer_shortage", "non_price_bridge_present", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable", "profile_stress_result": "C02 should not require price confirmation after the full breakout when a transformer maker has manufacturing capacity/US grid exposure and the return path confirms backlog-to-margin conversion."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 72, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 2, "evidence_url_pending_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 new symbols, +3 C02 trigger families, +2 structural transformer positives, +1 valuation-blowoff/local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 72, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "axis": "transformer_datacenter_capex_backlog_bridge_vs_price_only_grid_equipment_blowoff", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C02 needs a bridge split: transformer/datacenter CAPEX with backlog, export pricing, capacity and margin conversion can be Stage2-Actionable; price-only grid equipment rerating after large MFE should become local 4B-watch when MAE/drawdown rises and backlog-to-margin evidence is not fresh.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["267260", "298040"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 72, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C02 is not generic AI electricity enthusiasm. The positive route requires transformer/datacenter CAPEX evidence to connect into backlog, pricing, capacity and margin conversion. When valuation rerating outruns bridge evidence, local 4B-watch should fire before full 4B."}
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
267260:
  corporate_action_candidate_dates = 2017-11-17, 2017-11-28, 2017-12-11, 2018-11-23, 2018-12-18, 2019-12-30
  selected window = 2024-04-23~D+180
  contamination = false

010120:
  corporate_action_candidate_dates = 1995-09-28, 1999-04-08, 1999-07-26, 2003-04-16
  selected window = 2024-07-01~D+180
  contamination = false

298040:
  corporate_action_candidate_dates = none
  selected window = 2024-04-29~D+180
  contamination = false
```

Data-quality caveat:

```text
267260 and 298040 source URLs are proxy/pending.
They should be treated as source-repair candidates before any coding agent promotes a runtime rule.
010120 has verified external evidence but is a counterexample/local-4B row, not a positive weight row.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C02 artifact is marked do_not_propose_new_weight_delta=true because two positive rows need source repair.

Candidate axis:
transformer_datacenter_capex_backlog_bridge_vs_price_only_grid_equipment_blowoff

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 267260 and 298040.
4. Keep generic C02 positive weight unchanged until source repair is complete.
5. Consider scoped Stage2 bridge logic only when:
   - transformer/datacenter/grid capex evidence exists,
   - order backlog or delivery-slot visibility is present,
   - pricing/margin conversion is visible,
   - evidence is not merely AI-power-grid price momentum.
6. Consider local-4B-watch if:
   - MFE_30D >= 25%,
   - MAE_90D <= -25% or post-peak drawdown <= -35%,
   - bridge evidence is stale/weak,
   - valuation rerating has outrun backlog/margin confirmation.
7. Do not convert local 4B-watch into full 4B without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if C02 missed structural positives increase.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 72
next_round = R2
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

