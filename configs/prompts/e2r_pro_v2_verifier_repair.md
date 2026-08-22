아래 fact candidate가 deterministic verifier에서 탈락했다. rejection reason과 fetched source excerpt를 확인하고 같은 ChatGPT 대화에서 해당 question만 repair하라.

허용되는 조치는 원문에 맞는 exact excerpt로 수정, subject/target/segment/product 수정, 올바른 source URL로 대체, 과장된 statement 축소, 명시적 WITHDRAWN 결정뿐이다.

없는 quote 생성, 같은 잘못된 URL을 문장만 바꿔 재제출, score/Stage 보정을 위한 fact 창작, 기존 accepted fact 삭제는 금지한다. 수정 candidate 또는 WITHDRAWN 결정을 append-only ResearchDossierV2 delta로 반환한다. 수정본도 deterministic verifier를 다시 통과해야 한다.

{{COMPILED_CONTEXT}}
