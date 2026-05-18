# Checkpoint 28A Round 184 R13 Loop 11 Cross-Archetype RedTeam

Round 184 반영 목적은 새 섹터를 하나 더 만드는 것이 아니라, R1-R12에서 나온 모든 후보를 공통으로 검증하는 RedTeam / 4B / 가격검증 오버레이를 구조화하는 것이다.

## 반영 내용

- `STRUCTURAL_STAGE3_EARLY_CAPTURE`, `STAGE2_STRONG_NOT_GREEN`, `EVENT_PRICE_RALLY_NOT_STAGE3`, `CYCLE_SUCCESS_NOT_STRUCTURAL` 등 공통 검증 archetype을 추가했다.
- 한미반도체, 삼성E&A, 삼성SDS, 알테오젠, 핑크퐁, 삼성SDI, 한국가스공사/대성에너지, 기아, 제주항공, NAVER-Dunamu 등 15개 케이스 후보를 calibration 전용 case pack으로 만들었다.
- Stage 3 조기 포착은 9개 체크 중 6개 이상을 요구하도록 문서화했다.
- Stage 2 strong은 계약, 전략투자, 승인, 지분거래, IPO, 정책 실행, 가격반응이 있어도 EPS/FCF/OPM 전환 전에는 Green이 아니라고 명시했다.
- Stage 4B는 가격 급등, crowded narrative, revision lag, peer valuation 등을 함께 보는 감시 레이어로 분리했다.
- Stage 4C는 안전사고, PF, 사이버, 법률/거버넌스, 계약취소, 정책충격 같은 hard gate로 정리했다.

예를 들어 한국가스공사/대성에너지의 동해 가스 이벤트처럼 하루에 크게 오른 케이스는 가격검증 데이터로는 중요하지만, 상업성·매출·현금흐름이 확인되기 전에는 Stage 3가 아니다.

## 산출물

- `data/e2r_case_library/cases_r13_loop11_round184.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round184_r13_loop11_v11.csv`
- `output/e2r_round184_r13_loop11_cross_archetype_redteam/round184_r13_loop11_cross_archetype_redteam_summary.md`
- `output/e2r_round184_r13_loop11_cross_archetype_redteam/round184_r13_loop11_case_matrix.csv`
- `output/e2r_round184_r13_loop11_cross_archetype_redteam/round184_r13_loop11_stage_date_plan.csv`
- `output/e2r_round184_r13_loop11_cross_archetype_redteam/round184_r13_loop11_redteam_gate_plan.md`
- `output/e2r_round184_r13_loop11_cross_archetype_redteam/round184_r13_loop11_price_validation_plan.md`
- `output/e2r_round184_r13_loop11_cross_archetype_redteam/round184_r13_loop11_score_stage_price_alignment.md`

## 안전장치

- production scoring은 변경하지 않았다.
- case library는 candidate-generation input이 아니다.
- 이벤트 가격 급등, 미확정 고객 보도, MOU/LOI, 비구속 계약, private/holdco 가치만으로 Stage 3-Green을 만들지 않는다.
- 가격, MFE/MAE, 계약금액, 고객명, 기간, royalty, ARR, AFFO, 처방량은 아직 backfill 대상으로 남겼고 임의로 채우지 않았다.

## 다음 작업

Round 184 산출물은 향후 점수 구현 전에 필요한 공통 안전 체크리스트다. 다음 단계에서는 실제 가격 경로와 공시 detail을 backfill해서, Stage 2 strong과 Stage 3 early-capture 사이의 경계가 과도하게 느슨해지지 않는지 검증해야 한다.
