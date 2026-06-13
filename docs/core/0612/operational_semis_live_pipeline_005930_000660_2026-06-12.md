# 2026-06-12 삼성전자/SK하이닉스 운영형 파이프라인 재실행 기록

## 결론

2026-06-12 기준으로 삼성전자(`005930`)와 SK하이닉스(`000660`)를 실제 live 경로로 다시 실행했다.

최종 기준은 `v6` 실행이다.

- 출력 루트: `output/live_operational_semis_2026-06-12_after_corp_code_scoregap_patch_v6`
- cache 루트: `output/live_operational_semis_2026-06-12_after_corp_code_patch_v5_cache`

이번에 확인된 병목 두 개를 패치했다.

1. OpenDART 공식 재무 actual이 최근 공시의 `corp_code`에만 의존하던 문제
2. post-score-gap LLM provider 실패가 이미 계산된 점수까지 숨기던 문제

쉽게 말하면, 예전에는 "회사 고유번호를 못 찾으면 재무제표를 못 부르고, 추가 LLM 검토가 실패하면 점수표도 가린다"였다. 지금은 "OpenDART 공식 회사코드 맵으로 고유번호를 찾고, 추가 검토가 실패해도 이미 계산된 점수는 보여주며 warning으로 남긴다"가 됐다.

## 최종 결과

| 종목 | Stage | visible score | score valid | score block | score-gap warning |
|---|---:|---:|---:|---|---|
| 삼성전자 `005930` | `3-Yellow` | `78.2095` | `True` | `None` | `score_gap_round_limit` |
| SK하이닉스 `000660` | `3-Yellow` | `78.8551` | `True` | `None` | `score_gap_no_progress` |

주의: 이 문서는 투자 권고가 아니라 파이프라인 상태 기록이다. Stage는 모니터링 상태이고, 직접적인 매수/매도 지시가 아니다.

## 실행 조건

| 항목 | 값 |
|---|---|
| `as_of_date` | `2026-06-12` |
| `fixture_mode` | `False` |
| `live_enabled` | `True` |
| 대상 제한 | `targeted_smoke_enabled=True`, `targeted_smoke_only=True` |
| 검색/API | `.env`의 OPENDART, DATA_GO_KR, NAVER, CompanyGuide 경로 사용 |
| LLM provider | Codex theme route provider |
| page fetch | live page fetch |
| LLM 입력 제한 | search result 80건, document 32건 |
| score-gap 확장 | 최대 2라운드 |

## 패치 내용

### 1. OpenDART corp code 매핑

기존:

```text
OpenDART date-range disclosure 수집
-> 그 안에 해당 종목 corp_code가 있으면 재무제표 API 호출
-> 최근 공시가 없거나 target 종목 공시가 없으면 financial_actuals=0
```

변경:

```text
OpenDART date-range disclosure에서 corp_code 먼저 확인
-> 없으면 OpenDART corpCode.xml zip을 1회 다운로드
-> stock_code -> corp_code 공식 매핑 생성
-> fnlttSinglAcntAll 재무제표 API 호출
```

예를 들어 삼성전자는 `005930 -> 00126380`, SK하이닉스는 `000660 -> 00164779`로 매핑됐다. 이 값은 종목명 하드코딩이 아니라 OpenDART 공식 `corpCode.xml`에서 파싱한 결과다.

### 2. binary HTTP/cache

OpenDART `corpCode.xml`은 이름은 XML이지만 실제 응답은 zip이다. 그래서 기존 text/json HTTP 경로로는 안정적으로 처리할 수 없었다.

변경:

- `HttpClient.get_bytes()` 추가
- bytes cache read/write 추가
- OpenDART corpCode zip/XML 파서 추가

쉽게 말하면, 재무제표를 부르기 위한 "회사 주민번호표"가 압축파일로 오는데, 이제 그 압축파일을 제대로 읽는다.

### 3. score-gap provider error

v5 운영형 실행에서 삼성전자는 다음 상태가 재현됐다.

```text
financial_actuals=5
score_gap 전 score=78.2095
-> post-score-gap LLM provider_error
-> score_valid=False
-> visible_score=None
```

이건 점수 계산 실패가 아니라 추가 정밀검토 LLM 실패다. 그래서 `provider_error`와 `invalid_provider_output`은 post-score-gap 단계에서는 hard block이 아니라 warning으로 낮췄다.

단, 초기 theme route provider error는 여전히 hard block이다. 예를 들어 종목이 어떤 섹터/아키타입인지 아예 못 잡은 상태라면 점수를 막는다. 반대로 이미 route와 기본 점수가 계산된 뒤 추가 gap 검색 LLM이 실패하면 점수는 유지하고 warning만 남긴다.

