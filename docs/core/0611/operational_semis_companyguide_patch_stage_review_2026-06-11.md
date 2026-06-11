# 2026-06-11 삼성전자/SK하이닉스 운영형 재실행 기록

## 목적

CompanyGuide/WiseReport 리포트·컨센서스 유입 패치를 적용한 뒤, 삼성전자(`005930`)와 SK하이닉스(`000660`)를 실제 운영에 가깝게 다시 돌렸다.

핵심 확인점은 두 가지다.

- 리포트/컨센서스가 더 이상 0으로 비지 않고 파이프라인 입력에 들어오는가
- LLM이 AI 데이터센터/HBM 테마 전환과 부족한 슬롯 확장 검색을 실제로 수행하는가

## 실행 조건

| 항목 | 값 |
|---|---|
| 기준일 | `2026-06-11` |
| 실행 방식 | targeted smoke 후보로 종목 강제 투입 |
| fixture mode | `False` |
| live enabled | `True` |
| LLM provider | `E2R_THEME_ROUTE_PROVIDER=codex` |
| theme rebalance | `True` |
| max theme expansion rounds | `3` |
| CompanyGuide enrichment | `True` |
| page fetch | `True` |

targeted smoke는 종목을 강제로 검사하기 위한 운영형 확인 경로다. production 후보 편입 여부만 강제일 뿐, 가격/뉴스/공시/리포트/컨센서스/LLM 라우팅/점수화는 실제 runner 경로를 탄다.

## 산출물

| 종목 | run log | evidence |
|---|---|---|
| 삼성전자 | `output/live_verify_005930_2026-06-11_operational_companyguide_patch/korea_live_lite/2026-06-11_run_log.json` | `output/live_verify_005930_2026-06-11_operational_companyguide_patch/korea_live_lite/2026-06-11_evidence.json` |
| SK하이닉스 | `output/live_verify_000660_2026-06-11_operational_companyguide_patch/korea_live_lite/2026-06-11_run_log.json` | `output/live_verify_000660_2026-06-11_operational_companyguide_patch/korea_live_lite/2026-06-11_evidence.json` |
| 통합 요약 | `output/operational_semis_companyguide_patch_summary_2026-06-11.json` | - |

## 결론 요약

| 종목 | 최종 Stage | 총점 | 라우팅 | CompanyGuide | 리포트/컨센서스 입력 |
|---|---:|---:|---|---|---|
| 삼성전자 | Stage 1 | 49.2372 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | live 실행 | consensus 2, revision 1, report 22 |
| SK하이닉스 | Stage 1 | 55.7894 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | live 실행 | consensus 1, revision 0, report 20 |

이번 결과에서 중요한 점은, 둘 다 Stage 1로 나왔지만 예전처럼 `리포트/컨센서스가 비어서 0점`인 상태가 아니라는 것이다. CompanyGuide snapshot과 recent report는 실제로 들어왔다. 즉 이번 낮은 Stage는 "데이터 유입 실패"보다는 deterministic scoring gate가 아직 Stage 2 기준을 못 넘긴 결과다.

쉬운 예시:

- 예전 문제: 리포트를 못 찾아서 `research_reports=0`, `consensus=0`
- 이번 상태: 리포트와 컨센서스는 들어왔지만, EPS/FCF·실적가시성·계약 질·RPO/선수금 같은 확정 증거가 Stage 2 이상 점수로 충분히 전환되지 않음

## 소스 실행 상태

두 종목 모두 주요 live source는 정상 실행됐다.

| 소스 | 삼성전자 | SK하이닉스 |
|---|---|---|
| OpenDART | `live_executed` | `live_executed` |
| data.go.kr | `live_executed` | `live_executed` |
| NAVER Search | `live_executed` | `live_executed` |
| CompanyGuide | `live_executed` | `live_executed` |
| page fetch | `live` | `live` |

실제 호출 수:

| 종목 | NAVER queries | CompanyGuide calls | OpenDART logical | data.go.kr calls |
|---|---:|---:|---:|---:|
| 삼성전자 | 28 | 2 | 22 | 137 |
| SK하이닉스 | 26 | 2 | 22 | 137 |

`as_of_date=2026-06-11` 이후의 target evidence는 없었다. 즉 이번 산출물에서 삼성전자/SK하이닉스 target evidence 기준 미래 데이터 누수는 0건이다.

## 삼성전자 상세

### Stage

삼성전자는 `49.2372 / Stage 1`이다.

Stage reason:

`company-level event was present, but candidate score threshold was not met`

쉽게 말하면, 회사 단위 이벤트와 테마 전환은 잡혔지만 Stage 2 후보로 올릴 만큼 총점이 충분하지 않았다.

### 점수

| 축 | 점수 |
|---|---:|
| EPS/FCF | 1.4330 |
| 실적가시성 | 10.2666 |
| 병목/가격 | 16.7244 |
| 미스프라이싱 | 9.7872 |
| 밸류에이션 | 6.8904 |
| 자본정책 | 1.0000 |
| 정보신뢰 | 4.7500 |
| 리스크 패널티 | 0.0000 |
| 총점 | 49.2372 |

