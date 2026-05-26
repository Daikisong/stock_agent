# C17_CHEMICAL_COMMODITY_MARGIN_SPREAD Stage Transition Report

v12 stage transition은 shadow-only 진단입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, default scoring did not change.

- stage_transition_summary_rows: `16`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 004000 | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 006650 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 009830 | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 010060 | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 011170 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 011780 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 011790 | 011790 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 298020 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R13L26_C17_001 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 479000.0 | 700000.0 | None | 101.0482 | None | green_too_late |
| R13L26_C17_002 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 186000.0 | 276500.0 | None | 60.4889 | None | green_too_late |
| R13L26_C17_003 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R13L26_C17_004 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R13L28_C17_001 | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 65800.0 | 124000.0 | None | 156.8415 | None | green_too_late |
| R13L28_C17_002 | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 79300.0 | None | None | 28.0003 | None | stage2_actionable_best_entry |
| R13L28_C17_003 | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R13L28_C17_004 | 011790 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
