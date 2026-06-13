# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

```text
research_file = e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R1
selected_loop = 125
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = mixed_c02_power_grid_datacenter_capex_leaf_set
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Execution Contract

This MD follows the v12 stock-web historical calibration prompt. It is not a live stock discovery note, not investment advice, not an auto-trading design, and not a `stock_agent` source-code patch. The sole purpose is to add C02 residual calibration rows using actual `Songdaiki/stock-web` 1D OHLCV shards.

## 1. Price Atlas Confirmation

```text
primary_price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

Manifest and schema references checked:

- `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json`
- `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json`

All MFE/MAE values below use close-price entry and high/low path windows from `entry_date` through the requested number of tradable rows. Raw/unadjusted OHLC means corporate-action overlap is blocked by default.

## 2. Coverage-Index Selection

The latest No-Repeat Index shows C02 as the first Priority 0 archetype:

```text
C02_POWER_GRID_DATACENTER_CAPEX rows = 10
need_to_30 = 20
need_to_50 = 40
research focus = power grid / data-center CAPEX, backlog, CAPA lock, ASP, delivery visibility
```

Therefore the selected target is:

```text
selected_round = R1
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
```

This is archetype-first selection, not sequential R1→R13 cycling.

## 3. No-Repeat / Novelty Check

Known C02 top-covered symbols in the latest index include `000500`, `001440`, `006260`, `010120`, `017510`, `024840`. This run deliberately uses a mixed design:

- New C02 symbols: `267260`, `298040`, `006340`.
- Soft-reuse symbol with a new failure trigger family: `024840`.
- Exact duplicate key avoided: no reused `canonical_archetype_id + symbol + trigger_type + entry_date` key is intentionally repeated.

Novelty objective:

```text
new_symbol_bonus = used for 267260 / 298040 / 006340
new_trigger_family_bonus = used for 024840 copper-AI-powergrid theme blowoff
counterexample_gap_bonus = used for 024840 / 006340
missing_4b_path_bonus = used for price-only cable/copper theme rows
```

## 4. Archetype Definition

C02 is not “anything that goes up when power-grid headlines appear.” C02 requires a path from AI/data-center/grid CAPEX into company-level economic evidence:

```text
CAPEX / grid demand -> order or backlog -> capacity or delivery visibility -> ASP/margin/revision bridge -> durable return path
```

The negative mirror image is:

```text
copper / AI / electric-grid keyword -> small-cap theme price run -> no company-specific backlog bridge -> local MFE spike -> deep MAE / post-peak drawdown
```

## 5. Case Set Summary

| ticker | company | role | trigger_type | trigger_date | entry_date | entry_price | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | 180D close ret | CA status | profile error |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 267260 | HD현대일렉트릭 | positive | Stage2-Actionable | 2024-02-16 | 2024-02-19 | 123,600 | 49.68/-5.34 | 161.73/-5.34 | 234.55/-5.34 | 185.6 | clean_180D | false |
| 298040 | 효성중공업 | positive | Stage2-Actionable | 2025-04-29 | 2025-04-30 | 489,500 | 62.61/-0.31 | 186.01/-0.31 | 407.25/-0.31 | 378.86 | clean_180D | true |
| 024840 | KBI메탈 | counterexample | Stage4B | 2024-04-12 | 2024-04-15 | 2,130 | 122.77/-14.08 | 122.77/-14.08 | 122.77/-21.74 | -1.17 | clean_180D | true |
| 006340 | 대원전선 | counterexample | Stage4B | 2024-05-14 | 2024-05-16 | 4,910 | 3.26/-33.1 | 3.26/-48.07 | 3.26/-55.09 | -30.55 | clean_180D | true |
| 006340 | 대원전선 | narrative_overlay | Stage2 | 2024-04-16 | 2024-04-17 | 2,450 | 122.45/-10.61 | 122.45/-10.61 | 122.45/-10.61 | 62.86 | clean_180D | false |


## 6. Case 1 — HD현대일렉트릭 / Backlog-CAPA-Datacenter Positive

```text
case_id = C02_R1_L125_267260_20240219_BACKLOG_CAPA_DATACENTER_POSITIVE
ticker = 267260
company = HD현대일렉트릭
trigger_date = 2024-02-16
entry_date = 2024-02-19
entry_price = 123600
trigger_type = Stage2-Actionable
case_role = positive
fine_archetype_id = GRID_EQUIPMENT_US_DATACENTER_CAPEX_BACKLOG_CAPA_LOCK
```

