# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 72
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_EQUIPMENT_DATACENTER_CAPEX_EQUIPMENT_VS_WIRE_PROXY_SPLIT
output_file = e2r_stock_web_v12_residual_round_R1_loop_72_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

One-line contribution: This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the global Stage2/Green/4B rules. It stress-tests a narrower C02 residual: transformer/switchgear equipment bridges behaved differently from wire/copper proxy momentum, even when all names were pulled by the same grid/data-center CAPEX narrative.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R1 |
| scheduled_loop | 72 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX |
| fine_archetype_id | GRID_EQUIPMENT_DATACENTER_CAPEX_EQUIPMENT_VS_WIRE_PROXY_SPLIT |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R1 allows L1 only. This file uses C02 inside L1 and does not jump to a coverage gap outside the scheduled round.

## 3. Previous Coverage / Duplicate Avoidance Check

No stock_agent source code was opened or inferred. Duplicate avoidance uses the v12 hard key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

The loop deliberately reuses the C02 canonical bucket but uses new symbol/trigger-family combinations for this loop. The repeated archetype is not penalized; repeated symbol/date/evidence would be.

| Case | Symbol | Trigger family | Entry date | Duplicate status | Novelty reason |
|---|---:|---|---|---|---|
| CASE_R1_72_LS_ELECTRIC_DATACENTER_GRID | 010120 | equipment order / margin bridge | 2024-03-05 | non-duplicate | equipment bridge positive |
| CASE_R1_72_HYOSUNG_HEAVY_TRANSFORMER | 298040 | transformer backlog / margin bridge | 2024-03-04 | non-duplicate | high-MAE success positive |
| CASE_R1_72_DAEWON_WIRE_PROXY_BLOWOFF | 006340 | wire proxy / price-only blowoff | 2024-04-05 | non-duplicate | relative-strength counterexample |
| CASE_R1_72_TAIHAN_WIRE_PROXY_CAPEX_DILUTION | 001440 | wire proxy / capital-intensity overhang | 2024-04-05 | non-duplicate | proxy counterexample and 4B watch |

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Manifest facts used by this loop:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

## 5. Historical Eligibility Gate

All four representative triggers are historical and use stock-web tradable rows. Forward 180D windows are available before the manifest max date. The 2024 windows used here do not overlap corporate-action candidate dates inside the post-entry 180D interval. 대한전선 has a 2024-04-02 corporate-action candidate, so the representative entry is deliberately set to the later 2024-04-05 tradable close.

| Symbol | profile_path | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable |
|---:|---|---|---|---|---|
| 010120 | atlas/symbol_profiles/010/010120.json | 2024-03-05 | true | clean_180D_window | true |
| 298040 | atlas/symbol_profiles/298/298040.json | 2024-03-04 | true | clean_180D_window | true |
| 006340 | atlas/symbol_profiles/006/006340.json | 2024-04-05 | true | clean_180D_window | true |
| 001440 | atlas/symbol_profiles/001/001440.json | 2024-04-05 | true | clean_180D_window_after_2024_04_02_candidate | true |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX

fine/deep split:
1. GRID_EQUIPMENT_DATACENTER_CAPEX_MARGIN_VISIBILITY
2. TRANSFORMER_BACKLOG_MARGIN_BRIDGE
3. WIRE_PROXY_PRICE_ONLY_LOCAL_BLOWOFF
4. WIRE_PROXY_CAPITAL_INTENSITY_OVERHANG
```

The compression insight is simple: the same grid theme is not the same evidence. Transformer/switchgear equipment names had order, backlog, customer, capacity, and margin bridges. Wire/copper proxies often had relative strength and theme heat first, then needed separate proof before Stage3 promotion.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry | entry_price | MFE90 | MAE90 | peak | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE_R1_72_LS_ELECTRIC_DATACENTER_GRID | 010120 | LS ELECTRIC | structural_success | Stage2-Actionable | 2024-03-05 | 77800 | 213.62 | -8.99 | 2024-05-29 / 244000 | current_profile_correct |
| CASE_R1_72_HYOSUNG_HEAVY_TRANSFORMER | 298040 | 효성중공업 | high_mae_success | Stage2-Actionable | 2024-03-04 | 222500 | 110.79 | -12.36 | 2024-05-28 / 469000 | current_profile_correct |
| CASE_R1_72_DAEWON_WIRE_PROXY_BLOWOFF | 006340 | 대원전선 | price_moved_without_evidence | Stage2-RelativeStrength-Proxy | 2024-04-05 | 2095 | 160.14 | -16.61 | 2024-05-13 / 5450 | current_profile_false_positive |
| CASE_R1_72_TAIHAN_WIRE_PROXY_CAPEX_DILUTION | 001440 | 대한전선 | failed_rerating | Stage2-RelativeStrength-Proxy | 2024-04-05 | 12790 | 63.8 | -8.21 | 2024-05-21 / 20950 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
```

