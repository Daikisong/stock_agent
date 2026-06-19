# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_122_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round: R1
selected_loop: 122
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under_30_representative_rows / C02 rows 10 need_to_30 20 in static No-Repeat Index; session-local C02 loops 118-121 avoided by new symbol/date/evidence-family emphasis
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: DIRECT_GRID_DATACENTER_POWER_ORDER_BACKLOG_CAPA_BRIDGE_WITH_HOLDCO_AND_COMPONENT_PROXY_GUARD
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
investment_recommendation: false
```

This file is a standalone v12 historical calibration artifact. It does not recommend a current trade, does not scan live candidates, does not open or patch `src/e2r`, and does not change production scoring.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
production_scoring_changed = false for this research artifact
```

## 2. Round / Large Sector / Canonical Archetype Scope

- Selected canonical: `C02_POWER_GRID_DATACENTER_CAPEX`.
- Derived round/sector: `R1` / `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`.
- This is not R13 because the artifact is C02 sector-specific residual research, not cross-archetype red-team.

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` lists C02 as Priority 0 with 10 representative rows and a large need-to-30 gap. Session-local C02 outputs already touched HD Hyundai Electric, Jeeryong Electric, Hyosung Heavy, P&C Tech, Daewon Cable, Iljin Electric, Sanil Electric, GNC Energy, Vitzro Tech, LS Eco Energy, Gaon Cable, Taihan Cable, and several component proxies. This loop avoids strict duplicate keys and emphasizes: direct switchgear/transformer backlog, LS holding-company discount, Taihan late order reprice, HVDC fittings proxy, and transmission/distribution-material product identity.

```text
strict_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_count = 0
new_independent_case_ratio = 1.00
minimum_calibration_usable_case_count_pass = true
minimum_positive_case_count_pass = true
minimum_counterexample_count_pass = true
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
entry_price_basis = close c column on entry_date
MFE_N_pct = max high h from entry_date through N trading days / entry_price - 1
MAE_N_pct = min low l from entry_date through N trading days / entry_price - 1
```

All five selected trigger rows have 30D/90D/180D MFE/MAE fields and clean selected 180D windows in the local stock-web materialized shards used for this MD.

## 5. Historical Eligibility Gate

| check | result |
|---|---|
| past trigger date | pass |
| entry date in stock-web tradable shard | pass |
| 180 trading-row forward window | pass for all trigger rows |
| price source fields | pass |
| corporate action window | no selected-window contamination used for calibration |
| non-price evidence | mixed: two positive bridge rows, three guardrail rows |

## 6. Canonical Archetype Compression Map

C02 is not just “anything with electricity.” The useful rerating chain is:

```text
AI/data-center/grid capex
  -> named power-system product route: transformer / switchgear / busduct / EHV cable / grid installation
  -> customer/order/backlog/CAPA/delivery visibility
  -> OP margin / FCF / revision bridge
  -> Stage2-Actionable or Stage3-Yellow if price is not already crowded

If the row has only product identity, holding-company exposure, or theme vocabulary:
  -> Stage2-watch or discounted Stage2-Actionable
  -> local 4B overlay if entry follows sector crowding or MFE is already exhausted
