# 2026-06-11 반도체 운영형 Stage 점검

## 목적

삼성전자(`005930`)와 SK하이닉스(`000660`)를 실제 운영 경로에 가깝게 다시 돌려서, 현재 점수와 Stage가 왜 그렇게 나왔는지 확인했다.

이번 점검은 다른 섹터/아키타입으로 확장하기 전에 C06 HBM/AI 메모리 경로가 어느 정도 동작하는지 보는 기준점이다.

## 2026-06-11 추가 패치 반영

사용자 지적:

`research report/consensus proxy가 0`이라고 바로 끝나는 것은 에이전트답지 않다. 그건 "증거가 없다"가 아니라 "아직 못 찾았을 수 있다"에 가깝다. 특히 `HBM 장기공급계약 물량, 기간, 선수금, 취소 조건, RPO/수주잔고`가 비어 있으면 LLM이 그 빈 슬롯을 보고 추가 검색해야 한다.

반영:

- 문서검토 후 `missing_information`과 `suggested_queries`를 실제 post-parse gap search로 실행하도록 패치했다.
- 검색어 내용은 LLM이 직접 판단한 `suggested_queries`만 사용한다.
- deterministic 코드는 누락 슬롯명이나 아키타입명을 보고 검색어 템플릿을 합성하지 않는다.
- deterministic 코드는 LLM query의 회사 범위, as-of 미래누수, 중복, 예산만 검증하고 실행한다.
- 리포트/컨센서스, 계약 질, RPO/수주잔고, 선수금, 물량, 기간, 취소 조건이 비면 LLM이 그 빈 곳을 보고 직접 다음 검색어를 내야 한다.

쉬운 예시:

- 예전: `삼성전자 consensus=0` -> 그대로 0점 축으로 남음
- 지금: `삼성전자 consensus=0` -> LLM이 현재 문서와 missing slot을 보고 `suggested_queries`를 직접 생성 -> deterministic 코드는 그 query를 검증/실행 -> 다시 파싱 -> 다시 LLM 검토

## 실행 조건

- 기준일: `2026-06-11`
- 실행 방식: 특정 종목 확인을 위해 targeted smoke 후보로 강제 투입
- 데이터 수집: `.env` 기반 live API 사용
- 검색/본문: NAVER Search API + live page fetch
- LLM 라우팅: Codex theme provider 사용
- fixture 모드: `False`
- theme rebalance: `True`
- max theme expansion rounds: `3`

주의:

targeted smoke는 종목을 강제로 검사하기 위한 운영형 검증 경로다. 가격, 재무, 공시, 뉴스, 페이지 fetch, LLM 라우팅, 점수화는 실제 경로를 탄다. 다만 production morning brief에는 targeted smoke 결과가 의도적으로 들어가지 않는다. 그래서 이 문서에서는 `targeted_smoke_results`와 evidence 산출물을 기준으로 판단한다.

## 산출물 위치

| 종목 | run log | evidence |
|---|---|---|
| 삼성전자 | `output/live_verify_005930_2026-06-11_operational_semis_final/korea_live_lite/2026-06-11_run_log.json` | `output/live_verify_005930_2026-06-11_operational_semis_final/korea_live_lite/2026-06-11_evidence.json` |
| SK하이닉스 | `output/live_verify_000660_2026-06-11_operational_semis_final/korea_live_lite/2026-06-11_run_log.json` | `output/live_verify_000660_2026-06-11_operational_semis_final/korea_live_lite/2026-06-11_evidence.json` |
| 통합 요약 | `output/operational_semis_final_summary_2026-06-11.json` | - |

## 현재 Stage 임계값

활성 scoring profile 기준이다.

| 구분 | 기준 |
|---|---:|
| Stage 2 총점 | 65.0 이상 |
| Stage 2 EPS/FCF | 10.0 이상 |
| Stage 2 밸류에이션 | 7.0 이상 |
| Stage 2 정보신뢰 | 3.0 이상 |
| Stage 3-Yellow 총점 | 75.0 이상 |
| Stage 3-Green 총점 | 87.0 이상 |
| Stage 3-Green EPS/FCF | 17.0 이상 |
| Stage 3-Green 실적가시성 | 15.0 이상 |
| Stage 3-Green 병목/가격 | 15.0 이상 |
| Stage 3-Green 미스프라이싱 | 10.0 이상 |
| Stage 3-Green 밸류에이션 | 10.0 이상 |
| Stage 3-Green revision score | 55.0 이상 |
| Stage 3-Green 구조적 가시성 | 45.0 이상 |

