# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 108
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE
deep_sub_archetype_id = C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG
loop_objective = coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery
output_file = e2r_stock_web_v12_residual_round_R2_loop_108_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **7 calibration-usable triggers**, **7 representative triggers**, **4 positive cases**, **3 counterexamples**, and **2 Stage4B guard cases** for `R2 / L2 / C06`.

The intended residual is narrow: C06 is not broad memory-cycle beta and not HBM equipment relative strength. It asks whether a memory maker's HBM narrative is backed by **customer lock, capacity allocation, ASP/mix bridge, and revision/margin conversion**. Without that bridge, the same HBM word can be either a launchpad or a fog machine.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual tested here:

```text
C06_hypothesis =
    HBM customer/capacity evidence should unlock Stage2-Actionable or Yellow earlier
    only when customer lock + capacity allocation + ASP/mix/revision bridge are present.

C06_guardrail =
    sold-out HBM language after a large prior rerating, or partial qualification without volume/revision bridge,
    should route to Stage4B-watch or Stage2-watch rather than fresh Stage3-Green.
```

## 2. Round / Large Sector / Canonical Archetype Scope

- `C06_HBM_MEMORY_CUSTOMER_CAPACITY` maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`.
- This is **not** `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`; equipment supplier relative strength belongs to C07 unless the row is explicitly a memory maker/customer-capacity event.
- This is **not** `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`; broad DRAM/NAND recovery beta belongs to C10 unless the row has explicit HBM customer/capacity lock.
- Boundary compression: HBM3/HBM3E qualification, sold-out capacity, customer lock, and HBM mix/ASP are C06; downstream equipment order conversion is C07/C10 depending on evidence family.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for selection:

```text
Priority 0 row count before this loop:
C02 = 10
C09 = 10
C14 = 11
C10 = 13
C06 = 17
C07 = 18
C11 = 18
C01 = 19
C28 = 28
```

The immediate prior local session outputs already filled C02, C09, C14, and C10 once. Therefore this run selects C06, the next still-underfilled Priority 0 canonical archetype.

Existing visible `docs/round` C06 standard files include:

```text
e2r_stock_web_v12_residual_round_R2_loop_100_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
e2r_stock_web_v12_residual_round_R2_loop_100_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research_v2.md
e2r_stock_web_v12_residual_round_R2_loop_107_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
```

By the v12 loop rule, selected loop is `max(existing loop for R2 + C06) + 1 = 108`.

Duplicate hard gate:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
same_canonical_duplicate_found_in_visible_listing = false
same_symbol_allowed_if_new_trigger_date_or_new_trigger_family = true
new_independent_case_count = 7
reused_case_count = 0
new_symbol_count = 2
```

Caution: visible directory listing does not expose all prior JSONL trigger rows. If a later batch ingest finds an exact key collision, representative dedupe should collapse it. This MD uses distinct trigger dates and distinct event families to minimize that risk.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Manifest fields used:

```text
source_name = FinanceData/marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
```

## 5. Historical Eligibility Gate

All trigger rows below use stock-web tradable shards and have at least 180 forward trading days by the manifest/profile max date. Corporate-action candidate windows do not overlap the selected 180D forward windows.

| symbol | company | profile path | selected years | corporate-action overlap in selected 180D windows | status |
|---|---|---|---|---|---|
| 000660 | SK하이닉스 | atlas/symbol_profiles/000/000660.json | 2023-2025 | corporate-action candidates only 1998-2003; no overlap with 2023-2025 selected 180D windows | usable |
| 005930 | 삼성전자 | atlas/symbol_profiles/005/005930.json | 2024-2025 | corporate-action candidates 1996, 1997, 2018; no overlap with 2024 selected 180D windows | usable |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT | C06_HBM_MEMORY_CUSTOMER_CAPACITY | memory maker capacity allocation and customer lock are the core C06 evidence |
| HBM_ASP_MIX_REVISION_BRIDGE | C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM mix/ASP/revision converts the narrative into measurable rerating evidence |
| HBM_QUALIFICATION_LAG_4B_WATCH | C06_HBM_MEMORY_CUSTOMER_CAPACITY | failed or delayed customer qualification is the opposite side of the same C06 mechanism |
| PARTIAL_CLEARANCE_WITHOUT_VOLUME_BRIDGE | C06_HBM_MEMORY_CUSTOMER_CAPACITY | partial qualification does not equal full customer/revenue lock |

Deep sub-archetype used:

```text
C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG
```

## 7. Evidence Source Map

The evidence sources are event-date historical sources. The evidence is used only to anchor the trigger date and event family; all forward return calculations use stock-web OHLC.

