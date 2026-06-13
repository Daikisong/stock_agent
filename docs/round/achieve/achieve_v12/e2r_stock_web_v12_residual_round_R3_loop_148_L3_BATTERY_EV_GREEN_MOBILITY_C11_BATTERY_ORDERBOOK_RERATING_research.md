# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
filename = e2r_stock_web_v12_residual_round_R3_loop_148_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round = R3
selected_loop = 148
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = mixed_c11_equipment_orderbook_quality_revenue_timing_exit_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 7 new independent cases, 4 counterexamples, and 5 residual errors for `L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING`.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are treated as active: Stage2 actionable evidence bonus, Yellow/Green strictness, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing. This MD does not patch production scoring; it proposes a C11-specific shadow gate.

## 2. Round / Large Sector / Canonical Archetype Scope

C11 belongs to R3/L3. The selected scope is battery orderbook rerating, especially whether signed contracts, backlog, or equipment demand actually convert into revenue, margin, and FCF rather than becoming 2024 EV-downcycle false positives.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index lists C11 as Priority 0 with 18 representative rows, 18 symbols, and need-to-30 = 12. This session already added C11 loop 131 and loop 141, so this loop avoids those symbol clusters: 코윈테크, 윤성에프앤씨, 원익피앤이, 하나기술, 티에스아이, 포스코퓨처엠, 에코프로비엠, 피엔티, 씨아이에스, 필에너지, 엠플러스. New set: 나인테크, 탑머티리얼, 브이원텍, 엔시스, 에이프로, 원준.

```text
hard_duplicate_check = pass
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = none
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

- primary_price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- stock_web_manifest_max_date: `2026-02-20`
- entry_price basis: entry date close (`c` column), per v12 prompt.

## 5. Historical Eligibility Gate

All trigger rows below have entry date in tradable shard, high/low/close/volume present, forward 180 trading rows available by stock-web max date, and no corporate-action candidate inside entry~D+180.

## 6. Canonical Archetype Compression Map

```text
BATTERY_SYSTEM_ENGINEERING_US_PROJECT_ORDERBOOK_RERATING -> C11_BATTERY_ORDERBOOK_RERATING
BATTERY_FORMATION_EQUIPMENT_CUSTOMER_CAPEX_ORDER_CYCLE -> C11_BATTERY_ORDERBOOK_RERATING
BATTERY_INSPECTION_PRIOR_ORDER_TO_MARGIN_CONVERSION -> C11_BATTERY_ORDERBOOK_RERATING
BATTERY_INSPECTION_ORDER_WITH_WEAK_SECTOR_TAPE -> C11_BATTERY_ORDERBOOK_RERATING
BATTERY_ORDERBOOK_FORECAST_WITHOUT_NEW_SIGNED_ORDER_IN_WEAK_TAPE -> C11_BATTERY_ORDERBOOK_RERATING
BATTERY_HEAT_TREATMENT_TECHNOLOGY_EXPECTATION_WITH_ORDER_GAP_RISK -> C11_BATTERY_ORDERBOOK_RERATING
```

## 7. Case Selection Summary

| case | symbol | trigger | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 나인테크 | 267320 | Stage2 | 2023-04-03 | 3820 | 6.94 | -18.85 | 8.64 | -18.85 | 63.61 | -18.98 | current_profile_too_early |
| 탑머티리얼 | 360070 | Stage2-Actionable | 2023-03-08 | 53000 | 75.28 | -10.57 | 75.28 | -10.57 | 80.38 | -11.32 | current_profile_correct |
| 브이원텍 | 251630 | Stage2-Actionable | 2024-01-18 | 12200 | 3.28 | -30.33 | 3.28 | -33.77 | 3.28 | -63.73 | current_profile_false_positive |
| 엔시스 | 333620 | Stage2-Actionable | 2024-08-13 | 8950 | 46.15 | -2.23 | 46.15 | -22.91 | 46.15 | -29.5 | current_profile_4B_too_late |
| 탑머티리얼 | 360070 | Stage2 | 2024-05-13 | 52900 | 11.34 | -7.28 | 11.34 | -36.2 | 11.34 | -56.52 | current_profile_false_positive |
| 에이프로 | 262260 | Stage2-Actionable | 2023-05-11 | 16390 | 13.54 | -2.81 | 37.28 | -7.87 | 37.28 | -29.77 | current_profile_4B_too_late |
| 원준 | 382840 | Stage2 | 2024-04-22 | 15580 | 4.56 | -8.22 | 4.56 | -44.8 | 11.68 | -44.8 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 4
4B_watch_or_overlay_count = 5
4C_or_thesis_break_watch_count = 3
current_profile_error_count = 5
```

