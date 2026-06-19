# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
output_file = e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round = R2
selected_loop = 112
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3
deep_sub_archetype_id = C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. This loop does not alter production scoring. It stress-tests whether C08 needs a sharper canonical bridge: **test socket / probe card / memory tester / reliability-test labels should not become Yellow or Green unless customer quality, repeat demand, or revenue-margin conversion is visible.**

The already-applied global axes remain valid and are not globally reproposed:

```text
stage2_required_bridge
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
local_4b_watch_guard
```

## 2. Round / Large Sector / Canonical Archetype Scope

C08 maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`. This is not C06 HBM memory customer capacity, C07 HBM equipment relative strength, C09 valuation blowoff, or C10 memory equipment recovery cycle. The tested C08 mechanism is customer-quality / repeat-demand / socket-probe-test conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

Published No-Repeat Index places C08 at 50 rows, which makes it a Priority 2 quality-repair candidate rather than a minimum coverage gap. Local generated memory already contains C08 loop110 and loop111. This loop uses loop112 and avoids repeating exact symbol/date/entry groups.

```text
prior C08 loop110 visible/local symbols = 003160, 086390, 110990, 420770, 089790, 119830, 131970
prior C08 loop111 visible/local symbols = 131290, 098120, 425420, 253590, 252990, 064290, 098460
loop112 new symbols = 232140, 095340, 092870, 058470, 405100
loop112 reused symbols with new trigger family/date = 131290, 252990
minimum_new_symbol_count = 5
minimum_positive_case_count = 4
minimum_counterexample_count = 3
new_independent_case_ratio = 7/7
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_usage = diagnostic_only
local_csv_copy_root = /mnt/data/stockweb_c08
```

The local CSV copies used in this loop correspond to stock-web tradable shard paths for each symbol's 2024 and 2025 files. All representative trigger rows have at least 180 trading-day forward windows inside the local 2024-2025 copy and the published manifest max date.

## 5. Historical Eligibility Gate

```text
historical_only = true
live_candidate_mode = false
current_stock_discovery_allowed = false
brokerage_api_allowed = false
all_trigger_rows_have_entry_date = true
all_trigger_rows_have_entry_price = true
all_trigger_rows_have_MFE_MAE_30_90_180 = true
corporate_action_window_status = clean_180D_window_research_profile_check_required
source_proxy_only_count = 7
evidence_url_pending_count = 7
promotion_blocked_until_url_repair = true
```

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3
compression_rule = socket, probe card, test board, memory tester, reliability-test, ceramic STF, or inspection quality routes compress to C08 only when the tested mechanism is customer quality, repeat demand, qualification, or test-service revenue conversion.
out_of_scope = C06 customer capacity; C07 equipment relative strength; C09 valuation blowoff; C10 memory recovery equipment cycle
```

## 7. Price Data Source Map

| symbol | company | price_shard_path | profile_path |
|---|---|---|---|
| 232140 | 와이아이케이 | `atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv; atlas/ohlcv_tradable_by_symbol_year/232/232140/2025.csv` | `atlas/symbol_profiles/232/232140.json` |
| 095340 | ISC | `atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv; atlas/ohlcv_tradable_by_symbol_year/095/095340/2025.csv` | `atlas/symbol_profiles/095/095340.json` |
| 092870 | 엑시콘 | `atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv; atlas/ohlcv_tradable_by_symbol_year/092/092870/2025.csv` | `atlas/symbol_profiles/092/092870.json` |
| 058470 | 리노공업 | `atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv; atlas/ohlcv_tradable_by_symbol_year/058/058470/2025.csv` | `atlas/symbol_profiles/058/058470.json` |
| 405100 | 큐알티 | `atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/405/405100/2025.csv` | `atlas/symbol_profiles/405/405100.json` |
| 131290 | 티에스이 | `atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv; atlas/ohlcv_tradable_by_symbol_year/131/131290/2025.csv` | `atlas/symbol_profiles/131/131290.json` |
| 252990 | 샘씨엔에스 | `atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv; atlas/ohlcv_tradable_by_symbol_year/252/252990/2025.csv` | `atlas/symbol_profiles/252/252990.json` |

## 8. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role | current_profile_verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| C08_R2_L112_001_232140 | 232140 | 와이아이케이 | Stage3-Yellow | 2024-04-15 | 6330 | 181.67 | -3.00 | 262.56 | -3.00 | 262.56 | -3.00 | positive | current_profile_missed_structural |
| C08_R2_L112_002_095340 | 095340 | ISC | Stage2-Actionable | 2024-08-05 | 42550 | 39.37 | -3.41 | 65.22 | -3.41 | 89.66 | -3.41 | positive | current_profile_too_late |
| C08_R2_L112_003_092870 | 092870 | 엑시콘 | Stage2-Actionable | 2024-02-15 | 18810 | 78.10 | -9.62 | 88.20 | -11.91 | 88.20 | -46.84 | positive | current_profile_missed_structural |
| C08_R2_L112_004_058470 | 058470 | 리노공업 | Stage2-Actionable | 2024-02-15 | 217500 | 24.37 | -10.02 | 42.07 | -10.02 | 42.07 | -26.16 | positive | current_profile_too_late |
| C08_R2_L112_005_405100 | 405100 | 큐알티 | Stage4B | 2024-03-15 | 32550 | 8.45 | -31.03 | 8.45 | -52.41 | 8.45 | -69.65 | counterexample | current_profile_false_positive |
| C08_R2_L112_006_131290 | 131290 | 티에스이 | Stage4B | 2024-05-16 | 72900 | 7.41 | -27.98 | 7.41 | -47.81 | 7.41 | -51.99 | counterexample | current_profile_4B_too_late |
| C08_R2_L112_007_252990 | 252990 | 샘씨엔에스 | Stage4C | 2024-05-16 | 8050 | 6.09 | -12.55 | 6.09 | -40.99 | 6.09 | -56.46 | counterexample | current_profile_4C_too_late |

## 9. Positive vs Counterexample Balance

```text
positive_case_count = 4
counterexample_count = 3
stage4b_case_count = 5
stage4c_case_count = 1
current_profile_error_count = 7
```