Stage 2 기준은 총점 65 이상이다. 삼성전자는 병목/가격 점수는 높지만 EPS/FCF가 1.4330으로 매우 낮고, 밸류에이션도 Stage 2 기준 7에 살짝 못 미친다.

### 입력 데이터

| 데이터 | 수량 |
|---|---:|
| price bars | 46 |
| financial actuals | 0 |
| consensus | 2 |
| consensus revisions | 1 |
| disclosures | 0 |
| research reports | 22 |
| news items | 6 |
| agent extracted fields | 23 |

CompanyGuide 유입은 정상이다.

- CompanyGuide snapshot: FY2026 EPS `43,833`, target price `437,500`
- CompanyGuide recent report: 미래에셋, 신한, NH, KB, 키움, 삼성, 메리츠, 현대차 등 2026-05-20부터 2026-06-11까지 다수 리포트 유입
- NAVER report proxy: 한화 리포트 기반 FY2026 EPS `5,721`, target price `110,000`도 별도 consensus proxy로 생성됨

주의할 점:

CompanyGuide snapshot과 NAVER report proxy의 숫자가 크게 충돌한다. 예를 들어 CompanyGuide target price는 `437,500`인데, NAVER report proxy는 `110,000`이다. 이 경우 운영 품질을 높이려면 CompanyGuide snapshot 같은 구조화 consensus의 우선순위를 높이고, 검색 snippet 기반 proxy는 낮은 신뢰로 쓰는 검토가 필요하다.

### LLM 확장

LLM 라우팅은 `transition_detected`, confidence `0.86`으로 끝났다.

라우팅:

- large sector: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical archetype: `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
- theme evidence gate: `source_backed`

확장 쿼리:

- theme expansion query 24개
- post-parse gap expansion 4개

실제 확장 예:

- `삼성전자 HBM4 양산 출하 고객 승인 장기공급계약 선수금 취소 조건 2026`
- `삼성전자 HBM 장기공급계약 선수금 수주잔고 RPO 취소 조건 사업보고서`
- `삼성전자 HBM CAPEX 패키징 CAPA 수율 투자 현금흐름 2026 사업보고서`
- `삼성전자 DS부문 HBM DDR5 서버 SSD 매출 비중 영업이익률 2026 리포트`

남은 missing slot:

- HBM 매출/출하/마진을 DS·DRAM·NAND·DX와 분리한 공식 증거
- HBM backlog/RPO/order book
- 고객명, 기간, take-or-pay, 선수금, 취소권, 패널티가 있는 계약 질 증거
- HBM 전용 CAPEX, 패키징 CAPA, 수율, FCF 영향
- 고객 인증 지연, 재고/가격 반전 같은 반대 증거

## SK하이닉스 상세

### Stage

SK하이닉스는 `55.7894 / Stage 1`이다.

Stage reason:

`company-level event was present, but candidate score threshold was not met`

쉽게 말하면, HBM 구조적 테마는 강하게 잡혔지만 Stage 2 총점 65에는 못 미쳤다.

### 점수

| 축 | 점수 |
|---|---:|
| EPS/FCF | 10.2000 |
| 실적가시성 | 8.8124 |
| 병목/가격 | 10.5944 |
| 미스프라이싱 | 9.9195 |
| 밸류에이션 | 10.4527 |
| 자본정책 | 1.5000 |
| 정보신뢰 | 4.7500 |
| 리스크 패널티 | 0.0000 |
| 총점 | 55.7894 |

SK하이닉스는 EPS/FCF와 밸류에이션은 삼성전자보다 낫지만, 실적가시성과 병목/가격 점수가 아직 Stage 2 총점까지 끌어올리지는 못했다.

### 입력 데이터

| 데이터 | 수량 |
|---|---:|
| price bars | 46 |
| financial actuals | 2 |
| consensus | 1 |
| consensus revisions | 0 |
| disclosures | 0 |
| research reports | 20 |
| news items | 4 |
| agent extracted fields | 23 |

CompanyGuide 유입은 정상이다.

- CompanyGuide snapshot: FY2026 EPS `301,732`, target price `2,751,667`
- data.go.kr actuals: 2024, 2025 연간 매출/영업이익/순이익 유입
- CompanyGuide recent report: 유진, 다올, 한국투자, 신한, NH, 미래에셋, KB, 키움, 삼성, 메리츠 등 다수 리포트 유입

대표 리포트:

- 한국투자: 목표주가 85% 상향, LTA가 가격 하방을 지지한다는 내용
- NH: 장기계약 안정성, 2분기 실적 흐름
- 미래에셋: 장기공급계약 확대와 HBM 고객 다변화
- 키움: 2Q26/3Q26 영업이익 전망 상향

### LLM 확장

LLM 라우팅은 `transition_detected`, confidence `0.87`로 끝났다.

라우팅:

- large sector: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical archetype: `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
- theme evidence gate: `source_backed`

