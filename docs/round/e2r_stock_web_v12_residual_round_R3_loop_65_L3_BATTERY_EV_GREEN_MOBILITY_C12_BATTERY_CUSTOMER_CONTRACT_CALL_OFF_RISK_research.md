# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
repo_session = later_batch_implementation_only
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

- round: `R3`
- loop: `65`
- large_sector_id: `L3_BATTERY_EV_GREEN_MOBILITY`
- canonical_archetype_id: `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`
- fine_archetype_id: `CELL_SEPARATOR_CUSTOMER_ORDER_CALL_OFF_SLOWDOWN`
- loop_objective: `counterexample_mining`, `4C_thesis_break_timing_test`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `coverage_gap_fill`
- validation basis: historical trigger-level OHLC backtest, not live candidate discovery.
- non-validation scope: no current recommendation, no watchlist, no `stock_agent` source-code inspection, no production patch, no broker/API/autotrading.

이번 loop는 직전 C14 EV-demand-slowdown 연구와 겹치지 않도록, 완성차 수요 둔화 자체가 아니라 **고객사의 발주 지연·출하 감소·증설 속도 조절이 소재/셀/분리막 업체의 실적·가동률로 전이되는 C12 위험**을 본다. 물이 얼음으로 바뀌는 순간처럼, 뉴스 문장 하나가 아니라 고객의 실제 주문 리듬이 멈추면서 재고·가동률·마진이 함께 굳는지를 확인한다.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

v12의 목적은 위 global axis를 다시 증명하는 것이 아니다. 이번 연구는 C12 안에서 **hard 4C로 바로 보내야 하는 고객 call-off류 신호**와, **broad EV slowdown이지만 아직 고객별 call-off로 닫히지 않은 false-hard4C 신호**를 분리한다.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R3 |
| loop | 65 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK |
| fine_archetype_id | CELL_SEPARATOR_CUSTOMER_ORDER_CALL_OFF_SLOWDOWN |
| selected symbols | `361610` SK아이이테크놀로지, `006400` 삼성SDI, `373220` LG에너지솔루션 |
| case balance | positive risk detection 2, counterexample 1 |
| selected trigger families | customer shipment fall, weak customer EV demand, capacity expansion slowdown without direct call-off |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifact access was limited to coverage-gap/duplicate-avoidance search only. Repository source code was not opened. A direct artifact/code-search query for `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` returned no visible prior result in the accessible snapshot. Therefore this loop uses C12 as a coverage-gap fill rather than re-materializing an existing representative row.

```text
auto_selected_coverage_gap = C12 customer contract/call-off risk lacks visible prior residual file in accessible search snapshot
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest confirms the price atlas is generated from FinanceData/marcap, uses raw/unadjusted marcap OHLC, has `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `raw_row_count = 15214118`, `symbol_count = 5414`, and calibration shards under `atlas/ohlcv_tradable_by_symbol_year`. The manifest also states that zero-volume and invalid OHLC rows are excluded from calibration shards and corporate-action-contaminated windows are blocked by default. The schema defines tradable shard columns as `d,o,h,l,c,v,a,mc,s,m`, and gives the same MFE/MAE formulas used here.
Source validation references: manifest `atlas/manifest.json`; schema `atlas/schema.json`.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| symbol | profile_path | entry_date | 180D window | corporate-action status | calibration_usable |
|---|---|---:|---:|---|---:|
| 361610 | atlas/symbol_profiles/361/361610.json | 2024-05-16 | available | clean_180D_window; profile has 0 candidate dates | true |
| 006400 | atlas/symbol_profiles/006/006400.json | 2024-06-26 | available | profile has old candidate dates only: 1996-01-03, 1998-11-03, 2014-07-15; no overlap | true |
| 373220 | atlas/symbol_profiles/373/373220.json | 2024-07-25 | available | clean_180D_window; profile has 0 candidate dates | true |

All representative triggers have positive OHLCV, entry rows inside tradable shards, and at least 180 forward trading days before the stock-web manifest max date.

## 6. Canonical Archetype Compression Map

