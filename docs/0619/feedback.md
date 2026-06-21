# 0619 피드백 이행 메모

## 핵심 요구

- LLM은 점수와 Stage를 직접 정하지 않는다.
- 문서에서 claim을 추출하고, claim을 primitive로 모으고, primitive가 score contribution으로 이어진 뒤 deterministic scorer와 Stage gate가 최종 판단한다.
- `3-Green`, `3-Yellow`, `3-Red`, `4A`, `4B`, `4C`처럼 운영 판단에 쓰이는 유효 점수는 claim ledger와 score contribution ledger 없이 출력되면 안 된다.
- Stage 4A/4B/4C 전환은 Stage 3-Green gate와 별도로 진단되어야 한다.

쉬운 예:

- 나쁜 출력: `3-Green 82점`만 있고 어느 문장의 어떤 claim 때문에 82점인지 없다.
- 좋은 출력: `contract_quality +15점`이 `claim-001`, `claim-004`에서 왔고, 그 claim들이 원문 URL과 primitive에 연결되어 있다.

## 이번 패치 반영

- score-state contract가 Stage 3/4 유효 점수에 claim-backed ledger를 요구하도록 강화됐다.
- as-of replay와 live-lite 출력에 claim ledger, score contribution ledger, evidence contract coverage, red-team 근거 id, Stage 4 전환 진단이 함께 노출된다.
- Stage gate diagnostics에 4A continuation, 4B overlay, 4C thesis break readiness를 별도 필드로 추가했다.
- red-team soft 4B 신호도 thesis-break 신호처럼 evidence id를 보존한다.
- Green gate 실패 사유에 evidence contract positive/guard/claim-backed score 부족이 검색 가능한 코드로 들어간다.

## 검증

- `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 4,059개 테스트 통과

## 2026-06-21 score-gap 수집 폭 피드백 반영

추가 피드백:

- score-gap 루프의 목적은 맞다. 낮은 점수를 확정하기 전에 미충족 gap을 LLM에게 되돌려 추가 검색어를 만들고 재채점해야 한다.
- 다만 `검색어 10개 * 검색어당 100건 * top_results=None`을 그대로 본문 fetch에 태우면, gap 19개 수리가 아니라 대량 재크롤링처럼 동작한다.
- red-team hard break도 점수를 올리기 위한 반대 증거 찾기가 아니라, hard break claim이 사실인지 검증하고 맞으면 유지, 오독이면 제거하는 방식이어야 한다.

패치:

- initial/theme 확장 검색의 기본값은 유지했다.
- `post_parse_gap`과 `post_score_gap` fetch는 새 gap query만 incremental로 실행한 뒤 기존 `WebResearchResult`에 병합한다.
- gap fetch 기본 한도는 `post_gap_fetch_results_per_query=5`, `post_gap_fetch_min_results=20`이다.
- phase log에 `gap_fetch_mode=incremental`과 `top_results_override`가 남는다.
- 새 gap 문서는 LLM 재검토 앞쪽에 배치하고, 기존 증거 장부는 URL/evidence id 기준으로 보존한다.

실제 운영형 확인:

- 삼성전자 `005930`: initial fetched `1355`, post-parse gap `+18`, score-gap round0 `+18`, score-gap round1 `+13`. 최종 `63.2499`, Stage `4C`, score valid `true`.
- SK하이닉스 `000660`: initial fetched `1079`, post-parse gap `+16`, score-gap round0 `+17`, score-gap round1 `+28`. 최종 `63.8662`, Stage `3-Red`, score valid `true`.

검증:

- `PYTHONPATH=src python -m unittest tests.test_free_web_research_runner -v`
- `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 4,063개 테스트 통과
