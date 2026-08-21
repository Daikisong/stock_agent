# E2R 2.0 외부 분석 인계 — 2026-08-21

이 디렉터리는 E2R 2.0 operational acceptance 작업이 멈춘 정확한 상태와 문제 진단을 외부 검토자에게 넘기기 위한 인계 문서다. 투자 판단 자료가 아니라 파이프라인·증거 계보·결정론적 점수화 시스템 검토 자료다.

## 먼저 볼 결론

- 기준일은 `as_of_date=2026-07-12`다. 2026-07-13 이후 자료는 판단에 사용하면 안 된다.
- C06 canary 대상은 삼성전자 `005930`, SK하이닉스 `000660`이다.
- `005930`은 사실추출, 7개 구성요소 연구, Judge, Supervisor, semantic saturation까지 완료됐다.
- `000660`은 사실추출이 완료됐지만 Source Graph가 고객 공식·독립 브로커 계보 공백을 이유로 검색을 다시 열었다.
- `000660`의 현재 병목은 자료 개수가 아니다. `reasonable_positive_routes_remaining=true`와 source-family accepted-lineage 요구가 결합해 분석 전에 검색으로 재진입하는 상태다.
- 전체 점수를 강제로 만들거나 Stage를 LLM이 정하면 안 된다. 다만 확인하지 못한 독립 corroboration 한 항목은 `information_confidence`의 제한으로 반영해야지, 이미 충족된 모든 핵심 score source까지 자동으로 무효화해서는 안 된다.

## 포함 범위

다음 실행 디렉터리 전체를 Git에 강제로 포함했다. 원래 `output/`이 `.gitignore` 대상이지만, 이번 외부 검토 snapshot에서는 누락 없이 추적한다.

```text
output/researcher_mode/c06/2026-07-12-clean-v8/
```

snapshot에는 다음이 포함된다.

- 005930·000660 전체 target 산출물
- Source Graph checkpoint와 query/candidate/fetch/rejection ledger
- 원문 document 및 EvidenceFact 계보
- Collaboration request/response journal
- structured materialization, component memo, Judge, Red Team, Supervisor, saturation 중간산출물
- production lane manifest와 비교용 공통 산출물
- 당시 수동으로 만든 8개 response payload
- 원래 operational acceptance 목표 문서

복사 시점 기준 `clean-v8`는 파일 2,729개, 약 390MB였고 GitHub의 100MB 단일 파일 제한을 넘는 파일은 없었다. 용량 때문에 일부 파일을 샘플링하거나 제거하지 않았다.

## 현재 상태

| 대상 | 사실추출 | Source Graph | 구성요소 분석 | Saturation | 의미 |
|---|---|---|---|---|---|
| 005930 | `FACT_EXTRACTION_COMPLETE` | `STOPPED_ON_RESOLUTION` | `COMPONENT_SCORING_MEMOS_COMPLETE` | `CERTIFIED` | production research 완료, post-run Gold 대기 |
| 000660 | `FACT_EXTRACTION_COMPLETE` | `QUERY_GENERATION_PENDING` | `COMPONENT_SCORING_MEMOS_PENDING` | `PENDING` | 검색 재진입 때문에 분석 시작 전 정지 |

000660 Collaboration journal은 request 471개, response 469개다. 응답이 없는 두 request의 성격은 다르다.

1. `COLLABREQ-5e6c...`는 과거 잘못된 응답을 quarantine한 뒤 후속 retry/coverage로 대체 완료된 오래된 사실추출 request다. 현재 사실추출 미완료를 뜻하지 않는다.
2. `COLLABREQ-88bd...`는 현재 열린 `SOURCE_QUERY_GENERATION` request다. 이 request가 실제 현재 병목이다.

## 핵심 파일

- 전체 문제 진단: [문제진단.md](문제진단.md)
- 외부 검토 절차: [외부검토절차.md](외부검토절차.md)
- 원래 목표: [original_goal.md](original_goal.md)
- 000660 Source Graph: `output/researcher_mode/c06/2026-07-12-clean-v8/000660/source_graph_checkpoint.json`
- 000660 사실추출: `output/researcher_mode/c06/2026-07-12-clean-v8/000660/fact_extraction_result.json`
- 000660 구성요소 상태: `output/researcher_mode/c06/2026-07-12-clean-v8/000660/component_scoring_memo_run.json`
- 000660 연구 epoch: `output/researcher_mode/c06/2026-07-12-clean-v8/000660/research_epoch_checkpoint.json`
- 000660 request/response journal: `output/researcher_mode/c06/2026-07-12-clean-v8/000660/collaboration_codex_subagent_provider/`
- 상태 요약기: `scripts/inspect_e2r_v6_external_handoff.py`

## 빠른 상태 확인

저장소 루트에서 실행한다.

```bash
PYTHONPATH=src python scripts/inspect_e2r_v6_external_handoff.py
```

이 명령은 파일을 수정하거나 네트워크를 호출하지 않는다. 두 target의 핵심 상태, 000660 journal 수, 미응답 request, Source Graph pending reason을 출력한다.

## 동일 실행 재개 명령

아래 명령은 현재 checkpoint를 재사용한다. provider response가 없으면 pending으로 끝나는 것이 정상이다.

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_researcher_mode_until_pass \
  --as-of-date 2026-07-12 \
  --symbols 005930,000660 \
  --archetype C06_HBM_MEMORY_CUSTOMER_CAPACITY \
  --live-materialization-authorized true \
  --checkpoint-resume true \
  --gold-lane-isolated true \
  --require-researcher-parity true \
  --output-root output/researcher_mode/c06/2026-07-12-clean-v8 \
  --research-provider codex-collaboration \
  --fact-documents-per-call 8
```

## 외부 검토에 요청하는 판단

1. 같은 objective/source-family에서 새 accepted fact lineage가 생기지 않은 반복 검색을 어떤 semantic identity로 소진 처리할지.
2. Supervisor 문구가 조금 바뀌어도 이전 `SEMANTIC_NO_NEW_ROUTE_FIXPOINT`가 무효화되지 않도록 contract를 어떻게 정규화할지.
3. 고객 공식 계약조건 미확인을 `information_confidence` 감점으로 반영하면서도, 이미 충족된 deterministic score source 전체를 `score_valid=false`로 오염시키지 않는 경계를 어디에 둘지.
4. 000660에서 새 fetch 없이 7개 구성요소 메모와 21개 독립 Judge를 실행해도 되는지.
5. 테스트로 반드시 고정해야 할 무한 재검색 회귀 시나리오가 무엇인지.

직접적인 매수·매도·비중 판단은 이 인계의 범위가 아니다.
