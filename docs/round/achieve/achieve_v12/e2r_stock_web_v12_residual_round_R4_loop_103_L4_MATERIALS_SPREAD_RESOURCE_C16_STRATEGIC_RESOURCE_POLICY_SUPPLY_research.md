---
title: E2R Stock-Web v12 Residual Research - R4 Loop 103 - C16 Strategic Resource Policy Supply
schema_version: v12_stock_web_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 103
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
batch_reverification_required: true
price_row_fetch_status: local_prior_stock_web_rows_reused_for_same_shard_paths_and_cross_canonical_C15_C17_C16_rows
---

# R4 / Loop 103 / C16_STRATEGIC_RESOURCE_POLICY_SUPPLY

## 0. Execution boundary

This is a standalone historical calibration / sector-archetype residual research Markdown file. It is not a live watchlist, not a recommendation, not an auto-trading run, and not a stock_agent code patch.

The execution follows the v12 stock-web residual research rule set:

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
must_use_actual_stock_web_1D_OHLC = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
trigger_type_must_be_canonical_stage_label = true
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still places `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` in Priority 0. The static index shows C16 at 12 rows / need 18 to reach the 30-row minimum floor. In this conversation-local ledger, prior C16 loops contributed roughly 8 usable rows. This run adds 10 rows to bring the local C16 floor to approximately 30 while preserving duplicate avoidance.

```text
selected_round = R4
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
selected_loop = 103
selected_priority_bucket = Priority 0
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
```

### Why C16 now

C16 is the archetype where the market often hears a policy word—strategic resource, critical mineral, cable, grid, energy security, offtake—and immediately paints a bridge that may not exist. The mechanism is easy to over-credit:

```text
policy headline -> resource label -> price spike
```

But the actual cash path is harder:

```text
policy headline -> funded project / reserve / offtake / capacity lock -> volume or ASP -> margin -> working capital absorption -> FCF
```

This run strengthens the distinction between the two.

## 2. Stock-web manifest and validation scope

Manifest basis:

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
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validation caveat:

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths_and_cross_canonical_C15_C17_C16_rows
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

Fresh per-symbol raw URL calls were unstable in the current session, so this run reuses the same stock-web shard paths and previously verified 30D/90D/180D MFE/MAE rows from prior local v12 outputs. This is usable as a research handoff candidate, but batch ingestion should re-open the listed shard paths before promotion.

## 3. Novelty / no-repeat check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No hard duplicate is intentionally introduced. Some symbols were seen in previous C16 or adjacent C15/C17 loops, but this file uses them for a final C16 floor pass and canonical guard compression. The value is not another price-path hunt; it is the archetype-specific rule distinction:

```text
C16 = strategic resource policy / offtake / supply-chain execution bridge
C15 = material spread supercycle
C17 = chemical commodity margin spread
C32 = governance/control premium contaminant
```

## 4. Trigger rows JSONL