쉽게 말하면 Stage 2는 "후보로 볼 만하다"이고, Stage 3-Yellow는 "재평가 후보 점수는 충분하지만 Green 확정 조건 일부가 비어 있다"이다. Stage 3-Green은 총점뿐 아니라 revision, 계약 질, 구조적 가시성까지 같이 필요하다.

## 결과 요약

| 종목 | Stage | 총점 | 라우팅 | LLM 확장쿼리 | 핵심 차이 |
|---|---:|---:|---|---:|---|
| 삼성전자 | Stage 2 | 72.6211 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | 13개 | HBM/AI 메모리 증거는 잡혔지만 리포트/컨센서스 proxy가 0 |
| SK하이닉스 | Stage 3-Yellow | 80.7561 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | 11개 | 리포트 예상치와 consensus proxy가 들어와 Stage 3-Yellow까지 상승 |

두 종목 모두 LLM이 아키타입 전환/확장을 수행했다. 둘 다 `theme_route_status=transition_detected`, `theme_rebalance_status=completed`, `theme_evidence_gate_status=source_backed`로 끝났다.

## 삼성전자 상세

### 최종 판단

삼성전자는 `72.6211 / Stage 2`다.

Stage 2 이유:

- 총점 72.6211로 Stage 2 총점 65를 넘었다.
- EPS/FCF 20.0으로 Stage 2 기준 10을 넘었다.
- 밸류에이션 9.1882로 Stage 2 기준 7을 넘었다.
- 정보신뢰 3.0으로 Stage 2 기준 3을 충족했다.

Stage 3-Yellow가 아닌 이유:

- Stage 3-Yellow 총점 기준 75에 못 미친다.
- 현재 총점은 72.6211이라 약 2.38점 부족하다.

Stage 3-Green이 아닌 이유:

- Green 총점 87에 크게 부족하다.
- 실적가시성 13.4551이 Green 기준 15보다 낮다.
- 병목/가격 13.0609가 Green 기준 15보다 낮다.
- 밸류에이션 9.1882가 Green 기준 10보다 낮다.
- consensus와 consensus revision이 모두 0이다.
- 회사 기준 HBM 매출 비중, 장기공급계약/선수금/RPO, HBM4 고객 승인과 양산 매출 인식 근거가 아직 부족하다.

### 점수 구성

| 축 | 점수 |
|---|---:|
| EPS/FCF | 20.0000 |
| 실적가시성 | 13.4551 |
| 병목/가격 | 13.0609 |
| 미스프라이싱 | 10.7165 |
| 밸류에이션 | 9.1882 |
| 자본정책 | 1.2727 |
| 정보신뢰 | 3.0000 |
| 리스크 패널티 | 0.0000 |
| 총점 | 72.6211 |

### 입력 데이터 카운트

| 데이터 | 수량 |
|---|---:|
| price bars | 29 |
| financial actuals | 5 |
| disclosures | 6 |
| news items | 5 |
| research reports | 0 |
| consensus | 0 |
| consensus revisions | 0 |
| agent extracted fields | 17 |

### 실제 잡힌 핵심 evidence

- `대신증권 "삼성전자, HBM·DRAM 겹호재… 목표가 유지"`
- `삼성전자 2026년 실적 기대감 커져…170조 원 전망도 나와`
- `[컨콜] 삼성전자 "2분기 HBM4E 첫 샘플 공급"..AI 메모리 초격차 속도전`
- `엔비디아 차이나 공백… 삼성·SK HBM 전선 '숨은 변수'`

해석:

삼성전자는 HBM, DRAM, HBM4E, AI 메모리 샘플 공급 같은 방향성은 잡혔다. 하지만 리포트가 `research_report`로 구조화되지 않았고, forward estimate가 consensus proxy로 전환되지 않았다. 그래서 "테마와 방향은 있다"는 점수는 받았지만, "Green 확정"에 필요한 수치화된 계약/추정치/가시성 증거는 부족했다.

예시로 보면:

- `HBM4E 샘플 공급`은 긍정 증거다.
- 하지만 `고객 승인 완료 + 다년 공급계약 + 2026년 HBM 매출 비중 + OPM/FCF 영향`까지 있어야 Green 쪽으로 간다.

### LLM 확장 쿼리

LLM은 다음 같은 쿼리로 꼬리를 물고 확장했다.

- `삼성전자 HBM 매출 비중 2026 삼성전자 공식 실적 발표`
- `삼성전자 HBM 장기 공급 계약 선수금 고객 승인 2026`
- `삼성전자 HBM4 양산 출하 매출 마진 EPS 영향`
- `삼성전자 AI 데이터센터 반도체 수주잔고 RPO CAPEX`
- `삼성전자 DS부문 HBM DDR5 서버 SSD 매출 성장 2026`
- `삼성전자 수주잔고 RPO HBM 공급계약 2026 사업보고서`
- `삼성전자 AI 메모리 HBM FCF 현금흐름 전망 2026`

