# Gate 1 R0 읽기 전용 호출 그래프

기준일은 `2026-07-12`, 대상은 `000660`, 입력 snapshot은
`output/researcher_mode/c06/2026-07-12-clean-v8`이다. 이 문서는 코드를
실행하거나 고친 결과가 아니라, 현재 호출 관계를 읽기 전용으로 확인한
결과다.

## 현재 실제 흐름

```text
run_e2r_researcher_mode_until_pass.main
  -> _run_target_until_semantic_terminal
     -> CurrentResearcherModeTargetRunner.run_checkpoint
        -> SourceGraphExplorer.explore                 # 7개 objective 생성
        -> ResearcherSourceGraphAcquirer.acquire       # 현재 blocker
           -> ResearcherSourceQueryPlanner.generate
           -> Collaboration request 88bd... 대기
        -> ResearcherEvidenceFactExtractor.extract     # 현재는 COMPLETE
        -> exact upstream ordering boundary
           -> source response가 pending이면 여기서 중단
        -> CurrentStructuredMaterializer.materialize
        -> CanonicalResearchDossierBuilder.build
           -> business model
           -> 7개 component memo
           -> Red Team
           -> synthesis
        -> LLMComponentScoringMemoEngine.build
           -> component별 3 Judge, 총 21 Judge
        -> DeterministicScoreAggregator.aggregate_run
        -> ResearchEpochRunner.run_epoch
           -> ResearchSupervisor.review_epoch
           -> saturation A/B/Independent
        -> ResearcherStageCourt.decide                 # deterministic Stage
```

`CurrentResearcherModeTargetRunner.run_checkpoint`는 source collaboration 응답이
pending이면 fact extraction 뒤에서 downstream을 열지 않는다. 따라서 현재
component memo와 Judge가 0개인 직접 원인은 “facts가 없어서”가 아니라
`SOURCE_QUERY_GENERATION` 응답을 먼저 소비하도록 둔 upstream ordering
boundary다.

쉬운 예: 재료 996개가 냉장고에 이미 있어도, 주방 입구의 “추가 장보기 여부”
판정이 계속 대기 상태이면 요리 단계가 시작되지 않는다. Gate 1 수정은 재료를
다시 사 오는 것이 아니라, 같은 장보기 공백을 안정적인 키로 닫고 요리를
계속하게 만드는 작업이다.

## 반복이 열리는 지점

`ResearcherSourceGraphAcquirer.acquire`의 현재 로직은 다음 순서다.

1. unresolved objective와 source-family lineage failure를 다시 모은다.
2. `ResearcherSourceQueryPlanner.generate`를 호출한다.
3. query가 비어 있으면 `_query_generation_semantic_retry_context`로 다음 prompt를
   바꾼다.
4. 독립적으로 소비된 빈 응답 2개면
   `_query_generation_reached_supervisor_handoff`가
   `SEMANTIC_NO_NEW_ROUTE_FIXPOINT` handoff를 만든다.
5. `_query_generation_handoff_matches_supervisor_contract`가 handoff 유지 여부를
   판정한다.

문제는 `_supervisor_query_contract_hash`가 아래 자연어 배열까지 통째로 hash에
넣는다는 점이다.

- `missing_material_facts`
- `new_source_family_directions`
- `query_direction_briefs`
- `source_family_gaps`
- `parser_or_extractor_failures`
- `failure_assessments`

같은 공백이어도 Supervisor가 표현을 바꾸면 contract hash가 바뀐다. 그러면
기존 handoff 뒤의 history만 새 lineage로 취급되어 같은
`SOURCE_QUERY_GENERATION`이 다시 열릴 수 있다. prompt hash는 호출 계보에는
필요하지만 gap의 의미상 신원으로 쓰면 안 된다.

쉬운 예: “고객 공식 확인 부족”과 “고객사 독립 확인 미충족”은 문장은 다르지만
같은 공백이다. 현재 구조는 문장이 달라지면 다른 접수번호처럼 취급할 수 있다.

## Gate 1에서 바꿔야 할 경계

다음 수정은 종목명이나 C06 전용 분기 없이 일반화해야 한다.

1. objective id, affected component ids, required source family, fact/lineage state
   hash로 `EvidenceGapKey`를 만든다.
2. prompt hash와 Supervisor 자연어는 gap identity에서 제외한다.
3. 빈 응답 2개와 새 source direction 부재를 같은 stable key에 누적한다.
4. `CORE_SCORE_BLOCKER`, `CORROBORATION_CAP`, `MONITORING_GAP`을 분리한다.
5. `CORROBORATION_CAP`은 append-only disposition으로 닫고 영향 component만
   상단을 제한한다. FCF·revision·valuation 같은 무관 component를 0점이나
   pending으로 만들지 않는다.
6. fact roster, accepted lineage roster 또는 실행 가능한 새 source direction이
   실제로 바뀔 때만 disposition을 다시 연다.
7. 닫힌 동일 key의 세 번째 query 생성 시도는
   `REPEATED_EXHAUSTED_GAP_REOPENED` hard failure로 중단한다.
8. disposition은 source absence fact가 아니다. “못 찾음”을 “존재하지 않음”으로
   바꾸지 않는다.

## R0 판정

- fact extraction: 완료
- current/open facts: 996개, 동결 가능
- 현재 canonical blocker: `COLLABREQ-88bd...` 하나
- source query/fetch 추가: R0에서 0개
- 현재 7 component/21 Judge/후반 검증: 완료 증거 없음
- stable gap identity와 append-only disposition: 아직 구현 전

따라서 R0 판정은 `READ_ONLY_BASELINE_CAPTURED`다. Gate 1 완료 판정은 아니다.
