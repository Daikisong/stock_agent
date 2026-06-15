---
expected_v12_result_file: true
filename_pattern_pass: true
filename_matches_metadata: true
selected_round: R1
selected_loop: 140
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: mixed_C02_grid_datacenter_second_pass_order_margin_theme_split
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective: coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 5
reused_case_count: 0
calibration_usable_trigger_count: 5
representative_trigger_count: 5
positive_case_count: 2
counterexample_count: 3
four_b_case_count: 4
four_c_case_count: 0
current_profile_error_count: 5
do_not_propose_new_weight_delta: false
---

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_140_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
completed_round: R1
completed_loop: 140
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: mixed_C02_grid_datacenter_second_pass_order_margin_theme_split
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The loop tests residual errors after the broad global corrections: Stage2 bridge bonus, stricter Yellow/Green gates, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing. This file does not patch production scoring.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R1`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C02_POWER_GRID_DATACENTER_CAPEX`
- fine_archetype_id: `mixed_C02_grid_datacenter_second_pass_order_margin_theme_split`
- scope thesis: C02 should separate real grid/datacenter CAPEX order conversion from generic AI-power theme rallies. The practical gate is `named customer/order/backlog + delivery visibility + margin bridge`; without that, local price strength becomes Stage4B watch rather than Stage3.

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` lists C02 at 10 representative rows, still below the 30-row stability floor. The immediately prior session artifact in this chat already used C02 loop 139 with a different symbol set, so this loop uses `loop_140` and avoids the previous C02 symbols: `006340`, `033100`, `103590`, `267260`, `298040`.

Hard duplicate key checked: `canonical_archetype_id + symbol + trigger_type + entry_date`. This file uses five new symbols for C02 and five new trigger families.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
```

Schema interpretation used: MFE/MAE are computed from tradable raw OHLCV rows using max high / min low from entry through 30/90/180 tradable rows. All representative trigger rows below have the six required fields: `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`.

## 5. Historical Eligibility Gate

All five rows satisfy the historical gate:

- trigger date is before stock-web `max_date`.
- entry row exists in the tradable shard.
- at least 180 forward tradable rows exist.
- no corporate action candidate overlaps the 180D window.
- price basis is `tradable_raw`, unadjusted FinanceData/marcap.

## 6. Canonical Archetype Compression Map

| fine/deep sub-archetype | canonical mapping | interpretation |
|---|---|---|
| US data-center power equipment revenue mix revision | C02_POWER_GRID_DATACENTER_CAPEX | analyst/earnings bridge into real grid equipment demand |
| US power cable long-supply order bridge | C02_POWER_GRID_DATACENTER_CAPEX | named order/backlog visibility with cleaner 180D path |
| transformer IPO AI-demand theme | C02_POWER_GRID_DATACENTER_CAPEX | plausible structural demand but IPO/valuation high-MAE risk |
| legacy switchgear partner theme | C02_POWER_GRID_DATACENTER_CAPEX | old relationship + AI power theme without new order bridge |
| AI distribution-board data-center update | C02_POWER_GRID_DATACENTER_CAPEX | product capability narrative without repeat order/margin proof |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| C02_010120_20240701_us_growth_dc_power_equipment | 010120 | LS ELECTRIC | positive / high_mae_success | Stage2-Actionable 2024-07-01 | 2024-07-01 @ 204,500 | 34.23% | -38.29% | 48.41% | -38.29% | current_profile_4B_too_late |
| C02_001440_20241105_us_cable_long_supply_orders | 001440 | 대한전선 | positive / structural_success | Stage2-Actionable 2024-11-05 | 2024-11-05 @ 11,890 | 21.45% | -15.90% | 52.82% | -15.90% | current_profile_too_late |
| C02_062040_20240729_transformer_ipo_ai_demand | 062040 | 산일전기 | counterexample / failed_rerating | Stage2-Actionable 2024-07-15 | 2024-07-29 @ 50,200 | 37.85% | -44.12% | 66.33% | -44.12% | current_profile_false_positive |
| C02_017040_20240408_eaton_legacy_switchgear_theme | 017040 | 광명전기 | counterexample / price_moved_without_evidence | Stage4B 2024-04-08 | 2024-04-08 @ 2,715 | 22.28% | -40.55% | 22.28% | -53.96% | current_profile_false_positive |
| C02_388050_20240416_ai_distribution_board_datacenter_update | 388050 | 지투파워 | counterexample / price_moved_without_evidence | Stage4B 2024-04-16 | 2024-04-16 @ 8,590 | 48.31% | -35.16% | 48.31% | -42.26% | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