| trigger_id | symbol | trigger_date | entry_date | trigger_type | evidence summary | evidence_url |
|---|---|---|---|---|---|---|
| TRG_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY | 000660 | 2023-07-26 | 2023-07-26 | Stage2-Actionable | Q2 loss narrowed as AI chip demand lifted HBM/advanced DRAM signal; 2024 capex likely higher. | https://www.reuters.com/technology/sk-hynix-reports-q2-loss-chip-glut-continues-2023-07-25/ |
| TRG_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK | 000660 | 2023-10-26 | 2023-10-27 | Stage2-Actionable | Q3 event: HBM capacity for AI sold out next year; recovery visibility improved. | https://www.reuters.com/technology/sk-hynixs-q3-loss-narrows-previous-qtr-solid-demand-advanced-chips-2023-10-25/ |
| TRG_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE | 000660 | 2024-01-24 | 2024-01-25 | Stage3-Yellow | Q4 surprise profit and strong AI product demand; clients could not get enough supply. | https://www.reuters.com/technology/sk-hynix-swings-q4-profit-strong-ai-chip-demand-2024-01-24/ |
| TRG_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY | 000660 | 2024-04-25 | 2024-04-25 | Stage3-Yellow | Q1 highest profit since Q2 2022; full recovery expected on AI/HBM demand; HBM capex higher. | https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/ |
| TRG_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH | 000660 | 2024-07-25 | 2024-07-25 | Stage4B | Q2 strong HBM narrative, but post-rally fresh Green would be late-cycle; sold-out status already price-crowded. | https://www.reuters.com/technology/nvidia-supplier-sk-hynixs-q2-profit-soars-ai-boom-2024-07-24/ |
| TRG_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B | 005930 | 2024-05-24 | 2024-05-24 | Stage4B | HBM3/HBM3E qualification concerns against Nvidia due to heat/power; company disputed report but qualification lag mattered. | https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/ |
| TRG_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE | 005930 | 2024-08-07 | 2024-08-07 | Stage2-Actionable | 8-layer HBM3E clears Nvidia test, but Samsung still playing catch-up and 12-layer supply lag remained. | https://www.reuters.com/technology/artificial-intelligence/samsungs-8-layer-hbm3e-chips-clear-nvidias-tests-use-sources-say-2024-08-06/ |

## 8. Price Data Source Map

| symbol | shard paths used | entry rows checked |
|---|---|---|
| 000660 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv; 2024.csv; 2025.csv | 2023-07-26; 2023-10-27; 2024-01-25; 2024-04-25; 2024-07-25 |
| 005930 | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv; 2025.csv | 2024-05-24; 2024-08-07 |

## 9. MFE / MAE Method

```text
entry_price = open on entry_date from stock-web tradable shard

MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100

horizons = 30D, 90D, 180D trading-day windows
```

This is a trigger-level backtest. It does not infer current price routes and does not use manifest dates beyond `2026-02-20`.

## 10. Case-by-Case Trigger Grid

| trigger_id | type | symbol | company | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | 180D peak/trough | 4B local/full | case |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TRG_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY | Stage2-Actionable | 000660 | SK하이닉스 | 2023-07-26 @ 116,000 | 11.21 | -4.05 | 16.03 | -4.05 | 65.0 | -4.05 | 2024-04-12 / 2023-07-26 | n/a | positive |
| TRG_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK | Stage2-Actionable | 000660 | SK하이닉스 | 2023-10-27 @ 119,800 | 12.35 | -2.92 | 45.99 | -2.92 | 107.43 | -2.92 | 2024-07-11 / 2023-10-31 | n/a | positive |
| TRG_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE | Stage3-Yellow | 000660 | SK하이닉스 | 2024-01-25 @ 142,700 | 22.56 | -7.71 | 47.16 | -7.71 | 74.14 | -7.71 | 2024-07-11 / 2024-02-01 | n/a | positive |
| TRG_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY | Stage3-Yellow | 000660 | SK하이닉스 | 2024-04-25 @ 173,800 | 23.71 | -2.76 | 42.98 | -12.77 | 42.98 | -16.74 | 2024-07-11 / 2024-09-19 | n/a | positive |
| TRG_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH | Stage4B | 000660 | SK하이닉스 | 2024-07-25 @ 196,200 | 3.21 | -22.73 | 4.99 | -26.25 | 15.7 | -26.25 | 2025-01-22 / 2024-09-19 | local_4B=true / full_4B=false | counterexample |
| TRG_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B | Stage4B | 005930 | 삼성전자 | 2024-05-24 @ 76,800 | 13.41 | -4.3 | 15.62 | -22.53 | 15.62 | -35.03 | 2024-07-11 / 2024-11-14 | local_4B=true / full_4B=true | counterexample |
| TRG_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE | Stage2-Actionable | 005930 | 삼성전자 | 2024-08-07 @ 73,000 | 9.86 | -14.79 | 9.86 | -31.64 | 9.86 | -31.64 | 2024-08-16 / 2024-11-14 | n/a | counterexample |

## 11. Trigger-Level Interpretation

### 11.1 Positive bridge: SK Hynix early/mid HBM customer-capacity cycle

The SK Hynix 2023-07-26 and 2023-10-27 triggers show why C06 must not be treated as generic memory beta. The early July signal had only `16.03%` MFE90 but `65.00%` MFE180, because the actual bridge was still forming. By October, HBM3/HBM3E sold-out capacity and customer discussions converted the same broad AI memory theme into a much cleaner C06 signal: `45.99%` MFE90 and `107.43%` MFE180 from the next tradable open.

The January and April 2024 triggers then show the transition from Stage2-Actionable to Stage3-Yellow. HBM demand was no longer only a demand headline; it had operating profit, ASP/mix and capex behavior attached. These are the beams under the bridge.

### 11.2 Counterexample bridge: late sold-out language and qualification lag

