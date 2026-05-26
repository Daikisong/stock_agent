# V12 Archetype Shadow Profile

이 보고서는 v12 shadow-only 후보입니다. 기본 scoring profile을 바꾸지 않습니다.

| scope | sector | archetype | axis | direction | confidence | positive | counterexample | ready | reason |
|---|---|---|---|---|---|---:|---:|---|---|
| canonical_archetype | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | stage2_bonus_candidate_delta | strengthen_conditional_stage2_actionable | low_medium | 2 | 2 | False | Stage2/Stage2-Actionable rows show positive asymmetry with limited high-MAE evidence. |
| canonical_archetype | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | local_4b_watch_guard | keep_price_only_4b_as_watch_only | low_medium | 2 | 2 | False | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| canonical_archetype | None | C22_INSURANCE_RATE_CYCLE_RESERVE | stage2_bonus_candidate_delta | strengthen_conditional_stage2_actionable | low_medium | 2 | 1 | False | Stage2/Stage2-Actionable rows show positive asymmetry with limited high-MAE evidence. |
| canonical_archetype | None | C22_INSURANCE_RATE_CYCLE_RESERVE | local_4b_watch_guard | keep_price_only_4b_as_watch_only | low_medium | 2 | 1 | False | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| canonical_archetype | None | C22_INSURANCE_RATE_CYCLE_RESERVE | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | low_medium | 2 | 1 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
