# Research To Runtime Acceptance Report - 2026-07-05

## Verdict

- final_status: `MEANINGFUL_RUNTIME_PARITY_NOT_READY`
- production_full_e2r_score_path_pass: `True`
- meaningful_full_thesis_evidence_pass: `False`
- archetype_balanced_full_thesis_pass: `False`

쉬운 예: 이제 C05 한 과목만 채점된 상태는 벗어났고 7개 과목의 score path는 닫혔다. 하지만 7개 모두 필수 증빙칸과 Green 증빙칸이 비어 있어 최종 합격증은 아직 아니다.

## Required Metrics

- research case count: `11401`
- source quality breakdown: `{"A1_URL_PENDING": 19, "A2_URL_BACKED": 3150, "EVIDENCE_URL_PENDING": 185, "PRICE_PATH_ONLY": 2204, "SHADOW_ONLY": 529, "SOURCE_PROXY_ONLY": 5314}`
- URL-backed replay count: `3150`
- source-proxy-only repair count: `5314`
- archetype memory card count: `36`
- source route pattern count: `1855`
- source route gap task count: `15`
- full-thesis candidate attempts by archetype: `{"C01_ORDER_BACKLOG_MARGIN_BRIDGE": 2, "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 2, "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 3, "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 3, "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY": 1, "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": 1, "C15_MATERIAL_SPREAD_SUPERCYCLE": 1, "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": 1, "C24_BIO_TRIAL_DATA_EVENT_RISK": 1, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": 1, "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": 3}`
- promoted full-thesis rows by archetype: `{"C01_ORDER_BACKLOG_MARGIN_BRIDGE": 1, "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 1, "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 1, "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 1, "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": 1, "C24_BIO_TRIAL_DATA_EVENT_RISK": 1}`
- required positive missing rate: `0.833333`
- green gap rate: `0.833333`
- distinct archetype count: `6`
- C05 share: `0.166667`
- planner C05 top1 share: `0.027027`
- research memory follow-up task count: `38`
- research memory follow-up by archetype: `{"C01_ORDER_BACKLOG_MARGIN_BRIDGE": 5, "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 2, "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 3, "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 5, "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY": 2, "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": 10, "C15_MATERIAL_SPREAD_SUPERCYCLE": 4, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": 4, "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": 3}`
- all-archetype runtime status rows: `36`
- canonical C contract rows: `32`
- cross-archetype rows: `4`
- registry scope counts: `{"C_CANONICAL_ARCHETYPE": 32, "R13_CROSS_ARCHETYPE": 4}`
- exact registry row coverage: `True`
- missing parity source rows: `0`
- duplicate parity source rows: `0`
- extra parity source rows: `0`
- all contracts have memory card: `True`
- all contracts have source route patterns: `True`
- runtime proof counts: `{"NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP": 5, "NOT_PROVEN_SCORE_PATH_ONLY": 5, "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM": 22, "NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED": 3, "RUNTIME_PARITY_PROVEN": 1}`
- next runtime attempt plan rows: `35`
- next runtime source task shells: `105`
- next runtime seed events: `105`
- next runtime attempt types: `{"ARCHETYPE_TARGET_MATERIALIZATION": 3, "BLOCKED_CANDIDATE_GAP_CLOSURE": 5, "PROMOTED_SCORE_PATH_GAP_CLOSURE": 5, "SOURCE_EXECUTION_REPAIR": 22}`
- runtime execution manifest status: `READY_FOR_RESEARCH_BRAIN_INPUT_NOT_EXECUTED_BY_PARITY_CLI`
- runtime execution seed path: `docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl`
- runtime execution command target gate: `full_thesis`

## Production Vs Smoke

C06 production score-path symbols: `005930`
C06 remaining production blockers: `FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP, GREEN_GAP_ON_PROMOTED_ROW, REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW, SOURCE_PENDING_REQUIRED_OR_GREEN_PRIMITIVES`

삼성전자처럼 production score path까지 올라온 row도 controlled smoke와 섞으면 안 된다. production row는 source-backed claim/gap 장부 기준으로 읽고, smoke 점수는 파이프라인 반응을 보는 진단값으로만 본다.

쉬운 예: 삼성전자 production row는 실제 시험장 답안지이고, controlled smoke는 모의고사 답안지다. 실제 답안지가 있어도 필수 첨부서류가 빠졌으면 합격이 아니고, 모의고사 점수로 합격 처리하면 안 된다.

## Blockers

- `GREEN_GAP_ON_PROMOTED_ROWS`
- `MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING`
- `PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS`
- `REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS`
- candidate_selection: `required_positive_missing_promoted_rows`