The 2024-07-25 SK Hynix row is intentionally not another positive proof. HBM remained strong, but the trigger arrived after a large prior rerating. Forward path had only `4.99%` MFE90 against `-26.25%` MAE90. That is not a Green-unlock event; it is a C06 local 4B-watch case.

Samsung provides the clean residual counterexample. The May 2024 HBM qualification concern row had a modest short-term bounce but then `-22.53%` MAE90 and `-35.03%` MAE180. The August 2024 partial 8-layer clearance row also failed as a fresh Actionable trigger: `9.86%` MFE90 versus `-31.64%` MAE90. The lesson is sharp: partial qualification is not full customer capacity lock, just as hearing a door unlock is not the same as seeing the shipment leave the warehouse.

## 12. Aggregate Backtest Summary

| bucket | selected cases | avg MFE30 | avg MAE30 | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| C06 positives with customer/capacity + ASP/mix/revision bridge | 4 | 17.46 | -4.36 | 38.04 | -6.86 | 72.39 | -7.85 | structural HBM customer-capacity rerating |
| C06 counterexamples / 4B-watch / partial-clearance rows | 3 | 8.83 | -13.94 | 10.16 | -26.81 | 13.73 | -30.97 | late or incomplete C06 evidence |
| all representative C06 rows in this loop | 7 | 13.76 | -8.47 | 26.09 | -15.41 | 47.25 | -17.76 | mixed until bridge and guard are separated |

## 13. Current Calibrated Profile Stress Test

The current calibrated profile already blocks pure price-only blowoff and requires non-price evidence for full 4B. This loop does not argue for loosening Stage3-Green. It proposes a narrower C06 split:

```text
C06 positive route:
    verified HBM customer lock
    + capacity sold-out / allocated capacity
    + ASP or mix evidence
    + revision or margin bridge
    => allow Stage2-Actionable or Stage3-Yellow

C06 guard route:
    late sold-out language after major rerating
    OR HBM qualification failure
    OR partial qualification without volume/revision bridge
    => Stage4B-watch or Stage2-watch
```

Residual errors found:

| residual error type | trigger examples | proposed handling |
|---|---|---|
| early HBM winner too easily treated as generic memory beta | 000660 2023-07-26 | keep Stage2-Actionable but require customer/capacity bridge before Yellow |
| late HBM sold-out language treated as fresh Green | 000660 2024-07-25 | route to local 4B-watch unless incremental customer/revision evidence appears |
| qualification failure underweighted | 005930 2024-05-24 | 4B-watch even if broad memory cycle is recovering |
| partial clearance overcounted as full customer lock | 005930 2024-08-07 | cap at Stage2-watch until shipment/revision bridge appears |

## 14. Score-Return Alignment Matrix

| trigger_id | before_stage | after_shadow_stage | before_score | after_score | MFE90 | MAE90 | MFE180 | MAE180 | alignment |
|---|---|---|---|---|---|---|---|---|---|
| TRG_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY | Stage2 | Stage2-Actionable | 73.0 | 76.5 | 16.03 | -4.05 | 65.0 | -4.05 | aligned_positive |
| TRG_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK | Stage2-Actionable | Stage2-Actionable | 77.0 | 80.5 | 45.99 | -2.92 | 107.43 | -2.92 | aligned_positive |
| TRG_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE | Stage3-Yellow | Stage3-Yellow | 81.5 | 83.5 | 47.16 | -7.71 | 74.14 | -7.71 | aligned_positive |
| TRG_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY | Stage3-Yellow | Stage3-Yellow | 84.5 | 85.5 | 42.98 | -12.77 | 42.98 | -16.74 | aligned_positive |
| TRG_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH | Stage3-Green | Stage4B | 88.5 | 76.0 | 4.99 | -26.25 | 15.7 | -26.25 | aligned_4b_guard |
| TRG_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B | Stage2-Actionable | Stage4B | 76.0 | 63.0 | 15.62 | -22.53 | 15.62 | -35.03 | aligned_4b_guard |
| TRG_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE | Stage2-Actionable | Stage2-watch | 77.5 | 67.0 | 9.86 | -31.64 | 9.86 | -31.64 | false_positive_counterexample |

## 15. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| e2r_2_1_stock_web_calibrated_proxy | P0 | current calibrated proxy; C06 bridge not fully split | 7 | 26.09 | -15.41 | 47.25 | -17.76 | 0.43 | mixed: finds winners but still overcredits late/partial C06 evidence |
| e2r_2_0_baseline_reference | P0b | weaker global guard | 7 | 26.09 | -15.41 | 47.25 | -17.76 | 0.57 | worse: would likely Green late sold-out language and partial clearance |
| L2_sector_specific_candidate_profile | P1 | L2 memory customer bridge + qualification guard | 7 | 26.09 | -15.41 | 47.25 | -17.76 | 0.29 | improves guard but sector scope is broad |
| C06_canonical_shadow_candidate | P2 | C06 customer/capacity/mix/revision bridge split | 7 | 38.04 on positives | -6.86 on positives | 72.39 on positives | -7.85 on positives | 0.14 | best: preserves SK Hynix structural winners and blocks Samsung partial-clearance false positive |

