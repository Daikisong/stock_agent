# E2R Stock-Web v12 Residual Research — R3 loop 124 / L3 / C14 EV Demand Slowdown 4B·4C

```text
filename = e2r_stock_web_v12_residual_round_R3_loop_124_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round = R3
selected_loop = 124
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C14 EV-demand slowdown 4B/4C split, direct URL/proxy repair, complete 30/90/180D MFE/MAE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Executive summary

이번 연구는 C14_EV_DEMAND_SLOWDOWN_4B_4C의 잔여 오류를 보강한다. C14는 한 문장으로 “EV chasm / demand slowdown / utilization cut / inventory loss가 실제 thesis break인지, 아니면 회복 bridge가 남아 있는 4B watch인지”를 가르는 아키타입이다.

이번 표본의 핵심은 **hard 4C를 너무 빨리 걸면 POSCO퓨처엠·롯데에너지머티리얼즈 같은 rebound exception을 놓치고, 반대로 slowdown headline을 너무 가볍게 보면 에코프로비엠·엘앤에프 같은 깊은 90D/180D drawdown을 Stage2 watch로 방치한다**는 것이다. EV chasm headline은 빨간 신호등이지 다리 붕괴 보고서가 아니다. hard 4C는 교통이 느려졌다는 사실만이 아니라, 다리 상판 자체가 금 갔다는 증거가 두 개 이상 모일 때 눌러야 한다.

## 1. Selection rationale / No-repeat audit

- 직전 user-visible sequence에서 생성된 C05, C01, C13, C15, C10, C02, C16, R13, C17, C07, C06을 피했다.
- `docs/round` root에서 같은 pair의 기존 standard file은 R3/C14 loop 100, 120, 121, 122, 123까지 확인되므로 이번 output은 loop 124로 둔다.
- No-Repeat Index의 현재 국면은 모든 C01~C32 row 수량을 채운 뒤의 quality repair 단계다. 따라서 이번 선택은 단순 row 수 보강이 아니라 C14의 hard 4C confirmation, 4B rebound exception, proxy-only negative row 분리를 목표로 한다.

```text
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 7
calibration_usable_case_count = 6
calibration_usable_trigger_count = 6
trigger_rows_total = 7
positive_case_count = 3
counterexample_count = 4
stage4b_case_count = 4
stage4c_case_count = 3
source_proxy_only_count = 2
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
current_profile_error_count = 4
```

## 2. Stock-Web price source validation

```text
manifest = atlas/manifest.json
schema = atlas/schema.json
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_shard_columns = d/o/h/l/c/v/a/mc/s/m
raw_shard_columns = d/o/h/l/c/v/a/mc/s/m/rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

All price paths below were calculated from downloaded Stock-Web symbol-year CSV shards under `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`. Entry date follows the next-tradable-date rule when the evidence date is not itself the chosen entry row or when timing conservatism requires next trading day.

## 3. Case inventory

| case_id | symbol | company | trigger_type | trigger_date | entry_date | result_label | calibration_usable | source_proxy_only |
|---|---:|---|---|---:|---:|---|---:|---:|
| C14_R3L124_001_LGES_Q1_2024_EV_DEMAND_UTILIZATION_ADJUSTMENT | 373220 | LG에너지솔루션 | Stage4B | 2024-04-25 | 2024-04-26 | false_hard_4c_overblock_positive_rebound | true | false |
| C14_R3L124_002_SAMSUNG_SDI_Q2_2024_MUTED_EV_DEMAND_DELAYED_RECOVERY | 006400 | 삼성SDI | Stage4B | 2024-07-30 | 2024-07-31 | initial_rebound_then_high_MAE_4B_to_4C_timing_test | true | false |
| C14_R3L124_003_SK_INNOVATION_Q2_2024_BATTERY_LOSS_LOW_UTILIZATION | 096770 | SK이노베이션 | Stage4C | 2024-08-01 | 2024-08-02 | blocked_corporate_action_narrative_4c_reference | false | false |
| C14_R3L124_004_POSCO_FUTURE_M_2024_RESULTS_BATTERY_MATERIALS_LOSS_REBOUND_EXCEPTION | 003670 | POSCO퓨처엠 | Stage4B | 2025-02-03 | 2025-02-04 | false_hard_4c_overblock_large_rebound | true | false |
| C14_R3L124_005_ECOPRO_BM_Q2_2024_EV_SLOWDOWN_CAPACITY_ADJUSTMENT | 247540 | 에코프로비엠 | Stage4C | 2024-07-31 | 2024-08-01 | true_hard_4c_negative | true | true |
| C14_R3L124_006_LNF_MAY_2024_LITHIUM_EV_SLOWDOWN_LOSS_FORECAST | 066970 | 엘앤에프 | Stage4C | 2024-05-13 | 2024-05-14 | true_4c_negative_high_MAE | true | true |
| C14_R3L124_007_LOTTE_ENERGY_MATERIALS_2024_PRELIM_LOSS_FALSE_4C_OVERBLOCK | 020150 | 롯데에너지머티리얼즈 | Stage4B | 2025-01-24 | 2025-01-31 | false_hard_4c_overblock_positive_rebound | true | false |

