맞아. 지금은 **“막는 gate를 더 추가”할 때가 아니라, 왜 C05 10개 같은 이상한 결과가 나왔는지 원인을 끝까지 파고, 연구자료가 실제 운영 두뇌로 제대로 이어지게 고쳐야 하는 단계**야.

내가 본 결론은 이거야.

```text
지금 문제의 본질:
연구자료 → 운영 증거 수집 → primitive claim → full thesis score
이 경로가 자연스럽게 이어진 게 아니라,
Census event-board / refresh queue에서 쉬운 C05 계약형 문맥만 production full-thesis로 새고 있음.

그래서 결과가:
C05 10개
27.9998 / 50.0 / 77.9998 반복
required_positive_missing 10/10
green_gap 10/10
삼성/하이닉스 production full thesis 미승격
으로 나온 것.
```

0705 감사 문서 자체도 이걸 정확히 인정하고 있어. `FULL_THESIS_PRODUCTION_PASS`는 “모든 아키타입에서 의미 있는 full thesis가 운영 통과했다”가 아니라, “claim-backed FULL_E2R_100 score path가 production run에서 10개 row에 대해 닫혔다”는 뜻이고, 그 10개가 전부 C05이며 required-positive/green gap이 남아 있다고 적고 있어. 즉 이건 **score path closed**이지 **meaningful full thesis passed**가 아니야. ([GitHub][1])

---

# 지금 진짜 원인

## 1. C05 10개는 “전 시장에서 자연스럽게 뽑힌 10개”가 아님

0705 문서에 따르면 production runner는 후보 23개 중 10개를 promoted 했고, 그 10개가 전부 C05였어. 더 중요한 건 seed 단계의 `target_archetype_counts`가 전부 `UNKNOWN: 85`였다는 점이야. 즉 seed가 애초부터 “이 종목은 C05다”라고 명확히 준 게 아니라, `source_primary_archetype=C05`라는 event-board 문맥이 planner에 들어가고, planner top1도 전부 C05가 되면서 최종 C05로 닫힌 구조야. ([GitHub][1])

이건 “두뇌가 전 아키타입을 보고 최적 아키타입을 골랐다”라기보다:

```text
refresh queue가 C05 문맥을 많이 들고 있음
→ seed target은 UNKNOWN
→ source_primary_archetype C05가 planner context로 들어감
→ planner top1이 C05로 쏠림
→ Evidence Contract C05로 primitive/score 생성
```

에 가까워.

그래서 삼성제약, 성호전자, 에이전트AI, SK 같은 종목까지 C05로 들어간 게 수상한 거야. 건설/EPC 종목이면 이해가 되는데, 전부 C05인 건 **아키타입 라우팅 다양성이 아니라 C05 queue 편향**이야.

## 2. 27.9998 / 77.9998은 회사별 “두뇌 점수”가 아니라 C05 weight formula 반복값임

0705 문서가 점수 formula도 추적했어. `27.9998`은 별도 epsilon이 아니라, `earnings_visibility=13.3333/20*22 = 14.6666`, `information_confidence=3.3333/5*20 = 13.3332`, 합계 `27.9998`이야. `77.9998`도 같은 식으로 C05 runtime weight가 반복 적용된 결과야. ([GitHub][1])

즉 이건:

```text
문서 여러 개를 깊게 읽어 기업별 경제 메커니즘을 차별적으로 채점한 점수
```

라기보다:

```text
비슷한 primitive raw point가 C05 weight table에 들어가서 반복 산출된 점수
```

에 가깝다.

점수 엔진이 계산을 한 건 맞지만, **계산 가능한 칸을 계산한 것**이지, thesis가 완성됐다는 뜻은 아니다.

## 3. pass 조건이 “meaningful thesis”가 아니라 “score path closed”에 가까움

현재 production audit은 `production_full_thesis_row_count=10`, `production_pass_allowed=true`인데, 동시에 `production_full_thesis_row_with_required_positive_missing_primitives_count=10`, `production_full_thesis_row_with_green_gap_primitives_count=10`이야. production rows 10개 전부 required-positive와 green gap이 남아 있는데도 pass가 됐다. ([GitHub][2])

그러면 현재 pass 조건은 사실상 이거야.

```text
claim/score/stage trace가 생겼고
blocking source-pending gap은 없다
→ FULL_THESIS_PRODUCTION_PASS
```

하지만 우리가 원하는 건:

```text
주요 primitive가 실제로 채워졌고
아키타입별 thesis가 의미 있게 평가됐고
coverage가 C05에만 쏠리지 않았고
required-positive / green gap의 의미가 명확히 분리됨
→ MEANINGFUL_FULL_THESIS_PASS
```

야.

## 4. 연구자료는 “정답 점수표”가 아니라 “source route / primitive bridge 판례집”이었음

이게 가장 중요해.

과거 연구는 대부분 이런 방식이었어.

```text
No-Repeat Index에서 부족한 아키타입/섹터 선택
→ historical trigger case 선정
→ stock-web OHLC로 MFE/MAE 검증
→ positive/counterexample 구분
→ 어떤 primitive/bridge가 있었으면 Stage2/Yellow가 되고,
   어떤 bridge가 없으면 4B/4C/watch가 되는지 정리
→ source quality를 URL-backed / source_proxy_only / evidence_url_pending로 구분
→ production_scoring_changed=false, shadow_weight_only=true로 남김
```

예를 들어 C06 연구는 HBM이라는 단어가 문패일 뿐이고, 고객 배정·qualification·HBM 매출 mix·capacity allocation이 진짜 증거라고 정리해. SK하이닉스 HBM sold-out / revenue mix, 삼성 qualification lag 같은 URL-backed row도 있어서 replay 원료로 쓸 수 있어. 

반대로 C24, C28, C17 같은 연구는 상당수가 `source_proxy_only`, `evidence_url_pending`, `shadow_weight_only`야. C24는 임상 이벤트가 endpoint/regulatory/partner/funding bridge 없이는 Stage2/Green으로 가면 안 된다는 룰을 만들었지만, 그 자료 자체는 운영 점수 근거가 아니라 source-proxy/pending이라고 명시돼 있어.  C28도 보안/SW 키워드만으로는 안 되고 ARR/RPO/renewal/retention이 필요하다고 정리하지만 source-proxy/URL repair가 필요해.  C17도 원자재 spread는 날씨일 뿐이고 realized spread, OPM, EPS revision, FCF가 필요하다고 정리하지만 source_proxy_only가 많아. 

따라서 지금 필요한 건 **연구자료를 그대로 점수화하는 것**이 아니라:

```text
연구자료를 역추적해서
각 아키타입별로 어떤 source route와 primitive bridge가 필요했는지 복원하고,
현재 종목에서 그 source를 실제로 다시 찾아 Evidence OS claim으로 만들어내는 것
```

이야.

## 5. C06/C08/C15/C17/C24/C28이 “검증돼서 탈락”한 게 아님

