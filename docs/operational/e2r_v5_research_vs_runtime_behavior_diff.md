# E2R v5 Research vs Runtime Behavior Difference

- status: V5_PHASE80_WHOLE_REPO_FORENSIC_PASS
- audited base commit: `7f2fabe29dae193dacb02bb9fbdc69b82ffdfeba`
- critical_count_sum: 0

## 결론

현재 runtime은 안전성 검증은 강하지만 연구자의 broad component 판단을 복원하지 못했다. 13개 질문을 낮은 고정 budget으로 닫고 exact primitive와 여러 fraction cap을 통과한 잔여 credit만 합산한다. v5 canonical path는 `e2r.research_brain.researcher_mode` 하나로 통합한다.

쉬운 예: 식당 평가를 할 때 “주차장, 메뉴판, 영업시간” 체크박스를 모두 확인했다고 음식·가격·재방문 가치 조사까지 끝난 것은 아니다. 현재 FULL_E2R_100은 이 둘을 혼동한다.

## Historical research와 current runtime 차이

| 축 | 과거 연구 방식 | 현재 runtime | v5 방향 |
|---|---|---|---|
| 조사 종료 | material positive/counter와 정량자료 종합 | bounded route/질문 closure | supervisor 3자 semantic saturation |
| 점수 단위 | 7개 broad component 종합판단 | primitive impact fraction × subcriterion | component memo + historical anchor + judge consensus |
| source | official·structured·independent를 넓게 연결 | canary 최종 scoring 문서 1~2건 | material relevance 기반 source graph |
| valuation/revision | 가격·컨센서스·historical/peer band | 한 질문 family에 주로 종속 | structured financial/consensus/valuation engine |
| 반례 | phase·valuation·qualification을 thesis와 함께 종합 | impact counter fraction | memo와 skeptic judge에서 명시적 net 판단 |
| Stage | 연구 score와 판례를 종합한 후 검증 | low subtotal도 FULL_E2R_100으로 final 가능 | 7/7 research complete 뒤 deterministic StageCourt |

## 현재 canary score collapse

- 005930 삼성전자: documents=1, claims=18, score=18.159977, zero_components=['market_mispricing', 'valuation_rerating']
- 000660 SK하이닉스: documents=2, claims=33, score=19.120509, zero_components=['market_mispricing']

## production-reachable 병렬 scoring authority

- `LEGACY_FEATURE_SCORER`: KoreaLiveLiteRunner → `RETRIEVAL_ONLY_SCORE_RETIRED`
- `RESEARCH_BRAIN_V3_SCORER`: v3 daily shadow CLI → `COMPATIBILITY_ONLY`
- `RESEARCH_BRAIN_V4_SCORER`: v4 production shadow and census → `MATERIALIZATION_INPUT_ONLY`
- `DOSSIER_COMPONENT_SCORER`: dossier scoring CLI → `REPLACED_BY_RESEARCHER_MODE`
- `CENSUS_DIRECT_SCORER`: census v4 → `BASELINE_ONLY`
- `OFFICIAL_LIVE_SHADOW_SCORER`: official live shadow → `BASELINE_ONLY`

이 경로들은 Phase 80 시점에 동시에 접근 가능하다. v5 이후 current full-thesis authority는 Researcher Mode 하나만 남기고 나머지는 baseline, compatibility 또는 retrieval-only로 제한해야 한다.

## file/function root causes

- `FIXED_LOW_RESEARCH_LIMITS` — A transport limit can terminate the checklist before broad component research saturates. (`src/e2r/research_brain/dossier/orchestrator.py:39`)
- `QUESTION_TASK_BOUNDED_EXHAUSTION` — Thirteen question families use max_queries=3/max_fetches=6 and can close on bounded route exhaustion. (`configs/e2r_full_thesis_question_families_v1.json:22`)
- `KEYWORD_CLOSURE_SCORE_GATE` — Keyword groups choose SUPPORTED_SCORING/PARTIALLY_SUPPORTED_SCORING/EVALUATED_ABSENT. (`src/e2r/research_brain/scoring/question_impact_contract.py:42`)
- `QUESTION_CLOSURE_COMPONENT_DEPENDENCY` — Question closure feeds semantic reconciliation, terminal evidence, component assessment, and full validity. (`src/e2r/research_brain/dossier/scoring_pipeline.py:461`)
- `EXACT_PRIMITIVE_SUBCRITERION_GATE` — An impact without an allowed primitive/question subcriterion is unmapped and cannot open the broad component. (`src/e2r/research_brain/scoring/component_scoring_model.py:253`)
- `CHAINED_FRACTION_UNDERCREDIT` — Economic strength is repeatedly bounded before tiny subcriterion multiplication, collapsing strong-anchor-equivalent evidence. (`src/e2r/research_brain/scoring/impact_validator.py:233`)
- `VALUATION_REVISION_APERTURE_COLLAPSE` — Market expectation and valuation depend on one narrow family instead of structured price, consensus, peer, and scenario research. (`src/e2r/research_brain/dossier/scoring_pipeline.py:61`)
- `SMALL_GOLD_BENCHMARK_FALSE_COMPLETENESS` — Nine matched facts cannot prove complete seven-component research recall. (`docs/operational/e2r_research_quality_gold_audit.json:133`)

## Legacy에서 이식할 것

- LLM/sector-aware broad query expansion
- Naver API discovery transport
- full page and public PDF fetch
- document cache and content dedupe
- theme and score-gap query feedback
- OpenDART detail and structured financial collection
- CompanyGuide consensus/revision and Naver Finance structured snapshots

## Legacy scoring에서 폐기할 것

- parser field direct score mutation
- feature-field rewrite after search
- keyword-only risk or positive score
- input-order dependent score mutation
- legacy score and Stage as Researcher Mode authority

## 선택한 canonical future architecture

`target/as_of_date → Researcher Mode source graph → EvidenceFact graph → 7 ComponentResearchMemo → Analyst/Skeptic/CalibrationJudge → deterministic FinalComponentDecision/total → deterministic StageCourt`

QuestionImpactContract와 primitive는 조사 seed·guard·설명 태그로만 남고 production score/final Stage authority는 갖지 않는다.