## 4. Actual Stock-Web 1D OHLC path metrics

| symbol | entry_date | entry_close | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_180D | trough_180D | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| 373220 | 2024-04-26 | 372000 | 6.72 | -12.37 | 12.63 | -16.40 | 19.35 | -16.40 | 2024-10-08 / 444000 | 2024-08-05 / 311000 | -23.31 |
| 006400 | 2024-07-31 | 319500 | 18.94 | -7.82 | 23.16 | -26.29 | 23.16 | -46.79 | 2024-09-30 / 393500 | 2025-04-09 / 170000 | -56.80 |
| 096770 | 2024-08-02 | 104300 | 7.38 | -12.08 | 19.85 | -12.08 | 34.42 | -12.08 | 2025-03-13 / 140200 | 2024-08-05 / 91700 | -34.52 |
| 003670 | 2025-02-04 | 125000 | 24.48 | -1.84 | 24.48 | -21.20 | 108.00 | -21.20 | 2025-10-27 / 260000 | 2025-05-27 / 98500 | -12.69 |
| 247540 | 2024-08-01 | 185100 | 3.67 | -19.67 | 5.08 | -34.95 | 5.08 | -53.00 | 2024-10-10 / 194500 | 2025-04-03 / 87000 | -55.27 |
| 066970 | 2024-05-14 | 153700 | 15.16 | -9.24 | 15.16 | -46.06 | 15.16 | -50.10 | 2024-06-13 / 177000 | 2025-01-03 / 76700 | -56.67 |
| 020150 | 2025-01-31 | 22100 | 42.76 | -8.37 | 42.76 | -11.95 | 42.76 | -11.95 | 2025-02-20 / 31550 | 2025-05-22 / 19460 | -38.32 |

## 5. Entry row and validation notes

| symbol | entry_date | actual 1D OHLC | validation_scope |
|---:|---:|---|---|
| 373220 | 2024-04-26 | o=373000 h=375000 l=367500 c=372000 | 30D/90D/180D calibration usable; profile corporate_action_candidate_count=0 |
| 006400 | 2024-07-31 | o=330000 h=331500 l=312000 c=319500 | 30D/90D/180D calibration usable; profile corporate action dates outside 2024/2025 window |
| 096770 | 2024-08-02 | o=105100 h=106300 l=103000 c=104300 | blocked_by_corporate_action_contaminated_180D_window; profile corporate_action_candidate_date=2024-11-20 overlaps entry~D+180 |
| 003670 | 2025-02-04 | o=131300 h=133600 l=124800 c=125000 | 30D/90D/180D calibration usable; profile corporate action dates outside 2025 window |
| 247540 | 2024-08-01 | o=180000 h=186600 l=170800 c=185100 | 30D/90D/180D calibration usable; proxy source retained for guardrail not positive promotion |
| 066970 | 2024-05-14 | o=156500 h=159000 l=153500 c=153700 | 30D/90D/180D calibration usable; proxy source retained for negative guardrail only |
| 020150 | 2025-01-31 | o=22900 h=23000 l=22100 c=22100 | 30D/90D/180D calibration usable; profile corporate_action_candidate_count=0 |

## 6. Evidence notes and score-return alignment

### C14_R3L124_001_LGES_Q1_2024_EV_DEMAND_UTILIZATION_ADJUSTMENT — LG에너지솔루션 (373220)