Positive rows (`232140`, `095340`, `092870`, `058470`) show strong 90D MFE when socket/tester/probe quality is attached to customer demand or repeat conversion. Counterexamples (`405100`, `131290`, `252990`) show local peak behavior: label strength remains, but repeat-demand or margin bridge fails, and the price path opens large 90D/180D MAE.

## 10. Evidence Source Map

All evidence rows are `source_proxy_only_until_url_repair`. The MD is valid for shadow residual research, but promotion is blocked until a later coding/research pass adds verified disclosure, IR, or public source URLs.

## 11. Case-by-Case Trigger Grid


### C08_R2_L112_001_232140 — 232140 / 와이아이케이 / Stage3-Yellow

- role: `positive bridge`
- trigger_family: `memory_tester_customer_order_conversion_quality_positive`
- entry_date / entry_price: `2024-04-15` / `6330`
- MFE/MAE path: 30D `181.67/-3.00`, 90D `262.56/-3.00`, 180D `262.56/-3.00`
- profile verdict: `current_profile_missed_structural`
- interpretation: C08 should reward this row only to the extent that customer-quality/repeat-demand bridge is visible. If the row is a label-only spike, it stays as local 4B or hard 4C watch.

### C08_R2_L112_002_095340 — 095340 / ISC / Stage2-Actionable

- role: `positive bridge`
- trigger_family: `test_socket_customer_quality_recovery_bridge_positive`
- entry_date / entry_price: `2024-08-05` / `42550`
- MFE/MAE path: 30D `39.37/-3.41`, 90D `65.22/-3.41`, 180D `89.66/-3.41`
- profile verdict: `current_profile_too_late`
- interpretation: C08 should reward this row only to the extent that customer-quality/repeat-demand bridge is visible. If the row is a label-only spike, it stays as local 4B or hard 4C watch.

### C08_R2_L112_003_092870 — 092870 / 엑시콘 / Stage2-Actionable

- role: `positive bridge`
- trigger_family: `memory_tester_repeat_demand_quality_bridge_positive_high_MAE_watch`
- entry_date / entry_price: `2024-02-15` / `18810`
- MFE/MAE path: 30D `78.10/-9.62`, 90D `88.20/-11.91`, 180D `88.20/-46.84`
- profile verdict: `current_profile_missed_structural`
- interpretation: C08 should reward this row only to the extent that customer-quality/repeat-demand bridge is visible. If the row is a label-only spike, it stays as local 4B or hard 4C watch.

### C08_R2_L112_004_058470 — 058470 / 리노공업 / Stage2-Actionable

- role: `positive bridge`
- trigger_family: `premium_test_socket_customer_quality_positive_high_MAE_guard`
- entry_date / entry_price: `2024-02-15` / `217500`
- MFE/MAE path: 30D `24.37/-10.02`, 90D `42.07/-10.02`, 180D `42.07/-26.16`
- profile verdict: `current_profile_too_late`
- interpretation: C08 should reward this row only to the extent that customer-quality/repeat-demand bridge is visible. If the row is a label-only spike, it stays as local 4B or hard 4C watch.

### C08_R2_L112_005_405100 — 405100 / 큐알티 / Stage4B

- role: `guardrail / counterexample`
- trigger_family: `reliability_test_label_local_peak_without_conversion_counter`
- entry_date / entry_price: `2024-03-15` / `32550`
- MFE/MAE path: 30D `8.45/-31.03`, 90D `8.45/-52.41`, 180D `8.45/-69.65`
- profile verdict: `current_profile_false_positive`
- interpretation: C08 should reward this row only to the extent that customer-quality/repeat-demand bridge is visible. If the row is a label-only spike, it stays as local 4B or hard 4C watch.

### C08_R2_L112_006_131290 — 131290 / 티에스이 / Stage4B

- role: `guardrail / counterexample`
- trigger_family: `probe_card_quality_label_after_peak_4B_counter`
- entry_date / entry_price: `2024-05-16` / `72900`
- MFE/MAE path: 30D `7.41/-27.98`, 90D `7.41/-47.81`, 180D `7.41/-51.99`
- profile verdict: `current_profile_4B_too_late`
- interpretation: C08 should reward this row only to the extent that customer-quality/repeat-demand bridge is visible. If the row is a label-only spike, it stays as local 4B or hard 4C watch.

### C08_R2_L112_007_252990 — 252990 / 샘씨엔에스 / Stage4C

- role: `guardrail / counterexample`
- trigger_family: `ceramic_STF_quality_label_demand_reset_counter`
- entry_date / entry_price: `2024-05-16` / `8050`
- MFE/MAE path: 30D `6.09/-12.55`, 90D `6.09/-40.99`, 180D `6.09/-56.46`
- profile verdict: `current_profile_4C_too_late`
- interpretation: C08 should reward this row only to the extent that customer-quality/repeat-demand bridge is visible. If the row is a label-only spike, it stays as local 4B or hard 4C watch.

## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role | current_profile_verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| C08_R2_L112_001_232140 | 232140 | 와이아이케이 | Stage3-Yellow | 2024-04-15 | 6330 | 181.67 | -3.00 | 262.56 | -3.00 | 262.56 | -3.00 | positive | current_profile_missed_structural |
| C08_R2_L112_002_095340 | 095340 | ISC | Stage2-Actionable | 2024-08-05 | 42550 | 39.37 | -3.41 | 65.22 | -3.41 | 89.66 | -3.41 | positive | current_profile_too_late |
| C08_R2_L112_003_092870 | 092870 | 엑시콘 | Stage2-Actionable | 2024-02-15 | 18810 | 78.10 | -9.62 | 88.20 | -11.91 | 88.20 | -46.84 | positive | current_profile_missed_structural |
| C08_R2_L112_004_058470 | 058470 | 리노공업 | Stage2-Actionable | 2024-02-15 | 217500 | 24.37 | -10.02 | 42.07 | -10.02 | 42.07 | -26.16 | positive | current_profile_too_late |
| C08_R2_L112_005_405100 | 405100 | 큐알티 | Stage4B | 2024-03-15 | 32550 | 8.45 | -31.03 | 8.45 | -52.41 | 8.45 | -69.65 | counterexample | current_profile_false_positive |
| C08_R2_L112_006_131290 | 131290 | 티에스이 | Stage4B | 2024-05-16 | 72900 | 7.41 | -27.98 | 7.41 | -47.81 | 7.41 | -51.99 | counterexample | current_profile_4B_too_late |
| C08_R2_L112_007_252990 | 252990 | 샘씨엔에스 | Stage4C | 2024-05-16 | 8050 | 6.09 | -12.55 | 6.09 | -40.99 | 6.09 | -56.46 | counterexample | current_profile_4C_too_late |

