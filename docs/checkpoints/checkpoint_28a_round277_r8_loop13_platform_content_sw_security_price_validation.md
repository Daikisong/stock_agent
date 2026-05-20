# Checkpoint 28A Round 277 R8 Loop 13 Platform Content Software Security Price Validation

## 목적

`docs/round/round_277.md`의 플랫폼·콘텐츠·SW·보안 케이스를 calibration-only 자료로 구조화했다.

이번 라운드의 핵심은 `MAU`, `IPO`, `K-pop IP`, `게임 IP`, `AI/cloud`, `인도 다운로드`만으로 Stage 3-Green을 만들지 않는 것이다. 예를 들어 Webtoon의 170M MAU는 강한 Stage 2 신호지만, 유료 전환과 ARPU/take-rate, creator economics, OP/FCF, NAVER parent value bridge가 확인되기 전에는 Green이 아니다.

## 반영 내용

- canonical archetype 8개 추가
- Round 277 전용 케이스 팩 추가
- JSONL case library 생성
- audit JSON 생성
- shadow weight, deep sub-archetype, green gate, 4B/4C review 출력
- production scoring, 후보 생성, StageClassifier threshold는 변경하지 않음

## 추가 archetype

- `DATA_SOVEREIGNTY_PLATFORM_4C_WATCH`
- `GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN`
- `PLATFORM_GOVERNANCE_LEGAL_4C_WATCH`
- `KPOP_IP_GOVERNANCE_4C_WATCH`
- `GAME_IP_MONETIZATION_IPO_STAGE2`
- `AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE`
- `EMERGING_MARKET_GAME_PLATFORM_OPTION`
- `CYBERSECURITY_TRUST_HARD_4C`

## 케이스 요약

- 케이스 수: 8
- Stage 3 dated case: 0
- success_candidate: 4
- event_premium: 2
- 4C-watch / watch row: 3
- hard 4C direct case: 1

## 핵심 가드레일

- MAU-only Green 금지
- IPO pop-only Green 금지
- downloads without ARPU Green 금지
- AI/cloud keyword without margin Green 금지
- founder/legal overhang 미해소 시 platform premium 차단
- label/artist governance dispute 미해소 시 K-pop IP Green 차단
- 대형 data breach와 internal control failure는 hard 4C 후보

## 생성 파일

- `src/e2r/sector/round277_r8_loop13_platform_content_sw_security_price_validation.py`
- `src/e2r/cli/build_round277_r8_loop13_report.py`
- `tests/test_round277_r8_loop13_platform_content_sw_security_price_validation.py`
- `data/e2r_case_library/cases_r8_loop13_round277.jsonl`
- `data/sector_taxonomy/round277_r8_loop13_platform_content_sw_security_price_validation_audit.json`
- `output/e2r_round277_r8_loop13_platform_content_sw_security_price_validation/`

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round277_r8_loop13_platform_content_sw_security_price_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/archetypes.py src/e2r/sector/round277_r8_loop13_platform_content_sw_security_price_validation.py src/e2r/cli/build_round277_r8_loop13_report.py tests/test_round277_r8_loop13_platform_content_sw_security_price_validation.py
PYTHONPATH=src python -m e2r.cli.build_round277_r8_loop13_report
PYTHONPATH=src python -m unittest discover -s tests -v
```

라운드 전용 테스트 7개와 전체 테스트 3196개가 통과했다.

## 해석

이번 패치는 점수를 바꾸는 작업이 아니라 플랫폼/콘텐츠/SW/보안 archetype의 실패 패턴을 더 정확히 기록하는 작업이다. `SK Telecom`은 데이터 침해가 매출전망 하향, 보안투자, 과징금, 보상 가능성으로 이어진 hard 4C 기준점이다. 반대로 `Webtoon IPO`, `Shift Up IPO`, `Krafton India`는 Stage 2 후보일 수 있지만, 유료 전환과 반복 매출, ARPU, FCF가 없으면 Green으로 올리지 않는다.
