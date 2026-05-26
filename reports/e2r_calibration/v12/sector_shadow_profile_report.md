# V12 Sector Shadow Profile

이 보고서는 v12 shadow-only 후보입니다. 기본 scoring profile을 바꾸지 않습니다.

| scope | sector | archetype | axis | direction | confidence | positive | counterexample | ready | reason |
|---|---|---|---|---|---|---:|---:|---|---|
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 8 | 10 | True | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 8 | 10 | True | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 8 | 10 | True | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | low_medium | 2 | 1 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | low_medium | 2 | 1 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 8 | 5 | True | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 8 | 5 | True | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 8 | 5 | True | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 7 | 3 | True | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 7 | 3 | True | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | None | stage2_bonus_candidate_delta | strengthen_conditional_stage2_actionable | low_medium | 2 | 2 | True | Stage2/Stage2-Actionable rows show positive asymmetry with limited high-MAE evidence. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 17 | 12 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | local_4b_watch_guard | keep_price_only_4b_as_watch_only | medium | 17 | 12 | False | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 17 | 12 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 12 | 10 | True | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 12 | 10 | True | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 12 | 10 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 12 | 10 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 12 | 10 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 20 | 21 | True | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | local_4b_watch_guard | keep_price_only_4b_as_watch_only | medium | 20 | 21 | True | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 20 | 21 | True | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | None | stage2_bonus_candidate_delta | strengthen_conditional_stage2_actionable | low_medium | 2 | 2 | True | Stage2/Stage2-Actionable rows show positive asymmetry with limited high-MAE evidence. |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | low_medium | 2 | 2 | True | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
