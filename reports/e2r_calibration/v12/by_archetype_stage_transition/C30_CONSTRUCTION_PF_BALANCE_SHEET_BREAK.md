# C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `3`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C30_R10L92_009410_TAEYOUNG_PF_WORKOUT_HARD_BREAK | 009410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_R10L92_034300_SHINSEGAE_CONSTRUCTION_CA_LATE_PRICE | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_R10L92_183190_ASIA_CEMENT_MARGIN | 183190 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 10260.0 | None | None | 13.16 | None | stage2_actionable_best_entry |
