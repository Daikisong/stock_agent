# Checkpoint 28A Round 118: R13 Loop 6 Cross-Archetype RedTeam / 4B / Price Validation

## 목적

Round 118은 새 섹터 점수 모델이 아니라, R1~R12에서 나온 모든 후보에 공통으로 걸어야 하는 최종 검증층이다. 핵심은 `점수가 높다 = Stage 3-Green`이 아니라는 점을 명시하는 것이다.

쉬운 예시는 다음과 같다.

- SK하이닉스 HBM처럼 구조적 증거가 강해도, 이미 시장이 새 프레임을 충분히 반영했다면 `STRUCTURAL_SUCCESS_BUT_4B_WATCH`로 본다.
- Supermicro처럼 매출 성장 스토리가 있어도 감사인 사임, 제출 지연, 내부통제 문제가 있으면 `REDTEAM_ACCOUNTING_TRUST_OVERLAY`로 Green을 막는다.
- Fermi 같은 AI 전력/데이터센터 자산형 스토리는 매출, 임차인, 전력 인허가, 자금조달이 확인되기 전까지 `DISCLOSURE_CONFIDENCE_CAPPED`로 제한한다.

## 반영 내용

- R13 Loop 6 공통 RedTeam/4B/가격검증 타깃 21개를 추가했다.
- 라운드118 케이스 후보 25개를 JSONL로 생성했다.
- 공통 검증용 score-weight profile v6 CSV를 생성했다.
- 다음 신규/정리 archetype을 canonical enum에 추가했다.
  - `STRUCTURAL_SUCCESS_BUT_4B_WATCH`
  - `SECTOR_SUCCESS_BUT_POLICY_SHOCK_WATCH`
  - `DISCLOSURE_CONFIDENCE_CAPPED`
- 생산 scoring 변경은 하지 않았다.
- 케이스 레코드는 candidate generation 입력으로 쓰지 않는다.

## 산출물

- `src/e2r/sector/round118_r13_loop6_cross_archetype_redteam.py`
- `src/e2r/cli/build_round118_r13_loop6_report.py`
- `tests/test_round118_r13_loop6_cross_archetype_redteam.py`
- `data/e2r_case_library/cases_r13_loop6_round118.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round118_r13_loop6_v6.csv`
- `output/e2r_round118_r13_loop6_cross_archetype_redteam/round118_r13_loop6_cross_archetype_redteam_summary.md`
- `output/e2r_round118_r13_loop6_cross_archetype_redteam/round118_r13_loop6_case_matrix.csv`
- `output/e2r_round118_r13_loop6_cross_archetype_redteam/round118_r13_loop6_overlay_target_matrix.csv`
- `output/e2r_round118_r13_loop6_cross_archetype_redteam/round118_r13_loop6_stage_date_plan.csv`
- `output/e2r_round118_r13_loop6_cross_archetype_redteam/round118_r13_loop6_redteam_gate_plan.md`
- `output/e2r_round118_r13_loop6_cross_archetype_redteam/round118_r13_loop6_price_validation_plan.md`
- `output/e2r_round118_r13_loop6_cross_archetype_redteam/round118_r13_loop6_price_fields.csv`

## 요약 수치

- target_count: 21
- case_candidate_count: 25
- structural_success_count: 1
- success_candidate_count: 3
- cyclical_success_count: 1
- event_premium_count: 1
- overheat_count: 1
- failed_rerating_count: 8
- stage4b_case_count: 4
- stage4c_case_count: 8
- hard_gate_target_count: 10
- green_possible_count: 1
- watch_yellow_first_count: 6
- redteam_first_count: 14
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Green 차단 원칙

Round 118 기준 Stage 3-Green은 다음 조건을 동시에 요구한다.

- cross-evidence가 있어야 한다.
- EPS/FCF 지속성이 있어야 한다.
- 가격 경로가 증거와 맞아야 한다.
- 공시/리포트 신뢰도가 충분해야 한다.
- hard RedTeam flag가 없어야 한다.
- 이미 4B 포화 구간이면 안 된다.
- 정책 충격 overlay가 통과되어야 한다.

반대로 아래는 Green을 만들면 안 된다.

- 가격만 오른 경우
- 정책/MOU/이벤트 프리미엄만 있는 경우
- list-only 공시 제목만 있는 경우
- 회계 신뢰도 훼손이 있는 경우
- AFFO, capex, tenant, funding-cost가 불명확한 실물자산형 AI 인프라
- supplier-investor-customer 순환 구조가 강한 AI financing
- stablecoin convertibility/depeg 리스크

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round118_r13_loop6_cross_archetype_redteam -v
PYTHONPATH=src python -m e2r.cli.build_round118_r13_loop6_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

검증 결과:

- Round 118 전용 테스트: 11개 통과
- 전체 테스트: 1537개 통과
- diff whitespace check: 통과

## 다음 단계

Round 118은 점수 변경이 아니라 공통 가드레일 확장이다. 다음 라운드에서 실제 scoring shadow simulation을 할 때도 이 레이어는 “높은 점수를 Green으로 바로 승격하지 않는 안전장치”로 유지해야 한다.