- positive_case_count: 2 (`010120`, `001440`)
- counterexample_count: 3 (`062040`, `017040`, `388050`)
- 4B_case_count: 4 (`010120`, `062040`, `017040`, `388050`)
- 4C_case_count: 0

C02 has a special trap: the same AI/data-center electricity story can be true at the industry level while still being too thin at the issuer level. The power grid narrative is the weather system; the individual stock still needs its own plumbing, valves, and pressure gauge: named order, delivery route, margin bridge, and clean balance-sheet/FCF translation.

## 9. Evidence Source Map

| symbol | evidence date | source | URL | evidence use |
|---:|---|---|---|---|
| 010120 | 2024-07-01 | MarketWatch / Daiwa market talk | https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067 | U.S. revenue mix/data-center demand revision |
| 001440 | 2024-11-05 | CEO Score Daily | https://ceoscoredaily.com/page/view/2024110514334544267 | U.S. cable long-supply order bridge |
| 062040 | 2024-07-15 | Chosun Biz | https://biz.chosun.com/stock/stock_general/2024/07/15/OBQJZFVBWFBC3NJS3VIN7BVZJQ/ | transformer IPO / AI-demand theme |
| 017040 | 2024-04-08 | Investing.com Korea / MoneyS relay | https://kr.investing.com/news/stock-market-news/article-1037427 | Eaton legacy switchgear theme without new order |
| 388050 | 2024-04-16 | G2Power press/news page | https://www.g2p.co.kr/news/pressView.html?page=3&s_word=&txtIdx=41 | AI distribution-board product/update narrative |

## 10. Price Data Source Map

| symbol | price shard path | profile path | corporate-action status |
|---:|---|---|---|
| 010120 | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv | atlas/symbol_profiles/010/010120.json | clean_180D_window / profile CA candidates: 1995-09-28, 1999-04-08, 1999-07-26, 2003-04-16 |
| 001440 | atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv|atlas/ohlcv_tradable_by_symbol_year/001/001440/2025.csv | atlas/symbol_profiles/001/001440.json | clean_180D_window / profile CA candidates: 2002-04-22, 2003-10-13, 2010-05-03, 2010-10-18, 2012-11-08, 2012-12-21, 2014-01-10, 2015-12-08, 2022-03-30, 2023-05-16, 2024-04-02 |
| 062040 | atlas/ohlcv_tradable_by_symbol_year/062/062040/2024.csv|atlas/ohlcv_tradable_by_symbol_year/062/062040/2025.csv | atlas/symbol_profiles/062/062040.json | clean_180D_window / profile CA candidates: none |
| 017040 | atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv|atlas/ohlcv_tradable_by_symbol_year/017/017040/2025.csv | atlas/symbol_profiles/017/017040.json | clean_180D_window / profile CA candidates: 2000-01-24, 2000-04-25, 2001-12-10 |
| 388050 | atlas/ohlcv_tradable_by_symbol_year/388/388050/2024.csv|atlas/ohlcv_tradable_by_symbol_year/388/388050/2025.csv | atlas/symbol_profiles/388/388050.json | clean_180D_window / profile CA candidates: 2022-08-10, 2022-09-06 |


## 11. Case-by-Case Trigger Grid

### 010120 LS ELECTRIC

Stage2 evidence was strong enough to flag the U.S. grid/datacenter revenue-mix route, but the trigger lacked a dated named hyperscale order at that moment. The current profile can still be too slow to add a local 4B watch because the path had both +48.41% 180D MFE and -38.29% MAE before the later full-window peak.

