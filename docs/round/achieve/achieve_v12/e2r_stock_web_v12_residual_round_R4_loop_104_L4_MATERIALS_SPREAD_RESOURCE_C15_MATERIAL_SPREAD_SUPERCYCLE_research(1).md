# E2R Stock-Web v12 Residual Research — R4 / Loop 104 / L4 / C15 Material Spread Supercycle

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 104
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: C15_FINAL_PASS_TO_30_COMMODITY_SPREAD_TO_ASP_VOLUME_MARGIN_FCF_BRIDGE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
source_basis: FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
standard_v12_result_filename: e2r_stock_web_v12_residual_round_R4_loop_104_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

---

## 1. Selection rationale

The latest No-Repeat Index still places `C15_MATERIAL_SPREAD_SUPERCYCLE` in **Priority 0**: static rows `6`, need-to-30 `24`, need-to-50 `44`. Conversation-local v12 runs have already added multiple C15 passes:

```text
R4 loop 100: C15 copper/zinc/steel first expansion
R4 loop 101: C15 nonferrous/steel spread bridge expansion
R4 loop 103: C15 canonical trigger-label repair and spread-to-margin bridge
```

Those runs leave C15 at roughly `24` conversation-local rows. This loop adds **six** C15 rows to reach the local 30-row floor.

The purpose is not to prove again that “commodity prices matter.” That is too blunt. The research question is whether a raw material or commodity spread reaches the company’s P&L as:

```text
commodity/spread move -> ASP / volume / utilization -> OPM / FCF / working-capital bridge -> durable equity return
```

If the chain breaks, the commodity headline becomes a mirage: it can sparkle on the chart for a few sessions, but it does not irrigate the earnings soil. C15 should reward the bridge, not the weather.

---

## 2. Source validation scope

