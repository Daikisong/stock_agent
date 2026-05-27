# C17_CHEMICAL_COMMODITY_MARGIN_SPREAD Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `19`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R13L26_C17_001 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 479000.0 | 700000.0 | None | 101.0482 | None | green_too_late |
| R13L26_C17_002 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 186000.0 | 276500.0 | None | 60.4889 | None | green_too_late |
| R13L26_C17_003 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R13L26_C17_004 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R13L28_C17_001 | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 65800.0 | 124000.0 | None | 156.8415 | None | green_too_late |
| R13L28_C17_002 | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 79300.0 | None | None | 28.0003 | None | stage2_actionable_best_entry |
| R13L28_C17_003 | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R13L28_C17_004 | 011790 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R4L11-C17-011170-20240124 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 128700.0 | None | None | 9.4 | None | stage2_actionable_best_entry |
| R4L11-C17-011780-20240201 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 130400.0 | None | None | 28.07 | None | stage2_actionable_best_entry |
| R4L11-C17-298020-20240329 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 324500.0 | None | None | 29.8974 | None | stage2_actionable_best_entry |
| R4L18-C17-HYOTNC-2020-SPANDEX | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 155500.0 | None | None | 519.3062 | None | stage2_actionable_best_entry |
| R4L18-C17-HYOTNC-2020-SPANDEX | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 155500.0 | None | None | 519.3062 | None | stage2_actionable_best_entry |
| R4L18-C17-KKPC-2020-NBLATEX | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 82100.0 | None | None | 263.58 | None | stage2_actionable_best_entry |
| R4L18-C17-KKPC-2020-NBLATEX | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 82100.0 | None | None | 263.58 | None | stage2_actionable_best_entry |
| R4L18-C17-KPIC-2023-NCC-FAILED | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 162200.0 | None | None | 19.48 | None | stage2_captured_most_upside |
| R4L18-C17-KPIC-2023-NCC-FAILED | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 162200.0 | None | None | 19.48 | None | stage2_captured_most_upside |
| R4L18-C17-LOTTECHEM-2023-REOPEN-FAILED | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 175800.0 | None | None | 10.52 | None | stage2_captured_most_upside |
| R4L18-C17-LOTTECHEM-2023-REOPEN-FAILED | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 175800.0 | None | None | 10.52 | None | stage2_captured_most_upside |
