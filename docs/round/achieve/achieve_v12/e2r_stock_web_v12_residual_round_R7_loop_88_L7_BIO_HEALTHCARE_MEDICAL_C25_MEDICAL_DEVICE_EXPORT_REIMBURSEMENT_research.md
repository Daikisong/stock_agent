# E2R Stock-Web v12 Residual Research — R7 Loop 88 — L7 / C25

```yaml
schema_version: e2r_stock_web_v12_residual_research
scheduled_round: R7
scheduled_loop: 88
completed_round: R7
completed_loop: 88
next_round: R8
next_loop: 88
round_schedule_status: valid
round_sector_consistency: pass

large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DENTAL_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12

primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bridge_stress_test
  - local_4b_watch_guard_stress_test
  - medical_device_export_reimbursement_subarchetype_separation
```

---

## 1. 연구 목적

이번 R7은 `L7_BIO_HEALTHCARE_MEDICAL` 라운드이며, C25의 의료기기/시술형 헬스케어 export·reimbursement·adoption bridge를 점검한다.

C25는 이미 원텍, 클래시스, 아이센스, 덴티움, 큐렉소 등 특정 표본이 많이 쌓여 있기 때문에, 이번 loop에서는 과밀 표본을 피하고 다음 세 가지를 새 표본으로 사용했다.

```text
214450 파마리서치     : aesthetic procedure / regenerative product adoption positive
228670 레이           : dental digital workflow export headline fade counterexample
043150 바텍           : dental imaging export base but no new acceleration counterexample
```

핵심 질문은 단순하다.

```text
의료기기/시술형 헬스케어에서
“수출 회복 / 글로벌 미용의료 관심 / 치과 장비 해외 매출” 헤드라인만으로
Stage2-Actionable을 열 수 있는가?

아니면
반복 시술 수요, distributor reorder, reimbursement/approval visibility,
ASP/mix, margin bridge, EPS revision이 함께 붙어야 하는가?
```

이번 결론은 후자다. C25에서 가격 반응이 빠르게 나오는 경우가 많지만, 실제 rerating으로 남는 것은 “기기/제품이 팔렸다”가 아니라 **병·의원 채택 → 반복 사용 → 소모품/시술 매출 → 마진/EPS로 닫히는 회로**가 확인되는 경우였다.

---

## 2. No-Repeat / Novelty Check

No-Repeat Index 기준 C25의 top covered symbols는 다음과 같이 이미 과밀하다.

```text
336570, 100120, 060280, 099190, 145720, 214150
```

이번 연구는 위 과밀 symbol을 사용하지 않았다.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

이번 사용 key:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT + 214450 + Stage2-Actionable + 2024-08-07
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT + 228670 + Stage2-FalsePositive-Candidate + 2024-03-12
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT + 043150 + Stage2-FalsePositive-Candidate + 2024-04-01
```

이번 세 key는 이전 R7/C25 과밀 조합과 겹치지 않는 useful expansion이다.

```yaml
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 2
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
calibration_usable_case_count: 3
do_not_propose_new_weight_delta: true
```

---

## 3. Stock-Web Price-Atlas Validation

모든 가격 row는 `Songdaiki/stock-web`의 tradable shard에서 확인했다.

| symbol | name | profile path | tradable shard | profile caveat | usable |
|---|---|---|---|---|---|
| 214450 | 파마리서치 | `atlas/symbol_profiles/214/214450.json` | `atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv`, `2025.csv` | corporate_action_candidate_count = 0 | true |
| 228670 | 레이 | `atlas/symbol_profiles/228/228670.json` | `atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv` | old corporate-action candidates in 2021, outside window | true |
| 043150 | 바텍 | `atlas/symbol_profiles/043/043150.json` | `atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv` | old corporate-action candidate in 2010, outside window | true |

`214450` profile confirms no corporate-action candidate dates and stock-web tradable files through 2026.  
`228670` and `043150` have old corporate-action candidates, but none overlap the 2024 trigger windows used here.

---

## 4. Case Grid

### 4.1 Positive case — 214450 파마리서치

```yaml
case_id: R7_L88_C25_214450_2024_08_07_STAGE2_ACTIONABLE
symbol: "214450"
name: 파마리서치
trigger_type: Stage2-Actionable
entry_date: 2024-08-07
entry_price: 166900
evidence_family:
  - aesthetic_regenerative_product_repeat_procedure
  - export_adoption
  - margin_eps_revision_bridge
