아니. **지금 레포 기준으로는 네이버/웹검색이 전 종목에 붙고, LLM 두뇌가 알아서 판단하는 Census가 아니다.**
그리고 내가 직전에 준 v4 Goal도 “못 속이게 만드는 audit”은 강하게 넣었지만, **“네이버/뉴스/IR/리포트 웹획득 + LLM 두뇌 실행을 반드시 하라”는 pass 조건은 더 노골적으로 박아야 해.**

현재 레포에서 보이는 문제는 이거야.

```text
1. Census runner는 아직 구형 경로가 남아 있음
2. run_census_mode 안에서 llm_calls=0으로 SLA를 만들고 있음
3. build_stage_status에 accepted_claims=(), score_contributions=()를 넘기는 경로가 남아 있음
4. v3 report는 runtime_seconds=3.67초라고 함
5. 3391개 전 종목에 네이버/웹/LLM을 진짜 돌렸다면 3.67초는 불가능
```

실제 `census_runner.py`를 보면 `build_stage_status(... accepted_claims=(), score_contributions=())`가 그대로 있고, SLA 생성 때 `llm_calls=0`으로 들어간다. 이건 “LLM 두뇌가 전 종목을 판단했다”가 아니라, 적어도 해당 runner 경로에서는 **LLM 호출 없이 Census 상태 row를 만든 것**에 가깝다. ([GitHub][1])

v3 acceptance report도 `Research Brain plan count 92`, `accepted claim 92`, `StageCourt trace 92`를 말하지만 동시에 `runtime_seconds: 3.67`이라고 적혀 있다. 이건 전 종목 네이버/웹검색 + LLM 독해가 아니라, 기존 산출물/leaf/replay 기반 재조립에 가까운 실행 시간이다. ([GitHub][2])

원래 최종 목표는 LLM이 “이 종목 몇 점?”을 찍는 게 아니라, 원문에서 claim을 뽑고, 주체·날짜·현재성·대상회사 직접 귀속 여부를 검증한 뒤, 코드가 deterministic score/stage를 계산하는 구조야. 즉 **LLM 두뇌는 문서 독해와 조사계획을 해야 하고, 코드는 claim 검증과 Stage 판정을 해야 한다.**

그래서 답은 이거야.

```text
현재 되는 것:
- Census report/상태표 생성
- 일부 기존 claim/replay 기반 상태 분포 생성
- audit 형식 일부 존재

현재 안 되는 것:
- 전 종목 대상 네이버/웹/뉴스/IR/리포트 real acquisition
- LLM Planner가 각 후보를 실제로 읽고 routing
- LLM Claim Extractor가 실제 문서에서 claim 추출
- 웹/네이버 검색 결과가 SourceTask → Evidence OS → Stage까지 연결
- llm_calls / web_search_calls / naver_calls / provider_fetches가 pass 조건에 박힘
```

그러니까 다음 Goal에는 **“Real Brain + Real Web/News Acquisition Gate”**를 별도 섹션으로 반드시 추가해야 해.

아래를 기존 v4 Goal 뒤에 그대로 덧붙이면 돼.