결론:

LLM이 확장을 안 한 것은 아니다. 확장은 했지만, 현재 수집된 근거가 회사 단위 계약 질과 수치 연결까지 충분히 닿지 못했다.

## SK하이닉스 상세

### 최종 판단

SK하이닉스는 `80.7561 / Stage 3-Yellow`다.

Stage 3-Yellow 이유:

- 총점 80.7561로 Stage 3-Yellow 기준 75를 넘었다.
- EPS/FCF 20.0으로 Green 기준 17도 넘었다.
- 병목/가격 15.6202로 Green 기준 15를 넘었다.
- 미스프라이싱 12.3928로 Green 기준 10을 넘었다.
- 밸류에이션 11.6826으로 Green 기준 10을 넘었다.
- 리포트 예상치가 `consensus:000660:2026-06-11:2026` proxy로 들어왔다.

Stage 3-Green이 아닌 이유:

- Green 총점 기준 87에 못 미친다.
- 실적가시성 13.6547이 Green 기준 15보다 낮다.
- consensus는 1개 생겼지만 consensus revision은 0이다.
- Green revision score 기준 55를 채우기 어렵다.
- HBM 장기공급계약의 확정 물량, 기간, 선수금, 취소 조건, RPO/수주잔고 같은 회사 기준 지표가 아직 비어 있다.

### 점수 구성

| 축 | 점수 |
|---|---:|
| EPS/FCF | 20.0000 |
| 실적가시성 | 13.6547 |
| 병목/가격 | 15.6202 |
| 미스프라이싱 | 12.3928 |
| 밸류에이션 | 11.6826 |
| 자본정책 | 1.6757 |
| 정보신뢰 | 4.5000 |
| 리스크 패널티 | 0.0000 |
| 총점 | 80.7561 |

### 입력 데이터 카운트

| 데이터 | 수량 |
|---|---:|
| price bars | 29 |
| financial actuals | 5 |
| disclosures | 6 |
| news items | 5 |
| research reports | 1 |
| consensus | 1 |
| consensus revisions | 0 |
| agent extracted fields | 16 |

### 실제 잡힌 핵심 evidence

- `SK하이닉스 종목분석 - 2Q26 영업이익 70조원 예상`
- `Consensus FY2026`
- `SK하이닉스, '다년 LTA'로 계약 구조 재편…공급자 우위 시장 진입`
- `범용 디램 HBM 수익성 추월...메모리 빅2, 다른 대응 주목`
- `SK하이닉스, 분기·연간 역대 '최고 실적' 경신…HBM으로 새 역사`

해석:

하이닉스는 삼성전자와 달리 `research_report`가 잡혔고, 여기서 forward estimate가 consensus proxy로 들어갔다. 이 차이가 정보신뢰, 밸류에이션, 미스프라이싱 쪽을 더 밀어 올렸다.

예시로 보면:

- 삼성전자: "HBM 좋다, 샘플 공급, DRAM 겹호재" 중심
- 하이닉스: "HBM 다년 LTA, 리포트 예상치, consensus proxy"까지 들어옴

그래서 하이닉스가 Stage 3-Yellow까지 올라갔다.

### LLM 확장 쿼리

LLM은 다음 같은 쿼리로 확장했다.

- `SK하이닉스 HBM 장기공급계약 선수금 고객 물량 2026`
- `SK하이닉스 HBM 매출 비중 영업이익률 FCF 2026`
- `SK하이닉스 CAPA 증설 HBM TSV 패키징 투자 2026`
- `SK하이닉스 AI 서버 메모리 수요 둔화 고객 주문 축소 2026`
- `SK하이닉스 수주잔고 RPO backlog HBM contract`
- `SK하이닉스 2026 1분기 실적발표 컨퍼런스콜 HBM 다년 LTA 물량 확보`
- `SK하이닉스 HBM 매출 비중 영업이익률 FCF CAPEX 2026`

결론:

LLM이 단순히 HBM 키워드만 보고 멈춘 것이 아니라, 계약 물량, 선수금, FCF, CAPEX, RPO, 고객 주문 축소 위험까지 같이 확인하려고 확장했다. 다만 Green에 필요한 확정 계약 질과 회사 기준 정량 지표가 아직 충분하지 않았다.

## 두 종목 차이