fine_sub_archetype: AESTHETIC_REGENERATIVE_REPEAT_PROCEDURE_ADOPTION
verdict: positive_with_local_4b_overlay
```

Stock-web row anchor:

```text
2024-08-07,145200,168700,144900,166900,...
2024-09-11,195000,204000,183700,184600,...
2024-09-20,194200,205500,191700,201000,...
2024-12-16,262500,267000,254500,256000,...
2025-03-14,324500,336500,323500,335500,...
2025-04-11,346000,369000,344000,366000,...
```

Interpretation:

파마리서치는 단순 “미용의료 테마”가 아니라 반복 시술형 제품 수요와 ASP/mix, 마진/EPS bridge가 가격경로에 남았다. 2024-08-07 진입 후 30D 안에 20% 이상 MFE가 열렸고, 90D~180D에서도 고점을 계속 확장했다. 다만 2024-12~2025-04 구간은 `local_4b_watch`가 필요한 구간이다. 4B는 thesis break가 아니라 “좋은 thesis가 너무 빨리 가격화된 구간”으로 보는 것이 맞다.

Approximate price-path metrics:

| metric | value |
|---|---:|
| entry_price | 166,900 |
| MFE_30D | +23.1% |
| MAE_30D | -1.0% |
| MFE_90D | +60.0% |
| MAE_90D | -1.0% |
| MFE_180D | +121.1% |
| MAE_180D | -1.0% |
| local_4b_proximity | true |
| full_4b_thesis_break | false |

Raw component sketch:

| component | raw_score | note |
|---|---:|---|
| EPS/FCF Explosion | 15 | repeat procedure and margin leverage visible |
| Earnings Visibility | 16 | demand-to-earnings bridge stronger than generic device beta |
| Bottleneck/Pricing | 15 | branded procedure/product mix |
| Market Mispricing | 10 | rerating persisted after initial move |
| Valuation Rerating | 11 | local 4B needed after 90D/180D extension |
| Capital Allocation | 2 | not the main axis |
| Information Confidence | 4 | source_proxy_pending but price path strong |
| total_raw | 73 | Stage2-Actionable, not automatic Green without fresh evidence |

---

### 4.2 Counterexample — 228670 레이

```yaml
case_id: R7_L88_C25_228670_2024_03_12_STAGE2_FALSE_POSITIVE
symbol: "228670"
name: 레이
trigger_type: Stage2-FalsePositive-Candidate
entry_date: 2024-03-12
entry_price: 16870
evidence_family:
  - dental_digital_workflow_export_headline
  - china_channel_recovery_claim
  - no_margin_reorder_bridge
fine_sub_archetype: DENTAL_DIGITAL_EXPORT_HEADLINE_WITHOUT_REORDER_BRIDGE
verdict: counterexample
```

Stock-web row anchor:

```text
2024-03-12,15740,17040,15620,16870,...
2024-03-18,17300,17650,17180,17520,...
2024-06-26,12320,12900,12240,12640,...
2024-08-05,10340,10400,8860,8860,...
2024-09-10,8000,8040,7600,7670,...
```

Interpretation:

레이는 치과 디지털 장비/워크플로우 수출 회복이라는 서사는 만들 수 있었지만, 실제 경로는 30D 이후 계속 내려앉았다. 장비 업황에서 “수출 회복”이라는 말이 들어와도 병·의원 채택, 채널 재주문, 재고 정상화, margin bridge가 확인되지 않으면 C25 Stage2-Actionable로 올리면 안 된다.

Approximate price-path metrics:

| metric | value |
|---|---:|
| entry_price | 16,870 |
| MFE_30D | +4.8% |
| MAE_30D | -11.5% |
| MFE_90D | +4.8% |
| MAE_90D | -28.6% |
| MFE_180D | +4.8% |
| MAE_180D | -55.0% |
| local_4b_proximity | false |
| full_4b_thesis_break | true |

Raw component sketch:

| component | raw_score | note |
|---|---:|---|
| EPS/FCF Explosion | 4 | no durable earnings bridge |
| Earnings Visibility | 5 | recovery claim not enough |
| Bottleneck/Pricing | 6 | product category has value but channel proof weak |
| Market Mispricing | 4 | drawdown dominated |
| Valuation Rerating | 2 | rerating failed |
| Capital Allocation | 1 | not relevant |
| Information Confidence | 3 | source_proxy_pending |
| total_raw | 25 | false-positive / watch-only |

---

### 4.3 Counterexample — 043150 바텍

```yaml
case_id: R7_L88_C25_043150_2024_04_01_STAGE2_FALSE_POSITIVE
symbol: "043150"
name: 바텍
trigger_type: Stage2-FalsePositive-Candidate
entry_date: 2024-04-01
entry_price: 31300
evidence_family:
  - dental_imaging_export_base
  - no_new_acceleration
  - adoption_reimbursement_bridge_absent
