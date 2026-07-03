# Census v4 0701 Brain/Web Accepted Claim Metric Split Patch Result

작성 시점: 2026-07-02 KST  
patched diagnostic: `output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1`  
as_of_date: `2026-07-01`

최신 종합 교차검증과 다음 패치 우선순위는 아래 문서를 우선한다.

```text
docs/0701/census_v4_0701_raw_assertion_rejection_audit_patch_and_stage_truth_2026-07-02.md
docs/0701/census_v4_0701_brain_web_promotion_guard_patch_result_2026-07-02.md
docs/0701/census_v4_0701_next_agent_hard_review_after_metricsplit_2026-07-02.md
```

## 한 줄 결론

```text
OpenDART official accepted claim과 web/news/LLM accepted claim이 이제 gate에서 분리된다.
공식 claim 1개가 있어도 web/LLM accepted claim이 0개면 Brain/Web evidence pass는 막힌다.
```

쉬운 예:

```text
이전에는 "Brain/Web accepted 1개"라고 뭉뚱그려 보일 수 있었다.
그 1개가 사실 OpenDART 공식 공시 claim이면 "웹/LLM이 점수 claim을 찾았다"고 말하면 안 된다.

이제는:
  brain_accepted_claim_count = 1
  official_accepted_claim_count = 1
  web_or_llm_accepted_claim_count = 0

로 분리된다.
```

## 코드 패치

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_web_readiness_gate.py
```

추가/변경된 gate metric:

```text
brain_accepted_claim_count
official_accepted_claim_count
web_news_accepted_claim_count
llm_extracted_accepted_claim_count
web_or_llm_accepted_claim_count
full_thesis_claim_count
```

핵심 규칙:

```text
brain_accepted_claim_count:
  Brain/Web origin accepted claim 전체

official_accepted_claim_count:
  OpenDART/KIND/KRX/CompanyGuide/issuer official 계열 claim

web_news_accepted_claim_count:
  web_fetched_documents와 연결되거나 Naver/Web/News provider에서 온 claim

llm_extracted_accepted_claim_count:
  LLM extractor run의 raw_assertion_ids에서 나온 accepted claim

web_or_llm_accepted_claim_count:
  web_news_accepted 또는 llm_extracted accepted claim의 union

full_thesis_claim_count:
  full_thesis_claim=true인 accepted claim
```

운영 gate 변경:

```text
BRAIN_AND_WEB_ACQUISITION_ENABLED / FULL_LIVE_BRAIN_CENSUS에서는
accepted claim 전체가 아니라 web_or_llm_accepted_claim_count가 operational minimum을 채워야 한다.
```

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_bundle_export \
  tests.test_research_brain_v4_evidence_extraction_from_real_document -v
```

결과:

```text
Ran 28 tests
OK
```

새 핵심 테스트:

```text
test_official_only_brain_claim_does_not_count_as_web_or_llm_accepted_claim
```

검증 내용:

```text
OpenDART claim:
  brain_accepted_claim_count = 1
  official_accepted_claim_count = 1
  web_or_llm_accepted_claim_count = 0
  web_news_accepted_claim_count = 0
  llm_extracted_accepted_claim_count = 0
  verdict = BLOCKED
```

## Post-Patch Diagnostic

실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1 \
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
```

Gate 핵심 수치:

```text
verdict = BLOCKED

brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_news_accepted_claim_count = 0
llm_extracted_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
full_thesis_claim_count = 0

web_fetched_document_count = 4
web_rejected_document_count = 5
post_extraction_web_rejected_documents = 4
brain_promoted_stage_row_count = 1
stage_scope:
  CENSUS_EVENT_BOARD = 3390
  BRAIN_WEB_PARTIAL = 1
```

Blockers:

```text
web/LLM accepted claim count is zero
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 3/20
Brain/Web operational minimum web/news search calls not met: 3/20
Brain/Web operational minimum fetched documents not met: 4/10
Brain/Web operational minimum claim extractor attempts not met: 4/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

## 해석

이번 실행은 겉으로 보면 `BRAIN_WEB_PARTIAL` 1개가 다시 생겼다.
하지만 새 metric 덕분에 그 partial이 웹/LLM accepted claim 때문이 아니라 official accepted claim 때문이라는 사실이 드러난다.

따라서 운영 판단은:

```text
Brain/Web partial trace exists.
그러나 web/LLM accepted claim은 0개다.
그러므로 BRAIN_WEB_EVIDENCE_PASS는 false가 맞다.
```

## 남은 P0

```text
1. official-only partial promotion을 더 엄격히 제한할지 결정/패치.
2. feedback retry가 만든 새 source task가 web/LLM accepted claim까지 이어지게 acquisition loop 강화.
3. full thesis runner eligible row 0 문제 해결.
4. C01~C32 source-backed replay 6/32 -> 32/32 확장.
```

## 최종 판단

```text
metric split 패치는 성공했다.
하지만 전체 goal completion은 아직 아니다.
```

이제부터는 “accepted claim 몇 개”가 아니라 “그 accepted claim이 official인지, web/news인지, LLM extractor에서 온 것인지, full thesis인지”를 분리해서 봐야 한다.
