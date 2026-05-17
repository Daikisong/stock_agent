# Checkpoint 28A Round 89 R10 Loop 4 Construction / Real Estate / Building Materials

## 반영 범위

`docs/round/round_89.md`의 R10 Loop 4 내용을 calibration pack으로 반영했다. 생산 scoring은 변경하지 않았고, 케이스와 weight profile은 계속 평가/검증용 자료로만 둔다.

간단한 예시: 데이터센터 REIT IPO가 있어도 자산을 아직 사지 않았고 tenant lease와 NOI/AFFO가 없으면 Stage 3-Green 근거가 아니다. 이 경우 `DATA_CENTER_REIT_IPO_NO_ASSET` Watch로 분리한다.

## 생성/수정 파일

- `src/e2r/sector/round89_r10_loop4_construction_real_estate_materials.py`
- `src/e2r/cli/build_round89_r10_loop4_report.py`
- `tests/test_round89_r10_loop4_construction_real_estate_materials.py`
- `data/e2r_case_library/cases_r10_loop4_round89.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round89_r10_loop4_v4.csv`
- `output/e2r_round89_r10_loop4_construction_real_estate_materials/`

## 핵심 변경

- R10 target을 19개로 확장했다.
- 새 archetype/gate를 추가했다:
  - `DATA_CENTER_REIT_IPO_NO_ASSET`
  - `DATA_CENTER_CAPEX_AFFO_DILUTION`
  - `COLD_CHAIN_DEBT_OCCUPANCY_RISK`
- Round 89 우선 검증 case 19개를 반영했다.
- Equinix Malaysia, Fermi no-tenant/net-loss, Lineage debt/occupancy, Cemex price-cost mixed case를 추가했다.
- 가격 검증 필드에 `capex_to_affo_ratio`, `advanced_liquid_cooling_flag`, `debt_to_ebitda`, `funding_agreement_terminated_flag` 등을 추가했다.

## 요약 수치

- target_count: 19
- case_candidate_count: 19
- success_candidate_count: 3
- event_premium_count: 4
- failed_rerating_count: 1
- stage4b_case_count: 11
- stage4c_case_count: 7
- green_possible_count: 3
- watch_yellow_first_count: 6
- redteam_first_count: 10
- gate_only_target_count: 6

## Green Guardrail

R10은 `수주잔고`, `고배당`, `AI 데이터센터`, `재건 테마`를 먼저 보는 섹터가 아니다. 먼저 PF, cash conversion, occupancy, NOI/AFFO, 배당 커버리지, tenant lease, power/water, 원가율, 출하량을 확인한다.

예를 들어 고배당 REIT라도 `dividend_coverage_ratio`가 약하고 `maintenance_capex` 분류가 의심되면 Green이 아니라 `REIT_AFFO_INTEGRITY_OVERLAY`로 RedTeam 확인을 먼저 한다.

## 검증

실행한 targeted test:

```bash
PYTHONPATH=src python -m unittest tests.test_round89_r10_loop4_construction_real_estate_materials -v
```

결과: 통과.

전체 테스트와 diff check는 커밋 전 최종 검증에서 별도로 실행한다.