0705 문서에 따르면 C06은 삼성전자가 candidate였지만 source pending gap 때문에 blocked 됐고, SK하이닉스는 planner top1이 C06이었으나 accepted claim이 없어 production candidate로 승격되지 않았어. C08/C15/C17/C24/C28은 이번 full-thesis refresh queue/materialization 안에 사실상 후보가 없었다고 적혀 있어. ([GitHub][1])

즉 지금 결과는:

```text
전 아키타입을 다 검증해봤더니 C05만 통과했다
```

가 아니라:

```text
이번 refresh queue가 C05 중심이었고,
다른 아키타입은 source-backed full thesis 후보 경로에 거의 들어오지 않았다
```

가 맞아.

---

# 지금 해야 할 패치는 “막기”가 아니라 “연구→운영 역연결”

아래 Goal은 “더 많은 gate”가 아니라, **연구가 실제로 어떻게 진행됐는지 reverse-engineering하고, 그 방식이 운영에서 재현되도록 패치하는 Goal**이야.

핵심 이름은 이거다.

```text
Research-to-Runtime Evidence Parity v1
```

이걸 시키면 돼.

---

```text
너는 Daikisong/stock_agent 레포의 E2R Research-to-Runtime Evidence Parity v1을 구현하는 coding agent다.

이번 Goal은 단순히 Census v4의 PASS 라벨을 고치는 작업이 아니다.
이번 Goal의 목적은 “과거 연구가 어떻게 좋은 Green/Yellow/Stage2/4B/4C 판례를 만들었는지”를 역추적하고,
그 연구 방식이 실제 운영 파이프라인에서 재현되도록 만드는 것이다.

현재 전제:
- Evidence OS v2의 철학은 유지한다.
- Production Cutover v3는 CUTOVER_READY였다.
- Census v4는 anti-fake 상태판, Brain/Web partial evidence, 일부 FULL_THESIS score path를 만들었다.
- 하지만 2026-07-05 감사 결과에 따르면 production FULL_THESIS 10개가 전부 C05로 몰렸다.
- production full-thesis 10개는 모두 required_positive_missing_primitives와 green_gap_primitives가 남아 있다.
- 따라서 현재 FULL_THESIS_PRODUCTION_PASS는 “score path closed”이지 “meaningful full thesis passed”가 아니다.
- C05 외 C06/C08/C15/C17/C24/C28 등은 검증돼서 탈락한 것이 아니라, refresh queue/source route/materialization 경로에 충분히 들어오지 않았다.
- 연구자료에는 이미 아키타입별 positive/counterexample/guard 판례가 많지만, 그 자료는 대부분 shadow calibration, source_proxy_only, evidence_url_pending, production_scoring_changed=false 상태다.
- 이번 작업은 그 연구자료를 운영에서 쓸 수 있는 Evidence Contract / Source Route / Runtime Query Plan / Replay Fixture로 변환하는 것이다.

이번 Goal 이름:
E2R Research-to-Runtime Evidence Parity v1 — Historical Research Reverse Engineering, Source Route Recovery, Archetype-Balanced Full Thesis Operation

한 줄 목표:
과거 연구가 만든 “점수 비중”과 “Stage 판례”를 운영에서 재현할 수 있도록,
research MD / output / reports를 역추적해 아키타입별 source route와 primitive bridge를 복원하고,
현재 종목에서 그 source를 실제로 찾아 Evidence OS accepted claim으로 만들고,
C05뿐 아니라 C06/C08/C15/C17/C24/C28 등 주요 아키타입에서도 full-thesis production row가 나오게 한다.

절대 원칙:
1. 연구자료는 current score evidence가 아니다.
2. 연구자료는 source route, primitive bridge, guard pattern, false-positive pattern, query intent memory다.
3. source_proxy_only / evidence_url_pending / shadow_weight_only row는 production score에 직접 들어갈 수 없다.
4. URL-backed research row만 A2 replay 후보가 될 수 있다.
5. 과거 MFE/MAE/outcome은 current claim extraction prompt에 들어가면 안 된다.
6. LLM은 점수를 직접 주지 않는다.
7. LLM은 문서에서 claim을 추출하고, source route/query intent를 제안하고, missing primitive를 찾는다.
8. deterministic scorer/StageCourt만 score/stage를 계산한다.
9. C05 한 아키타입으로 full-thesis production이 몰리면 meaningful pass가 아니다.
10. target_archetype UNKNOWN → source_primary_archetype fallback → planner top1 고정 흐름은 반드시 provenance audit을 거쳐야 한다.
11. required_positive_missing_primitives가 남은 row는 “score path closed with remaining thesis gaps”이지 “meaningful full thesis complete”가 아니다.
12. 최근 공시 여부가 아니라 last effective thesis / lifecycle / current source-backed claim이 기준이다.
13. 실패하면 원인 파일/함수/설정까지 찾아 패치하고, 같은 명령으로 재실행한다.
14. 외부 API/유료 source/네트워크 장애만 EXTERNAL_SOURCE_BLOCKER로 남길 수 있다.
15. scoring weight와 Stage threshold는 변경하지 않는다.
16. 특정 종목명/URL/키워드 예외 처리 금지.

================================================================================
0. 2026-07-05 C05 Audit를 Root Cause 문서로 승격
================================================================================

입력 문서:
docs/0705/census_v4_full_thesis_production_c05_audit_2026-07-05.md

이 문서를 근거로 다음 문서를 생성하라.

docs/operational/research_to_runtime_root_cause_2026-07-05.md

반드시 포함:
- FULL_THESIS_PRODUCTION_PASS의 현재 의미는 score path closed다.
- meaningful full thesis pass가 아니다.
- production full-thesis 10개가 전부 C05다.
- seed target_archetype은 UNKNOWN 85개다.
- final C05는 source_primary_archetype context + planner top1 경로로 형성됐다.
- required_positive_missing_primitives 10/10.
- green_gap_primitives 10/10.
- C06 삼성전자는 source_pending_required_or_green_primitives로 blocked.
- SK하이닉스는 planner top1 C06이었으나 accepted claim이 생성되지 않아 full thesis 미생성.
- C08/C15/C17/C24/C28은 이번 refresh queue에 사실상 들어오지 않았다.
- 따라서 문제는 “점수 엔진이 막는다”가 아니라 “연구 판례와 운영 source route가 아직 제대로 연결되지 않는다”이다.

Acceptance:
- 기존 FULL_THESIS_PRODUCTION_PASS를 `PRODUCTION_FULL_E2R_SCORE_PATH_PASS`로 재라벨링.
- `MEANINGFUL_FULL_THESIS_PASS`는 false로 유지.
- C05 audit의 6개 질문과 답을 operational root cause 문서에 반영.

================================================================================
1. 연구 실행 방식 Reverse Engineering
================================================================================

과거 연구자료를 전부 분석해 “연구가 어떻게 증거와 점수비중을 만들었는지”를 구조화하라.

대상:
- docs/round/**/*.md
- output/e2r_round*/**/*.md
- reports/e2r_calibration/**
- docs/core/V12_Research_No_Repeat_Index.md
- configs/e2r_archetype_evidence_contracts_v12.json
- docs/0619, docs/0621, docs/0701, docs/0703, docs/0705
- production/census operational docs

생성:
src/e2r/research_reverse/
    __init__.py
    research_file_scanner.py
    research_case_extractor.py
    source_quality_inferencer.py
    archetype_pattern_extractor.py
    source_route_recoverer.py
    research_to_runtime_memory.py
    reports.py

ResearchCaseRecord:
{
  "research_case_id": "...",
  "source_file": "...",
  "canonical_archetype_id": "...",
  "large_sector_id": "...",
  "symbol": "...",
  "company_name": "...",
  "trigger_type": "...",
  "trigger_date": "...",
  "case_role": "positive|counterexample|4B|4C|guard|profile_cap|stage2_actionable|stage3_yellow|stage3_green",
  "evidence_family": "...",
  "source_urls": [],
  "source_quality": "A2_URL_BACKED|A1_URL_PENDING|SOURCE_PROXY_ONLY|EVIDENCE_URL_PENDING|PRICE_PATH_ONLY|SHADOW_ONLY",
  "source_proxy_only": true_or_false,
  "evidence_url_pending": true_or_false,
  "production_scoring_changed": false,
  "shadow_weight_only": true_or_false,
  "primitive_bridge_positive": [],
  "primitive_bridge_missing": [],
  "green_blockers": [],
  "false_positive_patterns": [],
  "stage_cap_rules": [],
  "runtime_source_route_hints": [],
  "price_path_metrics": {},
  "do_not_promote_reason": null
}

Acceptance:
- ResearchCaseRecord count > 1000 or documented corpus size.
- Every C01~C36 has extracted pattern summary or explicit source gap.
- Every record has source_quality.
- source_proxy_only rows cannot become runtime score evidence.
- URL-backed rows become replay candidates, not current score.
- price-path/outcome rows are not fed into current extraction prompts.

Reports:
docs/operational/research_reverse_case_inventory.json
docs/operational/research_reverse_archetype_coverage_matrix.json
docs/operational/research_reverse_source_quality_matrix.json

Tests:
tests/test_research_reverse_case_extractor.py
tests/test_research_reverse_source_quality.py
tests/test_research_reverse_no_proxy_to_score.py

================================================================================
2. 아키타입별 Research Memory Card v2 생성
================================================================================

연구자료를 raw case로만 저장하지 말고, 운영 planner가 읽을 수 있는 판례 카드로 압축하라.

ArchetypeRuntimeMemoryCard:
{
  "archetype_id": "...",
  "large_sector_id": "...",
  "canonical_mechanism": "...",
  "positive_unlock_primitives": [],
  "stage2_actionable_primitives": [],
  "yellow_unlock_primitives": [],
  "green_unlock_primitives": [],
  "required_positive_primitives": [],
  "green_blockers": [],
  "4b_watch_patterns": [],
  "4c_hard_break_patterns": [],
  "false_positive_patterns": [],
  "source_route_priority_by_primitive": {},
  "source_family_success_examples": [],
  "source_family_failure_examples": [],
  "url_backed_replay_cases": [],
  "source_proxy_only_cases": [],
  "evidence_url_pending_cases": [],
  "runtime_query_intent_templates": [],
  "do_not_promote_rules": [],
  "source_gap_repair_tasks": [],
  "confidence": "HIGH|MEDIUM|LOW",
  "runtime_usage_policy": "READY_FOR_ROUTING|SOURCE_REPAIR_REQUIRED|PLANNING_ONLY|UNSUPPORTED"
}

Examples:
- C06:
  HBM keyword alone is signboard.
  Unlock requires customer allocation, sold-out/pre-sold capacity, qualification status, shipment/revenue mix, margin/FCF/revision bridge.
  Samsung qualification lag is 4B/watch unless current permanent customer loss appears.
- C08:
  product/test socket profile is Stage2 cap.
  customer/order/qualification/margin conversion required for Actionable.
- C15:
  raw commodity weather is not enough.
  pass-through, product price, demand/customer route, realized margin/cash required.
- C17:
  commodity spread is weather.
  realized spread, feedstock cost, inventory timing, OPM, EPS revision, FCF required.
- C24:
  clinical event needs endpoint quality, regulatory path, partner/platform validation, funding runway.
- C28:
  software/security label is signboard.
  ARR/RPO/renewal/retention/churn/margin durability required.

Acceptance:
- C01~C36 cards generated.
- C06/C08/C15/C17/C24/C28 cards include positive and counterexample memory.
- Card clearly separates URL-backed vs source-proxy rows.
- Card does not include future price/outcome labels in runtime planner prompt payload.
- Card has source route priority per primitive.

Reports:
docs/operational/research_runtime_memory_cards_v2.json
docs/operational/research_runtime_memory_card_matrix_v2.json

Tests:
tests/test_research_runtime_memory_cards.py
tests/test_research_memory_no_future_outcome_in_prompt.py

================================================================================
3. Source Route Recovery Engine
================================================================================

과거 연구에서 어떤 source가 어떤 primitive를 실제로 뒷받침했는지 역추적해 runtime source route로 만든다.

구현:
src/e2r/source_routing/research_source_route_recovery.py

SourceRoutePattern:
{
  "archetype_id": "...",
  "primitive_id": "...",
  "source_family": "DART|KIND|KRX|CompanyGuide|IssuerIR|TrustedNews|BrokerReportPDF|IndustryMedia|NaverSearch|GeneralWebSearch|ResearchMemory",
  "route_role": "PRIMARY|SECONDARY|FALLBACK|DISCOVERY_ONLY|FORBIDDEN_FOR_SCORE",
  "examples": [],
  "requires_full_source": true,
  "requires_quote_anchor": true,
  "requires_current_lifecycle_check": true,
  "official_first_required": true,
  "query_intent_examples": [],
  "bad_query_patterns": [],
  "known_false_positive_sources": []
}

Rules:
- DART/KIND/KRX/IR/CompanyGuide official source first.
- Naver/Web is bounded fallback or discovery, not score source by itself.
- Snippet is never score evidence.
- Broker report/public PDF can be used only if legally accessible full text/anchor exists.
- ResearchMemory is planning-only.
- FCF/cash/revision/contract/backlog gaps cannot go to Naver before official sources.

Acceptance:
- SourceRoutePattern for each required primitive in C06/C08/C15/C17/C24/C28.
- For C06 HBM, Reuters/IR/news can discover, but production score requires current source-backed claim and lifecycle.
- For C15/C17, commodity headline routes to investigation, realized margin/FCF routes to official financials/reports.
- For C24/C28 source-proxy rows become source repair tasks, not score.

Reports:
docs/operational/research_source_route_recovery_matrix.json
docs/operational/research_source_route_gap_tasks.json

Tests:
tests/test_research_source_route_recovery.py
tests/test_research_source_route_official_first.py
tests/test_research_source_route_no_snippet_score.py

================================================================================
4. Full-Thesis Candidate Selection 재설계
================================================================================

현재 production full-thesis 후보가 C05로 쏠린다.
Refresh queue는 event-board 문맥만 보고 C05를 과잉 공급하지 말고, 아키타입별 runtime memory를 이용해 균형 잡힌 후보를 만들어야 한다.

구현/수정:
src/e2r/census/full_thesis_candidate_selector.py
src/e2r/census/full_thesis_refresh_queue.py

FullThesisCandidate:
{
  "candidate_id": "...",
  "symbol": "...",
  "company_name": "...",
  "candidate_source": "event_board|research_memory_seed|watchlist_seed|provider_gap_seed|manual_smoke|random_audit",
  "candidate_event_ids": [],
  "target_archetype": null_or_id,
  "target_archetype_source": "LLM_PLANNER|SOURCE_PRIMARY_CONTEXT|RESEARCH_MEMORY_CARD|EVIDENCE_CONTRACT|UNKNOWN",
  "source_primary_archetype": null_or_id,
  "planner_top_k": [],
  "archetype_confidence": "HIGH|MEDIUM|LOW",
  "archetype_provenance_trace": [],
  "reason_to_deepen": "...",
  "required_primitive_gaps": [],
  "source_route_plan": [],
  "balanced_selection_bucket": "...",
  "priority_score": 0.0
}

Rules:
- target_archetype UNKNOWN is allowed only before planner.
- After planner, production promotion requires target_archetype_source=LLM_PLANNER with confidence MEDIUM/HIGH.
- source_primary_archetype is context, not binding assignment.
- If final archetype equals source_primary but planner evidence is weak, mark `ARCTYPE_CONTEXT_BIAS_RISK`.
- Candidate selection must enforce archetype diversity.
- C05 can be selected but cannot dominate production full-thesis unless universe genuinely has C05-only source events and audit proves it.
- C06/C08/C15/C17/C24/C28 must receive minimum candidate attempts or explicit source/provider gap.
- Existing research memory can seed candidates, but not score.

Minimum production selection quotas:
- C05 max 35% of selected full-thesis candidates unless justified.
- At least 6 archetypes attempted in full-thesis production selection.
- Mandatory attempted archetypes:
  C06, C08, C15, C17, C24, C28.
- At least one candidate per large sector L1~L9 or documented no-source gap.
- If an archetype has URL-backed replay cases, at least one live/source-repair attempt must be scheduled.

Reports:
docs/operational/full_thesis_candidate_selection_audit_v2.json

Hard fail:
- distinct_attempted_archetype_count < 6.
- mandatory_archetype_attempt_missing_count > 0.
- c05_candidate_share > 0.35 without explicit low-signal justification.
- target_archetype_unknown_promoted_count > 0.
- source_primary_context_only_promoted_count > 0.
- archetype_context_bias_unreviewed_count > 0.

Tests:
tests/test_full_thesis_candidate_selection_diversity.py
tests/test_full_thesis_no_c05_monoculture.py
tests/test_full_thesis_target_archetype_provenance.py

================================================================================
5. Planner Bias Audit and Archetype Routing Repair
================================================================================

현재 seed target UNKNOWN + source_primary C05 context가 planner top1 C05를 유도했다.
Planner가 context를 참고할 수는 있지만, context bias를 audit해야 한다.

구현:
src/e2r/research_brain/planner_bias_audit.py

PlannerBiasRecord:
{
  "candidate_id": "...",
  "symbol": "...",
  "source_primary_archetype": "...",
  "planner_top1": "...",
  "planner_top2": "...",
  "planner_top3": "...",
  "final_archetype": "...",
  "context_bias_risk": true_or_false,
  "why_not_other_archetypes": [],
  "evidence_fields_supporting_top1": [],
  "evidence_fields_against_top1": [],
  "requires_disambiguation": true_or_false
}

Rules:
- If target_archetype unknown and planner top1 equals source_primary, require explicit evidence fields supporting top1.
- If company/sector mismatch with archetype, require disambiguation task.
- Samsung/Hynix C06 should not be demoted because recent DART event board lacks accepted claims; C06 memory/source route must create full-thesis tasks.
- If C05 top1 for non-EPC company, mark REVIEW_REQUIRED.

Hard fail:
- planner_top1_source_primary_copy_without_reason_count > 0.
- non_sector_archetype_assignment_without_disambiguation_count > 0.
- final_archetype_no_supporting_event_fields_count > 0.
- C05 assigned to non-EPC/non-contract economic mechanism without review.

Reports:
docs/operational/planner_bias_and_archetype_routing_audit.json

Tests:
tests/test_planner_bias_audit.py
tests/test_non_economic_mechanism_c05_requires_review.py

================================================================================
6. Full-Thesis Evidence Completion을 두 단계로 분리
================================================================================

현재 FULL_THESIS_PRODUCTION_PASS는 score path closed와 meaningful thesis complete를 섞고 있다.

새 라벨:
- PRODUCTION_FULL_E2R_SCORE_PATH_PASS
  claim → primitive → score → StageCourt path closed.
- MEANINGFUL_FULL_THESIS_EVIDENCE_PASS
  required_positive_missing_primitives materially resolved or stage explicitly low because evidence disproves thesis.
- GREEN_READY_FULL_THESIS_PASS
  green gap primitives resolved where stage claims Green.
- ARCHETYPE_BALANCED_FULL_THESIS_PASS
  C05 외 주요 아키타입도 source-backed production full-thesis attempt/pass.

Rules:
- required_positive_missing_primitives가 있으면 `MEANINGFUL_FULL_THESIS_EVIDENCE_PASS` 불가.
- green_gap_primitives가 있으면 Green 불가.
- Stage0/Stage1 can have required_positive_missing if the result is “thesis not supported”; but it must be labeled `THESIS_NOT_SUPPORTED`, not “complete positive thesis”.
- required_positive_missing 10/10 with C05-only rows cannot satisfy meaningful pass.

Audit:
docs/operational/full_thesis_evidence_completion_audit_v2.json

Hard fail for meaningful pass:
- required_positive_missing_rate > 0.3 among promoted rows.
- green_gap_rate > 0.3 among promoted rows.
- distinct_full_thesis_archetype_count < 3.
- C05-only promoted rows.
- production row count > 0 but all rows low-confidence event-context-only.

Tests:
tests/test_full_thesis_evidence_completion_split.py
tests/test_full_thesis_score_path_not_meaningful_pass.py

================================================================================
7. Research-to-Runtime Replay for Mandatory Archetypes
================================================================================

과거 연구의 대표 URL-backed / source-proxy 판례를 현재 운영 source route에서 재현한다.

Mandatory archetypes:
- C06_HBM_MEMORY_CUSTOMER_CAPACITY
- C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
- C15_MATERIAL_SPREAD_SUPERCYCLE
- C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
- C24_BIO_TRIAL_DATA_EVENT_RISK
- C28_SOFTWARE_SECURITY_CONTRACT_RETENTION

For each:
- one positive URL-backed or repaired source-backed replay attempt
- one counterexample/guard replay attempt
- one source-proxy-only case converted to source repair task
- one current-lifecycle validation task

ReplayResult:
{
  "archetype_id": "...",
  "case_id": "...",
  "source_quality": "...",
  "runtime_replay_status": "ACCEPTED_CLAIM_CREATED|SOURCE_REPAIR_REQUIRED|REJECTED_SCOPE|PROVIDER_FAILED|LIFECYCLE_NOT_CURRENT",
  "accepted_claim_ids": [],
  "primitive_states": [],
  "score_contributions": [],
  "stagecourt_trace_id": null,
  "expected_guard_result": "...",
  "actual_result": "...",
  "pass": true_or_false
}

Acceptance:
- C06 has accepted claim replay for SK Hynix HBM sold-out/revenue mix and Samsung qualification-lag guard.
- C08 has accepted claim replay for at least one direct customer/order bridge and one product-profile cap.
- C15 has accepted claim replay for pass-through positive and raw commodity false positive.
- C17 may remain source repair if no current URL repaired, but must not claim pass.
- C24/C28 source-proxy cases become source repair tasks unless URL repaired.
- All source-proxy cases are planning-only.

Reports:
docs/operational/research_to_runtime_replay_matrix_v1.json
docs/operational/research_to_runtime_source_repair_queue_v1.json

Tests:
tests/test_research_to_runtime_replay_mandatory_archetypes.py
tests/test_research_to_runtime_proxy_becomes_repair_task.py

================================================================================
8. Runtime Follow-up Loop must use Research Memory
================================================================================

현재 missing primitive가 생기면 follow-up seed는 생긴다.
하지만 그 seed가 연구 기억에서 “무엇을 찾아야 하는지”를 배워야 한다.

Implement:
src/e2r/census/research_memory_followup_planner.py

Input:
- blocked full-thesis candidate
- missing primitive
- archetype memory card
- source route recovery matrix
- current source failures
- previous claim ledger

Output:
ResearchMemoryFollowupTask:
{
  "task_id": "...",
  "symbol": "...",
  "archetype_id": "...",
  "missing_primitive": "...",
  "why_this_primitive_matters": "...",
  "source_route_priority": [],
  "query_intents": [],
  "disallowed_sources": [],
  "success_condition": "...",
  "expected_claim_schema": {},
  "fallback_if_not_found": "PENDING_SOURCE|THESIS_NOT_SUPPORTED|SOURCE_REPAIR_REQUIRED"
}

Rules:
- LLM generates query intents based on memory card and candidate context.
- Code validates official-first and source policy.
- Do not hardcode query strings per archetype.
- If task fails, append failure reason and next source repair task.

Acceptance:
- Every blocked production candidate has follow-up tasks tied to missing primitives.
- Follow-up tasks for C06 include allocation/pre-sold/revenue mix/margin bridge routes.
- Follow-up tasks for C15/C17 distinguish commodity headline vs realized margin/cash.
- Follow-up tasks for C24/C28 source-proxy cases are URL repair/source verification tasks.
- At least one second-iteration follow-up materially reduces missing primitive count or records source blocker.

Reports:
docs/operational/research_memory_followup_task_audit.json

Tests:
tests/test_research_memory_followup_planner.py
tests/test_followup_tasks_reduce_or_explain_missing_primitives.py

================================================================================
9. Meaningful Full-Thesis Production Acceptance
================================================================================

이번 Goal 완료 기준은 숫자 예쁜 PASS가 아니다.

Minimum pass:
- PRODUCTION_FULL_E2R_SCORE_PATH_PASS may pass if path closed.
- MEANINGFUL_FULL_THESIS_EVIDENCE_PASS requires:
  - distinct_full_thesis_archetype_count >= 3
  - mandatory_archetype_attempt_count >= 6
  - at least C06 or C08 source-backed full-thesis production row or explicit EXTERNAL_SOURCE_BLOCKER
  - C05 share among promoted rows <= 50%
  - required_positive_missing_rate <= 30% OR low-stage thesis-not-supported label with evidence.
  - source_primary_context_only_promoted_count = 0
  - target_archetype_unknown_promoted_count = 0
  - planner context bias audit pass
  - research memory route audit pass
  - replay matrix pass or explicit source repair gap

Full pass:
- ARCHETYPE_BALANCED_FULL_THESIS_PASS requires:
  - distinct_full_thesis_archetype_count >= 6
  - C06, C08, C15, C17, C24, C28 all attempted
  - at least 4 archetypes have accepted claims or source-repair tasks with explicit gap
  - no source-proxy score
  - all failures are source/claim/blocker categorized.

Hard fail:
- promoted rows all C05.
- required_positive_missing 100%.
- green_gap 100% and label says meaningful pass.
- SK Hynix/Samsung C06 controlled smoke is substituted for production row.
- C05 non-economic mechanism rows promoted without review.

Tests:
tests/test_meaningful_full_thesis_production_acceptance.py
tests/test_no_c05_only_meaningful_pass.py
tests/test_required_positive_missing_blocks_meaningful_pass.py

================================================================================
10. Research Parity Dashboards
================================================================================

Generate final dashboards:

docs/operational/research_to_runtime_acceptance_report.md
docs/operational/research_to_runtime_readiness_verdict.md
docs/operational/research_reverse_case_inventory.json
docs/operational/research_runtime_memory_cards_v2.json
docs/operational/research_source_route_recovery_matrix.json
docs/operational/full_thesis_candidate_selection_audit_v2.json
docs/operational/planner_bias_and_archetype_routing_audit.json
docs/operational/full_thesis_evidence_completion_audit_v2.json
docs/operational/research_to_runtime_replay_matrix_v1.json
docs/operational/research_memory_followup_task_audit.json

Acceptance report must include:
- research case count
- source quality breakdown
- URL-backed replay count
- source-proxy-only repair count
- archetype memory card count
- source route coverage by primitive
- full-thesis candidate attempts by archetype
- promoted full-thesis rows by archetype
- blocked candidates by archetype and primitive
- required positive missing rate
- green gap rate
- distinct archetype count
- C05 share
- C06/Samsung/Hynix production vs smoke separation
- research memory follow-up success/failure
- final verdict

================================================================================
11. Self-Repair Until Meaningful or Honest Blocker
================================================================================

Run:
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass \
  --as-of-date 2026-07-05 \
  --mode full_thesis_balanced \
  --mandatory-archetypes C06,C08,C15,C17,C24,C28 \
  --max-iterations 10 \
  --fail-on-c05-monoculture true \
  --fail-on-unknown-target-promoted true \
  --fail-on-required-positive-missing-over-threshold true \
  --fail-on-research-proxy-score true

Self-repair must:
- run research reverse inventory
- build memory cards
- build source routes
- select balanced candidates
- run Brain/Web/official source tasks
- run Evidence OS
- run StageCourt
- audit archetype diversity
- audit score path vs meaningful thesis
- patch root cause if fail
- rerun same command
- stop only on meaningful pass or external blocker

Failure classes:
- C05_MONOCULTURE
- TARGET_ARCHETYPE_UNKNOWN_PROMOTED
- SOURCE_PRIMARY_CONTEXT_BIAS
- REQUIRED_POSITIVE_MISSING_RATE_TOO_HIGH
- GREEN_GAP_RATE_TOO_HIGH
- MANDATORY_ARCHETYPE_NOT_ATTEMPTED
- RESEARCH_MEMORY_NOT_WIRED
- SOURCE_ROUTE_NOT_RECOVERED
- URL_BACKED_REPLAY_NOT_USED
- SOURCE_PROXY_TO_SCORE
- C06_PRODUCTION_BLOCKED
- SK_HYNIX_ACCEPTED_CLAIM_NOT_CREATED
- SAMSUNG_SOURCE_PENDING_UNRESOLVED
- ALL_NON_C05_QUEUE_EMPTY
- EXTERNAL_SOURCE_BLOCKER

If fail due code:
- patch.
- rerun.

If fail due external source:
- report provider/source/URL/API blocker.
- final status EXTERNAL_SOURCE_BLOCKER_NOT_READY.
- do not claim meaningful pass.

================================================================================
12. Required Tests
================================================================================

Add/strengthen:

tests/test_research_reverse_case_extractor.py
tests/test_research_runtime_memory_cards.py
tests/test_research_source_route_recovery.py
tests/test_full_thesis_candidate_selection_diversity.py
tests/test_full_thesis_no_c05_monoculture.py
tests/test_full_thesis_target_archetype_provenance.py
tests/test_planner_bias_audit.py
tests/test_full_thesis_evidence_completion_split.py
tests/test_research_to_runtime_replay_mandatory_archetypes.py
tests/test_research_memory_followup_planner.py
tests/test_meaningful_full_thesis_production_acceptance.py
tests/test_no_c05_only_meaningful_pass.py
tests/test_required_positive_missing_blocks_meaningful_pass.py
tests/test_source_proxy_never_runtime_score.py
tests/test_c06_samsung_hynix_production_not_smoke.py

Full command:
PYTHONPATH=src python -m unittest discover -s tests -v

No skipped tests for this goal.
Known bad cases:
- C05-only promoted rows must fail meaningful pass.
- target_archetype UNKNOWN promoted must fail.
- source_primary context-only promoted must fail.
- required_positive_missing 100% must fail meaningful pass.
- controlled smoke substituted as production must fail.

================================================================================
13. Final Status Labels
================================================================================

Allowed:
- IMPLEMENTATION_MERGED
- RESEARCH_REVERSE_INVENTORY_PASS
- RESEARCH_MEMORY_CARD_PASS
- SOURCE_ROUTE_RECOVERY_PASS
- FULL_THESIS_BALANCED_CANDIDATE_SELECTION_PASS
- PLANNER_BIAS_AUDIT_PASS
- PRODUCTION_FULL_E2R_SCORE_PATH_PASS
- MEANINGFUL_FULL_THESIS_EVIDENCE_PASS
- ARCHETYPE_BALANCED_FULL_THESIS_PASS
- RESEARCH_TO_RUNTIME_REPLAY_PASS
- READY_FOR_DAILY_TRIGGER_INTEGRATION_V2
- EXTERNAL_SOURCE_BLOCKER_NOT_READY

Do not use:
- FULL_THESIS_PRODUCTION_PASS alone.
- FULL_UNIVERSE_STAGE_MAP_PASS alone.
- MEANINGFUL pass when C05-only or required-positive missing 100%.

Goal completion minimum:
- RESEARCH_REVERSE_INVENTORY_PASS
- RESEARCH_MEMORY_CARD_PASS
- SOURCE_ROUTE_RECOVERY_PASS
- FULL_THESIS_BALANCED_CANDIDATE_SELECTION_PASS
- PLANNER_BIAS_AUDIT_PASS
- PRODUCTION_FULL_E2R_SCORE_PATH_PASS
- research memory follow-up audit pass
- full tests pass

True target:
- MEANINGFUL_FULL_THESIS_EVIDENCE_PASS
or
- EXTERNAL_SOURCE_BLOCKER_NOT_READY with exact source blockers.

================================================================================
14. Final Answer Format
================================================================================

After completion, report only:

1. Final status
2. Commit SHA / message / push status / working tree
3. Test result
4. Research reverse inventory
5. Source quality breakdown
6. Runtime memory cards
7. Source route recovery
8. Candidate selection by archetype
9. Planner bias audit
10. Full-thesis production rows by archetype
11. Required positive missing rate
12. Green gap rate
13. C05 share
14. Mandatory archetype attempts
15. C06 Samsung/Hynix production vs smoke
16. Research-to-runtime replay matrix
17. Follow-up task result
18. Final verdict
19. Remaining blockers

================================================================================
15. Prohibitions
================================================================================

- Do not claim meaningful full thesis pass with C05-only rows.
- Do not claim meaningful pass with required_positive_missing 100%.
- Do not treat source_primary_archetype as binding target.
- Do not promote target_archetype UNKNOWN.
- Do not use research source_proxy_only as score evidence.
- Do not use evidence_url_pending rows as production replay.
- Do not use price-path/outcome in current extraction prompt.
- Do not substitute controlled smoke as production.
- Do not ignore C06/Samsung/Hynix production failure.
- Do not hardcode symbol-specific fixes.
- Do not change scoring weights or Stage thresholds.
- Do not loosen gates to pass.
- Do not hide source gaps.

================================================================================
16. One-line goal
================================================================================

이번 Goal의 목적은 “C05에서 score path가 닫혔다”를 반복하는 것이 아니다.

목적은:

과거 연구가 어떻게 evidence bridge와 guardrail을 만들었는지 역추적하고,
그 연구 기억을 runtime source route와 LLM follow-up planner에 연결해서,
C05뿐 아니라 C06/C08/C15/C17/C24/C28 등 주요 아키타입에서
source-backed full thesis 시도를 실제로 수행하고,
증거가 있으면 accepted claim/score/stage로 닫고,
증거가 없으면 정확한 source repair blocker로 남기는 것이다.
```

