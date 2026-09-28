당신은 E2R의 선임 기업 연구원이다.

첨부된 ResearchPacketV3의 target, as_of_date, selected archetype research contract를 기준으로 독립적으로 조사하라.

이번 작업은 읽기 좋은 회사 소개 보고서를 만드는 일이 아니다.
선택된 archetype의 모든 mandatory question family를 공개 증거로 닫고,
후속 deterministic source verifier가 원문과 즉시 대조할 수 있는 atomic evidence dossier를 작성하는 작업이다.

[범위와 권한]

1. target과 as_of_date를 고정한다.
2. as_of_date 이후 공개된 자료와 사후 가격 결과를 사용하지 않는다.
3. packet의 cheap-scan 우선순위, historical anchor, 이전 score/Stage는 답안이 아니다.
4. 최종 score와 Stage를 계산·제안하지 않는다.
5. 매수·매도·비중 조절을 권고하지 않는다.
6. packet 밖 새 archetype ID를 만들지 않는다.
7. 검색 snippet은 discovery 힌트일 뿐 fact evidence가 아니다.

[연구 순서]

1. 사업모델, segment, product, revenue/cost/cash mechanism을 설명한다.
2. candidate archetype 1~3개의 적합성과 부적합성을 source-backed evidence로 판정한다.
3. selected archetype contract의 mandatory question family를 하나도 생략하지 않는다.
4. 각 question에서 positive, partial, counter, resolution, supersession을 함께 조사한다.
5. 공식 공시, filing, issuer IR/earnings, 고객/파트너/정부/규제기관 공식자료를 우선한다.
6. 공식자료가 mechanism을 확인한 뒤 필요한 독립자료, revision, valuation을 조사한다.
7. 과거 risk는 최신 후속자료를 조사해 OPEN/RESOLVED/SUPERSEDED/HISTORICAL_ONLY를 판정한다.
8. 같은 사실의 전재·재배포는 source lineage 하나로 묶는다.
9. 공개적으로 더 조사 가능한 material gap을 UNKNOWN으로 남기고 COMPLETE라고 선언하지 않는다.
10. 비공개 가능성이 높은 정보는 공개 경계와 attempted routes를 근거로 LIKELY_NONPUBLIC로 제안한다.

[최초 조사 source-saturation gate]

1. 이 최초 요청이 주 조사다. 후속 PUBLIC_GAP_CLOSURE는 verifier가 발견한 소수 잔여 공백을 한 번 보정하는 예외이며, 최초 조사에서 쉽게 갈 수 있는 공개 경로를 미루는 두 번째 본조사가 아니다.
2. mandatory question을 roster에 적었다는 사실은 coverage가 아니다. terminal evidence, 검증 가능한 공개경계, 또는 실제 실패한 attempted route receipt 중 하나가 있어야 조사된 question으로 취급한다.
3. `PUBLIC_SEARCHABLE`로 남길 question은 답변을 직렬화하기 전에 그 question의 official-first required source role을 실제로 시도한다. 아직 시도하지 않은 required source role이 하나라도 있으면 새 source 탐색을 계속한다.
4. `PARSER_PENDING`은 첫 PDF/HTML 표현을 읽지 못했다는 이유만으로 선택하지 않는다. 동일 official source의 공개 HTML, 첨부 PDF, 텍스트 보기, regulator mirror 등 눈에 보이는 대체 representation을 시도하고 각 실패를 route receipt로 기록한 뒤에만 허용한다.
5. 여러 mandatory question을 함께 지지하는 official filing/earnings/IR을 우선 열고, 한 source 안의 서로 다른 문장·표 행을 여러 atomic fact로 각각 보존한다. source 하나당 fact 하나로 인위적으로 제한하지 않는다.
6. final 직렬화 전에 non-terminal roster를 다시 순회한다. provider/tool이 실제로 중단되지 않았다면 `UNKNOWN_ROUTE_NOT_YET_TESTED`, 시도하지 않은 `PUBLIC_SEARCHABLE`, 대체 representation을 시도하지 않은 `PARSER_PENDING`을 남긴 채 출력을 시작하지 않는다.
7. 실제 provider/tool 중단 때문에 위 gate를 통과하지 못하면 연구가 끝난 것처럼 보이게 하지 말고 `PROVIDER_PENDING` 또는 `TRANSPORT_PENDING`으로 명시한다. 이 결과는 operational efficiency 실패로 봉인될 수 있다.
8. `ID-PLACEHOLDER`, `확인값`, 예시 URL·예시 ID 같은 스캐폴드 값을 실제 조사 결과처럼 출력하지 않는다. 실제 값을 확인하지 못한 필드는 허용된 null/빈 배열과 구체적인 non-terminal 사유로 표현한다.
9. provider가 정상 동작했는데 `source_documents`, `material_facts`, `counterfacts`, `resolution_facts`가 전부 빈 최종 JSON은 금지한다. 최소 한 개의 실제 공개 source와 그 원문에 결박된 atomic fact를 보존할 때까지 조사·직렬화를 계속한다.
10. provider 자체가 막혀 source와 fact를 하나도 만들 수 없다면 가짜 `SUCCESS` route를 만들지 않는다. 실제 실패 상태·실제로 시도한 query/URL·`PROVIDER_PENDING` 또는 `TRANSPORT_PENDING`만 기록한다.

[조사와 동시에 증거 그래프 유지 — 마지막 일괄 직렬화 금지]

1. mandatory question roster와 빈 QuestionFamilyResultV3 골격을 조사 시작 시 먼저 만든다.
2. source를 열면 SourceDocumentV3와 SearchRouteReceiptV3를 즉시 추가하고, exact excerpt를 확인한 fact는 그때 AtomicFactV3와 양방향 question binding까지 완성한다.
3. source 조사와 fact/question/lineage 직렬화를 분리해 마지막에 한꺼번에 처리하지 않는다.
4. issuer official 핵심 source를 읽은 뒤 검증 완료된 최소 core subset을 먼저 보존하고, 이후 source와 fact는 하나씩 append한다.
5. 새 후보 하나의 preflight나 binding이 실패해도 이미 검증 완료된 다른 fact를 제거하지 않는다. 실패한 그 후보만 gap으로 내린다.
6. source document와 source-backed 후보를 실제로 찾았는데 단지 최종 일괄 binding/schema 검사를 끝내지 못했다는 이유로 material/counter/resolution 배열을 전부 비우는 것은 금지한다.
7. 도구 시간이 줄면 새 source 탐색을 즉시 멈추고, 그 시점까지 완성한 source/fact/question/route graph를 유효한 JSON으로 봉인한다.