확장 쿼리:

- theme expansion query 22개
- post-parse gap expansion 5개

실제 확장 예:

- `SK하이닉스 2026 Q1 earnings call transcript HBM long term agreement prepayment contract liability`
- `SK하이닉스 2025 사업보고서 계약부채 선수금 HBM 장기공급계약`
- `SK하이닉스 HBM long term supply agreement prepayment price floor cancellation terms 2026`
- `SK하이닉스 HBM 수주잔고 RPO 빅테크 장기계약 2026`

남은 missing slot:

- HBM 장기공급계약의 고객 범위, 기간, 가격 상하한, 취소 조건, 선수금 비율이 확인된 원문
- 계약부채/선수금 증가가 HBM 공급계약과 연결되는 사업보고서/분기보고서 주석
- 2026년 1분기 기준 HBM 매출 비중, OPM, CAPEX, FCF를 동시에 확인할 원문
- HBM4/HBM4E 고객 인증, allocation, CAPA가 매출/마진으로 연결되는 원문
- 삼성전자·마이크론 진입, 가격 협상 난항, 공급과잉 우려가 마진/계약 조건을 훼손하는 반대 증거

## 이번 실행에서 확인된 것

1. CompanyGuide 패치는 실제 운영 경로에서 작동했다.

삼성전자와 SK하이닉스 모두 `company_guide=live_executed`였고, `company_guide_snapshot_calls=1`, `company_guide_recent_report_calls=1`이 실행됐다.

2. 리포트/컨센서스는 이제 실제 feature input에 들어온다.

삼성전자는 consensus 2개, revision 1개, research report 22개가 들어왔다. SK하이닉스는 consensus 1개, research report 20개가 들어왔다.

3. LLM은 하드코딩 없이 C06 HBM 경로로 라우팅했다.

둘 다 `transition_detected`였고, route confidence는 삼성전자 0.86, SK하이닉스 0.87이었다. 확장 쿼리도 종목별 부족 슬롯을 기준으로 생성됐다.

4. 낮은 Stage의 원인은 수집 실패가 아니라 점수 전환/게이트 문제다.

특히 삼성전자는 CompanyGuide EPS와 target price가 들어왔는데도 EPS/FCF 점수가 1.4330에 그쳤다. SK하이닉스도 consensus와 다수 리포트가 들어왔지만 실적가시성/병목 점수가 Stage 2 총점까지는 못 올렸다.

## 운영상 추가 점검 필요

이번 실행은 패치가 작동함을 확인했지만, 다음 개선 포인트가 보인다.

1. 구조화 consensus와 검색 proxy 충돌 처리

삼성전자처럼 CompanyGuide snapshot과 NAVER report proxy 숫자가 크게 다르면, 검색 proxy가 구조화 consensus를 희석할 수 있다. 운영에서는 CompanyGuide snapshot을 우선하고, snippet/report proxy는 보조로 쓰는 신뢰 우선순위가 필요하다.

2. official actual coverage

삼성전자는 data.go.kr financial actual 호출은 있었지만 target feature에는 financial actuals가 0개였다. SK하이닉스는 2024/2025 actuals 2개가 들어왔다. 삼성전자 actual 매핑이 왜 비었는지는 별도 확인이 필요하다.

3. 리포트 수량과 점수 반영 간극

리포트가 20개 이상 들어와도 단순 수량만으로 Stage가 올라가지 않는다. 이것은 원칙상 맞다. 다만 리포트 안의 EPS 상향, target 상향, LTA, HBM 매출/OP 전망이 현재 점수 축으로 충분히 변환되는지는 추가 점검해야 한다.

4. 원문 증거 슬롯

LLM은 필요한 질문을 잘 확장했다. 하지만 Green/Stage 2 이상의 강한 승격에는 계약 원문, 사업보고서 주석, HBM 매출 비중, FCF 영향 같은 회사 기준 증거가 더 필요하다.

## 판단

이번 패치는 방향이 맞다. 이제 `리포트/컨센서스 proxy가 0이라 판단 불가`인 상태는 아니고, 실제 live 파이프라인에서 CompanyGuide 데이터가 들어간다.

다만 현재 점수 엔진은 리포트/컨센서스를 받은 뒤에도 매우 보수적으로 Stage를 준다. 쉽게 말하면:

- "HBM 테마와 리포트는 확인됨" -> 맞음
- "그래서 바로 Stage 2/3" -> 아직 아님
- "왜?" -> 공식 actual, 계약 질, RPO/선수금, HBM 전용 매출/마진/FCF 연결이 아직 점수로 충분히 확정되지 않음

다음 패치 후보는 데이터 수집이 아니라, 구조화 consensus 우선순위와 리포트 수치의 feature 변환 품질이다.