The clean positives are 탑머티리얼 2023, 엔시스 2024 Q2, and 에이프로 2023. The failures are 브이원텍, 탑머티리얼 2024, 원준, and the early-entry part of 나인테크. The important nuance is that C11 can be both right and dangerous: even correct orderbook theses often need local 4B/exit overlays once early MFE arrives.

## 9. Evidence Source Map

- 나인테크 2023-04-03: https://www.theguru.co.kr/news/article.html?no=51903 — LG전자 207억원 2차전지 제조장비 공급계약, 최근 매출액 대비 32.81%, 계약기간 2024-12-30까지
- 탑머티리얼 2023-03-08: https://www.industrynews.co.kr/news/articleView.html?idxno=49090 — 미국 프로젝트 중심 이차전지 시스템엔지니어링 누적/신규 수주 693억원 규모 보도
- 브이원텍 2024-01-18: https://securities.miraeasset.com/bbs/download/2128023.pdf?attachmentId=2128023 — LG전자 90.369억원 규모 2차전지 검사시스템 공급계약, 2022년 연결 매출액의 15.12%, 계약기간 2025-12-30
- 엔시스 2024-08-12: https://n-sys.co.kr/kr/sub/pr/news_view.asp?idx=131 — 2024년 2분기 매출 310.45억원, 영업이익 68.26억원, 전년 대비 영업이익 292.5% 증가; 지난해 수주 실적 반영과 원가절감 설명
- 탑머티리얼 2024-05-13: https://www.dailyinvest.kr/news/articleView.html?idxno=58609 — 유럽·미국 신규 업체 공장 증설 지속, 올해 신규 수주 대폭 증가와 실적 성장 전망
- 에이프로 2023-05-11: https://ssl.pstatic.net/imgstock/upload/research/company/1683763323752.pdf — LG에너지솔루션을 핵심 고객으로 둔 활성화 장비 업체, 북미 합작법인 증설과 장비 발주 cycle 전망
- 원준 2024-04-22: https://m.thebell.co.kr/m/newsview.asp?newskey=202404220935151840108929&svccode= — 이차전지 양극재/음극재 열처리 기술 중요성과 EPC 사업 다각화 기대

## 10. Price Data Source Map

- 267320 나인테크: `atlas/ohlcv_tradable_by_symbol_year/267/267320/2023.csv` / `atlas/symbol_profiles/267/267320.json` / entry `2023-04-03` close `3820`
- 360070 탑머티리얼: `atlas/ohlcv_tradable_by_symbol_year/360/360070/2023.csv` / `atlas/symbol_profiles/360/360070.json` / entry `2023-03-08` close `53000`
- 251630 브이원텍: `atlas/ohlcv_tradable_by_symbol_year/251/251630/2024.csv` / `atlas/symbol_profiles/251/251630.json` / entry `2024-01-18` close `12200`
- 333620 엔시스: `atlas/ohlcv_tradable_by_symbol_year/333/333620/2024.csv` / `atlas/symbol_profiles/333/333620.json` / entry `2024-08-13` close `8950`
- 360070 탑머티리얼: `atlas/ohlcv_tradable_by_symbol_year/360/360070/2024.csv` / `atlas/symbol_profiles/360/360070.json` / entry `2024-05-13` close `52900`
- 262260 에이프로: `atlas/ohlcv_tradable_by_symbol_year/262/262260/2023.csv` / `atlas/symbol_profiles/262/262260.json` / entry `2023-05-11` close `16390`
- 382840 원준: `atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv` / `atlas/symbol_profiles/382/382840.json` / entry `2024-04-22` close `15580`

## 11. Case-by-Case Trigger Grid

### C11L148_267320_20230403_NINETECH_LGE_207B_ORDER
Signed order was real, but the price path first punished entry. MFE_180D later reached 63.61%, yet drawdown after peak was -50.48%. This is not a simple positive; it is a staged-entry plus exit-guard case.

### C11L148_360070_20230308_TOPMATERIAL_693B_SYSTEM_ENGINEERING
The orderbook and US project bridge worked. MFE_30D and MFE_90D both reached 75.28%, with MFE_180D 80.38%. This is a structural success, but the post-peak drawdown confirms local 4B overlay need.

### C11L148_251630_20240118_VONETECH_LGE_90B_INSPECTION_ORDER
The LG order was named and measurable, but it did not overcome weak sector tape or margin/revenue uncertainty. MAE_180D was -63.73%. This is a contract-size-only false positive.

