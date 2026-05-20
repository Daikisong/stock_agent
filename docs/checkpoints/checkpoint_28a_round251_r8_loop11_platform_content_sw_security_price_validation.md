# Checkpoint 28A Round 251: R8 Loop 11 Platform/Content/SW/Security Price Validation

## 목적

`docs/round/round_251.md`의 R8 Loop 11 내용을 calibration/evaluation 자료로 구조화했다.
이번 패치는 production scoring을 바꾸지 않는다.

쉬운 예시:

- 카카오/OpenAI 제휴처럼 주가가 먼저 움직여도, 유료 사용량·ARPU·마진·FCF가 없으면 Stage 3-Green이 아니다.
- SK텔레콤 보안 사고처럼 고객 데이터 유출, 매출 전망 하향, 보상비, 과징금이 같이 있으면 가격 반응만이 아니라 논리 훼손 hard 4C로 본다.

## 반영 파일

- `src/e2r/sector/round251_r8_loop11_platform_content_sw_security_price_validation.py`
- `src/e2r/cli/build_round251_r8_loop11_report.py`
- `tests/test_round251_r8_loop11_platform_content_sw_security_price_validation.py`
- `data/e2r_case_library/cases_r8_loop11_round251.jsonl`
- `data/sector_taxonomy/round251_r8_loop11_platform_content_sw_security_price_validation_audit.json`
- `output/e2r_round251_r8_loop11_platform_content_sw_security_price_validation/`

## 추가/확정한 canonical archetype

- `AI_SOFTWARE_PARTNERSHIP_EVENT`
- `GAME_IP_PLATFORM_EXPANSION`
- `GAME_IP_M_AND_A_CONTENT_EXPANSION`
- `SECURITY_OPERATIONAL_TRUST_HARD_4C`
- `KPOP_PLATFORM_CONTENT_IP_GOVERNANCE`

## 케이스 요약

| case | 판단 |
|---|---|
| Douzone Bizon | B2B SaaS Stage 2 watch. ARR, churn, OPM, FCF 확인 전 Green 금지 |
| Samsung SDS | AI capital allocation Stage 2 + 4B-watch. KKR/AI 이벤트가 매출 전환보다 먼저 가격에 반영 |
| LG CNS | cloud/AI evidence는 있으나 IPO 가격 반응 실패. evidence_good_but_price_failed |
| NAVER/Webtoon | IP platform Stage 2. MAU보다 paid usage, ARPU, IP licensing, FCF가 필요 |
| Kakao/OpenAI | partnership headline 기반 price_moved_without_evidence |
| Krafton | game/IP expansion Stage 2 watch. bookings, retention, India regulation, FCF 확인 필요 |
| SK Telecom | privacy/security trust break hard 4C |
| HYBE | governance/legal 4C-watch. hard 4C는 미확정 |

## Green gate 원칙

R8의 Green은 AI, 플랫폼, 웹툰, 게임, K-pop 같은 키워드만으로 만들 수 없다.
필수 확인 축은 다음이다.

- recurring revenue 또는 bookings
- ARPU, paid usage, ARR proxy
- OPM 또는 gross margin 개선
- FCF conversion
- retention 또는 churn 안정성
- IP monetization이 단일 launch/event를 넘어서는지
- AI 기능이 실제 paid revenue 또는 cost saving으로 이어지는지
- privacy/security/governance risk가 통과되는지
- 가격 경로가 evidence 이후에 정렬되는지

## 4B/4C 원칙

- 4B-watch: partnership, IPO, M&A, Disney/Webtoon event, game downloads처럼 매출 전환보다 price premium이 먼저 생긴 경우.
- hard 4C: 개인정보 유출, 보안 신뢰 훼손, 매출 전망 하향, 보상비, 규제 과징금, founder/legal 리스크가 사업 논리를 직접 훼손한 경우.

예시:

- `Kakao/OpenAI`: 이벤트는 있지만 monetization이 없어 4B-watch 성격이다.
- `SK Telecom`: 보안 사고가 매출 전망, 고객 보상, 과징금까지 연결되어 hard 4C다.

## 산출물

CLI:

```bash
PYTHONPATH=src python -m e2r.cli.build_round251_r8_loop11_report
```

생성 파일:

- `round251_r8_loop11_price_validation_summary.md`
- `round251_r8_loop11_case_matrix.csv`
- `round251_r8_loop11_target_aliases.csv`
- `round251_r8_loop11_deep_sub_archetypes.csv`
- `round251_r8_loop11_score_adjustments.csv`
- `round251_r8_loop11_shadow_weights.csv`
- `round251_r8_loop11_price_validation_fields.csv`
- `round251_r8_loop11_green_gate_review.md`
- `round251_r8_loop11_price_validation_plan.md`
- `round251_r8_loop11_stage4b_4c_review.md`
- `round251_r8_loop11_deep_sub_archetypes.md`

## 유지한 제약

- production scoring 변경 없음
- candidate generation input 아님
- shadow weight only
- full OHLC 미완성 상태를 명시
- Stage 3-Green threshold 완화 없음
- buy/sell 문구 없음
- API key 출력 없음

## 다음 작업

다음 라운드에서는 full OHLC와 ARR/paid usage/bookings/OPM/FCF 확인 자료를 추가해야 한다.
현재 round_251은 “어떤 증거가 없으면 Green을 막아야 하는지”를 정리한 검증팩이지, production score 적용 단계가 아니다.