---

# 요약 판단

지금까지의 문제는 **“증거가 없어서 못함”**이 아니라, 더 정확히는 이거야.

```text
연구 단계:
아키타입별로 어떤 증거가 필요한지 이미 많이 배웠음.

운영 단계:
그 연구 판례를 current source task로 바꾸는 계층이 약함.

결과:
쉬운 event-board/C05 계약형 문맥만 production full-thesis로 승격.
C06/C08/C15/C17/C24/C28은 source route에 제대로 못 올라오거나 accepted claim 생성 실패.
```

그러니까 이제는 gate를 더 세우는 게 아니라, **연구 판례를 역추적해 운영 source route와 follow-up planner에 먹이는 패치**가 맞아.
위 Goal은 그걸 하도록 만든 거야.

[1]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/docs/0705/census_v4_full_thesis_production_c05_audit_2026-07-05.md "raw.githubusercontent.com"
[2]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/docs/operational/census_mode_v4_full_thesis_production_audit.json "raw.githubusercontent.com"
맞아. **다른 것도 다 잘 안 된 거라고 보는 게 맞아.**
내가 C06/C08/C15/C17/C24/C28만 말한 건 “얘네만 문제”라는 뜻이 아니었고, **우리가 지금 손에 든 연구문서와 감사문서에서 실패 구조가 가장 선명하게 보이는 대표 축**이라 예로 든 거야.

