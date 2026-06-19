# E2R Historical Calibration v12 — R4/L4 C15 material spread pass-through phase guard

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 90
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 C15 spread reversal / inventory-cycle balance repair + Priority 0 direct URL/proxy/MFE-MAE repair
round_schedule_status: coverage_index_selected; local C15 max loop 89 -> selected loop 90; 직전 C13 반복 회피
round_sector_consistency: pass
price_source: Songdaiki/stock-web / atlas/ohlcv_tradable_by_symbol_year
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
live_candidate_mode: false
```

This loop adds **8 new independent cases**, **4 counterexamples**, and **6 current-profile residual errors** for `R4/L4/C15_MATERIAL_SPREAD_SUPERCYCLE`.

## 1. Scope and selection

The No-Repeat Index now says all C01~C32 archetypes are above the old 30/50/80 row thresholds, so this is no longer row-filling. The target is quality repair: direct URL/proxy/MFE-MAE repair plus Priority-1 balance work. C15 remains on the Priority-1 list for spread reversal and inventory-cycle counterexamples.

I selected C15 because the previous visible loop was C13, while recent C15 work has clustered around individual material themes. This loop intentionally mixes **steel pipe / paper-pulp / cement** rows to test whether the same canonical rule can compress pass-through, inventory lag, demand volume, and price-phase behavior across materials.

## 2. Stock-Web manifest/schema audit

- `source_name`: FinanceData/marcap
- `price_adjustment_status`: raw_unadjusted_marcap
- `calibration_shard_root`: `atlas/ohlcv_tradable_by_symbol_year`
- `tradable_row_count`: 14,354,401
- `raw_row_count`: 15,214,118
- `symbol_count`: 5,414
- `max_date`: 2026-02-20
- tradable columns: `d,o,h,l,c,v,a,mc,s,m`
- MFE/MAE basis: entry 이후 N개 tradable row의 max high / min low

## 3. Evidence source table

| symbol | source evidence | source URL | source_proxy_only |
|---:|---|---|---|
| 005010 | Hyusteel API steel-pipe US plant / tariff-quota differential / energy-use pipe price uplift | https://www.asiae.co.kr/en/article/2025030409200957191 | false |
| 306200 | 52-week low / weak steel-pipe market / US inventory issue / provision reversal | https://www.asiae.co.kr/en/article/2024082210235349849 | false |
| 092790 | East Sea oil/gas drilling casing demand theme; commercial production far later | https://www.mk.co.kr/en/stock/11034888 | true |
| 071090 | Same East Sea casing/cement work theme; poor conversion path | https://www.mk.co.kr/en/stock/11034888 | true |
| 038500 | Drilling cement-work theme with cement names rallying | https://www.mk.co.kr/en/stock/11034888 | true |
| 213500 | Hansol Paper export/specialty-paper rebound, but pulp and freight cost pressure | https://www.asiae.co.kr/en/article/2024071116573335226 | false |
| 009580 | Paper-sector pulp/freight setup used as proxy; issuer conversion not direct | https://www.asiae.co.kr/en/article/2024071116573335226 | true |
| 300720 | Cement prior strong result plus coal-cost relief, but housing permits and SCR capex burden | https://www.asiae.co.kr/en/article/2024032108180183866 | false |


## 4. Trigger-level backtest summary

| case | symbol | trigger | type | entry | MFE90/MAE90 | MFE180/MAE180 | outcome |
|---|---:|---|---|---|---:|---:|---|
| C15-L90-01 | 005010 Husteel | 2025-03-04 | Stage2-Actionable | 2025-03-04 @ 4,820 | 46.27% / -7.05% | 46.27% / -21.58% | positive_structural_success_or_guardrail_positive |
| C15-L90-02 | 306200 SeAH Steel | 2024-08-22 | 4B | 2024-08-22 @ 117,800 | 5.94% / -8.23% | 84.63% / -8.23% | positive_structural_success_or_guardrail_positive |
| C15-L90-03 | 092790 Nexteel | 2024-06-06 | Stage2 | 2024-06-07 @ 10,230 | 20.82% / -29.52% | 75.86% / -29.72% | positive_structural_success_or_guardrail_positive |
| C15-L90-04 | 071090 Histeel | 2024-06-06 | 4B | 2024-06-07 @ 4,660 | 2.68% / -38.20% | 2.68% / -46.35% | counterexample_or_failed_rerating |
| C15-L90-05 | 038500 Sampyo Cement | 2024-06-06 | Stage2 | 2024-06-07 @ 3,500 | 15.29% / -17.29% | 15.29% / -19.57% | counterexample_or_failed_rerating |
| C15-L90-06 | 213500 Hansol Paper | 2024-07-12 | Stage3-Yellow | 2024-07-12 @ 10,640 | 0.28% / -17.20% | 0.28% / -27.44% | counterexample_or_failed_rerating |
| C15-L90-07 | 009580 Moorim P&P | 2024-07-12 | Stage2 | 2024-07-12 @ 3,070 | 5.05% / -19.71% | 11.56% / -23.78% | counterexample_or_failed_rerating |
| C15-L90-08 | 300720 Hanil Cement | 2024-03-22 | Stage2-Actionable | 2024-03-22 @ 11,970 | 41.02% / -0.08% | 41.02% / -0.08% | positive_structural_success_or_guardrail_positive |


## 5. Actual Stock-Web entry rows and contamination audit

| symbol | entry row OHLCV | peak 180D | trough 180D | stock-count change 180D | usable |
|---:|---|---|---|---:|---|
| 005010 | 2025-03-04 o=4,820 h=6,050 l=4,820 c=5,600 v=35,896,579 | 2025-03-06 46.27% | 2025-10-13 -21.58% | 0.00% | true |
| 306200 | 2024-08-22 o=117,800 h=117,800 l=116,000 c=116,500 v=6,903 | 2025-03-06 84.63% | 2024-11-15 -8.23% | 0.00% | true |
| 092790 | 2024-06-07 o=10,230 h=10,770 l=9,150 c=9,700 v=29,273,594 | 2025-03-05 75.86% | 2024-12-09 -29.72% | 0.00% | true |
| 071090 | 2024-06-07 o=4,660 h=4,785 l=4,215 c=4,265 v=5,513,747 | 2024-06-07 2.68% | 2024-12-09 -46.35% | 0.00% | true |
| 038500 | 2024-06-07 o=3,500 h=3,580 l=3,115 c=3,165 v=8,148,105 | 2024-07-31 15.29% | 2024-12-10 -19.57% | 0.00% | true |
| 213500 | 2024-07-12 o=10,640 h=10,670 l=10,550 c=10,590 v=23,903 | 2024-07-12 0.28% | 2025-04-09 -27.44% | 0.00% | true |
| 009580 | 2024-07-12 o=3,070 h=3,100 l=3,055 c=3,065 v=62,713 | 2025-01-02 11.56% | 2024-12-10 -23.78% | 0.00% | true |
| 300720 | 2024-03-22 o=11,970 h=12,320 l=11,960 c=12,180 v=83,454 | 2024-06-05 41.02% | 2024-03-22 -0.08% | 0.00% | true |


Narrative-only blocked rows:

- `008970` Dongyang Steel Pipe / 2024-06-06 East Sea drilling casing theme: 180D stock-count change exceeded 20%, so it is excluded from calibration triggers.
- `198440` Korea Cement / 2024-06-06 East Sea drilling cement theme: 180D stock-count change exceeded 20%, so it is excluded from calibration triggers.

## 6. Raw score component simulation

C15 current weight basis from the runtime index is treated as `EPS/Vis/Bott/Mis/Val/Cap/Info = 20/12/20/10/10/8/20`. The important residual is that `Bottleneck` and `Info` can overpower the conversion quality check when the story says “raw material / drilling / paper / cement spread,” but the issuer-level pass-through is missing.

| case | symbol | raw components EPS/Vis/Bott/Mis/Val/Cap/Info | simulated total | residual diagnosis |
|---|---:|---|---:|---|
| C15-L90-01 | 005010 | 68/72/62/63/57/50/65 | 64.2 | would over-promote if tariff-spread headline is treated as realized margin/cash; late MAE requires phase guard |
| C15-L90-02 | 306200 | 45/50/52/70/66/45/58 | 55.9 | hard-4C would be too harsh because weak-market evidence was cyclical reset rather than issuer route death |
| C15-L90-03 | 092790 | 55/58/61/60/52/45/50 | 55.9 | profile needs cross-sectional route-quality guard: speculative route produced later MFE but with high MAE |
| C15-L90-04 | 071090 | 38/43/45/48/45/40/42 | 42.8 | same theme should not grant equal Stage2 bonus across steel-pipe names without issuer conversion |
| C15-L90-05 | 038500 | 42/45/48/50/48/43/45 | 45.3 | generic drilling-cement route should be capped until shipment/margin bridge appears |
| C15-L90-06 | 213500 | 50/55/45/48/42/40/43 | 47.0 | result/forecast Green trap: export rebound was offset by pulp/freight cost and price path immediately failed |
| C15-L90-07 | 009580 | 47/43/44/52/45/40/35 | 44.5 | proxy-only paper-sector read-through lacks issuer-level pass-through and should stay below Actionable/Yellow |
| C15-L90-08 | 300720 | 62/64/60/66/58/48/60 | 61.2 | profile should allow reset-positive when cost relief has margin bridge and low MAE, but still demand/capex gated |


## 7. Positive / counterexample balance

Positive or guardrail-positive cases:

- `005010` Husteel: direct API pipe US plant/tariff differential gave large short-term MFE, but the 180D MAE says Green should wait for margin/cash conversion.
- `306200` SeAH Steel: weak-market/provision evidence at a reset should not be hard 4C; later 180D MFE shows the warning was cyclical, not thesis death.
- `092790` Nexteel: speculative casing demand still produced strong later MFE, but with high interim MAE, so it is a Stage2/watch route rather than clean Green.
- `300720` Hanil Cement: cost relief after reset worked well, with low MAE, but it still needs demand/shipment/cash confirmation before Green.

Counterexamples:

- `071090` Histeel: same East Sea casing theme failed badly; cross-sectional issuer route quality matters.
- `038500` Sampyo Cement: drilling-cement work headline did not offset weak shipment/demand enough.
- `213500` Hansol Paper: export/specialty-paper rebound was offset by pulp/freight cost; Stage3-Yellow/Green would be a result-quality trap.
- `009580` Moorim P&P: paper-sector proxy without issuer-level conversion gave weak MFE and meaningful MAE.

## 8. Residual rule candidate

### Sector-specific rule candidate

`L4_MATERIALS_SPREAD_RESOURCE` rows should split:

1. commodity/weather headline,
2. product price or ASP pass-through,
3. inventory-cost lag,
4. demand/shipment/customer route,
5. realized margin/cash conversion,
6. local price phase.

A commodity or policy headline is only the gauge reading. Calibration should check whether pressure reaches the issuer's income statement.

### Canonical-archetype rule candidate

`C15_MATERIAL_SPREAD_SUPERCYCLE` should add a **cross-material pass-through / inventory-lag / phase ladder**:

```text
raw-material or policy headline
  -> product price / ASP pass-through
  -> demand, customer, shipment, or utilization route
  -> realized margin and cash conversion
  -> inventory-lag and local price-phase sanity