## 16. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate = L2_memory_hbm_customer_capacity_bridge_required_before_yellow_or_green
confidence = medium
```

Sector-level wording:

> In L2 memory/semiconductor names, HBM evidence may unlock Stage2-Actionable when customer/capacity evidence is explicit. Stage3-Yellow or Green should require at least one operating bridge: ASP/mix, margin, revision, or shipment/revenue confirmation.

## 17. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
new_axis_proposed = C06_verified_customer_lock_capacity_and_margin_revision_bridge_required_for_Yellow_or_Green_plus_qualification_lag_to_4B_watch
confidence = medium
```

Proposed C06 compression:

```text
if hbm_customer_capacity_signal == true:
    if customer_lock_verified and capacity_allocation_visible and (asp_mix_bridge or margin_revision_bridge):
        allow_stage = Stage2-Actionable_or_Stage3-Yellow
    elif partial_qualification_only or no_volume_bridge:
        max_stage = Stage2-watch

if hbm_sold_out_language == true and prior_rerating_extended == true:
    route_to = Stage4B-watch

if hbm_qualification_failure_or_lag == true:
    route_to = Stage4B-watch
```

## 18. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE | 4 | 3 | 2 | 0 | 7 | 0 | 7 | 7 | 4 | true | true | 6 rows to 30 by original index count; lower if this local output is later committed |

## 19. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, local_4b_watch_guard]
residual_error_types_found: [late_hbm_winner_requires_customer_capacity_bridge, late_cycle_hbm_sold_out_green_false_positive, hbm_qualification_lag_4b, partial_clearance_without_volume_bridge_false_positive]
new_axis_proposed: C06_verified_customer_lock_capacity_and_margin_revision_bridge_required_for_Yellow_or_Green_plus_qualification_lag_to_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 20. Validation Scope / Non-Validation Scope

Validated:

- stock-web tradable raw OHLC rows for all entry dates and 30/90/180D windows.
- profile-level corporate-action candidate windows are outside selected 180D windows.
- canonical trigger labels are limited to `Stage2-Actionable`, `Stage3-Yellow`, and `Stage4B`.
- evidence URLs are explicit historical event anchors.

Not validated:

- No live watchlist or present-day candidate scan.
- No production scoring code opened or patched.
- No broker API, no current stock discovery, no automated trading.
- No claim that these triggers are current recommendations.

