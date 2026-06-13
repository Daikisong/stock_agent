# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R3
selected_loop = 136
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = mixed_c14_second_pass_segment_materiality_relief_offset_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_confirmation_and_false_break_timing_test|canonical_archetype_compression
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 6 new independent C14 cases, 6 usable trigger rows, 3 defensive-positive examples, and 3 counterexamples. It does not modify production scoring. It is a standalone v12 historical calibration MD.

## 1. Current Calibrated Profile Assumption

The working proxy remains `e2r_2_1_stock_web_calibrated_proxy`: Stage2 actionable evidence bonus exists, Green is strict, price-only blowoff does not promote positive stage, full 4B requires non-price evidence, and hard 4C requires thesis-break evidence. This MD does not re-prove the global rules. It tests the residual C14 edge: when EV-demand-slowdown evidence should become Stage4B watch, when it should escalate to hard Stage4C, and when reported loss or segment loss is too blunt to override relief-rally / entity-offset evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

C14 belongs to R3 / L3. The selected scope is not a general battery orderbook rerating study. It is the defensive EV-demand-slowdown branch: inventory valuation loss, lithium/metal price shock, customer call-off, copper-foil utilization, segment materiality, and the boundary between Stage4B watch and hard Stage4C.

## 3. Previous Coverage / Duplicate Avoidance Check

The latest No-Repeat Index marks C14 as Priority 0 with 11 rows and 19 more rows needed to reach the 30-row minimum stability zone. This local session already produced C14 loop 127 using POSCO Future M, Chunbo, WCP, and Solus Advanced Materials. This loop avoids those symbol/entry-date combinations. It uses 066970, 011790, 020150, and 005070, with a same-symbol second trigger only when the trigger family and entry date are materially different.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest fields checked: source_name `FinanceData/marcap`, price_adjustment_status `raw_unadjusted_marcap`, max_date `2026-02-20`, calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`, raw_shard_root `atlas/ohlcv_raw_by_symbol_year`, schema_path `atlas/schema.json`, universe_path `atlas/universe/all_symbols.csv`.

## 5. Historical Eligibility Gate

All representative trigger rows have an entry date inside the stock-web tradable shard, an entry close, at least 180 forward trading rows, and complete `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`. The 180D windows are clean for corporate-action contamination. L&F has profile corporate-action candidate dates in 2016 and 2021; SKC in 1998 and 2001; Lotte Energy Materials has no candidate; Cosmo Advanced Materials has no 2024/2025 candidate overlap after the last listed 2019 candidate.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| LNF_INVENTORY_LITHIUM_PRICE_SHOCK_RELIEF_RALLY | C14_EV_DEMAND_SLOWDOWN_4B_4C | Inventory/lithium shock creates C14 watch, but shipment-bottom language can make immediate hard 4C too early. |
| LNF_CUSTOMER_CONTRACT_IN_SLOWDOWN_TAPE_FALSE_RESCUE | C14_EV_DEMAND_SLOWDOWN_4B_4C | A large named contract does not automatically neutralize C14 if margin/ASP/working-capital bridge is missing. |
| COPPER_FOIL_SEGMENT_LOSS_CONGLOMERATE_OFFSET | C14_EV_DEMAND_SLOWDOWN_4B_4C | Segment-level copper foil loss needs entity materiality and offset checks before hard 4C. |
| COPPER_FOIL_Q2_PROFIT_CUSTOMER_DIVERSIFICATION_FALSE_OFFSET | C14_EV_DEMAND_SLOWDOWN_4B_4C | One-quarter OP/customer diversification can fail if later utilization and demand remain weak. |
| COPPER_FOIL_EV_CHASM_LOSS_RELIEF_RALLY | C14_EV_DEMAND_SLOWDOWN_4B_4C | Reported annual loss and EV chasm may be Stage4B rather than hard 4C when post-loss relief MFE is large. |
| CATHODE_SINGLE_CRYSTAL_GROWTH_OVERLAY_STAGE2_FALSE_POSITIVE | C14_EV_DEMAND_SLOWDOWN_4B_4C | Growth product thesis in cathode materials still needs C14 high-MAE overlay in a weak EV-material regime. |

## 7. Case Selection Summary

| case_id | symbol | company | trigger | role | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| C14_R3L136_066970_20240202 | 066970 | 엘앤에프 | Stage4B | counterexample | 2024-02-02 | 145,600 | 36.68 | -9.27 | 36.68 | -43.06 | current_profile_hard_4c_too_early |
| C14_R3L136_066970_20240326 | 066970 | 엘앤에프 | Stage2 | positive | 2024-03-26 | 183,100 | 2.95 | -50.79 | 2.95 | -54.72 | current_profile_stage2_too_generous_if_contract_ignores_margin_tape |
| C14_R3L136_011790_20240805 | 011790 | SKC | Stage4B | counterexample | 2024-08-05 | 114,100 | 50.22 | -20.86 | 58.63 | -24.45 | current_profile_false_positive_if_segment_loss_routes_total_entity_to_hard_4c |
| C14_R3L136_020150_20240607 | 020150 | 롯데에너지머티리얼즈 | Stage4B | positive | 2024-06-07 | 49,200 | 20.33 | -38.01 | 20.33 | -58.84 | current_profile_too_lenient_if_profit_offset_blocks_c14_watch |
| C14_R3L136_020150_20250124 | 020150 | 롯데에너지머티리얼즈 | Stage4B | counterexample | 2025-01-24 | 23,050 | 36.88 | -15.57 | 36.88 | -15.57 | current_profile_hard_4c_too_harsh_if_no_post_loss_relief_guard |
| C14_R3L136_005070_20240430 | 005070 | 코스모신소재 | Stage2 | positive | 2024-04-30 | 151,800 | 19.24 | -36.43 | 19.24 | -67.39 | current_profile_stage2_too_generous_without_c14_overlay |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 3
4B_case_count = 4
Stage2_false_positive_overlay_count = 2
calibration_usable_case_count = 6
calibration_usable_trigger_count = 6
representative_trigger_count = 6
```