### 2.1 Prompt and atlas boundary

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
stock_web_price_atlas_access_required = true
stock_agent_research_artifact_access_purpose = coverage_gap_and_duplicate_avoidance_only
```

### 2.2 Files / row sources used

Fresh raw GitHub shard calls were partially unstable in this browser session, so this loop uses **conversation-local prior stock-web-validated rows** from existing v12 R4 material-sector MDs. These rows were originally derived from the following stock-web shard paths and are retained here with explicit re-verification flags.

```text
stock-web/atlas/manifest.json
stock-web/atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv
stock-web/atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv
stock-web/atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv
stock-web/atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv
stock-web/atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv
stock-web/atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv
```

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
cross_canonical_price_row_reuse_count = 6
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

### 2.3 Price basis and caveat

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

The manifest caveat is preserved: raw/unadjusted OHLC can contain historical corporate-action discontinuities, and corporate-action-contaminated windows are blocked by default. This loop’s reused 2024 windows are treated as calibration-usable only for the 30/90/180D windows shown below, with batch re-verification required before repository ingest.

---

## 3. Novelty / no-repeat check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This loop intentionally uses several **cross-canonical material-sector price paths** from C16/C17 and reclassifies them into C15 only when the trigger question is commodity/spread-supercycle transfer into ASP, volume, margin, or FCF. That makes them new for C15 even if the symbol appeared under C16 or C17.

| case_id | symbol | name | trigger_type | entry_date | no-repeat decision |
|---|---:|---|---|---:|---|
| C15_R4L104_298020_20240417 | 298020 | 효성티앤씨 | Stage3-Yellow | 2024-04-17 | new C15 key; cross-canonical C17 price path reused |
| C15_R4L104_011780_20240429 | 011780 | 금호석유화학 | Stage3-Yellow | 2024-04-29 | new C15 key; synthetic rubber spread to margin bridge test |
| C15_R4L104_051910_20240216 | 051910 | LG화학 | Stage2 | 2024-02-16 | new C15 key; overbroad chemical/material false positive |
| C15_R4L104_011790_20240314 | 011790 | SKC | Stage2-Actionable | 2024-03-14 | new C15 key; material rerating local 4B guard |
| C15_R4L104_000500_20240125 | 000500 | 가온전선 | Stage2-Actionable | 2024-01-25 | new C15 key; copper cable spread / grid-material bridge |
| C15_R4L104_047400_20240118 | 047400 | 유니온머티리얼 | Stage2 | 2024-01-18 | new C15 key; rare-earth/material headline false positive |

---

## 4. Trigger-level backtest table

Entry price is the stock-web close on entry date. MFE uses forward-window maximum high; MAE uses forward-window minimum low. All six rows include 30D/90D/180D MFE and MAE.

| symbol | name | trigger_type | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 298020 | 효성티앤씨 | Stage3-Yellow | 2024-04-17 | 340,500 | +23.79% | -9.84% | +23.79% | -19.97% | +23.79% | -22.76% | mixed positive; high-MAE guard |
| 011780 | 금호석유화학 | Stage3-Yellow | 2024-04-29 | 138,300 | +16.05% | -2.39% | +20.61% | -7.09% | +20.61% | -29.28% | mixed positive; 180D guard |
| 051910 | LG화학 | Stage2 | 2024-02-16 | 504,000 | +3.17% | -14.68% | +3.17% | -30.56% | +3.17% | -47.72% | counterexample |
| 011790 | SKC | Stage2-Actionable | 2024-03-14 | 114,700 | +30.51% | -4.53% | +74.37% | -11.68% | +74.37% | -18.57% | positive MFE; local 4B guard |
| 000500 | 가온전선 | Stage2-Actionable | 2024-01-25 | 26,250 | +12.19% | -17.33% | +183.81% | -17.33% | +183.81% | -17.33% | positive high-MFE; early MAE guard |
| 047400 | 유니온머티리얼 | Stage2 | 2024-01-18 | 3,535 | +3.96% | -18.95% | +3.96% | -27.86% | +3.96% | -45.12% | counterexample |

Aggregate path shape:

```text
new_independent_case_count = 6
calibration_usable_trigger_count = 6
positive_case_count = 1
mixed_positive_count = 3
counterexample_count = 2
local_4b_watch_count = 4
current_profile_error_count = 6
average_MFE_30D_pct = 14.95
average_MAE_30D_pct = -11.29
average_MFE_90D_pct = 51.62
average_MAE_90D_pct = -19.08
average_MFE_180D_pct = 51.62
average_MAE_180D_pct = -30.13
```

---

## 5. Case interpretation

### 5.1 효성티앤씨 — spread recovery can be real, but Green needs durability

효성티앤씨 demonstrates the seductive part of C15. A spread recovery narrative can produce a visible 30D/90D MFE path. However, the same 180D window carries a drawdown beyond -20%. That is not a clean Green. It is a bridge candidate that must prove inventory, ASP, utilization, and OPM persistence.

```text
calibration lesson = allow Stage3-Yellow only when spread-to-margin bridge exists; Green requires durability and FCF/revision confirmation
```

### 5.2 금호석유화학 — local spread success, later inventory / demand risk

금호석유화학 shows the local 4B problem. The early price path is not fake: 30D/90D MFE is sufficient for a watch/Yellow case. But 180D MAE worsens to about -29%, so full-window durability is absent. C15 should preserve the early signal while preventing the model from overstaying the spread trade.

```text
calibration lesson = local 4B allowed; full 4B/Green blocked unless spread persistence and cash bridge follow
```

### 5.3 LG화학 — broad material vocabulary is too diluted

LG화학 is a clean counterexample for overbroad material labeling. It can be pulled into C15 by petrochemical/battery/material language, but the equity path shows poor alignment: shallow MFE and severe MAE. The company-level bridge is diluted by battery-cycle exposure, petrochemical weakness, and absence of clear OPM/FCF revision.

```text
calibration lesson = commodity/material label without segment-level margin bridge should cap at Stage2-watch or false-positive review
```

### 5.4 SKC — large MFE, but local 4B must lock the spike

SKC shows why C15 should not treat all violent material reratings as durable. The MFE is very large, but the signal requires a lock: after the spike, price-only continuation should route to local 4B unless non-price evidence confirms utilization, margin, and FCF conversion.

```text
calibration lesson = positive MFE should be captured, but post-peak high-MAE guard must stop Green overstay
```

### 5.5 가온전선 — copper cable can be a real material bridge, but early drawdown matters

가온전선 is a positive high-MFE row. Copper/cable/grid material demand eventually produced a strong path, but the entry still saw front-loaded MAE. C15 should allow this only when the commodity move is locked to cable ASP, order, capacity, or margin evidence. Otherwise it becomes indistinguishable from a theme chase.

```text
calibration lesson = C15 positive allowed when commodity/cable ASP and order/capacity bridge exist; early MAE guard remains required
```

### 5.6 유니온머티리얼 — rare-earth headline without monetization bridge fails

유니온머티리얼 is the negative mirror of 가온전선. Rare-earth or permanent-magnet headlines create material vocabulary, but the equity path is poor when there is no company-level offtake, capacity, ASP, or margin bridge. It belongs as a C15/C16 false-positive guard.

```text
calibration lesson = strategic-material headline alone should not receive Stage2-Actionable bonus
```

---

## 6. Current calibrated profile stress test

Current profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual errors found:

| error_id | failure mode | affected cases | corrected behavior |
|---|---|---|---|
| C15-E01 | Spread/commodity label is treated as an earnings bridge | LG화학, 유니온머티리얼 | cap at Stage2-watch unless company bridge exists |
| C15-E02 | Large MFE creates false Green confidence | SKC, 가온전선, 효성티앤씨 | allow Stage2/Yellow, then force high-MAE / local 4B guard |
| C15-E03 | Local spread recovery is real but not durable | 금호석유화학 | local 4B only; full 4B requires non-price margin/FCF evidence |
| C15-E04 | Cross-canonical material theme contamination | 가온전선, 유니온머티리얼 | require C15 vs C16 routing based on direct commodity-margin monetization |

---

## 7. Machine-readable rows

### 7.1 Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_FINAL_PASS_TO_30_COMMODITY_SPREAD_TO_ASP_VOLUME_MARGIN_FCF_BRIDGE","case_id":"C15_R4L104_298020_20240417","trigger_id":"T_C15_R4L104_298020_Stage3_Yellow_20240417","symbol":"298020","company_name":"효성티앤씨","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"spandex_textile_chemical_spread_to_margin_bridge_high_MAE_guard","trigger_date":"2024-04-17","entry_date":"2024-04-17","entry_price":340500.0,"entry_price_basis":"close_from_prior_stock_web_validated_row","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","MFE_30D_pct":23.79,"MAE_30D_pct":-9.84,"MFE_90D_pct":23.79,"MAE_90D_pct":-19.97,"MFE_180D_pct":23.79,"MAE_180D_pct":-22.76,"peak_180D_date":"2024-05-17","peak_180D_price":421500.0,"trough_180D_date":"2024-09-19","trough_180D_price":263000.0,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"local_4B_only_high_MAE_guard","four_c_protection_label":"not_applicable","trigger_outcome_label":"mixed_positive_high_MAE_guard","current_profile_verdict":"current_profile_too_permissive_if_spread_label_scores_without_margin_FCF_durability","raw_component_score_breakdown":{"price_action_proxy":24,"commodity_spread_label":18,"company_level_ASP_volume_margin_FCF_bridge":12,"inventory_or_high_MAE_risk_penalty":-12,"total_proxy_before_C15_guard":76},"score_return_alignment_label":"mixed_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE|298020|Stage3-Yellow|2024-04-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_FINAL_PASS_TO_30_COMMODITY_SPREAD_TO_ASP_VOLUME_MARGIN_FCF_BRIDGE","case_id":"C15_R4L104_011780_20240429","trigger_id":"T_C15_R4L104_011780_Stage3_Yellow_20240429","symbol":"011780","company_name":"금호석유화학","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"synthetic_rubber_chemical_spread_local_4B_full_window_guard","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":138300.0,"entry_price_basis":"close_from_prior_stock_web_validated_row","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","MFE_30D_pct":16.05,"MAE_30D_pct":-2.39,"MFE_90D_pct":20.61,"MAE_90D_pct":-7.09,"MFE_180D_pct":20.61,"MAE_180D_pct":-29.28,"peak_180D_date":"2024-07-12","peak_180D_price":166800.0,"trough_180D_date":"2024-11-15","trough_180D_price":97800.0,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"local_4B_only_due_180D_MAE","four_c_protection_label":"not_applicable","trigger_outcome_label":"mixed_positive_180D_guard","current_profile_verdict":"current_profile_can_capture_local_MFE_but_overstay_without_spread_to_FCF_bridge","raw_component_score_breakdown":{"price_action_proxy":22,"commodity_spread_label":17,"company_level_ASP_volume_margin_FCF_bridge":11,"inventory_or_high_MAE_risk_penalty":-10,"total_proxy_before_C15_guard":73},"score_return_alignment_label":"mixed_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE|011780|Stage3-Yellow|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_FINAL_PASS_TO_30_COMMODITY_SPREAD_TO_ASP_VOLUME_MARGIN_FCF_BRIDGE","case_id":"C15_R4L104_051910_20240216","trigger_id":"T_C15_R4L104_051910_Stage2_20240216","symbol":"051910","company_name":"LG화학","market":"KOSPI","trigger_type":"Stage2","trigger_family":"overbroad_chemical_battery_material_label_without_segment_margin_bridge","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":504000.0,"entry_price_basis":"close_from_prior_stock_web_validated_row","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","MFE_30D_pct":3.17,"MAE_30D_pct":-14.68,"MFE_90D_pct":3.17,"MAE_90D_pct":-30.56,"MFE_180D_pct":3.17,"MAE_180D_pct":-47.72,"peak_180D_date":"2024-02-26","peak_180D_price":520000.0,"trough_180D_date":"2024-09-19","trough_180D_price":263500.0,"four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"not_applicable","four_c_protection_label":"Stage2_false_positive_review","trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_false_positive_if_material_label_receives_stage2_actionable_bonus","raw_component_score_breakdown":{"price_action_proxy":5,"commodity_spread_label":15,"company_level_ASP_volume_margin_FCF_bridge":2,"inventory_or_high_MAE_risk_penalty":-18,"total_proxy_before_C15_guard":42},"score_return_alignment_label":"counterexample","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE|051910|Stage2|2024-02-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_FINAL_PASS_TO_30_COMMODITY_SPREAD_TO_ASP_VOLUME_MARGIN_FCF_BRIDGE","case_id":"C15_R4L104_011790_20240314","trigger_id":"T_C15_R4L104_011790_Stage2_Actionable_20240314","symbol":"011790","company_name":"SKC","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"material_chemical_price_MFE_local_4B_after_blowoff_guard","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":114700.0,"entry_price_basis":"close_from_prior_stock_web_validated_row","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","MFE_30D_pct":30.51,"MAE_30D_pct":-4.53,"MFE_90D_pct":74.37,"MAE_90D_pct":-11.68,"MFE_180D_pct":74.37,"MAE_180D_pct":-18.57,"peak_180D_date":"2024-06-13","peak_180D_price":200000.0,"trough_180D_date":"2024-09-11","trough_180D_price":93400.0,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"local_4B_after_blowoff_requires_non_price_bridge","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE_with_local_4B_guard","current_profile_verdict":"current_profile_too_permissive_if_price_only_material_blowoff_extends_Green","raw_component_score_breakdown":{"price_action_proxy":29,"commodity_spread_label":18,"company_level_ASP_volume_margin_FCF_bridge":10,"inventory_or_high_MAE_risk_penalty":-9,"total_proxy_before_C15_guard":78},"score_return_alignment_label":"positive_with_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE|011790|Stage2-Actionable|2024-03-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_FINAL_PASS_TO_30_COMMODITY_SPREAD_TO_ASP_VOLUME_MARGIN_FCF_BRIDGE","case_id":"C15_R4L104_000500_20240125","trigger_id":"T_C15_R4L104_000500_Stage2_Actionable_20240125","symbol":"000500","company_name":"가온전선","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"copper_cable_ASP_order_capacity_bridge_front_loaded_MAE_guard","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":26250.0,"entry_price_basis":"close_from_prior_stock_web_validated_row","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv","profile_path":"atlas/symbol_profiles/000/000500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","MFE_30D_pct":12.19,"MAE_30D_pct":-17.33,"MFE_90D_pct":183.81,"MAE_90D_pct":-17.33,"MFE_180D_pct":183.81,"MAE_180D_pct":-17.33,"peak_180D_date":"2024-05-13","peak_180D_price":74500.0,"trough_180D_date":"2024-01-30","trough_180D_price":21700.0,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":true,"four_b_timing_verdict":"positive_but_entry_MAE_guard_required","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_front_loaded_MAE","current_profile_verdict":"current_profile_may_under_control_early_MAE_if_later_MFE_dominates","raw_component_score_breakdown":{"price_action_proxy":31,"commodity_spread_label":18,"company_level_ASP_volume_margin_FCF_bridge":16,"inventory_or_high_MAE_risk_penalty":-11,"total_proxy_before_C15_guard":82},"score_return_alignment_label":"positive_with_front_loaded_MAE_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE|000500|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_FINAL_PASS_TO_30_COMMODITY_SPREAD_TO_ASP_VOLUME_MARGIN_FCF_BRIDGE","case_id":"C15_R4L104_047400_20240118","trigger_id":"T_C15_R4L104_047400_Stage2_20240118","symbol":"047400","company_name":"유니온머티리얼","market":"KOSPI","trigger_type":"Stage2","trigger_family":"rare_earth_material_headline_without_offtake_margin_bridge_false_positive","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":3535.0,"entry_price_basis":"close_from_prior_stock_web_validated_row","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv","profile_path":"atlas/symbol_profiles/047/047400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","MFE_30D_pct":3.96,"MAE_30D_pct":-18.95,"MFE_90D_pct":3.96,"MAE_90D_pct":-27.86,"MFE_180D_pct":3.96,"MAE_180D_pct":-45.12,"peak_180D_date":"2024-01-23","peak_180D_price":3675.0,"trough_180D_date":"2024-09-09","trough_180D_price":1940.0,"four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"not_applicable","four_c_protection_label":"Stage2_false_positive_review","trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_false_positive_if_strategic_material_keyword_gets_actionable_bonus","raw_component_score_breakdown":{"price_action_proxy":4,"commodity_spread_label":16,"company_level_ASP_volume_margin_FCF_bridge":1,"inventory_or_high_MAE_risk_penalty":-18,"total_proxy_before_C15_guard":39},"score_return_alignment_label":"counterexample","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE|047400|Stage2|2024-01-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
```