정확히 고치면 이렇게 말해야 해.

```text
C01~C32, 또는 최신 Evidence OS 기준 C01~C36 전체가 아직 runtime parity를 통과한 게 아니다.

현재 문제는:
C05만 full-thesis score path가 닫혔고,
나머지 아키타입들은 대부분
1) 후보 queue에 제대로 안 올라왔거나
2) source route가 복원되지 않았거나
3) source_proxy/evidence_url_pending 상태라 score에 못 들어가거나
4) accepted claim은 만들어도 required primitive를 못 채웠거나
5) 아예 full-thesis production attempt가 없었다.
```

그래서 네 말이 맞아. **C06/C08/C15/C17/C24/C28만 잘 안 된 게 아니라, 전체 아키타입이 아직 운영적으로 다 안 된 상태**로 봐야 해.

---

## C01~C32냐 C01~C36이냐

문서마다 표현이 조금 달라. 일부 연구 문서에는 “C01~C32”라고 나오고, Evidence OS 목표 문서 쪽에는 “C01~C36 전체”를 운영 대상으로 본다. 예를 들어 Evidence OS 최종 목표 문서는 전 아키타입 공통 원칙과 replay 조건을 C01~C36 전체에 걸고 있어. 

그래서 다음 Goal에서는 이렇게 박는 게 맞아.