The two positives both have equipment/backlog/margin evidence. The two counterexamples are not “bad stocks” by price path; they are bad Stage3 promotion examples when the only real bridge is wire-proxy relative strength.

## 9. Evidence Source Map

| Symbol | Stage2 evidence | Stage3 evidence | 4B evidence | Current-profile issue |
|---:|---|---|---|---|
| 010120 | equipment order, customer quality, relative strength, backlog route | revision and margin bridge | none at entry | current profile aligned |
| 298040 | transformer backlog, margin bridge, capacity route | financial visibility and repeat order conversion | later drawdown watch | current profile aligned |
| 006340 | relative strength and theme optionality | not supported | valuation blowoff, positioning overheat, price-only local peak | false positive if Stage3 allowed |
| 001440 | wire proxy and capacity narrative | not supported at entry | capital intensity/overhang and price-only local peak | false positive if Stage3 allowed |

## 10. Price Data Source Map

| Symbol | Price shard | Profile | Price basis | Adjustment |
|---:|---|---|---|---|
| 010120 | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json | tradable_raw | raw_unadjusted_marcap |
| 298040 | atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv | atlas/symbol_profiles/298/298040.json | tradable_raw | raw_unadjusted_marcap |
| 006340 | atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv | atlas/symbol_profiles/006/006340.json | tradable_raw | raw_unadjusted_marcap |
| 001440 | atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv | atlas/symbol_profiles/001/001440.json | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger_type | entry | entry_price | MFE90 | MAE90 | peak | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE_R1_72_LS_ELECTRIC_DATACENTER_GRID | 010120 | LS ELECTRIC | structural_success | Stage2-Actionable | 2024-03-05 | 77800 | 213.62 | -8.99 | 2024-05-29 / 244000 | current_profile_correct |
| CASE_R1_72_HYOSUNG_HEAVY_TRANSFORMER | 298040 | 효성중공업 | high_mae_success | Stage2-Actionable | 2024-03-04 | 222500 | 110.79 | -12.36 | 2024-05-28 / 469000 | current_profile_correct |
| CASE_R1_72_DAEWON_WIRE_PROXY_BLOWOFF | 006340 | 대원전선 | price_moved_without_evidence | Stage2-RelativeStrength-Proxy | 2024-04-05 | 2095 | 160.14 | -16.61 | 2024-05-13 / 5450 | current_profile_false_positive |
| CASE_R1_72_TAIHAN_WIRE_PROXY_CAPEX_DILUTION | 001440 | 대한전선 | failed_rerating | Stage2-RelativeStrength-Proxy | 2024-04-05 | 12790 | 63.8 | -8.21 | 2024-05-21 / 20950 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 010120 | 2024-03-05 | 77800 | 102.7 | -8.99 | 213.62 | -8.99 | 213.62 | -8.99 | 2024-05-29 | 244000 | -25.12 |
| 298040 | 2024-03-04 | 222500 | 56.85 | -12.36 | 110.79 | -12.36 | 110.79 | -12.36 | 2024-05-28 | 469000 | -35.07 |
| 006340 | 2024-04-05 | 2095 | 160.14 | -16.61 | 160.14 | -16.61 | 160.14 | -16.61 | 2024-05-13 | 5450 | -39.72 |
| 001440 | 2024-04-05 | 12790 | 63.8 | -8.21 | 63.8 | -8.21 | 63.8 | -8.21 | 2024-05-21 | 20950 | -32.94 |