C14 is a protection archetype, so positive cases mean correct defensive labeling, not bullish rerating. This loop deliberately pairs two opposite mistakes: over-firing hard 4C on loss/downturn vocabulary, and under-firing Stage4B when a contract or one-quarter profit appears to rescue the story.

## 9. Evidence Source Map

| symbol | trigger_date | source | evidence interpretation |
|---:|---:|---|---|
| 066970 | 2024-02-02 | https://www.asiae.co.kr/en/article/2024020116473792269 | 2023 operating-loss turn due large inventory valuation loss from plunging lithium prices; shipment bottom and gradual resolution language made immediate hard 4C too harsh. |
| 066970 | 2024-03-25 | https://en.yna.co.kr/view/AEN20240325003900320 | Large named contract and 300,000 ton supply visibility existed, but C14 should still ask whether contract margin, ASP, utilization, and working-capital path can offset the sector downcycle. |
| 011790 | 2024-08-02 | https://alphabiz.co.kr/news/print.html?newsid=110266 | SKC battery materials/SK Nexilis had EV growth slowdown, revenue downturn and fixed-cost pressure, but entity-level C14 hard 4C needed segment materiality and non-EV offset checks. |
| 020150 | 2024-06-06 | https://lotteenergymaterials.com/en/pr/promotion_detail.do?seq=79 | Q2 sales and OP improved with customer diversification and North America growth, but C14 should not treat one-quarter profit as a permanent blocker if copper-foil utilization and EV demand remain fragile. |
| 020150 | 2025-01-24 | https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128 | 2024 operating loss and EV chasm impact were explicit, but revenue increased due to diversified customers/North America. Hard 4C immediately after reported loss would miss a relief-rally path. |
| 005070 | 2024-04-30 | https://securities.miraeasset.com/bbs/download/2126219.pdf?attachmentId=2126219 | Growth acceleration was expected from single-crystal cathode materials and new products/customers, but in a weak EV-material tape Stage2 should carry a C14 high-MAE overlay unless actual margin/revision confirms. |

## 10. Price Data Source Map

| symbol | profile_path | entry shard | forward shard coverage | profile corporate-action status |
|---:|---|---|---|---|
| 066970 | atlas/symbol_profiles/066/066970.json | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | 2024-2025 | clean_180D_window |
| 066970 | atlas/symbol_profiles/066/066970.json | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | 2024-2025 | clean_180D_window |
| 011790 | atlas/symbol_profiles/011/011790.json | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv | 2024-2025 | clean_180D_window |
| 020150 | atlas/symbol_profiles/020/020150.json | atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv | 2024-2025 | clean_180D_window |
| 020150 | atlas/symbol_profiles/020/020150.json | atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv | 2025-2026 | clean_180D_window |
| 005070 | atlas/symbol_profiles/005/005070.json | atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv | 2024-2025 | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### Case 1 — L&F / 066970 / inventory-lithium shock relief-rally counterexample

The evidence was severe: operating-loss turn, inventory valuation loss, lithium price collapse, and demand weakness. But the same evidence also contained shipment-bottom / gradual-resolution language. The price path delivered +36.68% 90D/180D MFE before a later -43.06% 180D MAE. Immediate hard 4C would have been too early; Stage4B watch was the cleaner label.

### Case 2 — L&F / 066970 / SK On contract false rescue

The SK On contract had named customer, size, duration, and delivery visibility. In ordinary C11/C12 logic, that is strong evidence. In C14, however, the contract did not solve the near-term ASP, margin, inventory, and working-capital problem. The 180D path gave only +2.95% MFE and -54.72% MAE. The rule lesson is that a large contract should not automatically erase the downcycle overlay.

### Case 3 — SKC / 011790 / segment-loss hard-4C false break