| 항목 | 삼성전자 | SK하이닉스 |
|---|---:|---:|
| 총점 | 72.6211 | 80.7561 |
| Stage | 2 | 3-Yellow |
| research report | 0 | 1 |
| consensus proxy | 0 | 1 |
| consensus revisions | 0 | 0 |
| 실적가시성 | 13.4551 | 13.6547 |
| 병목/가격 | 13.0609 | 15.6202 |
| 미스프라이싱 | 10.7165 | 12.3928 |
| 밸류에이션 | 9.1882 | 11.6826 |
| 정보신뢰 | 3.0000 | 4.5000 |
| LLM 확장쿼리 | 13 | 11 |

가장 큰 차이는 하이닉스는 리포트 예상치가 구조화되어 consensus proxy까지 들어갔다는 점이다. 삼성전자는 뉴스성 evidence는 충분히 있었지만 리포트/컨센서스 축이 비어 있었다.

## 운영 소스 상태

두 실행 모두 실제 소스가 동작했다.

| 종목 | data.go.kr | OpenDART | NAVER Search | page fetch |
|---|---:|---:|---:|---|
| 삼성전자 | 91 HTTP | 58 HTTP | 57 HTTP | live |
| SK하이닉스 | 91 HTTP | 58 HTTP | 51 HTTP | live |

source mode는 둘 다 다음과 같았다.

- `data_go_kr=live_executed`
- `opendart=live_executed`
- `naver_search=live_executed`
- `page_fetch=live`
- `krx=request_only`
- `krx_openapi=disabled_optional`
- `stock_issuance=disabled_optional`

## 확장 전 체크포인트

다른 아키타입으로 확장하기 전에 확인할 점은 다음이다.

1. 리포트 recall

삼성전자는 증권사 관련 뉴스는 잡혔지만 `research_report`로 구조화된 항목은 0이었다. 다른 섹터에서도 "증권사 기사"와 "실제 리포트/forward estimate"가 구분되어 들어오는지 확인해야 한다.

2. consensus revision

하이닉스도 consensus proxy는 생겼지만 revision은 0이었다. Green까지 가려면 `목표주가 기존 X에서 Y`, `EPS/OP 추정치 상향률`, `컨센서스 상향률` 같은 변화율 row가 더 중요하다.

3. 계약 질/RPO

C06 HBM 아키타입에서는 단순 수요 뉴스보다 `장기공급계약`, `선수금`, `확정 물량`, `고객 승인`, `수주잔고/RPO`, `취소 조건`이 Green 판단에 더 중요하다. 전력장비, 방산, 조선, 원전 등 수주형 아키타입으로 확장할 때도 같은 구조를 봐야 한다.

4. Stage 3-Green은 보수적으로 유지됨

현재 로직은 호재성 뉴스만으로 Green을 주지 않는다. 예를 들어 "HBM 좋다"는 Stage 2나 Yellow까지는 밀 수 있지만, "HBM 매출 비중 + 마진 + 계약 물량 + revision"이 없으면 Green은 막힌다.

## 결론

현재 반도체 C06 경로는 운영형으로 동작한다.

- LLM은 두 종목 모두 아키타입 전환을 `C06_HBM_MEMORY_CUSTOMER_CAPACITY`로 잡았다.
- 확장검색도 실제로 돌았다.
- 하이닉스는 리포트 예상치가 consensus proxy로 연결됐다.
- 삼성전자는 evidence는 잡혔지만 리포트/컨센서스 축이 비어 Stage 2에 머물렀다.
- 하이닉스는 총점이 충분해 Stage 3-Yellow까지 갔지만, Green 총점/visibility/revision/계약 질이 부족했다.

따라서 다음 확장 작업은 "Green을 쉽게 주기"가 아니라, 다른 아키타입에서도 리포트/계약/수주/정량 revision이 같은 방식으로 잘 들어오는지 확인하는 쪽이 맞다.

## 패치 후 재실행 검증

### 실행 산출물

data.go.kr 가격 페이지가 live 응답 대기에서 멈추는 현상이 재현됐다. 그래서 이번 재검증은 `DATA_GO_KR_SERVICE_KEY`만 끄고 실행했다. NAVER Search, page fetch, OpenDART, Codex LLM route provider는 그대로 사용했다.

이 재실행 점수는 price bars, financial actuals, disclosures가 빠져서 위의 full-data 운영 점수와 직접 비교하면 안 된다. 비교해야 할 것은 `post_parse_gap_expansion_count`, `research_reports`, `consensus`, 추가 검색어다.