| fine signal | canonical mapping | explanation |
|---|---|---|
| EV customer shipment fall | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 고객사의 실제 출하/주문 속도가 줄면 계약·capacity의 nominal value가 실적 visibility로 닫히지 않는다. |
| separator utilization pressure | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 분리막은 customer call-off가 곧 가동률·마진 압박으로 번역된다. |
| broad EV slowdown but policy/supply-chain offset | C12 counterexample guard | 고객별 주문 취소 없이 sector headline만 있는 경우 hard 4C는 너무 이르다. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger | summary |
|---|---:|---|---|---|---|---|
| C12-R3L65-361610 | 361610 | SK아이이테크놀로지 | 4C_success | positive | 2024-05-16 | SK On/EV shipment weakness plus possible SKIET disposal narrative; separator demand-quality route breaks. |
| C12-R3L65-006400 | 006400 | 삼성SDI | 4C_success | positive | 2024-06-26 | Europe-heavy EV customer exposure and expected earnings pressure; customer concentration makes slowdown investable as risk. |
| C12-R3L65-373220 | 373220 | LG에너지솔루션 | false_break | counterexample | 2024-07-25 | Weak EV demand and expansion slowdown were real, but no direct customer call-off was confirmed; stock first rerated upward. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
new_independent_case_count = 3
reused_case_count = 0
```

- Positive risk-detection cases: SK아이이테크놀로지 and 삼성SDI. In both cases, customer demand/order rhythm translated into large subsequent downside.
- Counterexample: LG에너지솔루션. Broad demand slowdown was public, but the same report also contained supply-chain/policy-offset logic and the market first repriced upward; a hard 4C label on the first headline would have been too blunt.

## 9. Evidence Source Map

| case_id | evidence_source | evidence_available_at_that_date | stage2 fields | stage3 fields | stage4b/4c fields |
|---|---|---|---|---|---|
| C12-R3L65-361610 | Reuters, 2024-05-15, SK Innovation considering sale of SKIET; notes weakening EV demand and SK On shipments fell | after Korea close; next-trading-day entry 2024-05-16 | public_event_or_disclosure, customer_or_order_quality | financial_visibility, low_red_team_risk | margin_or_backlog_slowdown, thesis_evidence_broken |
| C12-R3L65-006400 | MarketWatch/WSJ Market Talk, 2024-06-25, Samsung SDI Europe customer exposure may weigh on 2Q earnings | near/after close; next-trading-day entry 2024-06-26 | customer_or_order_quality, early_revision_signal | financial_visibility, multiple_public_sources | margin_or_backlog_slowdown, thesis_evidence_broken |
| C12-R3L65-373220 | Reuters, 2024-07-25, LGES cuts annual sales target and eases capacity expansion on weak EV demand | intraday Korea; same-day close entry 2024-07-25 | public_event_or_disclosure, policy_or_regulatory_optionality | financial_visibility | price_only_local_peak, broad_sector_slowdown_without_customer_calloff |

Evidence source URLs are recorded in the machine-readable rows. This file does not use later outcomes to revise the trigger date.

## 10. Price Data Source Map

| symbol | price_shard_path | entry_date | entry_price | profile_path |
|---:|---|---:|---:|---|
| 361610 | atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv | 2024-05-16 | 57600 | atlas/symbol_profiles/361/361610.json |
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | 2024-06-26 | 369000 | atlas/symbol_profiles/006/006400.json |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | 2024-07-25 | 332500 | atlas/symbol_profiles/373/373220.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | current_profile_verdict | trigger_outcome_label |
|---|---:|---|---:|---:|---:|---|---|
| C12-R3L65-361610-T1 | 361610 | Stage4C-Watch | 2024-05-15 | 2024-05-16 | 57600 | current_profile_too_late | hard_4c_success |
| C12-R3L65-006400-T1 | 006400 | Stage4C-Watch | 2024-06-25 | 2024-06-26 | 369000 | current_profile_too_late | hard_4c_success |
| C12-R3L65-373220-T1 | 373220 | Stage2-RiskWatch | 2024-07-25 | 2024-07-25 | 332500 | current_profile_false_positive | false_break |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE are computed from the entry close, using stock-web tradable raw high/low rows. The values are rounded to two decimals.

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C12-R3L65-361610-T1 | 57,600 | +1.04% | -25.87% | +1.04% | -48.26% | +1.04% | -62.41% | +1.04% | -66.48% | 2024-05-16 | 58,200 | -66.82% |
| C12-R3L65-006400-T1 | 369,000 | +5.69% | -20.19% | +6.64% | -20.19% | +6.64% | -49.38% | +6.64% | -57.26% | 2024-09-30 | 393,500 | -59.92% |
| C12-R3L65-373220-T1 | 332,500 | +25.98% | -6.47% | +33.53% | -6.47% | +33.53% | -6.62% | +33.53% | -20.00% | 2024-10-08 | 444,000 | -40.09% |

Interpretation: C12 is not “EV slowdown headline = sell.” The useful split is closer to a valve: if the customer order-flow valve actually closes, downstream OHLC tends to leak quickly; if the headline is broad but policy/geography/customer mix still keeps flow open, hard 4C is too blunt.

## 13. Current Calibrated Profile Stress Test

| case_id | P0 expected behavior | actual alignment | verdict |
|---|---|---|---|
| C12-R3L65-361610 | P0 may keep as risk overlay until non-price evidence deepens | MAE_90D -48.26%, MAE_180D -62.41%; earlier hard 4C would protect | current_profile_too_late |
| C12-R3L65-006400 | P0 may tag as Yellow/RiskWatch, not hard 4C, because signal begins as analyst channel | MAE_180D -49.38%; customer concentration + Europe exposure made risk real | current_profile_too_late |
| C12-R3L65-373220 | P0 hard 4C risk if it overweights broad EV slowdown and annual target cut | MFE_90D +33.53% before later drawdown; hard 4C on trigger would be false early break | current_profile_false_positive |

Answers to required stress-test questions:

1. P0 is broadly correct that price-only blowoff should not promote positive stages.
2. P0 is too slow for C12 when customer shipment/order evidence and utilization/margin stress appear together.
3. Stage2 actionable bonus is not the issue here; this is a 4C routing precision problem.
4. Yellow threshold 75 is acceptable for broad slowdown, but too permissive if it upgrades broad slowdown to hard 4C without customer-specific call-off.
5. Green threshold 87 / revision 55 is not the main axis; C12 is a risk/4C overlay.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement is strengthened: customer/order evidence matters.
8. Hard 4C routing is too late for SKIET/SamsungSDI but too early for LGES unless customer-specific call-off is confirmed.

## 14. Stage2 / Yellow / Green Comparison

No positive Stage3-Green trigger is proposed. C12 signals are risk overlays, not long-entry promotions.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger; cases are 4B/4C risk calibration rows
```

