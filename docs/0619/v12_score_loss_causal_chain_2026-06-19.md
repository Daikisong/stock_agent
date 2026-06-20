# V12 Score Loss Causal Chain

이 문서는 '삼전/하닉이 왜 이렇게 낮게 나오나'를 전체 아키타입 문제로 연결해 설명한다.
점수식을 바꾸는 문서가 아니라, 기존 0619 audit들을 합쳐 점수 손실 위치를 한 화면에 고정하는 장부다.

## Summary

- plain_answer: 점수표가 누적 연구를 잊은 것이 아니다. 누적 연구는 weight layer까지 들어갔지만, current pipeline은 candidate/archive, parser-feature bridge, stage gate 중 하나에서 멈춘다.
- research_support_rows: `12471`
- research_positive_cases: `1495`
- research_counterexamples: `2628`
- archetype_weight_count: `36`
- stop_layer_counts: `{'candidate_replay_archive': 29, 'manual_review': 3, 'stage_gate': 4}`
- runtime_gap_status_counts: `{'fixture_not_ready': 3, 'not_in_current_benchmark': 24, 'runtime_input_evidence_missing': 2, 'runtime_stage3_gate_blocked': 4}`
- first_slice_input_gap_counts: `{'archive_or_candidate_funnel_missing': 13, 'exact_candidate_reached_but_readiness_inputs_missing': 1, 'exact_candidate_reached_but_research_snapshot_missing': 1, 'runtime_symbol_reached_but_schedule_date_mismatch': 1, 'selected_manual_row_without_fixture_spec': 3}`
- hbm_generalization_guard: 삼전/하닉은 대표 테스트 케이스다. HBM만 통과시키는 패치는 실패이며, 비-HBM focus rows도 같은 chain에서 통과해야 한다.

## HBM Symbol Chain

| symbol | research HBM/raw Green/positive | positive signals | runtime best | zero/missing bridge fields | gap signals | answer |
| --- | ---: | --- | --- | --- | --- | --- |
| 000660 SK하이닉스 | 159/8/59 | {'capacity_lock': 45, 'direct_hbm': 55, 'lag_or_guard': 8, 'margin_or_mix': 25, 'named_customer': 52, 'order_or_contract': 32, 'revision_or_fcf': 18} | 3-Yellow/80.0131/C06_HBM_MEMORY_CUSTOMER_CAPACITY; bridge m,c,b,k=100.0/100.0/100.0/100.0; deficit=total:80.01/87.00(-6.99); bottleneck:12.18/14.25(-2.07) | contract_quality | none | 하닉은 EPS/revision이 깎인 것이 아니다. runtime best row가 revision, margin, customer/backlog/contract를 강하게 잡은 뒤에도 Green gate가 `total:80.01/87.00(-6.99); bottleneck:12.18/14.25(-2.07)`에서 막힌다. |
| 005930 삼성전자 | 75/0/3 | {'capacity_lock': 3, 'direct_hbm': 3, 'margin_or_mix': 1, 'named_customer': 2, 'order_or_contract': 1} | 2/72.1181/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE; bridge m,c,b,k=100.0/100.0/100.0/0.0; deficit=total:72.12/87.00(-14.88); yellow_total:72.12/75.00(-2.88); bottleneck:8.16/10.50(-2.33); visibility:13.17/13.50(-0.33) | research_axis_bridge_contract, contract_quality | none | 삼성은 누적 HBM 장부에서도 direct C06 Green보다 qualification lag/catch-up 성격이 강하다. runtime은 C10 memory recovery route로 남고 customer/backlog/contract가 0이라 Stage 2와 `total:72.12/87.00(-14.88); yellow_total:72.12/75.00(-2.88); bottleneck:8.16/10.50(-2.33); visibility:13.17/13.50(-0.33)`에 머문다. |

## Focus Archetype Chain