- trigger_type: `Stage4B`
- evidence_family: `official_Q1_2024_EV_demand_slowdown_utilization_adjustment_AMPC_GM_JV_bridge`
- evidence_url: https://inside.lgensol.com/en/2024/04/lg-energy-solution-makes-progress-amid-market-uncertainties-aims-to-strengthen-fundamental-competitiveness-this-year/
- interpretation: Q1 매출/OP 하락과 EV 수요둔화·utilization adjustment는 진짜였지만 AMPC, GM JV Tennessee shipment, Arizona/ESS bridge가 남아 있어 hard 4C보다는 4B watch가 맞았던 케이스.
- score_simulation_proxy: `EPS 11 / Vis 13 / Bott 8 / Mis 8 / Val 5 / Cap 4 / Info 8 / risk -10 = 47 pre-stage; 4B overlay`
- residual_contribution: C14 needs hard-4C confirmation rather than automatic thesis-break from one-quarter EV demand slowdown.

### C14_R3L124_002_SAMSUNG_SDI_Q2_2024_MUTED_EV_DEMAND_DELAYED_RECOVERY — 삼성SDI (006400)

- trigger_type: `Stage4B`
- evidence_family: `official_Q2_2024_muted_EV_demand_later_recovery_P6_ESS_StarPlus_bridge`
- evidence_url: https://www.samsungsdi.com/sdi-now/sdi-news/3862.html
- interpretation: 공식 release가 “muted EV market demand”와 회복 지연을 말했지만 P6·ESS·StarPlus bridge도 제시했다. 90D MFE는 컸으나 180D MAE가 깊어 4B→4C 전환 타이밍 검증에 좋다.
- score_simulation_proxy: `EPS 10 / Vis 14 / Bott 7 / Mis 7 / Val 5 / Cap 5 / Info 9 / risk -14 = 43; 4B with follow-through failure watch`
- residual_contribution: C14 requires post-bounce follow-through test; 30D/90D rebound did not protect from -46.79% MAE_180D.

### C14_R3L124_003_SK_INNOVATION_Q2_2024_BATTERY_LOSS_LOW_UTILIZATION — SK이노베이션 (096770)

- trigger_type: `Stage4C`
- evidence_family: `official_Q2_2024_battery_loss_low_utilization_AMPC_not_enough`
- evidence_url: https://www.skinnovation.com/esg_report/re/1/SK%20innovation_earning%20release_2Q24.pdf
- interpretation: 배터리 부문의 낮은 가동률과 초기비용, AMPC에도 불구한 손실 확대는 4C 논리에 가깝지만 2024-11-20 corporate-action candidate contamination 때문에 calibration_usable=false 처리.
- score_simulation_proxy: `EPS 8 / Vis 9 / Bott 6 / Mis 6 / Val 4 / Cap 4 / Info 8 / risk -18 = 27; 4C narrative-only`
- residual_contribution: Hard 4C logic is useful but row must not enter calibration aggregate because 180D window overlaps corporate-action candidate.

### C14_R3L124_004_POSCO_FUTURE_M_2024_RESULTS_BATTERY_MATERIALS_LOSS_REBOUND_EXCEPTION — POSCO퓨처엠 (003670)

- trigger_type: `Stage4B`
- evidence_family: `official_2024_results_OP_down_98_battery_materials_loss_inventory_loss_next_gen_bridge`
- evidence_url: https://www.poscofuturem.com/en/pr/view.do?num=899
- interpretation: 2024 OP -98%, battery materials 적자, cathode ASP/inventory loss는 컸지만 next-generation material roadmap과 recovery optionality가 남아 있어 hard 4C로 완전히 막으면 +108% MFE를 놓치는 경로.
- score_simulation_proxy: `EPS 9 / Vis 12 / Bott 8 / Mis 9 / Val 7 / Cap 4 / Info 9 / risk -12 = 46; 4B overblock exception`
- residual_contribution: Massive 180D MFE after severe 2024 earnings miss shows C14 hard 4C requires bridge-death, not merely chasm-year loss.

### C14_R3L124_005_ECOPRO_BM_Q2_2024_EV_SLOWDOWN_CAPACITY_ADJUSTMENT — 에코프로비엠 (247540)

