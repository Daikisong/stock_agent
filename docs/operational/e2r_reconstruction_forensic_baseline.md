# E2R Evidence Intelligence Reconstruction Forensic Baseline

작성 기준일: 2026-07-10  
기준 HEAD: 3e126efee61faf0c62a18c1d19d59d0a2ad7f2a8  
goal.md SHA-256: 3e64d7f5c2c0a56b237adf1ff04dcbd7871525286212cb4a05d36c26c36d223e

## 1. 결론

현재 공식 판정은 다음과 같다.

    MEANINGFUL_RUNTIME_PARITY_NOT_READY

이 판정은 보고서 문구가 아니라 최신 leaf artifact가 증명한다.

- production FULL_THESIS row: 0
- full E2R verified score row: 0
- Brain/Web StageCourt trace의 Census promotion: 0
- runtime parity blocker: FULL_THESIS_ARCHETYPE_DIVERSITY_BELOW_MINIMUM
- runtime parity blocker: MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING

7월 3~4일 문서에는 당시 fixture, replay, smoke, 부분 production run을 근거로 완료 가능하다고 쓴 기록이 있다. 그러나 7월 5~8일의 더 최신 runtime leaf는 그보다 낮은 상태를 증명한다. 이 reconstruction에서는 증거 우선순위를 다음처럼 고정한다.

1. 현재 leaf artifact
2. leaf에서 독립 재계산한 audit
3. generated summary
4. 과거 handoff/report 문구

쉬운 예: 예전 진료기록에 “퇴원 가능”이라고 적혀 있어도, 오늘 검사에서 중대한 이상이 확인되면 오늘 검사표를 따른다.

## 2. 읽은 범위와 자산 성격

다음 범위를 기준선으로 조사했다.

- AGENTS.md
- docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- docs/core/V12_Research_No_Repeat_Index.md
- docs/operational/research_to_runtime_acceptance_report.md
- docs/operational/research_to_runtime_readiness_verdict.md
- docs/0701, docs/0703, docs/0705의 감사·패치·handoff 기록
- src/e2r/research_brain
- src/e2r/research_reverse
- src/e2r/source_routing
- src/e2r/production
- src/e2r/census
- Evidence OS, deterministic scoring, Stage 관련 코드와 CLI/tests

docs/0701, docs/0703, docs/0705는 합계 114,389줄의 진행 기록이다. 이 기록은 반복된 안전 패치와 실패 이력을 이해하는 데 유용하지만, 현재 readiness를 직접 증명하지는 않는다.

V12 historical corpus는 원래 live 판단용이 아니라 calibration 연구용으로 만들어졌다. 따라서 MFE, MAE, outcome, expected stage는 evaluator-only다. 현재 planner나 claim extractor에 노출하면 미래 누수다.

## 3. 현재 production entrypoint

### 3.1 현재 공식 Census

    python -m e2r.cli.run_e2r_census_v4_until_pass

실제 호출:

    run_e2r_census_v4_until_pass
      -> census_runner_v4.run_census_mode_v4
      -> V3 leaf 준비/복사
      -> Research Brain v4 실행
      -> source acquisition
      -> Evidence OS bridge
      -> score/StageCourt
      -> Census promotion
      -> replay/smoke/audit/report

census_runner_v4.py는 약 14,000줄의 단일 orchestration 파일이며, production execution과 fixture replay, dedicated archetype replay, promotion, report 생성이 함께 있다.

### 3.2 Research Brain v4 shadow

    python -m e2r.cli.run_research_brain_v4_production_shadow

V4라는 이름이지만 다음 V2/V3 자산을 직접 사용한다.

- v2_memory_cards
- v2_archetype_router
- v2 CandidateEvent schema
- v3/V4 Evidence OS bridge와 source quality wrapper

따라서 버전 이름만 V4일 뿐 semantic source of truth가 하나인 구조는 아니다.

### 3.3 Research-to-runtime parity

    python -m e2r.cli.run_research_to_runtime_parity_until_pass

이 경로는 다음 legacy stack을 production-reachable하게 만든다.

    census.research_to_runtime_parity
      -> research_reverse.reports
      -> research_case_extractor
      -> research_to_runtime_memory
      -> source_routing.research_source_route_recovery

즉 goal.md가 지적한 두 번째 두뇌는 실제 감사/운영 경로에서 호출되고 있다.

### 3.4 병렬 production path

- unversioned run_e2r_census_mode는 legacy census_runner를 호출한다.
- production_cutover_v3는 contract-blind extraction과 official connector를 보유하지만 Research Brain runtime과 별도다.
- v2/v3 Research Brain CLI도 호출 가능하다.

## 4. 현재 parser / memory / planner / router / extractor