Evidence:

- Mirae Asset report, 2024-02-16: `https://securities.miraeasset.com/bbs/download/2122467.pdf?attachmentId=2122467`
- YNA, 2023-12-01 Silicon Valley Power transformer order: `https://en.yna.co.kr/view/AEN20231201006600320`

Interpretation: this row is C02-positive because the evidence has non-price bridge: North American grid/utility order visibility, transformer shortage, delivery visibility, and analyst-level valuation/fundamental bridge. The 180D path confirms the stock did not merely produce a local pop; it produced a large 90D and 180D MFE with shallow early MAE.

Price path:

```json
{"MFE_30D_pct": 49.68, "MAE_30D_pct": -5.34, "MFE_90D_pct": 161.73, "MAE_90D_pct": -5.34, "MFE_180D_pct": 234.55, "MAE_180D_pct": -5.34, "peak_date_180D": "2024-11-12", "drawdown_after_peak_180D_pct": -15.36, "close_return_180D_pct": 185.6}
```

## 7. Case 2 — 효성중공업 / Overseas Backlog-Margin Mix Positive

```text
case_id = C02_R1_L125_298040_20250430_US_EU_ORDER_MARGIN_POSITIVE
ticker = 298040
company = 효성중공업
trigger_date = 2025-04-29
entry_date = 2025-04-30
entry_price = 489500
trigger_type = Stage2-Actionable
case_role = positive
fine_archetype_id = TRANSFORMER_US_EU_ORDER_BACKLOG_MARGIN_MIX
```

Evidence:

- Hankyung, 2025-04-29: `https://www.hankyung.com/article/2025042921486`
- BusinessPost, 2025-04-29: `https://www.businesspost.co.kr/BP?command=article_view&num=393218`

Interpretation: this row strengthens C02 because overseas order share, high-voltage transformer demand, backlog margin mix, and expected OP growth form an explicit bridge. It also highlights a residual current-profile risk: waiting only for already-reported margin can make C02 positive recognition too late.

Price path:

```json
{"MFE_30D_pct": 62.61, "MAE_30D_pct": -0.31, "MFE_90D_pct": 186.01, "MAE_90D_pct": -0.31, "MFE_180D_pct": 407.25, "MAE_180D_pct": -0.31, "peak_date_180D": "2025-11-04", "drawdown_after_peak_180D_pct": -30.29, "close_return_180D_pct": 378.86}
```

## 8. Case 3 — KBI메탈 / Copper-AI-Powergrid Theme 4B Counterexample

```text
case_id = C02_R1_L125_024840_20240415_COPPER_AI_THEME_4B_COUNTER
ticker = 024840
company = KBI메탈
trigger_date = 2024-04-12
entry_date = 2024-04-15
entry_price = 2130
trigger_type = Stage4B
case_role = counterexample
fine_archetype_id = CABLE_MATERIAL_COPPER_AI_POWERGRID_THEME_BLOWOFF
```

Evidence:

- Investing.com Korea, 2024-04-12: `https://kr.investing.com/news/stock-market-news/article-1040411`
- TheBigData, 2024-04-15: `https://www.thebigdata.co.kr/view.php?ud=202404150327391657cd1e7f0bdf_23`

Interpretation: the row is not a simple “bad case” because the local MFE was large. It is exactly the C02 failure pattern that the engine must not confuse with a clean grid CAPEX winner. The source family is copper/AI/power-grid theme, not explicit company backlog/CAPA/margin conversion. The post-peak drawdown makes it a local 4B watch row, not a Stage2-Actionable positive.

Price path:

```json
{"MFE_30D_pct": 122.77, "MAE_30D_pct": -14.08, "MFE_90D_pct": 122.77, "MAE_90D_pct": -14.08, "MFE_180D_pct": 122.77, "MAE_180D_pct": -21.74, "peak_date_180D": "2024-05-21", "drawdown_after_peak_180D_pct": -64.87, "close_return_180D_pct": -1.17}
```

## 9. Case 4 — 대원전선 / Power Supercycle Blowoff + Block-Deal Overhang Counterexample