- trigger_type: `Stage4C`
- evidence_family: `media_Q2_2024_OP_down_96_sales_down_57_EV_slowdown_capacity_adjustment`
- evidence_url: https://www.koreatimes.co.kr/business/companies/20240731/posco-ecopro-lf-hit-by-ev-slowdown
- interpretation: Q2 OP -96.6%, sales -57.5%, EV 성장둔화와 capacity plan 조정이 같이 나와 hard 4C 쪽이 맞았고, 180D MAE -53.00%로 검증됐다.
- score_simulation_proxy: `EPS 7 / Vis 7 / Bott 5 / Mis 5 / Val 4 / Cap 4 / Info 6 / risk -18 = 20; hard 4C`
- residual_contribution: Low MFE and deep 180D MAE validate C14 hard-4C route when slowdown is symbol-level and margin/volume bridge is broken.

### C14_R3L124_006_LNF_MAY_2024_LITHIUM_EV_SLOWDOWN_LOSS_FORECAST — 엘앤에프 (066970)

- trigger_type: `Stage4C`
- evidence_family: `media_analyst_2024_sales_down_OP_loss_lithium_price_EV_slowdown`
- evidence_url: https://www.asiae.co.kr/en/print.htm?idxno=2024051307291711113
- interpretation: 2024 매출 감소와 연간 영업손실 전망, 리튬가격/EV slowdown 압박이 결합되어 30D 반등 후 90D/180D 급락으로 이어진 hard 4C 케이스.
- score_simulation_proxy: `EPS 7 / Vis 8 / Bott 5 / Mis 6 / Val 4 / Cap 3 / Info 6 / risk -17 = 22; hard 4C`
- residual_contribution: Deep 90D/180D MAE validates hard-4C when cathode margin pressure and loss forecast are explicit and recovery bridge is weak.

### C14_R3L124_007_LOTTE_ENERGY_MATERIALS_2024_PRELIM_LOSS_FALSE_4C_OVERBLOCK — 롯데에너지머티리얼즈 (020150)

- trigger_type: `Stage4B`
- evidence_family: `official_2024_preliminary_loss_EV_slowdown_customer_inventory_north_america_stable_financial_bridge`
- evidence_url: https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128
- interpretation: 2024 operating loss와 EV slow/chasm은 있었지만 고객다변화·북미 매출·재무안정성 bridge가 남아 있어 hard 4C 대신 4B watch가 맞았던 rebound exception.
- score_simulation_proxy: `EPS 9 / Vis 11 / Bott 7 / Mis 9 / Val 7 / Cap 5 / Info 8 / risk -11 = 45; 4B overblock exception`
- residual_contribution: Despite operating loss, 42.76% MFE with shallow MAE shows loss headline must be split from durable thesis death.


## 7. Residual error family

### 7.1 Hard 4C too early / overblock

- LG에너지솔루션, POSCO퓨처엠, 롯데에너지머티리얼즈는 headline 자체는 나쁘다. EV 수요둔화, utilization adjustment, operating-loss or inventory-loss language가 있었다.
- 그러나 official counter-bridge가 남아 있었다. LGES에는 AMPC, GM JV shipment, ESS/Arizona bridge가 있었고, POSCO Future M에는 next-generation battery material roadmap과 recovery optionality가 있었으며, Lotte Energy Materials에는 diversified customer base / North America sales / stable financial position bridge가 있었다.
- 이 그룹은 Stage4B watch는 필요하지만 hard 4C를 바로 눌렀다면 180D MFE +19.35%, +108.00%, +42.76%를 놓친다.

### 7.2 4B rebound trap / delayed 4C

- 삼성SDI는 30D/90D MFE가 각각 +18.94%, +23.16%였으나 180D MAE는 -46.79%까지 열렸다.
- C14에서는 local rebound가 thesis repair를 뜻하지 않는다. muted demand와 delayed recovery가 남아 있으면 4B watch 후 follow-through confirmation이 없을 때 4C 재평가가 필요하다.

### 7.3 True hard 4C / no positive-stage unlock