```

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE90 | MAE90 | key lesson |
|---|---:|---|---|---|---|---:|---:|---|
| C02_R1L122_010120_20250422_LS_ELECTRIC_1Q25_BACKLOG_SWITCHGEAR_TRANSFORMER | 010120 | LS ELECTRIC | positive | Stage3-Yellow | 2025-04-22 | 93.51 | -0.41 | allow_Yellow_when_switchgear_transformer_backlog_CAGR_and_capacity_expansion_are_visible |
| C02_R1L122_006260_20250422_LS_HOLDCO_POWER_INFRA_PROXY_SUCCESS_WITH_DISCOUNT | 006260 | LS | positive | Stage2-Actionable | 2025-04-22 | 85.34 | -1.01 | allow_Stage2_Actionable_only_with_holdco_proxy_discount |
| C02_R1L122_001440_20240618_TAIHAN_US_GRID_ORDER_LATE_REPRICE_COUNTER | 001440 | 대한전선 | counterexample | Stage2-Actionable | 2024-06-18 | 9.44 | -34.96 | attach_local_4B_when_direct_order_headline_follows_large_sector_rerating_without_margin_bridge |
| C02_R1L122_017510_20240801_SEMYUNG_HVDC_FITTINGS_PROXY_HIGH_MAE | 017510 | 세명전기 | counterexample | Stage2 | 2024-08-01 | 9.85 | -43.28 | keep_HVDC_fittings_proxy_at_Stage2_until_named_project_and_sales_conversion |
| C02_R1L122_147830_20240717_CHERYONG_INDUSTRIAL_PRODUCT_IDENTITY_TRAP | 147830 | 제룡산업 | counterexample | Stage2 | 2024-07-17 | 3.58 | -44.31 | block_Yellow_for_component_identity_without_named_grid_datacenter_order_or_backlog |


## 8. Positive vs Counterexample Balance

Positive rows: `2`. Counterexample/guardrail rows: `3`. The loop deliberately keeps the positive side narrow: direct backlog/capacity bridge and discounted holding-company bridge. Everything else is used to prevent C02 from over-promoting product identity or order headlines after crowding.

## 9. Evidence Source Map

| evidence_id | symbol | source URL | use |
|---|---:|---|---|
| EV_C02_R1L122_LS_ELECTRIC_20250422_MIRAE_1Q25 | 010120 | https://securities.miraeasset.com/bbs/download/2135699.pdf?attachmentId=2135699 | 1Q25 data-center power-infrastructure demand remained strong; switchgear and ultra-high-voltage transformer backlog expanded YoY and the company was securing additional U.S. land/capacity. This is a direct C02 route because the product, backlog, capacity and margin bridge are visible. |
| EV_C02_R1L122_LS_HOLDCO_20250422_SUBSIDIARY_POWER_BACKLOG | 006260 | https://securities.miraeasset.com/bbs/download/2135699.pdf?attachmentId=2135699 | LS holding-company exposure captured the same power-equipment rerating, but the evidence is subsidiary-level. C02 credit can exist, yet it should be capped below direct operating-company routes unless capital-allocation or NAV-realization evidence is present. |
| EV_C02_R1L122_TAIHAN_20240618_YNA_US_GRID_ORDERS | 001440 | https://en.yna.co.kr/view/AEN20240618003100320 | Taihan had actual U.S. power-grid contracts totaling KRW130bn and cumulative U.S. orders above KRW330bn in 2024. The order evidence is real, but the entry came after crowded cable rerating; price path shows low upside and large drawdown, so direct order alone needs local 4B context. |
| EV_C02_R1L122_SEMYUNG_20240801_FNNEWS_HVDC_AI_POWER | 017510 | https://www.fnnews.com/news/202408010941003670 | Semyung had HVDC/transmission fittings vocabulary and AI-power-demand linkage, but the as-of source was theme/proxy-heavy. Without named project volume, backlog and margin conversion, this should remain Stage2-watch even if later power-grid attention resumes. |
| EV_C02_R1L122_CHERYONGIND_PRODUCT_CATALOG | 147830 | https://www.cheryongind.com/ | Jeeryong Industrial has transmission/distribution/underground equipment product identity, but the selected trigger family lacks a named data-center/grid customer, backlog or margin bridge. The price path collapses almost immediately, making it a clean C02 product-identity trap. |


## 10. Price Data Source Map

| symbol | shard path | profile path | entry | entry price |
|---:|---|---|---|---:|
| 010120 | `atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv` | `atlas/symbol_profiles/010/010120.json` | 2025-04-22 | 172600.0 |
| 006260 | `atlas/ohlcv_tradable_by_symbol_year/006/006260/2025.csv` | `atlas/symbol_profiles/006/006260.json` | 2025-04-22 | 118700.0 |
| 001440 | `atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv` | `atlas/symbol_profiles/001/001440.json` | 2024-06-18 | 15790.0 |
| 017510 | `atlas/ohlcv_tradable_by_symbol_year/017/017510/2024.csv` | `atlas/symbol_profiles/017/017510.json` | 2024-08-01 | 6700.0 |
| 147830 | `atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv` | `atlas/symbol_profiles/147/147830.json` | 2024-07-17 | 9230.0 |


## 11. Case-by-Case Trigger Grid

### C02_R1L122_010120_20250422_LS_ELECTRIC_1Q25_BACKLOG_SWITCHGEAR_TRANSFORMER — LS ELECTRIC (010120)

- Trigger: `Stage3-Yellow` on `2025-04-22`, entry `2025-04-22` at `172600.0`.

- Evidence family: `direct_switchgear_transformer_backlog_and_US_capex_expansion`.

- Evidence summary: 1Q25 data-center power-infrastructure demand remained strong; switchgear and ultra-high-voltage transformer backlog expanded YoY and the company was securing additional U.S. land/capacity. This is a direct C02 route because the product, backlog, capacity and margin bridge are visible.

- Price path: MFE30/90/180 = `59.04 / 93.51 / 220.97`; MAE30/90/180 = `-0.41 / -0.41 / -0.41`.

- Peak/drawdown: peak `2026-01-14` at `554000.0`, drawdown after peak `-10.2%`.

- Residual: `current_profile_missed_structural_if_C02_waits_for_big_tech_named_customer_only` → `allow_Yellow_when_switchgear_transformer_backlog_CAGR_and_capacity_expansion_are_visible`.

### C02_R1L122_006260_20250422_LS_HOLDCO_POWER_INFRA_PROXY_SUCCESS_WITH_DISCOUNT — LS (006260)

- Trigger: `Stage2-Actionable` on `2025-04-22`, entry `2025-04-22` at `118700.0`.

- Evidence family: `holding_company_exposure_to_LS_Electric_LS_Cable_power_infra_backlog`.

- Evidence summary: LS holding-company exposure captured the same power-equipment rerating, but the evidence is subsidiary-level. C02 credit can exist, yet it should be capped below direct operating-company routes unless capital-allocation or NAV-realization evidence is present.

- Price path: MFE30/90/180 = `63.77 / 85.34 / 97.98`; MAE30/90/180 = `-1.01 / -1.01 / -1.01`.

- Peak/drawdown: peak `2025-11-04` at `235000.0`, drawdown after peak `-26.77%`.

- Residual: `current_profile_false_positive_if_holdco_proxy_gets_same_C02_score_as_direct_equipment_supplier` → `allow_Stage2_Actionable_only_with_holdco_proxy_discount`.

### C02_R1L122_001440_20240618_TAIHAN_US_GRID_ORDER_LATE_REPRICE_COUNTER — 대한전선 (001440)

- Trigger: `Stage2-Actionable` on `2024-06-18`, entry `2024-06-18` at `15790.0`.

- Evidence family: `actual_US_power_grid_contract_but_price_already_reflected`.

- Evidence summary: Taihan had actual U.S. power-grid contracts totaling KRW130bn and cumulative U.S. orders above KRW330bn in 2024. The order evidence is real, but the entry came after crowded cable rerating; price path shows low upside and large drawdown, so direct order alone needs local 4B context.

- Price path: MFE30/90/180 = `9.44 / 9.44 / 9.44`; MAE30/90/180 = `-14.44 / -34.96 / -36.67`.

- Peak/drawdown: peak `2024-06-28` at `17280.0`, drawdown after peak `-42.13%`.

- Residual: `current_profile_false_positive_if_actual_order_automatically_upgrades_to_Yellow_after_reprice` → `attach_local_4B_when_direct_order_headline_follows_large_sector_rerating_without_margin_bridge`.

### C02_R1L122_017510_20240801_SEMYUNG_HVDC_FITTINGS_PROXY_HIGH_MAE — 세명전기 (017510)

- Trigger: `Stage2` on `2024-08-01`, entry `2024-08-01` at `6700.0`.

- Evidence family: `HVDC_grid_fittings_theme_from_AI_power_demand_without_order_margin_confirmation`.

- Evidence summary: Semyung had HVDC/transmission fittings vocabulary and AI-power-demand linkage, but the as-of source was theme/proxy-heavy. Without named project volume, backlog and margin conversion, this should remain Stage2-watch even if later power-grid attention resumes.

- Price path: MFE30/90/180 = `9.85 / 9.85 / 29.4`; MAE30/90/180 = `-27.61 / -43.28 / -43.28`.

- Peak/drawdown: peak `2025-04-23` at `8670.0`, drawdown after peak `-28.14%`.

- Residual: `current_profile_false_positive_if_HVDC_component_vocabulary_is_promoted_to_Actionable` → `keep_HVDC_fittings_proxy_at_Stage2_until_named_project_and_sales_conversion`.

### C02_R1L122_147830_20240717_CHERYONG_INDUSTRIAL_PRODUCT_IDENTITY_TRAP — 제룡산업 (147830)

- Trigger: `Stage2` on `2024-07-17`, entry `2024-07-17` at `9230.0`.

- Evidence family: `transmission_distribution_material_identity_without_named_grid_datacenter_order`.

- Evidence summary: Jeeryong Industrial has transmission/distribution/underground equipment product identity, but the selected trigger family lacks a named data-center/grid customer, backlog or margin bridge. The price path collapses almost immediately, making it a clean C02 product-identity trap.

- Price path: MFE30/90/180 = `3.58 / 3.58 / 3.58`; MAE30/90/180 = `-33.37 / -44.31 / -51.19`.

- Peak/drawdown: peak `2024-07-18` at `9560.0`, drawdown after peak `-52.88%`.

- Residual: `current_profile_false_positive_if_power_component_identity_is_treated_like_transformer_backlog` → `block_Yellow_for_component_identity_without_named_grid_datacenter_order_or_backlog`.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TRIG_C02_R1L122_010120_20250422_STAGE3Y | 010120 | 2025-04-22 | 172600.0 | 59.04 | 93.51 | 220.97 | -0.41 | -0.41 | -0.41 | 2026-01-14 | 554000.0 | -10.2 |
| TRIG_C02_R1L122_006260_20250422_STAGE2A | 006260 | 2025-04-22 | 118700.0 | 63.77 | 85.34 | 97.98 | -1.01 | -1.01 | -1.01 | 2025-11-04 | 235000.0 | -26.77 |
| TRIG_C02_R1L122_001440_20240618_STAGE2A | 001440 | 2024-06-18 | 15790.0 | 9.44 | 9.44 | 9.44 | -14.44 | -34.96 | -36.67 | 2024-06-28 | 17280.0 | -42.13 |
| TRIG_C02_R1L122_017510_20240801_STAGE2 | 017510 | 2024-08-01 | 6700.0 | 9.85 | 9.85 | 29.4 | -27.61 | -43.28 | -43.28 | 2025-04-23 | 8670.0 | -28.14 |
| TRIG_C02_R1L122_147830_20240717_STAGE2 | 147830 | 2024-07-17 | 9230.0 | 3.58 | 3.58 | 3.58 | -33.37 | -44.31 | -51.19 | 2024-07-18 | 9560.0 | -52.88 |


## 13. Current Calibrated Profile Stress Test

- Existing `stage2_required_bridge` is strengthened, not repeated generically. C02 needs a product-route bridge that is narrower than “electricity demand.”
- `price_only_blowoff_blocks_positive_stage` remains necessary because Taihan, Semyung, and Jeeryong show high-MAE or peak-first behavior when the evidence is late or proxy-heavy.
- `full_4b_requires_non_price_evidence` remains correct; these rows mostly justify local 4B overlays rather than hard thesis breaks.
- No Green threshold relaxation is proposed. LS Electric can reach Yellow because backlog, capacity and margin bridge exist; component proxies cannot.

## 14. Stage2 / Yellow / Green Comparison

| profile interpretation | included cases | avg MFE90 | avg MAE90 | verdict |
|---|---:|---:|---:|---|
| positive_bridge_rows | 2 | 89.43 | -0.71 | bridge works |
| counterexample_guardrail_rows | 3 | 7.62 | -40.85 | needs guardrail |
| all_rows | 5 | 40.34 | -24.79 | needs guardrail |


## 15. 4B Local vs Full-window Timing Audit

- LS Electric and LS holding exposure both generated very large MFE. Their later states need local 4B/profit-lock overlays after fast reprice, but not a full 4B at entry because the non-price bridge was improving.
- Taihan has real order evidence, yet the order came after sector reprice and the forward path gave only 9.44% MFE180 against -36.67% MAE180. That is a clean local 4B guardrail.
- Semyung and Jeeryong demonstrate that product vocabulary can move first and then collapse; those should not become Stage3 without named order/backlog/margin evidence.

## 16. 4C Protection Audit

No hard 4C is proposed in this loop. The failure mode is mostly over-promotion and bad entry, not contract cancellation, legal block, accounting break, or confirmed thesis destruction.

## 17. Sector-Specific Rule Candidate

```text
L1_GRID_DATACENTER_CAPEX_DIRECT_BRIDGE_VS_PROXY_GUARD
- Direct suppliers: transformer/switchgear/EHV cable/busduct/grid system order + backlog/CAPA/delivery + margin bridge can reach Stage2-Actionable/Yellow.
- Holding-company exposure: cap one stage lower unless shareholder-return/NAV realization is also visible.
- Component identity: stay Stage2-watch until named order or sales/margin conversion appears.
- Direct order after large reprice: attach local 4B if MFE is small relative to MAE or if margin bridge is missing.
```

## 18. Canonical-Archetype Rule Candidate

```text
C02_DIRECT_GRID_DATACENTER_CAPEX_REQUIRES_NAMED_ORDER_BACKLOG_CAPA_OR_MARGIN_BRIDGE
```
Proposed effect: separate LS Electric-style direct backlog/capacity bridge from Taihan-style late direct order, LS holdco proxy, Semyung HVDC fittings proxy, and Jeeryong product-identity trap.

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive guard | missed-structural guard |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 5 | 40.34 | -24.79 | medium | medium |
| P2 C02 candidate profile | 5 | 40.34 | -24.79 | stronger for proxies | better for direct backlog bridge |


## 20. Score-Return Alignment Matrix

| case_id | before score/stage | after score/stage | alignment |
|---|---|---|---|
| C02_R1L122_010120_20250422_LS_ELECTRIC_1Q25_BACKLOG_SWITCHGEAR_TRANSFORMER | 75 / Stage3-Yellow | 84 / Stage3-Yellow | aligned_positive |
| C02_R1L122_006260_20250422_LS_HOLDCO_POWER_INFRA_PROXY_SUCCESS_WITH_DISCOUNT | 70 / Stage2 | 74 / Stage2-Actionable | aligned_positive |
| C02_R1L122_001440_20240618_TAIHAN_US_GRID_ORDER_LATE_REPRICE_COUNTER | 76 / Stage3-Yellow | 68 / Stage2-Actionable | guardrail_aligned |
| C02_R1L122_017510_20240801_SEMYUNG_HVDC_FITTINGS_PROXY_HIGH_MAE | 69 / Stage2 | 59 / Stage2 | guardrail_aligned |
| C02_R1L122_147830_20240717_CHERYONG_INDUSTRIAL_PRODUCT_IDENTITY_TRAP | 67 / Stage2 | 55 / Stage2 | guardrail_aligned |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representatives | current profile errors | sector rule | canonical rule | coverage gap after this loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | DIRECT_GRID_DATACENTER_POWER_ORDER_BACKLOG_CAPA_BRIDGE_WITH_HOLDCO_AND_COMPONENT_PROXY_GUARD | 2 | 3 | 3 | 0 | 5 | 0 | 5 | 5 | 5 | L1_GRID_DATACENTER_CAPEX_DIRECT_BRIDGE_VS_PROXY_GUARD | C02_DIRECT_GRID_DATACENTER_CAPEX_REQUIRES_NAMED_ORDER_BACKLOG_CAPA_OR_MARGIN_BRIDGE | static 10 + session-local C02 usable rows; still treat future C02 as new-symbol/date-family only |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_required_bridge, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: direct_order_late_reprice_false_positive, holding_company_proxy_discount_needed, component_identity_proxy_high_MAE
new_axis_proposed: C02_DIRECT_GRID_DATACENTER_CAPEX_REQUIRES_NAMED_ORDER_BACKLOG_CAPA_OR_MARGIN_BRIDGE
existing_axis_strengthened: stage2_required_bridge; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: none
existing_axis_kept: hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L1_GRID_DATACENTER_CAPEX_DIRECT_BRIDGE_VS_PROXY_GUARD
canonical_archetype_rule_candidate: C02_DIRECT_GRID_DATACENTER_CAPEX_REQUIRES_NAMED_ORDER_BACKLOG_CAPA_OR_MARGIN_BRIDGE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger rows, stock-web OHLC-derived 30/90/180D paths, C02 stage/evidence split, duplicate-key hygiene, and shadow-only rule candidate. Not validated: current live candidates, future post-2026-02-20 price path, production scoring code, and broker/API integration.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes

shadow_weight,C02_DIRECT_GRID_DATACENTER_CAPEX_REQUIRES_NAMED_ORDER_BACKLOG_CAPA_OR_MARGIN_BRIDGE,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1 guardrail-specific not production,Direct supplier backlog/capacity bridge differs from proxy identity or late order reprice,Improves split between direct LS Electric bridge and Taihan/Semyung/Jeeryong guardrails,TRIG_C02_R1L122_010120_20250422_STAGE3Y|TRIG_C02_R1L122_006260_20250422_STAGE2A|TRIG_C02_R1L122_001440_20240618_STAGE2A|TRIG_C02_R1L122_017510_20240801_STAGE2|TRIG_C02_R1L122_147830_20240717_STAGE2,5,5,3,medium,canonical_shadow_only,not production; post-calibrated residual

```