## 13. Current Calibrated Profile Stress Test

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
stage2_required_bridge = tested_and_strengthened_for_C08
price_only_blowoff_blocks_positive_stage = kept
full_4b_requires_non_price_evidence = kept
hard_4c_thesis_break_routes_to_4c = kept_with_C08_repeat_demand_break_subtype
```

Stress result: positives with verified customer/repeat-demand bridge retain Stage2-Actionable or Yellow status, while post-peak label-only rows move to local 4B or hard 4C watch. The current profile still misses some C08 positives when it treats socket/tester quality too conservatively after broad semiconductor drawdowns, and it remains too permissive when label-only reliability/test narratives appear near local peaks.

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2/Stage2-Actionable should require customer-quality or repeat-demand evidence.
Stage3-Yellow should require at least one of repeat-order conversion, margin bridge, or durable customer confirmation.
Stage3-Green is not loosened in this loop.
No Stage3-Green global threshold change is proposed.
```

## 15. 4B Local vs Full-window Timing Audit

C08 local 4B is most useful when a socket/probe/tester label has already rerated and the 30D or 90D path shows large downside asymmetry. `405100`, `131290`, and `252990` are local 4B/4C guardrail rows. `092870` and `058470` are positive but high-MAE rows, so they should remain Stage2/Yellows with a local 4B watch rather than automatic Green.

## 16. 4C Protection Audit

The cleanest C08 hard-4C candidate in this loop is `252990`, where the 180D MFE is only `6.09%` while 180D MAE is `-56.46%`. This supports a C08 subtype: repeat-demand/customer-quality break can become 4C only after non-price evidence confirms demand reset or qualification fade.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
new_axis_proposed = C08_verified_customer_quality_repeat_demand_revenue_margin_bridge_required_before_Yellow_or_Green_plus_label_spike_to_local_4B_or_4C_watch_v3
```

## 18. Canonical-Archetype Rule Candidate

C08 behaves like a socket in a test fixture: if the contact is clean and repeatable, the signal passes; if the contact is only a shiny label, the measurement jitters and the trade path turns into MAE. The proposed C08 rule therefore does not globally loosen semiconductor scoring. It sharpens the contact condition: **customer quality + repeat demand + revenue/margin bridge before Yellow or Green; label spike without bridge stays at 4B watch.**

## 19. Before / After Backtest Comparison

```text
P0 avg positive MFE90 = 114.51
P0 avg positive MAE90 = -7.08
P0 avg counterexample MFE90 = 7.32
P0 avg counterexample MAE90 = -47.07
P2 C08 shadow expected effect = keep positive bridge rows, downrank label-only 4B/4C rows
```

## 20. Score-Return Alignment Matrix

```text
P0 = calibrated global profile; residual errors remain in C08 label-spike and high-MAE cases.
P0b = old baseline; too permissive on price-only relative strength.
P1 = L2 sector-specific; useful but too broad because C06/C07/C09/C10 mechanisms differ.
P2 = C08 canonical-specific; best fit for socket/probe/test customer-quality bridge.
P3 = counterexample guard; blocks local peak labels but may miss low-MAE recovery positives.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3 | 4 | 3 | 5 | 1 | 7 | 2 | 7 | 7 | 7 | true | true | published C08 50 + local loop110/111/112 ≈ 71; quality repair not minimum fill |

## 22. Residual Contribution Summary