- 에코프로비엠과 엘앤에프는 source_proxy_only이지만 negative guardrail에는 유용하다.
- OP/sales collapse, loss forecast, lithium/EV slowdown, capacity/investment adjustment가 symbol-level로 결합되면 Stage2/Stage3 unlock이 아니라 hard 4C 또는 hard 4C watch로 가야 한다.
- SK이노베이션은 논리상 hard 4C reference지만 2024-11-20 corporate-action candidate가 entry~D+180 window를 오염시켜 calibration_usable=false로 둔다.

## 8. Shadow rule candidate

```text
new_axis_proposed = C14_EV_DEMAND_4C_CONFIRMATION_AND_REBOUND_EXCEPTION_GATE
production_scoring_changed = false
shadow_weight_only = true
```

### Proposed gate

C14 hard 4C는 아래 중 최소 2개가 symbol-level로 확인될 때만 full thesis break로 route한다.

1. sustained operating loss or explicit negative margin path
2. utilization cut, customer inventory adjustment, or lower plant utilization
3. explicit capacity/capex slowdown, customer call-off, or investment pace reduction
4. inventory valuation/raw-material price loss with no offsetting bridge
5. weak guidance with no recovery bridge

반대로 아래 bridge 중 2개 이상이 official source에 있으면 hard 4C 대신 Stage4B watch로 cap한다.

1. AMPC/IRA/tax-credit bridge that actually offsets loss
2. ESS/customer diversification or non-EV demand bridge
3. named launch/new product/customer shipment/JV ramp
4. North America/customer-specific revenue bridge
5. stable balance sheet / financial stability / no debt-stress language

### Existing axes strengthened

```text
stage2_required_bridge = strengthened
local_4b_watch_guard = strengthened
hard_4c_confirmation = strengthened
full_4b_requires_non_price_evidence = strengthened
drawdown_aware_confirmation = strengthened
```

## 9. JSONL rows

