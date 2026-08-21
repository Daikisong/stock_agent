# Gate 1 clean merge 검증 기록

## Git 기준

- source branch: `fix/e2r-stable-gap-fixpoint-20260821`
- source HEAD: `c831cc9a95144c77206db335d61cd98e2cab7bdf`
- clean branch: `fix/e2r-gate1-clean-merge-20260822`
- clean base: `origin/main` / `7e3f71793465c0e4d03cce57f9a75c2bb40943c2`
- clean HEAD: 외부 검토 시 `git rev-parse HEAD`로 확인
- source giant commit ancestry: `false`
- ancestry command: `git merge-base --is-ancestor c831cc9a95144c77206db335d61cd98e2cab7bdf HEAD`

초기 packaging commit 뒤 독립 검수 수정 commit이 같은 PR 브랜치에 추가됐다. 따라서 이 PR은 더 이상 단일 commit이라고 주장하지 않는다. 외부 검토자는 `git log --oneline origin/main..HEAD`와 `git rev-parse HEAD`로 실제 ancestry와 HEAD를 확인한다.

## 선택한 payload

코드 5개:

- `src/e2r/research_brain/researcher_mode/current_researcher_mode.py`
- `src/e2r/research_brain/researcher_mode/evidence_gap.py`
- `src/e2r/research_brain/researcher_mode/prompt_projection.py`
- `src/e2r/research_brain/researcher_mode/research_supervisor.py`
- `src/e2r/research_brain/researcher_mode/source_graph_explorer.py`

테스트 3개:

- `tests/test_e2r_evidence_gap_fixpoint.py`
- `tests/test_e2r_v5_semantic_research_saturation.py`
- `tests/test_e2r_v5_stagecourt.py`

운영 검증 문서 4개:

- `docs/operational/e2r_v5_final_readiness.md`
- `docs/operational/e2r_v5_full_test_result.json`
- `docs/operational/e2r_v5_full_test_result.log`
- `docs/operational/e2r_v5_reviewer_gate.json`

Gate 1 compact review 문서 29개와 clean packaging 문서 3개:

- `fix_result/000660_business_model_memo.json`
- `fix_result/000660_component_memos_compact.jsonl`
- `fix_result/000660_final_component_decisions.jsonl`
- `fix_result/000660_judge_decisions_compact.jsonl`
- `fix_result/000660_red_team_receipt.json`
- `fix_result/000660_saturation_certificate.json`
- `fix_result/000660_saturation_reviews_compact.jsonl`
- `fix_result/000660_score_receipt.json`
- `fix_result/000660_stage_gate_mappings_compact.jsonl`
- `fix_result/000660_stagecourt_receipt.json`
- `fix_result/000660_supervisor_receipt.json`
- `fix_result/000660_synthesis_receipt.json`
- `fix_result/before_state.json`
- `fix_result/current_fact_roster_receipt.json`
- `fix_result/current_pending_request_audit.json`
- `fix_result/current_request_response_audit.json`
- `fix_result/dependency_invalidation_audit.json`
- `fix_result/final_review.md`
- `fix_result/fixpoint_audit.json`
- `fix_result/focused_test_receipt.json`
- `fix_result/full_test_receipt.json`
- `fix_result/gap_identity_audit.json`
- `fix_result/gap_materiality_audit.json`
- `fix_result/gate1_reviewer_receipt.json`
- `fix_result/identical_rerun_audit.json`
- `fix_result/original_goal_status_matrix.json`
- `fix_result/readonly_call_graph.md`
- `fix_result/문제점과수정결과.md`
- `fix_result/외부검토번들안내.md`
- `fix_result/clean_merge_payload_manifest.json`
- `fix_result/external_artifact_receipt.json`
- `fix_result/clean_merge_verification.md`

전체 legacy diff 14,410개를 먼저 분류했고, 원본에서 41개를 선택했다. 초기 clean packaging은 새 문서 3개를 더한 44개였다. 독립 검수 후에는 generic integration 수정과 GitHub workflow 수정이 같은 PR delta에 추가됐다. `clean_merge_payload_manifest.json`은 초기 legacy diff 분류 영수증이며, 현재 최종 PR delta 자체는 `git diff --name-status origin/main...HEAD`로 확인한다. 제외 artifact 14,370개(legacy 추적 14,369개와 legacy worktree의 ignored raw 1개)는 `external_artifact_receipt.json`에 path/크기/SHA-256 단위로 기록했다.

## 제외 범주

- `.gitattributes`의 legacy 대형 artifact 추적 규칙
- `.e2r_cache/**`, `data/cache/**`, `output/**`
- collaboration request/response 원문
- claim provenance와 fetched page 원문
- runner output 전체와 과거 replay corpus
- gzip/zip/tar/zst 및 repository 내부 archive 복원 script
- `.pytest_cache`, `__pycache__`, `*.pyc`, 임시 로그