```text
canonical archetype registry를 source of truth로 삼아라.
현재 repo config에 존재하는 C01~C32 또는 C01~C36 전체를 자동 로드하라.
하드코딩으로 C06/C08/C15/C17/C24/C28만 보지 마라.
```

즉 숫자는 코드의 canonical registry에서 읽어야 하고, 프롬프트에는 이렇게 써야 해.

```text
ALL_CANONICAL_ARCHETYPES = load from configs / evidence contracts
Do not assume only C06/C08/C15/C17/C24/C28.
```

---

## 왜 내가 C06/C08/C15/C17/C24/C28을 말했냐

이 여섯 개는 **대표 canary**였어.

C06은 URL-backed 자료가 비교적 좋고, HBM customer allocation / qualification / revenue mix / capacity라는 운영 primitive가 명확해. C06 문서도 “HBM이라는 단어는 문패이고, 고객 배정·qualification·매출 mix·capacity allocation이 진짜 발자국”이라고 정리하고 있어. 

C08은 direct URL이 꽤 있고, product profile과 customer/order/revenue conversion을 구분하는 구조가 좋아. C08 연구는 test socket/product exposure만으로는 부족하고 named customer, qualification, supply order, recognized revenue, margin conversion이 있어야 Stage2-Actionable으로 간다고 정리해. 