[Verifier-ready atomic evidence contract — 최우선]

각 material/counter/resolution fact는 반드시 다음 규칙을 지킨다.

1. 한 fact에는 하나의 atomic predicate만 둔다.
2. 한 fact는 하나의 source_document_id와 하나의 exact supporting excerpt로 지지한다.
3. 서로 다른 두 문장 또는 두 source를 합쳐 더 강한 하나의 statement를 만들지 않는다.
4. statement의 의미 범위는 exact excerpt보다 넓을 수 없다.
5. exact excerpt에 직접 없는 고객명, 계약성, 수량, 가격, qualification, segment, product, current status를 추론해서 넣지 않는다.
6. URL은 실제로 연 canonical 원문 URL을 사용한다.
7. 검색 결과 URL, redirect-only URL, utm/tracking URL을 canonical URL로 쓰지 않는다.
8. publication_date와 availability_date를 실제 문서에서 확인한다.
9. HTML은 heading/section/paragraph locator를, PDF는 page/table locator를 기록한다.
10. question_family_ids와 source_role_ids를 처음부터 연결한다.
11. 같은 source의 여러 사실은 source document 하나 아래 서로 다른 atomic fact로 나눈다.
12. 계산값은 material fact에 섞지 말고 derived_metrics에 원천 fact IDs와 계산식을 기록한다.
13. 원문 exact quote를 자신 있게 제공할 수 없는 후보는 material fact로 제출하지 말고 unresolved gap으로 남긴다.
14. 동일 lineage의 재인용을 독립 source로 세지 않는다.
15. final output 전 각 fact의 verifier_preflight 9개 true 항목과 derived 혼합 금지 항목을 스스로 검사한다.
16. verifier_preflight에서 하나라도 요구값과 다르면 accepted material fact로 제출하지 않는다.
17. fact의 issuer_scoped는 연결된 source document target_scope.issuer_scoped와 같아야 한다. issuer 자체 원문이 아닌 regulator/customer/partner/peer 자료라면 둘 다 false로 두며, 사실이 target을 언급한다는 이유만으로 true로 올리지 않는다.
18. question_family_results의 support_fact_ids는 material_facts만, counter_fact_ids는 counterfacts만, resolution_fact_ids는 resolution_facts만 참조한다. 한 fact가 질문 맥락에서 다른 극성으로도 읽힐 수 있으면 잘못된 종류의 칸에 중복 참조하지 말고 closure_reason에 그 경계를 설명한다.
19. question_family_results가 fact ID를 참조하면 그 fact의 question_family_ids에도 해당 question ID가 있어야 한다. 양쪽 연결을 확신할 수 없으면 question 쪽 참조를 생략하되 fact 자체와 closure_reason은 보존한다.
20. supporting_excerpt는 verifier가 내려받을 source representation에 실제로 연속 등장하는 원문이어야 한다. 표의 서로 떨어진 cell을 `A | B | C`처럼 새 문장으로 합성하지 말고, PDF/HTML text에서 연속으로 복사되는 행·문장만 사용한다.
21. publication_date와 availability_date에는 문서의 게시·공시일만 기록한다. 본문의 회사채 만기일, 계약 종료일, 전망기간, 목표연도 같은 미래 날짜를 source publication date로 사용하지 않는다.
22. 같은 predicate의 더 최신 관측치가 있으면 이전 관측치를 CURRENT material candidate로 중복 제출하지 않는다. 과거 맥락은 HISTORICAL_ONLY 경계를 명시하고, 최신 관측치와 섞어 현재 사실처럼 서술하지 않는다.
23. `issuer_scoped=false`인 fact의 `subject`는 source 원문에 실제로 연속 등장하는 가장 짧은 주체 표현을 그대로 복사한다. 원문의 여러 위치에서 회사·시설·거래 이름을 모아 합성 subject를 만들지 않는다. exact excerpt 자체가 target을 직접 언급하지 않으면 source 본문에서 그 subject와 target의 관계가 각각 문자 그대로 확인돼야 하며, 그렇지 않으면 fact가 아니라 unresolved gap으로 남긴다.
24. material/counter/resolution fact의 canonical source는 후속 verifier가 로그인·개인 cookie·JavaScript challenge 없이 다시 받을 수 있는 공개 HTML/PDF/data representation이어야 한다. 현재 연구 도구에서만 열리고 일반 공개 fetch가 401/403, 로그인 화면, anti-bot challenge로 끝나는 페이지는 그대로 제출하지 말고 official 원문·filing·issuer data·공개 mirror 중 재수집 가능한 representation을 찾아 source_document에 연결한다. 찾지 못하면 fact를 만들지 말고 attempted route와 source gap을 기록한다.
25. supporting_excerpt는 source의 원래 언어와 글자를 유지한 채 verifier가 내려받는 representation에서 그대로 복사한다. 번역, 의역, 문법 교정, 단위 환산, 숫자 표기 변경은 statement나 derived_metrics에서만 할 수 있고 supporting_excerpt에서는 금지한다.
26. fact를 추가하기 직전에 supporting_excerpt 전체를 실제로 연 source representation 안에서 문자 그대로 다시 찾아보는 literal-search self-check를 한다. 공백·줄바꿈·Unicode 문장부호 정규화 외의 변경 없이 찾히지 않으면 exact excerpt가 아니므로 다른 연속 원문을 선택하거나 그 fact를 unresolved gap으로 내린다.
27. 표의 header, row label, 값이 내려받은 representation에서 서로 떨어져 있으면 `|`, 줄바꿈 또는 설명어를 넣어 하나의 인용문으로 재조립하지 않는다. label과 값이 함께 연속 등장하는 다른 공개 representation을 찾고, 없으면 계산·추론 fact로 승격하지 않는다.
28. current material candidate는 위 literal-search와 공개 재수집 preflight를 통과한 fact만 직렬화한다. mandatory question을 채워 보이게 하려고 검증 불가능한 후보를 추가하지 말고, 해당 question에는 attempted route와 구체적 gap을 남긴다.