raw 원문과 cache/output은 clean PR에 없다. archive를 만들거나 GitHub Release/LFS에 게시하지 않았다. 테스트에 필요한 기존 snapshot은 legacy worktree에서 clean worktree의 ignored 경로로만 임시 복사했고, Git 검증 전에 제거했다.

## Canonical Gate 1 보존

- verdict: `C06_ANALYST_MODE_RECOVERY_PASS`
- facts: total 2,190 / current-open 996 / closed-superseded 1,194
- component: 7/7
- Judge: 21/21
- Red Team / synthesis / Supervisor: 완료
- saturation A/B/Independent: `CERTIFIED`
- deterministic score: 70.2
- interval: 68.153813~72.246187
- score_valid: true
- canonical Stage: 2 / StageCourt `FINAL`
- 동일 snapshot 재실행: 신규 query 0, 신규 fetch 0, score variance 0, Stage variance 0, 동일 gap 재개방 0
- Gate 2: `NOT_EVALUATED`
- Phase101~109, C08/C15/C17/C24/C28, KRX Census, final market cutover: 미착수

## 테스트와 tracked-receipt 검증

중요: 이 clean PR에는 996개 fact 원장과 source checkpoint 원문이 없다. 따라서 아래 000660 acceptance는 clean clone에서 `996 facts → 7 memos → 21 judges → 70.2 → Stage 2`를 새로 계산하는 테스트가 아니다. 커밋된 compact memo/Judge/score/Stage/identical-rerun 영수증 사이의 숫자와 해시가 서로 일치하는지를 검사한다.

쉬운 예: 택배 상자 원본 전체를 다시 포장해 무게를 재는 검사가 아니라, 인수증 여러 장에 적힌 상자 수와 무게가 서로 맞는지 보는 검사다. 따라서 `identical_rerun_audit.json`은 legacy 실행의 불변성 영수증이며, PR 단독 raw replay 증명으로 해석하면 안 된다.

- focused: `PYTHONPATH=src python -m unittest tests.test_e2r_evidence_gap_fixpoint tests.test_e2r_v5_semantic_research_saturation tests.test_e2r_v5_stagecourt tests.test_e2r_v5_phase94_runner_contract -v` → 221 PASS, failure/error/skip 0
- full: `PYTHONPATH=src python -m e2r.cli.run_e2r_v5_full_test_evidence --workspace-root .` → 7,204 PASS, failure/error/skip 0, exit 0
- independent acceptance compile: `PYTHONPATH=src python -m e2r.cli.compile_e2r_v5_independent_acceptance --workspace-root .` → reviewer 10/10, critical 0, PASS
- Phase100: `PYTHONPATH=src python -m unittest tests.test_e2r_v5_phase100_independent_acceptance -v` → 15 PASS, failure/error/skip 0
- compile: `PYTHONPATH=src python -m compileall -q src tests` → exit 0
- tracked legacy rerun receipt: `identical_rerun_audit.json` → 내부 일관성 PASS, 신규 query/fetch 0/0, score/Stage variance 0/0
- network search/query/fetch/provider/LLM/subagent: 실행하지 않음

위 221/7,204/15 PASS는 초기 branch 내부 실행 영수증이다. GitHub Actions 독립 실행이 green이 되기 전에는 `CLEAN_PR_READY` 근거로 사용하지 않는다. 독립 검수 수정 후 현재 head의 실제 결과는 PR checks와 후속 검증 기록을 우선한다.

## Git payload hard gate

- `git diff --check`: PASS
- 초기 packaging changed file: 44개
- 초기 additions/deletions: 5,358 / 46
- 초기 changed blob byte 합계: 10,478,279 bytes
- tracked forbidden raw/cache/output: 0
- 10 MiB 초과 added blob: 0
- archive/binary: 0
- source giant commit ancestry 포함: false
- worktree/remote 일치: 후속 수정 commit 및 push 직후 `git status --short`와 `git rev-list --left-right --count HEAD...origin/fix/e2r-gate1-clean-merge-20260822`로 확인한다.

추가 blob 상위 10개(최종 worktree byte size 기준):

1. `clean_merge_payload_manifest.json` — 3,972,846 bytes
2. `external_artifact_receipt.json` — 3,750,476 bytes
3. `docs/operational/e2r_v5_full_test_result.log` — 1,060,957 bytes
4. `source_graph_explorer.py` — 385,341 bytes
5. `current_researcher_mode.py` — 323,006 bytes
6. `test_e2r_v5_semantic_research_saturation.py` — 245,232 bytes
7. `research_supervisor.py` — 164,964 bytes
8. `prompt_projection.py` — 129,995 bytes
9. `000660_component_memos_compact.jsonl` — 70,192 bytes
10. `evidence_gap.py` — 61,606 bytes

정확한 최종 `git diff --stat`, `git diff --name-status`, `git diff --numstat`, `git ls-tree -r -l HEAD`, `git count-objects -vH`는 commit 이후 clean HEAD를 기준으로 재확인한다.