## 21. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_verified_customer_lock_capacity_margin_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"HBM winners had customer/capacity lock plus ASP/mix/revision bridge; counterexamples had late price crowding or qualification lag.","Preserves 4 positive SK Hynix rows while routing 3 late/qualification rows to 4B-watch or Stage2-watch.","TRG_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY|TRG_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK|TRG_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE|TRG_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY|TRG_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH|TRG_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B|TRG_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE",7,7,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C06_partial_clearance_without_volume_bridge_stage_cap,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Partial qualification without shipment/revision bridge created a false positive path.","Caps partial clearance at Stage2-watch until customer volume bridge appears.","TRG_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE",7,7,3,medium,guardrail_shadow_only,"not production; 4B/watch calibration only"
```

## 22. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"CASE_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"aligned_or_slightly_late","price_source":"Songdaiki/stock-web","notes":"Q2 loss narrowed as AI chip demand lifted HBM/advanced DRAM signal; 2024 capex likely higher."}
{"row_type":"trigger","trigger_id":"TRG_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY","case_id":"CASE_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","symbol":"000660","company_name":"SK하이닉스","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-26","entry_date":"2023-07-26","entry_price":116000.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":11.21,"MAE_30D_pct":-4.05,"MFE_90D_pct":16.03,"MAE_90D_pct":-4.05,"MFE_180D_pct":65.0,"MAE_180D_pct":-4.05,"peak_30D_date":"2023-07-28","trough_30D_date":"2023-07-26","peak_90D_date":"2023-12-04","trough_90D_date":"2023-07-26","peak_180D_date":"2024-04-12","trough_180D_date":"2023-07-26","calibration_usable":true,"representative_for_aggregate":true,"aggregate_role":"representative","positive_or_counterexample":"positive","current_profile_error":true,"evidence_family":"verified_hbm_customer_capacity_or_qualification_event","evidence_url":"https://www.reuters.com/technology/sk-hynix-reports-q2-loss-chip-glut-continues-2023-07-25/","source_proxy_only":false,"evidence_url_pending":false,"corporate_action_overlap_180D":false,"forward_window_status":"available_180_trading_days","notes":"Q2 loss narrowed as AI chip demand lifted HBM/advanced DRAM signal; 2024 capex likely higher."}
{"row_type":"score_simulation","trigger_id":"TRG_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY","profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after":"C06_canonical_shadow_candidate","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"customer_lock_score":62,"capacity_visibility_score":58,"asp_mix_score":55,"revision_score":45,"margin_bridge_score":44,"relative_strength_score":68,"valuation_repricing_score":58,"qualification_risk_score":22,"positioning_overheat_score":18,"memory_cycle_beta_score":70},"weighted_score_before":73.0,"stage_label_before":"Stage2","raw_component_scores_after":{"customer_lock_score":62,"capacity_visibility_score":58,"asp_mix_score":55,"revision_score":45,"margin_bridge_score":44,"relative_strength_score":68,"valuation_repricing_score":58,"qualification_risk_score":22,"positioning_overheat_score":18,"memory_cycle_beta_score":70},"weighted_score_after":76.5,"stage_label_after":"Stage2-Actionable","score_return_alignment":"aligned_positive","MFE_90D_pct":16.03,"MAE_90D_pct":-4.05,"MFE_180D_pct":65.0,"MAE_180D_pct":-4.05,"calibration_usable":true,"notes":"shadow scoring only; production scoring not changed"}
{"row_type":"case","case_id":"CASE_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"aligned_or_slightly_late","price_source":"Songdaiki/stock-web","notes":"Q3 event: HBM capacity for AI sold out next year; recovery visibility improved."}
{"row_type":"trigger","trigger_id":"TRG_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK","case_id":"CASE_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","symbol":"000660","company_name":"SK하이닉스","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-26","entry_date":"2023-10-27","entry_price":119800.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":12.35,"MAE_30D_pct":-2.92,"MFE_90D_pct":45.99,"MAE_90D_pct":-2.92,"MFE_180D_pct":107.43,"MAE_180D_pct":-2.92,"peak_30D_date":"2023-12-04","trough_30D_date":"2023-10-31","peak_90D_date":"2024-03-08","trough_90D_date":"2023-10-31","peak_180D_date":"2024-07-11","trough_180D_date":"2023-10-31","calibration_usable":true,"representative_for_aggregate":true,"aggregate_role":"representative","positive_or_counterexample":"positive","current_profile_error":false,"evidence_family":"verified_hbm_customer_capacity_or_qualification_event","evidence_url":"https://www.reuters.com/technology/sk-hynixs-q3-loss-narrows-previous-qtr-solid-demand-advanced-chips-2023-10-25/","source_proxy_only":false,"evidence_url_pending":false,"corporate_action_overlap_180D":false,"forward_window_status":"available_180_trading_days","notes":"Q3 event: HBM capacity for AI sold out next year; recovery visibility improved."}
{"row_type":"score_simulation","trigger_id":"TRG_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK","profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after":"C06_canonical_shadow_candidate","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"customer_lock_score":78,"capacity_visibility_score":82,"asp_mix_score":64,"revision_score":52,"margin_bridge_score":50,"relative_strength_score":72,"valuation_repricing_score":61,"qualification_risk_score":18,"positioning_overheat_score":23,"memory_cycle_beta_score":76},"weighted_score_before":77.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_lock_score":78,"capacity_visibility_score":82,"asp_mix_score":64,"revision_score":52,"margin_bridge_score":50,"relative_strength_score":72,"valuation_repricing_score":61,"qualification_risk_score":18,"positioning_overheat_score":23,"memory_cycle_beta_score":76},"weighted_score_after":80.5,"stage_label_after":"Stage2-Actionable","score_return_alignment":"aligned_positive","MFE_90D_pct":45.99,"MAE_90D_pct":-2.92,"MFE_180D_pct":107.43,"MAE_180D_pct":-2.92,"calibration_usable":true,"notes":"shadow scoring only; production scoring not changed"}
{"row_type":"case","case_id":"CASE_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"aligned_or_slightly_late","price_source":"Songdaiki/stock-web","notes":"Q4 surprise profit and strong AI product demand; clients could not get enough supply."}
{"row_type":"trigger","trigger_id":"TRG_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE","case_id":"CASE_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","symbol":"000660","company_name":"SK하이닉스","trigger_type":"Stage3-Yellow","trigger_date":"2024-01-24","entry_date":"2024-01-25","entry_price":142700.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":22.56,"MAE_30D_pct":-7.71,"MFE_90D_pct":47.16,"MAE_90D_pct":-7.71,"MFE_180D_pct":74.14,"MAE_180D_pct":-7.71,"peak_30D_date":"2024-03-08","trough_30D_date":"2024-02-01","peak_90D_date":"2024-05-29","trough_90D_date":"2024-02-01","peak_180D_date":"2024-07-11","trough_180D_date":"2024-02-01","calibration_usable":true,"representative_for_aggregate":true,"aggregate_role":"representative","positive_or_counterexample":"positive","current_profile_error":false,"evidence_family":"verified_hbm_customer_capacity_or_qualification_event","evidence_url":"https://www.reuters.com/technology/sk-hynix-swings-q4-profit-strong-ai-chip-demand-2024-01-24/","source_proxy_only":false,"evidence_url_pending":false,"corporate_action_overlap_180D":false,"forward_window_status":"available_180_trading_days","notes":"Q4 surprise profit and strong AI product demand; clients could not get enough supply."}
{"row_type":"score_simulation","trigger_id":"TRG_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE","profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after":"C06_canonical_shadow_candidate","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"customer_lock_score":84,"capacity_visibility_score":86,"asp_mix_score":73,"revision_score":58,"margin_bridge_score":62,"relative_strength_score":76,"valuation_repricing_score":64,"qualification_risk_score":16,"positioning_overheat_score":35,"memory_cycle_beta_score":79},"weighted_score_before":81.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"customer_lock_score":84,"capacity_visibility_score":86,"asp_mix_score":73,"revision_score":58,"margin_bridge_score":62,"relative_strength_score":76,"valuation_repricing_score":64,"qualification_risk_score":16,"positioning_overheat_score":35,"memory_cycle_beta_score":79},"weighted_score_after":83.5,"stage_label_after":"Stage3-Yellow","score_return_alignment":"aligned_positive","MFE_90D_pct":47.16,"MAE_90D_pct":-7.71,"MFE_180D_pct":74.14,"MAE_180D_pct":-7.71,"calibration_usable":true,"notes":"shadow scoring only; production scoring not changed"}
{"row_type":"case","case_id":"CASE_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"aligned_or_slightly_late","price_source":"Songdaiki/stock-web","notes":"Q1 highest profit since Q2 2022; full recovery expected on AI/HBM demand; HBM capex higher."}
{"row_type":"trigger","trigger_id":"TRG_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY","case_id":"CASE_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","symbol":"000660","company_name":"SK하이닉스","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":173800.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":23.71,"MAE_30D_pct":-2.76,"MFE_90D_pct":42.98,"MAE_90D_pct":-12.77,"MFE_180D_pct":42.98,"MAE_180D_pct":-16.74,"peak_30D_date":"2024-06-11","trough_30D_date":"2024-05-02","peak_90D_date":"2024-07-11","trough_90D_date":"2024-08-05","peak_180D_date":"2024-07-11","trough_180D_date":"2024-09-19","calibration_usable":true,"representative_for_aggregate":true,"aggregate_role":"representative","positive_or_counterexample":"positive","current_profile_error":false,"evidence_family":"verified_hbm_customer_capacity_or_qualification_event","evidence_url":"https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/","source_proxy_only":false,"evidence_url_pending":false,"corporate_action_overlap_180D":false,"forward_window_status":"available_180_trading_days","notes":"Q1 highest profit since Q2 2022; full recovery expected on AI/HBM demand; HBM capex higher."}
{"row_type":"score_simulation","trigger_id":"TRG_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY","profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after":"C06_canonical_shadow_candidate","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"customer_lock_score":88,"capacity_visibility_score":90,"asp_mix_score":78,"revision_score":66,"margin_bridge_score":72,"relative_strength_score":82,"valuation_repricing_score":70,"qualification_risk_score":14,"positioning_overheat_score":52,"memory_cycle_beta_score":82},"weighted_score_before":84.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"customer_lock_score":88,"capacity_visibility_score":90,"asp_mix_score":78,"revision_score":66,"margin_bridge_score":72,"relative_strength_score":82,"valuation_repricing_score":70,"qualification_risk_score":14,"positioning_overheat_score":52,"memory_cycle_beta_score":82},"weighted_score_after":85.5,"stage_label_after":"Stage3-Yellow","score_return_alignment":"aligned_positive","MFE_90D_pct":42.98,"MAE_90D_pct":-12.77,"MFE_180D_pct":42.98,"MAE_180D_pct":-16.74,"calibration_usable":true,"notes":"shadow scoring only; production scoring not changed"}
{"row_type":"case","case_id":"CASE_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","case_type":"residual_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_4b_guard","current_profile_verdict":"current_profile_needs_4b_route","price_source":"Songdaiki/stock-web","notes":"Q2 strong HBM narrative, but post-rally fresh Green would be late-cycle; sold-out status already price-crowded."}
{"row_type":"trigger","trigger_id":"TRG_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH","case_id":"CASE_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","symbol":"000660","company_name":"SK하이닉스","trigger_type":"Stage4B","trigger_date":"2024-07-25","entry_date":"2024-07-25","entry_price":196200.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":3.21,"MAE_30D_pct":-22.73,"MFE_90D_pct":4.99,"MAE_90D_pct":-26.25,"MFE_180D_pct":15.7,"MAE_180D_pct":-26.25,"peak_30D_date":"2024-08-20","trough_30D_date":"2024-08-05","peak_90D_date":"2024-10-25","trough_90D_date":"2024-09-19","peak_180D_date":"2025-01-22","trough_180D_date":"2024-09-19","calibration_usable":true,"representative_for_aggregate":true,"aggregate_role":"representative","positive_or_counterexample":"counterexample","current_profile_error":true,"evidence_family":"verified_hbm_customer_capacity_or_qualification_event","evidence_url":"https://www.reuters.com/technology/nvidia-supplier-sk-hynixs-q2-profit-soars-ai-boom-2024-07-24/","source_proxy_only":false,"evidence_url_pending":false,"corporate_action_overlap_180D":false,"forward_window_status":"available_180_trading_days","notes":"Q2 strong HBM narrative, but post-rally fresh Green would be late-cycle; sold-out status already price-crowded."}
{"row_type":"score_simulation","trigger_id":"TRG_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH","profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after":"C06_canonical_shadow_candidate","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"customer_lock_score":90,"capacity_visibility_score":91,"asp_mix_score":80,"revision_score":70,"margin_bridge_score":74,"relative_strength_score":92,"valuation_repricing_score":83,"qualification_risk_score":14,"positioning_overheat_score":82,"memory_cycle_beta_score":84},"weighted_score_before":88.5,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"customer_lock_score":90,"capacity_visibility_score":91,"asp_mix_score":80,"revision_score":70,"margin_bridge_score":74,"relative_strength_score":92,"valuation_repricing_score":83,"qualification_risk_score":14,"positioning_overheat_score":82,"memory_cycle_beta_score":84},"weighted_score_after":76.0,"stage_label_after":"Stage4B","score_return_alignment":"aligned_4b_guard","MFE_90D_pct":4.99,"MAE_90D_pct":-26.25,"MFE_180D_pct":15.7,"MAE_180D_pct":-26.25,"calibration_usable":true,"notes":"shadow scoring only; production scoring not changed"}
{"row_type":"case","case_id":"CASE_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B","symbol":"005930","company_name":"삼성전자","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","case_type":"residual_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_4b_guard","current_profile_verdict":"current_profile_needs_4b_route","price_source":"Songdaiki/stock-web","notes":"HBM3/HBM3E qualification concerns against Nvidia due to heat/power; company disputed report but qualification lag mattered."}
{"row_type":"trigger","trigger_id":"TRG_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B","case_id":"CASE_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","symbol":"005930","company_name":"삼성전자","trigger_type":"Stage4B","trigger_date":"2024-05-24","entry_date":"2024-05-24","entry_price":76800.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":13.41,"MAE_30D_pct":-4.3,"MFE_90D_pct":15.62,"MAE_90D_pct":-22.53,"MFE_180D_pct":15.62,"MAE_180D_pct":-35.03,"peak_30D_date":"2024-07-05","trough_30D_date":"2024-05-30","peak_90D_date":"2024-07-11","trough_90D_date":"2024-10-07","peak_180D_date":"2024-07-11","trough_180D_date":"2024-11-14","calibration_usable":true,"representative_for_aggregate":true,"aggregate_role":"representative","positive_or_counterexample":"counterexample","current_profile_error":true,"evidence_family":"verified_hbm_customer_capacity_or_qualification_event","evidence_url":"https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/","source_proxy_only":false,"evidence_url_pending":false,"corporate_action_overlap_180D":false,"forward_window_status":"available_180_trading_days","notes":"HBM3/HBM3E qualification concerns against Nvidia due to heat/power; company disputed report but qualification lag mattered."}
{"row_type":"score_simulation","trigger_id":"TRG_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B","profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after":"C06_canonical_shadow_candidate","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"customer_lock_score":38,"capacity_visibility_score":44,"asp_mix_score":50,"revision_score":48,"margin_bridge_score":50,"relative_strength_score":54,"valuation_repricing_score":66,"qualification_risk_score":78,"positioning_overheat_score":55,"memory_cycle_beta_score":72},"weighted_score_before":76.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_lock_score":38,"capacity_visibility_score":44,"asp_mix_score":50,"revision_score":48,"margin_bridge_score":50,"relative_strength_score":54,"valuation_repricing_score":66,"qualification_risk_score":78,"positioning_overheat_score":55,"memory_cycle_beta_score":72},"weighted_score_after":63.0,"stage_label_after":"Stage4B","score_return_alignment":"aligned_4b_guard","MFE_90D_pct":15.62,"MAE_90D_pct":-22.53,"MFE_180D_pct":15.62,"MAE_180D_pct":-35.03,"calibration_usable":true,"notes":"shadow scoring only; production scoring not changed"}
{"row_type":"case","case_id":"CASE_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE","symbol":"005930","company_name":"삼성전자","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","case_type":"residual_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_counterexample","current_profile_verdict":"current_profile_false_positive_risk","price_source":"Songdaiki/stock-web","notes":"8-layer HBM3E clears Nvidia test, but Samsung still playing catch-up and 12-layer supply lag remained."}
{"row_type":"trigger","trigger_id":"TRG_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE","case_id":"CASE_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","deep_sub_archetype_id":"C06_DEEP_HBM3_HBM3E_CUSTOMER_LOCK_CAPACITY_SOLD_OUT_VS_QUALIFICATION_LAG","symbol":"005930","company_name":"삼성전자","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-07","entry_date":"2024-08-07","entry_price":73000.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":9.86,"MAE_30D_pct":-14.79,"MFE_90D_pct":9.86,"MAE_90D_pct":-31.64,"MFE_180D_pct":9.86,"MAE_180D_pct":-31.64,"peak_30D_date":"2024-08-16","trough_30D_date":"2024-09-19","peak_90D_date":"2024-08-16","trough_90D_date":"2024-11-14","peak_180D_date":"2024-08-16","trough_180D_date":"2024-11-14","calibration_usable":true,"representative_for_aggregate":true,"aggregate_role":"representative","positive_or_counterexample":"counterexample","current_profile_error":true,"evidence_family":"verified_hbm_customer_capacity_or_qualification_event","evidence_url":"https://www.reuters.com/technology/artificial-intelligence/samsungs-8-layer-hbm3e-chips-clear-nvidias-tests-use-sources-say-2024-08-06/","source_proxy_only":false,"evidence_url_pending":false,"corporate_action_overlap_180D":false,"forward_window_status":"available_180_trading_days","notes":"8-layer HBM3E clears Nvidia test, but Samsung still playing catch-up and 12-layer supply lag remained."}
{"row_type":"score_simulation","trigger_id":"TRG_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE","profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after":"C06_canonical_shadow_candidate","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"customer_lock_score":55,"capacity_visibility_score":58,"asp_mix_score":60,"revision_score":52,"margin_bridge_score":54,"relative_strength_score":60,"valuation_repricing_score":68,"qualification_risk_score":58,"positioning_overheat_score":62,"memory_cycle_beta_score":74},"weighted_score_before":77.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_lock_score":55,"capacity_visibility_score":58,"asp_mix_score":60,"revision_score":52,"margin_bridge_score":54,"relative_strength_score":60,"valuation_repricing_score":68,"qualification_risk_score":58,"positioning_overheat_score":62,"memory_cycle_beta_score":74},"weighted_score_after":67.0,"stage_label_after":"Stage2-watch","score_return_alignment":"false_positive_counterexample","MFE_90D_pct":9.86,"MAE_90D_pct":-31.64,"MFE_180D_pct":9.86,"MAE_180D_pct":-31.64,"calibration_usable":true,"notes":"shadow scoring only; production scoring not changed"}
{"row_type":"aggregate","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_ASP_MIX_REVISION_BRIDGE","trigger_row_count":7,"calibration_usable_trigger_count":7,"representative_trigger_count":7,"new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":2,"positive_case_count":4,"counterexample_count":3,"stage4b_case_count":2,"stage4c_case_count":0,"source_proxy_only_count":0,"evidence_url_pending_count":0,"current_profile_error_count":4,"avg_positive_MFE90":38.04,"avg_positive_MAE90":-6.86,"avg_counterexample_MFE90":10.16,"avg_counterexample_MAE90":-26.81,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"new_axis_proposed":"C06_verified_customer_lock_capacity_and_margin_revision_bridge_required_for_Yellow_or_Green_plus_qualification_lag_to_4B_watch","existing_axis_strengthened":"stage2_required_bridge|local_4b_watch_guard|price_only_blowoff_blocks_positive_stage","existing_axis_weakened":null}
{"row_type":"shadow_weight","axis":"C06_verified_customer_lock_capacity_margin_bridge_required","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","baseline_value":0,"tested_value":1,"delta":"+1","reason":"C06 winners had explicit customer/capacity lock and ASP/mix/revision bridge; counterexamples had late price crowding or qualification lag.","backtest_effect":"Preserves 4 positive SK Hynix HBM customer/capacity rows while routing 3 late/qualification rows to 4B-watch or Stage2-watch.","trigger_ids":"TRG_C06_R2_L108_000660_20230726_HBM_DEMAND_CAPEX_RECOVERY|TRG_C06_R2_L108_000660_20231027_HBM3_HBM3E_SOLD_OUT_CUSTOMER_LOCK|TRG_C06_R2_L108_000660_20240125_Q4_PROFIT_HBM_SUPPLY_SHORTAGE|TRG_C06_R2_L108_000660_20240425_Q1_HBM_CAPEX_FULL_RECOVERY|TRG_C06_R2_L108_000660_20240725_LATE_HBM_SOLD_OUT_4B_WATCH|TRG_C06_R2_L108_005930_20240524_HBM_QUALIFICATION_FAILURE_4B|TRG_C06_R2_L108_005930_20240807_8L_HBM3E_CLEAR_PARTIAL_FALSE_POSITIVE","calibration_usable_count":7,"new_independent_case_count":7,"counterexample_count":3,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; deferred coding handoff only"}
{"row_type":"residual_contribution","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_axis_proposed":"C06_verified_customer_lock_capacity_and_margin_revision_bridge_required_for_Yellow_or_Green_plus_qualification_lag_to_4B_watch","residual_error_types_found":["late_hbm_winner_requires_customer_capacity_bridge","late_cycle_hbm_sold_out_green_false_positive","hbm_qualification_lag_4b","partial_clearance_without_volume_bridge_false_positive"],"new_independent_case_count":7,"reused_case_count":0,"positive_case_count":4,"counterexample_count":3,"current_profile_error_count":4,"canonical_rule_candidate":true,"sector_rule_candidate":true,"do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","text":"This loop is not a current/live HBM recommendation. It is a historical calibration packet using stock-web raw/unadjusted tradable OHLC rows."}
```

## 23. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for stock_agent E2R v12 calibration. Do not execute this handoff during the research session that produced this MD.

Input file:
e2r_stock_web_v12_residual_round_R2_loop_108_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md

Objective:
Batch-ingest this MD together with other v12 residual research files. Parse machine-readable rows, validate required price fields, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and evaluate whether the following shadow-only candidate deserves a scoped patch:

candidate_axis = C06_verified_customer_lock_capacity_and_margin_revision_bridge_required_for_Yellow_or_Green_plus_qualification_lag_to_4B_watch
scope = canonical_archetype_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY

Expected behavior:
1. Do not change global Stage3-Green thresholds from this MD alone.
2. Do not use this as a live stock recommendation.
3. Preserve C06 positive route when customer/capacity lock plus ASP/mix/revision bridge exists.
4. Route late sold-out HBM language after extended rerating to local 4B-watch.
5. Cap partial HBM qualification without volume/revision bridge at Stage2-watch.
6. Keep production scoring unchanged until batch calibration confirms aggregate evidence.
```

## 24. Research State Footer

```text
completed_round = R2
completed_loop = 108
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