### 001440 대한전선

This is the cleanest positive in this loop. The U.S. cable long-supply order evidence had customer/geography/order duration content, and the price path showed +52.82% 180D MFE with only -15.90% 180D MAE. The calibrated profile can be too conservative if it waits for fully reported margin bridge before allowing Stage3-Yellow.

### 062040 산일전기

The transformer/AI-demand thesis was plausible, but entry at first tradable day after IPO produced -44.12% 30D/90D/180D MAE before the later +66.33% MFE. This is not a thesis rejection; it is a C02 high-MAE entry-quality counterexample requiring IPO/valuation local 4B watch.

### 017040 광명전기

The source linked AI power demand and Eaton data-center exposure to a legacy switchgear cooperation history. With no fresh order, delivery schedule, or margin bridge, this should be a Stage4B watch/blocked promotion row. The 180D path confirms it: +22.28% MFE but -53.96% MAE and -62.35% drawdown after the local peak.

### 388050 지투파워

The AI distribution-board product capability was real enough for narrative tracking, but not enough for Stage3 without repeat orders and margin/FCF bridge. The path had a fast +48.31% MFE but then -42.26% 180D MAE, which is exactly the C02 local-blowoff risk pattern.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | DD after peak | clean? |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| 010120 | 2024-07-01 | 204,500 | 34.23% | -29.10% | 34.23% | -38.29% | 48.41% | -38.29% | 2025-02-19 | 303,500 | -42.50% | clean_180D_window |
| 001440 | 2024-11-05 | 11,890 | 6.31% | -15.90% | 21.45% | -15.90% | 52.82% | -15.90% | 2025-06-25 | 18,170 | -16.35% | clean_180D_window |
| 062040 | 2024-07-29 | 50,200 | 22.11% | -44.12% | 37.85% | -44.12% | 66.33% | -44.12% | 2025-01-15 | 83,500 | -48.08% | clean_180D_window |
| 017040 | 2024-04-08 | 2,715 | 22.28% | -13.26% | 22.28% | -40.55% | 22.28% | -53.96% | 2024-05-08 | 3,320 | -62.35% | clean_180D_window |
| 388050 | 2024-04-16 | 8,590 | 48.31% | -8.03% | 48.31% | -35.16% | 48.31% | -42.26% | 2024-05-29 | 12,740 | -61.07% | clean_180D_window |


## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely behavior | actual path | residual verdict |
|---:|---|---|---|
| 010120 | allows Stage2/Yellow on revision and sector strength, but local 4B may come late | high MFE and high MAE | current_profile_4B_too_late |
| 001440 | may wait too long for realized margin bridge | strong 180D MFE with contained MAE | current_profile_too_late |
| 062040 | may over-credit transformer IPO theme and relative strength | severe early MAE despite later MFE | current_profile_false_positive |
| 017040 | should block price/theme row; if not, false positive | local MFE then deep drawdown | current_profile_false_positive |
| 388050 | product narrative can be over-credited without repeat order | fast MFE but deep 90/180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is assigned in this loop. Green lateness ratio is therefore `not_applicable`. The stress point is the Stage2/Stage3-Yellow boundary:

- 대한전선 shows that named U.S. order/backlog evidence can justify a faster Yellow unlock even before fully reported margin appears.
- 산일전기, 광명전기, 지투파워 show that industry-level AI-grid plausibility plus price strength is not enough for Yellow.
- LS ELECTRIC sits between the two: directionally correct but entry risk demands 4B watch before a full Green unlock.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence | local peak relation | full-window relation | verdict |
|---:|---|---|---|---|
| 010120 | valuation / positioning / high MAE | local overheat before Aug-Sep drawdown | later full-window peak in 2025 | full 4B should require non-price slowdown; local watch should be earlier |
| 062040 | IPO positioning / valuation | IPO entry immediately exposed to -44% MAE | later full-window peak after recovery | price-only local 4B watch was needed, not hard 4C |
| 017040 | legacy partner theme, no new order | May 2024 local peak near theme spike | no larger full-window peak | good Stage4B block candidate |
| 388050 | smallcap theme, no repeat order | May 2024 local peak | no larger full-window peak | good Stage4B block candidate |

