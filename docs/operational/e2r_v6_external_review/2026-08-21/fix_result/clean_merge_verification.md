# Gate 1 clean merge 검증 기록

## Git 기준

- source branch: `fix/e2r-stable-gap-fixpoint-20260821`
- source HEAD: `c831cc9a95144c77206db335d61cd98e2cab7bdf`
- clean branch: `fix/e2r-gate1-clean-merge-20260822`
- clean base: `origin/main` / `7e3f71793465c0e4d03cce57f9a75c2bb40943c2`
- clean HEAD: `THIS_COMMIT` (이 문서를 포함하는 clean branch의 단일 packaging commit)
- source giant commit ancestry: `false`
- ancestry command: `git merge-base --is-ancestor c831cc9a95144c77206db335d61cd98e2cab7bdf HEAD`

`THIS_COMMIT`은 자기 자신의 commit SHA를 파일 내용에 넣을 수 없는 Git의 순환 참조를 피하기 위한 표기다. 외부 검토자는 `git rev-parse HEAD`로 실제 SHA를 확인한다. 예를 들어 영수증 안에 자기 영수증의 최종 SHA를 다시 넣을 수 없는 것과 같은 이유다.

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

전체 legacy diff 14,410개를 먼저 분류했고, 원본에서 41개를 선택했다. 이 clean PR에서 새로 만든 packaging 문서 3개를 더해 최종 payload는 44개다. 전체 분류 행은 `clean_merge_payload_manifest.json`에, 제외 artifact 14,370개(legacy 추적 14,369개와 legacy worktree의 ignored raw 1개)는 `external_artifact_receipt.json`에 path/크기/SHA-256 단위로 기록했다.

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

## 테스트와 재현 검증

- focused: `PYTHONPATH=src python -m unittest tests.test_e2r_evidence_gap_fixpoint tests.test_e2r_v5_semantic_research_saturation tests.test_e2r_v5_stagecourt tests.test_e2r_v5_phase94_runner_contract -v` → 221 PASS, failure/error/skip 0
- full: `PYTHONPATH=src python -m e2r.cli.run_e2r_v5_full_test_evidence --workspace-root .` → 7,204 PASS, failure/error/skip 0, exit 0
- independent acceptance compile: `PYTHONPATH=src python -m e2r.cli.compile_e2r_v5_independent_acceptance --workspace-root .` → reviewer 10/10, critical 0, PASS
- Phase100: `PYTHONPATH=src python -m unittest tests.test_e2r_v5_phase100_independent_acceptance -v` → 15 PASS, failure/error/skip 0
- compile: `PYTHONPATH=src python -m compileall -q src tests` → exit 0
- deterministic offline rerun: `identical_rerun_audit.json` → PASS, 신규 query/fetch 0/0, score/Stage variance 0/0
- network search/query/fetch/provider/LLM/subagent: 실행하지 않음

## Git payload hard gate

- `git diff --check`: PASS
- changed file: 44개
- additions/deletions: 5,358 / 46
- 최종 changed blob byte 합계: 10,478,279 bytes
- tracked forbidden raw/cache/output: 0
- 10 MiB 초과 added blob: 0
- archive/binary: 0
- source giant commit ancestry 포함: false
- worktree clean: commit 및 push 직후 `git status --short`가 빈 출력이고, 원격 HEAD와 0/0인 상태로 확인한다.

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
