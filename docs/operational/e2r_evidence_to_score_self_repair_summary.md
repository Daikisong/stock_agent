# E2R Evidence-to-Score Self-Repair Summary

- as_of_date: 2026-07-11 KST
- targets: 삼성전자 005930, SK하이닉스 000660
- status: SELF_REPAIR_RESOLVED
- unresolved internal failure classes: []
- external blockers: []
- threshold loosening: 0
- synthetic/probe promotion: 0
- expected score/Stage hardcoding: 0

## Root causes fixed

1. 점수가 SourceTask 개수에 기대던 문제를 canonical 100점 component profile로 교체했다.
2. claim 하나를 primitive 하나에만 묶던 구조를 bounded many-to-many impact ledger로 교체했다.
3. rerouted claim을 버리거나 original gap까지 잘못 닫던 문제를 분리했다.
4. 확인된 component 점수가 다른 gap 때문에 사라지던 문제를 partial score와 provisional interval로 보존했다.
5. `VERIFIED_ABSENT_AFTER_SEARCH`와 `UNKNOWN/PENDING`을 분리해 조사 완료 0점과 미조사를 구분했다.
6. acceptance probe, fixture, source proxy가 organic score로 섞이지 않도록 scoring plane을 분리했다.
7. calibrated vector와 deterministic StageCourt trace를 원자적으로 연결했다.
8. 삼성 Q1 ASP/실적 claim은 고객 배정으로 과매핑하지 않되, 확인된 실적·정보 신뢰 impact는 폐기하지 않게 했다.
9. bounded 문서 선택에서 출처 이름의 우연한 토큰보다 실제 본문·anchor의 contract relevance를 먼저 보도록 고쳤다.
10. 61개 blind planner benchmark의 새 deterministic 결과를 재검증하고 stale golden hash를 동기화했다.

쉬운 예: “HBM 판매 증가로 DRAM ASP와 매출이 올랐다”는 문장은 실적 전환 근거로 쓸 수 있지만, 그 문장만으로 특정 고객이 미래 생산능력을 예약했다고 판단하면 안 된다. 이번 수리는 쓸 수 있는 부분은 제한적으로 점수화하고, 말하지 않은 부분은 `unsupported_aspects`로 남긴다.

## Dossier iterations

| target | iteration | failure class | root cause / repair | result |
|---|---:|---|---|---|
| 005930 | 0 | RESEARCH_NOT_EXECUTED | 12개 bounded question-family 조사를 초기화 | DOSSIER_ORCHESTRATOR_INITIALIZED |
| 005930 | 1 | IMPACT_ADJUDICATION_REQUIRED | semantic primitive contract 확장, 실제 full source 재컴파일 | organic claim 27, accepted mapping 31 |
| 000660 | 0 | RESEARCH_NOT_EXECUTED | 12개 bounded question-family 조사를 초기화 | DOSSIER_ORCHESTRATOR_INITIALIZED |
| 000660 | 1 | IMPACT_ADJUDICATION_REQUIRED | semantic primitive contract 확장, 실제 full source 재컴파일 | organic claim 12, accepted mapping 15 |

후속 deterministic closure에서 삼성 32개, 하이닉스 12개의 validated impact가 생성됐고 모든 7개 material component가 terminal 상태가 되었다. 두 dossier 모두 같은 proposal을 재사용한 replay에서 핵심 leaf SHA-256이 변하지 않았다.

## Failure-class closure

- CALIBRATED_PROFILE_NOT_LOADED: resolved
- BALANCED_POINTS_STILL_REACHABLE: resolved
- CLAIM_MAPPING_LINEAGE_LOST: resolved
- REROUTED_VALID_IMPACT_DROPPED: resolved
- MULTI_IMPACT_REJECTED: resolved
- IMPACT_ADJUDICATION_FAILED: resolved
- IMPACT_CAP_INVALID: resolved
- COMPONENT_STATE_COLLAPSED: resolved
- SUPPORTED_SCORE_ERASED: resolved
- FULL_SCORE_BLOCKED_BY_EVALUATED_ABSENT: resolved
- UNKNOWN_ALLOWED_FINAL: resolved
- ORGANIC_CLAIM_ZERO: resolved
- FULL_SCORE_INVALID: resolved
- STAGE_TRACE_MISMATCH: resolved
- PROBE_CONTAMINATION: resolved
- EXTERNAL_PROVIDER_BLOCKER: not present

## Verification leaves

- full unittest: `PYTHONPATH=src python -m unittest discover -s tests -v` → 5,786 tests PASS, skip/xfail 0
- `docs/operational/e2r_evidence_to_score_known_bad_audit.json`: 25/25 PASS
- `docs/operational/e2r_evidence_to_score_reviewer_gate.json`: Reviewer A~G PASS
- `docs/operational/e2r_c06_historical_component_replay.json`: PASS
- `docs/operational/e2r_evidence_to_score_generalization_audit.json`: PASS

## Exact self-repair verdict

SELF_REPAIR_RESOLVED