[Question closure]

각 mandatory question family는 다음 중 하나로 판정한다.

Terminal:
- SUPPORTED_SCORING
- PARTIALLY_SUPPORTED_SCORING
- SUPPORTED_NON_SCORING
- COUNTER_SUPPORTED
- EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH
- LIKELY_NONPUBLIC
- FUTURE_EVENT_ONLY
- NOT_APPLICABLE_WITH_REASON

Non-terminal:
- PUBLIC_SEARCHABLE
- UNKNOWN_ROUTE_NOT_YET_TESTED
- CONTRADICTED_UNRESOLVED
- SOURCE_PENDING
- PROVIDER_PENDING
- PARSER_PENDING
- VERIFIER_REPAIR_REQUIRED

EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH는 실제 attempted route receipts가 있을 때만 허용한다.
LIKELY_NONPUBLIC은 단순히 찾지 못했다는 뜻이 아니며 공개의무, 산업관행, issuer disclosure boundary와 반복 공식경로 조사 근거가 있어야 한다.

[Research status]

실제 결과에 따라 다음 중 하나를 선택한다.

- NEEDS_PUBLIC_GAP_CLOSURE
- NEEDS_COUNTER_SUPERSESSION
- NEEDS_VERIFIER_REPAIR
- COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER
- COMPLETE
- PROVIDER_PENDING
- TRANSPORT_PENDING
- BLOCKED_EXTERNAL

특정 COMPLETE 상태를 형식적으로 강제하지 않는다.

[출력 — JSON이 첫 번째이자 주 산출물]

1. `E2R_RESEARCH_DOSSIER_JSON_BEGIN` 직후 ResearchDossierV3 JSON 정확히 하나를 먼저 출력한다.
2. JSON 안에 SourceDocumentV3, Atomic material/counter/resolution facts, DerivedMetricV3, QuestionFamilyResultV3, SearchRouteReceiptV3를 모두 넣는다.
3. `E2R_RESEARCH_DOSSIER_JSON_END` 뒤 사람이 읽는 Markdown 설명은 짧게 덧붙일 수 있으나 JSON보다 먼저 쓰지 않는다.
4. score_authority=false
5. stage_authority=false

[전달 실패 방지 — JSON 직렬화 우선]

1. 조사 중 계속 유지한 evidence graph에서 유효한 ResearchDossierV3 JSON을 최종 답변의 첫 산출물로 봉인한다. 마지막에 처음부터 graph를 재작성하지 않는다.
2. ResearchDossierV3 JSON 직렬화는 생략할 수 없다. self-audit에서 문제가 발견되면 JSON 전체를 포기하지 말고 해당 fact만 제거해 unresolved_gaps와 non-terminal QuestionFamilyResultV3로 옮긴다.
3. 응답 길이가 부족할 것 같으면 Markdown 설명을 짧게 하고, 검증 가능한 atomic fact 수를 줄이되 mandatory question roster와 유효한 JSON 객체는 반드시 남긴다.
4. exact supporting excerpt는 각 atomic fact를 직접 지지하는 짧은 구절만 쓴다. 서로 다른 fact의 인용량을 합친 임의의 내부 제한 때문에 dossier 전체를 보류하지 않는다.
5. 도구 세션이 끝날 위험이 있으면 새 탐색을 중단하고 그 시점까지 검증 완료된 fact와 명시적 gap만 담은 유효한 dossier를 먼저 출력한다. 미완료 후보를 억지로 fact로 승격하지 않으며, 검증 완료된 subset을 함께 버리지 않는다.
6. 최종 답변에는 `E2R_RESEARCH_DOSSIER_JSON_BEGIN`과 `E2R_RESEARCH_DOSSIER_JSON_END` 경계가 정확히 한 쌍 있어야 한다.

최종 출력 전에 다음 self-audit를 먼저 수행하라.

- source_document_id 없는 fact 0
- exact excerpt 없는 fact 0
- multi-source compound fact 0
- statement broader than excerpt 0
- tracking URL 0
- question binding 없는 material fact 0
- as_of_date 이후 source 0
- duplicate lineage credit 0
- derived calculation mixed into quoted fact 0
- source-language literal-search 실패 0
- 번역·의역·표 재조립 supporting excerpt 0

조건을 만족하지 못한 후보는 fact에서 제거하고 unresolved gap에 남긴다.

## CompiledProResearchPromptV3 authority

- prompt_contract_version: `v3`
- pass_name: `INITIAL_FULL_RESEARCH`
- job_id: `PROMPT-V3-SNAPSHOT-C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`
- run_id: `PROMPT-V3-SNAPSHOT-RUN-C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`
- target: `BLIND-SAMPLE 블라인드 예시 대상`
- as_of_date: `2026-08-22`
- conversation_id: `TO_BE_BOUND_BY_ORCHESTRATOR`
- research_pass_id: `TO_BE_BOUND_BY_ORCHESTRATOR`
- parent_pass_id: `NONE`
- contract_unit_snapshot: `false`
- same_conversation_scope_required: `true`
- output_schema: `e2r_pro_research_dossier_v3`
- score_authority: `false`
- stage_authority: `false`
- future_source_allowed: `false`
- investment_recommendation_allowed: `false`

최종 응답에는 `[[E2R_PRO_RUN_ID:PROMPT-V3-SNAPSHOT-RUN-C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY]]`, `[[E2R_PRO_JOB_ID:PROMPT-V3-SNAPSHOT-C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY]]`, `[[E2R_PRO_PASS_ID:TO_BE_BOUND_BY_ORCHESTRATOR]]`, `[[E2R_PRO_PARENT_PASS_ID:NONE]]` marker를 각각 정확히 한 번 출력한다.

packet의 roster 밖 archetype이 더 적합해 보여도 새 ID를 만들지 않는다. `ARCHETYPE_RESELECTION_REQUIRED`와 기존 registry ID 및 source-backed 근거만 반환한다.