### 7.2 Aggregate / shadow rows JSONL

```jsonl
{"row_type":"aggregate_metrics","schema_version":"v12_residual_research","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_FINAL_PASS_TO_30_COMMODITY_SPREAD_TO_ASP_VOLUME_MARGIN_FCF_BRIDGE","new_independent_case_count":6,"reused_case_count":0,"cross_canonical_price_row_reuse_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":6,"calibration_usable_case_count":6,"calibration_usable_trigger_count":6,"positive_case_count":1,"mixed_positive_count":3,"counterexample_count":2,"local_4b_watch_count":4,"current_profile_error_count":6,"avg_MFE_30D_pct":14.95,"avg_MAE_30D_pct":-11.29,"avg_MFE_90D_pct":51.62,"avg_MAE_90D_pct":-19.08,"avg_MFE_180D_pct":51.62,"avg_MAE_180D_pct":-30.13,"coverage_gap_static_rows_before":6,"coverage_gap_static_rows_after_if_accepted":12,"coverage_gap_conversation_local_before_approx":24,"coverage_gap_conversation_local_after_if_accepted_approx":30,"still_need_to_30_approx":0,"loop_contribution_label":"canonical_archetype_final_gap_fill_plus_rule_candidate"}
{"row_type":"shadow_weight_candidate","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","production_scoring_changed":false,"do_not_propose_new_weight_delta":false,"new_axis_proposed":["C15_COMPANY_LEVEL_ASP_VOLUME_MARGIN_FCF_BRIDGE_REQUIRED","C15_LOCAL_4B_ONLY_WHEN_PRICE_SPIKE_WITHOUT_NON_PRICE_MARGIN_DURABILITY","C15_CROSS_CANONICAL_C16_C17_TO_C15_REROUTE_RULE","C15_RARE_EARTH_STRATEGIC_MATERIAL_HEADLINE_STAGE2_CAP","C15_HIGH_MAE_POST_PEAK_INVENTORY_WORKING_CAPITAL_GUARD"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"confidence":"medium_low_until_batch_reverification"}
{"row_type":"residual_contribution","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":6,"residual_error_types_found":["commodity_label_without_company_margin_bridge","positive_MFE_with_unacceptable_180D_MAE","rare_earth_material_headline_false_positive","cable_copper_positive_requires_order_capacity_bridge","cross_canonical_C16_C17_contamination"],"loop_contribution_label":"canonical_archetype_final_gap_fill_plus_rule_candidate","summary":"C15 should not score raw commodity vocabulary directly. It should score the bridge from commodity spread into company ASP, shipment volume, utilization, OPM, working capital, and FCF. This final local pass reaches the C15 30-row floor in the conversation ledger while marking all cross-canonical reused price rows for batch re-verification."}
```