## 16. 4C Protection Audit

No hard 4C row is proposed. None of the five cases shows a dated contract cancellation, accounting break, or thesis evidence broken at trigger. The correct route for the weak cases is Stage4B watch / Stage2 block, not hard 4C.

## 17. Sector-Specific Rule Candidate

```text
L1_C02_GRID_DATACENTER_NAMED_ORDER_MARGIN_BRIDGE_AND_THEME_BLOWOFF_SPLIT
```

Rule interpretation: in L1 power-grid/datacenter names, Stage3-Yellow can open earlier for named order/backlog/customer geography evidence when the 90D/180D MAE profile is contained. Generic AI/data-center power-demand news, old partnership memories, or IPO narratives should be capped as Stage2-watch or Stage4B unless they contain fresh order, delivery, capacity lock, or margin bridge evidence.

## 18. Canonical-Archetype Rule Candidate

```text
C02_NAMED_ORDER_DELIVERY_MARGIN_BRIDGE_GATE_WITH_LOCAL_4B_THEME_CAP
```

Canonical rule effect:

- increase weight on `contract_score`, `backlog_visibility_score`, `customer_quality_score`, and `margin_bridge_score` when a named order/delivery path exists;
- cap `relative_strength_score` and `valuation_repricing_score` when evidence is only industry-level AI-grid demand;
- allow `local_4b_watch_guard` for fast-MFE/high-MAE names without treating them as hard 4C.

## 19. Before / After Backtest Comparison

| profile | eligible cases | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 5 | 32.82% | -34.80% | 47.63% | -38.91% | 0.60 | directionally good but high-MAE false positives remain |
| P0b e2r_2_0_baseline_reference | 5 | 32.82% | -34.80% | 47.63% | -38.91% | 0.80 | over-credits relative strength/theme |
| P1 sector_specific_candidate_profile | 2 | 27.84% | -27.09% | 50.61% | -27.09% | 0.20 | improves MAE by blocking theme-only cases |
| P2 canonical_archetype_candidate_profile | 2 | 27.84% | -27.09% | 50.61% | -27.09% | 0.20 | best C02-specific split |
| P3 counterexample_guard_profile | 2 | 27.84% | -27.09% | 50.61% | -27.09% | 0.00 | stricter but may miss early LS-style structural signal |

## 20. Score-Return Alignment Matrix

| symbol | weighted before | stage before | weighted after | stage after | alignment |
|---:|---:|---|---:|---|---|
| 010120 | 72 | Stage3-Yellow | 68 | Stage2-Actionable | direction right, entry risk too high without local 4B watch |
| 001440 | 73 | Stage2-Actionable | 77 | Stage3-Yellow | positive evidence translated into strong 180D MFE with contained MAE |
| 062040 | 76 | Stage3-Yellow | 61 | Stage2-Actionable | theme was structurally plausible but entry timing required IPO/high-MAE guard |
| 017040 | 64 | Stage2 | 48 | Stage4B | MFE existed but MAE and post-peak drawdown dominated without new contract evidence |
| 388050 | 67 | Stage2-Actionable | 56 | Stage4B | short-window upside did not validate Stage3 because 90D/180D drawdown was severe |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | mixed_C02_grid_datacenter_second_pass_order_margin_theme_split | 2 | 3 | 4 | 0 | 5 | 0 | 5 | 5 | 5 | L1_C02_GRID_DATACENTER_NAMED_ORDER_MARGIN_BRIDGE_AND_THEME_BLOWOFF_SPLIT | C02_NAMED_ORDER_DELIVERY_MARGIN_BRIDGE_GATE_WITH_LOCAL_4B_THEME_CAP | ledger 10 -> 15; session-adjusted 15 -> 20 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_4B_too_late
  - current_profile_too_late