```jsonl
{"row_type":"trigger","case_id":"C14_R3L124_001_LGES_Q1_2024_EV_DEMAND_UTILIZATION_ADJUSTMENT","symbol":"373220","company":"LG에너지솔루션","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","trigger_type":"Stage4B","trigger_date":"2024-04-25","entry_date":"2024-04-26","entry_price":372000.0,"MFE_30D_pct":6.72,"MAE_30D_pct":-12.37,"MFE_90D_pct":12.63,"MAE_90D_pct":-16.4,"MFE_180D_pct":19.35,"MAE_180D_pct":-16.4,"peak_180D_date":"2024-10-08","peak_180D_price":444000.0,"trough_180D_date":"2024-08-05","trough_180D_price":311000.0,"drawdown_after_peak_pct":-23.31,"calibration_usable":true,"validation_scope":"30D/90D/180D calibration usable; profile corporate_action_candidate_count=0","source_proxy_only":false,"evidence_url":"https://inside.lgensol.com/en/2024/04/lg-energy-solution-makes-progress-amid-market-uncertainties-aims-to-strengthen-fundamental-competitiveness-this-year/","evidence_family":"official_Q1_2024_EV_demand_slowdown_utilization_adjustment_AMPC_GM_JV_bridge","same_entry_group":"C14_EV_DEMAND_SLOWDOWN_4B_4C|373220|Stage4B|2024-04-26","do_not_count_as_new_case":false,"reuse_reason":null,"current_profile_error_family":"hard_4c_overblock_risk_when_EV_slowdown_headline_has_GM_JV_AMPC_ESS_bridge","residual_contribution":"C14 needs hard-4C confirmation rather than automatic thesis-break from one-quarter EV demand slowdown."}
{"row_type":"trigger","case_id":"C14_R3L124_002_SAMSUNG_SDI_Q2_2024_MUTED_EV_DEMAND_DELAYED_RECOVERY","symbol":"006400","company":"삼성SDI","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","trigger_type":"Stage4B","trigger_date":"2024-07-30","entry_date":"2024-07-31","entry_price":319500.0,"MFE_30D_pct":18.94,"MAE_30D_pct":-7.82,"MFE_90D_pct":23.16,"MAE_90D_pct":-26.29,"MFE_180D_pct":23.16,"MAE_180D_pct":-46.79,"peak_180D_date":"2024-09-30","peak_180D_price":393500.0,"trough_180D_date":"2025-04-09","trough_180D_price":170000.0,"drawdown_after_peak_pct":-56.8,"calibration_usable":true,"validation_scope":"30D/90D/180D calibration usable; profile corporate action dates outside 2024/2025 window","source_proxy_only":false,"evidence_url":"https://www.samsungsdi.com/sdi-now/sdi-news/3862.html","evidence_family":"official_Q2_2024_muted_EV_demand_later_recovery_P6_ESS_StarPlus_bridge","same_entry_group":"C14_EV_DEMAND_SLOWDOWN_4B_4C|006400|Stage4B|2024-07-31","do_not_count_as_new_case":false,"reuse_reason":null,"current_profile_error_family":"local_rebound_can_mask_180D_thesis_decay_if_no_follow_through_confirmation","residual_contribution":"C14 requires post-bounce follow-through test; 30D/90D rebound did not protect from -46.79% MAE_180D."}
{"row_type":"trigger","case_id":"C14_R3L124_003_SK_INNOVATION_Q2_2024_BATTERY_LOSS_LOW_UTILIZATION","symbol":"096770","company":"SK이노베이션","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","trigger_type":"Stage4C","trigger_date":"2024-08-01","entry_date":"2024-08-02","entry_price":104300.0,"MFE_30D_pct":7.38,"MAE_30D_pct":-12.08,"MFE_90D_pct":19.85,"MAE_90D_pct":-12.08,"MFE_180D_pct":34.42,"MAE_180D_pct":-12.08,"peak_180D_date":"2025-03-13","peak_180D_price":140200.0,"trough_180D_date":"2024-08-05","trough_180D_price":91700.0,"drawdown_after_peak_pct":-34.52,"calibration_usable":false,"validation_scope":"blocked_by_corporate_action_contaminated_180D_window; profile corporate_action_candidate_date=2024-11-20 overlaps entry~D+180","source_proxy_only":false,"evidence_url":"https://www.skinnovation.com/esg_report/re/1/SK%20innovation_earning%20release_2Q24.pdf","evidence_family":"official_Q2_2024_battery_loss_low_utilization_AMPC_not_enough","same_entry_group":"C14_EV_DEMAND_SLOWDOWN_4B_4C|096770|Stage4C|2024-08-02","do_not_count_as_new_case":true,"reuse_reason":null,"current_profile_error_family":"do_not_promote_due_corporate_action_window_even_with_complete_mfe_mae","residual_contribution":"Hard 4C logic is useful but row must not enter calibration aggregate because 180D window overlaps corporate-action candidate."}
{"row_type":"trigger","case_id":"C14_R3L124_004_POSCO_FUTURE_M_2024_RESULTS_BATTERY_MATERIALS_LOSS_REBOUND_EXCEPTION","symbol":"003670","company":"POSCO퓨처엠","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","trigger_type":"Stage4B","trigger_date":"2025-02-03","entry_date":"2025-02-04","entry_price":125000.0,"MFE_30D_pct":24.48,"MAE_30D_pct":-1.84,"MFE_90D_pct":24.48,"MAE_90D_pct":-21.2,"MFE_180D_pct":108.0,"MAE_180D_pct":-21.2,"peak_180D_date":"2025-10-27","peak_180D_price":260000.0,"trough_180D_date":"2025-05-27","trough_180D_price":98500.0,"drawdown_after_peak_pct":-12.69,"calibration_usable":true,"validation_scope":"30D/90D/180D calibration usable; profile corporate action dates outside 2025 window","source_proxy_only":false,"evidence_url":"https://www.poscofuturem.com/en/pr/view.do?num=899","evidence_family":"official_2024_results_OP_down_98_battery_materials_loss_inventory_loss_next_gen_bridge","same_entry_group":"C14_EV_DEMAND_SLOWDOWN_4B_4C|003670|Stage4B|2025-02-04","do_not_count_as_new_case":false,"reuse_reason":null,"current_profile_error_family":"hard_4c_too_early_when_2024_loss_has_inventory_cycle_and_next_gen_recovery_bridge","residual_contribution":"Massive 180D MFE after severe 2024 earnings miss shows C14 hard 4C requires bridge-death, not merely chasm-year loss."}
{"row_type":"trigger","case_id":"C14_R3L124_005_ECOPRO_BM_Q2_2024_EV_SLOWDOWN_CAPACITY_ADJUSTMENT","symbol":"247540","company":"에코프로비엠","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","trigger_type":"Stage4C","trigger_date":"2024-07-31","entry_date":"2024-08-01","entry_price":185100.0,"MFE_30D_pct":3.67,"MAE_30D_pct":-19.67,"MFE_90D_pct":5.08,"MAE_90D_pct":-34.95,"MFE_180D_pct":5.08,"MAE_180D_pct":-53.0,"peak_180D_date":"2024-10-10","peak_180D_price":194500.0,"trough_180D_date":"2025-04-03","trough_180D_price":87000.0,"drawdown_after_peak_pct":-55.27,"calibration_usable":true,"validation_scope":"30D/90D/180D calibration usable; proxy source retained for guardrail not positive promotion","source_proxy_only":true,"evidence_url":"https://www.koreatimes.co.kr/business/companies/20240731/posco-ecopro-lf-hit-by-ev-slowdown","evidence_family":"media_Q2_2024_OP_down_96_sales_down_57_EV_slowdown_capacity_adjustment","same_entry_group":"C14_EV_DEMAND_SLOWDOWN_4B_4C|247540|Stage4C|2024-08-01","do_not_count_as_new_case":false,"reuse_reason":null,"current_profile_error_family":"positive_stage_must_be_blocked_when_profit_sales_collapse_and_capacity_plan_slows","residual_contribution":"Low MFE and deep 180D MAE validate C14 hard-4C route when slowdown is symbol-level and margin/volume bridge is broken."}
{"row_type":"trigger","case_id":"C14_R3L124_006_LNF_MAY_2024_LITHIUM_EV_SLOWDOWN_LOSS_FORECAST","symbol":"066970","company":"엘앤에프","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","trigger_type":"Stage4C","trigger_date":"2024-05-13","entry_date":"2024-05-14","entry_price":153700.0,"MFE_30D_pct":15.16,"MAE_30D_pct":-9.24,"MFE_90D_pct":15.16,"MAE_90D_pct":-46.06,"MFE_180D_pct":15.16,"MAE_180D_pct":-50.1,"peak_180D_date":"2024-06-13","peak_180D_price":177000.0,"trough_180D_date":"2025-01-03","trough_180D_price":76700.0,"drawdown_after_peak_pct":-56.67,"calibration_usable":true,"validation_scope":"30D/90D/180D calibration usable; proxy source retained for negative guardrail only","source_proxy_only":true,"evidence_url":"https://www.asiae.co.kr/en/print.htm?idxno=2024051307291711113","evidence_family":"media_analyst_2024_sales_down_OP_loss_lithium_price_EV_slowdown","same_entry_group":"C14_EV_DEMAND_SLOWDOWN_4B_4C|066970|Stage4C|2024-05-14","do_not_count_as_new_case":false,"reuse_reason":null,"current_profile_error_family":"if_stage2_watch_stays_open_after_loss_forecast_it_is_false_positive","residual_contribution":"Deep 90D/180D MAE validates hard-4C when cathode margin pressure and loss forecast are explicit and recovery bridge is weak."}
{"row_type":"trigger","case_id":"C14_R3L124_007_LOTTE_ENERGY_MATERIALS_2024_PRELIM_LOSS_FALSE_4C_OVERBLOCK","symbol":"020150","company":"롯데에너지머티리얼즈","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","trigger_type":"Stage4B","trigger_date":"2025-01-24","entry_date":"2025-01-31","entry_price":22100.0,"MFE_30D_pct":42.76,"MAE_30D_pct":-8.37,"MFE_90D_pct":42.76,"MAE_90D_pct":-11.95,"MFE_180D_pct":42.76,"MAE_180D_pct":-11.95,"peak_180D_date":"2025-02-20","peak_180D_price":31550.0,"trough_180D_date":"2025-05-22","trough_180D_price":19460.0,"drawdown_after_peak_pct":-38.32,"calibration_usable":true,"validation_scope":"30D/90D/180D calibration usable; profile corporate_action_candidate_count=0","source_proxy_only":false,"evidence_url":"https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128","evidence_family":"official_2024_preliminary_loss_EV_slowdown_customer_inventory_north_america_stable_financial_bridge","same_entry_group":"C14_EV_DEMAND_SLOWDOWN_4B_4C|020150|Stage4B|2025-01-31","do_not_count_as_new_case":false,"reuse_reason":null,"current_profile_error_family":"hard_4c_overblock_when_loss_is_inventory_utilization_cycle_not_balance_sheet_break","residual_contribution":"Despite operating loss, 42.76% MFE with shallow MAE shows loss headline must be split from durable thesis death."}
{"row_type":"v12_aggregate","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","new_independent_case_count":7,"reused_case_count":0,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"calibration_usable_case_count":6,"calibration_usable_trigger_count":6,"trigger_rows_total":7,"positive_case_count":3,"counterexample_count":4,"stage4b_case_count":4,"stage4c_case_count":3,"source_proxy_only_count":2,"evidence_url_pending_count":0,"rows_missing_required_mfe_mae":0,"current_profile_error_count":4,"selection_basis":"docs/core/V12_Research_No_Repeat_Index.md","round_schedule_status":"coverage_index_selected","round_sector_consistency":"pass"}
{"row_type":"shadow_weight_candidate","axis":"C14_EV_DEMAND_4C_CONFIRMATION_AND_REBOUND_EXCEPTION_GATE","selected_round":"R3","selected_loop":124,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_MARGIN_INVENTORY_4B_4C_SPLIT","production_scoring_changed":false,"shadow_weight_only":true,"rule_candidate":"For C14, route to hard 4C only when symbol-level EV slowdown evidence includes at least two of sustained operating loss/negative margin, utilization or customer inventory cut, explicit capacity/capex slowdown or customer call-off, inventory valuation/raw-material loss with no offset, weak guidance/no recovery bridge. Keep as 4B watch when official counter-bridges such as AMPC/IRA, ESS/customer diversification, launch/new-product bridge, confirmed customer shipment/JV ramp, or stable balance sheet remain.","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","hard_4c_confirmation","full_4b_requires_non_price_evidence","drawdown_aware_confirmation"],"existing_axis_weakened":[]}
```