```text
case_id = C02_R1_L125_006340_20240516_POWER_SUPERCYCLE_BLOCKDEAL_COUNTER
ticker = 006340
company = 대원전선
trigger_date = 2024-05-14
entry_date = 2024-05-16
entry_price = 4910
trigger_type = Stage4B
case_role = counterexample
fine_archetype_id = CABLE_POWER_SUPERCYCLE_OVERHANG_BLOWOFF
```

Evidence:

- Mirae Asset news digest, 2024-06-27: `https://securities.miraeasset.com/bbs/download/2129191.pdf?attachmentId=2129191`
- TheBigData, 2024-04-17 block-deal/overhang report: `https://www.thebigdata.co.kr/view.php?ud=202404170652483904cd1e7f0bdf_23`
- Hankyung, 2024-04-16 block deal: `https://www.hankyung.com/article/2024041634976`

Interpretation: this is the cleanest C02 counterexample in the set. The stock had already become a “power supercycle” proxy after a dramatic run, while shareholder block-sale/overhang evidence appeared. The forward 30/90/180D path shows minimal MFE and very large MAE, so the correct classification is local/full 4B risk watch, not new Stage2.

Price path:

```json
{"MFE_30D_pct": 3.26, "MAE_30D_pct": -33.1, "MFE_90D_pct": 3.26, "MAE_90D_pct": -48.07, "MFE_180D_pct": 3.26, "MAE_180D_pct": -55.09, "peak_date_180D": "2024-05-16", "drawdown_after_peak_180D_pct": -56.51, "close_return_180D_pct": -30.55}
```

## 10. Overlay Case — 대원전선 Early Block-Deal Warning

```text
case_id = C02_R1_L125_006340_20240417_BLOCKDEAL_EARLY_WARNING_OVERLAY
ticker = 006340
trigger_date = 2024-04-16
entry_date = 2024-04-17
trigger_type = Stage2
aggregate_group_role = non_representative_overlay
dedupe_for_aggregate = false
calibration_usable = false
reason = non_representative_overlay
```

This overlay is retained because it explains why the later May blowoff should not be read as a clean C02 positive. The early block-deal warning appeared before the theme continued upward. The overlay is not counted in aggregate to avoid double-counting the same symbol/failure family.

## 11. Corporate Action / Profile Check

| ticker | profile checked | 180D corporate-action overlap | decision |
|---|---|---|---|
| 267260 | symbol profile checked | none | usable |
| 298040 | symbol profile checked | none | usable |
| 024840 | symbol profile checked | none after 2017 | usable, but source_proxy_only |
| 006340 | symbol profile checked | none after 2010 | representative May row usable; April overlay not aggregate |

Profile URLs:

- `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/267/267260.json`
- `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/298/298040.json`
- `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/024/024840.json`
- `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/006/006340.json`

## 12. Positive vs Counterexample Balance

```text
new_independent_case_count = 4
usable_trigger_row_count = 4
representative_trigger_count = 4
positive_case_count = 2
counterexample_count = 2
stage4b_case_count = 2
current_profile_error_count = 3
```

The two positives are transformer/electrical-equipment cases where order/backlog/margin bridge is explicit. The two counterexamples are cable/copper/power-theme price rows where source evidence does not prove company-specific backlog or margin conversion.

## 13. Current Calibrated Profile Stress Test

Current profile proxy assumptions:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual errors found:

1. `298040`: if the profile waits for already-reported segment margin only, C02 recognition can be too late. Overseas backlog margin-mix should allow Stage2-Actionable, while Green still waits for realized margin or revision confirmation.
2. `024840`: if a copper/AI theme with strong MFE is promoted, it becomes a false positive. It should be local 4B watch.
3. `006340`: if a post-run power-supercycle headline is treated as a fresh Stage2 signal, it becomes a severe false positive because forward MAE dominates.

## 14. Score / Return Alignment

| group | expected profile behavior | realized path | calibration implication |
|---|---|---|---|
| 267260 | Stage2-Actionable allowed | MFE180 +234.55%, MAE180 -5.34% | Positive alignment |
| 298040 | Stage2-Actionable allowed earlier | MFE180 +407.25%, MAE180 -0.31% | Too-late risk if margin bridge ignored |
| 024840 | block positive; local 4B | MFE180 +122.77%, MAE180 -21.74%, post-peak DD -64.87% | Do not confuse local MFE with durable C02 |
| 006340 | local 4B / false-positive block | MFE180 +3.26%, MAE180 -55.09% | Strong counterexample |

## 15. Raw Component Score Breakdown