C15/C17은 소재·화학 쪽에서 “원자재 headline/weather”와 “issuer-level pass-through / realized margin / FCF bridge”를 구분해야 하는 대표 축이야. C15는 raw commodity headline이 아니라 product price/pass-through, demand/customer route, realized margin/cash conversion, inventory phase를 봐야 한다고 정리돼 있고, C17도 commodity spread는 날씨이고 calibration body는 realized spread, feedstock cost, inventory timing, OPM, EPS revision, FCF라고 정리돼 있어.  

C24/C28은 반대로 source_proxy/evidence_url_pending이 많아서 운영 score로 바로 못 올리는 대표 축이야. C24 문서는 source_proxy_only/evidence_url_pending, shadow_weight_only라고 명시하면서 clinical/data event는 endpoint quality, regulatory path, partner/platform validation, funding runway 없이는 Stage2/Green으로 올리면 안 된다고 말해.  C28도 software/security label은 signboard이고 ARR/RPO, renewal, retention, churn, margin durability가 필요하지만, 다수 연구가 source_proxy_only/evidence_url_pending이라 URL repair가 필요하다고 되어 있어. 

그러니까 이 여섯 개는 “여기만 문제”가 아니라:

```text
URL-backed positive가 있는 아키타입
source_proxy가 많은 아키타입
false-positive guard가 강한 아키타입
현재 queue에서 빠진 아키타입
```