## 점수 구성

### 삼성전자 `005930`

| 항목 | 점수 |
|---|---:|
| EPS/FCF | `20.0` |
| 실적가시성 | `11.7117` |
| 병목/가격 | `13.0751` |
| 미스프라이싱 | `13.3752` |
| 밸류에이션 | `12.8889` |
| 자본정책 | `2.0183` |
| 정보신뢰 | `4.75` |
| 리스크 차감 | `0.56` |
| 총점 | `78.2095` |

Stage는 `3-Yellow`다. EPS/FCF, 병목/가격, 미스프라이싱은 강하게 잡혔지만, score-gap round limit warning이 남아 Green까지 확정되지는 않았다.

### SK하이닉스 `000660`

| 항목 | 점수 |
|---|---:|
| EPS/FCF | `20.0` |
| 실적가시성 | `13.4017` |
| 병목/가격 | `13.0607` |
| 미스프라이싱 | `12.8255` |
| 밸류에이션 | `12.0566` |
| 자본정책 | `1.4435` |
| 정보신뢰 | `4.75` |
| 리스크 차감 | `0.0` |
| 총점 | `78.8551` |

Stage는 `3-Yellow`다. score-gap 추가 검색까지 수행됐고, 남은 gap 상태가 반복되어 `score_gap_no_progress` warning으로 종료됐다.

## 입력 증거 수

| 종목 | price bars | financial actuals | research reports | news items | consensus | consensus revisions | agent fields |
|---|---:|---:|---:|---:|---:|---:|---:|
| 삼성전자 | 247 | 5 | 20 | 22 | 1 | 0 | 24 |
| SK하이닉스 | 247 | 5 | 23 | 33 | 3 | 1 | 17 |

이전 v4의 `financial_actuals=0` 병목은 v6에서 해소됐다.

## Source 호출 요약

| 종목 | data.go.kr | OpenDART corpCode | OpenDART financial | OpenDART detail | Naver queries | CompanyGuide |
|---|---:|---:|---:|---:|---:|---:|
| 삼성전자 | 4 | 1 | 5 | 87 | 39 | 2 |
| SK하이닉스 | 4 | 1 | 5 | 87 | 29 | 2 |

`OpenDART financial=5`는 2026년 1분기, 2025년 1분기, 2025년 연간, 2024년 연간, 2023년 연간 요청이다.

## Phase Log 요약

| 종목 | phase rows | score-gap 시작 score | score-gap queries | 최종 stop |
|---|---:|---:|---:|---|
| 삼성전자 | 21 | `81.1848` | 10 | `post_score_gap_stop_round_limit` |
| SK하이닉스 | 16 | `78.8551` | 8 | `post_score_gap_stop_no_progress` |

삼성전자는 score-gap 검색 후 최종 visible score가 `78.2095`로 정리됐다. SK하이닉스는 score-gap 검색 후에도 같은 gap signature가 반복되어 warning으로 종료됐다.

## 산출 파일

요약:

- `output/live_operational_semis_2026-06-12_after_corp_code_scoregap_patch_v6/summary_after_corp_code_scoregap_patch_v6.json`

삼성전자:

- `output/live_operational_semis_2026-06-12_after_corp_code_scoregap_patch_v6/005930/korea_live_lite/2026-06-12_run_log.json`
- `output/live_operational_semis_2026-06-12_after_corp_code_scoregap_patch_v6/005930/korea_live_lite/2026-06-12_phase_log.jsonl`
- `output/live_operational_semis_2026-06-12_after_corp_code_scoregap_patch_v6/005930/korea_live_lite/2026-06-12_evidence.json`

SK하이닉스:

- `output/live_operational_semis_2026-06-12_after_corp_code_scoregap_patch_v6/000660/korea_live_lite/2026-06-12_run_log.json`
- `output/live_operational_semis_2026-06-12_after_corp_code_scoregap_patch_v6/000660/korea_live_lite/2026-06-12_phase_log.jsonl`
- `output/live_operational_semis_2026-06-12_after_corp_code_scoregap_patch_v6/000660/korea_live_lite/2026-06-12_evidence.json`

## 검증 상태

통과한 focused/module 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_sources.SourceConnectorTests.test_opendart_parses_corp_code_zip_by_stock_code \
  tests.test_korea_live_lite.KoreaLiveLiteTests.test_opendart_single_account_uses_corp_code_map_when_recent_disclosure_missing \
  -v

PYTHONPATH=src python -m unittest tests.test_free_web_research_runner tests.test_korea_live_lite tests.test_sources tests.test_score_validity -v
# Ran 161 tests ... OK
```

최종 전체 테스트도 통과했다.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
# Ran 3854 tests ... OK
```