For SamsungSDI and SKIET, Stage2-RiskWatch would not be enough if the model waits for confirmed accounting damage; by the time the damage is cleanly reported, the drawdown has often already moved. For LGES, however, the same early risk headline should not become hard 4C without customer-specific cancellation or shipment-collapse proof.

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence type | local peak proximity | full-window peak proximity | verdict |
|---|---|---:|---:|---|
| C12-R3L65-361610 | margin_or_backlog_slowdown, thesis_evidence_broken | n/a | n/a | not a 4B peak case; hard 4C risk route |
| C12-R3L65-006400 | margin_or_backlog_slowdown, customer concentration | 0.97 | 0.97 | risk overlay near limited upside; good protection if treated as 4C-watch |
| C12-R3L65-373220 | price_only, broad slowdown | 0.94 | 0.94 | local/full price peak came later; initial trigger should be Stage2-RiskWatch, not full 4B/4C |

## 16. 4C Protection Audit

| case_id | 4C label | protection interpretation |
|---|---|---|
| C12-R3L65-361610 | hard_4c_success | Early customer/order-quality deterioration protected from a -62% 180D path. |
| C12-R3L65-006400 | hard_4c_success | Europe customer concentration signal protected from a -49% 180D path. |
| C12-R3L65-373220 | false_break | Hard 4C on broad slowdown would have missed +33.5% upside first; only later drawdown validates risk-watch, not immediate thesis-break. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = c12_customer_order_flow_hard4c_promoter
baseline_value = 0
tested_value = +1
delta = +1
confidence = medium-low
proposal_type = sector_shadow_only
```

Proposed sector rule candidate:

> In L3 battery/EV materials, if a trigger contains at least two non-price elements among customer shipment fall, customer-specific demand cut, utilization decline, margin collapse, and capacity expansion delay tied to actual customer order cadence, promote the risk overlay from generic 4B-watch to C12 hard-4C-watch.

Counter-guard:

> If the evidence is broad EV slowdown, policy uncertainty, or sector sentiment without customer-specific order-flow break, cap it at Stage2-RiskWatch / 4B-watch and do not route to hard 4C.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
axis = c12_direct_calloff_vs_broad_slowdown_split
baseline_value = absent
tested_value = enabled
delta = split hard4C promotion and false-hard4C guard
confidence = medium
```

