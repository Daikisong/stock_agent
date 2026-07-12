# SK하이닉스 C06 semantic scoring v2

기준일은 `2026-07-11 KST`다. 기준일 이후 자료와 사후 주가 성과는 사용하지 않았다.

## 결론

SK하이닉스는 `FULL_E2R_100`, `19.120509점`, canonical `Stage 0`으로 종결됐다. `full_score_valid=true`, 7개 component terminal, 전체 critical 0이다. 낮은 점수로 확정한 이유는 source 실패가 아니라 13개 질문을 모두 조사한 뒤 6개가 충분한 검색 증명과 함께 absence/non-scoring으로 닫혔기 때문이다.

쉬운 예: “수요가 강하고 공급이 제한됐다”는 shortage 근거는 실제 점수를 받는다. 그래도 “고객이 수년 치 HBM 전량을 취소불가로 예약했다”는 별도 계약 사실이 없으면 그 강한 문턱까지 올리지 않는다.

## source와 claim 사슬

- 13개 material question 전부 bounded source task를 실행했다.
- research iteration은 `production-01`부터 `production-07`까지다.
- 최종 scoring full document는 2건이며, 핵심은 DART 2026년 1분기 분기보고서다.
- organic accepted claim 33건, accepted primitive mapping 37건이다.
- impact proposal 119건 중 115건이 validated impact로 남았다. scope validator가 거절한 impact는 점수에 들어가지 않았다.
- economic fact cluster는 19개다.
- search saturation은 `EVIDENCE_FOUND` 7개, `ADEQUATE_ABSENCE` 6개이며 pending은 0개다.

독립 gold lane에서는 [SK하이닉스 2026년 1분기 공식 실적 발표](https://news.skhynix.co.kr/q1-2026-business-results/), DART, [2026-07-10 Reuters 독립 보도](https://www.investing.com/news/stock-market-news/sk-hynix-ceo-sees-worstever-memory-supply-shortage-in-2027-says-demand-to-outstrip-supply-beyond-2030-4786660)를 별도로 확인했다. 하이닉스 gold fact 5개가 모두 production fact와 매칭됐고 critical miss는 0이다.

## 핵심 의미 판정

| 근거 | semantic 결과 | 금지된 과잉 추론 |
|---|---|---|
| `견조한 수요 대비 제한된 공급 환경이 지속` | HBM capacity constraint에 nonzero support | 취소불가 장기계약 또는 전량 sold-out으로 자동 승격하지 않음 |
| HBM·서버 DRAM·eSSD 가격 상승이 최대 실적과 수익률을 견인 | pricing과 actual earnings에 bounded support | HBM 단독 실적·ASP로 바꾸지 않음 |
| 1분기 영업이익 37.6조원, 영업이익률 72% | revenue/profit와 margin conversion support | FCF가 공시된 것으로 보지 않음 |
| 고객과 월별·분기별 합의로 공급량·가격 결정 | customer commitment의 약한 support | HBM 전용 장기 allocation으로 보지 않음 |
| substrate 9개사 공급 | profile/non-scoring guard | HBM 생산 CAPA나 고객 예약을 열지 않음 |

## component 결과

| component | 상태 | 점수 / 최대 |
|---|---:|---:|
| EPS/FCF explosion | VERIFIED_WEAK_SUPPORT | 6.440063 / 24 |
| earnings visibility | VERIFIED_WEAK_SUPPORT | 2.75 / 21 |
| bottleneck pricing | VERIFIED_WEAK_SUPPORT | 5.130446 / 19 |
| market mispricing | VERIFIED_ABSENT_AFTER_SEARCH | 0 / 15 |
| valuation rerating | VERIFIED_WEAK_SUPPORT | 0.2 / 12 |
| capital allocation | VERIFIED_WEAK_SUPPORT | 0.6 / 4 |
| information confidence | VERIFIED_STRONG_SUPPORT | 4 / 5 |

대표 subcriterion은 실제 실적 5.158013/7, margin conversion 1.28205/5, capacity constraint 1.304352/6, realized ASP 3.47827/5다. 과거 문제였던 “좋은 shortage·실적 claim이 있는데 cap 누락 때문에 0점”은 발생하지 않았다.

## 재현 leaf

canonical leaf는 `output/evidence_to_score_v2/live_2026-07-11/000660/` 아래에 있다. 각 claim의 eligibility, impact, fact cluster, subcriterion과 Stage 결정이 분리돼 있어 claim 수만 늘려 점수를 부풀릴 수 없다.

직접적인 투자 권고는 하지 않는다. 현재 결과의 적절한 표현은 “Stage 0, 공급 제약·가격·실적 전환은 관찰되지만 중기 revision·valuation bridge와 HBM 전용 고객 commitment를 계속 확인”이다.
