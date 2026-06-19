---
title: "E2R Stock-Web V12 Residual Research — R2 Loop 110 — C06 HBM Memory Customer Capacity"
created_at_kst: "2026-06-13"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R2"
selected_loop: 110
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
large_sector_id: "L2_AI_SEMICONDUCTOR_ELECTRONICS"
canonical_archetype_id: "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
fine_archetype_id: "C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK"
deep_sub_archetype_id: "C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK
deep_sub_archetype_id = C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG
loop_objective = coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery
output_filename = e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
```

This is a standalone historical calibration artifact. It is not a live scan, not a watchlist, not investment advice, not a code patch, and not a production scoring change. It follows the coverage-index-first scheduler; `V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance and coverage ledger.

## 1. Current Calibrated Profile Assumption

Assumed current profile proxy: `e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as constraints, not rediscoveries:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

This loop does not ask whether HBM was a strong 2024/2025 theme. It asks a narrower C06 question: when does HBM customer/capacity evidence become a verified direct memory-maker lock, and when is it only a substrate/socket/material proxy label that should be capped at Stage2-Actionable or routed to Stage4B-Watch?

## 2. Round / Large Sector / Canonical Archetype Scope

`C06_HBM_MEMORY_CUSTOMER_CAPACITY` maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`.

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK
deep_sub_archetype_id = C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG
```

C06 is compressed around memory-maker customer lock / capacity sold-out / HBM mix and its validated supply-chain proxies. It is not a generic semiconductor relative-strength bucket; C07/C09/C10 handle equipment order relative strength, advanced-equipment blowoff, and memory recovery equipment cycle separately.

## 3. Previous Coverage / Duplicate Avoidance Check

The published No-Repeat Index reports C06 as Priority 0 with 17 rows and 13 rows needed to reach the 30-row stability band. This local session already produced C06 loop108 and loop109. After those, C06 is locally above 30, but still below the 50-row practical calibration band. Therefore this loop selects C06 again under the same coverage-index-first rule, but changes the fine route to substrate/socket/material proxy versus direct memory-maker lock.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Avoidance note:

```text
Prior C06 direct memory maker symbols 000660 and 005930 are reused only with new trigger families and independent_evidence_weight=0.5.
New C06 proxy symbols in this loop: 222800, 131290, 095340, 389260, 005290.
No row repeats a prior C06 symbol + trigger_type + entry_date group.
```

Session-adjusted coverage estimate:

```text
Index C06 rows = 17
prior current-session C06 loop108 representative triggers = 7
prior current-session C06 loop109 representative triggers = 7
this loop representative triggers = 7
estimated C06 after this loop = 38
remaining to 30 = 0
remaining to 50 = 12
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The manifest basis used for this loop is `raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, `symbol_count=5414`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`. Every representative trigger row below includes the canonical six 30D/90D/180D MFE/MAE fields.

## 5. Historical Eligibility Gate

All representative trigger rows use historical trigger dates before the stock-web manifest max date, have `entry_date`, `entry_price`, 180 forward trading-day windows, canonical stage labels, and clean 180D corporate-action status for this research pass.

Rows using proxy-only evidence remain calibration-usable for price-path/error-shape study but are blocked from positive promotion until URL repair confirms the non-price bridge.

## 6. Canonical Archetype Compression Map

| level | id | treatment |
|---|---|---|
| large sector | `L2_AI_SEMICONDUCTOR_ELECTRONICS` | AI / semiconductor / electronics historical calibration |
| canonical | `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | direct HBM customer/capacity lock or verified supply-chain bridge |
| fine | `C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK` | separates memory-maker lock from substrate/socket/material proxy labels |
| deep | `C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG` | 12L HBM3E supply lock vs qualification lag and proxy-label overpromotion |

## 7. Case Selection Summary

| case_id | symbol | company | trigger | entry | role | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| C06-R2-L110-000660-20240926-HBM3E_12L_MASS_PRODUCTION_CUSTOMER_LOCK | 000660 | SK하이닉스 | Stage3-Yellow | 2024-09-26 @ 174,600 | structural_success | 11.23 | -5.10 | 26.63 | -7.90 | 43.99 | -8.25 | current_profile_too_late |
| C06-R2-L110-005930-20240807-HBM3E_CLEAR_BUT_QUALIFICATION_LAG_COUNTER | 005930 | 삼성전자 | Stage4B | 2024-08-07 @ 74,700 | failed_rerating | 3.88 | -10.71 | 4.69 | -29.05 | 13.52 | -32.26 | current_profile_false_positive |
| C06-R2-L110-222800-20240322-MEMORY_SUBSTRATE_HBM_CAPACITY_PROXY | 222800 | 심텍 | Stage2-Actionable | 2024-03-22 @ 33,150 | stage2_promote_candidate | 17.65 | -6.18 | 34.54 | -8.90 | 41.33 | -21.27 | current_profile_missed_structural |
| C06-R2-L110-131290-20240322-TEST_INTERFACE_HBM_CUSTOMER_PROXY | 131290 | 티에스이 | Stage2-Actionable | 2024-03-22 @ 58,300 | structural_success | 15.27 | -7.03 | 39.62 | -7.03 | 44.77 | -23.84 | current_profile_too_late |
| C06-R2-L110-095340-20240401-HBM_SOCKET_LABEL_WITHOUT_CUSTOMER_LOCK | 095340 | ISC | Stage3-Yellow | 2024-04-01 @ 82,100 | failed_rerating | 12.06 | -13.15 | 18.27 | -31.55 | 18.27 | -48.36 | current_profile_false_positive |
| C06-R2-L110-389260-20240418-PACKAGE_SUBSTRATE_LABEL_FALSE_YELLOW | 389260 | 대덕전자 | Stage4B | 2024-04-18 @ 25,200 | price_moved_without_evidence | 8.73 | -11.51 | 10.91 | -24.60 | 10.91 | -38.10 | current_profile_4B_too_late |
| C06-R2-L110-005290-20240322-MATERIAL_PROXY_NO_HBM_CUSTOMER_LOCK | 005290 | 동진쎄미켐 | Stage3-Yellow | 2024-03-22 @ 43,500 | failed_rerating | 11.72 | -8.97 | 18.16 | -19.77 | 18.16 | -36.55 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 4
4B_case_count = 2
4C_case_count = 0
new_independent_case_count = 7
reused_case_count = 2
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 7
```