C12 should not score “customer risk” as a single bucket. It should split:

1. **Direct call-off / shipment-fall / utilization-collapse route**: hard 4C-watch eligible.
2. **Broad EV demand slowdown route**: risk-watch only unless customer-specific conversion failure is present.
3. **Policy/geography offset route**: explicitly guard against false hard 4C.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global proxy | 3 | +13.74% | -24.97% | +13.74% | -39.47% | 0.33 | 2 | mixed; misses direct C12 risk and over-penalizes broad LGES slowdown |
| P0b_e2r_2_0_baseline_reference | rollback | 3 | +13.74% | -24.97% | +13.74% | -39.47% | 0.33 | 2 | worse timing; no clean C12 split |
| P1_L3_sector_specific_candidate | sector | 3 | +13.74% | -24.97% | +13.74% | -39.47% | 0.00 | 1 | improves by guarding LGES false-hard4C |
| P2_C12_archetype_candidate | canonical | 3 | +13.74% | -24.97% | +13.74% | -39.47% | 0.00 | 0 | best explanatory alignment; routes SKIET/SamsungSDI to hard4C-watch and LGES to risk-watch |
| P3_counterexample_guard_profile | guard | 1 counterexample focused | +33.53% | -6.47% | +33.53% | -6.62% | 0.00 | n/a | prevents broad-slowdown false hard4C |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| C12-R3L65-361610 | 78 | Stage4B-Watch | 91 | Hard4C-Watch | +1.04% | -48.26% | after_profile_aligned |
| C12-R3L65-006400 | 76 | Stage4B-Watch | 86 | Hard4C-Watch | +6.64% | -20.19% | after_profile_aligned |
| C12-R3L65-373220 | 82 | Hard4C-Watch | 72 | Stage2-RiskWatch | +33.53% | -6.47% | after_profile_aligned_by_guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | CELL_SEPARATOR_CUSTOMER_ORDER_CALL_OFF_SLOWDOWN | 2 | 1 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | still needs direct named contract cancellation cases with clean 180D window; 2025-12 cases are narrative-only until forward window exists |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 3
tested_existing_calibrated_axes: [full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, price_only_blowoff_blocks_positive_stage]
residual_error_types_found: [current_profile_too_late, current_profile_false_positive, false_hard4c_from_broad_slowdown]
new_axis_proposed: [c12_customer_order_flow_hard4c_promoter, c12_direct_calloff_vs_broad_slowdown_split]
existing_axis_strengthened: [full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [price_only_blowoff_blocks_positive_stage, stage2_actionable_evidence_bonus]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C12 customer call-off risk lacked visible prior residual rows in accessible search snapshot
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest/schema fields.
- stock profile availability and corporate-action candidate status.
- entry dates and prices from tradable shards.
- MFE/MAE and peak/drawdown using raw, unadjusted, tradable OHLC.
- score-return alignment under shadow-only C12 split.

Not validated:

- no `stock_agent/src/e2r` code inspection.
- no production scorer behavior, only proxy scoring.
- no live watchlist or 2026 candidate scan.
- no raw shard weight calibration.
- no investment recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_customer_order_flow_hard4c_promoter,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"customer shipment/order-flow evidence plus utilization/margin stress had strong downside alignment in 361610 and 006400","reduced missed hard4C risk; SKIET MAE_180D -62.41, SamsungSDI MAE_180D -49.38","C12-R3L65-361610-T1|C12-R3L65-006400-T1",2,2,0,medium-low,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c12_broad_slowdown_hard4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"broad EV slowdown without direct customer call-off produced false hard4C in LGES","prevented false hard4C; LGES MFE_90D +33.53 before later drawdown","C12-R3L65-373220-T1",1,1,1,medium,archetype_shadow_only,"guard broad slowdown; route to Stage2-RiskWatch unless call-off is direct"
```

## 25. Machine-Readable Rows

### 25.1 case rows

```jsonl
{"row_type":"case","case_id":"C12-R3L65-361610","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"65","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CELL_SEPARATOR_CUSTOMER_ORDER_CALL_OFF_SLOWDOWN","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"C12-R3L65-361610-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard4c_watch_aligned_with_large_drawdown","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Customer/order-flow weakness in separator chain; post-trigger path showed little upside and deep downside."}
{"row_type":"case","case_id":"C12-R3L65-006400","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"65","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"EUROPE_CUSTOMER_EXPOSURE_ORDER_SLOWDOWN","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"C12-R3L65-006400-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer_exposure_risk_aligned_with_180D_drawdown","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Europe-heavy customer exposure made broad EV slowdown actionable as customer-order risk."}
{"row_type":"case","case_id":"C12-R3L65-373220","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"65","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BROAD_EV_SLOWDOWN_WITH_POLICY_OFFSET","case_type":"false_break","positive_or_counterexample":"counterexample","best_trigger":"C12-R3L65-373220-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard4c_false_positive_if_no_customer_specific_calloff","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Broad slowdown and expansion adjustment were real, but no direct customer call-off; stock had +33.53% 90D MFE."}
```

### 25.2 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C12-R3L65-361610-T1","case_id":"C12-R3L65-361610","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"65","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CELL_SEPARATOR_CUSTOMER_ORDER_CALL_OFF_SLOWDOWN","sector":"battery_material_separator","primary_archetype":"customer_order_flow_break","loop_objective":"counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage4C-Watch","trigger_date":"2024-05-15","evidence_available_at_that_date":"Reuters reported SK Innovation was considering sale of SKIET amid weak EV demand and SK On shipments falling; report was after Korea close, so next-trading-day entry used.","evidence_source":"Reuters 2024-05-15 https://www.reuters.com/technology/sk-innovation-considering-sale-battery-materials-unit-skiet-paper-reports-2024-05-15/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv","profile_path":"atlas/symbol_profiles/361/361610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":57600,"MFE_30D_pct":1.04,"MFE_90D_pct":1.04,"MFE_180D_pct":1.04,"MFE_1Y_pct":1.04,"MFE_2Y_pct":null,"MAE_30D_pct":-25.87,"MAE_90D_pct":-48.26,"MAE_180D_pct":-62.41,"MAE_1Y_pct":-66.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":58200,"drawdown_after_peak_pct":-66.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_peak_case_hard4c_watch","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12-R3L65-361610-20240516-57600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C12-R3L65-006400-T1","case_id":"C12-R3L65-006400","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"65","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"EUROPE_CUSTOMER_EXPOSURE_ORDER_SLOWDOWN","sector":"battery_cell","primary_archetype":"customer_concentration_order_slowdown","loop_objective":"counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage4C-Watch","trigger_date":"2024-06-25","evidence_available_at_that_date":"MarketWatch/WSJ Market Talk cited Samsung SDI's Europe customer dependence and EV demand slowdown pressure; next-trading-day entry used.","evidence_source":"MarketWatch 2024-06-25 https://www.marketwatch.com/story/samsung-sdi-s-reliance-on-europe-could-weigh-on-2q-earnings-market-talk-a4a685a5","stage2_evidence_fields":["customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-26","entry_price":369000,"MFE_30D_pct":5.69,"MFE_90D_pct":6.64,"MFE_180D_pct":6.64,"MFE_1Y_pct":6.64,"MFE_2Y_pct":null,"MAE_30D_pct":-20.19,"MAE_90D_pct":-20.19,"MAE_180D_pct":-49.38,"MAE_1Y_pct":-57.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":393500,"drawdown_after_peak_pct":-59.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"risk_overlay_near_limited_upside","four_b_evidence_type":["margin_or_backlog_slowdown","revision_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12-R3L65-006400-20240626-369000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C12-R3L65-373220-T1","case_id":"C12-R3L65-373220","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"65","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BROAD_EV_SLOWDOWN_WITH_POLICY_OFFSET","sector":"battery_cell","primary_archetype":"broad_slowdown_without_direct_calloff","loop_objective":"counterexample_mining|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-RiskWatch","trigger_date":"2024-07-25","evidence_available_at_that_date":"Reuters reported LGES cut annual sales target and would ease expansion due to weak EV demand; same report also noted policy/supply-chain offset and stock rebound, so hard4C is guarded.","evidence_source":"Reuters 2024-07-25 https://www.reuters.com/technology/battery-firm-lg-energy-solution-q2-profit-plunges-weak-ev-demand-2024-07-25/","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-25","entry_price":332500,"MFE_30D_pct":25.98,"MFE_90D_pct":33.53,"MFE_180D_pct":33.53,"MFE_1Y_pct":33.53,"MFE_2Y_pct":null,"MAE_30D_pct":-6.47,"MAE_90D_pct":-6.47,"MAE_180D_pct":-6.62,"MAE_1Y_pct":-20.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000,"drawdown_after_peak_pct":-40.09,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"broad_slowdown_false_hard4c_guard_needed","four_b_evidence_type":["price_only"],"four_c_protection_label":"false_break","trigger_outcome_label":"false_hard4c_if_promoted","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12-R3L65-373220-20240725-332500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.3 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12-R3L65-361610","trigger_id":"C12-R3L65-361610-T1","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":1,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":1,"customer_quality_score":10,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":10,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"c12_customer_order_flow_break_score":10},"weighted_score_after":91,"stage_label_after":"Hard4C-Watch","changed_components":["customer_quality_score","execution_risk_score","c12_customer_order_flow_break_score"],"component_delta_explanation":"Customer shipment weakness plus potential asset-sale pressure is stronger than generic sector slowdown.","MFE_90D_pct":1.04,"MAE_90D_pct":-48.26,"score_return_alignment_label":"after_profile_aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12-R3L65-006400","trigger_id":"C12-R3L65-006400-T1","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":2,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":7,"relative_strength_score":2,"customer_quality_score":9,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"c12_customer_concentration_risk_score":9},"weighted_score_after":86,"stage_label_after":"Hard4C-Watch","changed_components":["revision_score","customer_quality_score","c12_customer_concentration_risk_score"],"component_delta_explanation":"Europe customer concentration made demand slowdown a customer-order risk, not just macro noise.","MFE_90D_pct":6.64,"MAE_90D_pct":-20.19,"score_return_alignment_label":"after_profile_aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12-R3L65-373220","trigger_id":"C12-R3L65-373220-T1","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Hard4C-Watch","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":8,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"c12_broad_slowdown_without_calloff_guard":10},"weighted_score_after":72,"stage_label_after":"Stage2-RiskWatch","changed_components":["customer_quality_score","execution_risk_score","c12_broad_slowdown_without_calloff_guard"],"component_delta_explanation":"Broad slowdown and capacity pacing are not enough for hard4C without customer-specific call-off; policy/geography offset was present.","MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"score_return_alignment_label":"after_profile_aligned_by_guard","current_profile_verdict":"current_profile_false_positive"}
```

### 25.4 residual contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"65","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":0,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3,"diversity_score_summary":"avg=30.0; new symbols=3; new trigger families=3; counterexample guard present","tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","false_hard4c_from_broad_slowdown"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C12 customer call-off risk lacked visible prior residual coverage in accessible search snapshot"}
```

### 25.5 narrative-only rows

```jsonl
{"row_type":"narrative_only","case_id":"C12-R3L65-LGES-2025-CONTRACT-CANCEL","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","reason":"2025-12 contract cancellation headlines are directly relevant to C12 but forward 180D window is unavailable under manifest_max_date 2026-02-20","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/&lt;prefix&gt;/&lt;ticker&gt;/&lt;year&gt;.csv.
- Symbol profile pattern: atlas/symbol_profiles/&lt;prefix&gt;/&lt;ticker&gt;.json.

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
next_round = R3_loop_66_C11_BATTERY_ORDERBOOK_RERATING
reason = C12 now has a call-off risk split; adjacent C11 should test the opposite path: when orderbook conversion is real rather than nominal.
```

## 28. Source Notes

Stock-Web inputs used:

- `atlas/manifest.json`: manifest max date, shard roots, raw/unadjusted price status, row counts.
- `atlas/schema.json`: tradable/raw schema and MFE/MAE definitions.
- `atlas/symbol_profiles/373/373220.json`: LG에너지솔루션 clean profile, no corporate-action candidates.
- `atlas/symbol_profiles/361/361610.json`: SK아이이테크놀로지 clean profile, no corporate-action candidates.
- `atlas/symbol_profiles/006/006400.json`: 삼성SDI profile; historical corporate-action candidates exist but none overlap 2024-06-26~D+180.
- `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv` and `2025.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv` and `2025.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv` and `2025.csv`.

External evidence sources used:

- Reuters, 2024-05-15: SK Innovation considering sale of SKIET; weakening EV demand and SK On shipment weakness.
- MarketWatch/WSJ Market Talk, 2024-06-25: Samsung SDI Europe customer exposure and EV demand slowdown risk.
- Reuters, 2024-07-25: LGES cuts annual sales target and eases capacity expansion due to weak EV demand, while policy/supply-chain offset limited immediate downside.

No live recommendation or current candidate discovery is made in this file.