```json
{
  "C02_R1_L125_267260_20240219_BACKLOG_CAPA_DATACENTER_POSITIVE": {
    "eps_fcf_explosion": 78,
    "earnings_visibility": 83,
    "bottleneck_pricing_power": 86,
    "market_mispricing": 73,
    "valuation_rerating": 76,
    "capital_allocation": 52,
    "information_confidence": 78
  },
  "C02_R1_L125_298040_20250430_US_EU_ORDER_MARGIN_POSITIVE": {
    "eps_fcf_explosion": 84,
    "earnings_visibility": 81,
    "bottleneck_pricing_power": 88,
    "market_mispricing": 68,
    "valuation_rerating": 82,
    "capital_allocation": 44,
    "information_confidence": 74
  },
  "C02_R1_L125_024840_20240415_COPPER_AI_THEME_4B_COUNTER": {
    "eps_fcf_explosion": 38,
    "earnings_visibility": 31,
    "bottleneck_pricing_power": 61,
    "market_mispricing": 43,
    "valuation_rerating": 51,
    "capital_allocation": 28,
    "information_confidence": 38
  },
  "C02_R1_L125_006340_20240516_POWER_SUPERCYCLE_BLOCKDEAL_COUNTER": {
    "eps_fcf_explosion": 30,
    "earnings_visibility": 24,
    "bottleneck_pricing_power": 54,
    "market_mispricing": 18,
    "valuation_rerating": 35,
    "capital_allocation": 22,
    "information_confidence": 35
  },
  "C02_R1_L125_006340_20240417_BLOCKDEAL_EARLY_WARNING_OVERLAY": {
    "eps_fcf_explosion": 28,
    "earnings_visibility": 20,
    "bottleneck_pricing_power": 47,
    "market_mispricing": 33,
    "valuation_rerating": 42,
    "capital_allocation": 15,
    "information_confidence": 42
  }
}
```

## 16. Local 4B vs Full 4B Split

C02 needs a strict split between:

```text
local_4B_watch = price has already run or theme is crowded, but non-price evidence is insufficient
full_4B = non-price thesis has also started to break or overhang/quality problem is explicit
```

This run supports:

- `024840`: local 4B watch. The evidence is mostly copper/AI/power-grid theme and price path has a large local MFE followed by extreme post-peak drawdown.
- `006340`: stronger 4B/full-watch candidate because the post-run entry had explicit block-deal/overhang evidence plus very poor forward path.

## 17. Sector-Specific Rule Candidate

```text
rule_id = C02_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_THEME_BLOWOFF_GATE_V1
scope = canonical_archetype_id:C02_POWER_GRID_DATACENTER_CAPEX
```

Rule candidate:

```text
For C02, Stage2-Actionable requires at least one company-specific non-price bridge:
1. signed order/backlog increase tied to grid/datacenter/utility CAPEX, or
2. CAPA lock / delivery visibility / customer delivery schedule, or
3. ASP/margin/revision bridge tied to high-voltage transformer or grid equipment mix.

If evidence is only copper price, AI electricity shortage vocabulary, electric cable theme, post-run price momentum, or broad ETF/sector beta, block positive promotion and route to local_4B_watch. If overhang/block-sale evidence appears during or after the run, require a stronger reset before any new Stage2 can be created.
```

## 18. Canonical Compression Note

Fine/deep leaves used here:

```text
GRID_EQUIPMENT_US_DATACENTER_CAPEX_BACKLOG_CAPA_LOCK -> C02
TRANSFORMER_US_EU_ORDER_BACKLOG_MARGIN_MIX -> C02
CABLE_MATERIAL_COPPER_AI_POWERGRID_THEME_BLOWOFF -> C02
CABLE_POWER_SUPERCYCLE_OVERHANG_BLOWOFF -> C02
CABLE_OVERHANG_EARLY_WARNING_BEFORE_BLOWOFF -> C02 overlay
```

All are compressed to canonical `C02_POWER_GRID_DATACENTER_CAPEX` for batch scoring.

## 19. Dedupe Groups

```text
C02_267260_20240219_Stage2Actionable_backlog_capa_datacenter -> representative
C02_298040_20250430_Stage2Actionable_overseas_order_margin -> representative
C02_024840_20240415_Stage4B_copper_ai_powergrid_theme -> representative
C02_006340_20240516_Stage4B_power_supercycle_blockdeal_overhang -> representative
C02_006340_20240417_Stage2_blockdeal_early_warning_overlay -> non_representative_overlay
```