### C11L148_333620_20240813_NSYS_Q2_ORDER_CONVERSION
Prior orders converted into Q2 revenue and margin. MFE_30D/90D/180D all peaked at 46.15%, but 180D MAE reached -29.50%. Good Stage2-Actionable entry, but late 4B was costly.

### C11L148_360070_20240513_TOPMATERIAL_NEW_ORDER_GROWTH_FORECAST
Compared with the 2023 signed-order case, this 2024 trigger was forecast-heavy. 90D and 180D drawdowns show that expected new orders without fresh signed bridge should not be promoted aggressively.

### C11L148_262260_20230511_APRO_ACTIVATION_EQUIPMENT_ORDER_CYCLE
The activation-equipment capex cycle worked for 90D MFE, but 180D MAE shows how quickly an order-cycle positive can become exit-risk if not paired with 4B timing.

### C11L148_382840_20240422_WONJUN_HEAT_TREATMENT_TECHNOLOGY_EXPECTATION
Technology importance was true but not sufficient. Without near-term named orderbook/revenue timing, 90D MAE was -44.80%.

## 12. Trigger-Level OHLC Backtest Tables

| case | symbol | trigger | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 나인테크 | 267320 | Stage2 | 2023-04-03 | 3820 | 6.94 | -18.85 | 8.64 | -18.85 | 63.61 | -18.98 | current_profile_too_early |
| 탑머티리얼 | 360070 | Stage2-Actionable | 2023-03-08 | 53000 | 75.28 | -10.57 | 75.28 | -10.57 | 80.38 | -11.32 | current_profile_correct |
| 브이원텍 | 251630 | Stage2-Actionable | 2024-01-18 | 12200 | 3.28 | -30.33 | 3.28 | -33.77 | 3.28 | -63.73 | current_profile_false_positive |
| 엔시스 | 333620 | Stage2-Actionable | 2024-08-13 | 8950 | 46.15 | -2.23 | 46.15 | -22.91 | 46.15 | -29.5 | current_profile_4B_too_late |
| 탑머티리얼 | 360070 | Stage2 | 2024-05-13 | 52900 | 11.34 | -7.28 | 11.34 | -36.2 | 11.34 | -56.52 | current_profile_false_positive |
| 에이프로 | 262260 | Stage2-Actionable | 2023-05-11 | 16390 | 13.54 | -2.81 | 37.28 | -7.87 | 37.28 | -29.77 | current_profile_4B_too_late |
| 원준 | 382840 | Stage2 | 2024-04-22 | 15580 | 4.56 | -8.22 | 4.56 | -44.8 | 11.68 | -44.8 | current_profile_false_positive |


MFE/MAE formula used: max high / min low from entry date through N trading rows vs entry close. N = 30/90/180 trading days.

## 13. Current Calibrated Profile Stress Test

- `current_profile_correct`: 탑머티리얼 2023.
- `current_profile_4B_too_late`: 엔시스, 에이프로.
- `current_profile_too_early`: 나인테크.
- `current_profile_false_positive`: 브이원텍, 탑머티리얼 2024, 원준.

The residual error is not that Stage2 evidence bonus exists. It is that C11 needs stricter separation between signed/converted orderbook and forecast-only/order-size-only narrative.

## 14. Stage2 / Yellow / Green Comparison

No clean Stage3-Green trigger is emitted here. Green would require confirmed margin/revision and durable repeat conversion. For C11, signed order alone can be Stage2 or Stage2-Actionable, but Green without revenue/margin conversion would have been false precision in 브이원텍, 원준, and 탑머티리얼 2024.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

Local 4B is necessary for C11 positives because fast orderbook rerating often gives a brief MFE window before EV-cycle drawdown. 탑머티리얼 2023, 엔시스, 에이프로, and 나인테크 all show drawdown_after_peak near or beyond -48%. This supports a C11-specific exit overlay, not a full bearish thesis break at entry.

## 16. 4C Protection Audit

Hard 4C should not fire on weak stock path alone. It should fire only when orderbook/revenue evidence breaks: call-off, named order delay/cancellation, or severe margin conversion failure. In this sample, 브이원텍, 탑머티리얼 2024, and 원준 are thesis-break-watch cases rather than immediate hard 4C at trigger date.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L3_BATTERY_ORDERBOOK_REVENUE_TIMING_AND_EV_TAPE_GATE_V1
```

For L3 battery equipment/material orderbook names, require at least one hard commercial bridge and one conversion bridge before Stage2-Actionable. Hard commercial bridge: signed order, named customer, order backlog, or capex program. Conversion bridge: delivery timing, revenue recognition, margin/revision, or demonstrated prior-order conversion.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C11_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_EXIT_GUARD_GATE_V3
```

