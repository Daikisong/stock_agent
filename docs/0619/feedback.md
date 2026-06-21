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
