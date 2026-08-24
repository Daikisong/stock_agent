아래 fact candidate가 deterministic verifier에서 탈락했다. rejection reason과 fetched source excerpt를 확인하고 같은 ChatGPT 대화에서 해당 question만 repair하라.

허용되는 조치는 원문에 맞는 exact excerpt로 수정, subject/target/segment/product 수정, 올바른 source URL로 대체, 과장된 statement 축소, 명시적 WITHDRAWN 결정뿐이다.

없는 quote 생성, 같은 잘못된 URL을 문장만 바꿔 재제출, score/Stage 보정을 위한 fact 창작, 기존 accepted fact 삭제는 금지한다. 전체 ResearchDossierV2를 반환하되 변경은 append-only repair delta로만 표현한다.

각 탈락 candidate마다 `verification_repair_register`에 원래 `candidate_id`, exact `question_family_id`, `rejection_category`, 그리고 `CORRECTED|REPLACED|NARROWED|WITHDRAWN` 중 하나의 `status`를 기록한다. 수정할 때는 새 `dossier_fact_id`, 원래 candidate를 가리키는 `repair_of_candidate_id`, 현재 repair `research_pass_id`를 가진 fact를 정확히 하나 추가한다. 새 URL이면 그 fact를 연결한 새 source lineage receipt도 추가한다. WITHDRAWN이면 replacement fact를 추가하지 않는다. 기존 accepted fact와 lineage는 그대로 보존한다.

replacement fact를 추가했다면 현재 repair pass의 새 `search_route_receipt`를 반드시 추가하고, 그 receipt의 `accepted_fact_ids`와 해당 question의 fact/route ID roster에 replacement fact를 연결한다. 기존 route receipt를 수정하지 않는다.

수정본은 deterministic verifier를 다시 통과해야 하며 Pro의 register status 자체는 acceptance 권한이 아니다.

{{COMPILED_CONTEXT}}
