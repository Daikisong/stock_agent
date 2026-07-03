# Census v4 0701 Brain/Web Partial Promotion Guard Patch Result

작성 시점: 2026-07-02 KST  
patched diagnostic: `output/census_v4/2026-07-01-brain-web-diagnostic-promotionguard-v1`  
as_of_date: `2026-07-01`

이 문서는 `promotionguard-v1` 당시 Brain/Web diagnostic 기준이다.

> 최신 주의: 이 문서는 `promotionguard-v1` 기준이다.
> 이후 `census_v4_0701_raw_assertion_rejection_audit_patch_and_stage_truth_2026-07-02.md`에서
> rejected RAW assertion 단위 장부와 fallback reason 분류를 추가했다.
> 최신 Brain/Web diagnostic은 `rawreject-v4`이며, 여전히 `BRAIN_WEB_PARTIAL row = 0`,
> `web_or_llm_accepted_claim_count = 0`, `FULL_THESIS row = 0`이다.

## 한 줄 결론

```text
official-only accepted claim은 더 이상 BRAIN_WEB_PARTIAL row로 승격되지 않는다.
```

쉬운 예:

```text
이전:
  웹 조사반 이름표를 달았는데 실제 근거는 DART 공시 1개였다.
  그래서 BRAIN_WEB_PARTIAL row가 1개 생겼다.

패치 후:
  DART 공시 1개는 official claim으로 남는다.
  하지만 web/news 또는 LLM-extracted accepted claim이 0개면
  BRAIN_WEB_PARTIAL 이름표를 붙이지 않는다.
```

## 코드 패치

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
```

핵심 변경:

```text
1. _brain_claim_source_split 추가.
2. Brain claim을 official / web-news / LLM-extracted로 분리.
3. _brain_stage_promotion_audit에서 web_or_llm_accepted_claim_count=0이면 BLOCKED.
4. StageCourt trace가 web/LLM accepted claim을 포함하지 않으면 BRAIN_WEB_PARTIAL promotion 차단.
5. _promote_brain_stage_rows도 trace별 accepted_claim_ids가 web/LLM claim과 교집합이 없으면 skip.
```

새 audit metric:

```text
web_or_llm_accepted_claim_count
web_news_accepted_claim_count
llm_extracted_accepted_claim_count
official_accepted_claim_count
brain_stage_trace_without_web_or_llm_claim_count
```

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_bundle_export \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_cutover_contract_blind_extraction \
  tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 66 tests
OK
```

새 핵심 테스트:

```text
test_official_only_brain_claim_does_not_promote_as_brain_web_partial
```

검증 내용:

```text
official-only OpenDART accepted claim:
  official_accepted_claim_count = 1
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_without_web_or_llm_claim_count = 1
  brain_stage_promotion_audit.verdict = BLOCKED
  BRAIN_WEB_PARTIAL row = 0
```

## Post-Patch Diagnostic

실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-promotionguard-v1 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-provider codex_cli \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate brain_web \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --write-operational-docs false
```

결과:

```text
stdout = NOT_READY
process exit code = 1
```

중요 수치:

```text
readiness_verdict.verdict = NOT_READY
brain_web_readiness_gate_audit.verdict = BLOCKED
brain_stage_promotion_audit.verdict = BLOCKED

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391
  BRAIN_WEB_PARTIAL = 0
  FULL_THESIS = 0

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_news_accepted_claim_count = 0
llm_extracted_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
full_thesis_claim_count = 0

brain_promoted_stage_row_count = 0
brain_stage_trace_without_web_or_llm_claim_count = 1

planner_runs = 22
web_search_tasks = 4
web_fetched_documents = 8
web_rejected_documents = 11
claim_extractor_runs = 8
raw_assertions = 184
accepted_claims.jsonl line count = 93
```

Blockers:

```text
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 4/20
Brain/Web operational minimum web/news search calls not met: 4/20
Brain/Web operational minimum fetched documents not met: 8/10
Brain/Web operational minimum claim extractor attempts not met: 8/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

Stage promotion blockers:

```text
web/LLM accepted brain claim count is zero for BRAIN_WEB_PARTIAL promotion
brain StageCourt traces have no web/LLM accepted claim support: 1
```

## 해석

이번 패치는 pass를 만들기 위한 패치가 아니다.
오히려 과대포장되던 partial row를 제거한 패치다.

```text
metricsplit-v1:
  BRAIN_WEB_PARTIAL = 1
  but web_or_llm_accepted_claim_count = 0

promotionguard-v1:
  BRAIN_WEB_PARTIAL = 0
  web_or_llm_accepted_claim_count = 0
```

쉬운 예:

```text
잘못된 합격증 1장을 회수했다.
합격자가 생긴 것은 아니다.
하지만 이제 출석부와 합격증을 섞어 말하지 않게 됐다.
```

## 남은 P0

### P0-1. Raw assertion rejection audit

`rawreject-v4` 기준 1차 패치는 완료됐다.
이제 `RAWLLM-*` assertion 단위로 왜 탈락했는지 `raw_assertion_rejections.jsonl`에 남는다.

```text
raw_assertions = 151
raw_assertion_rejections = 62
accepted web/LLM claim = 0

rejection_reason:
  primitive_mapping_rejected = 29
  target_scope_or_directness_rejected = 27
  temporal_status_rejected = 5
  anchor_validation:quote_not_found_in_document_text = 1
```

다음 질문에 답할 수 있게 됐다.

```text
각 RAWLLM assertion이 target mismatch였나?
temporal mismatch였나?
primitive mapping 실패였나?
score eligibility 실패였나?
gap과 무관했나?
```

남은 보강:

```text
fallback rejection row의 verification_status/source_type/provider_mode 같은 null 축을
adjudicated_claims/evidence_documents/raw_assertions/claim_extractor_runs와 join해서 채워야 한다.
```

### P0-2. Accepted web/LLM claim unblock

기준을 낮추는 게 아니라, 탈락 사유를 보고 acquisition/extractor/mapper를 고쳐야 한다.

```text
목표:
  source-backed, direct target, current, primitive-mapped web/LLM claim >= 1
```

### P0-3. Production FULL_THESIS runner

아직 운영 row는 0개다.

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
```

### P0-4. C01~C32 replay parity

```text
source_backed_ready_count = 6 / 32
guard_replay_ready_count = 6 / 32
missing_required_archetype_count = 26
```

## 최종 판단

```text
official-only BRAIN_WEB_PARTIAL promotion 문제는 패치됐다.
하지만 Brain/Web evidence pass는 아직 아니다.
운영 FULL_THESIS Stage도 아직 0개다.
```

다음 에이전트는 이제 `BRAIN_WEB_PARTIAL 1개가 있네`라는 오해를 하면 안 된다.
최신 기준은 `rawreject-v4`이고, 여기서도 Brain/Web partial row는 0개다.