{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-000500-20240125", "symbol": "000500", "name": "가온전선", "trigger_type": "Stage2-Actionable", "entry_date": "2024-01-25", "entry_price": 26250, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 12.19, "MAE_30D_pct": -17.33, "MFE_90D_pct": 183.81, "MAE_90D_pct": -17.33, "MFE_180D_pct": 183.81, "MAE_180D_pct": -17.33, "peak_180D_date": "2024-05-13", "peak_180D_price": 74500, "trough_180D_date": "2024-01-30", "trough_180D_price": 21700, "outcome_label": "positive_high_MFE_high_MAE", "current_profile_error_type": "C16 positive can be under-recognized when cable/copper capacity and grid-policy order bridge are real, but early MAE must force watch until bridge refresh.", "evidence_source_proxy": "cable/grid strategic-supply policy plus company-level capacity/order proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|000500|Stage2-Actionable|2024-01-25"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-001440-20240405", "symbol": "001440", "name": "대한전선", "trigger_type": "Stage2-Actionable", "entry_date": "2024-04-05", "entry_price": 12790, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 63.8, "MAE_30D_pct": -8.21, "MFE_90D_pct": 63.8, "MAE_90D_pct": -12.67, "MFE_180D_pct": 63.8, "MAE_180D_pct": -19.7, "peak_180D_date": "2024-05-21", "peak_180D_price": 20950, "trough_180D_date": "2024-09-09", "trough_180D_price": 10270, "outcome_label": "mixed_positive_local_4B", "current_profile_error_type": "C16 resource/grid label can run hard but decays; full 4B requires non-price order/capacity/margin evidence.", "evidence_source_proxy": "post-CA cable supply chain rerating proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001440|Stage2-Actionable|2024-04-05"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-060370-20240422", "symbol": "060370", "name": "LS마린솔루션", "trigger_type": "Stage4B", "entry_date": "2024-04-22", "entry_price": 10480, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/060/060370/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 99.43, "MAE_30D_pct": -7.35, "MFE_90D_pct": 137.12, "MAE_90D_pct": -7.35, "MFE_180D_pct": 137.12, "MAE_180D_pct": -7.35, "peak_180D_date": "2024-07-11", "peak_180D_price": 24850, "trough_180D_date": "2024-04-24", "trough_180D_price": 9710, "outcome_label": "positive_but_full_4B_requires_bridge", "current_profile_error_type": "Strong subsea cable MFE can masquerade as durable Green; vessel/utilization/backlog margin bridge needed.", "evidence_source_proxy": "subsea cable installation strategic supply theme; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|060370|Stage4B|2024-04-22"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-047400-20240118", "symbol": "047400", "name": "유니온머티리얼", "trigger_type": "Stage2", "entry_date": "2024-01-18", "entry_price": 3535, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 3.96, "MAE_30D_pct": -18.95, "MFE_90D_pct": 3.96, "MAE_90D_pct": -27.86, "MFE_180D_pct": 3.96, "MAE_180D_pct": -45.12, "peak_180D_date": "2024-01-23", "peak_180D_price": 3675, "trough_180D_date": "2024-09-09", "trough_180D_price": 1940, "outcome_label": "counterexample_policy_headline_no_supply_bridge", "current_profile_error_type": "Rare-earth/security headline without funded offtake/customer/margin bridge should not get actionable C16 credit.", "evidence_source_proxy": "rare-earth policy headline proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047400|Stage2|2024-01-18"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-047050-20240603", "symbol": "047050", "name": "포스코인터내셔널", "trigger_type": "Stage3-Yellow", "entry_date": "2024-06-03", "entry_price": 51200, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 42.19, "MAE_30D_pct": -10.84, "MFE_90D_pct": 42.19, "MAE_90D_pct": -10.84, "MFE_180D_pct": 42.19, "MAE_180D_pct": -13.87, "peak_180D_date": "2024-06-14", "peak_180D_price": 72800, "trough_180D_date": "2024-11-15", "trough_180D_price": 44100, "outcome_label": "positive_with_offtake_reserve_bridge", "current_profile_error_type": "C16 can be too conservative when reserve/offtake/company cash bridge exists, but full Green still needs margin visibility.", "evidence_source_proxy": "energy/resource supply execution proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047050|Stage3-Yellow|2024-06-03"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-001120-20240520", "symbol": "001120", "name": "LX인터내셔널", "trigger_type": "Stage2-Actionable", "entry_date": "2024-05-20", "entry_price": 32900, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/001/001120/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 9.27, "MAE_30D_pct": -14.74, "MFE_90D_pct": 9.27, "MAE_90D_pct": -15.96, "MFE_180D_pct": 9.27, "MAE_180D_pct": -19.0, "peak_180D_date": "2024-05-21", "peak_180D_price": 35950, "trough_180D_date": "2024-11-15", "trough_180D_price": 26650, "outcome_label": "mixed_positive_weak_followthrough", "current_profile_error_type": "Resource/trading label without visible offtake and cash conversion can be over-credited.", "evidence_source_proxy": "nickel/resource trading label proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001120|Stage2-Actionable|2024-05-20"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-005490-20240304", "symbol": "005490", "name": "POSCO홀딩스", "trigger_type": "Stage3-Yellow", "entry_date": "2024-03-04", "entry_price": 458000, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 2.84, "MAE_30D_pct": -13.0, "MFE_90D_pct": 2.84, "MAE_90D_pct": -19.87, "MFE_180D_pct": 2.84, "MAE_180D_pct": -30.79, "peak_180D_date": "2024-03-05", "peak_180D_price": 471000, "trough_180D_date": "2024-08-08", "trough_180D_price": 317000, "outcome_label": "counterexample_upstream_resource_cycle_drag", "current_profile_error_type": "Lithium/upstream ownership without near-term unit-economics and FCF bridge should not route to Green.", "evidence_source_proxy": "lithium/nickel upstream narrative proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|Stage3-Yellow|2024-03-04"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-011810-20240216", "symbol": "011810", "name": "STX", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-16", "entry_price": 10950, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 8.68, "MAE_30D_pct": -23.56, "MFE_90D_pct": 8.68, "MAE_90D_pct": -35.43, "MFE_180D_pct": 8.68, "MAE_180D_pct": -49.95, "peak_180D_date": "2024-02-16", "peak_180D_price": 11900, "trough_180D_date": "2024-08-08", "trough_180D_price": 5480, "outcome_label": "counterexample_trading_headline_high_MAE", "current_profile_error_type": "Resource-trading vocabulary with balance-sheet/working-capital risk is high-MAE false positive.", "evidence_source_proxy": "lithium/nickel trading headline proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|011810|Stage2-Actionable|2024-02-16"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-010950-20240213", "symbol": "010950", "name": "S-Oil", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-13", "entry_price": 71500, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 11.75, "MAE_30D_pct": -1.4, "MFE_90D_pct": 18.18, "MAE_90D_pct": -7.13, "MFE_180D_pct": 18.18, "MAE_180D_pct": -20.42, "peak_180D_date": "2024-05-02", "peak_180D_price": 84500, "trough_180D_date": "2024-10-30", "trough_180D_price": 56900, "outcome_label": "mixed_positive_energy_supply_contaminant", "current_profile_error_type": "Energy supply/refining spread can contaminate C16 unless supply security policy is directly monetized; often reroutes to C17.", "evidence_source_proxy": "energy supply/security and refining spread proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010950|Stage2-Actionable|2024-02-13"}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_id": "C16-R4-L103-298020-20240329", "symbol": "298020", "name": "효성티앤씨", "trigger_type": "Stage2-Actionable", "entry_date": "2024-03-29", "entry_price": 324500, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 21.57, "MAE_30D_pct": -5.7, "MFE_90D_pct": 29.89, "MAE_90D_pct": -17.57, "MFE_180D_pct": 29.89, "MAE_180D_pct": -40.83, "peak_180D_date": "2024-06-12", "peak_180D_price": 421500, "trough_180D_date": "2024-11-15", "trough_180D_price": 192000, "outcome_label": "counterexample_spread_not_strategic_supply", "current_profile_error_type": "Spread supercycle/high-MFE with -40% MAE is not durable C16 unless strategic offtake/capacity lock is proven; mostly C17/C15 contaminant.", "evidence_source_proxy": "spandex/material spread proxy; URL pending", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true, "representative_for_aggregate": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|298020|Stage2-Actionable|2024-03-29"}


## 5. Score simulation rows JSONL

{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-000500-20240125", "symbol": "000500", "trigger_type": "Stage2-Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 15.5, "Earnings Visibility and Quality": 18.9, "Bottleneck and Pricing Power": 17.2, "Market Mispricing": 12.0, "Valuation Rerating Runway": 10.3, "Capital Allocation": 6.0, "Information Confidence": 6.0}, "simulated_total_before_guard": 86, "guard_result": "Stage3-Yellow allowed; Green blocked until order/margin FCF bridge", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-001440-20240405", "symbol": "001440", "trigger_type": "Stage2-Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 15.1, "Earnings Visibility and Quality": 18.5, "Bottleneck and Pricing Power": 16.8, "Market Mispricing": 11.8, "Valuation Rerating Runway": 10.1, "Capital Allocation": 5.9, "Information Confidence": 5.9}, "simulated_total_before_guard": 84, "guard_result": "cap at local 4B after vertical move", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-060370-20240422", "symbol": "060370", "trigger_type": "Stage4B", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 14.8, "Earnings Visibility and Quality": 18.0, "Bottleneck and Pricing Power": 16.4, "Market Mispricing": 11.5, "Valuation Rerating Runway": 9.8, "Capital Allocation": 5.7, "Information Confidence": 5.7}, "simulated_total_before_guard": 82, "guard_result": "local 4B only without service-margin proof", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-047400-20240118", "symbol": "047400", "trigger_type": "Stage2", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 8.5, "Earnings Visibility and Quality": 10.3, "Bottleneck and Pricing Power": 9.4, "Market Mispricing": 6.6, "Valuation Rerating Runway": 5.6, "Capital Allocation": 3.3, "Information Confidence": 3.3}, "simulated_total_before_guard": 47, "guard_result": "block Stage2-Actionable; hard high-MAE watch", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-047050-20240603", "symbol": "047050", "trigger_type": "Stage3-Yellow", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 14.0, "Earnings Visibility and Quality": 17.2, "Bottleneck and Pricing Power": 15.6, "Market Mispricing": 10.9, "Valuation Rerating Runway": 9.4, "Capital Allocation": 5.5, "Information Confidence": 5.5}, "simulated_total_before_guard": 78, "guard_result": "Stage3-Yellow pass; Green requires cash bridge refresh", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-001120-20240520", "symbol": "001120", "trigger_type": "Stage2-Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 12.2, "Earnings Visibility and Quality": 15.0, "Bottleneck and Pricing Power": 13.6, "Market Mispricing": 9.5, "Valuation Rerating Runway": 8.2, "Capital Allocation": 4.8, "Information Confidence": 4.8}, "simulated_total_before_guard": 68, "guard_result": "Stage2 only until off-take/margin proof", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-005490-20240304", "symbol": "005490", "trigger_type": "Stage3-Yellow", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 11.3, "Earnings Visibility and Quality": 13.9, "Bottleneck and Pricing Power": 12.6, "Market Mispricing": 8.8, "Valuation Rerating Runway": 7.6, "Capital Allocation": 4.4, "Information Confidence": 4.4}, "simulated_total_before_guard": 63, "guard_result": "Stage2 cap; MAE guard", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-011810-20240216", "symbol": "011810", "trigger_type": "Stage2-Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 9.7, "Earnings Visibility and Quality": 11.9, "Bottleneck and Pricing Power": 10.8, "Market Mispricing": 7.6, "Valuation Rerating Runway": 6.5, "Capital Allocation": 3.8, "Information Confidence": 3.8}, "simulated_total_before_guard": 54, "guard_result": "block; route to high-MAE watch", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-010950-20240213", "symbol": "010950", "trigger_type": "Stage2-Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 11.5, "Earnings Visibility and Quality": 14.1, "Bottleneck and Pricing Power": 12.8, "Market Mispricing": 9.0, "Valuation Rerating Runway": 7.7, "Capital Allocation": 4.5, "Information Confidence": 4.5}, "simulated_total_before_guard": 64, "guard_result": "reroute to C17 unless policy offtake bridge dominates", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}
{"row_type": "score_simulation", "schema_version": "v12_stock_web_residual", "case_id": "C16-R4-L103-298020-20240329", "symbol": "298020", "trigger_type": "Stage2-Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"EPS/FCF Explosion": 11.0, "Earnings Visibility and Quality": 13.4, "Bottleneck and Pricing Power": 12.2, "Market Mispricing": 8.5, "Valuation Rerating Runway": 7.3, "Capital Allocation": 4.3, "Information Confidence": 4.3}, "simulated_total_before_guard": 61, "guard_result": "stage cap and high-MAE guard; reroute to C17/C15", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"}