Aggregate counting uses only representative rows.

## 20. Validation Scope

```text
all_usable_rows_include_MFE_MAE_30_90_180 = true
trigger_type_canonical_stage_label = true
entry_date_present = true
entry_price_present = true
price_source_present = true
large_sector_id_present = true
canonical_archetype_id_present = true
corporate_action_window_checked = true
same_entry_group_id_present = true
dedupe_for_aggregate_present = true
```

## 21. Machine-Readable Trigger Rows JSONL

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","case_id":"C02_R1_L125_267260_20240219_BACKLOG_CAPA_DATACENTER_POSITIVE","ticker":"267260","company":"HD현대일렉트릭","market":"KOSPI","selected_round":"R1","selected_loop":125,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_BACKLOG_CAPA_LOCK","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-16","entry_date":"2024-02-19","entry_price":123600.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":49.68,"MAE_30D_pct":-5.34,"MFE_90D_pct":161.73,"MAE_90D_pct":-5.34,"MFE_180D_pct":234.55,"MAE_180D_pct":-5.34,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_date_180D":"2024-11-12","peak_price_180D":413500.0,"drawdown_after_peak_180D_pct":-15.36,"close_180D_date":"2024-11-13","close_return_180D_pct":185.6,"corporate_action_window_status":"clean_180D","corporate_action_candidate_overlap_180D":[],"same_entry_group_id":"C02_267260_20240219_Stage2Actionable_backlog_capa_datacenter","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"calibration_usable_reason":"usable_representative_180D_clean","case_role":"positive","evidence_family":"backlog_capa_lock_datacenter_power_demand_analyst_bridge","source_url":"https://securities.miraeasset.com/bbs/download/2122467.pdf?attachmentId=2122467","source_secondary_url":"https://en.yna.co.kr/view/AEN20231201006600320","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":78,"earnings_visibility":83,"bottleneck_pricing_power":86,"market_mispricing":73,"valuation_rerating":76,"capital_allocation":52,"information_confidence":78},"current_profile_expected_stage":"Stage2-Actionable_or_Stage3-Yellow","current_profile_error_type":"none_material_positive_alignment","profile_error":false,"shadow_rule_decision":"allow_stage2_actionable; green_requires_margin_conversion_or_revision_confirmation","price_only_4b_local":false,"full_4b_non_price_evidence":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","case_id":"C02_R1_L125_298040_20250430_US_EU_ORDER_MARGIN_POSITIVE","ticker":"298040","company":"효성중공업","market":"KOSPI","selected_round":"R1","selected_loop":125,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_US_EU_ORDER_BACKLOG_MARGIN_MIX","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-29","entry_date":"2025-04-30","entry_price":489500.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":62.61,"MAE_30D_pct":-0.31,"MFE_90D_pct":186.01,"MAE_90D_pct":-0.31,"MFE_180D_pct":407.25,"MAE_180D_pct":-0.31,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"peak_date_180D":"2025-11-04","peak_price_180D":2483000.0,"drawdown_after_peak_180D_pct":-30.29,"close_180D_date":"2026-01-26","close_return_180D_pct":378.86,"corporate_action_window_status":"clean_180D","corporate_action_candidate_overlap_180D":[],"same_entry_group_id":"C02_298040_20250430_Stage2Actionable_overseas_order_margin","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"calibration_usable_reason":"usable_representative_180D_clean","case_role":"positive","evidence_family":"overseas_order_backlog_margin_mix_capacity_shortage","source_url":"https://www.hankyung.com/article/2025042921486","source_secondary_url":"https://www.businesspost.co.kr/BP?command=article_view&num=393218","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":84,"earnings_visibility":81,"bottleneck_pricing_power":88,"market_mispricing":68,"valuation_rerating":82,"capital_allocation":44,"information_confidence":74},"current_profile_expected_stage":"Stage2-Actionable","current_profile_error_type":"too_late_risk_if_waiting_for_reported_margin_only","profile_error":true,"shadow_rule_decision":"allow_stage2_actionable_when_overseas_backlog_margin_mix_is_explicit; cap_green_until_segment_margin_confirmed","price_only_4b_local":false,"full_4b_non_price_evidence":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","case_id":"C02_R1_L125_024840_20240415_COPPER_AI_THEME_4B_COUNTER","ticker":"024840","company":"KBI메탈","market":"KOSDAQ","selected_round":"R1","selected_loop":125,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"CABLE_MATERIAL_COPPER_AI_POWERGRID_THEME_BLOWOFF","trigger_type":"Stage4B","trigger_date":"2024-04-12","entry_date":"2024-04-15","entry_price":2130.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":122.77,"MAE_30D_pct":-14.08,"MFE_90D_pct":122.77,"MAE_90D_pct":-14.08,"MFE_180D_pct":122.77,"MAE_180D_pct":-21.74,"MFE_1Y_pct":122.77,"MAE_1Y_pct":-25.02,"peak_date_180D":"2024-05-21","peak_price_180D":4745.0,"drawdown_after_peak_180D_pct":-64.87,"close_180D_date":"2025-01-09","close_return_180D_pct":-1.17,"corporate_action_window_status":"clean_180D","corporate_action_candidate_overlap_180D":[],"same_entry_group_id":"C02_024840_20240415_Stage4B_copper_ai_powergrid_theme","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"calibration_usable_reason":"usable_representative_180D_clean","case_role":"counterexample","evidence_family":"copper_price_ai_powergrid_theme_without_company_specific_backlog","source_url":"https://kr.investing.com/news/stock-market-news/article-1040411","source_secondary_url":"https://www.thebigdata.co.kr/view.php?ud=202404150327391657cd1e7f0bdf_23","source_proxy_only":true,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":38,"earnings_visibility":31,"bottleneck_pricing_power":61,"market_mispricing":43,"valuation_rerating":51,"capital_allocation":28,"information_confidence":38},"current_profile_expected_stage":"Stage2_false_positive_or_local_4B","current_profile_error_type":"false_positive_if_theme_or_price_only_is_promoted_to_stage2_actionable","profile_error":true,"shadow_rule_decision":"block_positive_stage_without_company_specific_backlog_or_margin_bridge; route_to_local_4B_watch_when_mfe_spike_drawdown_is_extreme","price_only_4b_local":true,"full_4b_non_price_evidence":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","case_id":"C02_R1_L125_006340_20240516_POWER_SUPERCYCLE_BLOCKDEAL_COUNTER","ticker":"006340","company":"대원전선","market":"KOSPI","selected_round":"R1","selected_loop":125,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"CABLE_POWER_SUPERCYCLE_OVERHANG_BLOWOFF","trigger_type":"Stage4B","trigger_date":"2024-05-14","entry_date":"2024-05-16","entry_price":4910.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.26,"MAE_30D_pct":-33.1,"MFE_90D_pct":3.26,"MAE_90D_pct":-48.07,"MFE_180D_pct":3.26,"MAE_180D_pct":-55.09,"MFE_1Y_pct":3.26,"MAE_1Y_pct":-55.09,"peak_date_180D":"2024-05-16","peak_price_180D":5070.0,"drawdown_after_peak_180D_pct":-56.51,"close_180D_date":"2025-02-12","close_return_180D_pct":-30.55,"corporate_action_window_status":"clean_180D","corporate_action_candidate_overlap_180D":[],"same_entry_group_id":"C02_006340_20240516_Stage4B_power_supercycle_blockdeal_overhang","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"calibration_usable_reason":"usable_representative_180D_clean","case_role":"counterexample","evidence_family":"ai_datacenter_power_supercycle_headline_plus_blockdeal_overhang","source_url":"https://securities.miraeasset.com/bbs/download/2129191.pdf?attachmentId=2129191","source_secondary_url":"https://www.thebigdata.co.kr/view.php?ud=202404170652483904cd1e7f0bdf_23","source_proxy_only":true,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":30,"earnings_visibility":24,"bottleneck_pricing_power":54,"market_mispricing":18,"valuation_rerating":35,"capital_allocation":22,"information_confidence":35},"current_profile_expected_stage":"local_4B_watch_or_4C_if_promoted","current_profile_error_type":"false_positive_if_large_mfe_past_move_or_power_supercycle_theme_is_treated_as_new_stage2","profile_error":true,"shadow_rule_decision":"force_local_4b_watch_when blockdeal/overhang + post-run price basis dominates; do_not_promote_without_new_contract_or_margin_bridge","price_only_4b_local":true,"full_4b_non_price_evidence":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","case_id":"C02_R1_L125_006340_20240417_BLOCKDEAL_EARLY_WARNING_OVERLAY","ticker":"006340","company":"대원전선","market":"KOSPI","selected_round":"R1","selected_loop":125,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"CABLE_OVERHANG_EARLY_WARNING_BEFORE_BLOWOFF","trigger_type":"Stage2","trigger_date":"2024-04-16","entry_date":"2024-04-17","entry_price":2450.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":122.45,"MAE_30D_pct":-10.61,"MFE_90D_pct":122.45,"MAE_90D_pct":-10.61,"MFE_180D_pct":122.45,"MAE_180D_pct":-10.61,"MFE_1Y_pct":122.45,"MAE_1Y_pct":-10.61,"peak_date_180D":"2024-05-13","peak_price_180D":5450.0,"drawdown_after_peak_180D_pct":-59.54,"close_180D_date":"2025-01-13","close_return_180D_pct":62.86,"corporate_action_window_status":"clean_180D","corporate_action_candidate_overlap_180D":[],"same_entry_group_id":"C02_006340_20240417_Stage2_blockdeal_early_warning_overlay","dedupe_for_aggregate":false,"aggregate_group_role":"non_representative_overlay","calibration_usable":false,"calibration_usable_reason":"non_representative_overlay","case_role":"narrative_overlay","evidence_family":"blockdeal_overhang_early_warning_before_power_cable_theme_extension","source_url":"https://www.hankyung.com/article/2024041634976","source_secondary_url":"https://www.thebigdata.co.kr/view.php?ud=202404170652483904cd1e7f0bdf_23","source_proxy_only":true,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":28,"earnings_visibility":20,"bottleneck_pricing_power":47,"market_mispricing":33,"valuation_rerating":42,"capital_allocation":15,"information_confidence":42},"current_profile_expected_stage":"Stage2_watch_only","current_profile_error_type":"early_warning_overlay_not_representative","profile_error":false,"shadow_rule_decision":"when shareholder distribution appears before theme continuation, reduce confidence; do not treat subsequent MFE as evidence of C02 quality","price_only_4b_local":false,"full_4b_non_price_evidence":false}
{"row_type":"aggregate","research_file":"e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":125,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","priority_bucket":"Priority 0","coverage_before_rows":10,"coverage_after_if_accepted":14,"new_independent_case_count":4,"usable_trigger_row_count":4,"representative_trigger_count":4,"positive_case_count":2,"counterexample_count":2,"stage4b_case_count":2,"current_profile_error_count":3,"shadow_rule_candidate":"C02_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_THEME_BLOWOFF_GATE_V1","do_not_propose_new_weight_delta":false}
{"row_type":"shadow_weight_candidate","axis":"c02_capex_backlog_margin_bridge_vs_theme_blowoff_gate","scope":"canonical_archetype_id=C02_POWER_GRID_DATACENTER_CAPEX","recommendation":"Stage2-Actionable requires company-specific backlog/CAPA/delivery visibility plus margin/revision bridge. If evidence is only copper/AI/power-grid theme or post-run price momentum, route to local_4B_watch and block positive promotion until non-price bridge appears.","positive_support_case_ids":["C02_R1_L125_267260_20240219_BACKLOG_CAPA_DATACENTER_POSITIVE","C02_R1_L125_298040_20250430_US_EU_ORDER_MARGIN_POSITIVE"],"counterexample_case_ids":["C02_R1_L125_024840_20240415_COPPER_AI_THEME_4B_COUNTER","C02_R1_L125_006340_20240516_POWER_SUPERCYCLE_BLOCKDEAL_COUNTER"],"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","new_axis_proposed":"c02_capex_backlog_margin_bridge_vs_theme_blowoff_gate","existing_axis_strengthened":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_required_bridge"],"existing_axis_weakened":[],"current_profile_error_count":3,"residual_label":"C02 positive unlock is clean when backlog/capa/margin bridge is explicit; cable/copper theme with overhang remains a local 4B/false-positive risk despite large local MFE."}
```

## 22. Aggregate Metrics

```json
{
  "row_type": "aggregate",
  "research_file": "e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md",
  "selected_round": "R1",
  "selected_loop": 125,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "priority_bucket": "Priority 0",
  "coverage_before_rows": 10,
  "coverage_after_if_accepted": 14,
  "new_independent_case_count": 4,
  "usable_trigger_row_count": 4,
  "representative_trigger_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "stage4b_case_count": 2,
  "current_profile_error_count": 3,
  "shadow_rule_candidate": "C02_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_THEME_BLOWOFF_GATE_V1",
  "do_not_propose_new_weight_delta": false
}
```

## 23. Shadow Weight Candidate

```json
{
  "row_type": "shadow_weight_candidate",
  "axis": "c02_capex_backlog_margin_bridge_vs_theme_blowoff_gate",
  "scope": "canonical_archetype_id=C02_POWER_GRID_DATACENTER_CAPEX",
  "recommendation": "Stage2-Actionable requires company-specific backlog/CAPA/delivery visibility plus margin/revision bridge. If evidence is only copper/AI/power-grid theme or post-run price momentum, route to local_4B_watch and block positive promotion until non-price bridge appears.",
  "positive_support_case_ids": [
    "C02_R1_L125_267260_20240219_BACKLOG_CAPA_DATACENTER_POSITIVE",
    "C02_R1_L125_298040_20250430_US_EU_ORDER_MARGIN_POSITIVE"
  ],
  "counterexample_case_ids": [
    "C02_R1_L125_024840_20240415_COPPER_AI_THEME_4B_COUNTER",
    "C02_R1_L125_006340_20240516_POWER_SUPERCYCLE_BLOCKDEAL_COUNTER"
  ],
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 24. Residual Contribution Summary

```json
{
  "row_type": "residual_contribution",
  "new_axis_proposed": "c02_capex_backlog_margin_bridge_vs_theme_blowoff_gate",
  "existing_axis_strengthened": [
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "stage2_required_bridge"
  ],
  "existing_axis_weakened": [],
  "current_profile_error_count": 3,
  "residual_label": "C02 positive unlock is clean when backlog/capa/margin bridge is explicit; cable/copper theme with overhang remains a local 4B/false-positive risk despite large local MFE."
}
```

Plain-language contribution:

C02 should not be a power-grid keyword bucket. It should be an electrical-equipment CAPEX conversion bucket. The positive side is transformer/backlog/CAPA/margin bridge. The negative side is cable/copper/AI theme price momentum with no company-specific bridge and, in the worst case, block-sale overhang. The rule is like a transformer substation: the sector headline is high-voltage current, but Stage2 requires a safe step-down through signed orders, delivery schedules, and margins. Without that transformer, the current burns the signal.

## 25. Data Quality Caveats

- `024840` and `006340` counterexamples rely on media/proxy sources rather than company IR or signed-order disclosures; they are still valuable because the rule target is false-positive prevention.
- `006340` has one non-representative overlay row to explain early overhang; aggregate dedupe prevents double-counting.
- All price windows use raw/unadjusted OHLC from stock-web; no manifest date after 2026-02-20 is inferred.
- No production scoring change is made in this MD.

## 26. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent after the research phase is complete. Do not re-run live discovery. Ingest this standalone MD as one v12 research artifact. Validate all trigger rows under the v12 schema. Use only rows with calibration_usable=true and dedupe_for_aggregate=true for aggregate metrics. Treat non_representative_overlay rows as narrative support only. If batch promotion criteria are met, consider a shadow patch scoped to canonical_archetype_id=C02_POWER_GRID_DATACENTER_CAPEX:

C02_CAPEX_BACKLOG_MARGIN_BRIDGE_VS_THEME_BLOWOFF_GATE_V1:
- Stage2-Actionable can be allowed when company-specific backlog/order/CAPA/delivery visibility and margin/revision bridge are explicit.
- Price-only copper/AI/power-grid theme, broad cable beta, or post-run momentum should not become Stage2-Actionable.
- Local 4B watch should fire when theme MFE is large but non-price bridge is absent.
- Block-deal/overhang evidence during a power-theme run should reduce information confidence and require a new non-price reset before a later Stage2.

Do not apply any production change unless aggregate promotion gates pass across the full v12 corpus.
```

## 27. Final Research State

```text
completed_round = R1
completed_loop = 125
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
selected_archetype = C02_POWER_GRID_DATACENTER_CAPEX
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
coverage_before = C02 rows 10
coverage_after_if_accepted = C02 rows 14
need_to_30_after_if_accepted = 16
need_to_50_after_if_accepted = 36
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

## 28. Final Answer Contract

This MD is the sole research artifact for this execution. The final chat response should summarize the generated file, selected round/loop, selected priority bucket, case counts, and coverage contribution only.