The positive set is mostly early or direct lock evidence. The counterexample set shows that HBM label exposure through socket, substrate, or material proxies can look like C06 on the surface, but without customer lock, shipment, revenue, or margin bridge it tends to generate high MAE and false Yellow/Green risk.

## 9. Evidence Source Map

| symbol | evidence family | evidence_source | status |
|---:|---|---|---|
| 000660 | direct_memory_maker_hbm3e_12l_mass_production_customer_lock | https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-begins-mass-production-12-layer-hbm3e-chips-2024-09-26/ | direct_url |
| 005930 | memory_maker_hbm3e_qualification_headline_without_margin_revision_bridge | https://www.reuters.com/technology/artificial-intelligence/samsungs-8-layer-hbm3e-chips-clear-nvidias-tests-use-sources-say-2024-08-06/ | direct_url |
| 222800 | memory_substrate_hbm_capacity_proxy_with_order_cycle_recovery | source_proxy_only:DART_IR_and_public_HBM_substrate_context_URL_repair_required | source_proxy_only; promotion_blocked_until_url_repair |
| 131290 | test_interface_hbm_customer_capacity_proxy_order_conversion | source_proxy_only:DART_IR_and_public_test_interface_HBM_context_URL_repair_required | source_proxy_only; promotion_blocked_until_url_repair |
| 095340 | hbm_test_socket_label_without_verified_customer_lock | source_proxy_only:DART_IR_and_public_HBM_socket_context_URL_repair_required | source_proxy_only; promotion_blocked_until_url_repair |
| 389260 | package_substrate_hbm_label_without_customer_capacity_bridge | source_proxy_only:DART_IR_and_public_substrate_context_URL_repair_required | source_proxy_only; promotion_blocked_until_url_repair |
| 005290 | memory_material_hbm_proxy_without_direct_customer_capacity_lock | source_proxy_only:DART_IR_and_public_memory_material_context_URL_repair_required | source_proxy_only; promotion_blocked_until_url_repair |


Direct memory-maker evidence is represented by Reuters event coverage for SK hynix 12-layer HBM3E mass production and Samsung HBM3E qualification headlines. Proxy rows intentionally remain `source_proxy_only=true` until later URL repair ties the company-specific DART/IR material to HBM customer capacity.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry_date | forward_window | CA status |
|---:|---|---|---|---:|---:|---|
| 000660 | SK하이닉스 | `atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv` | `atlas/symbol_profiles/000/000660.json` | 2024-09-26 | 180D | clean_180D_window |
| 005930 | 삼성전자 | `atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv` | `atlas/symbol_profiles/005/005930.json` | 2024-08-07 | 180D | clean_180D_window |
| 222800 | 심텍 | `atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv` | `atlas/symbol_profiles/222/222800.json` | 2024-03-22 | 180D | clean_180D_window |
| 131290 | 티에스이 | `atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv` | `atlas/symbol_profiles/131/131290.json` | 2024-03-22 | 180D | clean_180D_window |
| 095340 | ISC | `atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv` | `atlas/symbol_profiles/095/095340.json` | 2024-04-01 | 180D | clean_180D_window |
| 389260 | 대덕전자 | `atlas/ohlcv_tradable_by_symbol_year/389/389260/2024.csv` | `atlas/symbol_profiles/389/389260.json` | 2024-04-18 | 180D | clean_180D_window |
| 005290 | 동진쎄미켐 | `atlas/ohlcv_tradable_by_symbol_year/005/005290/2024.csv` | `atlas/symbol_profiles/005/005290.json` | 2024-03-22 | 180D | clean_180D_window |


## 11. Case-by-Case Trigger Grid

The case grid below is duplicated into JSONL trigger rows under Section 25.