fine_sub_archetype: DENTAL_IMAGING_EXPORT_BASE_WITHOUT_NEW_ACCELERATION
verdict: counterexample
```

Stock-web row anchor:

```text
2024-04-01,30750,31650,30450,31300,...
2024-06-26,26400,27200,26400,26800,...
2024-08-05,25000,25150,23050,23250,...
2024-09-04,23350,23350,22700,22700,...
```

Interpretation:

바텍은 치과 영상장비의 기본 수출 기반을 갖고 있지만, 이번 trigger 형태는 “새로운 acceleration”이 아니라 기존 사업 안정성에 가까웠다. C25에서는 device export base만으로는 Stage2-Actionable이 아니라 Stage1/Watch에 머무르는 것이 맞다. 90D~180D 경로에서 고점 확장이 거의 없고 하방만 열린다.

Approximate price-path metrics:

| metric | value |
|---|---:|
| entry_price | 31,300 |
| MFE_30D | +1.1% |
| MAE_30D | -5.9% |
| MFE_90D | +1.1% |
| MAE_90D | -16.9% |
| MFE_180D | +1.1% |
| MAE_180D | -27.5% |
| local_4b_proximity | false |
| full_4b_thesis_break | true |

Raw component sketch:

| component | raw_score | note |
|---|---:|---|
| EPS/FCF Explosion | 4 | no acceleration proof |
| Earnings Visibility | 7 | stable base, but not rerating-grade |
| Bottleneck/Pricing | 6 | category quality exists |
| Market Mispricing | 3 | no price confirmation |
| Valuation Rerating | 2 | failed expansion |
| Capital Allocation | 1 | not relevant |
| Information Confidence | 3 | source_proxy_pending |
| total_raw | 26 | watch-only / false-positive candidate |

---

## 5. Machine-Readable Trigger Rows

```jsonl
{"schema_version":"e2r_v12_trigger_row","row_type":"trigger","round":"R7","loop":88,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_REGENERATIVE_REPEAT_PROCEDURE_ADOPTION","case_id":"R7_L88_C25_214450_2024_08_07_STAGE2_ACTIONABLE","symbol":"214450","name":"파마리서치","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-07","entry_date":"2024-08-07","entry_price":166900,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":23.1,"mae_30d_pct":-1.0,"mfe_90d_pct":60.0,"mae_90d_pct":-1.0,"mfe_180d_pct":121.1,"mae_180d_pct":-1.0,"peak_price_180d":369000,"max_drawdown_180d_pct":-1.0,"evidence_family":"aesthetic_regenerative_product_repeat_procedure|export_adoption|margin_eps_revision_bridge","positive_case":true,"counterexample":false,"local_4b_proximity":true,"full_4b_thesis_break":false,"calibration_usable":true,"source_proxy_pending":true,"usable_for_new_weight_evidence":false,"do_not_propose_new_weight_delta":true}
{"schema_version":"e2r_v12_trigger_row","row_type":"trigger","round":"R7","loop":88,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DIGITAL_EXPORT_HEADLINE_WITHOUT_REORDER_BRIDGE","case_id":"R7_L88_C25_228670_2024_03_12_STAGE2_FALSE_POSITIVE","symbol":"228670","name":"레이","trigger_type":"Stage2-FalsePositive-Candidate","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":16870,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.8,"mae_30d_pct":-11.5,"mfe_90d_pct":4.8,"mae_90d_pct":-28.6,"mfe_180d_pct":4.8,"mae_180d_pct":-55.0,"peak_price_180d":17680,"max_drawdown_180d_pct":-55.0,"evidence_family":"dental_digital_workflow_export_headline|china_channel_recovery_claim|no_margin_reorder_bridge","positive_case":false,"counterexample":true,"local_4b_proximity":false,"full_4b_thesis_break":true,"calibration_usable":true,"source_proxy_pending":true,"usable_for_new_weight_evidence":false,"do_not_propose_new_weight_delta":true}
{"schema_version":"e2r_v12_trigger_row","row_type":"trigger","round":"R7","loop":88,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMAGING_EXPORT_BASE_WITHOUT_NEW_ACCELERATION","case_id":"R7_L88_C25_043150_2024_04_01_STAGE2_FALSE_POSITIVE","symbol":"043150","name":"바텍","trigger_type":"Stage2-FalsePositive-Candidate","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":31300,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.1,"mae_30d_pct":-5.9,"mfe_90d_pct":1.1,"mae_90d_pct":-16.9,"mfe_180d_pct":1.1,"mae_180d_pct":-27.5,"peak_price_180d":31650,"max_drawdown_180d_pct":-27.5,"evidence_family":"dental_imaging_export_base|no_new_acceleration|adoption_reimbursement_bridge_absent","positive_case":false,"counterexample":true,"local_4b_proximity":false,"full_4b_thesis_break":true,"calibration_usable":true,"source_proxy_pending":true,"usable_for_new_weight_evidence":false,"do_not_propose_new_weight_delta":true}
```

---

## 6. Aggregation Row

```jsonl
{"schema_version":"e2r_v12_aggregate_metric","row_type":"aggregate_metric","round":"R7","loop":88,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DENTAL_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"full_4c_case_count":0,"median_mfe_30d_pct":4.8,"median_mae_30d_pct":-5.9,"median_mfe_90d_pct":4.8,"median_mae_90d_pct":-16.9,"median_mfe_180d_pct":4.8,"median_mae_180d_pct":-27.5,"residual_error_label":"device_export_headline_without_reorder_or_reimbursement_bridge_overpromotes_stage2","suggested_shadow_axis":"require_repeat_adoption_reorder_margin_bridge_before_stage2_actionable","do_not_propose_new_weight_delta":true}
```

---

## 7. Residual Contribution Summary

```yaml
loop_contribution_label: residual_error_found
residual_error_type:
  - stage2_false_positive_from_export_headline
  - medical_device_base_business_without_new_acceleration
  - positive_with_local_4b_watch
new_axis_proposed: null
existing_axis_strengthened:
  - require_non_price_adoption_reorder_or_reimbursement_bridge
  - local_4b_watch_after_fast_90d_mfe
existing_axis_weakened: null
global_weight_delta_recommended: false
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
```

Mechanism summary:

```text
C25 Stage2-Actionable should require:
1. export or reimbursement headline,
2. concrete adoption/reorder evidence,
3. margin/EPS bridge,
4. no obvious inventory/channel stuffing risk.

If only #1 exists:
    keep Stage1/Watch or Stage2-FalsePositive-Candidate.
If #1~#3 exist and price confirms:
    Stage2-Actionable possible.
If 90D~180D MFE expands too fast without new evidence:
    local 4B watch, not hard 4C.
```

---

## 8. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

Later coding agent task:
Parse this R7/L88/C25 MD as v12 research input.
Ingest all jsonl trigger rows and aggregate_metric rows.
Do not treat source_proxy_pending rows as automatic promotion evidence.
Use this file to strengthen C25 medical-device guardrails:
- Stage2-Actionable requires adoption/reorder/reimbursement/margin bridge, not export headline alone.
- Dental imaging/base device business without new acceleration should remain Watch.
- Aesthetic repeat-procedure positive cases may qualify for Stage2-Actionable, but 90D/180D extended MFE should activate local 4B watch.
Do not change production scoring directly from this file alone.
```

---

## 9. Round State

```text
completed_round = R7
completed_loop = 88
next_round = R8
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