을 대표해서 든 거야.

하지만 다음 패치에서는 **절대 이 여섯 개만 하면 안 돼.**

---

## 지금 전체 아키타입에 대해 실제로 봐야 하는 상태

각 C 아키타입은 아래 네 가지 중 하나로 분류되어야 해.

```text
A. RUNTIME_FULL_THESIS_READY
   현재 source route가 있고, accepted claim이 만들어지고,
   primitive coverage가 충분해 full thesis score/stage가 가능.

B. RUNTIME_SOURCE_REPAIR_REQUIRED
   연구 판례는 있으나 URL/source/anchor/claim이 부족해서
   운영 score에는 못 쓰고 source repair queue로 가야 함.

C. RUNTIME_PLANNING_ONLY
   source_proxy_only, evidence_url_pending, price_path_only 위주라
   현재는 MemoryCard / guard / query planner 원료로만 사용.

D. RUNTIME_UNTESTED_OR_NOT_ATTEMPTED
   연구자료가 있든 없든, 현재 production refresh queue에서
   실제 full-thesis attempt가 안 됨.
```

지금 C05 10개만 나왔다는 건 대부분이 A가 아니라는 뜻이야.
그리고 더 나쁘게 말하면, 많은 아키타입은 B/C로 판정된 것도 아니고 **D, 즉 제대로 시도조차 안 된 상태**일 가능성이 크다.

이게 진짜 문제야.

```text
검증해봤더니 안 된 것
≠
시도조차 안 한 것
```

현재는 후자가 많아 보여.

---

## 지금 패치 방향은 “대표 6개”가 아니라 “전체 아키타입 Coverage Parity”

다음 Goal은 이렇게 바꿔야 해.