| case_id | symbol | company | trigger | entry | role | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| C06-R2-L110-000660-20240926-HBM3E_12L_MASS_PRODUCTION_CUSTOMER_LOCK | 000660 | SK하이닉스 | Stage3-Yellow | 2024-09-26 @ 174,600 | structural_success | 11.23 | -5.10 | 26.63 | -7.90 | 43.99 | -8.25 | current_profile_too_late |
| C06-R2-L110-005930-20240807-HBM3E_CLEAR_BUT_QUALIFICATION_LAG_COUNTER | 005930 | 삼성전자 | Stage4B | 2024-08-07 @ 74,700 | failed_rerating | 3.88 | -10.71 | 4.69 | -29.05 | 13.52 | -32.26 | current_profile_false_positive |
| C06-R2-L110-222800-20240322-MEMORY_SUBSTRATE_HBM_CAPACITY_PROXY | 222800 | 심텍 | Stage2-Actionable | 2024-03-22 @ 33,150 | stage2_promote_candidate | 17.65 | -6.18 | 34.54 | -8.90 | 41.33 | -21.27 | current_profile_missed_structural |
| C06-R2-L110-131290-20240322-TEST_INTERFACE_HBM_CUSTOMER_PROXY | 131290 | 티에스이 | Stage2-Actionable | 2024-03-22 @ 58,300 | structural_success | 15.27 | -7.03 | 39.62 | -7.03 | 44.77 | -23.84 | current_profile_too_late |
| C06-R2-L110-095340-20240401-HBM_SOCKET_LABEL_WITHOUT_CUSTOMER_LOCK | 095340 | ISC | Stage3-Yellow | 2024-04-01 @ 82,100 | failed_rerating | 12.06 | -13.15 | 18.27 | -31.55 | 18.27 | -48.36 | current_profile_false_positive |
| C06-R2-L110-389260-20240418-PACKAGE_SUBSTRATE_LABEL_FALSE_YELLOW | 389260 | 대덕전자 | Stage4B | 2024-04-18 @ 25,200 | price_moved_without_evidence | 8.73 | -11.51 | 10.91 | -24.60 | 10.91 | -38.10 | current_profile_4B_too_late |
| C06-R2-L110-005290-20240322-MATERIAL_PROXY_NO_HBM_CUSTOMER_LOCK | 005290 | 동진쎄미켐 | Stage3-Yellow | 2024-03-22 @ 43,500 | failed_rerating | 11.72 | -8.97 | 18.16 | -19.77 | 18.16 | -36.55 | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

All MFE/MAE calculations use the v12 rule:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
N = 30 / 90 / 180 trading days
```

| bucket | cases | average MFE90 | average MAE90 | average MFE180 | average MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---|
| direct memory maker or strong bridge positive | 3 | 33.60 | -7.68 | 43.36 | -17.79 | works when customer/capacity bridge is visible |
| proxy/qualification counterexample | 4 | 12.51 | -26.24 | 15.22 | -38.82 | proxy label alone should not unlock Yellow/Green |
| all representative triggers | 7 | 21.55 | -18.28 | 27.28 | -29.80 | C06 needs bridge-sensitive routing |

## 13. Current Calibrated Profile Stress Test

1. The current calibrated profile would likely reward HBM relative strength and customer optionality. It may correctly handle SK hynix, but still risks overpromoting proxy rows if customer lock is not explicit.
2. The price path confirms the split: direct memory-maker lock and early substrate/test-interface proxies show acceptable MFE; proxy-only socket/material/substrate labels show poor MAE.
3. Stage2 actionable evidence bonus is useful but too generous if source_proxy_only is treated as customer lock.
4. Yellow threshold 75 is too loose for C06 proxy rows; it is acceptable for direct memory-maker HBM capacity lock.
5. Green threshold/revision rule should remain strict; this loop does not lower Green.
6. Price-only blowoff guard is strengthened for HBM label proxy rows.
7. Full 4B non-price requirement remains correct; proxy rows are watch/guardrail candidates, not automatic hard 4B unless order/qualification/margin evidence breaks.
8. Hard 4C routing is not exercised here; no Stage4C row is proposed.

## 14. Stage2 / Yellow / Green Comparison

| route | allowed stage before URL repair | allowed stage after URL repair | reason |
|---|---|---|---|
| direct memory maker HBM3E production/customer allocation | Stage2-Actionable / Stage3-Yellow | Stage3-Yellow; Green only with revision/margin | customer/capacity lock is direct, but Green still needs revision bridge |
| substrate/test-interface proxy with price path confirmation | Stage2-Actionable | Yellow only with order/revenue bridge | good MFE does not by itself prove customer lock |
| socket/material/substrate label without customer lock | Stage4B-Watch or failed-rerating review | no positive promotion | high MAE and weak MFE profile |

Stage3-Green lateness ratio is not calculated as a numeric ratio because this loop does not define a confirmed Stage3-Green trigger. All Green-related rows are treated as `not_applicable_no_confirmed_Stage3_Green_trigger`.

## 15. 4B Local vs Full-window Timing Audit

| case | trigger | local/full-window 4B treatment | verdict |
|---|---|---|---|
| 005930 Samsung qualification headline | Stage4B | qualification headline without confirmed Nvidia volume/margin bridge | good 4B-watch; not hard 4C |
| 389260 Daeduck substrate label | Stage4B | shallow MFE and deep MAE after local label spike | local 4B-watch needed |
| proxy rows 095340 / 005290 | Stage3-Yellow stress rows | not Stage4B by label, but shadow rule would downgrade to Watch | current profile false-positive risk |

## 16. 4C Protection Audit

No hard Stage4C row is emitted. This loop is about C06 positive-stage eligibility and 4B-watch routing, not confirmed thesis break. `hard_4c_confirmation` is kept, not weakened.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
rule_candidate = In L2, HBM-related proxy labels must not receive Yellow/Green credit unless customer/shipment/revenue/margin evidence links the proxy to actual HBM capacity allocation.
```

