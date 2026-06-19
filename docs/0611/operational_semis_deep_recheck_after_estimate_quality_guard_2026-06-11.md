# 2026-06-11 삼성전자/SK하이닉스 운영형 deep 재검증

## 목적

추정치 proxy 품질 방어 패치 이후, 실제 운영에 가깝게 삼성전자와 SK하이닉스를 다시 돌려서 다음을 확인했다.

- LLM route provider가 단순 초기 검색에서 멈추지 않고 부족 슬롯을 보고 추가 검색을 만드는지
- CompanyGuide, Naver, OpenDART, data.go.kr, page fetch가 실제 live 경로로 연결되는지
- 검색 리포트 proxy가 구조화 컨센서스를 잘못 덮어쓰지 않는지
- 최종 Stage는 LLM이 아니라 deterministic scorer/stage machine이 계산하는지
- `as_of_date=2026-06-11` 이후 데이터가 target evidence에 섞이지 않는지

## 실행 조건

- `as_of_date`: 2026-06-11
- LLM provider: `E2R_THEME_ROUTE_PROVIDER=codex`
- theme rebalance: enabled
- max theme expansion rounds: 3
- CompanyGuide: enabled
- page fetch: enabled
- deep research symbol budget: 1
- 결과 요약: `output/operational_recheck_deep_after_estimate_quality_guard_summary_2026-06-11.json`
- 삼성전자 run log: `output/live_verify_005930_2026-06-11_operational_recheck_deep_after_estimate_quality_guard/korea_live_lite/2026-06-11_run_log.json`
- SK하이닉스 run log: `output/live_verify_000660_2026-06-11_operational_recheck_deep_after_estimate_quality_guard/korea_live_lite/2026-06-11_run_log.json`

위 산출물은 점수와 evidence 연결을 확인한 뒤 커밋 전 실행 캐시/임시 output 정리 대상에서 제거했다. 재현은 같은 실행 조건으로 다시 돌리면 된다.

처음에는 deep budget을 0으로 둔 실행도 있었지만, 그 경우 `deep_research_symbol_budget_exhausted`로 LLM 확장이 실제로 돌지 않았다. 따라서 운영형 검증에는 부적합하다고 보고 deep budget 1로 다시 실행했다.

## 핵심 결과

| 종목 | Stage | 총점 | route | LLM 확장 | gap 확장 | 핵심 추정치 출처 | Green 미달 이유 |
| --- | --- | ---: | --- | ---: | ---: | --- | --- |
| 삼성전자 | 3-Yellow | 80.1102 | mixed_route | 22 | 5 | CompanyGuide snapshot | 총점 87 미만, 실적가시성/병목 점수 Green 문턱 미달, backlog/RPO/FCF/CAPEX 연결 증거 부족 |
| SK하이닉스 | 3-Yellow | 83.0245 | transition_detected | 23 | 4 | CompanyGuide snapshot + report_proxy OP | 총점 87 미만, revision/FCF 출처 부재, backlog/RPO/FCF/direct AI infra revenue bridge 부족 |

쉬운 예:

- "HBM이 좋다", "AI 메모리 수요가 강하다"는 Yellow까지는 밀어줄 수 있다.
- Green은 더 엄격하다. 예를 들어 "장기 공급 물량, 기간, 선수금, 취소 조건, RPO/수주잔고, FCF 연결"처럼 회사 실적과 현금흐름으로 잠기는 증거가 더 필요하다.

## 삼성전자 점수

| 항목 | 점수 |
| --- | ---: |
| EPS/FCF | 20.0000 |
| 실적가시성 | 13.6525 |
| 병목/가격 | 13.4809 |
| 미스프라이싱 | 12.6030 |
| 밸류에이션 | 12.1882 |
| 자본정책 | 2.0183 |
| 정보신뢰 | 5.0000 |
| 리스크 패널티 | 0.0000 |
| 총점 | 80.1102 |

입력 데이터 수:

- price bars 52
- financial actuals 5
- disclosures 13
- research reports 20
- consensus 1
- consensus revisions 0
- news 4
- agent extracted fields 25

추정치 품질:

- EPS 대표값: `company_guide_snapshot`, quality 90
- 목표가 대표값: `company_guide_snapshot`
- OP/FCF/revision 대표값: 없음
- proxy 충돌/격리: 0

LLM이 실제로 확장한 query 예:

- `삼성전자 2026 1분기 실적 발표 DS HBM DDR5 서버 SSD 매출 마진 컨퍼런스콜`
- `삼성전자 2026 1Q earnings call HBM customer qualification capacity ASP margin`
- `삼성전자 HBM4 HBM4E 양산 출하 고객 인증 공급 물량 2026`
- `삼성전자 HBM 장기공급계약 선수금 고객 할당 취소 조건 2026`
- `삼성전자 반도체 수주잔고 파운드리 AI accelerator backlog 2026 IR`
- `삼성전자 CAPEX HBM 생산능력 증설 FCF 2026`

## SK하이닉스 점수

| 항목 | 점수 |
| --- | ---: |
| EPS/FCF | 20.0000 |
| 실적가시성 | 14.0403 |
| 병목/가격 | 16.7702 |
| 미스프라이싱 | 11.9811 |
| 밸류에이션 | 11.7118 |
| 자본정책 | 2.5000 |
| 정보신뢰 | 5.0000 |
| 리스크 패널티 | 0.0000 |
| 총점 | 83.0245 |