| 계층 | 현재 구현 | 판정 |
|---|---|---|
| structured research parser | research_brain/research_artifact_parser.py, research_row_normalizer.py | 재사용 가능 |
| heuristic reverse parser | research_reverse/research_case_extractor.py | production 부적합 |
| memory compiler/store | research_brain/memory_compiler.py, memory_store.py | provisional |
| runtime card | v2_memory_cards.py, v3_memory_cards.py | contract 재포장 비중 큼 |
| heuristic route recovery | source_routing/research_source_route_recovery.py | production 부적합 |
| archetype router | archetype_classifier.py, v2_archetype_router.py | keyword/token 편향 |
| LLM planner | v4_planner_runtime.py | 재사용 가능하나 blind pass와 question contract 부족 |
| acquisition | v4_source_acquisition_runner.py | bounded/official-first 골격 재사용 |
| raw extraction | production/claim_extraction, v4_evidence_extraction_bridge.py | 재사용 가능하나 API 통합 필요 |
| adjudication/mapping | agentic/evidence_workflow.py | 핵심 안전 인프라 |
| score/stage | scoring.py, staging.py, stage_court.py, v4_scoring_stage.py | 다중 wrapper 통합 필요 |

## 5. 중복 Brain 경로

### 5.1 corpus identity

research_brain은 machine-readable row를 읽는 parser를 이미 갖고 있다. 반면 research_reverse는 파일 앞부분과 텍스트 패턴을 이용해 파일 단위 record를 만든다.

현재 research_reverse 방식의 위험:

- 24,000자 이후 structured row 손실
- 첫 번째 6자리 symbol 중심 압축
- company_name과 trigger_date 손실
- 한 파일의 여러 case를 하나로 압축
- 파일 URL을 모든 case URL처럼 사용
- primitive 문자열 출현을 positive/missing 의미처럼 해석

### 5.2 memory identity

다음이 병렬이다.

- ResearchMemoryRecord / Memory Store
- V2/V3 MemoryCard
- research_reverse Runtime MemoryCard
- Evidence Contract 기반 matrix/card

현재 card_count=36은 registry coverage를 뜻할 뿐, historical positive/counter/source-success가 의미 있게 학습됐다는 뜻이 아니다.

### 5.3 source route identity

현재 route pattern 1,855개는 historical source success를 case/anchor 단위로 복원한 수치가 아니다. primitive 문자열을 보고 DART, IR, report, web 같은 source family를 추정한 결과가 포함된다.

### 5.4 score/stage identity

다음 경로가 함께 존재한다.

- DeterministicScorer + StageClassifier
- Evidence OS StageCourt
- V3/V4 scoring_stage wrapper
- Census AtomicStageDecision

active profile의 Yellow/Green 기준과 StageCourt 기본값도 서로 다르다. reconstruction은 threshold를 바꾸지 않고, caller가 canonical profile 값을 명시적으로 한 번만 주도록 통합해야 한다.

## 6. summary artifact readback

docs/operational/census_mode_v4_artifact_manifest.json은 이후 parity code와 tests가 읽을 output_root를 가리킨다.

현재 경로:

    output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260708T131257Z

research_to_runtime_parity._resolve_output_root는 이 mutable manifest를 읽는다. 반면 일부 tests는 이전 leaf 상태인 C17 full-thesis 1건을 기대한다. 이 때문에 현재 전체 테스트 18개가 실패한다.

이 구조의 위험:

- summary pointer 변경이 고정 테스트 의미를 바꾼다.
- 오래된 expected snapshot과 최신 leaf가 섞인다.
- report 재생성이 runtime proof처럼 보일 수 있다.

새 구조는 run manifest를 immutable run identity로 고정하고, frozen replay fixture와 current canonical pointer를 분리해야 한다.

## 7. SourceTask에서 StageCourt까지 실제 연결

현재 leaf 연결은 다음 파일에 존재한다.

| 단계 | leaf |
|---|---|
| planner | planner_runs.jsonl |
| source task | source_tasks.jsonl |
| execution | source_task_executions.jsonl |
| document | evidence_documents.jsonl |
| anchor | evidence_anchors.jsonl |
| accepted claim | accepted_claims.jsonl |
| mapping/state | primitive_mappings.jsonl, primitive_states.jsonl |
| contribution | score_contributions.jsonl |
| StageCourt | stagecourt_traces.jsonl |
| promotion | census_stage_status.jsonl, brain_stage_promotion_audit.json |

이 연결은 부분적으로 실제다. 첫 leaf 예시는 OpenDART의 issuer-direct 계약 공시를 fetch하고, anchor와 direct current claim을 만들고, contract_quality로 mapping한다.

그러나 최종 funnel은 닫히지 않았다.

- StageCourt trace는 존재한다.
- accepted claim도 존재한다.
- score contribution도 존재한다.
- production FULL_THESIS promotion은 0이다.
- 원래 질문을 직접 닫은 closure를 독립 집계할 canonical leaf가 없다.

## 8. 현재 conversion funnel

### 8.1 historical inventory