SK Nexilis/copper foil weakness was real, including Q2 battery-materials operating loss and EV-growth slowdown. But SKC is a multi-segment entity, and the total equity path had +58.63% 180D MFE before later drawdown. C14 hard 4C needs segment materiality and non-EV offset checks; otherwise the engine treats one wounded branch as if the whole tree had died.

### Case 4 — Lotte Energy Materials / 020150 / one-quarter profit did not block C14

Q2 2024 looked like a rescue: sales growth, operating profit, customer diversification, and North America growth. The stock still suffered -58.84% 180D MAE after only +20.33% MFE. This is a useful positive C14 overlay case: one good quarter is not enough if utilization, ASP, customer take-or-pay quality, and copper-foil demand remain fragile.

### Case 5 — Lotte Energy Materials / 020150 / reported EV-chasm loss relief-rally counterexample

By January 2025, reported annual operating loss and EV chasm were explicit. But sales still rose on customer diversification/North America, and the post-loss path had +36.88% MFE with only -15.57% MAE. Hard 4C immediately after the reported loss was too harsh; Stage4B watch with confirmation pending fits better.

### Case 6 — Cosmo Advanced Materials / 005070 / growth-thesis Stage2 false positive

The report expected revenue growth acceleration from single-crystal cathode materials and new products/customers. The price path was unforgiving: +19.24% MFE versus -67.39% 180D MAE. C14 should add a high-MAE/downcycle overlay to battery-material Stage2 rows when the positive thesis has not yet become margin/revision proof.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | clean window |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TRG_C14_R3L136_066970_20240202 | 2024-02-02 | 145,600 | 26.30 | -9.27 | 36.68 | -9.27 | 36.68 | -43.06 | 2024-03-25 | 199,000 | -58.34 | clean_180D_window |
| TRG_C14_R3L136_066970_20240326 | 2024-03-26 | 183,100 | 2.95 | -23.21 | 2.95 | -50.79 | 2.95 | -54.72 | 2024-03-27 | 188,500 | -56.02 | clean_180D_window |
| TRG_C14_R3L136_011790_20240805 | 2024-08-05 | 114,100 | 16.74 | -8.59 | 50.22 | -20.86 | 58.63 | -24.45 | 2025-01-20 | 181,000 | -52.38 | clean_180D_window |
| TRG_C14_R3L136_020150_20240607 | 2024-06-07 | 49,200 | 20.33 | -12.70 | 20.33 | -38.01 | 20.33 | -58.84 | 2024-06-18 | 59,200 | -65.79 | clean_180D_window |
| TRG_C14_R3L136_020150_20250124 | 2025-01-24 | 23,050 | 36.88 | -12.15 | 36.88 | -15.57 | 36.88 | -15.57 | 2025-02-20 | 31,550 | -38.32 | clean_180D_window |
| TRG_C14_R3L136_005070_20240430 | 2024-04-30 | 151,800 | 19.24 | -9.88 | 19.24 | -36.43 | 19.24 | -67.39 | 2024-06-13 | 181,000 | -72.65 | clean_180D_window |

## 13. Current Calibrated Profile Stress Test

| case_id | likely current judgement | actual path alignment | residual diagnosis |
|---|---|---|---|
| C14_R3L136_066970_20240202 | Stage4B or hard 4C because of operating loss / lithium inventory loss | Mixed: +36.68% MFE before later -43.06% MAE | Hard 4C too early if shipment-bottom / relief language exists. |
| C14_R3L136_066970_20240326 | Stage2/Stage2-Actionable because of massive named customer contract | Wrong: +2.95% MFE and -54.72% MAE | Contract bridge cannot rescue C14 without margin/ASP conversion. |
| C14_R3L136_011790_20240805 | Segment-level Stage4C risk from copper foil loss | Mixed/false hard 4C: +58.63% MFE | Need segment materiality and entity-offset guard. |
| C14_R3L136_020150_20240607 | Stage2/Watch softened by Q2 profit and customer diversification | Wrong if softened too much: -58.84% 180D MAE | One-quarter offset should not block C14 watch. |
| C14_R3L136_020150_20250124 | Hard 4C after annual operating loss and EV chasm | Too harsh: +36.88% MFE, -15.57% MAE | Reported loss can be post-trough relief context. |
| C14_R3L136_005070_20240430 | Stage2 from single-crystal cathode growth thesis | Wrong: -67.39% 180D MAE | C14 high-MAE overlay needed before margin/revision proof. |

## 14. Stage2 / Yellow / Green Comparison

