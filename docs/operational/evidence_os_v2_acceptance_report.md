# Evidence OS v2 Operational Acceptance Report

- generated_at: 2026-06-28
- commit_sha: 3f30fe252f00da4a1f293cc538584859b490fc12
- verdict: READY

## 판단

Evidence OS v2 운영 전환 상태는 `READY`다. 단, 이 문서는 투자 판단이 아니라 증거 처리 파이프라인의 운영 인수 장부다.

쉬운 예: 예전 파이프라인은 기사에 `감사의견`이라는 단어가 있으면 바로 회계 위험으로 들어갈 수 있었다. 지금 장부는 `누구의 감사의견인지`, `정상인지 부정인지`, `현재도 살아 있는지`, `점수 primitive에 accepted mapping이 있는지`를 통과해야만 점수에 넣는다.

## 핵심 통과 항목

- C01-C36 replay ready: True
- 전 아키타입 Evidence Contract ready: 36/36
- 전 아키타입 StageCourt preview ready: 36/36
- source gap unresolved: 0
- nonzero contribution orphan blocked: 0
- legacy parser active direct score path: 0
- score delta without claim delta: 0
- live smoke accepted target count: 2
- actual candidate discovery path exercised: True

## 삼성전자/SK하이닉스 Smoke

- 삼성전자(005930): stage=3-Green, verified_score=97.5, score_status=FINAL, claims=96, mappings=24
- SK하이닉스(000660): stage=3-Green, verified_score=97.5, score_status=FINAL, claims=73, mappings=22

## 테스트

- command: `PYTHONPATH=src python -m unittest discover -s tests -v`
- passed: 4536
- failed: 0
- skipped: 0

## 산출물

- `evidence_os_v2_sector_matrix.json`
- `evidence_os_v2_archetype_matrix.json`
- `evidence_os_v2_replay_results.json`
- `evidence_os_v2_live_smoke_results.json`
- `evidence_os_v2_source_gap_inventory.json`
- `evidence_os_v2_score_delta_audit.json`
- `evidence_os_v2_legacy_quarantine_audit.json`
- `deprecated_live_results_2026-06-21.md`
- `evidence_os_v2_known_regressions.md`

## Cutover 결론

legacy parser는 mention 생성까지만 허용되고, 점수와 Stage에는 Evidence OS v2의 accepted/current/direct/source-backed claim만 들어간다. 그래서 월덱스 감사의견 같은 타사 정상 문구가 삼성전자 hard break로 들어가는 경로는 운영 출력에서 차단된다.