```text
This loop adds 7 new independent cases, 3 counterexamples, and 7 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.
new_independent_case_count: 7
reused_case_count: 2
reused_case_ids: C08_R2_L112_006_131290, C08_R2_L112_007_252990
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: customer_quality_positive_too_late, test_socket_label_false_positive, post_peak_probe_card_high_MAE, ceramic_STF_demand_reset_4C
new_axis_proposed: C08_verified_customer_quality_repeat_demand_revenue_margin_bridge_required_before_Yellow_or_Green_plus_label_spike_to_local_4B_or_4C_watch_v3
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

```text
validated_scope = historical 1D OHLC path, entry date, entry price, 30D/90D/180D MFE/MAE, C08 canonical compression, duplicate avoidance by local session memory
non_validation_scope = live recommendation, current watchlist, production scoring patch, brokerage API, investment advice
promotion_limit = source_proxy_only non-price evidence; URL repair required before apply_next_patch
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_verified_customer_quality_repeat_demand_revenue_margin_bridge_required_before_Yellow_or_Green_plus_label_spike_to_local_4B_or_4C_watch_v3,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 needs verified customer-quality/repeat-demand bridge before Yellow/Green","positive rows show avg MFE90 114.51 vs counterexample avg MAE90 -47.07","C08_R2_L112_001_232140_Stage3_Yellow|C08_R2_L112_002_095340_Stage2_Actionable|C08_R2_L112_003_092870_Stage2_Actionable|C08_R2_L112_004_058470_Stage2_Actionable|C08_R2_L112_005_405100_Stage4B|C08_R2_L112_006_131290_Stage4B|C08_R2_L112_007_252990_Stage4C",7,7,3,medium,canonical_shadow_only,"not production; URL repair required"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "local_copy_root": "/mnt/data/stockweb_c08", "notes": "C08 loop112 uses local CSV copies previously fetched from stock-web raw shard paths; rows are source_proxy_only for non-price evidence until URL repair."}
```

### 25.2 case rows

```jsonl
{"best_trigger": "Stage3-Yellow", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_001_232140", "case_type": "structural_success", "company_name": "와이아이케이", "current_profile_verdict": "current_profile_missed_structural", "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "notes": "memory_tester_customer_order_conversion_quality_positive / MFE90=262.56%, MAE90=-3.0%.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "case", "score_price_alignment": "aligned", "symbol": "232140"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_002_095340", "case_type": "structural_success", "company_name": "ISC", "current_profile_verdict": "current_profile_too_late", "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "notes": "test_socket_customer_quality_recovery_bridge_positive / MFE90=65.22%, MAE90=-3.41%.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "case", "score_price_alignment": "aligned", "symbol": "095340"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_003_092870", "case_type": "high_mae_success", "company_name": "엑시콘", "current_profile_verdict": "current_profile_missed_structural", "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "notes": "memory_tester_repeat_demand_quality_bridge_positive_high_MAE_watch / MFE90=88.2%, MAE90=-11.91%.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "case", "score_price_alignment": "aligned", "symbol": "092870"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_004_058470", "case_type": "high_mae_success", "company_name": "리노공업", "current_profile_verdict": "current_profile_too_late", "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "notes": "premium_test_socket_customer_quality_positive_high_MAE_guard / MFE90=42.07%, MAE90=-10.02%.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "case", "score_price_alignment": "aligned", "symbol": "058470"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_005_405100", "case_type": "failed_rerating", "company_name": "큐알티", "current_profile_verdict": "current_profile_false_positive", "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "notes": "reliability_test_label_local_peak_without_conversion_counter / MFE90=8.45%, MAE90=-52.41%.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "case", "score_price_alignment": "guardrail_aligned", "symbol": "405100"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_006_131290", "case_type": "4B_overlay_success", "company_name": "티에스이", "current_profile_verdict": "current_profile_4B_too_late", "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "notes": "probe_card_quality_label_after_peak_4B_counter / MFE90=7.41%, MAE90=-47.81%.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "reused_symbol_from_C08_loop111_but_new_trigger_family_and_entry_date", "round": "R2", "row_type": "case", "score_price_alignment": "guardrail_aligned", "symbol": "131290"}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_007_252990", "case_type": "4C_success", "company_name": "샘씨엔에스", "current_profile_verdict": "current_profile_4C_too_late", "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "notes": "ceramic_STF_quality_label_demand_reset_counter / MFE90=6.09%, MAE90=-40.99%.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "reused_symbol_from_C08_loop111_but_new_trigger_family_and_entry_date", "round": "R2", "row_type": "case", "score_price_alignment": "guardrail_aligned", "symbol": "252990"}
```

### 25.3 trigger rows

```jsonl
{"MAE_180D_pct": -3.0, "MAE_1Y_pct": null, "MAE_30D_pct": -3.0, "MAE_90D_pct": -3.0, "MFE_180D_pct": 262.56, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 181.67, "MFE_90D_pct": 262.56, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_001_232140", "company_name": "와이아이케이", "corporate_action_window_status": "clean_180D_window_research_profile_check_required; no known local stock-web row break in 2024_2025 CSV copy", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.97, "entry_date": "2024-04-15", "entry_price": 6330.0, "evidence_available_at_that_date": "historical_proxy; non-price evidence URL repair required before promotion", "evidence_family": "memory_tester_customer_order_conversion_quality_positive", "evidence_source": "source_proxy_only_until_url_repair", "evidence_url_pending": true, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "not_applicable_for_positive_case", "four_b_local_peak_proximity": "not_applicable_for_positive_case", "four_b_timing_verdict": "not_4B", "four_c_protection_label": "not_applicable", "green_lateness_ratio": 0.35, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_objective": "quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-06-13", "peak_price": 22950.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv; atlas/ohlcv_tradable_by_symbol_year/232/232140/2025.csv", "primary_archetype": "semi_test_socket_customer_quality", "profile_path": "atlas/symbol_profiles/232/232140.json", "promotion_block_reason": "source_proxy_only_until_evidence_URL_repair; use as shadow residual row only", "promotion_usable": false, "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "trigger", "rule_scope_candidate": "canonical_archetype_specific", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY+232140+Stage3-Yellow+2024-04-15", "sector": "semiconductor_test_socket_quality", "selected_loop": 112, "selected_round": "R2", "source_proxy_only": true, "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["repeat_order_or_conversion", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "232140", "trigger_date": "2024-04-15", "trigger_id": "C08_R2_L112_001_232140_Stage3_Yellow", "trigger_outcome_label": "memory_tester_customer_order_conversion_quality_positive", "trigger_type": "Stage3-Yellow"}
{"MAE_180D_pct": -3.41, "MAE_1Y_pct": null, "MAE_30D_pct": -3.41, "MAE_90D_pct": -3.41, "MFE_180D_pct": 89.66, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 39.37, "MFE_90D_pct": 65.22, "aggregate_group_role": "representative", "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_002_095340", "company_name": "ISC", "corporate_action_window_status": "clean_180D_window_research_profile_check_required; no known local stock-web row break in 2024_2025 CSV copy", "current_profile_verdict": "current_profile_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.96, "entry_date": "2024-08-05", "entry_price": 42550.0, "evidence_available_at_that_date": "historical_proxy; non-price evidence URL repair required before promotion", "evidence_family": "test_socket_customer_quality_recovery_bridge_positive", "evidence_source": "source_proxy_only_until_url_repair", "evidence_url_pending": true, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "not_applicable_for_positive_case", "four_b_local_peak_proximity": "not_applicable_for_positive_case", "four_b_timing_verdict": "not_4B", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_objective": "quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2025-01-09", "peak_price": 80700.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv; atlas/ohlcv_tradable_by_symbol_year/095/095340/2025.csv", "primary_archetype": "semi_test_socket_customer_quality", "profile_path": "atlas/symbol_profiles/095/095340.json", "promotion_block_reason": "source_proxy_only_until_evidence_URL_repair; use as shadow residual row only", "promotion_usable": false, "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "trigger", "rule_scope_candidate": "canonical_archetype_specific", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY+095340+Stage2-Actionable+2024-08-05", "sector": "semiconductor_test_socket_quality", "selected_loop": 112, "selected_round": "R2", "source_proxy_only": true, "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["repeat_order_or_conversion", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "095340", "trigger_date": "2024-08-05", "trigger_id": "C08_R2_L112_002_095340_Stage2_Actionable", "trigger_outcome_label": "test_socket_customer_quality_recovery_bridge_positive", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -46.84, "MAE_1Y_pct": null, "MAE_30D_pct": -9.62, "MAE_90D_pct": -11.91, "MFE_180D_pct": 88.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 78.1, "MFE_90D_pct": 88.2, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_003_092870", "company_name": "엑시콘", "corporate_action_window_status": "clean_180D_window_research_profile_check_required; no known local stock-web row break in 2024_2025 CSV copy", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -71.75, "entry_date": "2024-02-15", "entry_price": 18810.0, "evidence_available_at_that_date": "historical_proxy; non-price evidence URL repair required before promotion", "evidence_family": "memory_tester_repeat_demand_quality_bridge_positive_high_MAE_watch", "evidence_source": "source_proxy_only_until_url_repair", "evidence_url_pending": true, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "forward_window_trading_days": 180, "four_b_evidence_type": ["local_peak_after_fast_rerating"], "four_b_full_window_peak_proximity": "not_applicable_for_positive_case", "four_b_local_peak_proximity": "high_local_or_price_label_watch", "four_b_timing_verdict": "local_4B_or_4C_watch", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_objective": "quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-04-02", "peak_price": 35400.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv; atlas/ohlcv_tradable_by_symbol_year/092/092870/2025.csv", "primary_archetype": "semi_test_socket_customer_quality", "profile_path": "atlas/symbol_profiles/092/092870.json", "promotion_block_reason": "source_proxy_only_until_evidence_URL_repair; use as shadow residual row only", "promotion_usable": false, "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "trigger", "rule_scope_candidate": "canonical_archetype_specific", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY+092870+Stage2-Actionable+2024-02-15", "sector": "semiconductor_test_socket_quality", "selected_loop": 112, "selected_round": "R2", "source_proxy_only": true, "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["repeat_order_or_conversion", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": ["local_peak_after_fast_rerating"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "092870", "trigger_date": "2024-02-15", "trigger_id": "C08_R2_L112_003_092870_Stage2_Actionable", "trigger_outcome_label": "memory_tester_repeat_demand_quality_bridge_positive_high_MAE_watch", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -26.16, "MAE_1Y_pct": null, "MAE_30D_pct": -10.02, "MAE_90D_pct": -10.02, "MFE_180D_pct": 42.07, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 24.37, "MFE_90D_pct": 42.07, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_004_058470", "company_name": "리노공업", "corporate_action_window_status": "clean_180D_window_research_profile_check_required; no known local stock-web row break in 2024_2025 CSV copy", "current_profile_verdict": "current_profile_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.03, "entry_date": "2024-02-15", "entry_price": 217500.0, "evidence_available_at_that_date": "historical_proxy; non-price evidence URL repair required before promotion", "evidence_family": "premium_test_socket_customer_quality_positive_high_MAE_guard", "evidence_source": "source_proxy_only_until_url_repair", "evidence_url_pending": true, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "forward_window_trading_days": 180, "four_b_evidence_type": ["local_peak_after_fast_rerating"], "four_b_full_window_peak_proximity": "not_applicable_for_positive_case", "four_b_local_peak_proximity": "high_local_or_price_label_watch", "four_b_timing_verdict": "local_4B_or_4C_watch", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_objective": "quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-05-07", "peak_price": 309000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv; atlas/ohlcv_tradable_by_symbol_year/058/058470/2025.csv", "primary_archetype": "semi_test_socket_customer_quality", "profile_path": "atlas/symbol_profiles/058/058470.json", "promotion_block_reason": "source_proxy_only_until_evidence_URL_repair; use as shadow residual row only", "promotion_usable": false, "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "trigger", "rule_scope_candidate": "canonical_archetype_specific", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY+058470+Stage2-Actionable+2024-02-15", "sector": "semiconductor_test_socket_quality", "selected_loop": 112, "selected_round": "R2", "source_proxy_only": true, "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["repeat_order_or_conversion", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": ["local_peak_after_fast_rerating"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "058470", "trigger_date": "2024-02-15", "trigger_id": "C08_R2_L112_004_058470_Stage2_Actionable", "trigger_outcome_label": "premium_test_socket_customer_quality_positive_high_MAE_guard", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -69.65, "MAE_1Y_pct": null, "MAE_30D_pct": -31.03, "MAE_90D_pct": -52.41, "MFE_180D_pct": 8.45, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 8.45, "MFE_90D_pct": 8.45, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_005_405100", "company_name": "큐알티", "corporate_action_window_status": "clean_180D_window_research_profile_check_required; no known local stock-web row break in 2024_2025 CSV copy", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -72.01, "entry_date": "2024-03-15", "entry_price": 32550.0, "evidence_available_at_that_date": "historical_proxy; non-price evidence URL repair required before promotion", "evidence_family": "reliability_test_label_local_peak_without_conversion_counter", "evidence_source": "source_proxy_only_until_url_repair", "evidence_url_pending": true, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "four_b_full_window_peak_proximity": "good_full_window_4B_timing", "four_b_local_peak_proximity": "high_local_or_price_label_watch", "four_b_timing_verdict": "local_4B_or_4C_watch", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_objective": "quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-03-18", "peak_price": 35300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/405/405100/2025.csv", "primary_archetype": "semi_test_socket_customer_quality", "profile_path": "atlas/symbol_profiles/405/405100.json", "promotion_block_reason": "source_proxy_only_until_evidence_URL_repair; use as shadow residual row only", "promotion_usable": false, "reuse_reason": "new_symbol_for_local_C08_loop_set", "round": "R2", "row_type": "trigger", "rule_scope_candidate": "canonical_archetype_specific", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY+405100+Stage4B+2024-03-15", "sector": "semiconductor_test_socket_quality", "selected_loop": 112, "selected_round": "R2", "source_proxy_only": true, "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "405100", "trigger_date": "2024-03-15", "trigger_id": "C08_R2_L112_005_405100_Stage4B", "trigger_outcome_label": "reliability_test_label_local_peak_without_conversion_counter", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -51.99, "MAE_1Y_pct": null, "MAE_30D_pct": -27.98, "MAE_90D_pct": -47.81, "MFE_180D_pct": 7.41, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 7.41, "MFE_90D_pct": 7.41, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_006_131290", "company_name": "티에스이", "corporate_action_window_status": "clean_180D_window_research_profile_check_required; no known local stock-web row break in 2024_2025 CSV copy", "current_profile_verdict": "current_profile_4B_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.3, "entry_date": "2024-05-16", "entry_price": 72900.0, "evidence_available_at_that_date": "historical_proxy; non-price evidence URL repair required before promotion", "evidence_family": "probe_card_quality_label_after_peak_4B_counter", "evidence_source": "source_proxy_only_until_url_repair", "evidence_url_pending": true, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "four_b_full_window_peak_proximity": "good_full_window_4B_timing", "four_b_local_peak_proximity": "high_local_or_price_label_watch", "four_b_timing_verdict": "local_4B_or_4C_watch", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_objective": "quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-05-23", "peak_price": 78300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv; atlas/ohlcv_tradable_by_symbol_year/131/131290/2025.csv", "primary_archetype": "semi_test_socket_customer_quality", "profile_path": "atlas/symbol_profiles/131/131290.json", "promotion_block_reason": "source_proxy_only_until_evidence_URL_repair; use as shadow residual row only", "promotion_usable": false, "reuse_reason": "reused_symbol_from_C08_loop111_but_new_trigger_family_and_entry_date", "round": "R2", "row_type": "trigger", "rule_scope_candidate": "canonical_archetype_specific", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY+131290+Stage4B+2024-05-16", "sector": "semiconductor_test_socket_quality", "selected_loop": 112, "selected_round": "R2", "source_proxy_only": true, "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "131290", "trigger_date": "2024-05-16", "trigger_id": "C08_R2_L112_006_131290_Stage4B", "trigger_outcome_label": "probe_card_quality_label_after_peak_4B_counter", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -56.46, "MAE_1Y_pct": null, "MAE_30D_pct": -12.55, "MAE_90D_pct": -40.99, "MFE_180D_pct": 6.09, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 6.09, "MFE_90D_pct": 6.09, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_007_252990", "company_name": "샘씨엔에스", "corporate_action_window_status": "clean_180D_window_research_profile_check_required; no known local stock-web row break in 2024_2025 CSV copy", "current_profile_verdict": "current_profile_4C_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C08_DEEP_SOCKET_PROBE_MEMORY_TESTER_RELIABILITY_QUALIFICATION_REPEAT_DEMAND_VS_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -58.96, "entry_date": "2024-05-16", "entry_price": 8050.0, "evidence_available_at_that_date": "historical_proxy; non-price evidence URL repair required before promotion", "evidence_family": "ceramic_STF_quality_label_demand_reset_counter", "evidence_source": "source_proxy_only_until_url_repair", "evidence_url_pending": true, "fine_archetype_id": "C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "four_b_full_window_peak_proximity": "good_full_window_4B_timing", "four_b_local_peak_proximity": "high_local_or_price_label_watch", "four_b_timing_verdict": "local_4B_or_4C_watch", "four_c_protection_label": "hard_4c_success", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_objective": "quality_repair + positive_balance_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-05-23", "peak_price": 8540.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv; atlas/ohlcv_tradable_by_symbol_year/252/252990/2025.csv", "primary_archetype": "semi_test_socket_customer_quality", "profile_path": "atlas/symbol_profiles/252/252990.json", "promotion_block_reason": "source_proxy_only_until_evidence_URL_repair; use as shadow residual row only", "promotion_usable": false, "reuse_reason": "reused_symbol_from_C08_loop111_but_new_trigger_family_and_entry_date", "round": "R2", "row_type": "trigger", "rule_scope_candidate": "canonical_archetype_specific", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY+252990+Stage4C+2024-05-16", "sector": "semiconductor_test_socket_quality", "selected_loop": 112, "selected_round": "R2", "source_proxy_only": true, "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken", "customer_quality_or_repeat_demand_gap"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "252990", "trigger_date": "2024-05-16", "trigger_id": "C08_R2_L112_007_252990_Stage4C", "trigger_outcome_label": "ceramic_STF_quality_label_demand_reset_counter", "trigger_type": "Stage4C"}
```

### 25.4 score_simulation rows

```jsonl
{"MAE_90D_pct": -3.0, "MFE_90D_pct": 262.56, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_001_232140", "changed_components": ["customer_quality_score", "repeat_demand_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Require verified customer-quality/repeat-demand/revenue-margin bridge before Yellow/Green; route label-only or post-peak socket/test stories to local 4B/4C watch.", "current_profile_verdict": "current_profile_missed_structural", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C08_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 40, "contract_score": 45, "customer_quality_score": 78, "dilution_cb_risk_score": 5, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "margin_bridge_score": 62, "policy_or_regulatory_score": 10, "relative_strength_score": 60, "repeat_demand_quality_score": 82, "revision_score": 52, "test_socket_or_probe_quality_score": 80, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 35, "contract_score": 40, "customer_quality_score": 70, "dilution_cb_risk_score": 5, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "margin_bridge_score": 55, "policy_or_regulatory_score": 10, "relative_strength_score": 65, "repeat_demand_quality_score": 72, "revision_score": 48, "test_socket_or_probe_quality_score": 70, "valuation_repricing_score": 50}, "row_type": "score_simulation", "score_return_alignment_label": "aligned_positive", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "232140", "trigger_id": "C08_R2_L112_001_232140_Stage3_Yellow", "weighted_score_after": 82, "weighted_score_before": 78}
{"MAE_90D_pct": -3.41, "MFE_90D_pct": 65.22, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_002_095340", "changed_components": ["customer_quality_score", "repeat_demand_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Require verified customer-quality/repeat-demand/revenue-margin bridge before Yellow/Green; route label-only or post-peak socket/test stories to local 4B/4C watch.", "current_profile_verdict": "current_profile_too_late", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C08_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 40, "contract_score": 45, "customer_quality_score": 78, "dilution_cb_risk_score": 5, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "margin_bridge_score": 62, "policy_or_regulatory_score": 10, "relative_strength_score": 60, "repeat_demand_quality_score": 82, "revision_score": 52, "test_socket_or_probe_quality_score": 80, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 35, "contract_score": 40, "customer_quality_score": 70, "dilution_cb_risk_score": 5, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "margin_bridge_score": 55, "policy_or_regulatory_score": 10, "relative_strength_score": 65, "repeat_demand_quality_score": 72, "revision_score": 48, "test_socket_or_probe_quality_score": 70, "valuation_repricing_score": 50}, "row_type": "score_simulation", "score_return_alignment_label": "aligned_positive", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "095340", "trigger_id": "C08_R2_L112_002_095340_Stage2_Actionable", "weighted_score_after": 82, "weighted_score_before": 78}
{"MAE_90D_pct": -11.91, "MFE_90D_pct": 88.2, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_003_092870", "changed_components": ["customer_quality_score", "repeat_demand_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Require verified customer-quality/repeat-demand/revenue-margin bridge before Yellow/Green; route label-only or post-peak socket/test stories to local 4B/4C watch.", "current_profile_verdict": "current_profile_missed_structural", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C08_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 40, "contract_score": 45, "customer_quality_score": 78, "dilution_cb_risk_score": 5, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "margin_bridge_score": 62, "policy_or_regulatory_score": 10, "relative_strength_score": 60, "repeat_demand_quality_score": 82, "revision_score": 52, "test_socket_or_probe_quality_score": 80, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 35, "contract_score": 40, "customer_quality_score": 70, "dilution_cb_risk_score": 5, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "margin_bridge_score": 55, "policy_or_regulatory_score": 10, "relative_strength_score": 65, "repeat_demand_quality_score": 72, "revision_score": 48, "test_socket_or_probe_quality_score": 70, "valuation_repricing_score": 50}, "row_type": "score_simulation", "score_return_alignment_label": "aligned_positive", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "092870", "trigger_id": "C08_R2_L112_003_092870_Stage2_Actionable", "weighted_score_after": 82, "weighted_score_before": 78}
{"MAE_90D_pct": -10.02, "MFE_90D_pct": 42.07, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_004_058470", "changed_components": ["customer_quality_score", "repeat_demand_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Require verified customer-quality/repeat-demand/revenue-margin bridge before Yellow/Green; route label-only or post-peak socket/test stories to local 4B/4C watch.", "current_profile_verdict": "current_profile_too_late", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C08_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 40, "contract_score": 45, "customer_quality_score": 78, "dilution_cb_risk_score": 5, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "margin_bridge_score": 62, "policy_or_regulatory_score": 10, "relative_strength_score": 60, "repeat_demand_quality_score": 82, "revision_score": 52, "test_socket_or_probe_quality_score": 80, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 35, "contract_score": 40, "customer_quality_score": 70, "dilution_cb_risk_score": 5, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "margin_bridge_score": 55, "policy_or_regulatory_score": 10, "relative_strength_score": 65, "repeat_demand_quality_score": 72, "revision_score": 48, "test_socket_or_probe_quality_score": 70, "valuation_repricing_score": 50}, "row_type": "score_simulation", "score_return_alignment_label": "aligned_positive", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "058470", "trigger_id": "C08_R2_L112_004_058470_Stage2_Actionable", "weighted_score_after": 82, "weighted_score_before": 78}
{"MAE_90D_pct": -52.41, "MFE_90D_pct": 8.45, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_005_405100", "changed_components": ["customer_quality_score", "repeat_demand_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Require verified customer-quality/repeat-demand/revenue-margin bridge before Yellow/Green; route label-only or post-peak socket/test stories to local 4B/4C watch.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C08_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 12, "contract_score": 20, "customer_quality_score": 20, "dilution_cb_risk_score": 5, "execution_risk_score": 85, "legal_or_contract_risk_score": 10, "margin_bridge_score": 15, "policy_or_regulatory_score": 10, "relative_strength_score": 55, "repeat_demand_quality_score": 15, "revision_score": 15, "test_socket_or_probe_quality_score": 18, "valuation_repricing_score": 60}, "raw_component_scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 15, "contract_score": 25, "customer_quality_score": 32, "dilution_cb_risk_score": 5, "execution_risk_score": 76, "legal_or_contract_risk_score": 10, "margin_bridge_score": 22, "policy_or_regulatory_score": 10, "relative_strength_score": 72, "repeat_demand_quality_score": 25, "revision_score": 18, "test_socket_or_probe_quality_score": 30, "valuation_repricing_score": 80}, "row_type": "score_simulation", "score_return_alignment_label": "aligned_guardrail", "stage_label_after": "Stage4B_watch", "stage_label_before": "Stage3-Yellow", "symbol": "405100", "trigger_id": "C08_R2_L112_005_405100_Stage4B", "weighted_score_after": 59, "weighted_score_before": 76}
{"MAE_90D_pct": -47.81, "MFE_90D_pct": 7.41, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_006_131290", "changed_components": ["customer_quality_score", "repeat_demand_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Require verified customer-quality/repeat-demand/revenue-margin bridge before Yellow/Green; route label-only or post-peak socket/test stories to local 4B/4C watch.", "current_profile_verdict": "current_profile_4B_too_late", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C08_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 12, "contract_score": 20, "customer_quality_score": 20, "dilution_cb_risk_score": 5, "execution_risk_score": 85, "legal_or_contract_risk_score": 10, "margin_bridge_score": 15, "policy_or_regulatory_score": 10, "relative_strength_score": 55, "repeat_demand_quality_score": 15, "revision_score": 15, "test_socket_or_probe_quality_score": 18, "valuation_repricing_score": 60}, "raw_component_scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 15, "contract_score": 25, "customer_quality_score": 32, "dilution_cb_risk_score": 5, "execution_risk_score": 76, "legal_or_contract_risk_score": 10, "margin_bridge_score": 22, "policy_or_regulatory_score": 10, "relative_strength_score": 72, "repeat_demand_quality_score": 25, "revision_score": 18, "test_socket_or_probe_quality_score": 30, "valuation_repricing_score": 80}, "row_type": "score_simulation", "score_return_alignment_label": "aligned_guardrail", "stage_label_after": "Stage4B_watch", "stage_label_before": "Stage3-Yellow", "symbol": "131290", "trigger_id": "C08_R2_L112_006_131290_Stage4B", "weighted_score_after": 59, "weighted_score_before": 76}
{"MAE_90D_pct": -40.99, "MFE_90D_pct": 6.09, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_R2_L112_007_252990", "changed_components": ["customer_quality_score", "repeat_demand_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Require verified customer-quality/repeat-demand/revenue-margin bridge before Yellow/Green; route label-only or post-peak socket/test stories to local 4B/4C watch.", "current_profile_verdict": "current_profile_4C_too_late", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C08_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 12, "contract_score": 20, "customer_quality_score": 20, "dilution_cb_risk_score": 5, "execution_risk_score": 85, "legal_or_contract_risk_score": 10, "margin_bridge_score": 15, "policy_or_regulatory_score": 10, "relative_strength_score": 55, "repeat_demand_quality_score": 15, "revision_score": 15, "test_socket_or_probe_quality_score": 18, "valuation_repricing_score": 60}, "raw_component_scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 15, "contract_score": 25, "customer_quality_score": 32, "dilution_cb_risk_score": 5, "execution_risk_score": 76, "legal_or_contract_risk_score": 10, "margin_bridge_score": 22, "policy_or_regulatory_score": 10, "relative_strength_score": 72, "repeat_demand_quality_score": 25, "revision_score": 18, "test_socket_or_probe_quality_score": 30, "valuation_repricing_score": 80}, "row_type": "score_simulation", "score_return_alignment_label": "aligned_guardrail", "stage_label_after": "Stage4C", "stage_label_before": "Stage3-Yellow", "symbol": "252990", "trigger_id": "C08_R2_L112_007_252990_Stage4C", "weighted_score_after": 59, "weighted_score_before": 76}
```

### 25.5 aggregate / shadow / residual rows

```jsonl
{"calibration_usable_trigger_count": 7, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "counterexample_count": 3, "current_profile_error_count": 7, "do_not_propose_new_weight_delta": false, "evidence_url_pending_count": 7, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 7, "new_symbol_count": 5, "new_trigger_family_count": 7, "positive_case_count": 4, "promotion_blocked_until_url_repair": true, "representative_trigger_count": 7, "reused_case_count": 2, "round": "R2", "row_type": "aggregate", "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 7, "source_proxy_only_count": 7, "stage4b_case_count": 5, "stage4c_case_count": 1}
{"axis": "C08_verified_customer_quality_repeat_demand_revenue_margin_bridge_required_before_Yellow_or_Green_plus_label_spike_to_local_4B_or_4C_watch_v3", "backtest_effect": "preserve high-MFE/low-MAE customer-quality positives while downgrading local-peak test/socket label spikes with deep MAE.", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": null, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "promotion_caveat": "source_proxy_only rows; URL repair required before apply_next_patch", "proposal_type": "canonical_shadow_only", "row_type": "shadow_weight", "scope": "canonical_archetype_specific"}
{"canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "do_not_propose_new_weight_delta": false, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": 112, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "C08_verified_customer_quality_repeat_demand_revenue_margin_bridge_required_before_Yellow_or_Green_plus_label_spike_to_local_4B_or_4C_watch_v3", "new_independent_case_count": 7, "new_symbol_count": 5, "new_trigger_family_count": 7, "residual_error_types_found": ["customer_quality_positive_too_late", "test_socket_label_false_positive", "post_peak_probe_card_high_MAE", "ceramic_STF_demand_reset_4C"], "reused_case_count": 2, "round": "R2", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]}
{"completed_loop": 112, "completed_round": "R2", "next_recommended_archetypes": ["C22_INSURANCE_RATE_CYCLE_RESERVE", "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "C19_BRAND_RETAIL_INVENTORY_MARGIN", "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "C24_BIO_TRIAL_DATA_EVENT_RISK", "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"], "round_schedule_status": "coverage_index_selected", "round_sector_consistency": "pass", "row_type": "next_research_state", "selected_priority_bucket": "Priority 2 quality_repair_after_local_priority0_priority1_fill", "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md"}
```

## 26. Deferred Coding Agent Handoff Prompt

```text
Purpose:
You are now in the repository implementation phase. The attached Markdown file is a v12 post-calibrated residual research output produced using the Songdaiki/stock-web OHLC atlas. It is not live candidate research and not investment advice.

Target file:
e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md

Rules:
1. Parse price_source_validation, case, trigger, score_simulation, shadow_weight, residual_contribution, and next_research_state rows.
2. Use only calibration_usable=true rows for quantitative shadow calibration.
3. Do not treat reused symbol rows as duplicate if trigger family and entry date are new; use independent_evidence_weight.
4. Keep production scoring unchanged unless the user later asks for a promotion batch.
5. Because this file marks non-price evidence as source_proxy_only/evidence_url_pending, require URL repair before apply_next_patch.
6. Candidate scope is canonical_archetype_specific: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.
7. Candidate axis: C08_verified_customer_quality_repeat_demand_revenue_margin_bridge_required_before_Yellow_or_Green_plus_label_spike_to_local_4B_or_4C_watch_v3.
8. Reject compact filename aliases; this file follows the standard v12 filename pattern.
```

## 27. Next Round State

```text
completed_round = R2
completed_loop = 112
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = C08_TEST_SOCKET_PROBE_CARD_RELIABILITY_TEST_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_V3
new_independent_case_count = 7
reused_case_count = 2
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 7
new_trigger_family_count = 7
positive_case_count = 4
counterexample_count = 3
stage4b_case_count = 5
stage4c_case_count = 1
current_profile_error_count = 7
source_proxy_only_count = 7
evidence_url_pending_count = 7
promotion_blocked_until_url_repair = true
next_recommended_archetypes = C22_INSURANCE_RATE_CYCLE_RESERVE, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C19_BRAND_RETAIL_INVENTORY_MARGIN, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C24_BIO_TRIAL_DATA_EVENT_RISK, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt requires Stock-Web OHLC, complete 30/90/180D MFE/MAE, canonical trigger labels, standard v12 filename, and machine-readable JSONL rows.
- No-Repeat Index shows C08 at published 50 rows and recommends Priority 2 quality repair after under-covered axes are filled.
- Stock-Web manifest fields used here: `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.
