# Project Instructions

이 저장소는 E2R 2.0 리서치 에이전트의 핵심 로직을 다룬다.

## Communication

- 설명은 한국어로 한다.
- 어려운 판단은 쉬운 예시를 붙여 설명한다.
- 예: `as_of_date=2023-07-27`이면 2023-07-28 이후에 나온 리포트, 가격, 공시는 그날 판단에 쓰면 안 된다.

## E2R Rules

- E2R 2.0은 단순 스크리너가 아니라 Stage 상태기계다.
- canonical Stage enum은 `0`, `1`, `2`, `3-Green`, `3-Yellow`, `3-Red`, `4A`, `4B`, `4C`, `5`를 유지한다.
- Stage 4B 내부 진단은 `4B-watch`, `4B-elevated`, `4B-graduated`로 나눌 수 있지만 canonical Stage는 가능하면 바꾸지 않는다.
- EPS만 보지 말고 FCF, 계약 질, 수주잔고/RPO, CAPA, ASP, 쇼티지 성격을 함께 본다.
- 구조적 쇼티지는 장기계약, 선수금, RPO, 수주잔고, CAPA 잠김, ASP 상승이 같이 있을 때 강하게 본다.
- 일회성 쇼티지는 실적이 강해도 Stage 3-Green을 조심한다.

## Data Discipline

- 모든 판단은 `as_of_date` 기준으로 재현 가능해야 한다.
- 미래 데이터 누수, 후견지명, 과거 성공 종목명 하드코딩을 금지한다.
- 과거 종목명은 fixture와 문서에는 둘 수 있지만, scoring/staging/red-team 로직에서 종목명을 조건으로 쓰지 않는다.
- LLM은 텍스트에서 구조화된 증거를 뽑는 보조 역할만 한다. 최종 score와 stage는 deterministic rule engine이 계산한다.
- live web scraping이나 live API 연결은 별도 요청 전까지 추가하지 않는다.

## LLM Agent Workflow

- 이 프로젝트는 섹터/아키타입 확장형 리서치 에이전트다. 새 섹터, 새 테마, 새 누락 슬롯이 들어올 때마다 코드에 검색어 템플릿을 추가하는 방식으로 해결하지 않는다.
- 종목명, 섹터명, 아키타입명, 누락 슬롯명을 조건으로 검색어를 하드코딩하지 않는다. 예: `if C06 then "HBM 장기공급계약 선수금..."`, `if contract_quality missing then "장기공급계약 선수금..."` 같은 deterministic query synthesis는 금지한다.
- LLM의 역할은 현재 evidence, fetched documents, missing_information, score_gap_context를 보고 다음에 무엇을 찾아야 하는지 판단하고 `suggested_queries`를 생성하는 것이다. deterministic 코드는 LLM이 만든 query를 `as_of_date`, 회사 범위, 중복, 미래누수 기준으로 검증하고 실행만 한다.
- LLM이 빈 `suggested_queries`, 이미 실행한 중복 query, 미래누수 query처럼 새 검색으로 이어지지 않는 답을 주면 그대로 멈추지 않는다. deterministic 코드는 실패 사유만 `score_gap_context`에 되돌려 보내고, 새 query 생성은 다시 LLM에게 맡긴다.
- 운영 기본값과 운영용 preset에서 검색/API accounting cap은 `None`이다. 작은 숫자 cap은 skip 처리 자체를 검증하는 단위테스트처럼 명시적 테스트 입력에서만 둔다. 점수 공백을 피하려고 검색을 하다가 기본 cap 때문에 멈추는 구조를 만들지 않는다.
- 검색 결과 기본 수집은 API 단일 요청 한도까지 넓게 본다. 기본 `max_results_per_query`는 100이고, 기본 `top_results`는 `None`이다. 기본값으로 상위 N개만 파싱하고 나머지를 `not_selected`로 버리는 구조를 만들지 않는다.
- Stage 2/3 gate 실패는 최종 설명으로만 소비하지 않는다. `failed_stage3_revision`, `failed_stage3_visibility`, `failed_stage3_red_team` 같은 gate 실패와 missing evidence family는 LLM `score_gap_context`로 되돌려 추가 검색 판단을 시킨다.
- live/API 운영 경로는 프로젝트 `.env`를 읽어 비어 있는 환경변수를 채운다. `.env`에 있는 키를 무시해서 provider가 missing credential로 떨어지는 구조를 만들지 않는다. 테스트에서만 명시적으로 env file 로딩을 끌 수 있다.
- `theme_rebalance_enabled=True`처럼 LLM 확장을 명시적으로 켠 경로는 provider가 없다는 이유로 `disabled_no_provider`에 멈추지 않는다. 기본 Codex provider를 붙이고, 실패하더라도 provider_error로 기록하며 검색 확장 시도를 남긴다.
- 부족한 정보가 있으면 LLM provider/prompt/schema를 개선해야 한다. deterministic fallback query 템플릿을 늘리는 것으로 해결하지 않는다.
- 단, 최종 score/stage 계산은 계속 deterministic rule engine이 한다. LLM은 stage를 직접 결정하거나 덮어쓰지 않는다.
- LLM이 제안한 검색으로 새 리포트, 공시, 뉴스, 컨콜, IR이 실제 fetch/parse되고 source-backed evidence id와 연결될 때만 점수 재료로 쓴다. LLM-only 추론은 diagnostics로만 남긴다.
- 운영형 LLM 확장 경로에서 핵심 score source가 비어 있는데 LLM이 새 검색을 만들지 못하거나 provider_error로 끝나면, 낮은 점수를 정상 점수로 확정하지 않는다. `score_valid=false`, raw 참고점수 분리, Stage 0 보류로 처리한다.

쉬운 예:

- 나쁜 방식: `contract_quality`가 비었으니 코드가 항상 `{company} 장기공급계약 선수금 수주잔고 RPO`를 만든다.
- 좋은 방식: LLM이 현재 문서에서 무엇이 빠졌는지 판단해 `{company} 2026 1Q earnings call HBM customer allocation cancellation terms` 같은 query를 직접 제안하고, 코드는 그 query를 검증 후 실행한다.
- 보류 방식 예: FCF/revision source가 비었고 LLM이 새 검색을 못 만들면 `68점 Stage2`로 내보내지 않고 `score pending / raw 68점 참고`로 남긴다.

## Output Safety

- 투자 권고 문구를 출력하지 않는다.
- 예: 직접적인 매수, 매도, 비중 축소 지시는 쓰지 않는다.
- 대신 "Stage 4B-watch", "논리 훼손 감시", "다음 실적과 수주잔고 확인"처럼 모니터링 언어를 쓴다.

## Verification

- 기본 테스트 명령:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

- 새 기능은 원천 데이터에서 score가 생성되는 경로를 테스트해야 한다.
- 예: CSV/JSON fixture를 connector로 읽고, feature engineer가 `ScoringPayload`를 만들고, `DeterministicScorer`가 점수를 산출해야 한다.