This is not a global rule; it is specific to the semiconductor/HBM evidence chain where the market often prices the second-order proxy before customer allocation is visible.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
new_axis_proposed = C06_direct_HBM_customer_capacity_lock_or_verified_substrate_socket_material_shipment_bridge_required_before_Yellow_or_Green
```

Implementation meaning for a later coding batch:

```text
if canonical_archetype_id == C06 and evidence is direct memory-maker customer/capacity lock:
    allow Stage2-Actionable and possible Yellow when revision/margin bridge exists
if canonical_archetype_id == C06 and evidence is substrate/socket/material proxy only:
    cap at Stage2-Actionable before URL repair
    if late relative strength + no customer lock + high MAE pattern: route to Stage4B-Watch
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | existing global axes only | 7 | 22.31 | -18.91 | 0.57 | too permissive for proxy labels, too late for direct SK hynix lock |
| P0b_e2r_2_0_baseline_reference | rollback reference | no stock-web calibration | 7 | 22.31 | -18.91 | 0.71 | worse; lets relative strength over-promote |
| P1_L2_sector_shadow_profile | sector shadow | require verified order/revenue/margin bridge for Yellow | 7 | 31.04 | -11.38 | 0.29 | improves C06/C07/C09 separation |
| P2_C06_canonical_shadow_profile | canonical shadow | direct customer lock or verified proxy bridge before Yellow/Green | 7 | 33.60 | -7.68 | 0.14 | best alignment for this loop |
| P3_counterexample_guard_profile | guardrail | proxy-only HBM labels route to Stage4B-Watch | 4 counterexamples | 12.51 | -26.24 | 0.00 | strong guardrail, may be too conservative for early substrate winners |


## 20. Score-Return Alignment Matrix

