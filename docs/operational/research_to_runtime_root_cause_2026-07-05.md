# Research To Runtime Root Cause - 2026-07-05

## Verdict

`FULL_THESIS_PRODUCTION_PASS`라는 예전 라벨은 너무 넓었다. 현재 정확한 라벨은 `PRODUCTION_FULL_E2R_SCORE_PATH_PASS`이고, `MEANINGFUL_FULL_THESIS_EVIDENCE_PASS=false`다.

쉬운 예: 예전에는 한 과목(C05) 시험지만 10장 채점된 상태였고, 현재는 6개 과목의 시험지가 채점대에 올라왔다. 하지만 필수 증빙칸이 비어 있으면 전체 과목 합격은 아니다.

## Current Facts

- full_thesis_row_count: `6`
- full_thesis_by_archetype: `{"C01_ORDER_BACKLOG_MARGIN_BRIDGE": 1, "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 1, "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 1, "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 1, "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": 1, "C24_BIO_TRIAL_DATA_EVENT_RISK": 1}`
- distinct_full_thesis_archetype_count: `6`
- c05_full_thesis_share: `0.166667`
- required_positive_missing_full_thesis_row_count: `5`
- green_gap_full_thesis_row_count: `5`
- target_archetype_unknown_promoted_count: `0`
- source_primary_context_promoted_count: `0`

## Six Audit Questions

1. 왜 예전 production FULL_THESIS 10개가 전부 C05였고, 현재는 어떻게 바뀌었나?
   - 예전 seed target은 UNKNOWN이었고 source_primary/planner top1 경로가 C05로 쏠렸다. 현재 promoted row는 C01_ORDER_BACKLOG_MARGIN_BRIDGE/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG/C05_EPC_MEGA_CONTRACT_MARGIN_GAP/C06_HBM_MEMORY_CUSTOMER_CAPACITY/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD/C24_BIO_TRIAL_DATA_EVENT_RISK 경로로 분산됐다.
2. target_archetype_counts가 UNKNOWN인데 왜 C05가 되는가?
   - 예전에는 target이 아니라 event-board/refresh queue의 source_primary 문맥과 planner top1이 최종 primary가 됐다. 현재 promoted row의 target_archetype_unknown_promoted_count는 0이다.
3. 27.9998 / 77.9998 점수는 어디서 나오는가?
   - C05 weight profile에 raw component를 clamp 후 재가중한 FULL_E2R_100 score path에서 나온다.
4. C05가 아닌 후보는 왜 0개인가?
   - 이 질문은 예전 C05-only 산출물에 대한 질문이다. 현재 non-C05 score-path row는 C01_ORDER_BACKLOG_MARGIN_BRIDGE/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG/C06_HBM_MEMORY_CUSTOMER_CAPACITY/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD/C24_BIO_TRIAL_DATA_EVENT_RISK이고, mandatory missing prefix는 C08/C15/C28다.
5. required_positive_missing_primitives가 있는데 왜 pass인가?
   - 기존 pass는 score path closed만 봤기 때문이다. meaningful pass는 required-positive gap을 허용하면 안 된다.
6. 삼성전자/하이닉스는 왜 production row가 아닌가?
   - 현재 삼성전자 005930은 C06 production score-path row가 생겼지만 required-positive/Green gap 때문에 meaningful pass가 아니다. 하이닉스 controlled smoke는 여전히 production full-thesis row와 분리해서 본다.

## Required Direction

C05 하나가 아니라 C01~C32와 R13 cross-archetype 4개, 총 36개 contract에 대해 attempt, source route, accepted claim, StageCourt, full-thesis 상태를 계속 이 matrix로 증명해야 한다.