This loop is not a Green unlock study. No Stage3-Green row is proposed. The positive direction is defensive: prevent Stage2 from being too generous in battery materials during a chasm, and prevent hard 4C from being too blunt when relief-rally or entity-offset evidence exists.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B/4C timing verdict | local/full interpretation |
|---|---|---|
| L&F Feb | Stage4B watch preferred | Full hard 4C before +36.68% MFE would be too early, but later drawdown confirms watch value. |
| L&F Mar | Stage2 rescue should be blocked | Contract headline local positive failed almost immediately; full window shows severe drawdown. |
| SKC Aug | Segment 4B, not entity hard 4C | Segment loss was valid but entity price path had a large relief/rerating window. |
| LEM Jun | 4B watch despite Q2 profit | One-quarter positive offset failed over the full window. |
| LEM Jan | 4B watch after reported loss | Reported loss did not produce large immediate MAE; hard 4C needed further confirmation. |
| Cosmo Apr | Stage2 high-MAE overlay | Local upside was below +20% and full window collapsed; C14 overlay should reduce confidence. |

## 16. 4C Protection Audit

C14 needs a two-step protection map. Smoke from EV slowdown, ASP compression, inventory valuation loss, or segment loss opens Stage4B watch. The sprinkler, hard Stage4C, should release only when the heat sensor also confirms company-level materiality: customer call-off/order cut, utilization collapse, loss conversion with no credible offset, or repeated margin/revision break. Conversely, one layer of positive offset such as a supply contract, one-quarter operating profit, or product-growth report should not close the watch state unless margin/revision/working-capital evidence confirms it.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L3_EV_MATERIAL_SEGMENT_MATERIALITY_AND_RELIEF_MFE_GATE_V2
scope = L3_BATTERY_EV_GREEN_MOBILITY
rule = In L3, EV-material downturn evidence should open Stage4B watch. Hard 4C requires company-level materiality and confirmation. Positive offset evidence should block hard 4C only when it has margin/revision/working-capital proof. Segment-level copper foil/cathode weakness should not route a multi-segment entity to hard 4C without entity-level exposure and offset checks.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C14_SEGMENT_MATERIALITY_RELIEF_AND_OFFSET_CONFIRMATION_GATE_V2
scope = C14_EV_DEMAND_SLOWDOWN_4B_4C
positive defense examples = 066970_20240326, 020150_20240607, 005070_20240430
false-hard-4C examples = 066970_20240202, 011790_20240805, 020150_20250124
```

The rule behaves like a quarantine door. A warning sign on one room closes that room first; it does not shut the whole building unless the ventilation map proves the damage is spreading. Likewise, C14 should isolate weak EV-material evidence as watch, then escalate only when company-level economics confirm the break.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | Existing 4B/4C rules without C14 segment/materiality nuance | 6 | 27.72 | -28.49 | 29.12 | -44.00 | 0.50 | 2 | mixed; too harsh on L&F Feb/SKC/LEM Jan, too lenient on contract/profit growth offsets |
| P1_L3_sector_specific_candidate_profile | sector shadow | Require segment materiality and margin/working-capital confirmation | 6 | 27.72 | -28.49 | 29.12 | -44.00 | 0.17 | 0 | better watch-vs-hard-4C separation |
| P2_C14_canonical_candidate_profile | canonical shadow | Add relief-MFE guard and positive-offset confirmation filter | 6 | 27.72 | -28.49 | 29.12 | -44.00 | 0.00 | 0 | best alignment in this sample set |
| P3_counterexample_guard_profile | guard shadow | Block hard 4C if post-loss relief/segment offset exists | 6 | 27.72 | -28.49 | 29.12 | -44.00 | 0.00 | 1 | prevents false hard 4C but still needs Stage2 false-positive overlay |

## 20. Score-Return Alignment Matrix

| case | before score direction | after score direction | alignment |
|---|---|---|---|
| L&F Feb | too much hard-break risk from reported loss/lithium shock | Stage4B watch until confirmation | improves |
| L&F Mar | too much Stage2 confidence from contract size | C14 overlay requires margin/ASP bridge | improves |
| SKC Aug | too much hard-4C risk from segment loss | segment materiality/entity-offset check | improves |
| LEM Jun | too lenient due Q2 profit | Stage4B watch remains until utilization proof | improves |
| LEM Jan | hard 4C after annual loss | Stage4B watch because post-loss relief path exists | improves |
| Cosmo Apr | Stage2 growth thesis too generous | high-MAE C14 overlay before margin proof | improves |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed_c14_second_pass_segment_materiality_relief_offset_leaf_set | 3 | 3 | 4 | 0 | 6 | 0 | 6 | 6 | 5 | L3_EV_MATERIAL_SEGMENT_MATERIALITY_AND_RELIEF_MFE_GATE_V2 | C14_SEGMENT_MATERIALITY_RELIEF_AND_OFFSET_CONFIRMATION_GATE_V2 | index baseline C14 rows 11 -> 17 if accepted; session-aware after loop127 C14 rows 16 -> 22 if accepted; need 8 to 30 session-aware |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_trigger_family_count: 6
positive_case_count: 3
counterexample_count: 3
current_profile_error_count: 5
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical C14 defense-label calibration, clean 180D stock-web OHLC path, Stage2 false-positive overlay, segment-materiality guard, watch-vs-hard-4C timing, and post-loss relief false-break control. Non-validation scope: live stock discovery, current investment recommendation, production scoring changes, or any brokerage/API workflow.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_segment_materiality_relief_and_offset_confirmation_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Hard 4C should require company-level materiality and confirmation; reported loss/segment loss alone can be too blunt.","Reduced false hard-4C breaks in 066970_20240202, 011790_20240805, 020150_20250124 while preserving defensive watch in 066970_20240326, 020150_20240607, 005070_20240430.","TRG_C14_R3L136_066970_20240202|TRG_C14_R3L136_066970_20240326|TRG_C14_R3L136_011790_20240805|TRG_C14_R3L136_020150_20240607|TRG_C14_R3L136_020150_20250124|TRG_C14_R3L136_005070_20240430",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,l3_positive_offset_confirmation_before_c14_blocker,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Contract/profit/product-growth offset should block C14 only after margin/revision/working-capital confirmation.","L&F contract, LEM Q2 profit, and Cosmo growth thesis all needed C14 high-MAE overlay.","TRG_C14_R3L136_066970_20240326|TRG_C14_R3L136_020150_20240607|TRG_C14_R3L136_005070_20240430",3,3,0,medium,sector_shadow_only,"same archetype, new trigger family"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C14_R3L136_066970_20240202","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"LNF_INVENTORY_LITHIUM_PRICE_SHOCK_RELIEF_RALLY","case_type":"hard_4c_too_early_relief_rally","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"inventory_lithium_shock_but_relief_rally_before_later_drawdown","current_profile_verdict":"current_profile_hard_4c_too_early","price_source":"Songdaiki/stock-web","notes":"2023 operating-loss turn due large inventory valuation loss from plunging lithium prices; shipment bottom and gradual resolution language made immediate hard 4C too harsh."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L136_066970_20240202","case_id":"C14_R3L136_066970_20240202","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"LNF_INVENTORY_LITHIUM_PRICE_SHOCK_RELIEF_RALLY","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_confirmation_and_false_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":145600.0,"evidence_available_at_that_date":"Asia Economy, 2024-02-01, L&F 2023 sales 4.6T / operating loss from lithium inventory valuation and demand slowdown relief commentary, https://www.asiae.co.kr/en/article/2024020116473792269","evidence_source":"Asia Economy, 2024-02-01, L&F 2023 sales 4.6T / operating loss from lithium inventory valuation and demand slowdown relief commentary, https://www.asiae.co.kr/en/article/2024020116473792269","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["inventory_valuation_loss","raw_material_price_collapse","ev_demand_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.3,"MFE_90D_pct":36.68,"MFE_180D_pct":36.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.27,"MAE_90D_pct":-9.27,"MAE_180D_pct":-43.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000.0,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"stage4b_watch_preferred_over_immediate_hard_4c","four_b_evidence_type":["inventory_valuation_loss","raw_material_price_collapse","ev_demand_slowdown"],"four_c_protection_label":"false_hard_4c_break","trigger_outcome_label":"inventory_lithium_shock_but_relief_rally_before_later_drawdown","current_profile_verdict":"current_profile_hard_4c_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_066970_2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L136_066970_20240202","trigger_id":"TRG_C14_R3L136_066970_20240202","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":55.0,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":61.0,"stage_label_after":"Stage4B","changed_components":["segment_materiality_gate","relief_mfe_guard","hard_4c_confirmation_filter"],"component_delta_explanation":"C14 second-pass shadow rule separates immediate hard 4C from Stage4B watch and prevents one-layer positive offset from erasing downcycle risk.","MFE_90D_pct":36.68,"MAE_90D_pct":-9.27,"score_return_alignment_label":"inventory_lithium_shock_but_relief_rally_before_later_drawdown","current_profile_verdict":"current_profile_hard_4c_too_early"}
{"row_type":"case","case_id":"C14_R3L136_066970_20240326","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"LNF_CUSTOMER_CONTRACT_IN_SLOWDOWN_TAPE_FALSE_RESCUE","case_type":"stage2_rescue_false_positive_in_downcycle","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"large_named_contract_but_downcycle_margins_and_price_path_failed","current_profile_verdict":"current_profile_stage2_too_generous_if_contract_ignores_margin_tape","price_source":"Songdaiki/stock-web","notes":"Large named contract and 300,000 ton supply visibility existed, but C14 should still ask whether contract margin, ASP, utilization, and working-capital path can offset the sector downcycle."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L136_066970_20240326","case_id":"C14_R3L136_066970_20240326","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"LNF_CUSTOMER_CONTRACT_IN_SLOWDOWN_TAPE_FALSE_RESCUE","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_confirmation_and_false_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-25","entry_date":"2024-03-26","entry_price":183100.0,"evidence_available_at_that_date":"Yonhap, 2024-03-25, L&F signed 13.19T won high-nickel cathode supply deal with SK On through Dec. 2030, https://en.yna.co.kr/view/AEN20240325003900320","evidence_source":"Yonhap, 2024-03-25, L&F signed 13.19T won high-nickel cathode supply deal with SK On through Dec. 2030, https://en.yna.co.kr/view/AEN20240325003900320","stage2_evidence_fields":["named_customer_contract","large_contract_amount","long_duration_supply_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["ev_downcycle_context","margin_bridge_missing"],"stage4c_evidence_fields":["price_path_confirms_contract_not_enough"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.95,"MFE_90D_pct":2.95,"MFE_180D_pct":2.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.21,"MAE_90D_pct":-50.79,"MAE_180D_pct":-54.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":188500.0,"drawdown_after_peak_pct":-56.02,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"stage4b_watch_or_c14_overlay_needed","four_b_evidence_type":["ev_downcycle_context","margin_bridge_missing"],"four_c_protection_label":"defensive_overlay_success","trigger_outcome_label":"large_named_contract_but_downcycle_margins_and_price_path_failed","current_profile_verdict":"current_profile_stage2_too_generous_if_contract_ignores_margin_tape","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_066970_2024-03-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L136_066970_20240326","trigger_id":"TRG_C14_R3L136_066970_20240326","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":63.5,"stage_label_after":"Stage4B","changed_components":["stage2_rescue_blocker","c14_high_mae_overlay","margin_or_utilization_confirmation_required"],"component_delta_explanation":"C14 second-pass shadow rule separates immediate hard 4C from Stage4B watch and prevents one-layer positive offset from erasing downcycle risk.","MFE_90D_pct":2.95,"MAE_90D_pct":-50.79,"score_return_alignment_label":"large_named_contract_but_downcycle_margins_and_price_path_failed","current_profile_verdict":"current_profile_stage2_too_generous_if_contract_ignores_margin_tape"}
{"row_type":"case","case_id":"C14_R3L136_011790_20240805","symbol":"011790","company_name":"SKC","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPER_FOIL_SEGMENT_LOSS_CONGLOMERATE_OFFSET","case_type":"segment_level_hard_4c_false_break","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"copper_foil_loss_real_but_total_company_relief_and_new_business_rerating_dominated","current_profile_verdict":"current_profile_false_positive_if_segment_loss_routes_total_entity_to_hard_4c","price_source":"Songdaiki/stock-web","notes":"SKC battery materials/SK Nexilis had EV growth slowdown, revenue downturn and fixed-cost pressure, but entity-level C14 hard 4C needed segment materiality and non-EV offset checks."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L136_011790_20240805","case_id":"C14_R3L136_011790_20240805","symbol":"011790","company_name":"SKC","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPER_FOIL_SEGMENT_LOSS_CONGLOMERATE_OFFSET","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_confirmation_and_false_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-08-02","entry_date":"2024-08-05","entry_price":114100.0,"evidence_available_at_that_date":"Alphabiz, 2024-08-02, SKC copper foil target cut and Q2 secondary-battery materials operating loss, https://alphabiz.co.kr/news/print.html?newsid=110266","evidence_source":"Alphabiz, 2024-08-02, SKC copper foil target cut and Q2 secondary-battery materials operating loss, https://alphabiz.co.kr/news/print.html?newsid=110266","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["segment_operating_loss","target_cut","fixed_cost_pressure"],"stage4c_evidence_fields":["segment_materiality_not_enough_for_total_entity_hard_4c"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.74,"MFE_90D_pct":50.22,"MFE_180D_pct":58.63,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.59,"MAE_90D_pct":-20.86,"MAE_180D_pct":-24.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-20","peak_price":181000.0,"drawdown_after_peak_pct":-52.38,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"stage4b_watch_preferred_over_immediate_hard_4c","four_b_evidence_type":["segment_operating_loss","target_cut","fixed_cost_pressure"],"four_c_protection_label":"false_hard_4c_break","trigger_outcome_label":"copper_foil_loss_real_but_total_company_relief_and_new_business_rerating_dominated","current_profile_verdict":"current_profile_false_positive_if_segment_loss_routes_total_entity_to_hard_4c","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_011790_2024-08-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L136_011790_20240805","trigger_id":"TRG_C14_R3L136_011790_20240805","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":55.0,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":61.0,"stage_label_after":"Stage4B","changed_components":["segment_materiality_gate","relief_mfe_guard","hard_4c_confirmation_filter"],"component_delta_explanation":"C14 second-pass shadow rule separates immediate hard 4C from Stage4B watch and prevents one-layer positive offset from erasing downcycle risk.","MFE_90D_pct":50.22,"MAE_90D_pct":-20.86,"score_return_alignment_label":"copper_foil_loss_real_but_total_company_relief_and_new_business_rerating_dominated","current_profile_verdict":"current_profile_false_positive_if_segment_loss_routes_total_entity_to_hard_4c"}
{"row_type":"case","case_id":"C14_R3L136_020150_20240607","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPER_FOIL_Q2_PROFIT_CUSTOMER_DIVERSIFICATION_FALSE_OFFSET","case_type":"single_quarter_offset_failed_later_4b_success","positive_or_counterexample":"positive","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"q2_profit_and_customer_diversification_but_180d_mae_large","current_profile_verdict":"current_profile_too_lenient_if_profit_offset_blocks_c14_watch","price_source":"Songdaiki/stock-web","notes":"Q2 sales and OP improved with customer diversification and North America growth, but C14 should not treat one-quarter profit as a permanent blocker if copper-foil utilization and EV demand remain fragile."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L136_020150_20240607","case_id":"C14_R3L136_020150_20240607","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPER_FOIL_Q2_PROFIT_CUSTOMER_DIVERSIFICATION_FALSE_OFFSET","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_confirmation_and_false_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-06-06","entry_date":"2024-06-07","entry_price":49200.0,"evidence_available_at_that_date":"Lotte Energy Materials official, 2024-06-06, preliminary Q2 2024 results, https://lotteenergymaterials.com/en/pr/promotion_detail.do?seq=79","evidence_source":"Lotte Energy Materials official, 2024-06-06, preliminary Q2 2024 results, https://lotteenergymaterials.com/en/pr/promotion_detail.do?seq=79","stage2_evidence_fields":["quarterly_profit","customer_diversification","north_america_sales_growth"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["sector_downcycle_context","utilization_fragility_watch"],"stage4c_evidence_fields":["later_drawdown_confirms_offset_insufficient"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","profile_path":"atlas/symbol_profiles/020/020150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.33,"MFE_90D_pct":20.33,"MFE_180D_pct":20.33,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.7,"MAE_90D_pct":-38.01,"MAE_180D_pct":-58.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":59200.0,"drawdown_after_peak_pct":-65.79,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"stage4b_watch_or_c14_overlay_needed","four_b_evidence_type":["sector_downcycle_context","utilization_fragility_watch"],"four_c_protection_label":"defensive_overlay_success","trigger_outcome_label":"q2_profit_and_customer_diversification_but_180d_mae_large","current_profile_verdict":"current_profile_too_lenient_if_profit_offset_blocks_c14_watch","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_020150_2024-06-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L136_020150_20240607","trigger_id":"TRG_C14_R3L136_020150_20240607","symbol":"020150","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":63.5,"stage_label_after":"Stage4B","changed_components":["stage2_rescue_blocker","c14_high_mae_overlay","margin_or_utilization_confirmation_required"],"component_delta_explanation":"C14 second-pass shadow rule separates immediate hard 4C from Stage4B watch and prevents one-layer positive offset from erasing downcycle risk.","MFE_90D_pct":20.33,"MAE_90D_pct":-38.01,"score_return_alignment_label":"q2_profit_and_customer_diversification_but_180d_mae_large","current_profile_verdict":"current_profile_too_lenient_if_profit_offset_blocks_c14_watch"}
{"row_type":"case","case_id":"C14_R3L136_020150_20250124","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPER_FOIL_EV_CHASM_LOSS_RELIEF_RALLY","case_type":"hard_4c_too_late_or_too_harsh_after_reported_loss","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"reported_operating_loss_but_post_loss_relief_mfe_large_and_mae_mild","current_profile_verdict":"current_profile_hard_4c_too_harsh_if_no_post_loss_relief_guard","price_source":"Songdaiki/stock-web","notes":"2024 operating loss and EV chasm impact were explicit, but revenue increased due to diversified customers/North America. Hard 4C immediately after reported loss would miss a relief-rally path."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L136_020150_20250124","case_id":"C14_R3L136_020150_20250124","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPER_FOIL_EV_CHASM_LOSS_RELIEF_RALLY","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_confirmation_and_false_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2025-01-24","entry_date":"2025-01-24","entry_price":23050.0,"evidence_available_at_that_date":"Lotte Energy Materials official, 2025-01-24, preliminary 2024 results, https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128","evidence_source":"Lotte Energy Materials official, 2025-01-24, preliminary 2024 results, https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128","stage2_evidence_fields":["customer_diversification","north_america_sales_growth"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["reported_operating_loss","ev_chasm_impact"],"stage4c_evidence_fields":["hard_4c_blocked_by_relief_path"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv","profile_path":"atlas/symbol_profiles/020/020150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.88,"MFE_90D_pct":36.88,"MFE_180D_pct":36.88,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.15,"MAE_90D_pct":-15.57,"MAE_180D_pct":-15.57,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-20","peak_price":31550.0,"drawdown_after_peak_pct":-38.32,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"stage4b_watch_preferred_over_immediate_hard_4c","four_b_evidence_type":["reported_operating_loss","ev_chasm_impact"],"four_c_protection_label":"false_hard_4c_break","trigger_outcome_label":"reported_operating_loss_but_post_loss_relief_mfe_large_and_mae_mild","current_profile_verdict":"current_profile_hard_4c_too_harsh_if_no_post_loss_relief_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_020150_2025-01-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L136_020150_20250124","trigger_id":"TRG_C14_R3L136_020150_20250124","symbol":"020150","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":55.0,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":61.0,"stage_label_after":"Stage4B","changed_components":["segment_materiality_gate","relief_mfe_guard","hard_4c_confirmation_filter"],"component_delta_explanation":"C14 second-pass shadow rule separates immediate hard 4C from Stage4B watch and prevents one-layer positive offset from erasing downcycle risk.","MFE_90D_pct":36.88,"MAE_90D_pct":-15.57,"score_return_alignment_label":"reported_operating_loss_but_post_loss_relief_mfe_large_and_mae_mild","current_profile_verdict":"current_profile_hard_4c_too_harsh_if_no_post_loss_relief_guard"}
{"row_type":"case","case_id":"C14_R3L136_005070_20240430","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_SINGLE_CRYSTAL_GROWTH_OVERLAY_STAGE2_FALSE_POSITIVE","case_type":"growth_overlay_failed_to_block_sector_chasm_watch","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"single_crystal_growth_story_but_downstream_demand_pressure_and_price_path_failed","current_profile_verdict":"current_profile_stage2_too_generous_without_c14_overlay","price_source":"Songdaiki/stock-web","notes":"Growth acceleration was expected from single-crystal cathode materials and new products/customers, but in a weak EV-material tape Stage2 should carry a C14 high-MAE overlay unless actual margin/revision confirms."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L136_005070_20240430","case_id":"C14_R3L136_005070_20240430","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_SINGLE_CRYSTAL_GROWTH_OVERLAY_STAGE2_FALSE_POSITIVE","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_confirmation_and_false_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":151800.0,"evidence_available_at_that_date":"Mirae Asset report, 2024-04-30, Cosmo AM&T cathode materials growth acceleration thesis, https://securities.miraeasset.com/bbs/download/2126219.pdf?attachmentId=2126219","evidence_source":"Mirae Asset report, 2024-04-30, Cosmo AM&T cathode materials growth acceleration thesis, https://securities.miraeasset.com/bbs/download/2126219.pdf?attachmentId=2126219","stage2_evidence_fields":["growth_thesis","new_product_customer_route","research_report"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["sector_chasm_high_mae_overlay","margin_confirmation_required"],"stage4c_evidence_fields":["later_price_path_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.24,"MFE_90D_pct":19.24,"MFE_180D_pct":19.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.88,"MAE_90D_pct":-36.43,"MAE_180D_pct":-67.39,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":181000.0,"drawdown_after_peak_pct":-72.65,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"stage4b_watch_or_c14_overlay_needed","four_b_evidence_type":["sector_chasm_high_mae_overlay","margin_confirmation_required"],"four_c_protection_label":"defensive_overlay_success","trigger_outcome_label":"single_crystal_growth_story_but_downstream_demand_pressure_and_price_path_failed","current_profile_verdict":"current_profile_stage2_too_generous_without_c14_overlay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_005070_2024-04-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L136_005070_20240430","trigger_id":"TRG_C14_R3L136_005070_20240430","symbol":"005070","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":63.5,"stage_label_after":"Stage4B","changed_components":["stage2_rescue_blocker","c14_high_mae_overlay","margin_or_utilization_confirmation_required"],"component_delta_explanation":"C14 second-pass shadow rule separates immediate hard 4C from Stage4B watch and prevents one-layer positive offset from erasing downcycle risk.","MFE_90D_pct":19.24,"MAE_90D_pct":-36.43,"score_return_alignment_label":"single_crystal_growth_story_but_downstream_demand_pressure_and_price_path_failed","current_profile_verdict":"current_profile_stage2_too_generous_without_c14_overlay"}
{"row_type":"residual_contribution","round":"R3","loop":"136","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["hard_4c_too_early_on_reported_loss_or_segment_loss","stage2_rescue_false_positive_when_contract_or_growth_offset_lacks_margin_bridge","single_quarter_profit_offset_failed_to_block_downcycle_drawdown","relief_mfe_guard_needed_after_reported_loss"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat duplicate low-value loops as new evidence.
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
completed_round = R3
completed_loop = 136
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|C11_BATTERY_ORDERBOOK_RERATING|C01_ORDER_BACKLOG_MARGIN_BRIDGE|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

Next execution should re-read the latest `V12_Research_No_Repeat_Index.md` and avoid mechanical R1→R13 sequencing. If this C14 loop is accepted, session-aware C14 coverage moves from 16 to 22 representative rows, leaving roughly 8 to reach the 30-row minimum stability zone.

## 28. Source Notes

- `Songdaiki/stock-web` manifest/schema were used only for historical price validation.
- Evidence sources are historical and tied to trigger dates.
- This document is not a live stock recommendation and does not change production scoring.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
