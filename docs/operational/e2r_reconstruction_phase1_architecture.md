# E2R Reconstruction Phase 1 — Unified Research Brain

## 결과

    UNIFIED_RESEARCH_BRAIN_ARCHITECTURE_PASS

src/e2r/research_brain을 유일한 canonical intelligence namespace로 고정했다.

## 변경한 구조

새 canonical package:

    research_brain/
      corpus/
      compiler/
      recipes/
      retrieval/
      planning/
      replay/
      runtime/

기존 research_reverse와 source_routing의 구현 원본을 위 namespace로 이동했다. 기존 import path에는 deprecation adapter만 남겼다.

production parity path는 이제 다음을 직접 import한다.

    research_brain.compiler.legacy_compatibility_reports
    research_brain.recipes.legacy_route_recovery

다음 import는 production parity path에서 0개다.

    e2r.research_reverse
    e2r.source_routing

## primitive-name route guesser 제거

기존 route recovery는 primitive 문자열에 contract, margin, hbm, clinical, arr 등이 들어가는지 보고 source family를 바꿨다.

Phase 1 compatibility projection은 primitive 이름을 전혀 읽지 않는다. 모든 primitive에 neutral official-first route를 주며, 이 projection은 EvidenceRecipe가 아니고 recovered route로 세지 않는다.

실제 question-specific source route는 Phase 4 Evidence Recipe compiler가 historical source success/failure에서 만든다.

## Legacy CLI 정책

다음 CLI는 기본 실행에서 LEGACY_DIAGNOSTIC_ONLY를 반환하고 명시적 opt-in 없이는 실행하지 않는다.

- Census v2
- Census v3
- Research Brain v2
- Research Brain v3
- Goal4 research-to-runtime parity

V2/V3/V4 readiness builder에는 legacy path가 canonical production readiness를 만들 수 없도록 unconditional production blocker를 추가했다.

쉬운 예: 예전 시험기는 계속 고장 재현과 호환 테스트에 쓸 수 있지만, 새 제품의 출고 합격 스티커를 발행할 권한은 없다.

## Canonical CLI 표면

다음 공식 module을 만들었다.

- compile_e2r_research_intelligence
- run_e2r_historical_replay
- run_e2r_current_operation
- audit_e2r_evidence_intelligence

아직 담당 Phase가 구현되지 않은 command는 성공을 가장하지 않고 RECONSTRUCTION_COMPONENT_NOT_READY와 required_phase를 반환한다. 이후 Phase에서 같은 CLI를 실제 compiler/runtime에 연결한다.

## 호환성

- 기존 research_reverse tests는 adapter를 통해 기존 shape을 읽을 수 있다.
- 기존 source route report tests는 neutral official-first projection으로 유지된다.
- 원본 historical research MD는 변경하지 않았다.
- scoring weight와 Stage threshold는 변경하지 않았다.

## 검증

Focused tests:

    test_research_brain_single_source_of_truth
    test_legacy_research_reverse_not_production_reachable
    test_legacy_source_route_not_production_reachable
    test_legacy_cli_cannot_claim_ready
    existing research_reverse/source_route compatibility tests

결과:

    30 tests, 0 failures

추가 legacy readiness 및 parity retry test:

    13 tests, 0 failures
    12 tests, 0 failures

## 다음 Phase

현재 canonical namespace 안의 legacy_case_inventory는 여전히 기존 shallow semantics를 보존한 migration implementation이다. Phase 2에서 이를 structured-row-first HistoricalResearchCase compiler로 교체한다. 그 전까지 11,394 record는 meaningful case로 승격되지 않는다.