```text
================================================================================
추가 필수 섹션: Real Brain + Web/News/Naver Acquisition Gate
================================================================================

현재 문제:
Census v3/v4가 FULL_UNIVERSE_STAGE_MAP_PASS를 주장하더라도, 실제로는 네이버/웹/뉴스/IR/리포트 검색과 LLM Brain 판단이 실행되지 않을 수 있다.
이번 Gate는 “두뇌가 실제로 판단했는가”와 “웹/뉴스 source가 실제로 획득되었는가”를 leaf artifact로 증명한다.

절대 원칙:
1. llm_calls=0이면 “LLM Brain used”라고 말할 수 없다.
2. naver_search_call_count=0, web_search_call_count=0이면 “web/news search used”라고 말할 수 없다.
3. 네이버/웹검색은 전 종목 무차별 실행이 아니라, DepthPolicy가 L3/L4 이상으로 올린 종목에 bounded fallback으로 실행한다.
4. DART/KIND/KRX/CompanyGuide로 해결 가능한 source gap은 네이버로 먼저 보내지 않는다.
5. 네이버/뉴스 snippet은 score evidence가 아니다.
6. 네이버/뉴스/IR/리포트 full source가 fetch되고, quote/date/subject/target/current validity가 검증되어야 score evidence가 된다.
7. LLM Planner는 route/source task/query intent를 만들 수 있지만 score/stage를 직접 만들 수 없다.
8. LLM Claim Extractor는 문서 원문에서 RawAssertion/EvidenceClaim을 추출해야 하며 primitive/score/stage를 미리 보여주면 안 된다.
9. Research Brain MemoryCard는 조사 방향을 주는 판례집이지 current claim이 아니다.
10. report가 아니라 planner_runs.jsonl, llm_prompt_response.jsonl, web_search_results.jsonl, source_task_executions.jsonl, accepted_claims.jsonl이 source of truth다.

================================================================================
1. Brain Execution Modes
================================================================================

Census는 실행 모드를 명확히 분리한다.

A. OFFICIAL_BASELINE_ONLY
- LLM Brain 사용 안 함
- 네이버/웹검색 사용 안 함
- 결과 라벨은 baseline map까지만 가능
- FULL_UNIVERSE_STAGE_MAP_PASS 가능하더라도 “Brain/Web disabled”로 표시
- READY_FOR_DAILY_TRIGGER_INTEGRATION 금지

B. BRAIN_TRIAGE_ENABLED
- L3/L4 선별 종목에 LLM Planner 사용
- top-k archetype / source task / query intent 생성
- score/stage 직접 출력 금지

C. BRAIN_AND_WEB_ACQUISITION_ENABLED
- LLM Planner + bounded web/news/Naver acquisition 실행
- web/news/IR/report source를 Evidence OS로 통과시킴
- 이 모드만 “두뇌 + 웹 조사 Census”라고 부를 수 있음

D. FULL_LIVE_BRAIN_CENSUS
- official baseline + LLM Brain + selected web/news acquisition + Evidence OS + StageCourt
- 실제 운영 전 최종 목표

Acceptance:
- run_mode must be one of above.
- If run_mode != BRAIN_AND_WEB_ACQUISITION_ENABLED or FULL_LIVE_BRAIN_CENSUS, do not claim “네이버/웹/LLM 두뇌가 작동했다.”
- report_claims_brain_but_llm_calls_zero_count = 0.
- report_claims_web_but_web_calls_zero_count = 0.

================================================================================
2. LLM Brain Planner Mandatory Trace
================================================================================

For every symbol selected for L3_RESEARCH_BRAIN_TRIAGE or deeper:

PlannerRun:
{
  "planner_run_id": "...",
  "symbol": "...",
  "company_name": "...",
  "input_refs": {
    "census_stage_status_id": "...",
    "source_timeline_id": "...",
    "last_effective_thesis_id": "...",
    "memory_card_ids": [],
    "baseline_event_ids": []
  },
  "provider_name": "...",
  "model": "...",
  "prompt_hash": "...",
  "response_hash": "...",
  "raw_prompt_path": "...",
  "raw_response_path": "...",
  "llm_call_status": "SUCCESS|PROVIDER_FAILED|VALIDATION_FAILED|SKIPPED_BY_DEPTH_POLICY",
  "top_k_archetype_hypotheses": [],
  "positive_thesis": "...",
  "counter_thesis": "...",
  "must_verify_primitives": [],
  "source_task_drafts": [],
  "query_intents": [],
  "do_not_promote_reasons": [],
  "forbidden_keys_detected": []
}

Rules:
- Planner prompt may include Candidate/Census events, source timeline, memory card summaries, source policy.
- Planner prompt must not include future MFE/MAE/outcome labels.
- Planner output must not include score, stage, hard_break final, current_score_eligible.
- If LLM provider fails, candidate becomes PlannerPending / ProviderPending, not low score.

Acceptance:
- research_brain_selected_symbol_count > 0.
- llm_planner_call_count >= min(30, selected_deep_symbol_count) unless EXTERNAL_PROVIDER_BLOCKER.
- llm_planner_success_count > 0.
- planner_output_score_stage_key_count = 0.
- planner_provider_failure_final_score_count = 0.
- Every L3/L4 symbol has planner_run_id or explicit skipped/provider_failed reason.
- If llm_planner_call_count = 0, final label cannot exceed OFFICIAL_BASELINE_MAP_PASS.

Required leaf artifacts:
output/census_v4/YYYY-MM-DD/planner_runs.jsonl
output/census_v4/YYYY-MM-DD/llm_prompts.jsonl
output/census_v4/YYYY-MM-DD/llm_responses.jsonl

Tests:
tests/test_census_v4_brain_planner_real_calls.py
tests/test_census_v4_no_brain_claim_with_zero_llm_calls.py
tests/test_census_v4_planner_output_no_score_stage.py

================================================================================
3. Web / Naver / News Acquisition Gate
================================================================================

Census must support bounded web/news acquisition for selected symbols.

Source families:
- NaverSearch
- GeneralWebSearch
- TrustedNews
- IssuerIR
- ReportPDF
- BrokerReportPublicPDF
- IndustryMedia
- CompanyNewsroom

Important:
- Naver/general web is not used for every ticker.
- It is only used after Research Brain selects a source task requiring external verification.
- Official source comes first.
- Web/Naver is fallback or discovery for missing primitive, not primary FCF/contract source.

WebSearchTask:
{
  "web_task_id": "...",
  "symbol": "...",
  "company_name": "...",
  "source_task_id": "...",
  "query_intent": "...",
  "llm_generated_query": "...",
  "allowed_domains": [],
  "forbidden_domains": [],
  "date_window": {},
  "max_results": 10,
  "max_fetches": 3,
  "search_provider": "NaverSearch|GeneralWebSearch|TrustedNews",
  "reason_from_memory": "...",
  "primitive_gap": "...",
  "official_source_attempted_first": true
}

WebSearchResult:
{
  "web_task_id": "...",
  "query": "...",
  "provider": "...",
  "result_count": 0,
  "selected_result_count": 0,
  "fetched_document_count": 0,
  "snippet_only_count": 0,
  "full_source_count": 0,
  "provider_error": null
}

Rules:
- snippet_only_count can create follow-up task only.
- full_source_count with fetched document can go to Evidence OS.
- score from snippet is forbidden.
- Naver result without full article fetch is not score evidence.
- If news source is duplicate/repost, mark duplicate and do not score unless original source is found.
- If article subject differs from target company, issuer_scoped=false.

Acceptance:
- web_search_task_count > 0 in BRAIN_AND_WEB_ACQUISITION_ENABLED mode.
- naver_search_call_count > 0 OR trusted_news_search_call_count > 0 OR documented external blocker.
- web_fetched_document_count > 0 OR documented source gap.
- snippet_to_score_count = 0.
- web_claim_accepted_count >= 1 OR all web docs rejected with reasons.
- official_source_attempted_first_count == web_search_task_count for DART/KIND/IR-solvable tasks.
- FCF_gap_sent_to_naver_count = 0.
- contract_gap_sent_to_naver_before_DART_count = 0.
- news_article_wrong_subject_score_count = 0.

Required leaf artifacts:
output/census_v4/YYYY-MM-DD/web_search_tasks.jsonl
output/census_v4/YYYY-MM-DD/web_search_results.jsonl
output/census_v4/YYYY-MM-DD/web_fetched_documents.jsonl
output/census_v4/YYYY-MM-DD/web_rejected_documents.jsonl

Tests:
tests/test_census_v4_web_naver_acquisition.py
tests/test_census_v4_snippet_never_scores.py
tests/test_census_v4_official_first_before_naver.py
tests/test_census_v4_wrong_subject_news_rejected.py

================================================================================
4. LLM Claim Extractor Realness Gate
================================================================================

For fetched web/news/IR/report documents, LLM Claim Extractor must run unless document is structured official API.

LLMClaimExtractionRun:
{
  "extractor_run_id": "...",
  "document_id": "...",
  "symbol": "...",
  "provider_name": "...",
  "model": "...",
  "prompt_hash": "...",
  "response_hash": "...",
  "raw_prompt_path": "...",
  "raw_response_path": "...",
  "status": "SUCCESS|PROVIDER_FAILED|VALIDATION_FAILED|SKIPPED_STRUCTURED_API",
  "raw_assertion_ids": [],
  "rejected_reason": null
}

Rules:
- Raw extractor prompt must not see desired primitive_id, score, stage, green gate, MFE/MAE.
- Extractor returns claims/assertions only.
- Primitive mapping happens after extraction.
- If extractor fails on unstructured text, document remains mention-only/pending.
- Rule fallback can score only official structured API records with explicit fields/date/subject.

Acceptance:
- unstructured_document_count > 0 in web-enabled mode.
- llm_claim_extractor_attempt_count >= unstructured_document_count unless external blocker.
- llm_claim_extractor_success_count > 0 OR all unstructured docs rejected/pending with reasons.
- rule_fallback_unstructured_score_count = 0.
- contract_visible_to_raw_extractor_count = 0.
- primitive_gap_visible_to_raw_extractor_count = 0.
- event_summary_used_as_quote_count = 0.
- forced_positive_polarity_count = 0.
- forced_current_temporal_count = 0.
- forced_target_subject_count = 0.

Required leaf artifacts:
output/census_v4/YYYY-MM-DD/claim_extractor_runs.jsonl
output/census_v4/YYYY-MM-DD/raw_assertions.jsonl
output/census_v4/YYYY-MM-DD/adjudicated_claims.jsonl
output/census_v4/YYYY-MM-DD/accepted_claims.jsonl

Tests:
tests/test_census_v4_llm_claim_extractor_realness.py
tests/test_census_v4_no_contract_visible_to_extractor.py
tests/test_census_v4_unstructured_rule_fallback_cannot_score.py

================================================================================
5. Brain-to-Source-to-Claim Trace
================================================================================

For every accepted claim produced from Brain/Web path:

BrainTrace:
{
  "symbol": "...",
  "planner_run_id": "...",
  "source_task_id": "...",
  "web_task_id": null_or_id,
  "document_id": "...",
  "extractor_run_id": "...",
  "raw_assertion_id": "...",
  "adjudicated_claim_id": "...",
  "accepted_claim_id": "...",
  "primitive_state_id": "...",
  "score_contribution_id": "...",
  "stagecourt_trace_id": "...",
  "census_stage_status_id": "..."
}

Acceptance:
- Every web-derived accepted claim has full BrainTrace.
- Every LLM-derived accepted claim has extractor_run_id.
- Every score contribution using LLM/web claim references accepted_claim_id.
- brain_trace_missing_count = 0.
- claim_to_stage_trace_missing_for_brain_claim_count = 0.

Required artifact:
output/census_v4/YYYY-MM-DD/brain_to_claim_trace.jsonl

Tests:
tests/test_census_v4_brain_to_claim_trace.py

================================================================================
6. Run Mode Hard Labels
================================================================================

Readiness label must depend on actual Brain/Web usage.

Allowed labels:
- OFFICIAL_BASELINE_MAP_PASS
  official/structured baseline only, no LLM/web.
- BRAIN_TRIAGE_PASS
  LLM planner used for selected symbols, but no web/news acquisition.
- BRAIN_WEB_EVIDENCE_PASS
  LLM planner + web/news acquisition + LLM extraction + accepted claims.
- FULL_LIVE_BRAIN_CENSUS_PASS
  official baseline + LLM planner + web/news/IR/report acquisition + Evidence OS + StageCourt across selected deep symbols.
- EXTERNAL_PROVIDER_BLOCKER_NOT_READY

Rules:
- If llm_planner_call_count = 0, cannot exceed OFFICIAL_BASELINE_MAP_PASS.
- If web_search_task_count = 0, cannot claim BRAIN_WEB_EVIDENCE_PASS.
- If llm_claim_extractor_attempt_count = 0 on unstructured docs, cannot claim BRAIN_WEB_EVIDENCE_PASS.
- If accepted_claim_count from web/LLM = 0, cannot claim Brain/Web evidence produced; may claim Brain/Web search attempted with no accepted claims.
- If all web docs rejected, report why and stay below BRAIN_WEB_EVIDENCE_PASS unless official claim path suffices.

================================================================================
7. Minimum Brain/Web Acceptance for This Goal
================================================================================

To answer the user’s concern, this Goal must explicitly prove Brain/Web is active.

Minimum run:
- selected_deep_symbol_count >= 30
- llm_planner_call_count >= 30
- web_search_task_count >= 20
- naver_search_call_count + trusted_news_search_call_count + general_web_search_call_count >= 20
- web_fetched_document_count >= 10
- llm_claim_extractor_attempt_count >= 10
- web_or_llm_accepted_claim_count >= 3 OR all fetched docs rejected with structured reasons and final label below BRAIN_WEB_EVIDENCE_PASS
- brain_to_claim_trace_count >= web_or_llm_accepted_claim_count
- official_first_violation_count = 0
- snippet_to_score_count = 0
- provider failure final score count = 0

If these fail due code:
- self-repair loop must patch and rerun.

If these fail due external API/provider:
- EXTERNAL_PROVIDER_BLOCKER_NOT_READY with exact provider/key/error.

================================================================================
8. Required Audits
================================================================================

Generate:

docs/operational/census_mode_v4_brain_planner_audit.json
docs/operational/census_mode_v4_web_naver_acquisition_audit.json
docs/operational/census_mode_v4_llm_claim_extraction_audit.json
docs/operational/census_mode_v4_brain_to_claim_trace_audit.json
docs/operational/census_mode_v4_run_mode_honesty_audit.json

Critical counts:
- llm_claimed_but_zero_calls_count
- web_claimed_but_zero_search_count
- naver_claimed_but_zero_naver_count
- brain_plan_without_prompt_hash_count
- planner_output_score_stage_key_count
- source_task_without_brain_trace_count
- web_result_snippet_to_score_count
- web_doc_without_fetch_count
- web_doc_wrong_subject_to_score_count
- llm_extractor_prompt_primitive_leak_count
- llm_extractor_prompt_score_stage_leak_count
- unstructured_rule_fallback_score_count
- brain_claim_missing_stage_trace_count
- official_first_violation_count

All critical counts must be 0.

================================================================================
9. Final Report Additions
================================================================================

Acceptance report must include:

- run_mode
- llm_planner_call_count
- llm_planner_success_count
- llm_planner_provider/model
- web_search_task_count
- naver_search_call_count
- trusted_news_search_call_count
- general_web_search_call_count
- web_result_count
- web_fetched_document_count
- snippet_only_count
- llm_claim_extractor_attempt_count
- llm_claim_extractor_success_count
- web_or_llm_accepted_claim_count
- brain_to_claim_trace_count
- official_first_violation_count
- snippet_to_score_count
- report_claims_brain_but_llm_calls_zero_count
- report_claims_web_but_web_calls_zero_count
- final honest label

If LLM/web is not active, report must say:
“Census executed in official baseline / ledger refresh mode. LLM Brain and Naver/Web evidence acquisition were not exercised.”

================================================================================
10. Prohibitions
================================================================================

- Do not say “두뇌가 판단했다” if llm_planner_call_count = 0.
- Do not say “네이버/웹을 썼다” if naver/web call count = 0.
- Do not say “LLM이 원문 claim을 추출했다” if llm_claim_extractor_attempt_count = 0.
- Do not count existing report replay as web search.
- Do not count existing claim ledger as new web/LLM claim.
- Do not count Research Memory as current web evidence.
- Do not use Naver snippets as score.
- Do not use web/news before official source for official-solvable gaps.
- Do not run unbounded Naver/web search over all tickers.
- Do not hide external provider blocker.
```