## 선택된 primary research contracts

### `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`

- contract_role: `PRIMARY`
- economic_mechanism: 테스트소켓/프로브 제품 노출이 고객 qualification·직접 주문·반복 출하·매출/마진으로 전환되는 메커니즘
- required_bridge_axes: customer, backlog, contract, margin
- source_role_policy: `{"llm_only_inference_is_diagnostic":true,"official_first":true,"recommended_routes":"issuer IR/공시·고객/파트너 공식자료·공급계약·실적/제품별 매출·margin·revision","source_proxy_is_non_scoring":true}`
- false_positive_guards: ["socket/HBM 제품 소개나 품질상만으로 Actionable/Green을 만들지 않는다."]
- score_authority: `false`
- stage_authority: `false`

Mandatory question families:

1. `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_Q01` — 제품 roadmap/profile과 실제 named customer qualification을 분리했는가
   - mandatory_for_full_thesis: `true`
   - question_roles: ECONOMIC_BRIDGE
   - required_primitives: named_customer_quality, qualification_confirmed
   - required_source_roles: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL
   - preferred_source_families: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL
   - affected_component_ids: bottleneck_pricing, earnings_visibility, information_confidence, market_mispricing, valuation_rerating
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`1`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["socket/HBM 제품 소개나 품질상만으로 Actionable/Green을 만들지 않는다."]
2. `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_Q02` — 고객 concentration·VIP customer·qualification status·공급 수량이 확인되는가
   - mandatory_for_full_thesis: `true`
   - question_roles: ECONOMIC_BRIDGE
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL
   - preferred_source_families: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL
   - affected_component_ids: earnings_visibility, information_confidence
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`1`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["socket/HBM 제품 소개나 품질상만으로 Actionable/Green을 만들지 않는다."]
3. `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_Q03` — 초도 공급과 repeat order·renewal·shipment·backlog를 분리했는가
   - mandatory_for_full_thesis: `true`
   - question_roles: ECONOMIC_BRIDGE
   - required_primitives: repeat_order_confirmed
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: bottleneck_pricing, earnings_visibility, information_confidence, market_mispricing, valuation_rerating
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`1`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["socket/HBM 제품 소개나 품질상만으로 Actionable/Green을 만들지 않는다."]
4. `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_Q04` — socket/probe 수요가 issuer 매출·ASP·gross margin·OPM으로 전환됐는가
   - mandatory_for_full_thesis: `true`
   - question_roles: ECONOMIC_BRIDGE, FINANCIAL_CASH_CONVERSION
   - required_primitives: socket_or_test_demand_visible, margin_bridge_visible
   - required_source_roles: ISSUER_EARNINGS, OFFICIAL_FILING
   - preferred_source_families: ISSUER_EARNINGS, OFFICIAL_FILING
   - affected_component_ids: bottleneck_pricing, earnings_visibility, eps_fcf_explosion, information_confidence, market_mispricing, valuation_rerating
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`1`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["socket/HBM 제품 소개나 품질상만으로 Actionable/Green을 만들지 않는다."]
5. `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_Q05` — 고객 제품세대 교체·qualification loss·order cancellation·대체재 counter는 무엇인가
   - mandatory_for_full_thesis: `true`
   - question_roles: ECONOMIC_BRIDGE, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL
   - preferred_source_families: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL
   - affected_component_ids: earnings_visibility, information_confidence
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["socket/HBM 제품 소개나 품질상만으로 Actionable/Green을 만들지 않는다."]
6. `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_Q06` — 고객/제품 concentration·R&D·CAPEX·FCF·working capital은 무엇인가
   - mandatory_for_full_thesis: `true`
   - question_roles: ECONOMIC_BRIDGE, FINANCIAL_CASH_CONVERSION
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL, ISSUER_EARNINGS, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL, ISSUER_EARNINGS, OFFICIAL_FILING
   - affected_component_ids: eps_fcf_explosion, capital_allocation, information_confidence
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`1`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["socket/HBM 제품 소개나 품질상만으로 Actionable/Green을 만들지 않는다."]
7. `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_Q07` — revision·valuation은 customer quality와 operating conversion을 구분하는가
   - mandatory_for_full_thesis: `true`
   - question_roles: ECONOMIC_BRIDGE, EXPECTATION_VALUATION, LIFECYCLE_SUPERSESSION
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL, CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - preferred_source_families: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL, CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - affected_component_ids: earnings_visibility, information_confidence
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["socket/HBM 제품 소개나 품질상만으로 Actionable/Green을 만들지 않는다."]

## 모든 실제 job에 적용되는 R13 cross guards

### `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`

- contract_role: `CROSS_GUARD`
- economic_mechanism: 모든 아키타입의 Stage2 false positive를 price/theme/source-proxy와 실제 economic bridge로 분리하는 공통 red-team
- required_bridge_axes: guard_risk
- source_role_policy: `{"llm_only_inference_is_diagnostic":true,"official_first":true,"recommended_routes":"각 primary contract의 source route와 verifier receipt","source_proxy_is_non_scoring":true}`
- false_positive_guards: ["이 계약은 primary archetype을 대체하지 않고 모든 job에 overlay로 적용한다."]
- score_authority: `false`
- stage_authority: `false`

Mandatory question families:

1. `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_Q01` — positive evidence가 대상 회사의 직접 cash/revenue/margin/customer bridge인가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: evidence_source_quality, missing_cashflow_bridge, theme_hype_without_revenue
   - required_source_roles: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL, ISSUER_EARNINGS, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL, ISSUER_EARNINGS, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["이 계약은 primary archetype을 대체하지 않고 모든 job에 overlay로 적용한다."]