| case type | before alignment | after shadow alignment | reason |
|---|---|---|---|
| direct memory-maker HBM lock | sometimes too late | better | customer/capacity lock is allowed to carry more C06 weight |
| supply-chain proxy with early evidence | mixed | Stage2-only until URL repair | avoids overpromoting proxy rows |
| HBM socket/material/substrate label only | false positive | filtered to Watch | relative strength is no longer enough |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK | 3 | 4 | 2 | 0 | 7 | 2 | 7 | 7 | 7 | true | true | C06 local-session adjusted about 38; 12 short of 50 |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 2
reused_case_ids: C06-R2-L110-000660-20240926-HBM3E_12L_MASS_PRODUCTION_CUSTOMER_LOCK, C06-R2-L110-005930-20240807-HBM3E_CLEAR_BUT_QUALIFICATION_LAG_COUNTER
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: proxy_label_false_yellow, direct_memory_maker_stage_too_late, qualification_headline_false_positive, substrate_socket_material_proxy_missing_customer_lock
new_axis_proposed: C06_direct_HBM_customer_capacity_lock_or_verified_substrate_socket_material_shipment_bridge_required_before_Yellow_or_Green
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 7 new independent trigger families, 4 counterexamples, and 6 residual errors for R2/L2/C06.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical trigger-level calibration only
- Stock-Web tradable_raw OHLC path fields included
- C06 evidence compression and residual error labeling
- Shadow-only sector/canonical rule candidate
```

Non-validation scope:

```text
- No current/live recommendation
- No production scoring patch
- No brokerage/API/auto-trading action
- No new price route discovery
- Proxy-only evidence rows require later URL repair before positive promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_verified_customer_capacity_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Require direct HBM customer/capacity lock or verified proxy shipment/revenue/margin bridge before Yellow/Green","filters four proxy false positives while preserving three positive bridge cases","TRG-C06-L110-000660-Stage3Yellow-2024-09-26|TRG-C06-L110-005930-Stage4B-2024-08-07|TRG-C06-L110-222800-Stage2Actionable-2024-03-22|TRG-C06-L110-131290-Stage2Actionable-2024-03-22|TRG-C06-L110-095340-Stage3Yellow-2024-04-01|TRG-C06-L110-389260-Stage4B-2024-04-18|TRG-C06-L110-005290-Stage3Yellow-2024-03-22",7,7,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","source_name":"FinanceData/marcap","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414}
{"row_type":"case","case_id":"C06-R2-L110-000660-20240926-HBM3E_12L_MASS_PRODUCTION_CUSTOMER_LOCK","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C06-L110-000660-Stage3Yellow-2024-09-26","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_direct_memory_maker","independent_evidence_weight":0.5,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C06 loop110 reused direct memory maker with new trigger family; source_proxy_only=false"}
{"row_type":"case","case_id":"C06-R2-L110-005930-20240807-HBM3E_CLEAR_BUT_QUALIFICATION_LAG_COUNTER","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG-C06-L110-005930-Stage4B-2024-08-07","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_direct_memory_maker","independent_evidence_weight":0.5,"score_price_alignment":"false_positive_or_4B_guardrail_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C06 loop110 reused direct memory maker with new trigger family; source_proxy_only=false"}
{"row_type":"case","case_id":"C06-R2-L110-222800-20240322-MEMORY_SUBSTRATE_HBM_CAPACITY_PROXY","symbol":"222800","company_name":"심텍","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"TRG-C06-L110-222800-Stage2Actionable-2024-03-22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"C06 loop110 new symbol/supply-chain proxy; source_proxy_only=true"}
{"row_type":"case","case_id":"C06-R2-L110-131290-20240322-TEST_INTERFACE_HBM_CUSTOMER_PROXY","symbol":"131290","company_name":"티에스이","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C06-L110-131290-Stage2Actionable-2024-03-22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C06 loop110 new symbol/supply-chain proxy; source_proxy_only=true"}
{"row_type":"case","case_id":"C06-R2-L110-095340-20240401-HBM_SOCKET_LABEL_WITHOUT_CUSTOMER_LOCK","symbol":"095340","company_name":"ISC","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG-C06-L110-095340-Stage3Yellow-2024-04-01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_4B_guardrail_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C06 loop110 new symbol/supply-chain proxy; source_proxy_only=true"}
{"row_type":"case","case_id":"C06-R2-L110-389260-20240418-PACKAGE_SUBSTRATE_LABEL_FALSE_YELLOW","symbol":"389260","company_name":"대덕전자","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"TRG-C06-L110-389260-Stage4B-2024-04-18","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_4B_guardrail_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"C06 loop110 new symbol/supply-chain proxy; source_proxy_only=true"}
{"row_type":"case","case_id":"C06-R2-L110-005290-20240322-MATERIAL_PROXY_NO_HBM_CUSTOMER_LOCK","symbol":"005290","company_name":"동진쎄미켐","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG-C06-L110-005290-Stage3Yellow-2024-03-22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_4B_guardrail_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C06 loop110 new symbol/supply-chain proxy; source_proxy_only=true"}
{"row_type":"trigger","trigger_id":"TRG-C06-L110-000660-Stage3Yellow-2024-09-26","case_id":"C06-R2-L110-000660-20240926-HBM3E_12L_MASS_PRODUCTION_CUSTOMER_LOCK","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-09-26","entry_date":"2024-09-26","entry_price":174600,"evidence_available_at_that_date":"direct_memory_maker_hbm3e_12l_mass_production_customer_lock","evidence_source":"https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-begins-mass-production-12-layer-hbm3e-chips-2024-09-26/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["durable_customer_confirmation","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.23,"MFE_90D_pct":26.63,"MFE_180D_pct":43.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.1,"MAE_90D_pct":-7.9,"MAE_180D_pct":-8.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-17","peak_price":251400,"drawdown_after_peak_pct":-52.24,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"direct_memory_maker_hbm3e_12l_mass_production_customer_lock_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_profile_check","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage3-Yellow|2024-09-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_direct_memory_maker","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","trigger_id":"TRG-C06-L110-005930-Stage4B-2024-08-07","case_id":"C06-R2-L110-005930-20240807-HBM3E_CLEAR_BUT_QUALIFICATION_LAG_COUNTER","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-08-07","entry_date":"2024-08-07","entry_price":74700,"evidence_available_at_that_date":"memory_maker_hbm3e_qualification_headline_without_margin_revision_bridge","evidence_source":"https://www.reuters.com/technology/artificial-intelligence/samsungs-8-layer-hbm3e-chips-clear-nvidias-tests-use-sources-say-2024-08-06/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["qualification_lag","price_only_local_peak","margin_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.88,"MFE_90D_pct":4.69,"MFE_180D_pct":13.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.71,"MAE_90D_pct":-29.05,"MAE_180D_pct":-32.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-26","peak_price":84800,"drawdown_after_peak_pct":-45.78,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"local_4B_watch_or_failed_rerating_guardrail","four_b_evidence_type":"price_only|customer_lock_missing|margin_bridge_missing","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"memory_maker_hbm3e_qualification_headline_without_margin_revision_bridge_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_profile_check","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage4B|2024-08-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_direct_memory_maker","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","trigger_id":"TRG-C06-L110-222800-Stage2Actionable-2024-03-22","case_id":"C06-R2-L110-222800-20240322-MEMORY_SUBSTRATE_HBM_CAPACITY_PROXY","symbol":"222800","company_name":"심텍","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":33150,"evidence_available_at_that_date":"memory_substrate_hbm_capacity_proxy_with_order_cycle_recovery","evidence_source":"source_proxy_only:DART_IR_and_public_HBM_substrate_context_URL_repair_required","stage2_evidence_fields":["capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion_proxy"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv","profile_path":"atlas/symbol_profiles/222/222800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.65,"MFE_90D_pct":34.54,"MFE_180D_pct":41.33,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.18,"MAE_90D_pct":-8.9,"MAE_180D_pct":-21.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-09","peak_price":46850,"drawdown_after_peak_pct":-62.6,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"memory_substrate_hbm_capacity_proxy_with_order_cycle_recovery_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_profile_check","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|222800|Stage2-Actionable|2024-03-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","trigger_id":"TRG-C06-L110-131290-Stage2Actionable-2024-03-22","case_id":"C06-R2-L110-131290-20240322-TEST_INTERFACE_HBM_CUSTOMER_PROXY","symbol":"131290","company_name":"티에스이","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":58300,"evidence_available_at_that_date":"test_interface_hbm_customer_capacity_proxy_order_conversion","evidence_source":"source_proxy_only:DART_IR_and_public_test_interface_HBM_context_URL_repair_required","stage2_evidence_fields":["customer_or_order_quality_proxy","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["repeat_order_or_conversion_proxy","financial_visibility_proxy"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.27,"MFE_90D_pct":39.62,"MFE_180D_pct":44.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.03,"MAE_90D_pct":-7.03,"MAE_180D_pct":-23.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":84400,"drawdown_after_peak_pct":-68.61,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"test_interface_hbm_customer_capacity_proxy_order_conversion_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_profile_check","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|131290|Stage2-Actionable|2024-03-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","trigger_id":"TRG-C06-L110-095340-Stage3Yellow-2024-04-01","case_id":"C06-R2-L110-095340-20240401-HBM_SOCKET_LABEL_WITHOUT_CUSTOMER_LOCK","symbol":"095340","company_name":"ISC","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":82100,"evidence_available_at_that_date":"hbm_test_socket_label_without_verified_customer_lock","evidence_source":"source_proxy_only:DART_IR_and_public_HBM_socket_context_URL_repair_required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","customer_lock_missing","large_90D_180D_MAE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.06,"MFE_90D_pct":18.27,"MFE_180D_pct":18.27,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.15,"MAE_90D_pct":-31.55,"MAE_180D_pct":-48.36,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-22","peak_price":97100,"drawdown_after_peak_pct":-66.63,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"hbm_test_socket_label_without_verified_customer_lock_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_profile_check","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|095340|Stage3-Yellow|2024-04-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","trigger_id":"TRG-C06-L110-389260-Stage4B-2024-04-18","case_id":"C06-R2-L110-389260-20240418-PACKAGE_SUBSTRATE_LABEL_FALSE_YELLOW","symbol":"389260","company_name":"대덕전자","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":25200,"evidence_available_at_that_date":"package_substrate_hbm_label_without_customer_capacity_bridge","evidence_source":"source_proxy_only:DART_IR_and_public_substrate_context_URL_repair_required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","order_revenue_bridge_missing","large_180D_MAE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/389/389260/2024.csv","profile_path":"atlas/symbol_profiles/389/389260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.73,"MFE_90D_pct":10.91,"MFE_180D_pct":10.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.51,"MAE_90D_pct":-24.6,"MAE_180D_pct":-38.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":27950,"drawdown_after_peak_pct":-49.01,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"local_4B_watch_or_failed_rerating_guardrail","four_b_evidence_type":"price_only|customer_lock_missing|margin_bridge_missing","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"package_substrate_hbm_label_without_customer_capacity_bridge_counterexample","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_profile_check","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|389260|Stage4B|2024-04-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","trigger_id":"TRG-C06-L110-005290-Stage3Yellow-2024-03-22","case_id":"C06-R2-L110-005290-20240322-MATERIAL_PROXY_NO_HBM_CUSTOMER_LOCK","symbol":"005290","company_name":"동진쎄미켐","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","deep_sub_archetype_id":"C06_DEEP_HBM3E_12L_MEMORY_MAKER_SUPPLY_LOCK_VS_SUBSTRATE_SOCKET_MATERIAL_PROXY_QUALIFICATION_LAG","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"HBM_memory_customer_capacity","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":43500,"evidence_available_at_that_date":"memory_material_hbm_proxy_without_direct_customer_capacity_lock","evidence_source":"source_proxy_only:DART_IR_and_public_memory_material_context_URL_repair_required","stage2_evidence_fields":["policy_or_regulatory_optionality_proxy","capacity_or_volume_route_proxy","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["order_bridge_missing","margin_bridge_missing","large_180D_MAE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005290/2024.csv","profile_path":"atlas/symbol_profiles/005/005290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.72,"MFE_90D_pct":18.16,"MFE_180D_pct":18.16,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.97,"MAE_90D_pct":-19.77,"MAE_180D_pct":-36.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":51400,"drawdown_after_peak_pct":-54.71,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"memory_material_hbm_proxy_without_direct_customer_capacity_lock_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_profile_check","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005290|Stage3-Yellow|2024-03-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C06_shadow","case_id":"C06-R2-L110-000660-20240926-HBM3E_12L_MASS_PRODUCTION_CUSTOMER_LOCK","trigger_id":"TRG-C06-L110-000660-Stage3Yellow-2024-09-26","symbol":"000660","company_name":"SK하이닉스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":60,"revision_score":58,"relative_strength_score":78,"customer_quality_score":82,"policy_or_regulatory_score":16,"valuation_repricing_score":58,"execution_risk_score":34,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":75,"qualification_lag_risk_score":22},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":64,"revision_score":58,"relative_strength_score":78,"customer_quality_score":86,"policy_or_regulatory_score":16,"valuation_repricing_score":54,"execution_risk_score":34,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":75,"qualification_lag_risk_score":22},"weighted_score_after":76.5,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","qualification_lag_risk_score"],"component_delta_explanation":"C06 shadow profile separates direct HBM memory-maker customer/capacity lock from substrate/socket/material proxy labels. Proxy-only labels cannot unlock Yellow/Green until customer, shipment, revenue, or margin bridge is URL-verified.","MFE_90D_pct":26.63,"MAE_90D_pct":-7.9,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C06_shadow","case_id":"C06-R2-L110-005930-20240807-HBM3E_CLEAR_BUT_QUALIFICATION_LAG_COUNTER","trigger_id":"TRG-C06-L110-005930-Stage4B-2024-08-07","symbol":"005930","company_name":"삼성전자","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":82,"customer_quality_score":42,"policy_or_regulatory_score":16,"valuation_repricing_score":76,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":48,"qualification_lag_risk_score":74},"weighted_score_before":74.0,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":60,"customer_quality_score":42,"policy_or_regulatory_score":16,"valuation_repricing_score":50,"execution_risk_score":86,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":48,"qualification_lag_risk_score":82},"weighted_score_after":47.5,"stage_label_after":"Stage4B-Watch","changed_components":["customer_quality_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","qualification_lag_risk_score"],"component_delta_explanation":"C06 shadow profile separates direct HBM memory-maker customer/capacity lock from substrate/socket/material proxy labels. Proxy-only labels cannot unlock Yellow/Green until customer, shipment, revenue, or margin bridge is URL-verified.","MFE_90D_pct":4.69,"MAE_90D_pct":-29.05,"score_return_alignment_label":"counterexample_filtered_to_4B_watch","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C06_shadow","case_id":"C06-R2-L110-222800-20240322-MEMORY_SUBSTRATE_HBM_CAPACITY_PROXY","trigger_id":"TRG-C06-L110-222800-Stage2Actionable-2024-03-22","symbol":"222800","company_name":"심텍","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":60,"revision_score":58,"relative_strength_score":78,"customer_quality_score":64,"policy_or_regulatory_score":16,"valuation_repricing_score":58,"execution_risk_score":34,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":75,"qualification_lag_risk_score":22},"weighted_score_before":70.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":54,"revision_score":58,"relative_strength_score":78,"customer_quality_score":56,"policy_or_regulatory_score":16,"valuation_repricing_score":54,"execution_risk_score":34,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":75,"qualification_lag_risk_score":22},"weighted_score_after":68.0,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","qualification_lag_risk_score"],"component_delta_explanation":"C06 shadow profile separates direct HBM memory-maker customer/capacity lock from substrate/socket/material proxy labels. Proxy-only labels cannot unlock Yellow/Green until customer, shipment, revenue, or margin bridge is URL-verified.","MFE_90D_pct":34.54,"MAE_90D_pct":-8.9,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C06_shadow","case_id":"C06-R2-L110-131290-20240322-TEST_INTERFACE_HBM_CUSTOMER_PROXY","trigger_id":"TRG-C06-L110-131290-Stage2Actionable-2024-03-22","symbol":"131290","company_name":"티에스이","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":60,"revision_score":58,"relative_strength_score":78,"customer_quality_score":64,"policy_or_regulatory_score":16,"valuation_repricing_score":58,"execution_risk_score":34,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":75,"qualification_lag_risk_score":22},"weighted_score_before":70.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":54,"revision_score":58,"relative_strength_score":78,"customer_quality_score":56,"policy_or_regulatory_score":16,"valuation_repricing_score":54,"execution_risk_score":34,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":75,"qualification_lag_risk_score":22},"weighted_score_after":68.0,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","qualification_lag_risk_score"],"component_delta_explanation":"C06 shadow profile separates direct HBM memory-maker customer/capacity lock from substrate/socket/material proxy labels. Proxy-only labels cannot unlock Yellow/Green until customer, shipment, revenue, or margin bridge is URL-verified.","MFE_90D_pct":39.62,"MAE_90D_pct":-7.03,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C06_shadow","case_id":"C06-R2-L110-095340-20240401-HBM_SOCKET_LABEL_WITHOUT_CUSTOMER_LOCK","trigger_id":"TRG-C06-L110-095340-Stage3Yellow-2024-04-01","symbol":"095340","company_name":"ISC","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":82,"customer_quality_score":42,"policy_or_regulatory_score":16,"valuation_repricing_score":76,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":48,"qualification_lag_risk_score":74},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":60,"customer_quality_score":42,"policy_or_regulatory_score":16,"valuation_repricing_score":50,"execution_risk_score":86,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":48,"qualification_lag_risk_score":82},"weighted_score_after":47.5,"stage_label_after":"Stage4B-Watch","changed_components":["customer_quality_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","qualification_lag_risk_score"],"component_delta_explanation":"C06 shadow profile separates direct HBM memory-maker customer/capacity lock from substrate/socket/material proxy labels. Proxy-only labels cannot unlock Yellow/Green until customer, shipment, revenue, or margin bridge is URL-verified.","MFE_90D_pct":18.27,"MAE_90D_pct":-31.55,"score_return_alignment_label":"counterexample_filtered_to_4B_watch","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C06_shadow","case_id":"C06-R2-L110-389260-20240418-PACKAGE_SUBSTRATE_LABEL_FALSE_YELLOW","trigger_id":"TRG-C06-L110-389260-Stage4B-2024-04-18","symbol":"389260","company_name":"대덕전자","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":82,"customer_quality_score":42,"policy_or_regulatory_score":16,"valuation_repricing_score":76,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":48,"qualification_lag_risk_score":74},"weighted_score_before":74.0,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":60,"customer_quality_score":42,"policy_or_regulatory_score":16,"valuation_repricing_score":50,"execution_risk_score":86,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":48,"qualification_lag_risk_score":82},"weighted_score_after":47.5,"stage_label_after":"Stage4B-Watch","changed_components":["customer_quality_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","qualification_lag_risk_score"],"component_delta_explanation":"C06 shadow profile separates direct HBM memory-maker customer/capacity lock from substrate/socket/material proxy labels. Proxy-only labels cannot unlock Yellow/Green until customer, shipment, revenue, or margin bridge is URL-verified.","MFE_90D_pct":10.91,"MAE_90D_pct":-24.6,"score_return_alignment_label":"counterexample_filtered_to_4B_watch","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C06_shadow","case_id":"C06-R2-L110-005290-20240322-MATERIAL_PROXY_NO_HBM_CUSTOMER_LOCK","trigger_id":"TRG-C06-L110-005290-Stage3Yellow-2024-03-22","symbol":"005290","company_name":"동진쎄미켐","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":82,"customer_quality_score":42,"policy_or_regulatory_score":16,"valuation_repricing_score":76,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":48,"qualification_lag_risk_score":74},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":38,"backlog_visibility_score":34,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":60,"customer_quality_score":42,"policy_or_regulatory_score":16,"valuation_repricing_score":50,"execution_risk_score":86,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8,"capacity_or_shipment_score":48,"qualification_lag_risk_score":82},"weighted_score_after":47.5,"stage_label_after":"Stage4B-Watch","changed_components":["customer_quality_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","qualification_lag_risk_score"],"component_delta_explanation":"C06 shadow profile separates direct HBM memory-maker customer/capacity lock from substrate/socket/material proxy labels. Proxy-only labels cannot unlock Yellow/Green until customer, shipment, revenue, or margin bridge is URL-verified.","MFE_90D_pct":18.16,"MAE_90D_pct":-19.77,"score_return_alignment_label":"counterexample_filtered_to_4B_watch","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"aggregate","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_SUBSTRATE_SOCKET_MATERIAL_PROXY_BRIDGE_VS_DIRECT_CUSTOMER_LOCK","calibration_usable_trigger_count":7,"representative_trigger_count":7,"new_independent_case_count":7,"reused_case_count":2,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":7,"new_trigger_family_count":7,"positive_case_count":3,"counterexample_count":4,"stage4b_case_count":2,"stage4c_case_count":0,"current_profile_error_count":7,"source_proxy_only_count":5,"evidence_url_pending_count":5,"narrative_only_or_rejected_count":0,"auto_selected_coverage_gap":"C06 base index 17 + local loop108 7 + local loop109 7 + loop110 7 = local-session adjusted about 38; above 30-row stability band, about 12 short of 50-row practical calibration band","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"new_axis_proposed":"C06_direct_HBM_customer_capacity_lock_or_verified_substrate_socket_material_shipment_bridge_required_before_Yellow_or_Green","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_weakened":null}
{"row_type":"residual_contribution","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":7,"reused_case_count":2,"new_symbol_count":5,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["proxy_label_false_yellow","direct_memory_maker_stage_too_late","qualification_headline_false_positive","substrate_socket_material_proxy_missing_customer_lock"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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
completed_round = R2
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

Next execution should again read the latest No-Repeat Index and local session outputs rather than mechanically proceeding through R1~R13.

## 28. Source Notes

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat / coverage ledger: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price atlas manifest: `Songdaiki/stock-web/atlas/manifest.json`.
- Direct event evidence examples used for C06 context: Reuters SK hynix HBM3E 12-layer mass production, Reuters SK hynix HBM sold-out/capacity allocation, Reuters Samsung HBM3E Nvidia qualification headline.
- Proxy rows are intentionally marked `source_proxy_only=true` and `evidence_url_pending=true` until later URL repair.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
