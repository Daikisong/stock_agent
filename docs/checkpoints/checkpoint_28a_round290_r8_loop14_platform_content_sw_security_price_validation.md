# Checkpoint 28A Round 290 R8 Loop 14 Platform Content Software Security Price Validation

## 반영 범위

- 입력 문서: `docs/round/round_290.md`
- analyst round id: `round_218`
- 대섹터: `PLATFORM_CONTENT_SW_SECURITY`
- 생산 점수 변경: 없음
- candidate generation 입력 사용: 없음
- 적용 방식: `shadow_weight_only`

이번 라운드는 플랫폼, 콘텐츠, 게임, 기업용 SW, 보안 신뢰를 같은 대섹터 안에서 더 좁게 쪼갠 검증팩이다. 예를 들어 Webtoon의 IPO 첫날 상승은 좋은 이벤트지만, NAVER의 EPS/FCF 체급 변화로 닫히려면 유료전환, ARPU, IP 매출 안정성, 모회사 가치 연결이 필요하다.

## 추가된 Canonical Archetype

- `WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE`
- `KAKAO_PLATFORM_GOVERNANCE_4C_WATCH`
- `KPOP_IP_CONTRACT_GOVERNANCE_4C`
- `GAME_IP_IPO_STAGE2_QUALITY_GATE`
- `LEGACY_GAME_TURNAROUND_BUYBACK_4B`
- `AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE`
- `ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2`
- `CYBERSECURITY_TRUST_HARD_4C_REFERENCE`

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| NAVER / Webtoon | event premium + aftermarket gate | 170M MAU와 IPO pop은 Stage 2. Green은 paid conversion, IP revenue stability, parent value capture 필요 |
| Kakao / SM | 4C-watch | 창업자 법률 리스크와 금융 자회사 control risk가 platform premium을 막음 |
| HYBE / ADOR / NewJeans | 4C-watch | fandom과 artist IP만으로는 부족. contract continuity와 label governance 필요 |
| Shift Up | success candidate | Hit IP와 IPO는 Stage 2. live-service retention, monetization, next-title pipeline 필요 |
| NCSoft | event premium + 4B-watch | Q1 beat와 buyback은 이벤트. 신작 retention과 global monetization 전에는 Green 아님 |
| LG CNS | evidence good but price failed | cloud/AI 매출비중과 청약 흥행에도 공모가를 지키지 못함 |
| Douzone Bizon | enterprise SW Stage 2 | EQT control premium은 Stage 2. ARR, churn, cloud margin, regulatory approval 필요 |
| SK Telecom | hard 4C reference | 데이터 유출이 주가 하락, 매출전망 하향, 보상비용, 보안투자, 과징금으로 연결 |

## Green Gate 보정 방향

올릴 축:

- paid conversion / ARPU
- retention and repeat usage
- IP revenue stability
- artist contract continuity
- game live-service retention
- new-title pipeline execution
- cloud/AI recurring revenue
- ARR retention for enterprise SW
- data trust / internal control
- regulatory / governance clearance

내릴 축:

- MAU headline only
- IPO pop only
- AI/cloud keyword only
- creator/IP optional value only
- fandom without contract stability
- buyback without new-title retention
- PE control premium without ARR
- cybersecurity theme read-through without contract
- unresolved governance/legal risk

## 4B / 4C 해석

- `4B-watch`: IPO 첫날 급등, AI/cloud 키워드 고평가, hit title 하나에 집중된 게임 밸류, buyback rally, PE control premium처럼 증거보다 가격이 먼저 간 상태.
- `hard 4C`: SK Telecom처럼 데이터 신뢰 훼손이 매출전망 하향, 보상비용, 보안투자, 과징금으로 실제 손익에 내려온 상태.

## 생성 산출물

- `data/e2r_case_library/cases_r8_loop14_round290.jsonl`
- `data/sector_taxonomy/round290_r8_loop14_platform_content_sw_security_price_validation_audit.json`
- `output/e2r_round290_r8_loop14_platform_content_sw_security_price_validation/round290_r8_loop14_price_validation_summary.md`
- `output/e2r_round290_r8_loop14_platform_content_sw_security_price_validation/round290_r8_loop14_case_matrix.csv`
- `output/e2r_round290_r8_loop14_platform_content_sw_security_price_validation/round290_r8_loop14_shadow_weights.csv`
- `output/e2r_round290_r8_loop14_platform_content_sw_security_price_validation/round290_r8_loop14_green_gate_review.md`
- `output/e2r_round290_r8_loop14_platform_content_sw_security_price_validation/round290_r8_loop14_stage4b_4c_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests/test_round290_r8_loop14_platform_content_sw_security_price_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round290_r8_loop14_report
```

결과:

- round_290 단위 테스트 통과
- case library 레코드 validation 통과
- 리포트 생성 완료
- production scoring 변경 없음

## 다음 라운드에 남긴 기준

이 라운드의 핵심은 “플랫폼 숫자”가 아니라 “반복 수익과 신뢰가 손익으로 닫혔는지”다. 예를 들어 `MAU=170M`은 사용자가 많다는 뜻이지, 곧바로 EPS/FCF가 커진다는 뜻은 아니다. 반대로 `data breach`는 성장 이벤트가 아니라 고객 신뢰와 비용 구조가 깨지는 hard 4C 기준이다.