| 종목 | run log | evidence |
|---|---|---|
| 삼성전자 | `output/live_verify_005930_2026-06-11_operational_semis_gap_patch_no_datago/korea_live_lite/2026-06-11_run_log.json` | `output/live_verify_005930_2026-06-11_operational_semis_gap_patch_no_datago/korea_live_lite/2026-06-11_evidence.json` |
| SK하이닉스 | `output/live_verify_000660_2026-06-11_operational_semis_gap_patch_no_datago/korea_live_lite/2026-06-11_run_log.json` | `output/live_verify_000660_2026-06-11_operational_semis_gap_patch_no_datago/korea_live_lite/2026-06-11_evidence.json` |
| 요약 | `output/operational_semis_gap_patch_no_datago_summary_2026-06-11.json` | - |

### 핵심 결과

| 항목 | 삼성전자 패치 전 full-data | 삼성전자 패치 후 gap 검증 | SK하이닉스 패치 전 full-data | SK하이닉스 패치 후 gap 검증 |
|---|---:|---:|---:|---:|
| Stage | 2 | 1 | 3-Yellow | 1 |
| 총점 | 72.6211 | 28.6871 | 80.7561 | 37.5758 |
| price bars | 29 | 0 | 29 | 0 |
| financial actuals | 5 | 0 | 5 | 0 |
| disclosures | 6 | 0 | 6 | 0 |
| research reports | 0 | 2 | 1 | 1 |
| consensus | 0 | 1 | 1 | 1 |
| agent fields | 17 | 23 | 16 | 28 |
| LLM 확장쿼리 | 13 | 24 | 11 | 24 |
| post-parse gap 확장 | 없음 | 4 | 없음 | 6 |

해석:

- 삼성전자는 원래 `research_reports=0`, `consensus=0`이었다.
- 패치 후에는 누락 슬롯을 보고 추가 검색을 실행해서 `research_reports=2`, `consensus=1`까지 들어왔다.
- SK하이닉스는 원래도 `research_reports=1`, `consensus=1`이었지만, 패치 후 계약/RPO/선수금 쪽 누락 슬롯 때문에 post-gap 검색이 6개 더 실행됐다.
- 재실행 Stage가 1로 낮은 것은 data.go를 꺼서 가격/재무/공시 입력이 0이기 때문이다. 패치 품질 판단에는 이 점수를 쓰지 않는다.

### 실제 추가 검색 예시

삼성전자:

- `삼성전자 HBM EPS FCF 컨센서스 상향 브로커 리포트 2026년 6월 이전`
- `삼성전자 HBM 수주잔고 RPO backlog 고객 주문 공식 공시 IR earnings call`
- `삼성전자 장기공급계약 선수금 수주잔고 RPO`

SK하이닉스:

- `SK하이닉스 2026 EPS FCF revision consensus broker report 목표주가 상향 근거`
- `SK하이닉스 HBM 수주잔고 RPO 고객 예약 물량 CAPA full booking IR 실적발표`
- `SK하이닉스 장기공급계약 선수금 수주잔고 RPO`
- `SK하이닉스 컨퍼런스콜 장기공급계약 물량 기간 취소 조건`

이제 "없다"와 "아직 못 찾았다"를 구분한다. 파서가 못 찾은 슬롯은 LLM이 직접 검색어로 확장하고, 새 문서가 들어오면 다시 파싱/검토한다. deterministic 템플릿으로 검색어를 만들어내지는 않는다.

### 남은 한계

추가 검색 후에도 Green을 바로 주지는 않는다. 예를 들어 하이닉스에서 `LTA`, `RPO`, `선수금`을 검색했지만, LLM 검토 결과는 여전히 다음을 missing으로 남겼다.

- SK하이닉스 자체 HBM 수주잔고/RPO 또는 예약 물량 수치
- SK하이닉스 계약 기간, 수량, 취소조건, 선수금 조건
- HBM 증설, TSV 패키징, 감가상각, FCF 영향의 회사별 근거

즉 검색은 더 깊어졌지만, source-backed evidence가 없으면 Green 조건으로 쓰지 않는 안전장치는 유지된다.

### data.go 지연 방어

이번 운영 재실행에서 data.go.kr 가격 페이지가 `timeout_seconds`를 줬는데도 SSL read에서 오래 대기하는 현상이 있었다. 그래서 `HttpClient`에 Unix hard timeout 방어를 추가했다.

쉬운 예시:

- 예전: data.go 한 요청이 응답을 안 주면 전체 종목 검증이 멈출 수 있음
- 지금: hard timeout이 발생하면 해당 요청은 실패로 기록되고 파이프라인은 fallback/다음 단계로 진행할 수 있음