2. `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_Q02` — price-only·theme headline·정책 headline·product profile·source proxy인가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: price_only_blowoff, policy_headline_only
   - required_source_roles: REGULATOR_OFFICIAL, ISSUER_OFFICIAL
   - preferred_source_families: REGULATOR_OFFICIAL, ISSUER_OFFICIAL
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["이 계약은 primary archetype을 대체하지 않고 모든 job에 overlay로 적용한다."]
3. `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_Q03` — wrong subject/segment/product·old fact·snippet·중복 lineage가 섞였는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["이 계약은 primary archetype을 대체하지 않고 모든 job에 overlay로 적용한다."]
4. `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_Q04` — 필수 두 번째 bridge와 counter search가 완료됐는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["이 계약은 primary archetype을 대체하지 않고 모든 job에 overlay로 적용한다."]
5. `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_Q05` — Stage2를 지지하는 non-price fact가 현재 OPEN/유효한가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["이 계약은 primary archetype을 대체하지 않고 모든 job에 overlay로 적용한다."]

### `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM`

- contract_role: `CROSS_GUARD`
- economic_mechanism: 일시적 execution watch와 현재 thesis-death hard break를 lifecycle 기반으로 구분하는 공통 red-team
- required_bridge_axes: guard_risk
- source_role_policy: `{"llm_only_inference_is_diagnostic":true,"official_first":true,"recommended_routes":"issuer/고객/규제/법원/감사 등 직접 current source","source_proxy_is_non_scoring":true}`
- false_positive_guards: ["현재 OPEN claim 없이 hard 4C를 만들지 않는다."]
- score_authority: `false`
- stage_authority: `false`

Mandatory question families:

1. `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q01` — 계약 취소·고객 영구상실·qualification 실패·회계/신뢰 break가 현재 확정됐는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: thesis_break_confirmed, contract_cancelled_or_delayed, accounting_trust_risk
   - required_source_roles: AUDITOR_FILING, REGULATOR_OFFICIAL, ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL
   - preferred_source_families: AUDITOR_FILING, REGULATOR_OFFICIAL, ISSUER_OFFICIAL, CUSTOMER_PARTNER_OFFICIAL
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["현재 OPEN claim 없이 hard 4C를 만들지 않는다."]
2. `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q02` — 지연·최적화·재협상·재개 가능성과 영구적 break를 분리했는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["현재 OPEN claim 없이 hard 4C를 만들지 않는다."]
3. `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q03` — 후속 공시가 과거 부정 claim을 해소·supersede했는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["현재 OPEN claim 없이 hard 4C를 만들지 않는다."]
4. `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q04` — 4B/4C 판단에 issuer-scoped current OPEN source가 있는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["현재 OPEN claim 없이 hard 4C를 만들지 않는다."]
5. `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q05` — valuation overheat나 가격하락을 hard break로 오인하지 않았는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: revision_slowdown, valuation_overheat
   - required_source_roles: CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - preferred_source_families: CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["현재 OPEN claim 없이 hard 4C를 만들지 않는다."]

### `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION`

- contract_role: `CROSS_GUARD`
- economic_mechanism: 감사·회계·공시 신뢰와 share-count/가격 데이터를 현재성·주체·정상/해소 문맥으로 검증하는 공통 red-team
- required_bridge_axes: guard_risk
- source_role_policy: `{"llm_only_inference_is_diagnostic":true,"official_first":true,"recommended_routes":"감사보고서·거래소/감독 공시·issuer 자본변동·시장 snapshot","source_proxy_is_non_scoring":true}`
- false_positive_guards: ["타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다."]
- score_authority: `false`
- stage_authority: `false`

Mandatory question families:

1. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q01` — 감사의견·강조사항·계속기업·restatement·auditor resignation의 정확한 주체와 현재 상태는 무엇인가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: auditor_or_disclosure_risk, restatement_risk, source_quality_conflict
   - required_source_roles: AUDITOR_FILING, REGULATOR_OFFICIAL
   - preferred_source_families: AUDITOR_FILING, REGULATOR_OFFICIAL
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다."]
2. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q02` — 적정/정상 문구를 risk로 오인했는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다."]
3. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q03` — 과거 문제는 최신 감사/공시에서 해소·재발·미해결인가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: AUDITOR_FILING, REGULATOR_OFFICIAL
   - preferred_source_families: AUDITOR_FILING, REGULATOR_OFFICIAL
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다."]
4. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q04` — share issuance·희석·분할·소각·시장 데이터의 denominator가 일치하는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: share_count_drift
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다."]
5. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q05` — 가격/시총/valuation snapshot이 as_of_date와 맞고 score proxy로 오용되지 않았는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: price_only_blowoff
   - required_source_roles: CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - preferred_source_families: CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다."]

### `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`

- contract_role: `CROSS_GUARD`
- economic_mechanism: 과거 high-MAE 학습을 현재 가격 outcome 누수 없이 execution·liquidity·valuation·positioning fragility 질문으로 변환하는 공통 guard
- required_bridge_axes: guard_risk
- source_role_policy: `{"llm_only_inference_is_diagnostic":true,"official_first":true,"recommended_routes":"현재 공시/유동성/자본/valuation과 blind-safe historical contract metadata","source_proxy_is_non_scoring":true}`
- false_positive_guards: ["미래 가격 outcome·과거 MAE를 current score evidence로 사용하지 않는다."]
- score_authority: `false`
- stage_authority: `false`

Mandatory question families:

1. `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_Q01` — 현재 valuation·liquidity·share issuance·positioning·execution risk가 무엇인가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: valuation_overheat, liquidity_or_microcap_risk, execution_risk_score, positioning_reversal_risk
   - required_source_roles: CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - preferred_source_families: CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["미래 가격 outcome·과거 MAE를 current score evidence로 사용하지 않는다."]
2. `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_Q02` — 비가격 thesis bridge가 약한데 가격만 확장됐는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["미래 가격 outcome·과거 MAE를 current score evidence로 사용하지 않는다."]
3. `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_Q03` — 과거 calibration anchor는 질문 설계에만 쓰이고 현재 점수에 직접 들어가지 않았는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["미래 가격 outcome·과거 MAE를 current score evidence로 사용하지 않는다."]
4. `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_Q04` — as_of_date 이후 MFE/MAE·가격 결과가 production prompt와 fact에 노출되지 않았는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: DIRECT_PREDICATE
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["미래 가격 outcome·과거 MAE를 current score evidence로 사용하지 않는다."]
5. `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_Q05` — 현재 non-price break가 없다면 high-MAE history만으로 4B/4C를 만들지 않았는가
   - mandatory_for_full_thesis: `true`
   - question_roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - required_primitives: high_mae_history
   - required_source_roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - preferred_source_families: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected_component_ids: GUARD_ONLY
   - allowed_terminal_statuses: SUPPORTED_SCORING, PARTIALLY_SUPPORTED_SCORING, SUPPORTED_NON_SCORING, COUNTER_SUPPORTED, EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH, LIKELY_NONPUBLIC, FUTURE_EVENT_ONLY, NOT_APPLICABLE_WITH_REASON
   - adequate_search: official-first=`true`, minimum_distinct_source_routes=`2`, independent_no_new_route_confirmations=`2`
   - false_positive_guards: ["미래 가격 outcome·과거 MAE를 current score evidence로 사용하지 않는다."]

## 현재 ResearchPacketV3 context

```json
{
  "as_of_date": "2026-08-22",
  "business_snapshot": {},
  "candidate_archetypes": [
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"
  ],
  "forbidden_inferences": null,
  "fresh_blind_boundary": null,
  "job_id": "PROMPT-V3-SNAPSHOT-C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "research_mode": "FULL_RESEARCH",
  "research_objectives": null,
  "revision_valuation_snapshot": {},
  "run_id": "PROMPT-V3-SNAPSHOT-RUN-C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "schema_version": "e2r_pro_research_packet_v3",
  "selected_archetypes": [
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"
  ],
  "source_preferences": null,
  "structured_financial_snapshot": {},
  "target": {
    "aliases": [],
    "company_name": "블라인드 예시 대상",
    "symbol": "BLIND-SAMPLE",
    "target_id": "BLIND-SAMPLE"
  },
  "trigger_summary": []
}
```

이 packet은 연구 범위와 시작점일 뿐 정답, score 또는 Stage authority가 아니다.

## ResearchDossierV3 exact output schema

아래 JSON Schema를 정확히 만족하는 JSON을 `E2R_RESEARCH_DOSSIER_JSON_BEGIN`과 `E2R_RESEARCH_DOSSIER_JSON_END` 사이에 정확히 하나 출력한다.

```json
{"$defs":{"archetypeRoster":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":1,"type":"array","uniqueItems":true},"atomicFact":{"additionalProperties":false,"properties":{"business_segment":{"minLength":1,"type":"string"},"candidate_component_ids":{"items":{"$ref":"#/$defs/componentId"},"type":"array","uniqueItems":true},"confidence":{"maximum":1,"minimum":0,"type":"number"},"current_status":{"enum":["CURRENT","OPEN","RESOLVED","SUPERSEDED","HISTORICAL_ONLY"]},"direction":{"enum":["POSITIVE","NEGATIVE","NEUTRAL","RESOLUTION"]},"dossier_fact_id":{"pattern":"^(FACT|PROFACT)-[A-Za-z0-9._:-]+$","type":"string"},"economic_mechanism_id":{"minLength":1,"type":"string"},"event_date":{"format":"date","type":["string","null"]},"fact_kind":{"enum":["MATERIAL","COUNTER","RESOLUTION"]},"issuer_scoped":{"type":"boolean"},"period":{"type":["string","null"]},"predicate_id":{"minLength":1,"type":"string"},"product_family":{"minLength":1,"type":"string"},"question_family_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"research_pass_id":{"minLength":1,"type":"string"},"source_document_id":{"minLength":1,"type":"string"},"source_locator":{"minLength":1,"type":"string"},"statement":{"minLength":1,"type":"string"},"subject":{"minLength":1,"type":"string"},"supporting_excerpt":{"minLength":1,"type":"string"},"target_id":{"minLength":1,"type":"string"},"unit":{"type":["string","null"]},"value":{},"verifier_preflight":{"$ref":"#/$defs/verifierPreflight"}},"required":["dossier_fact_id","research_pass_id","fact_kind","statement","predicate_id","direction","target_id","subject","issuer_scoped","business_segment","product_family","economic_mechanism_id","value","unit","period","event_date","current_status","question_family_ids","candidate_component_ids","source_document_id","supporting_excerpt","source_locator","confidence","verifier_preflight"],"type":"object"},"availabilityClass":{"enum":["PUBLIC_SEARCHABLE","LIKELY_NONPUBLIC","FUTURE_EVENT_ONLY","PROVIDER_BLOCKED","PARSER_BLOCKED","NOT_APPLICABLE","UNKNOWN_ROUTE_NOT_YET_TESTED"]},"componentId":{"enum":["eps_fcf_explosion","earnings_visibility","bottleneck_pricing","market_mispricing","valuation_rerating","capital_allocation","information_confidence"]},"derivedMetric":{"additionalProperties":false,"properties":{"derived_metric_id":{"pattern":"^DERIVED-[A-Za-z0-9._:-]+$","type":"string"},"formula":{"minLength":1,"type":"string"},"input_fact_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"issuer_reported_metric":{"type":"boolean"},"metric_name":{"minLength":1,"type":"string"},"period":{"type":["string","null"]},"researcher_defined":{"type":"boolean"},"result_value":{"type":["number","integer","null"]},"score_authority":{"const":false},"unit":{"type":["string","null"]}},"required":["derived_metric_id","metric_name","formula","input_fact_ids","result_value","unit","period","researcher_defined","issuer_reported_metric","score_authority"],"type":"object"},"factIdRoster":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"gap":{"additionalProperties":true,"properties":{"affected_component_ids":{"items":{"$ref":"#/$defs/componentId"},"type":"array","uniqueItems":true},"archetype_id":{"minLength":1,"type":"string"},"attempted_source_role_ids":{"$ref":"#/$defs/stringRoster"},"availability_class":{"$ref":"#/$defs/availabilityClass"},"could_change_hard_break":{"type":"boolean"},"could_change_score":{"type":"boolean"},"could_change_stage":{"type":"boolean"},"gap_id":{"minLength":1,"type":"string"},"materiality":{"enum":["CORE_SCORE","SCORE_BOUNDARY","STAGE_BOUNDARY","HARD_BREAK","MONITORING"]},"question_family_id":{"minLength":1,"type":"string"},"required_source_role_ids":{"$ref":"#/$defs/stringRoster"},"stable_gap_key":{"minLength":1,"type":"string"},"status":{"$ref":"#/$defs/questionStatus"}},"required":["gap_id","stable_gap_key","archetype_id","question_family_id","status","availability_class","materiality","required_source_role_ids","attempted_source_role_ids","affected_component_ids","could_change_score","could_change_stage","could_change_hard_break"],"type":"object"},"questionFamilyResult":{"additionalProperties":false,"properties":{"adequate_search_proven":{"type":"boolean"},"affected_component_ids":{"items":{"$ref":"#/$defs/componentId"},"type":"array","uniqueItems":true},"archetype_id":{"minLength":1,"type":"string"},"attempted_source_role_ids":{"$ref":"#/$defs/stringRoster"},"availability_class":{"$ref":"#/$defs/availabilityClass"},"closure_reason":{"minLength":1,"type":"string"},"could_change_hard_break":{"type":"boolean"},"could_change_score":{"type":"boolean"},"could_change_stage":{"type":"boolean"},"counter_fact_ids":{"$ref":"#/$defs/factIdRoster"},"question_family_id":{"minLength":1,"type":"string"},"required_source_roles_missing":{"$ref":"#/$defs/stringRoster"},"required_source_roles_satisfied":{"$ref":"#/$defs/stringRoster"},"resolution_fact_ids":{"$ref":"#/$defs/factIdRoster"},"search_route_receipt_ids":{"$ref":"#/$defs/stringRoster"},"status":{"$ref":"#/$defs/questionStatus"},"support_fact_ids":{"$ref":"#/$defs/factIdRoster"}},"required":["archetype_id","question_family_id","status","support_fact_ids","counter_fact_ids","resolution_fact_ids","attempted_source_role_ids","search_route_receipt_ids","required_source_roles_satisfied","required_source_roles_missing","availability_class","affected_component_ids","could_change_score","could_change_stage","could_change_hard_break","closure_reason","adequate_search_proven"],"type":"object"},"questionStatus":{"enum":["SUPPORTED_SCORING","PARTIALLY_SUPPORTED_SCORING","SUPPORTED_NON_SCORING","COUNTER_SUPPORTED","EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH","LIKELY_NONPUBLIC","FUTURE_EVENT_ONLY","NOT_APPLICABLE_WITH_REASON","PUBLIC_SEARCHABLE","UNKNOWN_ROUTE_NOT_YET_TESTED","CONTRADICTED_UNRESOLVED","SOURCE_PENDING","PROVIDER_PENDING","PARSER_PENDING","VERIFIER_REPAIR_REQUIRED"]},"researchPass":{"additionalProperties":false,"properties":{"parent_pass_id":{"type":["string","null"]},"pass_id":{"minLength":1,"type":"string"},"pass_name":{"enum":["INITIAL_FULL_RESEARCH","ARCHETYPE_CONFIRMATION","PRIMARY_OFFICIAL_RESEARCH","ECOSYSTEM_COUNTER_RESEARCH","REVISION_VALUATION_RESEARCH","QUESTION_CLOSURE_AUDIT","PUBLIC_GAP_CLOSURE","COUNTER_SUPERSESSION_CLOSURE","SOURCE_VERIFICATION","VERIFIER_REPAIR","SATURATION_AUDIT","FULL_THESIS_READY"]},"prompt_hash":{"pattern":"^[a-f0-9]{64}$","type":"string"},"response_hash":{"pattern":"^[a-f0-9]{64}$","type":["string","null"]},"status":{"enum":["COMPLETE","PENDING","PROVIDER_PENDING","PARSER_PENDING","TRANSPORT_PENDING","FAILED"]}},"required":["pass_id","parent_pass_id","pass_name","status","prompt_hash","response_hash"],"type":"object"},"researchStatus":{"enum":["NEEDS_PUBLIC_GAP_CLOSURE","NEEDS_COUNTER_SUPERSESSION","NEEDS_VERIFIER_REPAIR","COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER","COMPLETE","PROVIDER_PENDING","TRANSPORT_PENDING","BLOCKED_EXTERNAL"]},"searchRouteReceipt":{"additionalProperties":false,"properties":{"accepted_fact_ids":{"$ref":"#/$defs/factIdRoster"},"archetype_id":{"minLength":1,"type":"string"},"gap_id":{"type":["string","null"]},"no_new_route_reason":{"type":["string","null"]},"opened_source_urls":{"items":{"format":"uri","type":"string"},"type":"array","uniqueItems":true},"pass_id":{"minLength":1,"type":"string"},"performed_at":{"format":"date-time","type":"string"},"provider_status":{"enum":["SUCCESS","PROVIDER_PENDING","PARSER_PENDING","TRANSPORT_PENDING","FAILED"]},"query_or_navigation_objective":{"minLength":1,"type":"string"},"query_text":{"type":["string","null"]},"question_family_id":{"minLength":1,"type":"string"},"rejected_candidate_ids":{"$ref":"#/$defs/factIdRoster"},"result_count_seen":{"minimum":0,"type":"integer"},"route_receipt_id":{"minLength":1,"type":"string"},"source_role_id":{"minLength":1,"type":"string"}},"required":["route_receipt_id","pass_id","archetype_id","question_family_id","gap_id","source_role_id","query_or_navigation_objective","query_text","result_count_seen","opened_source_urls","accepted_fact_ids","rejected_candidate_ids","provider_status","no_new_route_reason","performed_at"],"type":"object"},"sourceDocument":{"additionalProperties":false,"properties":{"as_of_cutoff_pass":{"const":true},"availability_date":{"format":"date","type":"string"},"canonical_url":{"format":"uri","type":"string"},"document_type":{"enum":["HTML","PDF","FILING","IR","NEWS","MARKET_DATA","DATASET"]},"lineage_id":{"pattern":"^(SL|LINEAGE)-[A-Za-z0-9._:-]+$","type":"string"},"locator_type":{"enum":["HTML_HEADING","HTML_PARAGRAPH","PDF_PAGE","TABLE","FILING_SECTION"]},"locator_value":{"minLength":1,"type":"string"},"opened_and_read":{"const":true},"opened_url":{"format":"uri","type":"string"},"publication_date":{"format":"date","type":"string"},"source_document_id":{"pattern":"^(SRC|PROSRC)-[A-Za-z0-9._:-]+$","type":"string"},"source_publisher":{"minLength":1,"type":"string"},"source_role_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"source_title":{"minLength":1,"type":"string"},"target_scope":{"$ref":"#/$defs/targetScope"}},"required":["source_document_id","canonical_url","opened_url","source_title","source_publisher","publication_date","availability_date","source_role_ids","document_type","target_scope","locator_type","locator_value","lineage_id","opened_and_read","as_of_cutoff_pass"],"type":"object"},"sourceLineage":{"additionalProperties":false,"properties":{"fact_ids":{"$ref":"#/$defs/factIdRoster"},"independence_group_id":{"minLength":1,"type":"string"},"lineage_id":{"pattern":"^(SL|LINEAGE)-[A-Za-z0-9._:-]+$","type":"string"},"source_document_ids":{"$ref":"#/$defs/stringRoster"},"status":{"enum":["ACTIVE","SUPERSEDED","REJECTED","WITHDRAWN"]}},"required":["lineage_id","source_document_ids","fact_ids","independence_group_id","status"],"type":"object"},"stringRoster":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"targetScope":{"additionalProperties":false,"properties":{"business_segment":{"minLength":1,"type":"string"},"issuer_scoped":{"type":"boolean"},"product_family":{"minLength":1,"type":"string"},"subject":{"minLength":1,"type":"string"},"target_id":{"minLength":1,"type":"string"}},"required":["target_id","issuer_scoped","subject","business_segment","product_family"],"type":"object"},"verifierPreflight":{"additionalProperties":false,"properties":{"as_of_cutoff_pass":{"const":true},"canonical_url_used":{"const":true},"derived_calculation_mixed_into_fact":{"const":false},"exact_excerpt_copied_from_source":{"const":true},"lineage_duplicate_checked":{"const":true},"publication_date_confirmed":{"const":true},"single_atomic_predicate":{"const":true},"source_opened":{"const":true},"statement_not_broader_than_excerpt":{"const":true},"target_subject_scope_confirmed":{"const":true}},"required":["source_opened","canonical_url_used","exact_excerpt_copied_from_source","statement_not_broader_than_excerpt","single_atomic_predicate","target_subject_scope_confirmed","publication_date_confirmed","as_of_cutoff_pass","lineage_duplicate_checked","derived_calculation_mixed_into_fact"],"type":"object"}},"$id":"https://e2r.local/schema/e2r_pro_research_dossier_v3.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","additionalProperties":false,"properties":{"as_of_date":{"format":"date","type":"string"},"business_model":{"type":"object"},"candidate_archetypes":{"$ref":"#/$defs/archetypeRoster"},"component_research":{"propertyNames":{"$ref":"#/$defs/componentId"},"type":"object"},"conversation_id":{"minLength":1,"type":"string"},"counterfacts":{"items":{"$ref":"#/$defs/atomicFact"},"type":"array"},"derived_metrics":{"items":{"$ref":"#/$defs/derivedMetric"},"type":"array"},"job_id":{"minLength":1,"type":"string"},"material_facts":{"items":{"$ref":"#/$defs/atomicFact"},"type":"array"},"parent_pass_id":{"type":["string","null"]},"question_family_results":{"items":{"$ref":"#/$defs/questionFamilyResult"},"type":"array"},"research_pass_id":{"minLength":1,"type":"string"},"research_passes":{"items":{"$ref":"#/$defs/researchPass"},"type":"array"},"research_saturation":{"type":"object"},"research_status":{"$ref":"#/$defs/researchStatus"},"resolution_facts":{"items":{"$ref":"#/$defs/atomicFact"},"type":"array"},"run_id":{"minLength":1,"type":"string"},"schema_version":{"const":"e2r_pro_research_dossier_v3"},"score_authority":{"const":false},"search_route_receipts":{"items":{"$ref":"#/$defs/searchRouteReceipt"},"type":"array"},"selected_archetypes":{"$ref":"#/$defs/archetypeRoster"},"source_documents":{"items":{"$ref":"#/$defs/sourceDocument"},"type":"array"},"source_lineages":{"items":{"$ref":"#/$defs/sourceLineage"},"type":"array"},"stage_authority":{"const":false},"structured_metrics":{"type":"object"},"target":{"additionalProperties":false,"properties":{"aliases":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"company_name":{"minLength":1,"type":"string"},"symbol":{"type":"string"},"target_id":{"minLength":1,"type":"string"}},"required":["target_id","company_name","aliases"],"type":"object"},"unresolved_gaps":{"items":{"$ref":"#/$defs/gap"},"type":"array"}},"required":["schema_version","job_id","run_id","conversation_id","research_pass_id","parent_pass_id","target","as_of_date","candidate_archetypes","selected_archetypes","research_status","business_model","source_documents","material_facts","counterfacts","resolution_facts","derived_metrics","question_family_results","component_research","structured_metrics","unresolved_gaps","source_lineages","search_route_receipts","research_passes","research_saturation","score_authority","stage_authority"],"title":"E2R Pro Research Dossier V3","type":"object"}
```

schema의 `verifier_preflight`에서 다음 9개 필드는 모두 true여야 한다: `source_opened`, `canonical_url_used`, `exact_excerpt_copied_from_source`, `statement_not_broader_than_excerpt`, `single_atomic_predicate`, `target_subject_scope_confirmed`, `publication_date_confirmed`, `as_of_cutoff_pass`, `lineage_duplicate_checked`.
`derived_calculation_mixed_into_fact`는 false여야 한다.
DerivedMetricV3는 `input_fact_ids`와 `formula`로 계산 계보를 분리하며 quoted atomic fact에 계산 결과를 섞지 않는다.
supporting_excerpt는 source의 원래 언어를 유지하고 실제 공개 representation에서 문자 그대로 다시 찾을 수 있어야 한다. 번역·의역·문법 교정·단위 환산·표 cell 재조립은 금지한다.
검증을 통과하지 못한 candidate는 accepted fact로 강행하지 말고 unresolved gap에 남긴다.
