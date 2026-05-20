# Checkpoint 28A Round 240 R10 Loop 10 Construction Real Estate Materials Price Validation

## 목적

`docs/round/round_240.md`의 R10 Loop 10 내용을 case-library 가격경로 검증팩으로 반영했다.
이번 라운드는 건설·부동산·건자재 안에서 원전 EPC 수출, 항만 인프라 준공, 서울 주택정책, PF credit break, 건설 안전사고, workplace fatality 규제, AI data-center real asset, 철근/건자재 수요 약화를 분리한다.

쉬운 예로, `우선협상대상자 선정`은 관심 신호가 될 수 있지만 상장사별 수주 패키지, 마진, 운전자본, 현금회수가 확인되기 전에는 Stage 3-Green 근거가 아니다.

## 반영 파일

- `src/e2r/sector/round240_r10_loop10_construction_real_estate_materials_price_validation.py`
- `src/e2r/cli/build_round240_r10_loop10_report.py`
- `tests/test_round240_r10_loop10_construction_real_estate_materials_price_validation.py`
- `data/e2r_case_library/cases_r10_loop10_round240.jsonl`
- `data/sector_taxonomy/round240_r10_loop10_construction_real_estate_materials_price_validation_audit.json`
- `output/e2r_round240_r10_loop10_construction_real_estate_materials_price_validation/`

## 핵심 결과

- source_round: `docs/round/round_240.md`
- analyst_round_id: `round_168`
- large_sector: `CONSTRUCTION_REAL_ESTATE_MATERIALS`
- cases: 8
- success_candidate: 3
- event_premium: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 6
- 4C-watch cases: 3
- hard_4c_case_count: 2
- price_validation_completed: `partial_with_reported_price_anchors`
- full_ohlc_complete: false
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true

## 새 canonical archetype

- `NUCLEAR_INFRA_EPC_EXPORT`
- `PORT_INFRA_DELIVERY`
- `HOUSING_POLICY_SUPPLY_EVENT`
- `REAL_ESTATE_PF_CREDIT_BREAK`
- `CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C`
- `WORKPLACE_FATALITY_REGULATORY_4C`
- `BUILDING_MATERIALS_DEMAND_CYCLE`
- `PRICE_ONLY_POLICY_RALLY`
- `EVIDENCE_GOOD_BUT_PRICE_UNPROVEN`

`AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT`는 기존 enum을 R10 Loop10 관점으로 상세 정의했다.

## 케이스 해석

- Czech nuclear infra: KHNP 계약은 407B koruna / $18.7B 규모 signed contract로 Stage 2다. 두산에너빌리티 +48%, 한전기술 +41% 같은 preferred-bidder 구간 가격 반응은 4B-watch 성격이며, 상장사별 package/margin/cashflow 전 Green 보류.
- Daewoo E&C Grand Faw Port: dock 5개 완공과 2028년 350만 컨테이너 capacity 목표는 delivery Stage 2다. 추가 수주, 마진, 현금회수가 필요하다.
- Seoul housing policy: LTV 50%에서 40%로 강화되고 공급정책이 같이 나왔다. 정책 event일 뿐, 분양률·원가율·PF 안정·FCF 전 Green 금지.
- Taeyoung / PF basket: PF delinquency가 0.37%에서 2.70%로 상승한 것은 hard 4C다. 40.6조원 지원책은 Green이 아니라 relief다.
- Hyundai Engineering bridge collapse: 4명 사망, 6명 부상, 10명 추락은 sector hard 4C다. 직접 상장사 mapping이 불명확해도 safety gate는 닫힌다.
- POSCO E&C / DL Construction safety: 103개 현장중단, 약 80명 임원 사퇴, 영업이익 최대 5% 벌금·면허취소 리스크는 4C-watch다.
- SK/AWS·OpenAI/Samsung data center: 7조원, 100MW, 1GW 확장 가능성, Kakao +11% 등은 Stage 1/2 + event premium이다. Tenant, NOI/AFFO, 전력·용수·인허가, capex per share 전 Green 금지.
- Hyundai Steel rebar proxy: 29,000원, -1.2%, 2024 순이익 추정 -73%, 철근 가격 -10% 전망은 building-material demand 4C-watch다.

## Guardrail

- Preferred bidder, contract headline, PF relief, housing policy, data-center theme, asset headline만으로 Green 금지.
- Margin/NOI/AFFO, cash flow after working capital, PF/funding cost 통과, 공정률·원가율 안정, tenant/occupancy/utilization, 안전·품질 hard risk 부재가 확인돼야 Stage 3 검토 가능.
- PF workout/debt reschedule과 fatal construction accident는 hard 4C reference로 둔다.
- 이 팩은 calibration/evaluation 전용이며 production scoring과 candidate generation에는 사용하지 않는다.

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round240_r10_loop10_construction_real_estate_materials_price_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round240_r10_loop10_report`
