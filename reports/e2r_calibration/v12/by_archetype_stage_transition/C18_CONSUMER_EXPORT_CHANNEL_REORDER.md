# C18_CONSUMER_EXPORT_CHANNEL_REORDER Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `3`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R5L99_C18_CJSEAFOOD_2024_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP_4B | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 6320.0 | None | None | 4b_good_peak_capture |
| R5L99_C18_FNF_2024_APPAREL_EXPORT_CHANNEL_INVENTORY_FALSE_STAGE2 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 87300.0 | None | None | 2.52 | None | stage2_actionable_best_entry |
| R5L99_C18_SAMYANGFOODS_2024_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_POSITIVE | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 177400.0 | None | None | 304.74 | None | stage2_actionable_best_entry |