## 25. Machine-Readable Rows

```jsonl

{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","round":"R1","loop":122,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX"}

{"row_type":"case","case_id":"C02_R1L122_010120_20250422_LS_ELECTRIC_1Q25_BACKLOG_SWITCHGEAR_TRANSFORMER","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_TRANSFORMER_BACKLOG_DATACENTER_DEMAND_TO_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural_if_C02_waits_for_big_tech_named_customer_only","price_source":"Songdaiki/stock-web","notes":"1Q25 data-center power-infrastructure demand remained strong; switchgear and ultra-high-voltage transformer backlog expanded YoY and the company was securing additional U.S. land/capacity. This is a direct C02 route because the product, backlog, capacity and margin bridge are visible."}

{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C02_R1L122_010120_20250422_STAGE3Y","case_id":"C02_R1L122_010120_20250422_LS_ELECTRIC_1Q25_BACKLOG_SWITCHGEAR_TRANSFORMER","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_TRANSFORMER_BACKLOG_DATACENTER_DEMAND_TO_MARGIN_BRIDGE","sector":"industrial_power_grid_datacenter","primary_archetype":"C02_power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2025-04-22","entry_date":"2025-04-22","entry_price":172600.0,"evidence_available_at_that_date":"1Q25 data-center power-infrastructure demand remained strong; switchgear and ultra-high-voltage transformer backlog expanded YoY and the company was securing additional U.S. land/capacity. This is a direct C02 route because the product, backlog, capacity and margin bridge are visible.","evidence_source":"EV_C02_R1L122_LS_ELECTRIC_20250422_MIRAE_1Q25","evidence_source_url":"https://securities.miraeasset.com/bbs/download/2135699.pdf?attachmentId=2135699","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","margin_bridge","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":["positioning_overheat_after_large_MFE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":59.04,"MFE_90D_pct":93.51,"MFE_180D_pct":220.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.41,"MAE_90D_pct":-0.41,"MAE_180D_pct":-0.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-01-14","peak_price":554000.0,"drawdown_after_peak_pct":-10.2,"green_lateness_ratio":null,"green_lateness_reason":"not_applicable_or_no_prior_stage3_green_pair_in_this_case","four_b_local_peak_proximity":"overlay_if_fast_MFE_or_high_MAE","four_b_full_window_peak_proximity":"not_full_4B_without_non_price_thesis_break","four_b_timing_verdict":"local_4B_overlay_only","four_b_evidence_type":["positioning_overheat_after_large_MFE"],"four_c_protection_label":"not_applicable_at_entry","trigger_outcome_label":"direct_grid_power_backlog_margin_bridge_positive","current_profile_verdict":"current_profile_missed_structural_if_C02_waits_for_big_tech_named_customer_only","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_selected_stock_web_profile_or_no_overlap_with_selected_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_010120_2025-04-22_172600.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"hard_duplicate_key":"C02_POWER_GRID_DATACENTER_CAPEX|010120|Stage3-Yellow|2025-04-22","dedupe_key":"v12_strict|C02_POWER_GRID_DATACENTER_CAPEX|010120|Stage3-Yellow|2025-04-22|direct_switchgear_transformer_backlog_and_US_capex_expansion","positive_or_counterexample":"positive","case_type":"structural_success","residual_contribution":"allow_Yellow_when_switchgear_transformer_backlog_CAGR_and_capacity_expansion_are_visible"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L122_010120_20250422_LS_ELECTRIC_1Q25_BACKLOG_SWITCHGEAR_TRANSFORMER","trigger_id":"TRIG_C02_R1L122_010120_20250422_STAGE3Y","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":14,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":9,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":19,"margin_bridge_score":15,"revision_score":13,"relative_strength_score":9,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"allow_Yellow_when_switchgear_transformer_backlog_CAGR_and_capacity_expansion_are_visible","MFE_90D_pct":93.51,"MAE_90D_pct":-0.41,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural_if_C02_waits_for_big_tech_named_customer_only"}

{"row_type":"case","case_id":"C02_R1L122_006260_20250422_LS_HOLDCO_POWER_INFRA_PROXY_SUCCESS_WITH_DISCOUNT","symbol":"006260","company_name":"LS","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"LS_GROUP_POWER_INFRA_HOLDCO_PROXY_WITH_DIRECT_SUBSIDIARY_DISCOUNT","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_false_positive_if_holdco_proxy_gets_same_C02_score_as_direct_equipment_supplier","price_source":"Songdaiki/stock-web","notes":"LS holding-company exposure captured the same power-equipment rerating, but the evidence is subsidiary-level. C02 credit can exist, yet it should be capped below direct operating-company routes unless capital-allocation or NAV-realization evidence is present."}

{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C02_R1L122_006260_20250422_STAGE2A","case_id":"C02_R1L122_006260_20250422_LS_HOLDCO_POWER_INFRA_PROXY_SUCCESS_WITH_DISCOUNT","symbol":"006260","company_name":"LS","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"LS_GROUP_POWER_INFRA_HOLDCO_PROXY_WITH_DIRECT_SUBSIDIARY_DISCOUNT","sector":"industrial_power_grid_datacenter","primary_archetype":"C02_power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-22","entry_date":"2025-04-22","entry_price":118700.0,"evidence_available_at_that_date":"LS holding-company exposure captured the same power-equipment rerating, but the evidence is subsidiary-level. C02 credit can exist, yet it should be capped below direct operating-company routes unless capital-allocation or NAV-realization evidence is present.","evidence_source":"EV_C02_R1L122_LS_HOLDCO_20250422_SUBSIDIARY_POWER_BACKLOG","evidence_source_url":"https://securities.miraeasset.com/bbs/download/2135699.pdf?attachmentId=2135699","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["subsidiary_financial_visibility"],"stage4b_evidence_fields":["holding_company_discount","positioning_overheat_after_large_MFE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2025.csv","profile_path":"atlas/symbol_profiles/006/006260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":63.77,"MFE_90D_pct":85.34,"MFE_180D_pct":97.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.01,"MAE_90D_pct":-1.01,"MAE_180D_pct":-1.01,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-04","peak_price":235000.0,"drawdown_after_peak_pct":-26.77,"green_lateness_ratio":null,"green_lateness_reason":"not_applicable_or_no_prior_stage3_green_pair_in_this_case","four_b_local_peak_proximity":"overlay_if_fast_MFE_or_high_MAE","four_b_full_window_peak_proximity":"not_full_4B_without_non_price_thesis_break","four_b_timing_verdict":"local_4B_overlay_only","four_b_evidence_type":["holding_company_discount","positioning_overheat_after_large_MFE"],"four_c_protection_label":"not_applicable_at_entry","trigger_outcome_label":"holdco_proxy_worked_but_needs_discount","current_profile_verdict":"current_profile_false_positive_if_holdco_proxy_gets_same_C02_score_as_direct_equipment_supplier","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_selected_stock_web_profile_or_no_overlap_with_selected_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_006260_2025-04-22_118700.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"hard_duplicate_key":"C02_POWER_GRID_DATACENTER_CAPEX|006260|Stage2-Actionable|2025-04-22","dedupe_key":"v12_strict|C02_POWER_GRID_DATACENTER_CAPEX|006260|Stage2-Actionable|2025-04-22|holding_company_exposure_to_LS_Electric_LS_Cable_power_infra_backlog","positive_or_counterexample":"positive","case_type":"stage2_promote_candidate","residual_contribution":"allow_Stage2_Actionable_only_with_holdco_proxy_discount"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L122_006260_20250422_LS_HOLDCO_POWER_INFRA_PROXY_SUCCESS_WITH_DISCOUNT","trigger_id":"TRIG_C02_R1L122_006260_20250422_STAGE2A","symbol":"006260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":11,"margin_bridge_score":7,"revision_score":9,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":14,"margin_bridge_score":9,"revision_score":11,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"allow_Stage2_Actionable_only_with_holdco_proxy_discount","MFE_90D_pct":85.34,"MAE_90D_pct":-1.01,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_false_positive_if_holdco_proxy_gets_same_C02_score_as_direct_equipment_supplier"}

{"row_type":"case","case_id":"C02_R1L122_001440_20240618_TAIHAN_US_GRID_ORDER_LATE_REPRICE_COUNTER","symbol":"001440","company_name":"대한전선","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"EXTRA_HIGH_VOLTAGE_US_GRID_ORDER_WITH_LATE_REPRICE_4B_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_aligned","current_profile_verdict":"current_profile_false_positive_if_actual_order_automatically_upgrades_to_Yellow_after_reprice","price_source":"Songdaiki/stock-web","notes":"Taihan had actual U.S. power-grid contracts totaling KRW130bn and cumulative U.S. orders above KRW330bn in 2024. The order evidence is real, but the entry came after crowded cable rerating; price path shows low upside and large drawdown, so direct order alone needs local 4B context."}

{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C02_R1L122_001440_20240618_STAGE2A","case_id":"C02_R1L122_001440_20240618_TAIHAN_US_GRID_ORDER_LATE_REPRICE_COUNTER","symbol":"001440","company_name":"대한전선","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"EXTRA_HIGH_VOLTAGE_US_GRID_ORDER_WITH_LATE_REPRICE_4B_GUARD","sector":"industrial_power_grid_datacenter","primary_archetype":"C02_power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-18","entry_date":"2024-06-18","entry_price":15790.0,"evidence_available_at_that_date":"Taihan had actual U.S. power-grid contracts totaling KRW130bn and cumulative U.S. orders above KRW330bn in 2024. The order evidence is real, but the entry came after crowded cable rerating; price path shows low upside and large drawdown, so direct order alone needs local 4B context.","evidence_source":"EV_C02_R1L122_TAIHAN_20240618_YNA_US_GRID_ORDERS","evidence_source_url":"https://en.yna.co.kr/view/AEN20240618003100320","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["missing_margin_bridge","missing_FCF_conversion"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak","deep_MAE_after_order_headline"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv","profile_path":"atlas/symbol_profiles/001/001440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.44,"MFE_90D_pct":9.44,"MFE_180D_pct":9.44,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.44,"MAE_90D_pct":-34.96,"MAE_180D_pct":-36.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":17280.0,"drawdown_after_peak_pct":-42.13,"green_lateness_ratio":null,"green_lateness_reason":"not_applicable_or_no_prior_stage3_green_pair_in_this_case","four_b_local_peak_proximity":"overlay_if_fast_MFE_or_high_MAE","four_b_full_window_peak_proximity":"not_full_4B_without_non_price_thesis_break","four_b_timing_verdict":"local_4B_overlay_only","four_b_evidence_type":["positioning_overheat","price_only_local_peak","deep_MAE_after_order_headline"],"four_c_protection_label":"not_applicable_at_entry","trigger_outcome_label":"direct_order_but_bad_entry_local_4B","current_profile_verdict":"current_profile_false_positive_if_actual_order_automatically_upgrades_to_Yellow_after_reprice","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_selected_stock_web_profile_or_no_overlap_with_selected_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_001440_2024-06-18_15790.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"hard_duplicate_key":"C02_POWER_GRID_DATACENTER_CAPEX|001440|Stage2-Actionable|2024-06-18","dedupe_key":"v12_strict|C02_POWER_GRID_DATACENTER_CAPEX|001440|Stage2-Actionable|2024-06-18|actual_US_power_grid_contract_but_price_already_reflected","positive_or_counterexample":"counterexample","case_type":"failed_rerating","residual_contribution":"attach_local_4B_when_direct_order_headline_follows_large_sector_rerating_without_margin_bridge"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L122_001440_20240618_TAIHAN_US_GRID_ORDER_LATE_REPRICE_COUNTER","trigger_id":"TRIG_C02_R1L122_001440_20240618_STAGE2A","symbol":"001440","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":13,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":13,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":-4,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"attach_local_4B_when_direct_order_headline_follows_large_sector_rerating_without_margin_bridge","MFE_90D_pct":9.44,"MAE_90D_pct":-34.96,"score_return_alignment_label":"guardrail_aligned","current_profile_verdict":"current_profile_false_positive_if_actual_order_automatically_upgrades_to_Yellow_after_reprice"}

{"row_type":"case","case_id":"C02_R1L122_017510_20240801_SEMYUNG_HVDC_FITTINGS_PROXY_HIGH_MAE","symbol":"017510","company_name":"세명전기","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HVDC_TRANSMISSION_FITTINGS_OPTIONALITY_WITHOUT_CONFIRMED_MARGIN_BRIDGE","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_aligned","current_profile_verdict":"current_profile_false_positive_if_HVDC_component_vocabulary_is_promoted_to_Actionable","price_source":"Songdaiki/stock-web","notes":"Semyung had HVDC/transmission fittings vocabulary and AI-power-demand linkage, but the as-of source was theme/proxy-heavy. Without named project volume, backlog and margin conversion, this should remain Stage2-watch even if later power-grid attention resumes."}

{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C02_R1L122_017510_20240801_STAGE2","case_id":"C02_R1L122_017510_20240801_SEMYUNG_HVDC_FITTINGS_PROXY_HIGH_MAE","symbol":"017510","company_name":"세명전기","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HVDC_TRANSMISSION_FITTINGS_OPTIONALITY_WITHOUT_CONFIRMED_MARGIN_BRIDGE","sector":"industrial_power_grid_datacenter","primary_archetype":"C02_power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":6700.0,"evidence_available_at_that_date":"Semyung had HVDC/transmission fittings vocabulary and AI-power-demand linkage, but the as-of source was theme/proxy-heavy. Without named project volume, backlog and margin conversion, this should remain Stage2-watch even if later power-grid attention resumes.","evidence_source":"EV_C02_R1L122_SEMYUNG_20240801_FNNEWS_HVDC_AI_POWER","evidence_source_url":"https://www.fnnews.com/news/202408010941003670","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","power_grid_component_vocabulary"],"stage3_evidence_fields":["missing_named_customer","missing_backlog_conversion","missing_margin_bridge"],"stage4b_evidence_fields":["source_proxy_only","deep_90D_MAE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017510/2024.csv","profile_path":"atlas/symbol_profiles/017/017510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.85,"MFE_90D_pct":9.85,"MFE_180D_pct":29.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.61,"MAE_90D_pct":-43.28,"MAE_180D_pct":-43.28,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-04-23","peak_price":8670.0,"drawdown_after_peak_pct":-28.14,"green_lateness_ratio":null,"green_lateness_reason":"not_applicable_or_no_prior_stage3_green_pair_in_this_case","four_b_local_peak_proximity":"overlay_if_fast_MFE_or_high_MAE","four_b_full_window_peak_proximity":"not_full_4B_without_non_price_thesis_break","four_b_timing_verdict":"local_4B_overlay_only","four_b_evidence_type":["source_proxy_only","deep_90D_MAE"],"four_c_protection_label":"not_applicable_at_entry","trigger_outcome_label":"HVDC_component_proxy_high_MAE","current_profile_verdict":"current_profile_false_positive_if_HVDC_component_vocabulary_is_promoted_to_Actionable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_selected_stock_web_profile_or_no_overlap_with_selected_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_017510_2024-08-01_6700.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"hard_duplicate_key":"C02_POWER_GRID_DATACENTER_CAPEX|017510|Stage2|2024-08-01","dedupe_key":"v12_strict|C02_POWER_GRID_DATACENTER_CAPEX|017510|Stage2|2024-08-01|HVDC_grid_fittings_theme_from_AI_power_demand_without_order_margin_confirmation","positive_or_counterexample":"counterexample","case_type":"price_moved_without_evidence","residual_contribution":"keep_HVDC_fittings_proxy_at_Stage2_until_named_project_and_sales_conversion"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L122_017510_20240801_SEMYUNG_HVDC_FITTINGS_PROXY_HIGH_MAE","trigger_id":"TRIG_C02_R1L122_017510_20240801_STAGE2","symbol":"017510","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":11,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":-3,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59,"stage_label_after":"Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"keep_HVDC_fittings_proxy_at_Stage2_until_named_project_and_sales_conversion","MFE_90D_pct":9.85,"MAE_90D_pct":-43.28,"score_return_alignment_label":"guardrail_aligned","current_profile_verdict":"current_profile_false_positive_if_HVDC_component_vocabulary_is_promoted_to_Actionable"}

{"row_type":"case","case_id":"C02_R1L122_147830_20240717_CHERYONG_INDUSTRIAL_PRODUCT_IDENTITY_TRAP","symbol":"147830","company_name":"제룡산업","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSMISSION_DISTRIBUTION_MATERIAL_PRODUCT_IDENTITY_WITHOUT_DATACENTER_ORDER","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_aligned","current_profile_verdict":"current_profile_false_positive_if_power_component_identity_is_treated_like_transformer_backlog","price_source":"Songdaiki/stock-web","notes":"Jeeryong Industrial has transmission/distribution/underground equipment product identity, but the selected trigger family lacks a named data-center/grid customer, backlog or margin bridge. The price path collapses almost immediately, making it a clean C02 product-identity trap."}

{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C02_R1L122_147830_20240717_STAGE2","case_id":"C02_R1L122_147830_20240717_CHERYONG_INDUSTRIAL_PRODUCT_IDENTITY_TRAP","symbol":"147830","company_name":"제룡산업","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSMISSION_DISTRIBUTION_MATERIAL_PRODUCT_IDENTITY_WITHOUT_DATACENTER_ORDER","sector":"industrial_power_grid_datacenter","primary_archetype":"C02_power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":9230.0,"evidence_available_at_that_date":"Jeeryong Industrial has transmission/distribution/underground equipment product identity, but the selected trigger family lacks a named data-center/grid customer, backlog or margin bridge. The price path collapses almost immediately, making it a clean C02 product-identity trap.","evidence_source":"EV_C02_R1L122_CHERYONGIND_PRODUCT_CATALOG","evidence_source_url":"https://www.cheryongind.com/","stage2_evidence_fields":["power_grid_component_vocabulary","relative_strength"],"stage3_evidence_fields":["missing_named_order","missing_revenue_conversion","missing_margin_bridge"],"stage4b_evidence_fields":["source_proxy_only","immediate_peak_then_drawdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv","profile_path":"atlas/symbol_profiles/147/147830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.58,"MFE_90D_pct":3.58,"MFE_180D_pct":3.58,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-33.37,"MAE_90D_pct":-44.31,"MAE_180D_pct":-51.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":9560.0,"drawdown_after_peak_pct":-52.88,"green_lateness_ratio":null,"green_lateness_reason":"not_applicable_or_no_prior_stage3_green_pair_in_this_case","four_b_local_peak_proximity":"overlay_if_fast_MFE_or_high_MAE","four_b_full_window_peak_proximity":"not_full_4B_without_non_price_thesis_break","four_b_timing_verdict":"local_4B_overlay_only","four_b_evidence_type":["source_proxy_only","immediate_peak_then_drawdown"],"four_c_protection_label":"not_applicable_at_entry","trigger_outcome_label":"product_identity_proxy_bad_entry","current_profile_verdict":"current_profile_false_positive_if_power_component_identity_is_treated_like_transformer_backlog","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_selected_stock_web_profile_or_no_overlap_with_selected_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_147830_2024-07-17_9230.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"hard_duplicate_key":"C02_POWER_GRID_DATACENTER_CAPEX|147830|Stage2|2024-07-17","dedupe_key":"v12_strict|C02_POWER_GRID_DATACENTER_CAPEX|147830|Stage2|2024-07-17|transmission_distribution_material_identity_without_named_grid_datacenter_order","positive_or_counterexample":"counterexample","case_type":"failed_rerating","residual_contribution":"block_Yellow_for_component_identity_without_named_grid_datacenter_order_or_backlog"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L122_147830_20240717_CHERYONG_INDUSTRIAL_PRODUCT_IDENTITY_TRAP","trigger_id":"TRIG_C02_R1L122_147830_20240717_STAGE2","symbol":"147830","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":1,"revision_score":3,"relative_strength_score":10,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":-4,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"block_Yellow_for_component_identity_without_named_grid_datacenter_order_or_backlog","MFE_90D_pct":3.58,"MAE_90D_pct":-44.31,"score_return_alignment_label":"guardrail_aligned","current_profile_verdict":"current_profile_false_positive_if_power_component_identity_is_treated_like_transformer_backlog"}

{"row_type":"aggregate","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","trigger_count":5,"representative_trigger_count":5,"positive_case_count":2,"counterexample_count":3,"avg_MFE_90D_pct":40.34,"avg_MAE_90D_pct":-24.79,"avg_MFE_180D_pct":72.27,"avg_MAE_180D_pct":-26.51,"current_profile_error_count":5}

{"row_type":"shadow_weight","axis":"C02_DIRECT_GRID_DATACENTER_CAPEX_REQUIRES_NAMED_ORDER_BACKLOG_CAPA_OR_MARGIN_BRIDGE","scope":"canonical_archetype_specific","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","baseline_value":0,"tested_value":1,"delta":"+1 guardrail-specific, not production","reason":"Direct power-equipment order/backlog/capacity bridge produced high MFE, but cable/order headlines and product-identity proxies produced high MAE if entered after reprice or without margin bridge.","backtest_effect":"improves positive/counterexample split by separating LS Electric direct backlog from Taihan late order, Semyung HVDC proxy, and Jeeryong product-identity trap","trigger_ids":"TRIG_C02_R1L122_010120_20250422_STAGE3Y|TRIG_C02_R1L122_006260_20250422_STAGE2A|TRIG_C02_R1L122_001440_20240618_STAGE2A|TRIG_C02_R1L122_017510_20240801_STAGE2|TRIG_C02_R1L122_147830_20240717_STAGE2","calibration_usable_count":5,"new_independent_case_count":5,"counterexample_count":3,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}

{"row_type":"residual_contribution","round":"R1","loop":"122","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["direct_order_late_reprice_false_positive","holding_company_proxy_discount_needed","component_identity_proxy_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}

```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 2
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.


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
- Production scoring must not change unless explicitly promoted.


### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report accepted/rejected rows and new coverage.
10. Add tests that duplicate low-value loops cannot change weights.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 122
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C02 under-30 follow-up
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_followup_new_symbols_only; C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_customer_route; C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_followup_new_order_route; C11_BATTERY_ORDERBOOK_RERATING_followup_margin_FCF_bridge; R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_if_source_proxy_repair_needed
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md

- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json

- Evidence URLs are listed in section 9 and inside each trigger row.
