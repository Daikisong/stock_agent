# C17_CHEMICAL_COMMODITY_MARGIN_SPREAD Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `21`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 011170 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | 134700.0 | None | None | no_valid_stage_transition |
| 011790 | 011790 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | 97000.0 | None | None | no_valid_stage_transition |
| 051910 | 051910 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | 430000.0 | None | None | no_valid_stage_transition |
| C17_166_001 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_166_002 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_166_003 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_166_004 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 110600.0 | None | None | 20.52 | None | stage2_actionable_best_entry |
| C17_166_005 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 306000.0 | None | None | 37.75 | None | stage2_actionable_best_entry |
| C17_166_006 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_166_007 | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_166_008 | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_166_009 | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_166_010 | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_193_001 | 051910 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 402500.0 | None | None | 2.36 | None | stage2_captured_most_upside |
| C17_193_002 | 051910 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_193_003 | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 25500.0 | None | None | 13.73 | None | stage2_captured_most_upside |
| C17_193_004 | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_193_005 | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 95400.0 | None | None | 12.47 | None | stage2_captured_most_upside |
| C17_193_006 | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 77000.0 | None | None | 71.17 | None | stage2_actionable_best_entry |
| C17_193_007 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 133000.0 | None | None | 21.05 | None | stage2_captured_most_upside |
| C17_193_008 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 104800.0 | None | None | 12.6 | None | stage2_captured_most_upside |