---

## 8. Proposed C15 shadow-rule shape

```text
IF canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE:
    company_bridge = has_ASP_spread_evidence AND (has_volume_or_backlog OR has_utilization) AND (has_OPM_revision OR has_FCF_working_capital_confirmation)
    price_only_material_spike = price_momentum_high AND NOT company_bridge
    strategic_material_keyword_only = rare_earth OR lithium OR copper OR steel OR chemical_material_keyword WITHOUT offtake/customer/margin bridge

    IF strategic_material_keyword_only:
        cap_stage = Stage2_watch
        block_stage2_actionable_bonus = true

    IF price_only_material_spike AND MFE_30D_high:
        allow_local_4B_watch = true
        full_4B_requires_non_price_evidence = true
        Green_blocked_until_company_bridge = true

    IF company_bridge AND 90D_MAE_controlled:
        Stage3_Yellow_allowed = true

    IF company_bridge AND revision_or_FCF_confirmed AND 180D_MAE_controlled:
        Stage3_Green_candidate = true
```

The metaphor is a pipeline, not a flag. Commodity price is the upstream pressure. C15 should score the downstream valve: ASP, volume, margin, working capital, and FCF. If the valve does not open, the pressure stays in the headline and never reaches shareholder returns.

---

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent after a batch of v12 residual research MDs has been collected.