| 지표 | 수치 | 의미 |
|---|---:|---|
| V12 result MD | 2,263 | historical artifacts |
| raw trigger rows | 18,760 | parser raw rows |
| validated rows | 13,738 | calibration validation 통과 |
| representative rows | 12,471 | calibration dedupe 대표 |
| calibration unique cases | 9,161 | calibration용 case key |
| research_reverse records | 11,394 | heuristic inventory, meaningful case 아님 |
| source_proxy_only | 3,723 | planning/repair only |
| evidence_url_pending | 3,906 | URL repair 필요 |

### 8.2 provisional intelligence

| 지표 | 수치 | 의미 |
|---|---:|---|
| MemoryCard | 36 | registry coverage |
| route pattern | 1,855 | heuristic 포함 |
| executable recipe | 0 | 새 schema 기준 |

### 8.3 current runtime leaf

| 단계 | row 수 |
|---|---:|
| planner | 458 |
| source task | 901 |
| source execution | 901 |
| fetched document | 238 |
| accepted claim | 161 |
| primitive mapping | 96 |
| primitive state | 114 |
| score contribution | 105 |
| StageCourt trace | 95 |
| production full thesis | 0 |

이 수치를 단순 전환율로 읽으면 안 된다. 여러 run/retry/baseline이 합쳐진 leaf이기 때문이다. 새 observability는 candidate_id, question_id, recipe_id, task_id를 따라 동일 cohort만 집계해야 한다.

## 9. 현재 failure funnel

111개 full-thesis seed의 최신 상태:

| 상태 | 수 |
|---|---:|
| ACCEPTED_CLAIM_NOT_CREATED | 79 |
| PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS | 1 |
| SOURCE_TASK_NOT_EXECUTED | 8 |
| STAGECOURT_READY_NOT_PROMOTED | 3 |
| STAGECOURT_TRACE_NOT_CREATED | 20 |

Brain/Web readiness blocker:

- score eligibility deterministic guard 실패 64
- representative trace의 StageCourt reference 누락 12
- StageCourt trace의 Census promotion 없음
- promotion verdict ELIGIBLE_NOT_PROMOTED

과거 live bounded audit의 대표 semantic failure:

- primitive gap unsatisfied가 가장 큰 실패 cluster였다.
- 2017 broker PDF의 과거 전망이 2026 CURRENT FCF claim으로 처리됐다.
- 원래 질문과 다른 rerouted claim이 accepted되어 progress처럼 보였다.

최근 guard patch는 final export 일부를 막았지만, canonical question-to-closure API가 없으므로 경로별 중복 방어가 남아 있다.

## 10. production reachable / test-only / dead

### Production reachable

- run_e2r_census_v4_until_pass
- census_runner_v4
- Research Brain v4와 그 V2 memory/router dependency
- v4 acquisition / Evidence OS bridge / StageCourt
- research_to_runtime_parity
- research_reverse reports/extractor
- source_routing primitive-name route recovery
- production cutover v3
- unversioned legacy census

### Test-only 또는 fixture-only로 유지해야 하는 것

- controlled semantic replay
- controlled full-thesis smoke
- output/0621_agentic_replay
- fake planner/provider
- dedicated C06/C08/C15/C17/C24/C28 fixture replay

### Deprecated candidate

- Research Brain v2/v3 CLI
- Census v2/v3 CLI
- report-only until_pass/parity label path
- research_reverse/source_routing의 독립 schema

정적 dead code는 Phase 1 migration 후 canonical entrypoint import graph를 기준으로 다시 판정한다. 지금은 import 가능하다는 이유만으로 안전하게 삭제하지 않는다.

## 11. 테스트 기준선

실행:

    PYTHONPATH=src python -m unittest discover -s tests -v

결과:

- tests: 5,305
- pass: 5,287
- failures: 18
- errors: 0
- duration: 517.308초

18개 실패는 모두 current runtime-parity/full-thesis artifact drift cluster에 속한다.

현재 leaf:

    full_thesis_row_count = 0
    score_path = PENDING

고정 기대값:

    C17 full_thesis_row_count = 1
    score_path = PASS

어느 쪽을 canonical fixture로 삼을지 숨기지 않고 Phase 11 frozen replay migration에서 명시적으로 고정한다.

## 12. Phase 0 판정

유효한 기반:

- Evidence OS safety model
- official source connector와 bounded acquisition 골격
- deterministic scoring과 canonical Stage enum
- provider/source pending 안전 철학
- 광범위한 known-bad tests

재건 대상:

- case-level semantic compiler
- case-level source verification
- Evidence Recipe OS
- balanced semantic retrieval
- two-pass blind planner
- question-centric SourceTask
- direct task satisfaction ledger
- adaptive investigation
- replay/current separation
- single AtomicStageDecision runtime

Phase 0에서는 기존 Goal4 산출물을 삭제하거나 PASS로 올리지 않는다. 현재 NOT_READY와 full-thesis 0건을 안전한 시작점으로 보존한다.