```text
C06/C08/C15/C17/C24/C28 mandatory canary는 유지하되,
C01~C32/C36 전체에 대해
attempt / source route / accepted claim / primitive coverage / blocker를 matrix로 만든다.
```

아래를 기존 Goal에 반드시 추가해야 해.

---

```text
================================================================================
ALL ARCHETYPE RUNTIME PARITY MATRIX — 필수 추가
================================================================================

현재 문제:
이전 답변과 일부 Goal은 C06/C08/C15/C17/C24/C28을 대표 canary로 다뤘다.
그러나 실제 E2R 운영 대상은 C01~C32 또는 현재 canonical registry에 존재하는 전체 C archetype이다.
C05만 production full-thesis row가 나온 상태에서, 나머지 아키타입이 “검증 실패”인지 “시도조차 안 됨”인지 구분되지 않는다.

이번 패치에서는 특정 6개 아키타입만 보지 말고, canonical registry에 존재하는 모든 archetype을 자동 로드해 전수 matrix를 만든다.

Source of truth:
- configs/e2r_archetype_evidence_contracts_v12.json
- configs/e2r_archetype_weight_profile*.json
- docs/core/V12_Research_No_Repeat_Index.md
- research_reverse case inventory
- canonical archetype registry loader

Do not hardcode:
- C06/C08/C15/C17/C24/C28 only
- C01~C32 fixed count
- C01~C36 fixed count

Instead:
ALL_CANONICAL_ARCHETYPES = load_current_registry()

For each archetype:
ArchetypeRuntimeParityRow:
{
  "archetype_id": "...",
  "large_sector_id": "...",
  "exists_in_registry": true,
  "research_case_count": 0,
  "url_backed_case_count": 0,
  "source_proxy_case_count": 0,
  "evidence_url_pending_count": 0,
  "positive_case_count": 0,
  "counterexample_case_count": 0,
  "guard_case_count": 0,

  "runtime_candidate_attempt_count": 0,
  "runtime_planner_attempt_count": 0,
  "runtime_source_task_count": 0,
  "runtime_source_task_executed_count": 0,
  "runtime_accepted_claim_count": 0,
  "runtime_score_contribution_count": 0,
  "runtime_stagecourt_trace_count": 0,
  "runtime_full_thesis_row_count": 0,

  "runtime_status": "FULL_THESIS_READY|SCORE_PATH_CLOSED|SOURCE_REPAIR_REQUIRED|PLANNING_ONLY|NOT_ATTEMPTED|EXTERNAL_BLOCKER",
  "primary_blocker_class": "...",
  "blocker_detail": "...",
  "required_positive_missing_rate": null,
  "green_gap_rate": null,
  "source_route_ready": true_or_false,
  "source_route_gaps": [],
  "memory_card_ready": true_or_false,
  "followup_task_count": 0,
  "source_repair_task_count": 0
}

Blocker classes:
- NO_RESEARCH_MEMORY
- RESEARCH_MEMORY_SOURCE_PROXY_ONLY
- URL_BACKED_CASE_EXISTS_BUT_NOT_REPLAYED
- SOURCE_ROUTE_NOT_RECOVERED
- CANDIDATE_SELECTOR_DID_NOT_ATTEMPT
- PLANNER_DID_NOT_ROUTE
- SOURCE_TASK_NOT_CREATED
- SOURCE_TASK_NOT_EXECUTED
- SOURCE_FETCH_FAILED
- LLM_EXTRACTOR_FAILED
- ACCEPTED_CLAIM_NOT_CREATED
- PRIMITIVE_MAPPING_FAILED
- REQUIRED_POSITIVE_MISSING
- GREEN_GAP_MISSING
- SCORE_PATH_NOT_CLOSED
- EXTERNAL_PROVIDER_BLOCKER
- INTENTIONALLY_UNSUPPORTED

Acceptance:
- Every registered archetype has exactly one ArchetypeRuntimeParityRow.
- missing_archetype_parity_row_count = 0.
- C05-only pass cannot satisfy all-archetype parity.
- Every archetype is at least attempted or explicitly classified as PLANNING_ONLY / SOURCE_REPAIR_REQUIRED / NOT_ATTEMPTED with reason.
- NOT_ATTEMPTED without reason is hard fail.
- URL_BACKED_CASE_EXISTS_BUT_NOT_REPLAYED is hard fail unless source provider blocker is documented.
- source_proxy_only cases must become source repair tasks, not score.
- mandatory canary archetypes C06/C08/C15/C17/C24/C28 still get detailed rows, but they are not the whole scope.

Reports:
docs/operational/all_archetype_runtime_parity_matrix.json
docs/operational/all_archetype_runtime_parity_summary.md

Hard fail:
- all_archetype_count < registry_archetype_count
- missing_parity_rows > 0
- c05_only_full_thesis_pass_claimed_as_meaningful > 0
- not_attempted_without_reason_count > 0
- url_backed_case_exists_but_not_replayed_count > 0
- source_proxy_to_score_count > 0

Tests:
tests/test_all_archetype_runtime_parity_matrix.py
tests/test_all_registered_archetypes_have_parity_row.py
tests/test_c05_only_does_not_satisfy_all_archetype_parity.py
tests/test_url_backed_cases_must_be_replayed_or_blocked.py
```

---

## 지금 네 질문에 대한 정확한 답

> C1부터 32까지인가 있는거아니야?

응. 최소 C01~C32, 최신 운영 목표 문서 기준으로는 C01~C36 전체를 봐야 한다. 숫자는 코드 registry에서 읽게 해야 하고, 사람이 프롬프트에서 여섯 개만 고정하면 안 된다.

> 왜 C06/C08/C15/C17/C24/C28만 말하는거야?

그 여섯 개는 대표 실패 유형이 잘 보이는 canary였기 때문이야. 하지만 “다른 건 잘 됐다”는 뜻이 절대 아니다.

> 다른 것도 다 잘 안된 거 아니야?

맞아. 현재 증거 기준으로는 대부분의 다른 아키타입도 다음 중 하나일 가능성이 높다.

```text
- full-thesis 후보로 시도되지 않음
- source route가 없음
- research memory가 source_proxy_only라 score 불가
- accepted claim 생성 실패
- primitive coverage 부족
- 그냥 parity matrix가 아직 없음
```

그래서 다음 Goal은 **mandatory 6개 + all archetype parity matrix**로 가야 해.

---

## 표현을 앞으로 이렇게 바꾸자

이전 표현:

```text
C06/C08/C15/C17/C24/C28이 source route에 못 올라옴
```

정확한 표현:

```text
C05 외 전체 아키타입에 대해 runtime parity가 아직 증명되지 않았다.
C06/C08/C15/C17/C24/C28은 대표 canary일 뿐이고,
나머지 C01~C32/C36도 attempt/source route/accepted claim/full thesis 상태를 전수 matrix로 증명해야 한다.
```

이게 맞아.