Calculation basis:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
peak_price = max(high over observed representative window after entry_date)
drawdown_after_peak_pct = (min(low after peak_date) / peak_price - 1) * 100
```

## 13. Current Calibrated Profile Stress Test

| Symbol | P0 verdict | Actual path | Residual interpretation |
|---:|---|---|---|
| 010120 | current_profile_correct | strong MFE with controlled MAE after equipment bridge | Stage2/Yellow logic works |
| 298040 | current_profile_correct | high-MAE success with backlog/margin bridge | keep Stage2 actionable, do not loosen Green |
| 006340 | current_profile_false_positive | large MFE but price-only local blowoff and sharp drawdown | relative strength alone should route to 4B-watch |
| 001440 | current_profile_false_positive | large MFE then deep peak drawdown; capital intensity/proxy issue | require independent order/margin bridge |

Answers to the required stress questions:

```text
1. Current profile can separate positives if equipment/backlog/margin evidence is explicit.
2. It remains vulnerable if wire-proxy relative strength is treated like equipment visibility.
3. Stage2 bonus is not too high for equipment cases, but too generous for proxy-only cases.
4. Yellow threshold 75 is acceptable only after bridge-quality filtering.
5. Green threshold 87 / revision 55 should not be loosened for C02.
6. price_only_blowoff guard is appropriate and strengthened here.
7. full 4B non-price requirement remains appropriate; wire proxy overheat is watch-only unless non-price cap/overhang is present.
8. hard 4C was not the main issue in this loop.
```

## 14. Stage2 / Yellow / Green Comparison

The two equipment cases justify Stage2-actionable or Yellow before full Green. The two wire-proxy cases should not be promoted to Green from relative strength and theme heat. In this loop, Green lateness is not the residual error; false-positive promotion from proxy evidence is.

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is used as the representative aggregate trigger in this loop
```

## 15. 4B Local vs Full-window Timing Audit

| Symbol | 4B evidence type | local proximity | full-window proximity | verdict |
|---:|---|---:|---:|---|
| 006340 | price_only, valuation_blowoff, positioning_overheat | 0.94 | 0.94 | price_only_local_4B_too_early; watch-only unless non-price bridge exists |
| 001440 | price_only, valuation_blowoff, capital_raise_or_overhang | 0.94 | 0.94 | good full-window 4B watch; not positive promotion evidence |

The required split matters because a fast local peak in wire proxies can look like a “good trade” but still be poor calibration evidence for Stage3. It belongs to overlay/risk calibration, not positive Stage evidence.

## 16. 4C Protection Audit

No hard 4C routing is proposed in this loop. The dominant failure type is not thesis break after verified Stage3; it is over-promotion before the thesis is specific enough.

```text
four_c_protection_label = not_applicable
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
candidate = L1 power-grid positive promotion requires direct equipment/order/backlog/margin bridge
```

Rationale: in L1, grid CAPEX narratives spread through transformers, switchgear, cables, copper, construction, and holding-company proxies. The price tape can pull them together, but the evidence tape is not identical. Equipment names with customer/order/margin bridge had cleaner score-return alignment.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
new_axis_proposed = C02_wire_proxy_requires_equipment_or_order_margin_bridge_before_stage3_promotion
secondary_axis = C02_equipment_backlog_margin_bridge_promotes_stage2_actionable
```

Candidate logic:

```text
if canonical_archetype_id == C02 and only relative_strength + generic grid narrative exists:
    allow Stage2-watch
    block Stage3-Yellow/Green promotion
    route price-only blowoff to 4B-watch overlay

if canonical_archetype_id == C02 and transformer/switchgear/equipment order + customer quality + margin bridge exists:
    allow Stage2-actionable support
    allow Yellow if revision/visibility evidence also exists
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Existing global calibration catches broad Stage2/4B logic but can still over-score wire-proxy relative strength in C02. | none | 4 | 137.09 | -11.54 | 2/4 when wire proxies are allowed to behave like equipment backlog cases | mixed |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Pre-stock-web baseline would likely be slower on LS/Hyosung and still unable to distinguish wire proxy blowoff. | rollback_reference_only | 4 | 137.09 | -11.54 | 2/4 | weaker |
| P1_sector_specific_candidate_profile | sector_specific | L1 power-grid CAPEX should require direct equipment/order/backlog/margin bridge for positive promotion. | equipment_margin_bridge_required_before_stage3 | 4 | 162.21 | -10.68 | 0/2 among wire proxies selected for promotion | improved |
| P2_C02_canonical_archetype_candidate_profile | canonical_archetype_specific | C02 distinguishes transformer/switchgear equipment bridges from copper/wire proxy momentum. | wire_proxy_guard; equipment_order_margin_bridge_bonus | 4 | 162.21 | -10.68 | 0/2 promoted; wire proxies routed to 4B-watch | best_fit |
| P3_counterexample_guard_profile | guard_profile | When relative strength is the only bridge, route C02 wire/copper proxies to watch-only until customer/order/margin evidence appears. | relative_strength_only_demote_to_watch | 4 | 162.21 | -10.68 | 0/2 promoted | guardrail_passed |