```

Raw proxy alone stays `Stage2-watch`. Product-route after reset can become `Stage2-Actionable`. Result-only or route-only rows after rerating become `local 4B-watch`. High MAE with a surviving issuer route should not be automatic hard 4C.

## 9. Existing axis stress test

```text
existing_axis_tested:
  - stage2_required_bridge
  - stage3_green_revision_min_by_margin_cash_freshness
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - hard_4c_confirmation
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - stage3_green_revision_min_by_margin_cash_freshness
existing_axis_weakened:
  - hard_4c_thesis_break_routes_to_4c qualified for high-MAE rows with surviving issuer route only
new_axis_proposed:
  - c15_cross_material_passthrough_inventory_lag_and_phase_guard
```

## 10. Machine-readable JSONL rows

```jsonl
{"row_type": "trigger", "schema_version": "e2r_v12", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD", "case_id": "C15-L90-01", "symbol": "005010", "name": "Husteel", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-03-04", "entry_date": "2025-03-04", "entry_price": 4820.0, "entry_open": 4820.0, "entry_high": 6050.0, "entry_low": 4820.0, "entry_close": 5600.0, "MFE_30D_pct": 46.27, "MFE_90D_pct": 46.27, "MFE_180D_pct": 46.27, "MAE_30D_pct": -7.05, "MAE_90D_pct": -7.05, "MAE_180D_pct": -21.58, "peak_180D_date": "2025-03-06", "trough_180D_date": "2025-10-13", "rows_forward": 204, "window_180D_corporate_action_contaminated": false, "window_180D_stock_change_pct": 0.0, "calibration_usable": true, "case_outcome": "positive_structural_success_or_guardrail_positive", "evidence_family": "US_API_pipe_plant_tariff_avoidance_energy_pipe_spread", "evidence_url": "https://www.asiae.co.kr/en/article/2025030409200957191", "source_proxy_only": false, "reuse_reason": "new symbol or new trigger family inside local C15 archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap"}
{"row_type": "trigger", "schema_version": "e2r_v12", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD", "case_id": "C15-L90-02", "symbol": "306200", "name": "SeAH Steel", "trigger_type": "4B", "trigger_date": "2024-08-22", "entry_date": "2024-08-22", "entry_price": 117800.0, "entry_open": 117800.0, "entry_high": 117800.0, "entry_low": 116000.0, "entry_close": 116500.0, "MFE_30D_pct": 1.7, "MFE_90D_pct": 5.94, "MFE_180D_pct": 84.63, "MAE_30D_pct": -7.81, "MAE_90D_pct": -8.23, "MAE_180D_pct": -8.23, "peak_180D_date": "2025-03-06", "trough_180D_date": "2024-11-15", "rows_forward": 328, "window_180D_corporate_action_contaminated": false, "window_180D_stock_change_pct": 0.0, "calibration_usable": true, "case_outcome": "positive_structural_success_or_guardrail_positive", "evidence_family": "steel_pipe_inventory_weak_market_provision_reset", "evidence_url": "https://www.asiae.co.kr/en/article/2024082210235349849", "source_proxy_only": false, "reuse_reason": "new symbol or new trigger family inside local C15 archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap"}
{"row_type": "trigger", "schema_version": "e2r_v12", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD", "case_id": "C15-L90-03", "symbol": "092790", "name": "Nexteel", "trigger_type": "Stage2", "trigger_date": "2024-06-06", "entry_date": "2024-06-07", "entry_price": 10230.0, "entry_open": 10230.0, "entry_high": 10770.0, "entry_low": 9150.0, "entry_close": 9700.0, "MFE_30D_pct": 20.82, "MFE_90D_pct": 20.82, "MFE_180D_pct": 75.86, "MAE_30D_pct": -15.25, "MAE_90D_pct": -29.52, "MAE_180D_pct": -29.72, "peak_180D_date": "2025-03-05", "trough_180D_date": "2024-12-09", "rows_forward": 381, "window_180D_corporate_action_contaminated": false, "window_180D_stock_change_pct": 0.0, "calibration_usable": true, "case_outcome": "positive_structural_success_or_guardrail_positive", "evidence_family": "east_sea_drilling_casing_demand_speculative_route", "evidence_url": "https://www.mk.co.kr/en/stock/11034888", "source_proxy_only": true, "reuse_reason": "new symbol or new trigger family inside local C15 archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap"}
{"row_type": "trigger", "schema_version": "e2r_v12", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD", "case_id": "C15-L90-04", "symbol": "071090", "name": "Histeel", "trigger_type": "4B", "trigger_date": "2024-06-06", "entry_date": "2024-06-07", "entry_price": 4660.0, "entry_open": 4660.0, "entry_high": 4785.0, "entry_low": 4215.0, "entry_close": 4265.0, "MFE_30D_pct": 2.68, "MFE_90D_pct": 2.68, "MFE_180D_pct": 2.68, "MAE_30D_pct": -24.89, "MAE_90D_pct": -38.2, "MAE_180D_pct": -46.35, "peak_180D_date": "2024-06-07", "trough_180D_date": "2024-12-09", "rows_forward": 381, "window_180D_corporate_action_contaminated": false, "window_180D_stock_change_pct": 0.0, "calibration_usable": true, "case_outcome": "counterexample_or_failed_rerating", "evidence_family": "same_drilling_casing_theme_low_conversion_counterexample", "evidence_url": "https://www.mk.co.kr/en/stock/11034888", "source_proxy_only": true, "reuse_reason": "new symbol or new trigger family inside local C15 archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap"}
{"row_type": "trigger", "schema_version": "e2r_v12", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD", "case_id": "C15-L90-05", "symbol": "038500", "name": "Sampyo Cement", "trigger_type": "Stage2", "trigger_date": "2024-06-06", "entry_date": "2024-06-07", "entry_price": 3500.0, "entry_open": 3500.0, "entry_high": 3580.0, "entry_low": 3115.0, "entry_close": 3165.0, "MFE_30D_pct": 2.29, "MFE_90D_pct": 15.29, "MFE_180D_pct": 15.29, "MAE_30D_pct": -14.0, "MAE_90D_pct": -17.29, "MAE_180D_pct": -19.57, "peak_180D_date": "2024-07-31", "trough_180D_date": "2024-12-10", "rows_forward": 381, "window_180D_corporate_action_contaminated": false, "window_180D_stock_change_pct": 0.0, "calibration_usable": true, "case_outcome": "counterexample_or_failed_rerating", "evidence_family": "drilling_cement_work_cement_material_route", "evidence_url": "https://www.mk.co.kr/en/stock/11034888", "source_proxy_only": true, "reuse_reason": "new symbol or new trigger family inside local C15 archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap"}
{"row_type": "trigger", "schema_version": "e2r_v12", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD", "case_id": "C15-L90-06", "symbol": "213500", "name": "Hansol Paper", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-07-12", "entry_date": "2024-07-12", "entry_price": 10640.0, "entry_open": 10640.0, "entry_high": 10670.0, "entry_low": 10550.0, "entry_close": 10590.0, "MFE_30D_pct": 0.28, "MFE_90D_pct": 0.28, "MFE_180D_pct": 0.28, "MAE_30D_pct": -10.71, "MAE_90D_pct": -17.2, "MAE_180D_pct": -27.44, "peak_180D_date": "2024-07-12", "trough_180D_date": "2025-04-09", "rows_forward": 356, "window_180D_corporate_action_contaminated": false, "window_180D_stock_change_pct": 0.0, "calibration_usable": true, "case_outcome": "counterexample_or_failed_rerating", "evidence_family": "specialty_paper_export_rebound_vs_pulp_freight_cost", "evidence_url": "https://www.asiae.co.kr/en/article/2024071116573335226", "source_proxy_only": false, "reuse_reason": "new symbol or new trigger family inside local C15 archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap"}
{"row_type": "trigger", "schema_version": "e2r_v12", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD", "case_id": "C15-L90-07", "symbol": "009580", "name": "Moorim P&P", "trigger_type": "Stage2", "trigger_date": "2024-07-12", "entry_date": "2024-07-12", "entry_price": 3070.0, "entry_open": 3070.0, "entry_high": 3100.0, "entry_low": 3055.0, "entry_close": 3065.0, "MFE_30D_pct": 5.05, "MFE_90D_pct": 5.05, "MFE_180D_pct": 11.56, "MAE_30D_pct": -7.49, "MAE_90D_pct": -19.71, "MAE_180D_pct": -23.78, "peak_180D_date": "2025-01-02", "trough_180D_date": "2024-12-10", "rows_forward": 356, "window_180D_corporate_action_contaminated": false, "window_180D_stock_change_pct": 0.0, "calibration_usable": true, "case_outcome": "counterexample_or_failed_rerating", "evidence_family": "paper_pulp_integrated_cost_buffer_proxy", "evidence_url": "https://www.asiae.co.kr/en/article/2024071116573335226", "source_proxy_only": true, "reuse_reason": "new symbol or new trigger family inside local C15 archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap"}
{"row_type": "trigger", "schema_version": "e2r_v12", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_STEEL_PIPE_PAPER_CEMENT_PASSTHROUGH_PHASE_GUARD", "case_id": "C15-L90-08", "symbol": "300720", "name": "Hanil Cement", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-22", "entry_date": "2024-03-22", "entry_price": 11970.0, "entry_open": 11970.0, "entry_high": 12320.0, "entry_low": 11960.0, "entry_close": 12180.0, "MFE_30D_pct": 10.86, "MFE_90D_pct": 41.02, "MFE_180D_pct": 41.02, "MAE_30D_pct": -0.08, "MAE_90D_pct": -0.08, "MAE_180D_pct": -0.08, "peak_180D_date": "2024-06-05", "trough_180D_date": "2024-03-22", "rows_forward": 431, "window_180D_corporate_action_contaminated": false, "window_180D_stock_change_pct": 0.0, "calibration_usable": true, "case_outcome": "positive_structural_success_or_guardrail_positive", "evidence_family": "cement_coal_cost_decline_vs_demand_cost_capex", "evidence_url": "https://www.asiae.co.kr/en/article/2024032108180183866", "source_proxy_only": false, "reuse_reason": "new symbol or new trigger family inside local C15 archive", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap"}
{"row_type": "score_simulation", "case_id": "C15-L90-01", "symbol": "005010", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "EPS": 68, "Visibility": 72, "Bottleneck": 62, "Mispricing": 63, "Valuation": 57, "Capital": 50, "Info": 65, "calibrated_total": 64.2, "simulated_stage": "Stage2-Actionable kept; Green capped until margin/cash conversion", "current_profile_error": "would over-promote if tariff-spread headline is treated as realized margin/cash; late MAE requires phase guard", "existing_axis_tested": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"]}
{"row_type": "score_simulation", "case_id": "C15-L90-02", "symbol": "306200", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "EPS": 45, "Visibility": 50, "Bottleneck": 52, "Mispricing": 70, "Valuation": 66, "Capital": 45, "Info": 58, "calibrated_total": 55.9, "simulated_stage": "4B-watch not hard 4C; later MFE confirms reset bucket", "current_profile_error": "hard-4C would be too harsh because weak-market evidence was cyclical reset rather than issuer route death", "existing_axis_tested": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"]}
{"row_type": "score_simulation", "case_id": "C15-L90-03", "symbol": "092790", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "EPS": 55, "Visibility": 58, "Bottleneck": 61, "Mispricing": 60, "Valuation": 52, "Capital": 45, "Info": 50, "calibrated_total": 55.9, "simulated_stage": "Stage2-watch; high MAE prevents Green", "current_profile_error": "profile needs cross-sectional route-quality guard: speculative route produced later MFE but with high MAE", "existing_axis_tested": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"]}
{"row_type": "score_simulation", "case_id": "C15-L90-04", "symbol": "071090", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "EPS": 38, "Visibility": 43, "Bottleneck": 45, "Mispricing": 48, "Valuation": 45, "Capital": 40, "Info": 42, "calibrated_total": 42.8, "simulated_stage": "4B-watch / counterexample", "current_profile_error": "same theme should not grant equal Stage2 bonus across steel-pipe names without issuer conversion", "existing_axis_tested": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"]}
{"row_type": "score_simulation", "case_id": "C15-L90-05", "symbol": "038500", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "EPS": 42, "Visibility": 45, "Bottleneck": 48, "Mispricing": 50, "Valuation": 48, "Capital": 43, "Info": 45, "calibrated_total": 45.3, "simulated_stage": "Stage2-watch capped; shipment bridge missing", "current_profile_error": "generic drilling-cement route should be capped until shipment/margin bridge appears", "existing_axis_tested": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"]}
{"row_type": "score_simulation", "case_id": "C15-L90-06", "symbol": "213500", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "EPS": 50, "Visibility": 55, "Bottleneck": 45, "Mispricing": 48, "Valuation": 42, "Capital": 40, "Info": 43, "calibrated_total": 47.0, "simulated_stage": "Yellow rejected; cost/freight bridge negative", "current_profile_error": "result/forecast Green trap: export rebound was offset by pulp/freight cost and price path immediately failed", "existing_axis_tested": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"]}
{"row_type": "score_simulation", "case_id": "C15-L90-07", "symbol": "009580", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "EPS": 47, "Visibility": 43, "Bottleneck": 44, "Mispricing": 52, "Valuation": 45, "Capital": 40, "Info": 35, "calibrated_total": 44.5, "simulated_stage": "Stage2-watch only; source proxy", "current_profile_error": "proxy-only paper-sector read-through lacks issuer-level pass-through and should stay below Actionable/Yellow", "existing_axis_tested": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"]}
{"row_type": "score_simulation", "case_id": "C15-L90-08", "symbol": "300720", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "EPS": 62, "Visibility": 64, "Bottleneck": 60, "Mispricing": 66, "Valuation": 58, "Capital": 48, "Info": 60, "calibrated_total": 61.2, "simulated_stage": "Stage2-Actionable/Yellow after reset; Green waits for shipment/cash", "current_profile_error": "profile should allow reset-positive when cost relief has margin bridge and low MAE, but still demand/capex gated", "existing_axis_tested": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_confirmation"]}
{"row_type": "aggregate", "selected_round": "R4", "selected_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "calibration_usable_case_count": 8, "calibration_usable_trigger_count": 8, "new_independent_case_count": 8, "reused_case_count": 0, "new_symbol_count": 7, "same_archetype_new_symbol_count": 7, "same_archetype_new_trigger_family_count": 8, "new_trigger_family_count": 8, "positive_case_count": 4, "counterexample_count": 4, "current_profile_error_count": 6, "diversity_score_summary": "7 symbols / 8 trigger families / steel pipe, paper-pulp, cement spread rows / 4 positive + 4 counterexample / no 180D corporate-action contamination", "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md", "selected_priority_bucket": "Priority 1 C15 spread reversal/inventory-cycle balance repair + Priority 0 URL/proxy/MFE-MAE repair", "round_schedule_status": "coverage_index_selected; local C15 max loop 89 -> selected loop 90; 직전 C13 반복 회피", "round_sector_consistency": "pass", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "shadow_weight", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "before_weights": "20/12/20/10/10/8/20", "after_weights_shadow_only": "20/13/19/10/10/8/20", "production_scoring_changed": false, "rationale": "Increase visibility/finality slightly and reduce bottleneck credit for raw commodity/weather headlines unless issuer pass-through and margin/cash conversion are visible."}
{"row_type": "residual_contribution", "selected_round": "R4", "selected_loop": 90, "sector_specific_rule_candidate": "L4 material-spread rows should split commodity weather, product ASP/pass-through, inventory-cost lag, demand/shipment/customer route, realized margin/cash conversion, and price phase.", "canonical_archetype_rule_candidate": "C15 should use a pass-through and phase ladder: raw-material or policy headline -> product price/ASP pass-through -> demand/customer/shipment route -> realized margin/cash conversion -> inventory-lag and price-phase sanity. Raw proxy alone stays Stage2-watch; route after rerating is local 4B-watch; high MAE with live route is not hard 4C.", "new_axis_proposed": "c15_cross_material_passthrough_inventory_lag_and_phase_guard", "existing_axis_strengthened": "stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard; full_4b_requires_non_price_evidence", "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c qualified for high-MAE rows with surviving issuer route only"}
{"row_type": "narrative_only", "symbol": "008970", "name": "Dongyang Steel Pipe", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "trigger_date": "2024-06-06", "reason": "180D stock-count change exceeded 20% corporate-action contamination gate in downloaded Stock-Web window; not counted as trigger", "evidence_url": "https://www.mk.co.kr/en/stock/11034888"}
{"row_type": "narrative_only", "symbol": "198440", "name": "Korea Cement", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "trigger_date": "2024-06-06", "reason": "180D stock-count change exceeded 20% corporate-action contamination gate in downloaded Stock-Web window; not counted as trigger", "evidence_url": "https://www.mk.co.kr/en/stock/11034888"}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during research generation.

When batch-implementing, read this MD together with other v12 residual research files. Do not change production scoring based on one loop alone. Consider adding an archetype-scoped C15 guard only if multiple independent C15 loops support the same pattern:

- raw commodity/weather/policy headline is not enough for Stage2-Actionable;
- issuer-level product ASP/pass-through or customer/shipment route is required;
- Stage3-Yellow/Green requires realized margin/cash freshness;
- route-after-rerating becomes local 4B-watch;
- high MAE with live issuer route should not auto-route to hard 4C.

Expected patch style: shadow-only rule candidate -> batch calibration review -> profile spec if supported.
```

## 12. Next research state

```text
completed_round = R4
completed_loop = 90
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C15 spread reversal / inventory-cycle balance repair + Priority 0 direct URL/proxy/MFE-MAE repair
next_recommended_archetypes = C01/C05 direct FCF or cash-conversion rows; C13 strict-new utilization/ex-credit rows; C10 strict-new order-conversion rows; C31 non-semi/battery awarded-cashflow rows; R13 only for genuinely new taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