## 10. Batch ingest self-audit

```text
required_filename_regex_pass = true
compact_filename_forbidden = true
filename_round = R3
metadata_round = R3
filename_loop = 124
metadata_loop = 124
large_sector_id_valid = true
canonical_archetype_id_valid = true
round_sector_consistency = pass
trigger_type_canonical_stage_label_only = true
MFE_30D_pct_present_all_trigger_rows = true
MFE_90D_pct_present_all_trigger_rows = true
MFE_180D_pct_present_all_trigger_rows = true
MAE_30D_pct_present_all_trigger_rows = true
MAE_90D_pct_present_all_trigger_rows = true
MAE_180D_pct_present_all_trigger_rows = true
rows_missing_required_mfe_mae = 0
actual_stock_web_1D_OHLC_used = true
manifest_max_date_respected = true
corporate_action_contamination_checked = true
096770_SK_Innovation_calibration_usable = false
096770_block_reason = corporate_action_contaminated_180D_window
source_proxy_only_rows_not_used_for_positive_promotion = true
evidence_url_pending_count = 0
same_entry_duplicate_count = 0
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not execute this handoff during research generation.

Input file:
e2r_stock_web_v12_residual_round_R3_loop_124_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md

Task:
1. Parse JSONL trigger, aggregate, and shadow_weight_candidate rows.
2. Validate every trigger row has MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
3. Exclude calibration_usable=false rows from promotion aggregate while retaining them for narrative-only blocked-reason analysis.
4. Treat source_proxy_only=true rows as guardrail evidence only unless later direct company/KRX/KIND evidence is attached.
5. Evaluate whether C14_EV_DEMAND_4C_CONFIRMATION_AND_REBOUND_EXCEPTION_GATE should be merged into the C14 runtime rule profile as a shadow-only candidate.
6. Do not loosen Stage3-Green threshold. Do not change production scoring unless the batch promotion planner independently approves.
```

## 12. Completed state

```text
completed_round = R3
completed_loop = 124
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C14 EV-demand slowdown 4B/4C split, direct URL/proxy repair, complete 30/90/180D MFE/MAE
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION; C18_CONSUMER_EXPORT_CHANNEL_REORDER; C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY; C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
