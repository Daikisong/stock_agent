# V12 Sector Shadow Profile

이 보고서는 v12 rolling calibration 후보 장부입니다.
`run-v12-calibration`은 여기서 검증된 apply_next_patch를 기본 scoring profile에 반영합니다.
case_fixture나 과거 연구 재현 성공은 live discovery 증명이 아닙니다.

| scope | sector | archetype | axis | direction | confidence | positive | counterexample | ready | reason |
|---|---|---|---|---|---|---:|---:|---|---|
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 15 | 207 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 15 | 207 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 15 | 207 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 18 | 55 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 18 | 55 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 18 | 55 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 12 | 38 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 12 | 38 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 12 | 38 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 26 | 88 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 26 | 88 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 26 | 88 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 10 | 40 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 10 | 40 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 10 | 40 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 14 | 40 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 14 | 40 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 14 | 40 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 9 | 45 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 9 | 45 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 9 | 45 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 13 | 43 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 13 | 43 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L7_BIO_HEALTHCARE_MEDICAL | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 13 | 43 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 13 | 41 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 13 | 41 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 13 | 41 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | None | stage2_required_bridge | tighten_stage2_bridge_or_high_mae_guard | medium | 11 | 43 | False | Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge. |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | None | full_4b_overlay_candidate | strengthen_non_price_4b_overlay | medium | 11 | 43 | False | Non-price 4B rows show useful peak-capture timing in this scope. |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | None | hard_4c_confirmation | retain_hard_4c_when_non_price_break_exists | medium | 11 | 43 | False | Hard 4C rows are supported by thesis-break evidence in this scope. |
