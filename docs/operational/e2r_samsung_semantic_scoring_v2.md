# 삼성전자 C06 semantic scoring v2

기준일은 `2026-07-11 KST`다. 이 문서는 그 날짜까지 공개된 자료만 사용한 production 결과를 설명한다. 미래 가격이나 사후 성과는 입력하지 않았다.

## 결론

삼성전자는 `FULL_E2R_100`, `18.159977점`, canonical `Stage 0`으로 종결됐다. `full_score_valid=true`, 7개 component terminal, 전체 critical 0이다. Stage 0은 “HBM4 근거가 없다”는 뜻이 아니다. HBM4 양산 출하와 메모리 ASP 상승은 확인됐지만, 중기 추정치·시장 기대·FCF 같은 더 강한 논리를 완결할 독립 근거가 부족하다는 뜻이다.

쉬운 예: “HBM4를 실제 출하했다”는 제품 실행 근거는 점수를 받는다. 그러나 이 문장 하나로 “고객이 장기 물량을 모두 예약했다”거나 “FCF가 폭발한다”고 점프하지 않는다.

## source와 claim 사슬

- 13개 material question 전부 bounded source task를 실행했다.
- research iteration은 `production-01`부터 `production-06`까지다.
- 최종 scoring에 들어간 full document는 DART 2026년 1분기 분기보고서 1건이다.
- organic accepted claim 18건, accepted primitive mapping 22건이다.
- impact proposal 37건 전부 검증됐고, 그중 실제 accepted mapping에 유효한 경제 impact는 결정론적 validator를 통과했다.
- economic fact cluster는 10개다.
- search saturation은 `EVIDENCE_FOUND` 5개, `ADEQUATE_ABSENCE` 8개이며 pending은 0개다.

독립 gold lane에서는 [삼성 HBM4 상용 출하 공식 발표](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing), 삼성 공식 IR, DART를 별도로 확인했다. 삼성 gold fact 4개가 production fact와 모두 매칭됐고 critical miss는 0이다.

## 핵심 의미 판정

| 근거 | semantic 결과 | 금지된 과잉 추론 |
|---|---|---|
| `세계 최초 ... HBM4 양산 출하 (2026.02.)` | shipment/revenue-mix와 information 계열의 bounded support | 고객 장기 allocation, 선판매 CAPA로 자동 승격하지 않음 |
| `제한된 공급 가용량 내에서 ... CPU/GPU향 초기 메모리 수요` | HBM capacity constraint의 약한 support | sold-out 또는 취소불가 계약으로 보지 않음 |
| 메모리 평균판매가격 약 146% 상승 | realized pricing support | HBM 단독 ASP로 바꾸지 않음 |
| 11.2조원 첨단공정 증설·전환 투자 | capital allocation support이자 shortage 논리의 counter | 현재 shortage 근거를 삭제하지 않고 같은 component에서 cap 적용 |

Tesla/Foundry 관련 claim이 C06 고객 allocation을 지원한 건수는 0이다. 같은 삼성전자 공시라도 Foundry 수주와 HBM 고객 배정은 사업 메커니즘이 다르기 때문이다. 예를 들어 “한 식당의 단체예약”을 같은 회사가 운영하는 다른 카페의 예약으로 세면 안 되는 것과 같다.

## component 결과

| component | 상태 | 점수 / 최대 |
|---|---:|---:|
| EPS/FCF explosion | VERIFIED_WEAK_SUPPORT | 5.625823 / 24 |
| earnings visibility | VERIFIED_WEAK_SUPPORT | 4.157904 / 21 |
| bottleneck pricing | SUPPORT_WITH_COUNTER_CAP | 3.551250 / 19 |
| market mispricing | VERIFIED_ABSENT_AFTER_SEARCH | 0 / 15 |
| valuation rerating | VERIFIED_ABSENT_AFTER_SEARCH | 0 / 12 |
| capital allocation | VERIFIED_WEAK_SUPPORT | 0.825 / 4 |
| information confidence | VERIFIED_STRONG_SUPPORT | 4 / 5 |

대표 subcriterion은 실제 실적 5.625823/7, 출하·매출믹스 3.368424/4, realized ASP 2.95125/5다. 공급 대응 subcriterion은 support 0.05와 counter 0.05가 함께 남아 순점수 0이 됐다. 이것은 counter 누락이 아니라 양쪽 근거를 같은 component에서 실제 상계한 결과다.

## 재현 leaf

canonical leaf는 `output/evidence_to_score_v2/live_2026-07-11/005930/` 아래에 있다. gold, production, 비교, source task, adequacy, full document, accepted claim, eligibility, proposed/validated impact, fact cluster, subcriterion, component, score vector, semantic trace, StageCourt trace를 각각 독립 파일로 보존했다.

직접적인 투자 권고는 하지 않는다. 현재 결과의 적절한 표현은 “Stage 0, HBM4 출하·가격 근거는 확인됐으나 고객 commitment·revision·valuation bridge를 계속 관찰”이다.
