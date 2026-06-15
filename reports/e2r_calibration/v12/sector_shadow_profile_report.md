# V12 Sector Shadow Profile

이 보고서는 v12 rolling calibration 후보 장부입니다.
`run-v12-calibration`은 여기서 검증된 apply_next_patch를 기본 scoring profile에 반영합니다.
case_fixture나 과거 연구 재현 성공은 live discovery 증명이 아닙니다.

| scope | sector | archetype | axis | direction | confidence | positive | counterexample | ready | reason |
|---|---|---|---|---|---|---:|---:|---|---|
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 187 | 701 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 187 | 701 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 187 | 701 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 205 | 268 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | None | local_4b_watch_guard | keep_price_only_4b_as_watch_only | medium | 205 | 268 | False | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 205 | 268 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 209 | 298 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | local_4b_watch_guard | keep_price_only_4b_as_watch_only | medium | 209 | 298 | False | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 209 | 298 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 209 | 370 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | None | local_4b_watch_guard | keep_price_only_4b_as_watch_only | medium | 209 | 370 | False | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 209 | 370 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 87 | 159 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 87 | 159 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 87 | 159 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 110 | 121 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 110 | 121 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 110 | 121 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 86 | 91 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 86 | 91 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 86 | 91 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 91 | 122 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 91 | 122 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 91 | 122 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 107 | 191 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | local_4b_watch_guard | keep_price_only_4b_as_watch_only | medium | 107 | 191 | False | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 107 | 191 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 35 | 64 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | None | local_4b_watch_guard | keep_price_only_4b_as_watch_only | medium | 35 | 64 | False | Price-only or early 4B rows dominate, so full 4B must not be strengthened. |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | None | earlier_thesis_break_watch | tighten_4c_watch_before_hard_4c | medium | 35 | 64 | False | Some 4C rows were late; propose earlier watch logic, not automatic hard 4C. |
