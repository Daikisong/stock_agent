# Research To Runtime Root Cause - 2026-07-05

## Verdict

`FULL_THESIS_PRODUCTION_PASS`라는 예전 라벨은 너무 넓었다. 현재 정확한 라벨은 `PRODUCTION_FULL_E2R_SCORE_PATH_PASS`이고, `MEANINGFUL_FULL_THESIS_EVIDENCE_PASS=false`다.

쉬운 예: 시험지가 100점 만점으로 채점되긴 했지만, 한 과목(C05) 시험지만 10장 채점된 상태다. 전체 과목 시험이 끝난 것이 아니다.

## Current Facts

- full_thesis_row_count: `3`
- full_thesis_by_archetype: `{"C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 2, "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 1}`
- distinct_full_thesis_archetype_count: `2`
- c05_full_thesis_share: `0.666667`
- required_positive_missing_full_thesis_row_count: `3`
- green_gap_full_thesis_row_count: `3`
- target_archetype_unknown_promoted_count: `0`
- source_primary_context_promoted_count: `0`

## Six Audit Questions

1. 왜 production FULL_THESIS 10개가 전부 C05인가?
   - seed target은 UNKNOWN이었고, source_primary/planner top1 경로가 C05로 쏠렸다.
2. target_archetype_counts가 UNKNOWN인데 왜 C05가 되는가?
   - target이 아니라 event-board/refresh queue의 source_primary 문맥과 planner top1이 최종 primary가 됐다.
3. 27.9998 / 77.9998 점수는 어디서 나오는가?
   - C05 weight profile에 raw component를 clamp 후 재가중한 FULL_E2R_100 score path에서 나온다.
4. C05가 아닌 후보는 왜 0개인가?
   - C06/C01 일부는 source pending으로 막혔고, C08/C15/C17/C24/C28 등은 이번 production full-thesis 후보 경로에 올라오지 않았다.
5. required_positive_missing_primitives가 있는데 왜 pass인가?
   - 기존 pass는 score path closed만 봤기 때문이다. meaningful pass는 required-positive gap을 허용하면 안 된다.
6. 삼성전자/하이닉스는 왜 production row가 아닌가?
   - 삼성전자는 C06 blocked candidate이고, 하이닉스는 planner C06 시도 후 accepted claim이 만들어지지 않았다. controlled smoke 점수는 production 점수가 아니다.

## Required Direction

C05 하나가 아니라 C01~C36 각 아키타입에 대해 attempt, source route, accepted claim, StageCourt, full-thesis 상태를 계속 이 matrix로 증명해야 한다.