정리하면:

```text
지금 goal에는 “속이지 못하게”는 꽤 들어갔다.
하지만 “네이버/웹 + LLM 두뇌 실제 사용”은 별도 hard gate로 더 박아야 한다.
```

그리고 중요한 건, **네이버를 전 종목에 다 돌리는 게 정답은 아니야.**
그렇게 하면 삼성전자 하나에서 캐시 수천 개 쌓이던 예전 문제가 전체 시장으로 폭발한다. 실제로 과거 삼성전자 실행은 initial 6 queries에서 search result 600개, 이후 query 22개, top_results=null, cache 2천 개 이상으로 커졌던 기록이 있어.

정상 플로우는 이거야.

```text
전 종목:
official baseline + price + 기존 ledger + source timeline

선별 종목:
LLM Brain planner

더 필요한 종목:
bounded Naver/Web/News/IR/Report source task

점수:
Evidence OS accepted claim만
```

즉 **두뇌는 전 종목에 “무식하게 네이버 검색”하는 게 아니라, 전 종목 baseline을 본 뒤 깊게 볼 종목과 찾을 증거를 고르는 역할**이어야 해. 그렇지만 지금처럼 `llm_calls=0`이면 두뇌가 돈 게 아니니까, 위 gate를 추가해야 진짜로 확인 가능해.

[1]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/src/e2r/census/census_runner.py "raw.githubusercontent.com"
[2]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/docs/operational/census_mode_v3_acceptance_report.md "raw.githubusercontent.com"