## 20. Score-Return Alignment Matrix

| Symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | alignment |
|---:|---:|---|---:|---|---|
| 010120 | 82 | Stage3-Yellow | 84 | Stage3-Yellow | aligned |
| 298040 | 80 | Stage3-Yellow | 84 | Stage3-Yellow | aligned |
| 006340 | 76 | Stage3-Yellow_false_positive | 68 | Stage2-watch | false-positive reduced |
| 001440 | 78 | Stage3-Yellow_false_positive | 69 | Stage2-watch | false-positive reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | GRID_EQUIPMENT_DATACENTER_CAPEX_EQUIPMENT_VS_WIRE_PROXY_SPLIT | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 2 | true | true | wire-proxy false-positive guard improved; C02 equipment-vs-wire split still needs more non-Korea validation |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - wire_proxy_false_positive
  - price_only_local_blowoff
  - stage3_without_margin_bridge
new_axis_proposed:
  - C02_wire_proxy_requires_equipment_or_order_margin_bridge_before_stage3_promotion
  - C02_equipment_backlog_margin_bridge_promotes_stage2_actionable
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus_requires_customer_or_order_bridge_in_C02
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical trigger-level OHLC backtest only.
- Uses Songdaiki/stock-web tradable_raw OHLC.
- Uses representative trigger dedupe for aggregate.
- Uses research proxy score, not production score.
- No current/live recommendation.
- No stock_agent code patch.
```

Non-validation scope:

```text
- Does not validate present-day investment attractiveness.
- Does not assert production scoring changes.
- Does not use raw shard rows for weight calibration.
- Does not make global rule proposals.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_wire_proxy_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Wire/copper proxy relative strength without equipment-order/margin bridge should not promote to Stage3.","Reduces 2 wire-proxy false positives while keeping 2 equipment positives.","TRG_R1_72_006340_Stage2_RelativeStrength_Proxy|TRG_R1_72_001440_Stage2_RelativeStrength_Proxy",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C02_equipment_margin_bridge_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Transformer/switchgear equipment cases with order/backlog/customer/margin bridge deserve Stage2-actionable support.","Keeps LS ELECTRIC and Hyosung positives aligned with strong MFE/MAE path.","TRG_R1_72_010120_Stage2_Actionable|TRG_R1_72_298040_Stage2_Actionable",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "CASE_R1_72_LS_ELECTRIC_DATACENTER_GRID", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_EQUIPMENT_DATACENTER_CAPEX_MARGIN_VISIBILITY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "US data-center/grid CAPEX and equipment order/margin bridge visible before the 2024 run; entry uses 2024-03-05 close from stock-web."}
{"row_type": "case", "case_id": "CASE_R1_72_HYOSUNG_HEAVY_TRANSFORMER", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_BACKLOG_MARGIN_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Transformer backlog and margin bridge became visible before the late-May peak; entry uses 2024-03-04 close from stock-web."}
{"row_type": "case", "case_id": "CASE_R1_72_DAEWON_WIRE_PROXY_BLOWOFF", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "WIRE_PROXY_PRICE_ONLY_LOCAL_BLOWOFF", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-RelativeStrength-Proxy", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_without_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Wire proxy moved sharply with grid/copper narrative, but equipment backlog/customer/margin bridge was not sufficiently specific."}
{"row_type": "case", "case_id": "CASE_R1_72_TAIHAN_WIRE_PROXY_CAPEX_DILUTION", "symbol": "001440", "company_name": "대한전선", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "WIRE_PROXY_CAPITAL_INTENSITY_OVERHANG", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-RelativeStrength-Proxy", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_without_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Cable/wire exposure captured headline grid theme but did not carry the same transformer/equipment margin bridge."}
{"row_type": "trigger", "trigger_id": "TRG_R1_72_010120_Stage2_Actionable", "case_id": "CASE_R1_72_LS_ELECTRIC_DATACENTER_GRID", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_EQUIPMENT_DATACENTER_CAPEX_MARGIN_VISIBILITY", "sector": "industrials_power_grid", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 77800, "evidence_available_at_that_date": "US data-center/grid CAPEX and equipment order/margin bridge visible before the 2024 run; entry uses 2024-03-05 close from stock-web.", "evidence_source": "public disclosure/research proxy available by trigger date; stock-web OHLC validates price path only", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "profile_path": "atlas/symbol_profiles/010/010120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 102.7, "MFE_90D_pct": 213.62, "MFE_180D_pct": 213.62, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.99, "MAE_90D_pct": -8.99, "MAE_180D_pct": -8.99, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-29", "peak_price": 244000, "drawdown_after_peak_pct": -25.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1_72_010120_2024-03-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R1_72_298040_Stage2_Actionable", "case_id": "CASE_R1_72_HYOSUNG_HEAVY_TRANSFORMER", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_BACKLOG_MARGIN_BRIDGE", "sector": "industrials_power_grid", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-04", "entry_date": "2024-03-04", "entry_price": 222500, "evidence_available_at_that_date": "Transformer backlog and margin bridge became visible before the late-May peak; entry uses 2024-03-04 close from stock-web.", "evidence_source": "public disclosure/research proxy available by trigger date; stock-web OHLC validates price path only", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv", "profile_path": "atlas/symbol_profiles/298/298040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 56.85, "MFE_90D_pct": 110.79, "MFE_180D_pct": 110.79, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.36, "MAE_90D_pct": -12.36, "MAE_180D_pct": -12.36, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-28", "peak_price": 469000, "drawdown_after_peak_pct": -35.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1_72_298040_2024-03-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R1_72_006340_Stage2_RelativeStrength_Proxy", "case_id": "CASE_R1_72_DAEWON_WIRE_PROXY_BLOWOFF", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "WIRE_PROXY_PRICE_ONLY_LOCAL_BLOWOFF", "sector": "industrials_power_grid", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-RelativeStrength-Proxy", "trigger_date": "2024-04-05", "entry_date": "2024-04-05", "entry_price": 2095, "evidence_available_at_that_date": "Wire proxy moved sharply with grid/copper narrative, but equipment backlog/customer/margin bridge was not sufficiently specific.", "evidence_source": "relative-strength/news narrative proxy; stock-web OHLC validates price path only", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv", "profile_path": "atlas/symbol_profiles/006/006340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 160.14, "MFE_90D_pct": 160.14, "MFE_180D_pct": 160.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.61, "MAE_90D_pct": -16.61, "MAE_180D_pct": -16.61, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-13", "peak_price": 5450, "drawdown_after_peak_pct": -39.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1_72_006340_2024-04-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R1_72_006340_4B_WATCH", "case_id": "CASE_R1_72_DAEWON_WIRE_PROXY_BLOWOFF", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "WIRE_PROXY_PRICE_ONLY_LOCAL_BLOWOFF", "sector": "industrials_power_grid", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-04-05", "entry_date": "2024-04-05", "entry_price": 2095, "evidence_available_at_that_date": "Wire proxy moved sharply with grid/copper narrative, but equipment backlog/customer/margin bridge was not sufficiently specific.", "evidence_source": "relative-strength/news narrative proxy; stock-web OHLC validates price path only", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv", "profile_path": "atlas/symbol_profiles/006/006340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 160.14, "MFE_90D_pct": 160.14, "MFE_180D_pct": 160.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.61, "MAE_90D_pct": -16.61, "MAE_180D_pct": -16.61, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-13", "peak_price": 5450, "drawdown_after_peak_pct": -39.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1_72_006340_2024-04-05", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R1_72_001440_Stage2_RelativeStrength_Proxy", "case_id": "CASE_R1_72_TAIHAN_WIRE_PROXY_CAPEX_DILUTION", "symbol": "001440", "company_name": "대한전선", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "WIRE_PROXY_CAPITAL_INTENSITY_OVERHANG", "sector": "industrials_power_grid", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-RelativeStrength-Proxy", "trigger_date": "2024-04-05", "entry_date": "2024-04-05", "entry_price": 12790, "evidence_available_at_that_date": "Cable/wire exposure captured headline grid theme but did not carry the same transformer/equipment margin bridge.", "evidence_source": "relative-strength/news narrative proxy; stock-web OHLC validates price path only", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "capital_raise_or_overhang", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv", "profile_path": "atlas/symbol_profiles/001/001440.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 63.8, "MFE_90D_pct": 63.8, "MFE_180D_pct": 63.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.21, "MAE_90D_pct": -8.21, "MAE_180D_pct": -8.21, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 20950, "drawdown_after_peak_pct": -32.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_watch_only", "four_b_evidence_type": ["valuation_blowoff", "capital_raise_or_overhang", "price_only_local_peak"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1_72_001440_2024-04-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R1_72_001440_4B_WATCH", "case_id": "CASE_R1_72_TAIHAN_WIRE_PROXY_CAPEX_DILUTION", "symbol": "001440", "company_name": "대한전선", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "WIRE_PROXY_CAPITAL_INTENSITY_OVERHANG", "sector": "industrials_power_grid", "primary_archetype": "power_grid_datacenter_capex", "loop_objective": "residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-04-05", "entry_date": "2024-04-05", "entry_price": 12790, "evidence_available_at_that_date": "Cable/wire exposure captured headline grid theme but did not carry the same transformer/equipment margin bridge.", "evidence_source": "relative-strength/news narrative proxy; stock-web OHLC validates price path only", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "capital_raise_or_overhang", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv", "profile_path": "atlas/symbol_profiles/001/001440.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 63.8, "MFE_90D_pct": 63.8, "MFE_180D_pct": 63.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.21, "MAE_90D_pct": -8.21, "MAE_180D_pct": -8.21, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 20950, "drawdown_after_peak_pct": -32.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_watch_only", "four_b_evidence_type": ["valuation_blowoff", "capital_raise_or_overhang", "price_only_local_peak"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R1_72_001440_2024-04-05", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "CASE_R1_72_LS_ELECTRIC_DATACENTER_GRID", "trigger_id": "TRG_R1_72_010120_Stage2_Actionable", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 13, "relative_strength_score": 13, "customer_quality_score": 13, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 9, "fcf_conversion_score": 5, "positioning_overheat_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 13, "relative_strength_score": 13, "customer_quality_score": 13, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 9, "fcf_conversion_score": 5, "positioning_overheat_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "customer_quality_score", "positioning_overheat_score", "dilution_cb_risk_score"], "component_delta_explanation": "C02 shadow profile rewards equipment/customer/backlog/margin bridge and demotes wire-proxy relative strength without independent order or margin bridge.", "MFE_90D_pct": 213.62, "MAE_90D_pct": -8.99, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C02_grid_equipment_wire_proxy_shadow_profile", "case_id": "CASE_R1_72_LS_ELECTRIC_DATACENTER_GRID", "trigger_id": "TRG_R1_72_010120_Stage2_Actionable", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 13, "relative_strength_score": 13, "customer_quality_score": 13, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 9, "fcf_conversion_score": 5, "positioning_overheat_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 16, "margin_bridge_score": 17, "revision_score": 13, "relative_strength_score": 13, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 9, "fcf_conversion_score": 5, "positioning_overheat_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "customer_quality_score", "positioning_overheat_score", "dilution_cb_risk_score"], "component_delta_explanation": "C02 shadow profile rewards equipment/customer/backlog/margin bridge and demotes wire-proxy relative strength without independent order or margin bridge.", "MFE_90D_pct": 213.62, "MAE_90D_pct": -8.99, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "CASE_R1_72_HYOSUNG_HEAVY_TRANSFORMER", "trigger_id": "TRG_R1_72_298040_Stage2_Actionable", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 14, "revision_score": 13, "relative_strength_score": 13, "customer_quality_score": 13, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 9, "fcf_conversion_score": 5, "positioning_overheat_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 14, "revision_score": 13, "relative_strength_score": 13, "customer_quality_score": 13, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 9, "fcf_conversion_score": 5, "positioning_overheat_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "customer_quality_score", "positioning_overheat_score", "dilution_cb_risk_score"], "component_delta_explanation": "C02 shadow profile rewards equipment/customer/backlog/margin bridge and demotes wire-proxy relative strength without independent order or margin bridge.", "MFE_90D_pct": 110.79, "MAE_90D_pct": -12.36, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C02_grid_equipment_wire_proxy_shadow_profile", "case_id": "CASE_R1_72_HYOSUNG_HEAVY_TRANSFORMER", "trigger_id": "TRG_R1_72_298040_Stage2_Actionable", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 15, "margin_bridge_score": 14, "revision_score": 13, "relative_strength_score": 13, "customer_quality_score": 13, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 9, "fcf_conversion_score": 5, "positioning_overheat_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 16, "revision_score": 13, "relative_strength_score": 13, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 9, "fcf_conversion_score": 5, "positioning_overheat_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "customer_quality_score", "positioning_overheat_score", "dilution_cb_risk_score"], "component_delta_explanation": "C02 shadow profile rewards equipment/customer/backlog/margin bridge and demotes wire-proxy relative strength without independent order or margin bridge.", "MFE_90D_pct": 110.79, "MAE_90D_pct": -12.36, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "CASE_R1_72_DAEWON_WIRE_PROXY_BLOWOFF", "trigger_id": "TRG_R1_72_006340_Stage2_RelativeStrength_Proxy", "symbol": "006340", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -2, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": -10}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow_false_positive", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -2, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": -10}, "weighted_score_after": 68, "stage_label_after": "Stage2-watch", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "customer_quality_score", "positioning_overheat_score", "dilution_cb_risk_score"], "component_delta_explanation": "C02 shadow profile rewards equipment/customer/backlog/margin bridge and demotes wire-proxy relative strength without independent order or margin bridge.", "MFE_90D_pct": 160.14, "MAE_90D_pct": -16.61, "score_return_alignment_label": "false_positive_avoided_after_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C02_grid_equipment_wire_proxy_shadow_profile", "case_id": "CASE_R1_72_DAEWON_WIRE_PROXY_BLOWOFF", "trigger_id": "TRG_R1_72_006340_Stage2_RelativeStrength_Proxy", "symbol": "006340", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -2, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": -10}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow_false_positive", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 14, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -2, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": -12}, "weighted_score_after": 68, "stage_label_after": "Stage2-watch", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "customer_quality_score", "positioning_overheat_score", "dilution_cb_risk_score"], "component_delta_explanation": "C02 shadow profile rewards equipment/customer/backlog/margin bridge and demotes wire-proxy relative strength without independent order or margin bridge.", "MFE_90D_pct": 160.14, "MAE_90D_pct": -16.61, "score_return_alignment_label": "false_positive_avoided_after_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "CASE_R1_72_TAIHAN_WIRE_PROXY_CAPEX_DILUTION", "trigger_id": "TRG_R1_72_001440_Stage2_RelativeStrength_Proxy", "symbol": "001440", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -8, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": -10}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow_false_positive", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -8, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": -10}, "weighted_score_after": 69, "stage_label_after": "Stage2-watch", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "customer_quality_score", "positioning_overheat_score", "dilution_cb_risk_score"], "component_delta_explanation": "C02 shadow profile rewards equipment/customer/backlog/margin bridge and demotes wire-proxy relative strength without independent order or margin bridge.", "MFE_90D_pct": 63.8, "MAE_90D_pct": -8.21, "score_return_alignment_label": "false_positive_avoided_after_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C02_grid_equipment_wire_proxy_shadow_profile", "case_id": "CASE_R1_72_TAIHAN_WIRE_PROXY_CAPEX_DILUTION", "trigger_id": "TRG_R1_72_001440_Stage2_RelativeStrength_Proxy", "symbol": "001440", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -8, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": -10}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow_false_positive", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 14, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -10, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": -12}, "weighted_score_after": 69, "stage_label_after": "Stage2-watch", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "customer_quality_score", "positioning_overheat_score", "dilution_cb_risk_score"], "component_delta_explanation": "C02 shadow profile rewards equipment/customer/backlog/margin bridge and demotes wire-proxy relative strength without independent order or margin bridge.", "MFE_90D_pct": 63.8, "MAE_90D_pct": -8.21, "score_return_alignment_label": "false_positive_avoided_after_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R1", "loop": "72", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["wire_proxy_false_positive", "price_only_local_blowoff", "stage3_without_margin_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 72
next_round = R2
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files directly consulted for this standalone research:

```text
atlas/manifest.json
atlas/symbol_profiles/010/010120.json
atlas/symbol_profiles/298/298040.json
atlas/symbol_profiles/006/006340.json
atlas/symbol_profiles/001/001440.json
atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv
atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv
```

All price calculations are based on raw, unadjusted, calibration-safe tradable OHLC rows from Songdaiki/stock-web. Corporate-action candidate windows are blocked by default; the representative windows here are treated as clean 180D windows under that rule.

