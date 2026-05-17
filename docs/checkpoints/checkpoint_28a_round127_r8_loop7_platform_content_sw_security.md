# Checkpoint 28A Round 127: R8 Loop 7 플랫폼·콘텐츠·SW·보안

## 반영 범위

- 입력 문서: `docs/round/round_127.md`
- 추가 모듈: `src/e2r/sector/round127_r8_loop7_platform_content_sw_security.py`
- 추가 CLI: `src/e2r/cli/build_round127_r8_loop7_report.py`
- 추가 테스트: `tests/test_round127_r8_loop7_platform_content_sw_security.py`
- 산출물:
  - `data/e2r_case_library/cases_r8_loop7_round127.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round127_r8_loop7_v7.csv`
  - `output/e2r_round127_r8_loop7_platform_content_sw_security/`

## 핵심 판단

R8 Loop 7은 "AI 기능이 있나"가 아니라 "AI·플랫폼·콘텐츠·보안이 반복매출과 FCF로 바뀌었나"를 본다.

예를 들어 AI assistant 출시만 있으면 Stage 1 근거다. 하지만 ARR, billings, bookings, contract value, guidance 상향, churn 안정, OPM/FCF 전환이 같이 보이면 Stage 2~3 후보가 된다.

## 새로 보강한 내용

- `AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER` canonical archetype을 추가했다.
- Cisco AI networking 사례를 `CLOUD_AI_SOFTWARE_INFRA` 보조 사례가 아니라 R8 crossover target으로 분리했다.
- R8 v7 기본 점수축 7개를 추가했다.
  - ARR/billings/bookings/ad revenue/contract value: 24점
  - 반복성·retention·workflow lock-in: 20점
  - AI/cloud/security/platform 병목성: 14점
  - OPM/FCF/gross margin 전환: 12점
  - 시장 오해·리레이팅 gap: 10점
  - valuation room/4B 여지: 8점
  - 운영 신뢰·법적 리스크·privacy·youth safety·disclosure: 12점

## Green Guardrail

- AI 기능, 유저 수, 신작 기대, 광고 회복, 보안 수요만으로 Stage 3-Green을 만들지 않는다.
- 보안 장애, ARR/guidance miss, bookings cut, scam ads, privacy/youth safety, 저작권/IP 리스크는 RedTeam gate다.
- 케이스 팩은 calibration/evaluation 자료이며 production scoring input이 아니다.

## 검증

- `PYTHONPATH=src python -m unittest tests/test_round127_r8_loop7_platform_content_sw_security.py -v`
- `PYTHONPATH=src python -m e2r.cli.build_round127_r8_loop7_report`

## 남은 작업

- 가격 경로 backfill로 Stage 2/3/4B/4C 가격과 MFE/MAE를 채워야 한다.
- R8 v7 점수축은 아직 production scoring에 적용하지 않는다.
- 이후 shadow scoring에서 기존 점수와 병렬 비교한 뒤 적용 여부를 판단한다.