new_axis_proposed:
  - C02_NAMED_ORDER_DELIVERY_MARGIN_BRIDGE_GATE_WITH_LOCAL_4B_THEME_CAP
existing_axis_strengthened:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
existing_axis_weakened: []
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L1_C02_GRID_DATACENTER_NAMED_ORDER_MARGIN_BRIDGE_AND_THEME_BLOWOFF_SPLIT
canonical_archetype_rule_candidate: C02_NAMED_ORDER_DELIVERY_MARGIN_BRIDGE_GATE_WITH_LOCAL_4B_THEME_CAP
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- actual Stock-Web 1D tradable OHLC rows for all entries;
- 30D/90D/180D MFE/MAE;
- entry-date availability and 180 forward trading-day sufficiency;
- no 180D corporate-action contamination from profile candidate dates;
- canonical/round/sector consistency.

Not validated:

- live/current valuation after stock-web `max_date`;
- production scoring code behavior;
- brokerage or live scan state;
- adjustment for dividends/splits beyond Stock-Web raw/unadjusted caveat.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_named_order_margin_bridge_gate,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Require named order/backlog or customer revenue bridge before Stage3-Yellow; cap legacy/generic AI data-center theme as Stage4B watch.","Improves distinction between 대한전선/LS ELECTRIC positives and 산일전기/광명전기/지투파워 high-MAE theme entries.","TRG_C02_010120_20240701_us_growth_dc_power_equipment|TRG_C02_001440_20241105_us_cable_long_supply_orders|TRG_C02_062040_20240729_transformer_ipo_ai_demand|TRG_C02_017040_20240408_eaton_legacy_switchgear_theme|TRG_C02_388050_20240416_ai_distribution_board_datacenter_update",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C02_010120_20240701_us_growth_dc_power_equipment","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"direction right, entry risk too high without local 4B watch","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"structural_positive_but_high_MAE_requires_4B_watch"}
{"row_type":"trigger","trigger_id":"TRG_C02_010120_20240701_us_growth_dc_power_equipment","case_id":"C02_010120_20240701_us_growth_dc_power_equipment","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":204500.0,"evidence_available_at_that_date":"Daiwa/MarketWatch note: U.S. operations could rise toward 20% of 2024 revenue from below 5% in 2022, driven by data-center construction, renewables and EV value-chain demand.","evidence_source":"MarketWatch / Daiwa market talk, 2024-07-01","evidence_source_url":"https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067","stage2_evidence_fields":["US revenue growth opportunity","data-center construction boom","electrical-equipment demand route","analyst revision signal"],"stage3_evidence_fields":["US mix expansion visible but named hyperscale order not yet public at trigger","margin bridge partially supported by earnings trajectory"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.23,"MFE_90D_pct":34.23,"MFE_180D_pct":48.41,"MAE_30D_pct":-29.1,"MAE_90D_pct":-38.29,"MAE_180D_pct":-38.29,"peak_date":"2025-02-19","peak_price":303500.0,"drawdown_after_peak_pct":-42.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.7,"four_b_full_window_peak_proximity":0.35,"four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"trigger_outcome_label":"structural_positive_but_high_MAE_requires_4B_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":["1995-09-28","1999-04-08","1999-07-26","2003-04-16"],"same_entry_group_id":"SEG_C02_010120_20240701_us_growth_dc_power_equipment","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_010120_20240701_us_growth_dc_power_equipment","trigger_id":"TRG_C02_010120_20240701_us_growth_dc_power_equipment","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":45,"margin_bridge_score":50,"revision_score":78,"relative_strength_score":82,"customer_quality_score":60,"policy_or_regulatory_score":30,"valuation_repricing_score":72,"execution_risk_score":45,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":72,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":50,"backlog_visibility_score":48,"margin_bridge_score":52,"revision_score":74,"relative_strength_score":70,"customer_quality_score":62,"policy_or_regulatory_score":30,"valuation_repricing_score":58,"execution_risk_score":58,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 shadow gate rewards named order/backlog-to-margin bridge and caps generic data-center theme or local price blowoff without fresh order evidence.","MFE_90D_pct":34.23,"MAE_90D_pct":-38.29,"score_return_alignment_label":"direction right, entry risk too high without local 4B watch","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C02_001440_20241105_us_cable_long_supply_orders","symbol":"001440","company_name":"대한전선","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive evidence translated into strong 180D MFE with contained MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"cleaner_order_bridge_structural_success"}
{"row_type":"trigger","trigger_id":"TRG_C02_001440_20241105_us_cable_long_supply_orders","case_id":"C02_001440_20241105_us_cable_long_supply_orders","symbol":"001440","company_name":"대한전선","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-05","entry_date":"2024-11-05","entry_price":11890.0,"evidence_available_at_that_date":"U.S. cable long-supply and East/West U.S. cable projects expanded 2024 U.S. order intake above prior North America record, giving a cleaner order/backlog bridge than generic power-grid theme.","evidence_source":"CEO Score Daily, 2024-11-05","evidence_source_url":"https://ceoscoredaily.com/page/view/2024110514334544267","stage2_evidence_fields":["US power cable long supply project","named regional cable projects","order intake visibility","grid/cable demand route"],"stage3_evidence_fields":["order-to-revenue bridge improving","customer geography repeatability","cleaner backlog visibility than theme peers"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv|atlas/ohlcv_tradable_by_symbol_year/001/001440/2025.csv","profile_path":"atlas/symbol_profiles/001/001440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.31,"MFE_90D_pct":21.45,"MFE_180D_pct":52.82,"MAE_30D_pct":-15.9,"MAE_90D_pct":-15.9,"MAE_180D_pct":-15.9,"peak_date":"2025-06-25","peak_price":18170.0,"drawdown_after_peak_pct":-16.35,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_evidence_type":[],"trigger_outcome_label":"cleaner_order_bridge_structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":["2002-04-22","2003-10-13","2010-05-03","2010-10-18","2012-11-08","2012-12-21","2014-01-10","2015-12-08","2022-03-30","2023-05-16","2024-04-02"],"same_entry_group_id":"SEG_C02_001440_20241105_us_cable_long_supply_orders","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_001440_20241105_us_cable_long_supply_orders","trigger_id":"TRG_C02_001440_20241105_us_cable_long_supply_orders","symbol":"001440","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":47,"revision_score":58,"relative_strength_score":55,"customer_quality_score":70,"policy_or_regulatory_score":35,"valuation_repricing_score":48,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":76,"backlog_visibility_score":68,"margin_bridge_score":54,"revision_score":60,"relative_strength_score":58,"customer_quality_score":74,"policy_or_regulatory_score":35,"valuation_repricing_score":50,"execution_risk_score":32,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 shadow gate rewards named order/backlog-to-margin bridge and caps generic data-center theme or local price blowoff without fresh order evidence.","MFE_90D_pct":21.45,"MAE_90D_pct":-15.9,"score_return_alignment_label":"positive evidence translated into strong 180D MFE with contained MAE","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C02_062040_20240729_transformer_ipo_ai_demand","symbol":"062040","company_name":"산일전기","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"theme was structurally plausible but entry timing required IPO/high-MAE guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"eventual_MFE_but_initial_high_MAE_IPO_theme_counterexample"}
{"row_type":"trigger","trigger_id":"TRG_C02_062040_20240729_transformer_ipo_ai_demand","case_id":"C02_062040_20240729_transformer_ipo_ai_demand","symbol":"062040","company_name":"산일전기","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-15","entry_date":"2024-07-29","entry_price":50200.0,"evidence_available_at_that_date":"IPO narrative emphasized transformer supercycle, AI/data-center demand and 2024 order target, but at the first tradable entry the order-to-margin evidence was still untested as public equity.","evidence_source":"Chosun Biz, 2024-07-15","evidence_source_url":"https://biz.chosun.com/stock/stock_general/2024/07/15/OBQJZFVBWFBC3NJS3VIN7BVZJQ/","stage2_evidence_fields":["transformer supercycle narrative","AI/data-center demand route","order target disclosed in IPO narrative"],"stage3_evidence_fields":["public-equity margin bridge not yet confirmed at listing","post-listing repeat-order evidence pending"],"stage4b_evidence_fields":["IPO_positioning_overheat","valuation_blowoff","execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/062/062040/2024.csv|atlas/ohlcv_tradable_by_symbol_year/062/062040/2025.csv","profile_path":"atlas/symbol_profiles/062/062040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.11,"MFE_90D_pct":37.85,"MFE_180D_pct":66.33,"MAE_30D_pct":-44.12,"MAE_90D_pct":-44.12,"MAE_180D_pct":-44.12,"peak_date":"2025-01-15","peak_price":83500.0,"drawdown_after_peak_pct":-48.08,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.7,"four_b_full_window_peak_proximity":0.35,"four_b_evidence_type":["IPO_positioning_overheat","valuation_blowoff","execution_risk"],"trigger_outcome_label":"eventual_MFE_but_initial_high_MAE_IPO_theme_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":[],"same_entry_group_id":"SEG_C02_062040_20240729_transformer_ipo_ai_demand","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_062040_20240729_transformer_ipo_ai_demand","trigger_id":"TRG_C02_062040_20240729_transformer_ipo_ai_demand","symbol":"062040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":58,"margin_bridge_score":38,"revision_score":58,"relative_strength_score":88,"customer_quality_score":55,"policy_or_regulatory_score":25,"valuation_repricing_score":78,"execution_risk_score":68,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":52,"margin_bridge_score":35,"revision_score":50,"relative_strength_score":62,"customer_quality_score":48,"policy_or_regulatory_score":25,"valuation_repricing_score":55,"execution_risk_score":75,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":61,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 shadow gate rewards named order/backlog-to-margin bridge and caps generic data-center theme or local price blowoff without fresh order evidence.","MFE_90D_pct":37.85,"MAE_90D_pct":-44.12,"score_return_alignment_label":"theme was structurally plausible but entry timing required IPO/high-MAE guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C02_017040_20240408_eaton_legacy_switchgear_theme","symbol":"017040","company_name":"광명전기","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"MFE existed but MAE and post-peak drawdown dominated without new contract evidence","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"price_theme_4B_counterexample"}
{"row_type":"trigger","trigger_id":"TRG_C02_017040_20240408_eaton_legacy_switchgear_theme","case_id":"C02_017040_20240408_eaton_legacy_switchgear_theme","symbol":"017040","company_name":"광명전기","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-04-08","entry_date":"2024-04-08","entry_price":2715.0,"evidence_available_at_that_date":"Theme article linked AI power demand and Eaton data-center exposure to an old switchgear partnership history, but did not show a new order, backlog, delivery schedule or margin bridge for 광명전기.","evidence_source":"Investing.com Korea / MoneyS relay, 2024-04-08","evidence_source_url":"https://kr.investing.com/news/stock-market-news/article-1037427","stage2_evidence_fields":["old Eaton switchgear cooperation history","AI data-center power-demand theme"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only","legacy_relationship_theme","no_new_order_or_margin_bridge","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv|atlas/ohlcv_tradable_by_symbol_year/017/017040/2025.csv","profile_path":"atlas/symbol_profiles/017/017040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.28,"MFE_90D_pct":22.28,"MFE_180D_pct":22.28,"MAE_30D_pct":-13.26,"MAE_90D_pct":-40.55,"MAE_180D_pct":-53.96,"peak_date":"2024-05-08","peak_price":3320.0,"drawdown_after_peak_pct":-62.35,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.2,"four_b_evidence_type":["price_only","legacy_relationship_theme","no_new_order_or_margin_bridge","positioning_overheat"],"trigger_outcome_label":"price_theme_4B_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":["2000-01-24","2000-04-25","2001-12-10"],"same_entry_group_id":"SEG_C02_017040_20240408_eaton_legacy_switchgear_theme","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_017040_20240408_eaton_legacy_switchgear_theme","trigger_id":"TRG_C02_017040_20240408_eaton_legacy_switchgear_theme","symbol":"017040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":10,"revision_score":30,"relative_strength_score":78,"customer_quality_score":30,"policy_or_regulatory_score":20,"valuation_repricing_score":70,"execution_risk_score":70,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":64,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":20,"relative_strength_score":45,"customer_quality_score":25,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":82,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":48,"stage_label_after":"Stage4B","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 shadow gate rewards named order/backlog-to-margin bridge and caps generic data-center theme or local price blowoff without fresh order evidence.","MFE_90D_pct":22.28,"MAE_90D_pct":-40.55,"score_return_alignment_label":"MFE existed but MAE and post-peak drawdown dominated without new contract evidence","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C02_388050_20240416_ai_distribution_board_datacenter_update","symbol":"388050","company_name":"지투파워","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"short-window upside did not validate Stage3 because 90D/180D drawdown was severe","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"fast_MFE_high_MAE_theme_counterexample"}
{"row_type":"trigger","trigger_id":"TRG_C02_388050_20240416_ai_distribution_board_datacenter_update","case_id":"C02_388050_20240416_ai_distribution_board_datacenter_update","symbol":"388050","company_name":"지투파워","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"mixed_C02_grid_datacenter_second_pass_order_margin_theme_split","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-04-16","entry_date":"2024-04-16","entry_price":8590.0,"evidence_available_at_that_date":"Company/news item described AI distribution-board upgrade and prior data-center delivery, but the trigger did not contain fresh named order size, repeat customer conversion, or margin/FCF bridge.","evidence_source":"G2Power company press/news page, 2024-04-16","evidence_source_url":"https://www.g2p.co.kr/news/pressView.html?page=3&s_word=&txtIdx=41","stage2_evidence_fields":["AI distribution-board product capability","data-center customer requirement response","NEP/AI+ certification narrative"],"stage3_evidence_fields":["fresh recurring order bridge missing","margin bridge missing"],"stage4b_evidence_fields":["price_only","theme_positioning_overheat","smallcap_liquidity_MAE_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/388/388050/2024.csv|atlas/ohlcv_tradable_by_symbol_year/388/388050/2025.csv","profile_path":"atlas/symbol_profiles/388/388050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":48.31,"MFE_90D_pct":48.31,"MFE_180D_pct":48.31,"MAE_30D_pct":-8.03,"MAE_90D_pct":-35.16,"MAE_180D_pct":-42.26,"peak_date":"2024-05-29","peak_price":12740.0,"drawdown_after_peak_pct":-61.07,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.2,"four_b_evidence_type":["price_only","theme_positioning_overheat","smallcap_liquidity_MAE_risk"],"trigger_outcome_label":"fast_MFE_high_MAE_theme_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":["2022-08-10","2022-09-06"],"same_entry_group_id":"SEG_C02_388050_20240416_ai_distribution_board_datacenter_update","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_388050_20240416_ai_distribution_board_datacenter_update","trigger_id":"TRG_C02_388050_20240416_ai_distribution_board_datacenter_update","symbol":"388050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":35,"relative_strength_score":85,"customer_quality_score":38,"policy_or_regulatory_score":45,"valuation_repricing_score":72,"execution_risk_score":65,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":36,"backlog_visibility_score":30,"margin_bridge_score":18,"revision_score":28,"relative_strength_score":55,"customer_quality_score":36,"policy_or_regulatory_score":45,"valuation_repricing_score":50,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":56,"stage_label_after":"Stage4B","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 shadow gate rewards named order/backlog-to-margin bridge and caps generic data-center theme or local price blowoff without fresh order evidence.","MFE_90D_pct":48.31,"MAE_90D_pct":-35.16,"score_return_alignment_label":"short-window upside did not validate Stage3 because 90D/180D drawdown was severe","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R1","loop":"140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["current_profile_false_positive","current_profile_4B_too_late","current_profile_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 4
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

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

```yaml
completed_round: R1
completed_loop: 140
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
next_recommended_archetypes:
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Evidence URLs are embedded in the trigger JSONL rows.