C11 should distinguish four leaves:

1. signed order + revenue/margin timing = actionable;
2. signed order but no margin bridge in weak tape = watch;
3. forecast-only orderbook narrative = watch or reject;
4. confirmed conversion with fast MFE = actionable plus local 4B exit overlay.

## 19. Before / After Backtest Comparison

| profile_id | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 7 | 26.65 | -25.00 | 36.25 | -36.37 | 0.57 | too permissive for contract-size-only C11 |
| P0b e2r_2_0_baseline_reference | 7 | 26.65 | -25.00 | 36.25 | -36.37 | 0.57 | similar but less explicit about 4B overlay |
| P1 sector_specific_candidate_profile | 4 | 42.14 | -14.55 | 56.86 | -22.39 | 0.25 | better, keeps NineTech as staged watch |
| P2 canonical_archetype_candidate_profile | 3 | 52.90 | -13.78 | 54.60 | -23.53 | 0.00 | best precision; accepts signed+conversion positives only |
| P3 counterexample_guard_profile | 3 | 6.96 | -33.41 | 22.48 | -46.01 | n/a | guard bucket correctly isolates failures |


## 20. Score-Return Alignment Matrix

The positive bucket has average MFE_90D 52.90% and average MAE_90D -13.78%. The counterexample bucket has average MFE_90D 6.96% and average MAE_90D -33.41%. This gap is explained less by order size itself and more by whether the orderbook has revenue/margin timing and whether the EV equipment tape is supportive.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | mixed_c11_equipment_orderbook_quality_revenue_timing_exit_leaf_set | 3 | 4 | 5 | 3 | 7 | 0 | 7 | 7 | 5 | L3_BATTERY_ORDERBOOK_REVENUE_TIMING_AND_EV_TAPE_GATE_V1 | C11_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_EXIT_GUARD_GATE_V3 | index baseline 18 -> 25; session-aware after loop131/141/148 about 36 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: contract_size_without_margin_bridge_false_positive|orderbook_forecast_without_signed_order_false_positive|confirmed_order_conversion_needs_4B_exit_guard|technology_importance_without_near_orderbook_false_positive
new_axis_proposed: c11_orderbook_quality_revenue_timing_and_exit_guard_gate_v3
existing_axis_strengthened: full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus|hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L3_BATTERY_ORDERBOOK_REVENUE_TIMING_AND_EV_TAPE_GATE_V1
canonical_archetype_rule_candidate: C11_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_EXIT_GUARD_GATE_V3
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical C11 trigger-level calibration using stock-web 1D OHLCV only. Non-validation scope: live recommendation, forward watchlist, production scoring patch, brokerage/API action, or current market opinion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_orderbook_quality_revenue_timing_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,Require signed/order-quality plus revenue or margin timing bridge; downgrade forecast-only or order-without-margin cases,avg positive MFE90 52.9 vs counterexample MFE90 7.0; counterexample MAE90 -33.4,TRIG_R3_L148_C11_02_360070_20230308|TRIG_R3_L148_C11_04_333620_20240813|TRIG_R3_L148_C11_06_262260_20230511,7,7,4,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c11_4b_exit_after_fast_orderbook_mfe,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,Add local 4B/exit watch when early MFE appears but 180D drawdown after peak exceeds 45%,captures TopMaterial 2023 NSYS APRO and NineTech delayed-MFE drawdowns,TRIG_R3_L148_C11_02_360070_20230308|TRIG_R3_L148_C11_04_333620_20240813|TRIG_R3_L148_C11_06_262260_20230511,7,7,4,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C11L148_267320_20230403_NINETECH_LGE_207B_ORDER", "symbol": "267320", "company_name": "나인테크", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_SIGNED_ORDER_HIGH_MAE_DELAYED_MFE", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R3_L148_C11_01_267320_20230403", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_or_guard_needed", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "계약 크기는 컸지만 30/90D 경로는 음수권이었다가 180D 내 테마성 peak가 뒤늦게 출현. 단일 수주 headline은 staged-entry/exit guard가 필요."}
{"row_type": "case", "case_id": "C11L148_360070_20230308_TOPMATERIAL_693B_SYSTEM_ENGINEERING", "symbol": "360070", "company_name": "탑머티리얼", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_SYSTEM_ENGINEERING_US_PROJECT_ORDERBOOK_RERATING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R3_L148_C11_02_360070_20230308", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "수주 규모와 미국 프로젝트 visibility가 맞물리며 30D/90D MFE가 폭발. 다만 peak 후 drawdown도 커 4B exit guard가 필요."}
{"row_type": "case", "case_id": "C11L148_251630_20240118_VONETECH_LGE_90B_INSPECTION_ORDER", "symbol": "251630", "company_name": "브이원텍", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_INSPECTION_ORDER_WITH_WEAK_SECTOR_TAPE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R3_L148_C11_03_251630_20240118", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_or_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "계약 자체는 명확했지만 EV 장비 tape와 매출/마진 bridge가 약해 30/90/180D 모두 큰 drawdown."}
{"row_type": "case", "case_id": "C11L148_333620_20240813_NSYS_Q2_ORDER_CONVERSION", "symbol": "333620", "company_name": "엔시스", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_INSPECTION_PRIOR_ORDER_TO_MARGIN_CONVERSION", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R3_L148_C11_04_333620_20240813", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "수주→매출→마진 전환의 깨끗한 positive. 그러나 30D MFE 후 180D 음수 전환이 커 4B overlay가 유효."}
{"row_type": "case", "case_id": "C11L148_360070_20240513_TOPMATERIAL_NEW_ORDER_GROWTH_FORECAST", "symbol": "360070", "company_name": "탑머티리얼", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_FORECAST_WITHOUT_NEW_SIGNED_ORDER_IN_WEAK_TAPE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R3_L148_C11_05_360070_20240513", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_or_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2023년 signed-order positive와 달리 2024년은 전망/기대 중심. 실제 가격경로는 90D/180D MAE가 커졌다."}
{"row_type": "case", "case_id": "C11L148_262260_20230511_APRO_ACTIVATION_EQUIPMENT_ORDER_CYCLE", "symbol": "262260", "company_name": "에이프로", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FORMATION_EQUIPMENT_CUSTOMER_CAPEX_ORDER_CYCLE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R3_L148_C11_06_262260_20230511", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "30/90D MFE는 양호했으나 180D MAE가 -29.77%까지 커져 exit/4B overlay가 같이 필요."}
{"row_type": "case", "case_id": "C11L148_382840_20240422_WONJUN_HEAT_TREATMENT_TECHNOLOGY_EXPECTATION", "symbol": "382840", "company_name": "원준", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_HEAT_TREATMENT_TECHNOLOGY_EXPECTATION_WITH_ORDER_GAP_RISK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R3_L148_C11_07_382840_20240422", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_or_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "기술 중요성은 맞지만 trigger 시점의 명명 수주/매출 timing이 부족. 90D MAE -44.80%로 hard guard가 필요."}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L148_C11_01_267320_20230403", "case_id": "C11L148_267320_20230403_NINETECH_LGE_207B_ORDER", "symbol": "267320", "company_name": "나인테크", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_SIGNED_ORDER_HIGH_MAE_DELAYED_MFE", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_orderbook_rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2023-04-03", "entry_date": "2023-04-03", "entry_price": 3820.0, "evidence_available_at_that_date": "LG전자 207억원 2차전지 제조장비 공급계약, 최근 매출액 대비 32.81%, 계약기간 2024-12-30까지", "evidence_source": "https://www.theguru.co.kr/news/article.html?no=51903", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["repeat_order_or_conversion"], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267320/2023.csv", "profile_path": "atlas/symbol_profiles/267/267320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.94, "MFE_90D_pct": 8.64, "MFE_180D_pct": 63.61, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.85, "MAE_90D_pct": -18.85, "MAE_180D_pct": -18.98, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-21", "peak_price": 6250.0, "drawdown_after_peak_pct": -50.48, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "exit_guard_needed_after_fast_mfe", "four_b_evidence_type": "price_only_local_peak|margin_or_backlog_slowdown", "four_c_protection_label": null, "trigger_outcome_label": "signed_order_but_early_entry_high_mae_delayed_180D_mfe", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R3_L148_C11_267320_20230403", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L148_C11_02_360070_20230308", "case_id": "C11L148_360070_20230308_TOPMATERIAL_693B_SYSTEM_ENGINEERING", "symbol": "360070", "company_name": "탑머티리얼", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_SYSTEM_ENGINEERING_US_PROJECT_ORDERBOOK_RERATING", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_orderbook_rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-08", "entry_date": "2023-03-08", "entry_price": 53000.0, "evidence_available_at_that_date": "미국 프로젝트 중심 이차전지 시스템엔지니어링 누적/신규 수주 693억원 규모 보도", "evidence_source": "https://www.industrynews.co.kr/news/articleView.html?idxno=49090", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/360/360070/2023.csv", "profile_path": "atlas/symbol_profiles/360/360070.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 75.28, "MFE_90D_pct": 75.28, "MFE_180D_pct": 80.38, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.57, "MAE_90D_pct": -10.57, "MAE_180D_pct": -11.32, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-20", "peak_price": 95600.0, "drawdown_after_peak_pct": -50.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "exit_guard_needed_after_fast_mfe", "four_b_evidence_type": "price_only_local_peak|positioning_overheat", "four_c_protection_label": null, "trigger_outcome_label": "orderbook_quality_converted_to_fast_rerating_but_4B_exit_needed", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R3_L148_C11_360070_20230308", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L148_C11_03_251630_20240118", "case_id": "C11L148_251630_20240118_VONETECH_LGE_90B_INSPECTION_ORDER", "symbol": "251630", "company_name": "브이원텍", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_INSPECTION_ORDER_WITH_WEAK_SECTOR_TAPE", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_orderbook_rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-18", "entry_date": "2024-01-18", "entry_price": 12200.0, "evidence_available_at_that_date": "LG전자 90.369억원 규모 2차전지 검사시스템 공급계약, 2022년 연결 매출액의 15.12%, 계약기간 2025-12-30", "evidence_source": "https://securities.miraeasset.com/bbs/download/2128023.pdf?attachmentId=2128023", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["contract_delay", "margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/251/251630/2024.csv", "profile_path": "atlas/symbol_profiles/251/251630.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.28, "MFE_90D_pct": 3.28, "MFE_180D_pct": 3.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.33, "MAE_90D_pct": -33.77, "MAE_180D_pct": -63.73, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 12600.0, "drawdown_after_peak_pct": -64.88, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_or_block_before_actionable", "four_b_evidence_type": "contract_delay|margin_or_backlog_slowdown|price_only_local_peak", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "named_customer_contract_failed_price_path", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R3_L148_C11_251630_20240118", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L148_C11_04_333620_20240813", "case_id": "C11L148_333620_20240813_NSYS_Q2_ORDER_CONVERSION", "symbol": "333620", "company_name": "엔시스", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_INSPECTION_PRIOR_ORDER_TO_MARGIN_CONVERSION", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_orderbook_rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-12", "entry_date": "2024-08-13", "entry_price": 8950.0, "evidence_available_at_that_date": "2024년 2분기 매출 310.45억원, 영업이익 68.26억원, 전년 대비 영업이익 292.5% 증가; 지난해 수주 실적 반영과 원가절감 설명", "evidence_source": "https://n-sys.co.kr/kr/sub/pr/news_view.asp?idx=131", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/333/333620/2024.csv", "profile_path": "atlas/symbol_profiles/333/333620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 46.15, "MFE_90D_pct": 46.15, "MFE_180D_pct": 46.15, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.23, "MAE_90D_pct": -22.91, "MAE_180D_pct": -29.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 13080.0, "drawdown_after_peak_pct": -51.76, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "exit_guard_needed_after_fast_mfe", "four_b_evidence_type": "price_only_local_peak|positioning_overheat", "four_c_protection_label": null, "trigger_outcome_label": "order_conversion_success_but_fast_local_peak_reversal", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R3_L148_C11_333620_20240813", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L148_C11_05_360070_20240513", "case_id": "C11L148_360070_20240513_TOPMATERIAL_NEW_ORDER_GROWTH_FORECAST", "symbol": "360070", "company_name": "탑머티리얼", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_ORDERBOOK_FORECAST_WITHOUT_NEW_SIGNED_ORDER_IN_WEAK_TAPE", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_orderbook_rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2024-05-13", "entry_date": "2024-05-13", "entry_price": 52900.0, "evidence_available_at_that_date": "유럽·미국 신규 업체 공장 증설 지속, 올해 신규 수주 대폭 증가와 실적 성장 전망", "evidence_source": "https://www.dailyinvest.kr/news/articleView.html?idxno=58609", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["call_off_or_order_cut"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/360/360070/2024.csv", "profile_path": "atlas/symbol_profiles/360/360070.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.34, "MFE_90D_pct": 11.34, "MFE_180D_pct": 11.34, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.28, "MAE_90D_pct": -36.2, "MAE_180D_pct": -56.52, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-12", "peak_price": 58900.0, "drawdown_after_peak_pct": -60.95, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_or_block_before_actionable", "four_b_evidence_type": "margin_or_backlog_slowdown|positioning_overheat", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "orderbook_forecast_failed_under_EV_downcycle", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R3_L148_C11_360070_20240513", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L148_C11_06_262260_20230511", "case_id": "C11L148_262260_20230511_APRO_ACTIVATION_EQUIPMENT_ORDER_CYCLE", "symbol": "262260", "company_name": "에이프로", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FORMATION_EQUIPMENT_CUSTOMER_CAPEX_ORDER_CYCLE", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_orderbook_rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-11", "entry_date": "2023-05-11", "entry_price": 16390.0, "evidence_available_at_that_date": "LG에너지솔루션을 핵심 고객으로 둔 활성화 장비 업체, 북미 합작법인 증설과 장비 발주 cycle 전망", "evidence_source": "https://ssl.pstatic.net/imgstock/upload/research/company/1683763323752.pdf", "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/262/262260/2023.csv", "profile_path": "atlas/symbol_profiles/262/262260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.54, "MFE_90D_pct": 37.28, "MFE_180D_pct": 37.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.81, "MAE_90D_pct": -7.87, "MAE_180D_pct": -29.77, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-20", "peak_price": 22500.0, "drawdown_after_peak_pct": -48.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "exit_guard_needed_after_fast_mfe", "four_b_evidence_type": "price_only_local_peak|positioning_overheat", "four_c_protection_label": null, "trigger_outcome_label": "capex_order_cycle_positive_with_exit_risk", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R3_L148_C11_262260_20230511", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L148_C11_07_382840_20240422", "case_id": "C11L148_382840_20240422_WONJUN_HEAT_TREATMENT_TECHNOLOGY_EXPECTATION", "symbol": "382840", "company_name": "원준", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_HEAT_TREATMENT_TECHNOLOGY_EXPECTATION_WITH_ORDER_GAP_RISK", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_orderbook_rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2024-04-22", "entry_date": "2024-04-22", "entry_price": 15580.0, "evidence_available_at_that_date": "이차전지 양극재/음극재 열처리 기술 중요성과 EPC 사업 다각화 기대", "evidence_source": "https://m.thebell.co.kr/m/newsview.asp?newskey=202404220935151840108929&svccode=", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["contract_delay", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv", "profile_path": "atlas/symbol_profiles/382/382840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.56, "MFE_90D_pct": 4.56, "MFE_180D_pct": 11.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.22, "MAE_90D_pct": -44.8, "MAE_180D_pct": -44.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-07", "peak_price": 17400.0, "drawdown_after_peak_pct": -49.71, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_or_block_before_actionable", "four_b_evidence_type": "contract_delay|margin_or_backlog_slowdown", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "technology_importance_without_near_orderbook_failed", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R3_L148_C11_382840_20240422", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C11L148_267320_20230403_NINETECH_LGE_207B_ORDER", "trigger_id": "TRIG_R3_L148_C11_01_267320_20230403", "symbol": "267320", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 20, "relative_strength_score": 35, "customer_quality_score": 60, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 55, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10}, "weighted_score_before": 52.2, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 35, "margin_bridge_score": 13, "revision_score": 12, "relative_strength_score": 35, "customer_quality_score": 60, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 67, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10}, "weighted_score_after": 47.8, "stage_label_after": "Watch", "changed_components": ["margin_bridge_score", "execution_risk_score", "backlog_visibility_score", "revision_score"], "component_delta_explanation": "C11 gate adds revenue/margin timing confirmation and weak-sector-tape guard; confirmed order conversion is rewarded, forecast-only or order-without-margin is downgraded.", "MFE_90D_pct": 8.64, "MAE_90D_pct": -18.85, "score_return_alignment_label": "false_positive_or_high_mae_guard_needed", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C11L148_360070_20230308_TOPMATERIAL_693B_SYSTEM_ENGINEERING", "trigger_id": "TRIG_R3_L148_C11_02_360070_20230308", "symbol": "360070", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 74.6, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 78, "margin_bridge_score": 63, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 77.1, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "execution_risk_score", "backlog_visibility_score", "revision_score"], "component_delta_explanation": "C11 gate adds revenue/margin timing confirmation and weak-sector-tape guard; confirmed order conversion is rewarded, forecast-only or order-without-margin is downgraded.", "MFE_90D_pct": 75.28, "MAE_90D_pct": -10.57, "score_return_alignment_label": "good_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C11L148_251630_20240118_VONETECH_LGE_90B_INSPECTION_ORDER", "trigger_id": "TRIG_R3_L148_C11_03_251630_20240118", "symbol": "251630", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 35, "margin_bridge_score": 10, "revision_score": 20, "relative_strength_score": 35, "customer_quality_score": 65, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10}, "weighted_score_before": 45.7, "stage_label_before": "Watch", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 35, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 35, "customer_quality_score": 65, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 92, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10}, "weighted_score_after": 41.7, "stage_label_after": "Watch", "changed_components": ["margin_bridge_score", "execution_risk_score", "backlog_visibility_score", "revision_score"], "component_delta_explanation": "C11 gate adds revenue/margin timing confirmation and weak-sector-tape guard; confirmed order conversion is rewarded, forecast-only or order-without-margin is downgraded.", "MFE_90D_pct": 3.28, "MAE_90D_pct": -33.77, "score_return_alignment_label": "false_positive_or_high_mae_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C11L148_333620_20240813_NSYS_Q2_ORDER_CONVERSION", "trigger_id": "TRIG_R3_L148_C11_04_333620_20240813", "symbol": "333620", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 74.6, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 78, "margin_bridge_score": 63, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 77.1, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "execution_risk_score", "backlog_visibility_score", "revision_score"], "component_delta_explanation": "C11 gate adds revenue/margin timing confirmation and weak-sector-tape guard; confirmed order conversion is rewarded, forecast-only or order-without-margin is downgraded.", "MFE_90D_pct": 46.15, "MAE_90D_pct": -22.91, "score_return_alignment_label": "good_alignment", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C11L148_360070_20240513_TOPMATERIAL_NEW_ORDER_GROWTH_FORECAST", "trigger_id": "TRIG_R3_L148_C11_05_360070_20240513", "symbol": "360070", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 35, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 35, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 65, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10}, "weighted_score_before": 42.1, "stage_label_before": "Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 35, "margin_bridge_score": 3, "revision_score": 12, "relative_strength_score": 35, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 77, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10}, "weighted_score_after": 37.8, "stage_label_after": "Rejected", "changed_components": ["margin_bridge_score", "execution_risk_score", "backlog_visibility_score", "revision_score"], "component_delta_explanation": "C11 gate adds revenue/margin timing confirmation and weak-sector-tape guard; confirmed order conversion is rewarded, forecast-only or order-without-margin is downgraded.", "MFE_90D_pct": 11.34, "MAE_90D_pct": -36.2, "score_return_alignment_label": "false_positive_or_high_mae_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C11L148_262260_20230511_APRO_ACTIVATION_EQUIPMENT_ORDER_CYCLE", "trigger_id": "TRIG_R3_L148_C11_06_262260_20230511", "symbol": "262260", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 74.6, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 78, "margin_bridge_score": 63, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 77.1, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "execution_risk_score", "backlog_visibility_score", "revision_score"], "component_delta_explanation": "C11 gate adds revenue/margin timing confirmation and weak-sector-tape guard; confirmed order conversion is rewarded, forecast-only or order-without-margin is downgraded.", "MFE_90D_pct": 37.28, "MAE_90D_pct": -7.87, "score_return_alignment_label": "good_alignment", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C11L148_382840_20240422_WONJUN_HEAT_TREATMENT_TECHNOLOGY_EXPECTATION", "trigger_id": "TRIG_R3_L148_C11_07_382840_20240422", "symbol": "382840", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 10, "revision_score": 20, "relative_strength_score": 35, "customer_quality_score": 30, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10}, "weighted_score_before": 35.4, "stage_label_before": "Rejected", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 35, "customer_quality_score": 30, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 87, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": 10}, "weighted_score_after": 31.4, "stage_label_after": "Rejected", "changed_components": ["margin_bridge_score", "execution_risk_score", "backlog_visibility_score", "revision_score"], "component_delta_explanation": "C11 gate adds revenue/margin timing confirmation and weak-sector-tape guard; confirmed order conversion is rewarded, forecast-only or order-without-margin is downgraded.", "MFE_90D_pct": 4.56, "MAE_90D_pct": -44.8, "score_return_alignment_label": "false_positive_or_high_mae_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R3", "loop": "148", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "new_independent_case_count": 7, "reused_case_count": 0, "new_symbol_count": 6, "new_trigger_family_count": 7, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["contract_size_without_margin_bridge_false_positive", "orderbook_forecast_without_signed_order_false_positive", "confirmed_order_conversion_needs_4B_exit_guard", "technology_importance_without_near_orderbook_false_positive"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
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
completed_round = R3
completed_loop = 148
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|C14_EV_DEMAND_SLOWDOWN_4B_4C|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://github.com/Daikisong/stock-web/blob/main/atlas/manifest.json?plain=1
- All price rows were computed from stock-web local downloaded shards listed in section 10 using entry-date close.