입력 데이터 수:

- price bars 53
- financial actuals 5
- disclosures 9
- research reports 21
- consensus 2
- consensus revisions 0
- news 7
- agent extracted fields 28

추정치 품질:

- EPS 대표값: `company_guide_snapshot`, quality 90
- 목표가 대표값: `company_guide_snapshot`
- OP 대표값: `report_proxy`
- FCF/revision 대표값: 없음
- proxy 충돌 1, proxy 격리 1

여기서 중요한 점은 report proxy가 무조건 배제된 것이 아니다. 구조화 컨센서스가 없는 OP 같은 항목에는 보조로 쓸 수 있다. 다만 CompanyGuide와 크게 충돌하는 EPS/목표가 같은 항목은 낮은 품질 proxy가 대표값을 빼앗지 못한다.

LLM이 실제로 확장한 query 예:

- `SK하이닉스 2026 1Q earnings call transcript HBM revenue mix capacity customer allocation cancellation terms`
- `SK하이닉스 2026년 1분기 실적발표 자료 HBM 매출 비중 영업이익률 FCF CAPEX`
- `SK하이닉스 HBM 장기공급계약 선수금 물량 배정 취소 조건 고객 2026`
- `SK하이닉스 HBM4 HBM3E CAPA TSV 패키징 생산능력 증설 고객 인증 2026`
- `SK하이닉스 AI 메모리 DRAM NAND 가격 상승 2026 영업이익률 현금흐름 리포트`
- `SK하이닉스 SO-CAMM 메모리 탑재량 둔화 HBM 수요 리스크 2026 리포트`

## 출처 연결 상태

| source | 삼성전자 | SK하이닉스 |
| --- | --- | --- |
| CompanyGuide | live_executed | live_executed |
| data.go.kr | live_executed | live_executed |
| OpenDART | live_executed | live_executed |
| Naver search | live_executed | live_executed |
| page fetch | live | live |
| KRX | request_only | request_only |
| KRX OpenAPI | disabled_optional | disabled_optional |
| stock issuance | disabled_optional | disabled_optional |

`KRX=request_only`는 치명적 fallback이 아니다. 이번 실행에서는 가격/상장 정보가 data.go.kr live 경로로 들어왔고, KRX는 요청 가능한 소스로 기록만 된 상태다.

## 파생 문제 확인

통과:

- 관련 단위테스트 41개 통과
- `git diff --check` 통과
- 삼성전자 target evidence 미래날짜 누수 0건
- SK하이닉스 target evidence 미래날짜 누수 0건
- 두 종목 모두 `fallback_reasons={}`로 live 실행 완료

전체 테스트:

- `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3710개 중 3709개 통과, 1개 실패

실패한 테스트:

- `test_real_generated_md_files_are_discovered_and_prompt_sections_do_not_exclude_results`
- 원인: 현재 워킹트리에서 `docs/round` 최상위 연구 md가 0개이고, `docs/round/achieve` 아래에는 1778개가 있다.
- 이 실패는 이번 추정치 품질/LLM 확장 패치의 로직 실패가 아니라, 연구 파일이 achieve 쪽으로 이동/정리된 현재 데이터 배치 상태 때문이다.

운영 영향:

- live stage 산정 경로에는 직접 장애가 없다.
- 다만 `docs/round` 최상위 md를 기대하는 calibration/goal 계열 테스트나 작업은 현재 상태 그대로면 실패할 수 있다. goal 계열을 돌릴 때는 achieve archive를 포함하도록 discovery 설정을 바꾸거나, 입력 연구 md 위치를 다시 맞춰야 한다.

## 지연 영향

예상되는 지연은 있다. 이유는 LLM provider와 page fetch가 추가됐기 때문이다.

- 기존: 초기 검색 결과를 파싱하고 deterministic scorer로 바로 계산
- 변경 후: LLM이 route를 판단하고, 부족 슬롯별 suggested query를 더 만들고, page fetch로 본문을 더 확인

이번 실행 기준:

- 삼성전자: Naver query 28개, live request 352개
- SK하이닉스: Naver query 29개, live request 97개

쉬운 예:

- 예전에는 "HBM 뉴스가 있네"에서 멈추기 쉬웠다.
- 지금은 "HBM 뉴스는 있는데 계약 물량/RPO/FCF가 없네. 그럼 컨콜, IR, 장기공급계약, CAPEX/FCF를 더 찾아보자"로 한 단계 더 간다.

그래서 속도는 느려질 수 있지만, 초반 cheap scan에서 걸러진 소수 종목에 deep research를 쓰는 구조라면 의도한 지연이다. 대량 종목에 무제한으로 적용하면 지연과 API 사용량이 커지므로 budget이 반드시 필요하다.

## 결론

이번 패치는 "모르면 기본점수/fallback으로 간다"가 아니라 "모르면 LLM이 부족한 증거를 판단해 추가 검색하고, 그래도 source-backed 증거가 부족하면 Green까지 올리지 않는다"로 바뀐 것이다.

삼성전자와 SK하이닉스는 둘 다 AI/HBM 모멘텀과 실적 기대가 확인되어 3-Yellow까지 올라왔다. 하지만 Green은 계약 잠김, 수주잔고/RPO, FCF 연결, revision 품질 같은 더 강한 증거가 부족해서 막혔다. 이는 보수적이지만, 현재 E2R 원칙에는 맞는 결과다.