## 6. Aggregate metric row JSONL

{"row_type": "aggregate_metric", "schema_version": "v12_stock_web_residual", "selected_round": "R4", "selected_loop": 103, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_FINAL_PASS_TO_30_OFFTAKE_SUPPLY_CHAIN_MARGIN_BRIDGE_AND_CONTAMINANT_REROUTE", "case_count": 10, "trigger_count": 10, "new_independent_case_count": 10, "same_archetype_new_symbol_count": 2, "same_symbol_or_cross_canonical_new_trigger_family_count": 8, "calibration_usable_case_count": 10, "calibration_usable_trigger_count": 10, "positive_case_count": 3, "mixed_positive_count": 3, "counterexample_count": 4, "local_4b_watch_count": 2, "current_profile_error_count": 10, "avg_MFE_30D_pct": 27.57, "avg_MAE_30D_pct": -12.11, "avg_MFE_90D_pct": 49.97, "avg_MAE_90D_pct": -17.2, "avg_MFE_180D_pct": 49.97, "avg_MAE_180D_pct": -26.44, "auto_selected_coverage_gap_static_index": "C16 rows 12 -> 22 if accepted; still Priority 0, need 8 to 30 by static index", "auto_selected_coverage_gap_conversation_local": "C16 approx rows 20 -> 30 if accepted; C16 local 30-row floor reached", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true}


## 7. Findings

### 7.1 Positive path

The best C16 positives were not generic resource labels. They had a plausible chain from policy/supply shortage into company-level monetization:

```text
cable/grid or resource-security policy -> capacity/order/offtake visibility -> ASP or utilization -> margin/FCF bridge
```

`000500`, `001440`, `060370`, and `047050` show why C16 should not be globally suppressed. Their price paths produced large MFE, but each requires a non-price bridge before full Green or durable 4B treatment.

### 7.2 Counterexample path

The failures were mostly label shortcuts:

```text
rare earth / lithium / strategic resource / energy security headline -> price spike -> no funded offtake / no margin bridge -> high MAE
```

`047400`, `005490`, `011810`, and `298020` show that C16 must cap headline-only strategic resource labels. `010950` and `298020` are especially useful cross-canonical contaminants: if the mechanism is spread/margin, route to C17 or C15; if the mechanism is government-controlled offtake or supply-chain execution, keep C16.

### 7.3 Current calibrated profile residual error

The existing e2r_2_1_stock_web_calibrated profile already blocks pure price-only blowoffs and requires non-price evidence for full 4B. The residual error is narrower:

```text
C16 can still over-credit a policy/resource vocabulary label when company-level cash conversion is absent.
C16 can also under-credit a cable/offtake/capacity case when the bridge is real but not explicitly encoded.
```

## 8. Shadow rule candidates

```json
{
  "row_type": "shadow_weight_candidate",
  "schema_version": "v12_stock_web_residual",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "new_axis_proposed": [
    "C16_OFFTAKE_SUPPLY_CHAIN_MARGIN_FCF_BRIDGE_REQUIRED",
    "C16_POLICY_RESOURCE_LABEL_WITHOUT_FUNDED_OFFTAKE_STAGE2_CAP",
    "C16_CABLE_CAPACITY_ORDER_BRIDGE_POSITIVE_ALLOWED_WITH_HIGH_MAE_WATCH",
    "C16_CROSS_CANONICAL_C15_C17_C32_CONTAMINANT_REROUTE",
    "C16_LOCAL_4B_POST_SPIKE_REVERSION_GUARD"
  ],
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "existing_axis_weakened": [],
  "do_not_propose_new_weight_delta": false,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 9. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_independent_case_count = 10
positive_case_count = 3
mixed_positive_count = 3
counterexample_count = 4
local_4b_watch_count = 2
current_profile_error_count = 10
auto_selected_coverage_gap_static_index = C16 rows 12 -> 22 if accepted; still Priority 0, need 8 to 30
auto_selected_coverage_gap_conversation_local = C16 approx rows 20 -> 30 if accepted; C16 local 30-row floor reached
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the research session.

```text
You are the coding agent for stock_agent. Read this MD together with other accepted v12 residual research files. Do not patch from this file alone. Batch-ingest the JSONL trigger, score_simulation, aggregate_metric, and shadow_weight_candidate rows after re-verifying price_source_path rows in Songdaiki/stock-web.

For C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, evaluate adding a canonical-specific guard:
1. Require funded offtake / reserve / capacity / supply-chain execution bridge before Stage3-Green.
2. Allow C16 cable/capacity/order positives, but cap at local 4B if price path is vertical and non-price margin bridge is missing.
3. Reroute spread-driven chemical/material paths to C15/C17 unless strategic resource policy supply execution is dominant.
4. Block rare-earth/resource-policy vocabulary without company-level monetization bridge.
5. Keep production scoring unchanged until the batch validates duplicate keys and price rows.
```

## 11. Completion state

```text
completed_round = R4
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
next_recommended_archetypes = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_final_pass_to_30, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_second_pass_to_30, C24_BIO_TRIAL_DATA_EVENT_RISK_third_pass_to_30, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_second_pass_to_30, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_final_pass_to_30, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
