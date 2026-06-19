# E2R Stock-Web v12 Residual Research — R13 Stage2 False Positive Review

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R13
selected_loop = 153
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 over-repeat inspection / taxonomy repair — R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id = CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
output_filename = e2r_stock_web_v12_residual_round_R13_loop_153_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
```

## 0. Executive Summary

이번 R13 실행은 새 섹터 winner를 찾는 연구가 아니라, 이미 충분히 쌓인 C01~C32 corpus 위에서 **Stage2 false positive가 어떤 얼굴로 반복되는지**를 압축하는 cross-archetype holdout이다. 같은 Stage2라도 삼양식품·HD현대일렉트릭·유한양행처럼 비가격 bridge가 실제 매출/수주/승인으로 이어진 경우와, HLB·에코프로비엠·엘앤에프·두산로보틱스·카카오처럼 headline은 컸지만 entry 시점의 bridge가 얇았던 경우를 같은 테이블에 올렸다.

핵심 발견은 단순하다. false-positive group은 평균 MFE90도 작지 않았다. 그러나 MAE90과 MAE180은 positive control과 완전히 다른 얼굴을 보였다. 즉 “초반에 오를 수 있다”는 사실은 Stage2를 열어주는 충분조건이 아니다. Stage2는 작은 문이고, 그 문을 지나려면 최소 두 개의 비가격 bridge가 문고리처럼 맞물려 있어야 한다.

## 1. Profile Assumption / Non-Execution Guard

- current default proxy: `e2r_2_2_rolling_calibrated` / prior prompt proxy: `e2r_2_1_stock_web_calibrated`
- 이번 파일은 `stock_agent` 코드를 열거나 patch하지 않는다.
- production scoring은 변경하지 않는다.
- 모든 weight/rule 제안은 `shadow_weight_only=true`다.
- R13은 cross-archetype checkpoint이므로 `large_sector_id=L10_POLICY_EVENT_CROSS_REDTEAM_MISC`만 사용한다.

## 2. No-Repeat / Coverage Selection

No-Repeat Index는 누적 corpus에서 v12 result MD 2081개, representative rows 11200개, C01~C32 전부 80 rows 이상이라고 보고한다. 따라서 이번 실행은 단순 수량 채우기가 아니라 URL/proxy·entry/MFE/MAE 품질과 R13 taxonomy 압축이 목적이다. R13_STAGE2_FALSE_POSITIVE_REVIEW는 이미 411 rows가 있지만 positive controls가 5개로 얇고, false-positive 원인 taxonomy를 정리하라는 지침이 있다.

```text
why_not_C32 = previous output already used C32 governance/tender cap
why_R13_now = after C01~C32 sweep, cross-scope Stage2 false-positive taxonomy repair is the natural next checkpoint
hard_duplicate_policy = avoid same canonical + symbol + trigger_type + entry_date + evidence family where visible
new_independent_case_count = 5
reused_positive_control_count = 3
positive_case_count = 3
counterexample_count = 5
stage4b_case_count = 5
stage4c_case_count = 3
```

## 3. Price Source Validation

```jsonl
{"row_type":"price_source_validation","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","price_source":"Songdaiki/stock-web","source_basis":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","symbol_count":5414,"tradable_row_count":14354401,"forward_window_rule":"entry_date_through_N_tradable_rows_max_high_min_low","manifest_checked":true,"schema_checked":true}
```

Stock-Web 기준은 `tradable_raw`, `raw_unadjusted_marcap`, `atlas/ohlcv_tradable_by_symbol_year`다. 각 trigger의 entry는 evidence timing이 장마감 후/불명확이면 다음 tradable close, listing-day case는 same-day close로 잡았다. 30D/90D/180D MFE·MAE는 entry close 대비 forward N trading rows의 high/low로 계산했다.

## 4. Compression Map

| source archetype family | R13 false-positive taxonomy | decision use |
|---|---|---|
| C18/C20 export/sell-through | positive control: current earnings bridge | accept comparator |
| C02 grid/backlog | positive control: order/backlog/earnings bridge | accept comparator |
| C23 approval/commercialization | positive control: regulatory approval, commercialization still staged | accept comparator |
| C23/C24 PDUFA expectation | event expectation without final regulatory clearance | Stage2 false positive / 4C after outcome |
| C11/C12 long-dated battery contracts | contract size without current utilization/margin/call-off bridge | Stage2 false positive / 4B-4C watch |
| IPO/robotics price-only | listing scarcity and price move without revenue/margin bridge | Stage4B price-only block |
| C26/C32 platform/governance | one-quarter OP rebound with unresolved trust/legal overhang | Stage2 false positive / 4C watch |

## 5. Case Grid

| case_id | ticker | korean | trigger_date | entry_date | entry_price | trigger_type | canonical_source_scope | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13SFP_003230_SAMYANG_EXPORT_OP_BRIDGE_CONTROL | 003230 | 삼양식품 | 2024-05-16 | 2024-05-17 | 446500.00 | Stage3-Green | C18/C20 | 60.81 | 0.00 | 60.81 | 0.00 | 97.54 | 0.00 | current_profile_should_accept |
| R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL | 267260 | HD현대일렉트릭 | 2025-04-22 | 2025-04-23 | 297500.00 | Stage3-Green | C02 | 45.55 | -2.02 | 74.79 | -2.02 | 228.07 | -2.02 | current_profile_should_accept |
| R13SFP_000100_YUHAN_FDA_APPROVAL_CONTROL | 000100 | 유한양행 | 2024-08-20 | 2024-08-21 | 94300.00 | Stage3-Yellow | C23 | 69.99 | -2.97 | 76.99 | -2.97 | 76.99 | -2.97 | current_profile_should_accept_but_green_waits_for_commercialization |
| R13SFP_028300_HLB_PDUFA_EXPECTATION_FALSE_POSITIVE | 028300 | HLB | 2024-04-09 | 2024-04-11 | 90500.00 | Stage2-Actionable | C23/C24 | 26.30 | -50.11 | 26.30 | -50.11 | 26.30 | -50.11 | current_profile_false_positive_if_pdufa_event_overweighted |
| R13SFP_247540_ECOPROBM_LONG_DATED_CONTRACT_FALSE_POSITIVE | 247540 | 에코프로비엠 | 2023-12-01 | 2023-12-04 | 323000.00 | Stage2-Actionable | C11/C12/C14 | 9.60 | -17.96 | 9.60 | -34.67 | 9.60 | -49.23 | current_profile_false_positive_if_contract_size_overweighted |
| R13SFP_066970_LNF_TESLA_CATHODE_HIGH_MAE_FALSE_POSITIVE | 066970 | 엘앤에프 | 2023-02-28 | 2023-03-02 | 250500.00 | Stage2-Actionable | C11/C12 | 39.52 | -12.57 | 39.52 | -12.57 | 39.52 | -48.94 | current_profile_too_early_without_calloff_margin_gate |
| R13SFP_454910_DOOSAN_ROBOTICS_IPO_PRICE_ONLY_FALSE_POSITIVE | 454910 | 두산로보틱스 | 2023-10-05 | 2023-10-05 | 51400.00 | Stage4B | R13/advanced_equipment_proxy | 31.52 | -37.45 | 142.22 | -37.45 | 142.22 | -37.45 | current_profile_false_positive_if_price_only_stage2_allowed |
| R13SFP_035720_KAKAO_OP_REBOUND_LEGAL_TRUST_FALSE_POSITIVE | 035720 | 카카오 | 2024-05-09 | 2024-05-10 | 47800.00 | Stage2-Actionable | C26/C32 | 2.62 | -14.23 | 2.62 | -31.17 | 2.62 | -31.90 | current_profile_false_positive_if_op_rebound_overweighted |

## 6. Positive vs False-Positive Balance

| bucket | count | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | reading |
|---|---:|---:|---:|---:|---:|---|
| positive controls | 3 | 70.86 | -1.66 | 134.20 | -1.66 | strong bridge survived drawdown |
| false-positive candidates | 5 | 44.05 | -33.19 | 44.05 | -43.53 | upside headline existed, but bridge quality failed |

Interpretation: false-positive cases often produced tradable MFE, so the fix is not “kill all event Stage2.” The fix is to delay `Stage2-Actionable` until bridge purity is visible. The profile should let a weak headline remain watchable, but it should not award the same Actionable status as direct order/backlog/earnings/approval evidence.

## 7. Case Notes

### R13SFP_003230_SAMYANG_EXPORT_OP_BRIDGE_CONTROL — 삼양식품 (003230)

- trigger / entry: `2024-05-16` → `2024-05-17` at `446500.00`
- evidence: Q1 2024 record operating profit and overseas growth; Buldak export/sell-through turned theme into current earnings.
- source: https://www.yna.co.kr/view/AKR20240516147700030
- price path: MFE90 `60.81%`, MAE90 `0.00%`, MFE180 `97.54%`, MAE180 `0.00%`.
- R13 reading: `current_profile_should_accept`; bridge = `strong_two_plus_bridge`.

### R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL — HD현대일렉트릭 (267260)

- trigger / entry: `2025-04-22` → `2025-04-23` at `297500.00`
- evidence: Q1 2025 order/backlog and operating profit bridge; power transformer/grid demand translated into backlog and earnings.
- source: https://en.yna.co.kr/view/AEN20250422006151320
- price path: MFE90 `74.79%`, MAE90 `-2.02%`, MFE180 `228.07%`, MAE180 `-2.02%`.
- R13 reading: `current_profile_should_accept`; bridge = `strong_two_plus_bridge`.

### R13SFP_000100_YUHAN_FDA_APPROVAL_CONTROL — 유한양행 (000100)

- trigger / entry: `2024-08-20` → `2024-08-21` at `94300.00`
- evidence: FDA approved lazertinib plus amivantamab for EGFR-mutated NSCLC; listed-company economics still need royalty/commercial follow-through, so Yellow control rather than automatic Green.
- source: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer
- price path: MFE90 `76.99%`, MAE90 `-2.97%`, MFE180 `76.99%`, MAE180 `-2.97%`.
- R13 reading: `current_profile_should_accept_but_green_waits_for_commercialization`; bridge = `strong_regulatory_bridge_partial_commercial_bridge`.

### R13SFP_028300_HLB_PDUFA_EXPECTATION_FALSE_POSITIVE — HLB (028300)

- trigger / entry: `2024-04-09` → `2024-04-11` at `90500.00`
- evidence: Pre-PDUFA approval-expectation event had survival-data narrative but no final FDA approval or GMP/BIMO clearance at entry; later CRL falsified the Stage2 bridge.
- source: https://www.cancertherapyadvisor.com/news/oncology-drug-approval-decisions-may-2024/
- secondary: https://www.koreatimes.co.kr/business/companies/20240517/south-korean-drugmaker-hlb-hit-by-us-fdas-rejection-of-rivoceranib-liver-cancer-drug
- price path: MFE90 `26.30%`, MAE90 `-50.11%`, MFE180 `26.30%`, MAE180 `-50.11%`.
- R13 reading: `current_profile_false_positive_if_pdufa_event_overweighted`; bridge = `headline_event_weak_quality_bridge`.

### R13SFP_247540_ECOPROBM_LONG_DATED_CONTRACT_FALSE_POSITIVE — 에코프로비엠 (247540)

- trigger / entry: `2023-12-01` → `2023-12-04` at `323000.00`
- evidence: Large Samsung SDI cathode contract was real, but long-dated supply headline lacked current utilization/margin/call-off protection; forward path suffered large MAE.
- source: https://www.asiae.co.kr/en/article/2023120409265042282
- secondary: https://chargedevs.com/newswire/ecopro-wins-5-year-high-nickel-nca-cathode-material-supply-contract-with-samsung-sdi/
- price path: MFE90 `9.60%`, MAE90 `-34.67%`, MFE180 `9.60%`, MAE180 `-49.23%`.
- R13 reading: `current_profile_false_positive_if_contract_size_overweighted`; bridge = `contract_size_strong_current_conversion_weak`.

### R13SFP_066970_LNF_TESLA_CATHODE_HIGH_MAE_FALSE_POSITIVE — 엘앤에프 (066970)

- trigger / entry: `2023-02-28` → `2023-03-02` at `250500.00`
- evidence: Tesla high-nickel cathode order created early MFE, but current margin/utilization/call-off durability was not proven and 180D MAE became severe.
- source: https://batteryindustry.net/tesla-signs-2-year-2-9b-order-with-south-koreas-lf-for-high-nickel-cathode-materials/
- price path: MFE90 `39.52%`, MAE90 `-12.57%`, MFE180 `39.52%`, MAE180 `-48.94%`.
- R13 reading: `current_profile_too_early_without_calloff_margin_gate`; bridge = `customer_contract_strong_margin_bridge_weak`.

### R13SFP_454910_DOOSAN_ROBOTICS_IPO_PRICE_ONLY_FALSE_POSITIVE — 두산로보틱스 (454910)

- trigger / entry: `2023-10-05` → `2023-10-05` at `51400.00`
- evidence: Listing-day robotics scarcity/IPO demand produced a large price move but no contemporaneous order/revenue/margin bridge; Stage2 should be blocked by price-only guard.
- source: https://www.doosanrobotics.com/en/about/promotion/news/view/64
- secondary: https://koreajoongangdaily.joins.com/news/2023-10-05/business/industry/Doosan-Robotics-shares-double-in-trading-debut/1883974
- price path: MFE90 `142.22%`, MAE90 `-37.45%`, MFE180 `142.22%`, MAE180 `-37.45%`.
- R13 reading: `current_profile_false_positive_if_price_only_stage2_allowed`; bridge = `price_event_strong_fundamental_bridge_absent`.

### R13SFP_035720_KAKAO_OP_REBOUND_LEGAL_TRUST_FALSE_POSITIVE — 카카오 (035720)

- trigger / entry: `2024-05-09` → `2024-05-10` at `47800.00`
- evidence: Q1 2024 OP rebound was real, but platform/user monetization bridge was shallow and governance/legal overhang later dominated; Stage2 should require trust/continuity gate.
- source: https://t1.kakaocdn.net/kakaocorp/admin/ir/results-announcement/5659.pdf
- secondary: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/
- price path: MFE90 `2.62%`, MAE90 `-31.17%`, MFE180 `2.62%`, MAE180 `-31.90%`.
- R13 reading: `current_profile_false_positive_if_op_rebound_overweighted`; bridge = `one_quarter_op_rebound_weak_trust_bridge`.

## 8. Stage2 False-Positive Taxonomy

| taxonomy | example cases | failure mechanism | proposed guard |
|---|---|---|---|
| regulatory-calendar expectation | HLB | PDUFA expectation was treated like de-risked approval before final FDA/GMP/BIMO clearance | require final approval or explicit regulatory-quality clearance before Stage2-Actionable |
| long-dated contract size | EcoPro BM, L&F | contract not matched with current utilization, margin, inventory/call-off durability | require current-year shipment/margin/utilization bridge |
| price-only listing/scarcity | Doosan Robotics | IPO and scarcity price action lacked order/revenue/margin conversion | block positive Stage2; use Stage4B/watch until fundamentals appear |
| one-quarter rebound with trust overhang | Kakao | OP rebound existed but governance/legal trust destroyed visibility | require trust/continuity gate for platform/governance overhang cases |
| true bridge controls | Samyang, HD Hyundai Electric, Yuhan | non-price bridge existed before or at trigger | preserve Stage2/Yellow/Green path |

## 9. 4B Local vs Full-Window Audit

| case_id | local/price 4B? | full 4B? | 4C evidence? | audit note |
|---|---|---|---|---|
| R13SFP_003230_SAMYANG_EXPORT_OP_BRIDGE_CONTROL | false | false | false | post-peak DD180 `-8.96`; bridge `strong_two_plus_bridge` |
| R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL | false | false | false | post-peak DD180 `-24.59`; bridge `strong_two_plus_bridge` |
| R13SFP_000100_YUHAN_FDA_APPROVAL_CONTROL | false | false | false | post-peak DD180 `-39.84`; bridge `strong_regulatory_bridge_partial_commercial_bridge` |
| R13SFP_028300_HLB_PDUFA_EXPECTATION_FALSE_POSITIVE | true | true | true | post-peak DD180 `-60.5`; bridge `headline_event_weak_quality_bridge` |
| R13SFP_247540_ECOPROBM_LONG_DATED_CONTRACT_FALSE_POSITIVE | true | true | true | post-peak DD180 `-53.67`; bridge `contract_size_strong_current_conversion_weak` |
| R13SFP_066970_LNF_TESLA_CATHODE_HIGH_MAE_FALSE_POSITIVE | true | true | false | post-peak DD180 `-63.4`; bridge `customer_contract_strong_margin_bridge_weak` |
| R13SFP_454910_DOOSAN_ROBOTICS_IPO_PRICE_ONLY_FALSE_POSITIVE | true | true | false | post-peak DD180 `-45.94`; bridge `price_event_strong_fundamental_bridge_absent` |
| R13SFP_035720_KAKAO_OP_REBOUND_LEGAL_TRUST_FALSE_POSITIVE | true | true | true | post-peak DD180 `-33.64`; bridge `one_quarter_op_rebound_weak_trust_bridge` |

## 10. Current Profile Stress Test

The current calibrated profile already has global guards: Stage2 bridge requirement, price-only blowoff block, full 4B non-price evidence, and hard 4C routing. This R13 file does not ask to loosen Green. It narrows a residual issue: event or headline cases can still look Actionable if visibility is inferred from story heat rather than from verified non-price bridge families.

| profile variant | accepted positives | accepted false positives | false-positive rate among accepted | missed positives | reading |
|---|---:|---:|---:|---:|---|
| current_e2r_2_2_proxy | 3 | 4 | 57% | 0 | still too permissive when headline/event evidence is over-weighted |
| shadow_bridge_purity_gate | 3 | 1 | 25% | 0 | preserves controls; caps weak bridge cases to watch/4B/4C |
| overly_hard_event_block | 2 | 0 | 0% | 1 | too strict; would under-credit Yuhan-style true regulatory bridge |

## 11. Score Simulation Rows

```jsonl
{"row_type":"score_simulation","case_id":"R13SFP_003230_SAMYANG_EXPORT_OP_BRIDGE_CONTROL","profile":"current_e2r_2_2_proxy","symbol":"003230","trigger_type":"Stage3-Green","total_score_before_shadow_gate":90,"stage_before_shadow_gate":"Stage3-Green","total_score_after_shadow_gate":91,"stage_after_shadow_gate":"Stage3-Green","raw_component_score_breakdown_before":{"EPS":20,"Visibility":24,"Bottleneck":12,"Mispricing":12,"Valuation":10,"Capital":6,"Info":6},"shadow_gate_adjustment":{"headline_or_price_event_penalty":0,"missing_two_bridge_penalty":0,"trust_or_regulatory_quality_penalty":0,"positive_control_credit":2},"shadow_axis":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","outcome_MFE90_pct":60.81,"outcome_MAE90_pct":0.0}
{"row_type":"score_simulation","case_id":"R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL","profile":"current_e2r_2_2_proxy","symbol":"267260","trigger_type":"Stage3-Green","total_score_before_shadow_gate":91,"stage_before_shadow_gate":"Stage3-Green","total_score_after_shadow_gate":92,"stage_after_shadow_gate":"Stage3-Green","raw_component_score_breakdown_before":{"EPS":20,"Visibility":24,"Bottleneck":12,"Mispricing":12,"Valuation":10,"Capital":6,"Info":6},"shadow_gate_adjustment":{"headline_or_price_event_penalty":0,"missing_two_bridge_penalty":0,"trust_or_regulatory_quality_penalty":0,"positive_control_credit":2},"shadow_axis":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","outcome_MFE90_pct":74.79,"outcome_MAE90_pct":-2.02}
{"row_type":"score_simulation","case_id":"R13SFP_000100_YUHAN_FDA_APPROVAL_CONTROL","profile":"current_e2r_2_2_proxy","symbol":"000100","trigger_type":"Stage3-Yellow","total_score_before_shadow_gate":82,"stage_before_shadow_gate":"Stage3-Yellow","total_score_after_shadow_gate":80,"stage_after_shadow_gate":"Stage3-Yellow","raw_component_score_breakdown_before":{"EPS":20,"Visibility":24,"Bottleneck":12,"Mispricing":12,"Valuation":10,"Capital":6,"Info":6},"shadow_gate_adjustment":{"headline_or_price_event_penalty":0,"missing_two_bridge_penalty":0,"trust_or_regulatory_quality_penalty":0,"positive_control_credit":2},"shadow_axis":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","outcome_MFE90_pct":76.99,"outcome_MAE90_pct":-2.97}
{"row_type":"score_simulation","case_id":"R13SFP_028300_HLB_PDUFA_EXPECTATION_FALSE_POSITIVE","profile":"current_e2r_2_2_proxy","symbol":"028300","trigger_type":"Stage2-Actionable","total_score_before_shadow_gate":78,"stage_before_shadow_gate":"Stage3-Yellow","total_score_after_shadow_gate":55,"stage_after_shadow_gate":"Stage4C","raw_component_score_breakdown_before":{"EPS":14,"Visibility":14,"Bottleneck":8,"Mispricing":12,"Valuation":10,"Capital":6,"Info":14},"shadow_gate_adjustment":{"headline_or_price_event_penalty":-8,"missing_two_bridge_penalty":-7,"trust_or_regulatory_quality_penalty":-7,"positive_control_credit":0},"shadow_axis":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","outcome_MFE90_pct":26.3,"outcome_MAE90_pct":-50.11}
{"row_type":"score_simulation","case_id":"R13SFP_247540_ECOPROBM_LONG_DATED_CONTRACT_FALSE_POSITIVE","profile":"current_e2r_2_2_proxy","symbol":"247540","trigger_type":"Stage2-Actionable","total_score_before_shadow_gate":77,"stage_before_shadow_gate":"Stage3-Yellow","total_score_after_shadow_gate":57,"stage_after_shadow_gate":"Stage4C","raw_component_score_breakdown_before":{"EPS":14,"Visibility":14,"Bottleneck":8,"Mispricing":12,"Valuation":10,"Capital":6,"Info":14},"shadow_gate_adjustment":{"headline_or_price_event_penalty":-8,"missing_two_bridge_penalty":-7,"trust_or_regulatory_quality_penalty":-7,"positive_control_credit":0},"shadow_axis":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","outcome_MFE90_pct":9.6,"outcome_MAE90_pct":-34.67}
{"row_type":"score_simulation","case_id":"R13SFP_066970_LNF_TESLA_CATHODE_HIGH_MAE_FALSE_POSITIVE","profile":"current_e2r_2_2_proxy","symbol":"066970","trigger_type":"Stage2-Actionable","total_score_before_shadow_gate":78,"stage_before_shadow_gate":"Stage3-Yellow","total_score_after_shadow_gate":62,"stage_after_shadow_gate":"Stage4B","raw_component_score_breakdown_before":{"EPS":14,"Visibility":14,"Bottleneck":8,"Mispricing":12,"Valuation":10,"Capital":6,"Info":14},"shadow_gate_adjustment":{"headline_or_price_event_penalty":-8,"missing_two_bridge_penalty":-7,"trust_or_regulatory_quality_penalty":-3,"positive_control_credit":0},"shadow_axis":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","outcome_MFE90_pct":39.52,"outcome_MAE90_pct":-12.57}
{"row_type":"score_simulation","case_id":"R13SFP_454910_DOOSAN_ROBOTICS_IPO_PRICE_ONLY_FALSE_POSITIVE","profile":"current_e2r_2_2_proxy","symbol":"454910","trigger_type":"Stage4B","total_score_before_shadow_gate":73,"stage_before_shadow_gate":"Stage2","total_score_after_shadow_gate":50,"stage_after_shadow_gate":"Stage4B","raw_component_score_breakdown_before":{"EPS":14,"Visibility":14,"Bottleneck":8,"Mispricing":12,"Valuation":10,"Capital":6,"Info":14},"shadow_gate_adjustment":{"headline_or_price_event_penalty":-8,"missing_two_bridge_penalty":-7,"trust_or_regulatory_quality_penalty":-3,"positive_control_credit":0},"shadow_axis":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","outcome_MFE90_pct":142.22,"outcome_MAE90_pct":-37.45}
{"row_type":"score_simulation","case_id":"R13SFP_035720_KAKAO_OP_REBOUND_LEGAL_TRUST_FALSE_POSITIVE","profile":"current_e2r_2_2_proxy","symbol":"035720","trigger_type":"Stage2-Actionable","total_score_before_shadow_gate":76,"stage_before_shadow_gate":"Stage3-Yellow","total_score_after_shadow_gate":56,"stage_after_shadow_gate":"Stage4C","raw_component_score_breakdown_before":{"EPS":14,"Visibility":14,"Bottleneck":8,"Mispricing":12,"Valuation":10,"Capital":6,"Info":14},"shadow_gate_adjustment":{"headline_or_price_event_penalty":-8,"missing_two_bridge_penalty":-7,"trust_or_regulatory_quality_penalty":-7,"positive_control_credit":0},"shadow_axis":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","outcome_MFE90_pct":2.62,"outcome_MAE90_pct":-31.17}
```

## 12. Rule Candidate

```text
new_axis_proposed = R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE
rule_candidate = For Stage2-Actionable in cross-archetype event/headline cases, require at least two independent non-price bridge families before assigning Actionable status. One family may be event/regulatory/contract; the second must be current revenue/order/backlog/margin/commercialization/trust-quality bridge. If the second family is absent, cap at Stage2 watch or Stage4B depending on price location. If later hard thesis break appears, route to Stage4C.
existing_axis_strengthened = stage2_required_bridge; price_only_blowoff_blocks_positive_stage; local_4b_watch_guard; hard_4c_confirmation; information_confidence_gate
existing_axis_weakened = null
production_scoring_changed = false
shadow_weight_only = true
```

Why this is sector-agnostic: the same false-positive skeleton appears in biotech PDUFA dates, battery mega-contracts, robotics IPO scarcity, and platform OP rebounds. The costume changes by sector, but the bone is identical: a narrative bridge is being confused with a cash or regulatory bridge.

## 13. Before / After Weight Sketch

| profile | EPS | Vis | Bott | Mis | Val | Cap | Info | note |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| before R13 stage2 false-positive scope | 10 | 14 | 8 | 12 | 10 | 6 | 40 | current R13 false-positive review weight seed |
| after shadow gate | 8 | 18 | 7 | 10 | 8 | 6 | 43 | more weight on visibility/information confidence; less on price/story attractiveness |
| delta | -2 | +4 | -1 | -2 | -2 | 0 | +3 | shadow-only, not production patch |

## 14. Residual Contribution Rows

```jsonl
{"row_type":"residual_contribution","case_id":"R13SFP_003230_SAMYANG_EXPORT_OP_BRIDGE_CONTROL","symbol":"003230","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_type":"positive_control","residual_axis":"bridge_purity_vs_headline_event","error_severity":"none","rule_candidate":"require_two_non_price_bridge_families_before_stage2_actionable_for_headline_event_or_price_only_cases","usable_for_shadow_weight":true,"usable_for_production_patch_now":false}
{"row_type":"residual_contribution","case_id":"R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL","symbol":"267260","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_type":"positive_control","residual_axis":"bridge_purity_vs_headline_event","error_severity":"none","rule_candidate":"require_two_non_price_bridge_families_before_stage2_actionable_for_headline_event_or_price_only_cases","usable_for_shadow_weight":true,"usable_for_production_patch_now":false}
{"row_type":"residual_contribution","case_id":"R13SFP_000100_YUHAN_FDA_APPROVAL_CONTROL","symbol":"000100","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_type":"positive_control","residual_axis":"bridge_purity_vs_headline_event","error_severity":"none","rule_candidate":"require_two_non_price_bridge_families_before_stage2_actionable_for_headline_event_or_price_only_cases","usable_for_shadow_weight":true,"usable_for_production_patch_now":false}
{"row_type":"residual_contribution","case_id":"R13SFP_028300_HLB_PDUFA_EXPECTATION_FALSE_POSITIVE","symbol":"028300","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_type":"stage2_false_positive","residual_axis":"bridge_purity_vs_headline_event","error_severity":"high","rule_candidate":"require_two_non_price_bridge_families_before_stage2_actionable_for_headline_event_or_price_only_cases","usable_for_shadow_weight":true,"usable_for_production_patch_now":false}
{"row_type":"residual_contribution","case_id":"R13SFP_247540_ECOPROBM_LONG_DATED_CONTRACT_FALSE_POSITIVE","symbol":"247540","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_type":"stage2_false_positive","residual_axis":"bridge_purity_vs_headline_event","error_severity":"high","rule_candidate":"require_two_non_price_bridge_families_before_stage2_actionable_for_headline_event_or_price_only_cases","usable_for_shadow_weight":true,"usable_for_production_patch_now":false}
{"row_type":"residual_contribution","case_id":"R13SFP_066970_LNF_TESLA_CATHODE_HIGH_MAE_FALSE_POSITIVE","symbol":"066970","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_type":"stage2_false_positive","residual_axis":"bridge_purity_vs_headline_event","error_severity":"medium","rule_candidate":"require_two_non_price_bridge_families_before_stage2_actionable_for_headline_event_or_price_only_cases","usable_for_shadow_weight":true,"usable_for_production_patch_now":false}
{"row_type":"residual_contribution","case_id":"R13SFP_454910_DOOSAN_ROBOTICS_IPO_PRICE_ONLY_FALSE_POSITIVE","symbol":"454910","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_type":"stage2_false_positive","residual_axis":"bridge_purity_vs_headline_event","error_severity":"high","rule_candidate":"require_two_non_price_bridge_families_before_stage2_actionable_for_headline_event_or_price_only_cases","usable_for_shadow_weight":true,"usable_for_production_patch_now":false}
{"row_type":"residual_contribution","case_id":"R13SFP_035720_KAKAO_OP_REBOUND_LEGAL_TRUST_FALSE_POSITIVE","symbol":"035720","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_type":"stage2_false_positive","residual_axis":"bridge_purity_vs_headline_event","error_severity":"high","rule_candidate":"require_two_non_price_bridge_families_before_stage2_actionable_for_headline_event_or_price_only_cases","usable_for_shadow_weight":true,"usable_for_production_patch_now":false}
```

## 15. Case Rows

```jsonl
{"row_type":"case","case_id":"R13SFP_003230_SAMYANG_EXPORT_OP_BRIDGE_CONTROL","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"003230","company_name":"삼양식품","market":"KOSPI/KOSDAQ","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":446500.0,"trigger_family":"consumer_export_sellthrough_profit_bridge_positive_control","evidence_family":"export_channel_reorder_sellthrough_profit_bridge","case_role":"positive_control","is_new_independent_case":false,"reuse_reason":"positive_control_reused_as_R13_holdout_comparator","independent_evidence_weight":0.35,"do_not_count_as_new_case":true,"source_url":"https://www.yna.co.kr/view/AKR20240516147700030","secondary_url":null,"source_proxy_only":false,"evidence_url_pending":false,"calibration_usable":true}
{"row_type":"case","case_id":"R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"267260","company_name":"HD현대일렉트릭","market":"KOSPI/KOSDAQ","trigger_date":"2025-04-22","entry_date":"2025-04-23","entry_price":297500.0,"trigger_family":"grid_order_backlog_earnings_bridge_positive_control","evidence_family":"grid_datacenter_order_backlog_margin_bridge","case_role":"positive_control","is_new_independent_case":false,"reuse_reason":"positive_control_reused_as_R13_holdout_comparator","independent_evidence_weight":0.35,"do_not_count_as_new_case":true,"source_url":"https://en.yna.co.kr/view/AEN20250422006151320","secondary_url":null,"source_proxy_only":false,"evidence_url_pending":false,"calibration_usable":true}
{"row_type":"case","case_id":"R13SFP_000100_YUHAN_FDA_APPROVAL_CONTROL","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"000100","company_name":"유한양행","market":"KOSPI/KOSDAQ","trigger_date":"2024-08-20","entry_date":"2024-08-21","entry_price":94300.0,"trigger_family":"bio_approval_commercialization_positive_control","evidence_family":"fda_approval_to_partner_commercialization_bridge","case_role":"positive_control","is_new_independent_case":false,"reuse_reason":"positive_control_reused_as_R13_holdout_comparator","independent_evidence_weight":0.35,"do_not_count_as_new_case":true,"source_url":"https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer","secondary_url":null,"source_proxy_only":false,"evidence_url_pending":false,"calibration_usable":true}
{"row_type":"case","case_id":"R13SFP_028300_HLB_PDUFA_EXPECTATION_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"028300","company_name":"HLB","market":"KOSPI/KOSDAQ","trigger_date":"2024-04-09","entry_date":"2024-04-11","entry_price":90500.0,"trigger_family":"bio_pdufa_event_expectation_false_positive","evidence_family":"pdufa_expectation_without_regulatory_quality_clearance","case_role":"false_positive_or_guardrail_case","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_url":"https://www.cancertherapyadvisor.com/news/oncology-drug-approval-decisions-may-2024/","secondary_url":"https://www.koreatimes.co.kr/business/companies/20240517/south-korean-drugmaker-hlb-hit-by-us-fdas-rejection-of-rivoceranib-liver-cancer-drug","source_proxy_only":true,"evidence_url_pending":false,"calibration_usable":true}
{"row_type":"case","case_id":"R13SFP_247540_ECOPROBM_LONG_DATED_CONTRACT_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"247540","company_name":"에코프로비엠","market":"KOSPI/KOSDAQ","trigger_date":"2023-12-01","entry_date":"2023-12-04","entry_price":323000.0,"trigger_family":"battery_orderbook_long_dated_false_positive","evidence_family":"long_dated_orderbook_without_current_utilization_margin_bridge","case_role":"false_positive_or_guardrail_case","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_url":"https://www.asiae.co.kr/en/article/2023120409265042282","secondary_url":"https://chargedevs.com/newswire/ecopro-wins-5-year-high-nickel-nca-cathode-material-supply-contract-with-samsung-sdi/","source_proxy_only":true,"evidence_url_pending":false,"calibration_usable":true}
{"row_type":"case","case_id":"R13SFP_066970_LNF_TESLA_CATHODE_HIGH_MAE_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"066970","company_name":"엘앤에프","market":"KOSPI/KOSDAQ","trigger_date":"2023-02-28","entry_date":"2023-03-02","entry_price":250500.0,"trigger_family":"battery_customer_contract_high_mfe_high_mae_false_positive","evidence_family":"customer_contract_headline_calloff_and_margin_risk","case_role":"false_positive_or_guardrail_case","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_url":"https://batteryindustry.net/tesla-signs-2-year-2-9b-order-with-south-koreas-lf-for-high-nickel-cathode-materials/","secondary_url":null,"source_proxy_only":true,"evidence_url_pending":false,"calibration_usable":true}
{"row_type":"case","case_id":"R13SFP_454910_DOOSAN_ROBOTICS_IPO_PRICE_ONLY_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"454910","company_name":"두산로보틱스","market":"KOSPI/KOSDAQ","trigger_date":"2023-10-05","entry_date":"2023-10-05","entry_price":51400.0,"trigger_family":"ipo_listing_price_only_blowoff_false_positive","evidence_family":"ipo_price_only_theme_without_revenue_margin_bridge","case_role":"false_positive_or_guardrail_case","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_url":"https://www.doosanrobotics.com/en/about/promotion/news/view/64","secondary_url":"https://koreajoongangdaily.joins.com/news/2023-10-05/business/industry/Doosan-Robotics-shares-double-in-trading-debut/1883974","source_proxy_only":false,"evidence_url_pending":false,"calibration_usable":true}
{"row_type":"case","case_id":"R13SFP_035720_KAKAO_OP_REBOUND_LEGAL_TRUST_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"035720","company_name":"카카오","market":"KOSPI/KOSDAQ","trigger_date":"2024-05-09","entry_date":"2024-05-10","entry_price":47800.0,"trigger_family":"platform_op_rebound_governance_false_positive","evidence_family":"one_quarter_platform_op_rebound_with_governance_legal_overhang","case_role":"false_positive_or_guardrail_case","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_url":"https://t1.kakaocdn.net/kakaocorp/admin/ir/results-announcement/5659.pdf","secondary_url":"https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/","source_proxy_only":false,"evidence_url_pending":false,"calibration_usable":true}
```

## 16. Trigger Rows

```jsonl
{"row_type":"trigger","case_id":"R13SFP_003230_SAMYANG_EXPORT_OP_BRIDGE_CONTROL","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"003230","company_name":"삼양식품","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_publication_timing":"after_market_or_unknown_next_tradable_entry","entry_date":"2024-05-17","entry_price":446500.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":60.81,"MFE_90D_pct":60.81,"MFE_180D_pct":97.54,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"peak_30D_date":"2024-06-19","peak_90D_date":"2024-06-19","peak_180D_date":"2025-02-14","trough_30D_date":"2024-05-17","trough_90D_date":"2024-05-17","trough_180D_date":"2024-05-17","post_peak_drawdown_180D_pct":-8.96,"same_entry_group_id":"R13SFP::003230::Stage3-Green::2024-05-17","dedupe_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW::003230::Stage3-Green::2024-05-17::consumer_export_sellthrough_profit_bridge_positive_control","representative_for_aggregate":true,"calibration_usable":true,"corporate_action_window_status":"clean_no_large_close_gap_in_loaded_tradable_window","insufficient_forward_window":false,"source_url":"https://www.yna.co.kr/view/AKR20240516147700030","secondary_url":null,"evidence_url_pending":false,"source_proxy_only":false,"current_profile_verdict":"current_profile_should_accept","current_profile_error":false,"false_positive_taxonomy":null,"bridge_strength":"strong_two_plus_bridge","stage4b_required":false,"stage4c_required":false}
{"row_type":"trigger","case_id":"R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"267260","company_name":"HD현대일렉트릭","trigger_type":"Stage3-Green","trigger_date":"2025-04-22","evidence_publication_timing":"after_market_or_unknown_next_tradable_entry","entry_date":"2025-04-23","entry_price":297500.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":45.55,"MFE_90D_pct":74.79,"MFE_180D_pct":228.07,"MAE_30D_pct":-2.02,"MAE_90D_pct":-2.02,"MAE_180D_pct":-2.02,"peak_30D_date":"2025-06-10","peak_90D_date":"2025-07-01","peak_180D_date":"2025-11-04","trough_30D_date":"2025-04-24","trough_90D_date":"2025-04-24","trough_180D_date":"2025-04-24","post_peak_drawdown_180D_pct":-24.59,"same_entry_group_id":"R13SFP::267260::Stage3-Green::2025-04-23","dedupe_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW::267260::Stage3-Green::2025-04-23::grid_order_backlog_earnings_bridge_positive_control","representative_for_aggregate":true,"calibration_usable":true,"corporate_action_window_status":"clean_no_large_close_gap_in_loaded_tradable_window","insufficient_forward_window":false,"source_url":"https://en.yna.co.kr/view/AEN20250422006151320","secondary_url":null,"evidence_url_pending":false,"source_proxy_only":false,"current_profile_verdict":"current_profile_should_accept","current_profile_error":false,"false_positive_taxonomy":null,"bridge_strength":"strong_two_plus_bridge","stage4b_required":false,"stage4c_required":false}
{"row_type":"trigger","case_id":"R13SFP_000100_YUHAN_FDA_APPROVAL_CONTROL","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"000100","company_name":"유한양행","trigger_type":"Stage3-Yellow","trigger_date":"2024-08-20","evidence_publication_timing":"after_market_or_unknown_next_tradable_entry","entry_date":"2024-08-21","entry_price":94300.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"peak_30D_date":"2024-09-24","peak_90D_date":"2024-10-15","peak_180D_date":"2024-10-15","trough_30D_date":"2024-08-22","trough_90D_date":"2024-08-22","trough_180D_date":"2024-08-22","post_peak_drawdown_180D_pct":-39.84,"same_entry_group_id":"R13SFP::000100::Stage3-Yellow::2024-08-21","dedupe_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW::000100::Stage3-Yellow::2024-08-21::bio_approval_commercialization_positive_control","representative_for_aggregate":true,"calibration_usable":true,"corporate_action_window_status":"clean_no_large_close_gap_in_loaded_tradable_window","insufficient_forward_window":false,"source_url":"https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer","secondary_url":null,"evidence_url_pending":false,"source_proxy_only":false,"current_profile_verdict":"current_profile_should_accept_but_green_waits_for_commercialization","current_profile_error":false,"false_positive_taxonomy":null,"bridge_strength":"strong_regulatory_bridge_partial_commercial_bridge","stage4b_required":false,"stage4c_required":false}
{"row_type":"trigger","case_id":"R13SFP_028300_HLB_PDUFA_EXPECTATION_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"028300","company_name":"HLB","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-09","evidence_publication_timing":"after_market_or_unknown_next_tradable_entry","entry_date":"2024-04-11","entry_price":90500.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":26.3,"MFE_90D_pct":26.3,"MFE_180D_pct":26.3,"MAE_30D_pct":-50.11,"MAE_90D_pct":-50.11,"MAE_180D_pct":-50.11,"peak_30D_date":"2024-04-30","peak_90D_date":"2024-04-30","peak_180D_date":"2024-04-30","trough_30D_date":"2024-05-21","trough_90D_date":"2024-05-21","trough_180D_date":"2024-05-21","post_peak_drawdown_180D_pct":-60.5,"same_entry_group_id":"R13SFP::028300::Stage2-Actionable::2024-04-11","dedupe_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW::028300::Stage2-Actionable::2024-04-11::bio_pdufa_event_expectation_false_positive","representative_for_aggregate":true,"calibration_usable":true,"corporate_action_window_status":"clean_no_large_close_gap_in_loaded_tradable_window","insufficient_forward_window":false,"source_url":"https://www.cancertherapyadvisor.com/news/oncology-drug-approval-decisions-may-2024/","secondary_url":"https://www.koreatimes.co.kr/business/companies/20240517/south-korean-drugmaker-hlb-hit-by-us-fdas-rejection-of-rivoceranib-liver-cancer-drug","evidence_url_pending":false,"source_proxy_only":true,"current_profile_verdict":"current_profile_false_positive_if_pdufa_event_overweighted","current_profile_error":true,"false_positive_taxonomy":"bio_pdufa_event_expectation_false_positive","bridge_strength":"headline_event_weak_quality_bridge","stage4b_required":true,"stage4c_required":true}
{"row_type":"trigger","case_id":"R13SFP_247540_ECOPROBM_LONG_DATED_CONTRACT_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"247540","company_name":"에코프로비엠","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-01","evidence_publication_timing":"after_market_or_unknown_next_tradable_entry","entry_date":"2023-12-04","entry_price":323000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":9.6,"MFE_90D_pct":9.6,"MFE_180D_pct":9.6,"MAE_30D_pct":-17.96,"MAE_90D_pct":-34.67,"MAE_180D_pct":-49.23,"peak_30D_date":"2023-12-04","peak_90D_date":"2023-12-04","peak_180D_date":"2023-12-04","trough_30D_date":"2024-01-04","trough_90D_date":"2024-02-01","trough_180D_date":"2024-08-05","post_peak_drawdown_180D_pct":-53.67,"same_entry_group_id":"R13SFP::247540::Stage2-Actionable::2023-12-04","dedupe_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW::247540::Stage2-Actionable::2023-12-04::battery_orderbook_long_dated_false_positive","representative_for_aggregate":true,"calibration_usable":true,"corporate_action_window_status":"clean_no_large_close_gap_in_loaded_tradable_window","insufficient_forward_window":false,"source_url":"https://www.asiae.co.kr/en/article/2023120409265042282","secondary_url":"https://chargedevs.com/newswire/ecopro-wins-5-year-high-nickel-nca-cathode-material-supply-contract-with-samsung-sdi/","evidence_url_pending":false,"source_proxy_only":true,"current_profile_verdict":"current_profile_false_positive_if_contract_size_overweighted","current_profile_error":true,"false_positive_taxonomy":"battery_orderbook_long_dated_false_positive","bridge_strength":"contract_size_strong_current_conversion_weak","stage4b_required":true,"stage4c_required":true}
{"row_type":"trigger","case_id":"R13SFP_066970_LNF_TESLA_CATHODE_HIGH_MAE_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"066970","company_name":"엘앤에프","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-28","evidence_publication_timing":"after_market_or_unknown_next_tradable_entry","entry_date":"2023-03-02","entry_price":250500.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":39.52,"MFE_90D_pct":39.52,"MFE_180D_pct":39.52,"MAE_30D_pct":-12.57,"MAE_90D_pct":-12.57,"MAE_180D_pct":-48.94,"peak_30D_date":"2023-04-03","peak_90D_date":"2023-04-03","peak_180D_date":"2023-04-03","trough_30D_date":"2023-03-20","trough_90D_date":"2023-03-20","trough_180D_date":"2023-11-01","post_peak_drawdown_180D_pct":-63.4,"same_entry_group_id":"R13SFP::066970::Stage2-Actionable::2023-03-02","dedupe_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW::066970::Stage2-Actionable::2023-03-02::battery_customer_contract_high_mfe_high_mae_false_positive","representative_for_aggregate":true,"calibration_usable":true,"corporate_action_window_status":"clean_no_large_close_gap_in_loaded_tradable_window","insufficient_forward_window":false,"source_url":"https://batteryindustry.net/tesla-signs-2-year-2-9b-order-with-south-koreas-lf-for-high-nickel-cathode-materials/","secondary_url":null,"evidence_url_pending":false,"source_proxy_only":true,"current_profile_verdict":"current_profile_too_early_without_calloff_margin_gate","current_profile_error":true,"false_positive_taxonomy":"battery_customer_contract_high_mfe_high_mae_false_positive","bridge_strength":"customer_contract_strong_margin_bridge_weak","stage4b_required":true,"stage4c_required":false}
{"row_type":"trigger","case_id":"R13SFP_454910_DOOSAN_ROBOTICS_IPO_PRICE_ONLY_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"454910","company_name":"두산로보틱스","trigger_type":"Stage4B","trigger_date":"2023-10-05","evidence_publication_timing":"same_day_listing_entry","entry_date":"2023-10-05","entry_price":51400.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":31.52,"MFE_90D_pct":142.22,"MFE_180D_pct":142.22,"MAE_30D_pct":-37.45,"MAE_90D_pct":-37.45,"MAE_180D_pct":-37.45,"peak_30D_date":"2023-10-05","peak_90D_date":"2023-12-21","peak_180D_date":"2023-12-21","trough_30D_date":"2023-10-27","trough_90D_date":"2023-10-27","trough_180D_date":"2023-10-27","post_peak_drawdown_180D_pct":-45.94,"same_entry_group_id":"R13SFP::454910::Stage4B::2023-10-05","dedupe_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW::454910::Stage4B::2023-10-05::ipo_listing_price_only_blowoff_false_positive","representative_for_aggregate":true,"calibration_usable":true,"corporate_action_window_status":"clean_no_large_close_gap_in_loaded_tradable_window","insufficient_forward_window":false,"source_url":"https://www.doosanrobotics.com/en/about/promotion/news/view/64","secondary_url":"https://koreajoongangdaily.joins.com/news/2023-10-05/business/industry/Doosan-Robotics-shares-double-in-trading-debut/1883974","evidence_url_pending":false,"source_proxy_only":false,"current_profile_verdict":"current_profile_false_positive_if_price_only_stage2_allowed","current_profile_error":true,"false_positive_taxonomy":"ipo_listing_price_only_blowoff_false_positive","bridge_strength":"price_event_strong_fundamental_bridge_absent","stage4b_required":true,"stage4c_required":false}
{"row_type":"trigger","case_id":"R13SFP_035720_KAKAO_OP_REBOUND_LEGAL_TRUST_FALSE_POSITIVE","selected_round":"R13","selected_loop":153,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_SCOPE_STAGE2_BRIDGE_VS_HEADLINE_FALSE_POSITIVE_GATE","symbol":"035720","company_name":"카카오","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-09","evidence_publication_timing":"after_market_or_unknown_next_tradable_entry","entry_date":"2024-05-10","entry_price":47800.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":2.62,"MFE_90D_pct":2.62,"MFE_180D_pct":2.62,"MAE_30D_pct":-14.23,"MAE_90D_pct":-31.17,"MAE_180D_pct":-31.9,"peak_30D_date":"2024-05-10","peak_90D_date":"2024-05-10","peak_180D_date":"2024-05-10","trough_30D_date":"2024-06-25","trough_90D_date":"2024-09-09","trough_180D_date":"2024-11-14","post_peak_drawdown_180D_pct":-33.64,"same_entry_group_id":"R13SFP::035720::Stage2-Actionable::2024-05-10","dedupe_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW::035720::Stage2-Actionable::2024-05-10::platform_op_rebound_governance_false_positive","representative_for_aggregate":true,"calibration_usable":true,"corporate_action_window_status":"clean_no_large_close_gap_in_loaded_tradable_window","insufficient_forward_window":false,"source_url":"https://t1.kakaocdn.net/kakaocorp/admin/ir/results-announcement/5659.pdf","secondary_url":"https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/","evidence_url_pending":false,"source_proxy_only":false,"current_profile_verdict":"current_profile_false_positive_if_op_rebound_overweighted","current_profile_error":true,"false_positive_taxonomy":"platform_op_rebound_governance_false_positive","bridge_strength":"one_quarter_op_rebound_weak_trust_bridge","stage4b_required":true,"stage4c_required":true}
```

## 17. Aggregate / Shadow Rows

```jsonl
{"row_type":"aggregate_summary","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","selected_round":"R13","selected_loop":153,"total_trigger_rows":8,"calibration_usable_trigger_rows":8,"positive_control_count":3,"false_positive_candidate_count":5,"new_independent_case_count":5,"reused_positive_control_count":3,"positive_avg_MFE90":70.86,"positive_avg_MAE90":-1.66,"false_avg_MFE90":44.05,"false_avg_MAE90":-33.19,"positive_avg_MFE180":134.2,"positive_avg_MAE180":-1.66,"false_avg_MFE180":44.05,"false_avg_MAE180":-43.53,"key_observation":"false-positive group had attractive average MFE90 but much worse MAE90/MAE180; Stage2 must distinguish bridge purity from headline heat."}
{"row_type":"shadow_weight","selected_round":"R13","selected_loop":153,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","new_axis_proposed":"R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE","production_scoring_changed":false,"shadow_weight_only":true,"before_weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"10/14/8/12/10/6/40","after_weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"8/18/7/10/8/6/43","delta":"-2/+4/-1/-2/-2/0/+3","rationale":"raise visibility/information-confidence and lower mispricing/valuation weight for Stage2 false-positive review; do not loosen Green."}
```

## 18. Batch Ingest Self-Audit

```text
filename_matches_required_regex = true
metadata_round_matches_filename = true
metadata_loop_matches_filename = true
round_sector_consistency = pass
r13_large_sector_is_L10 = true
trigger_type_canonical_labels_only = true
rows_missing_required_mfe_mae = 0
entry_date_present_all_trigger_rows = true
entry_price_present_all_trigger_rows = true
price_source_valid_all_trigger_rows = true
source_url_pending_count = 0
source_proxy_only_count = 3
calibration_usable_trigger_count = 8
representative_trigger_candidate_count = 8
new_independent_case_count = 5
reused_positive_control_count = 3
positive_case_count = 3
counterexample_count = 5
stage4b_case_count = 5
stage4c_case_count = 3
current_profile_error_count = 5
same_entry_group_dedupe_ready = true
production_scoring_changed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 19. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent. Do not execute this during research ingestion. Read this MD only after multiple v12 residual MDs are collected. Parse JSONL rows with row_type in {price_source_validation, case, trigger, score_simulation, residual_contribution, aggregate_summary, shadow_weight}. Validate canonical_archetype_id=R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, selected_round=R13, large_sector_id=L10_POLICY_EVENT_CROSS_REDTEAM_MISC, and required MFE/MAE fields. Consider a shadow-only rule candidate named R13_STAGE2_BRIDGE_PURITY_AND_OUTCOME_DISCONFIRMATION_GATE. Do not loosen Stage3-Green. If sufficient corroborating R13 rows exist, add or adjust only R13 diagnostic/guardrail profile behavior so that headline/event/price-only Stage2 candidates require at least two independent non-price bridge families before Stage2-Actionable. Preserve true bridge positives such as export earnings bridge, order/backlog/earnings bridge, and approved regulatory/commercialization bridge. Route later-confirmed regulatory/trust/financial thesis breaks to Stage4C. Do not apply production patch unless aggregate support is confirmed across representative rows.
```

## 20. Next Research State

```text
completed_round = R13
completed_loop = 153
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 over-repeat inspection / taxonomy repair — R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
next_recommended_archetypes = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION; R13_CROSS_ARCHETYPE_4B_4C_REDTEAM; C05_EPC_MEGA_CONTRACT_MARGIN_GAP; C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 21. Source Notes

- Prompt basis: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- Duplicate ledger basis: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price basis: `Songdaiki/stock-web`, `atlas/ohlcv_tradable_by_symbol_year`, raw/unadjusted tradable rows.
- Evidence source URLs are embedded in JSONL rows and case notes. Secondary URLs are used only to classify later outcome/disconfirmation, not to pretend that later evidence was known at the original trigger entry.