| archetype | research Green clean/raw | weight support/positive/guard | stop layer | runtime | missing axes | first-slice input gaps | plain failure | next fix |
| --- | ---: | ---: | --- | --- | --- | --- | --- | --- |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 5/9 | 229/32/56 | stage_gate | 3-Yellow/80.0131/C06_HBM_MEMORY_CUSTOMER_CAPACITY; bridge m,c,b,k=100.0/100.0/100.0/100.0; deficit=total:80.01/87.00(-6.99); bottleneck:12.18/14.25(-2.07) | none | exact_candidate_reached_but_research_snapshot_missing, runtime_symbol_reached_but_schedule_date_mismatch | source-backed field가 일부 들어왔지만 weighted Stage3-Green 총점/과락 gate에서 막힌다. | source-backed field가 들어온 뒤에도 Green이 막히는지 weighted gate threshold와 component balance를 검증한다. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 4/4 | 366/60/79 | stage_gate | 2/72.1181/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE; bridge m,c,b,k=100.0/100.0/100.0/0.0; deficit=total:72.12/87.00(-14.88); yellow_total:72.12/75.00(-2.88); bottleneck:8.16/10.50(-2.33); visibility:13.17/13.50(-0.33) | none | archive_or_candidate_funnel_missing | source-backed field가 일부 들어왔지만 weighted Stage3-Green 총점/과락 gate에서 막힌다. | source-backed field가 들어온 뒤에도 Green이 막히는지 weighted gate threshold와 component balance를 검증한다. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 23/37 | 413/44/43 | candidate_replay_archive | not scored | capital_return, valuation_repricing, guard_risk | archive_or_candidate_funnel_missing | 연구 Green은 있지만 시험지가 current replay에 없다. 점수가 낮은 게 아니라 아직 채점 자체를 못 했다. | Green/guard fixture를 local official/search/report archive와 exact symbol+date replay 후보로 고정한다. |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 16/30 | 269/27/24 | candidate_replay_archive | not scored | bio_commercialization, guard_risk | archive_or_candidate_funnel_missing | 연구 Green은 있지만 시험지가 current replay에 없다. 점수가 낮은 게 아니라 아직 채점 자체를 못 했다. | Green/guard fixture를 local official/search/report archive와 exact symbol+date replay 후보로 고정한다. |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 11/19 | 334/35/65 | candidate_replay_archive | not scored | software_retention, customer, margin | archive_or_candidate_funnel_missing | 연구 Green은 있지만 시험지가 current replay에 없다. 점수가 낮은 게 아니라 아직 채점 자체를 못 했다. | Green/guard fixture를 local official/search/report archive와 exact symbol+date replay 후보로 고정한다. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 22/33 | 358/42/45 | stage_gate | 1/64.161/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION; bridge m,c,b,k=100.0/100.0/0.0/0.0; deficit=total:64.16/87.00(-22.84); domain_evidence:14.29/35.00(-20.71); yellow_total:64.16/75.00(-10.84); sector_bottleneck:25.50/35.00(-9.50); bottleneck:2.89/9.00(-6.11); visibility:15.06/17.25(-2.19); valuation:7.57/8.67(-1.10); mispricing:10.60/10.67(-0.07) | none | archive_or_candidate_funnel_missing | source-backed field가 일부 들어왔지만 weighted Stage3-Green 총점/과락 gate에서 막힌다. | source-backed field가 들어온 뒤에도 Green이 막히는지 weighted gate threshold와 component balance를 검증한다. |
| C02_POWER_GRID_DATACENTER_CAPEX | 3/5 | 277/50/58 | stage_gate | 2/72.9252/C02_POWER_GRID_DATACENTER_CAPEX; bridge m,c,b,k=100.0/100.0/100.0/100.0; deficit=total:72.93/87.00(-14.07); bottleneck:9.90/15.00(-5.09); contract:41.50/45.00(-3.50); yellow_total:72.93/75.00(-2.07) | none | archive_or_candidate_funnel_missing, exact_candidate_reached_but_readiness_inputs_missing | source-backed field가 일부 들어왔지만 weighted Stage3-Green 총점/과락 gate에서 막힌다. | source-backed field가 들어온 뒤에도 Green이 막히는지 weighted gate threshold와 component balance를 검증한다. |

## Easy Reading

- 하닉 예: 연구에는 HBM sold-out/customer allocation이 있고, weight와 bridge field에도 반영됐다. 이제 남은 것은 total/bottleneck gate 검증이다.
- 삼성 예: 삼성은 같은 C06 direct Green이 아니라 C10 memory recovery/catch-up route로 잡힌다. customer/backlog/contract bridge가 약해 Stage 2에 남는다.
- C01/C19/R13 예: 후보 row는 있지만 원천 입력 가족이 부족하면 parser 실패인지 아직 판정할 수 없다.
- C21/C23/C26 예: 연구 Green은 있지만 current replay 후보가 0개다. 시험지가 없으니 채점표를 아무리 잘 만들어도 점수가 안 나온다.
- C02 예: 후보와 field가 있어도 Green gate 총점/필수축에서 막힐 수 있다. 이 경우에는 threshold/component balance를 positive/guard 쌍으로 검증해야 한다.
- 결론: 점수표 문제 하나가 아니라 `후보 입력`, `field 번역`, `gate 검증` 세 층의 문제다. 하닉/삼전만 좋아지는 패치는 실패다.
