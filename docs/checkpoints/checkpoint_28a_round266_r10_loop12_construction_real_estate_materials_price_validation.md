# Checkpoint 28A Round 266 R10 Loop 12 Construction / Real Estate / Materials Price Validation

## 목적

`docs/round/round_266.md`의 R10 Loop 12 내용을 케이스 라이브러리와 가격 검증 보고서로 구조화했다.

이번 라운드는 **캘리브레이션 전용**이다. 생산 점수, StageClassifier 임계값, 후보 생성 로직은 바꾸지 않았다.

쉬운 예시:

- Czech 원전 preferred bidder는 강한 `Stage 2` 증거다.
- 하지만 final contract, 법적 이슈 해소, 상장사별 scope, margin, 현금회수 전에는 `Stage 3-Green`이 아니다.
- 건설은 "수주했다"보다 "돈을 벌고 현금으로 회수한다"가 닫혀야 한다.

## 반영 범위

- 원본 라운드: `docs/round/round_266.md`
- 분석 라운드 ID: `round_194`
- 대섹터: `CONSTRUCTION_REAL_ESTATE_MATERIALS`
- 가격 검증 상태: `partial_with_reported_price_anchors`
- 전체 조정 OHLC 완성 여부: `false`
- 생산 scoring 변경: `false`
- shadow weight만 기록: `true`
- hard 4C: `true_for_safety_reference`
- direct listed hard 4C: `false`

## 추가한 canonical archetype

이번 라운드에서 다음 archetype을 canonical enum과 정의에 추가했다.

- `NUCLEAR_EPC_EXPORT_STAGE2`
- `NUCLEAR_EXPORT_LEGAL_4C_WATCH`
- `CONSTRUCTION_SAFETY_HARD_REFERENCE`
- `RECURRING_FATAL_ACCIDENT_REGULATORY_4C`
- `HOUSING_SUPPLY_POLICY_EVENT`
- `PUBLIC_INFRASTRUCTURE_POLICY_EVENT`
- `LNG_POWER_INFRA_CONSORTIUM_OPTION`
- `BUILDING_MATERIALS_DEMAND_BREAK`

## 케이스 요약

| case | 분류 | 핵심 판단 |
|---|---|---|
| Czech nuclear read-through | success candidate + 4C-watch | preferred bidder와 3개월 주가 반응은 Stage 2지만 EDF/Westinghouse/Czech court 리스크 때문에 legal 4C-watch다. |
| Hyundai E&C Bulgaria Kozloduy | success candidate | parliament nod와 talks는 Stage 2 pipeline이며 final EPC contract가 아니다. |
| Hyundai Engineering Anseong collapse | hard safety reference | 직접 상장사는 아니지만 fatal bridge collapse는 R10 섹터 safety hard reference다. |
| POSCO E&C / DL safety regulation | 4C-watch | 5% OP fine, license revocation, 반복 사망사고 regulation은 backlog보다 먼저 보는 gate다. |
| Seoul housing policy | event premium | LTV 50% to 40%와 공급확대가 같이 있어 presales/margin/PF 확인 전 Green 금지다. |
| Sejong presidential office | event premium / insufficient evidence | site area와 prep cost는 있지만 listed contractor와 contract value가 없다. |
| Daewoo E&C Nghi Son LNG | success candidate | consortium candidate는 award가 아니다. EPC scope, financing, offtake가 필요하다. |
| Hyundai Steel rebar | 4C-watch | rebar price -10%, net-profit forecast -73%는 building-material demand break다. |

## 산출물

- `data/e2r_case_library/cases_r10_loop12_round266.jsonl`
- `data/sector_taxonomy/round266_r10_loop12_construction_real_estate_materials_price_validation_audit.json`
- `output/e2r_round266_r10_loop12_construction_real_estate_materials_price_validation/round266_r10_loop12_price_validation_summary.md`
- `output/e2r_round266_r10_loop12_construction_real_estate_materials_price_validation/round266_r10_loop12_case_matrix.csv`
- `output/e2r_round266_r10_loop12_construction_real_estate_materials_price_validation/round266_r10_loop12_shadow_weights.csv`
- `output/e2r_round266_r10_loop12_construction_real_estate_materials_price_validation/round266_r10_loop12_green_gate_review.md`
- `output/e2r_round266_r10_loop12_construction_real_estate_materials_price_validation/round266_r10_loop12_stage4b_4c_review.md`

## 핵심 가드레일

- 라운드 케이스는 candidate-generation input이 아니다.
- shadow weight는 production scoring에 적용하지 않는다.
- preferred bidder, talks, public-infra headline, housing policy, candidate consortium만으로 Green을 만들지 않는다.
- 안전사고, 법적 항소, PF/미분양, 건자재 수요 붕괴는 Red Team/4C gate로 유지한다.
- 가격 앵커가 없는 경우 OHLC, MFE, MAE, margin, working capital, cash collection, presales, PF 데이터를 만들지 않는다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round266_r10_loop12_construction_real_estate_materials_price_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round266_r10_loop12_report
```

결과:

- 라운드 266 전용 테스트 통과
- 케이스 8개 JSONL 생성
- 감사 JSON 생성
- 가격 검증/Green gate/4B-4C 보고서 생성

## 다음 작업

R10의 다음 검증은 final contract 이후 실제 progress revenue, margin, working capital, cash collection이 따라왔는지 확인하는 쪽이어야 한다. 예를 들어 원전은 preferred bidder에서 끝나면 Stage 2이고, 건자재는 target upside가 작게 남아 있어도 수요와 spread가 깨지면 4C-watch로 봐야 한다.