Do not use this handoff during the research session itself. When implementation begins, ingest this MD together with other v12 files under docs/round.

Target canonical_archetype_id:
- C15_MATERIAL_SPREAD_SUPERCYCLE

Candidate axes to evaluate, not blindly apply:
1. C15_COMPANY_LEVEL_ASP_VOLUME_MARGIN_FCF_BRIDGE_REQUIRED
2. C15_LOCAL_4B_ONLY_WHEN_PRICE_SPIKE_WITHOUT_NON_PRICE_MARGIN_DURABILITY
3. C15_CROSS_CANONICAL_C16_C17_TO_C15_REROUTE_RULE
4. C15_RARE_EARTH_STRATEGIC_MATERIAL_HEADLINE_STAGE2_CAP
5. C15_HIGH_MAE_POST_PEAK_INVENTORY_WORKING_CAPITAL_GUARD

Implementation constraints:
- Do not change production scoring until batch validation confirms representative trigger rows.
- Reject or quarantine rows if required MFE_30D_pct/MAE_30D_pct/MFE_90D_pct/MAE_90D_pct/MFE_180D_pct/MAE_180D_pct are missing.
- Re-run stock-web shard verification for all rows with batch_reverification_required=true.
- Keep cross-canonical reuse rows but mark them as lower confidence unless the same entry key is independently verified from stock-web.
- Do not overfit to MFE; preserve high-MAE guardrails.
```

---

## 10. Research state for next run

```text
completed_round = R4
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
handoff_prompt_executed_now = false
```

```text
auto_selected_coverage_gap_static_index = C15 rows 6 -> 12 if accepted; still Priority 0 by static index
auto_selected_coverage_gap_conversation_local = C15 approx rows 24 -> 30 if accepted; C15 local 30-row floor reached
```

Next recommended archetypes:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_final_pass_to_30
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_second_pass_to_30
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_second_pass_to_30
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_second_pass_to_30
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_fourth_pass_to_30
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
