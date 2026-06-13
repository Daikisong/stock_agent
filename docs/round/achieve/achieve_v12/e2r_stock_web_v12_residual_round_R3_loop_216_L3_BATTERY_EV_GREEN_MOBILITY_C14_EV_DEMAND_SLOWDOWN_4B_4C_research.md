# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
completed_round = R3
completed_loop = 216
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing; original Index Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5
production_scoring_changed = false
shadow_weight_only = true
output_file = e2r_stock_web_v12_residual_round_R3_loop_216_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
```

## 1. Current Calibrated Profile Assumption

Current calibrated profile proxy is `e2r_2_1_stock_web_calibrated` with the known applied axes: `stage2_actionable_evidence_bonus`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`. This MD does not alter production scoring. It tests a narrower C14 residual: **battery proxy/theme vocabulary and EV-demand slowdown headlines should not open Stage2-Actionable unless issuer-level call-off, utilization, revenue timing, margin, or customer offset evidence is present.**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R3 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C |
| fine_archetype_id | C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5 |
| objective | coverage_gap_fill, counterexample_mining, 4B/4C timing audit, canonical rule discovery |

C14 is not simply “battery stocks fell.” It is the moment when the EV chain’s demand tape, utilization, call-off, price/cost spread, or issuer-level conversion bridge stops supporting the prior rerating. A theme-only proxy is a paper lantern: it glows when the crowd shines on it, but it has no battery of its own.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index baseline still lists C14 as Priority 0 with 11 representative rows in the original ledger. In this session, prior C14 passes already covered POSCO퓨처엠, 천보, WCP, 솔루스첨단소재, 엘앤에프, SKC, 롯데에너지머티리얼즈, 코스모신소재, SK이노베이션, 나노신소재, 에코프로, 엔켐, 동화기업, 삼아알미늄, LG에너지솔루션, 삼성SDI, SK아이이테크놀로지, 에코프로머티리얼즈, 에코프로비엠. This loop deliberately avoids those names and uses a **battery proxy / LFP plan / lithium material / pouch film / delayed component visibility** leaf.

| duplicate rule | status |
|---|---|
| same canonical + symbol + trigger_type + entry_date hard duplicate | avoided |
| same symbol reused inside loop | only 자이글, with different trigger dates and evidence families |
| same evidence family as previous C14 loops | avoided |
| compact filename | not used |

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| source | Songdaiki/stock-web |
| source_name | FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| MFE/MAE rule | entry close `c`; forward 30/90/180 trading rows max high / min low |

## 5. Historical Eligibility Gate

|symbol|company|profile_path|price_shards|corporate_action_window_status|
|---|---|---|---|---|
|001570|금양|atlas/symbol_profiles/001/001570.json|atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv / atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv|no selected trigger was blocked in this MD; raw/unadjusted caveat remains for batch verifier|
|005420|코스모화학|atlas/symbol_profiles/005/005420.json|atlas/ohlcv_tradable_by_symbol_year/005/005420/2023.csv / atlas/ohlcv_tradable_by_symbol_year/005/005420/2024.csv|no selected trigger was blocked in this MD; raw/unadjusted caveat remains for batch verifier|
|008730|율촌화학|atlas/symbol_profiles/008/008730.json|atlas/ohlcv_tradable_by_symbol_year/008/008730/2024.csv / atlas/ohlcv_tradable_by_symbol_year/008/008730/2025.csv|no selected trigger was blocked in this MD; raw/unadjusted caveat remains for batch verifier|
|089980|상아프론테크|atlas/symbol_profiles/089/089980.json|atlas/ohlcv_tradable_by_symbol_year/089/089980/2024.csv / atlas/ohlcv_tradable_by_symbol_year/089/089980/2025.csv|no selected trigger was blocked in this MD; raw/unadjusted caveat remains for batch verifier|
|093370|후성|atlas/symbol_profiles/093/093370.json|atlas/ohlcv_tradable_by_symbol_year/093/093370/2023.csv / atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv|no selected trigger was blocked in this MD; raw/unadjusted caveat remains for batch verifier|
|131400|이브이첨단소재|atlas/symbol_profiles/131/131400.json|atlas/ohlcv_tradable_by_symbol_year/131/131400/2023.csv / atlas/ohlcv_tradable_by_symbol_year/131/131400/2024.csv|no selected trigger was blocked in this MD; raw/unadjusted caveat remains for batch verifier|
|234920|자이글|atlas/symbol_profiles/234/234920.json|atlas/ohlcv_tradable_by_symbol_year/234/234920/2023.csv / atlas/ohlcv_tradable_by_symbol_year/234/234920/2024.csv|no selected trigger was blocked in this MD; raw/unadjusted caveat remains for batch verifier|
|290670|대보마그네틱|atlas/symbol_profiles/290/290670.json|atlas/ohlcv_tradable_by_symbol_year/290/290670/2023.csv / atlas/ohlcv_tradable_by_symbol_year/290/290670/2024.csv / atlas/ohlcv_tradable_by_symbol_year/290/290670/2025.csv|no selected trigger was blocked in this MD; raw/unadjusted caveat remains for batch verifier|


All selected trigger rows have at least 180 forward trading rows inside the stock-web manifest max date. This MD uses tradable shards only. Raw/unadjusted corporate-action caveat remains and should be rechecked in the batch verifier.

## 6. Canonical Archetype Compression Map

| fine leaf | canonical route | rule implication |
|---|---|---|
| battery_proxy_theme_blowoff | C14 | stage2_watch_or_4b; no positive promotion without issuer money-road |
| LFP_plan_funding_gap | C14 | demand/call-off visibility required before Stage2-Actionable |
| lithium_material_halt | C14 | hard 4C allowed only when utilization/supply economics actually break |
| pouch_film_visibility_gap | C14 | high-MFE/high-MAE rows need staged-entry and exit guard |
| delayed_component_conversion | C14 | 2025+ visibility is not 2024 actionable without revenue timing bridge |

## 7. Case Selection Summary

|case_id|symbol|company|trigger_date|trigger_type|case_label|MFE90|MAE90|MFE180|MAE180|verdict|
|---|---|---|---:|---|---|---:|---:|---:|---:|---|
|C14_L216_001570_KUMYANG_BATTERY_THEME_PEAK|001570|금양|2023-07-26|Stage4B-Watch|risk_signal_success_theme_blowoff|27.46|-45.47|27.46|-52.5|current_profile_false_positive_if_battery_theme_peak_promoted_to_stage2_actionable|
|C14_L216_234920_ZAIGLE_LFP_FINANCING_GAP|234920|자이글|2023-05-11|Stage2-FalsePositive|counterexample_stage2_theme_with_future_mfe_but_no_money_road|67.42|-13.23|67.42|-60.65|stage2_should_require_capex_funding_customer_calloff_or_revenue_bridge|
|C14_L216_234920_ZAICELL_US_LFP_JV|234920|자이글|2023-08-07|Stage4B-Watch|counterexample_high_mfe_then_collapse|45.23|-58.34|45.23|-62.46|hard_4c_too_early_but_stage2_actionable_also_too_loose|
|C14_L216_131400_EV_ADVANCED_MATERIAL_THEME_HALT|131400|이브이첨단소재|2023-04-19|Stage4B-Watch|risk_signal_success_price_only_blowoff|52.49|-64.24|52.49|-73.97|price_only_blowoff_should_block_positive_stage|
|C14_L216_093370_FOOSUNG_LIPF6_HALT|093370|후성|2023-04-18|Stage4C|risk_signal_success_actual_supply_utilization_break|3.89|-26.27|3.89|-35.99|hard_4c_thesis_break_routes_to_4c_worked|
|C14_L216_005420_COSMO_RECYCLING_INDEX_SPIKE|005420|코스모화학|2023-04-03|Stage4B-Watch|counterexample_high_mfe_event_cap_not_hard4c|45.99|-30.48|45.99|-52.24|local_4b_exit_guard_better_than_hard_4c|
|C14_L216_290670_DAEBO_MAGNETIC_TAKEOVER_PEAK|290670|대보마그네틱|2023-04-19|Stage4B-Watch|risk_signal_success_ownership_and_battery_theme_blowoff|6.58|-47.81|6.58|-67.23|stage2_actionable_should_not_fire_on_takeover_premium_after_battery_blowoff|
|C14_L216_008730_YULCHON_POUCH_FILM_VISIBILITY_GAP|008730|율촌화학|2024-05-29|Stage2-Watch|counterexample_early_mfe_then_deep_mae_visibility_gap|25.22|-40.76|25.22|-43.4|stage2_watch_with_exit_guard_not_clean_actionable|
|C14_L216_089980_SANG_A_BATTERY_CAP_DELAYED|089980|상아프론테크|2024-07-08|Stage2-Watch|risk_signal_success_delayed_battery_visibility|3.66|-34.41|3.66|-47.32|watch_only_until_customer_calloff_or_revenue_timing_confirmed|


## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| new_independent_case_count | 9 |
| reused_case_count | 0 |
| new_symbol_count | 8 |
| usable_trigger_row_count | 9 |
| representative_trigger_count | 9 |
| positive_case_count | 5 |
| counterexample_count | 4 |
| high_MAE_90_count <= -20% | 8 |
| current_profile_error_count | 4 |

Here, “positive” means the C14/4B/4C guard would have protected the system from a bad Stage2 promotion, not that the stock was a long-side winner. C14 is a brake-system archetype: success often means preventing the engine from accelerating into a wall.

## 9. Evidence Source Map

|symbol|company|trigger_date|evidence_family|evidence_summary|evidence_url|
|---|---|---:|---|---|---|
|001570|금양|2023-07-26|battery_material_theme_peak_and_SMLab_investment|투자경고 속 시총 10조와 52주 신고가가 나온 2차전지 테마 고점권. SM Lab 투자 narrative는 있었지만 listed issuer money-road가 가격보다 늦었다.|https://www.yeongnam.com/web/view.php?key=20230726001019031|
|234920|자이글|2023-05-11|LFP_business_plan_vs_losses_and_funding_gap|LFP 배터리 진출 포부와 주가 200% 폭등이 있었지만, 2년 연속 적자와 투자 여력 부족이 같이 확인된 케이스.|https://marketin.edaily.co.kr/News/Read?newsId=03545686635607936|
|234920|자이글|2023-08-07|ZAICELL_JV_US_LFP_plan_but_funding_execution_uncertain|자이셀 지분 취득과 미국 LFP 공장 계획이 재점화됐지만 funding/call-off/revenue bridge는 약했다. 이후 큰 MFE가 있었으나 drawdown도 매우 깊다.|https://www.thebigdata.co.kr/view.php?ud=202308070634164211cd1e7f0bdf_23|
|131400|이브이첨단소재|2023-04-19|secondary_battery_lithium_theme_and_investment_warning|2차전지 테마 열풍 속 투자주의·경고·위험종목 지정과 거래정지 가능성이 동반된 가격-only blowoff.|https://www.etnews.com/20230419000027|
|093370|후성|2023-04-18|LiPF6_production_halt_and_battery_material_downcycle|울산 LiPF6 생산중단은 전해질 소재 수요/가격/가동률 축이 실제로 꺾인 hard C14 샘플.|https://dealsite.co.kr/articles/102284/025116|
|005420|코스모화학|2023-04-03|recycling_related_theme_and_index_inclusion_expectation|폐배터리 관련주와 코스피200 편입 가능성이 가격을 밀어올린 이벤트성 4B. 단기 MFE가 커서 즉시 hard 4C는 과했다.|https://www.g-enews.com/article/Securities/2023/04/20230403104218991590369a393b_1|
|290670|대보마그네틱|2023-04-19|EMF_battery_equipment_takeover_price_gap_after_theme_rally|2차전지 급등 후 경영권 매각가격 갭이 생기며 매각 일정이 중단된 고점권 4B. 이후 가격경로가 C14/4B guard를 지지했다.|https://www.mk.co.kr/news/stock/10716698|
|008730|율촌화학|2024-05-29|pouch_film_investment_but_visible_revenue_gap|파우치필름 기대와 투자가 있었지만 전자소재 매출 감소와 가시성 논란이 남은 케이스. 30D MFE는 있었지만 90/180D MAE가 깊다.|https://www.ibtomato.com/ExternalView.aspx?no=12290&type=1|
|089980|상아프론테크|2024-07-08|2025_plus_battery_component_expectation_without_near_term_conversion|2차전지 부품/모듈 성과는 2025년 하반기 이후 기대라는 지연 구조였다. trigger 시점의 near-term call-off/margin bridge가 약했고 가격경로도 낮은 MFE와 깊은 MAE를 보였다.|https://w4.kirs.or.kr/download/research/240708_%EC%83%81%EC%95%84%ED%94%84%EB%A1%A0%ED%85%8C%ED%81%AC.pdf|


## 10. Price Data Source Map

| symbol | shard pattern |
|---|---|
| 001570 | atlas/ohlcv_tradable_by_symbol_year/001/001570/YYYY.csv |
| 005420 | atlas/ohlcv_tradable_by_symbol_year/005/005420/YYYY.csv |
| 008730 | atlas/ohlcv_tradable_by_symbol_year/008/008730/YYYY.csv |
| 089980 | atlas/ohlcv_tradable_by_symbol_year/089/089980/YYYY.csv |
| 093370 | atlas/ohlcv_tradable_by_symbol_year/093/093370/YYYY.csv |
| 131400 | atlas/ohlcv_tradable_by_symbol_year/131/131400/YYYY.csv |
| 234920 | atlas/ohlcv_tradable_by_symbol_year/234/234920/YYYY.csv |
| 290670 | atlas/ohlcv_tradable_by_symbol_year/290/290670/YYYY.csv |


## 11. Case-by-Case Trigger Grid

|case_id|symbol|company|trigger_date|trigger_type|case_label|MFE90|MAE90|MFE180|MAE180|verdict|
|---|---|---|---:|---|---|---:|---:|---:|---:|---|
|C14_L216_001570_KUMYANG_BATTERY_THEME_PEAK|001570|금양|2023-07-26|Stage4B-Watch|risk_signal_success_theme_blowoff|27.46|-45.47|27.46|-52.5|current_profile_false_positive_if_battery_theme_peak_promoted_to_stage2_actionable|
|C14_L216_234920_ZAIGLE_LFP_FINANCING_GAP|234920|자이글|2023-05-11|Stage2-FalsePositive|counterexample_stage2_theme_with_future_mfe_but_no_money_road|67.42|-13.23|67.42|-60.65|stage2_should_require_capex_funding_customer_calloff_or_revenue_bridge|
|C14_L216_234920_ZAICELL_US_LFP_JV|234920|자이글|2023-08-07|Stage4B-Watch|counterexample_high_mfe_then_collapse|45.23|-58.34|45.23|-62.46|hard_4c_too_early_but_stage2_actionable_also_too_loose|
|C14_L216_131400_EV_ADVANCED_MATERIAL_THEME_HALT|131400|이브이첨단소재|2023-04-19|Stage4B-Watch|risk_signal_success_price_only_blowoff|52.49|-64.24|52.49|-73.97|price_only_blowoff_should_block_positive_stage|
|C14_L216_093370_FOOSUNG_LIPF6_HALT|093370|후성|2023-04-18|Stage4C|risk_signal_success_actual_supply_utilization_break|3.89|-26.27|3.89|-35.99|hard_4c_thesis_break_routes_to_4c_worked|
|C14_L216_005420_COSMO_RECYCLING_INDEX_SPIKE|005420|코스모화학|2023-04-03|Stage4B-Watch|counterexample_high_mfe_event_cap_not_hard4c|45.99|-30.48|45.99|-52.24|local_4b_exit_guard_better_than_hard_4c|
|C14_L216_290670_DAEBO_MAGNETIC_TAKEOVER_PEAK|290670|대보마그네틱|2023-04-19|Stage4B-Watch|risk_signal_success_ownership_and_battery_theme_blowoff|6.58|-47.81|6.58|-67.23|stage2_actionable_should_not_fire_on_takeover_premium_after_battery_blowoff|
|C14_L216_008730_YULCHON_POUCH_FILM_VISIBILITY_GAP|008730|율촌화학|2024-05-29|Stage2-Watch|counterexample_early_mfe_then_deep_mae_visibility_gap|25.22|-40.76|25.22|-43.4|stage2_watch_with_exit_guard_not_clean_actionable|
|C14_L216_089980_SANG_A_BATTERY_CAP_DELAYED|089980|상아프론테크|2024-07-08|Stage2-Watch|risk_signal_success_delayed_battery_visibility|3.66|-34.41|3.66|-47.32|watch_only_until_customer_calloff_or_revenue_timing_confirmed|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|symbol|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|drawdown_after_peak|
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|T_C14_L216_001570_20230726_THEME_PEAK|001570|2023-07-26|152200|27.46|-30.75|27.46|-45.47|27.46|-52.5|2023-07-26|-62.73|
|T_C14_L216_234920_20230511_LFP_FINANCING_GAP|234920|2023-05-11|15500|67.42|-9.42|67.42|-13.23|67.42|-60.65|2023-05-22|-76.49|
|T_C14_L216_234920_20230807_ZAICELL_JV|234920|2023-08-07|16250|45.23|-12.37|45.23|-58.34|45.23|-62.46|2023-09-07|-74.15|
|T_C14_L216_131400_20230419_THEME_HALT|131400|2023-04-19|11660|52.49|-56.86|52.49|-64.24|52.49|-73.97|2023-04-19|-82.93|
|T_C14_L216_093370_20230418_LIPF6_HALT|093370|2023-04-18|14920|3.89|-15.95|3.89|-26.27|3.89|-35.99|2023-04-18|-38.39|
|T_C14_L216_005420_20230403_RECYCLING_SPIKE|005420|2023-04-03|64800|45.99|-25.08|45.99|-30.48|45.99|-52.24|2023-04-10|-67.28|
|T_C14_L216_290670_20230419_TAKEOVER_PEAK|290670|2023-04-19|77500|6.58|-31.61|6.58|-47.81|6.58|-67.23|2023-04-19|-69.25|
|T_C14_L216_008730_20240529_POUCH_FILM_GAP|008730|2024-05-29|34100|25.22|-7.48|25.22|-40.76|25.22|-43.4|2024-06-13|-54.8|
|T_C14_L216_089980_20240708_BATTERY_CAP_DELAYED|089980|2024-07-08|25950|3.66|-30.64|3.66|-34.41|3.66|-47.32|2024-07-11|-49.18|


## 13. Current Calibrated Profile Stress Test

The current profile already blocks many price-only 4B rows, but C14 still has a residual boundary problem: some rows have enough “battery words” to look like Stage2, while the actual issuer-level bridge is missing. The candidate profile pushes those rows into watch/4B unless a second bridge exists.

|profile|hypothesis|eligible_rows|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|verdict|
|---|---|---:|---:|---:|---:|---:|---:|---|
|P0|e2r_2_1_stock_web_calibrated_proxy_all_rows|9|30.88|-40.11|30.88|-55.08|0.44|baseline allows residual proxy/theme errors|
|P1|C14_watch_only_if_proxy_or_calloff_gap|8|26.32|-43.47|26.32|-54.39|0.38|guard improves bridge discipline|
|P2|C14_4B_exit_guard_for_theme_blowoff_and_high_MFE_high_MAE|8|28.18|-37.1|28.18|-52.72|0.5|guard improves bridge discipline|
|P3|counterexample_guard_profile_no_actionable_without_calloff_margin_bridge|5|18.82|-43.64|18.82|-55.4|0.0|guard improves bridge discipline|


## 14. Stage2 / Yellow / Green Comparison

| rule | baseline behavior | proposed C14 behavior |
|---|---|---|
| Stage2-Watch | can still be opened by battery/LFP/lithium vocabulary | allowed, but marked watch-only when call-off/utilization bridge is absent |
| Stage2-Actionable | too loose for funding-gap or proxy-theme rows | requires issuer-level customer/call-off/utilization/revenue/margin bridge |
| Stage3-Yellow | not supported in this MD | no Yellow promotion from proxy/theme rows |
| Stage3-Green | forbidden by price-only blowoff axis | still forbidden; C14 does not loosen Green |
| Stage4B | late peak/theme row protection | strengthened with high-MFE/high-MAE exit logic |
| Stage4C | direct utilization/supply/economics break | requires direct break or second non-price confirmation; not vocabulary-only |

## 15. 4B Local vs Full-window Timing Audit

- 금양, 이브이첨단소재, 코스모화학, 대보마그네틱 all show event/peak-like behavior where the local peak was very near the trigger.
- 자이글 and 율촌화학 show high-MFE/high-MAE geometry. These are not clean positives; they need 4B exit guard and staged entry.
- 후성 and 상아프론테크 show low-MFE/deep-MAE geometry, supporting a stricter C14 watch/protection route.

## 16. 4C Protection Audit

Hard 4C is supported for direct supply/utilization/economics breaks such as 후성 LiPF6 production halt. Hard 4C is not supported for 코스모화학 or 율촌화학-style rows where early MFE opened before the collapse; those are better modeled as 4B exit / false-hard-4C audit.

## 17. Sector-Specific Rule Candidate

`L3_EV_DEMAND_SLOWDOWN_PROXY_AND_CALLOFF_GATE_V5`

L3 battery/EV rows should split support evidence into two wires:

1. **Theme/support wire:** battery, lithium, LFP, pouch film, recycling, component exposure.
2. **Conversion wire:** customer call-off, utilization, revenue timing, margin/revision, inventory normalization, direct production halt.

Only the second wire can carry Stage2-Actionable current. The first wire can only light Stage2-Watch unless price geometry and evidence both remain clean.

## 18. Canonical-Archetype Rule Candidate

`C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5`

```text
if C14 row has battery/lithium/LFP/recycling/component vocabulary
and lacks issuer-level calloff/utilization/revenue/margin bridge:
    cap at Stage2-Watch
    if MAE90 <= -20 or event peak proximity is high:
        route to Local4B-Watch

if direct production halt / utilization break / demand cut / customer calloff is confirmed:
    allow Stage4C or Stage4C-Watch

if MFE30 or MFE90 >= 25 and MAE90 <= -30:
    do not mark clean positive
    use staged-entry + 4B exit guard

if hard-4C-looking headline appears after valuation reset and MFE180 reopens:
    use false-hard-4C audit instead of irreversible 4C
```

## 19. Before / After Backtest Comparison

|profile|hypothesis|eligible_rows|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|verdict|
|---|---|---:|---:|---:|---:|---:|---:|---|
|P0|e2r_2_1_stock_web_calibrated_proxy_all_rows|9|30.88|-40.11|30.88|-55.08|0.44|baseline allows residual proxy/theme errors|
|P1|C14_watch_only_if_proxy_or_calloff_gap|8|26.32|-43.47|26.32|-54.39|0.38|guard improves bridge discipline|
|P2|C14_4B_exit_guard_for_theme_blowoff_and_high_MFE_high_MAE|8|28.18|-37.1|28.18|-52.72|0.5|guard improves bridge discipline|
|P3|counterexample_guard_profile_no_actionable_without_calloff_margin_bridge|5|18.82|-43.64|18.82|-55.4|0.0|guard improves bridge discipline|


## 20. Score-Return Alignment Matrix

| alignment type | rows | interpretation |
|---|---:|---|
| low MFE + deep MAE | 3 | C14 protection worked or should be strengthened |
| high MFE + deep MAE | 5 | stage geometry problem; use 4B exit/staged entry |
| theme/proxy vocabulary gap | 7 | block Stage2-Actionable unless money-road appears |
| direct utilization/supply break | 1 | supports C14/4C-watch path |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5 | 5 | 4 | 7 | 1 | 9 | 0 | 9 | 9 | 4 | L3_EV_DEMAND_SLOWDOWN_PROXY_AND_CALLOFF_GATE_V5 | C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5 | original index 11 -> 20 if accepted; session-aware C14 already beyond 30, this is quality-repair |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 9
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 9
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: battery_proxy_theme_false_positive|high_mfe_high_mae_event_cap|hard_4c_too_early_without_second_confirmation|actual_utilization_break_protection
new_axis_proposed: c14_battery_proxy_blowoff_demand_slowdown_and_false_4c_gate_v5
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_on_proxy_or_reset_rows_without_second_confirmation
existing_axis_kept: stage3_green_thresholds_unchanged
sector_specific_rule_candidate: L3_EV_DEMAND_SLOWDOWN_PROXY_AND_CALLOFF_GATE_V5
canonical_archetype_rule_candidate: C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Stock-web actual daily OHLC rows for every trigger.
- Entry close, 30/90/180 trading-row MFE/MAE.
- Trigger evidence timing before or on entry date.
- Duplicate avoidance at canonical/symbol/trigger_type/entry_date level.

Not validated here:
- Production scoring patch.
- Live/current candidate list.
- Broker/API or trading execution.
- Adjusted-price reconstruction.
- Full corporate-action audit beyond selected raw/unadjusted calibration caveat; batch verifier must re-check profile metadata.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_proxy_theme_money_road_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"require issuer-level calloff/utilization/margin bridge before Stage2-Actionable in C14", "reduces proxy/theme false positives while preserving actual utilization breaks", "T_C14_L216_001570_20230726_THEME_PEAK|T_C14_L216_131400_20230419_THEME_HALT|T_C14_L216_093370_20230418_LIPF6_HALT",9,9,3,medium,canonical_shadow_only,"not production; batch calibration only"
shadow_weight,c14_false_hard4c_reset_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"do not hard-4C rows with high early MFE or reset/rebound unless second non-price break appears", "routes high-MFE/high-MAE to 4B exit guard instead of hard block", "T_C14_L216_005420_20230403_RECYCLING_SPIKE|T_C14_L216_008730_20240529_POUCH_FILM_GAP",9,9,3,medium,canonical_shadow_only,"not production; batch calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C14_L216_001570_KUMYANG_BATTERY_THEME_PEAK", "symbol": "001570", "company_name": "금양", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "risk_signal_success_theme_blowoff", "positive_or_counterexample": "positive", "best_trigger": "T_C14_L216_001570_20230726_THEME_PEAK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_false_positive_if_battery_theme_peak_promoted_to_stage2_actionable", "current_profile_verdict": "current_profile_false_positive_if_battery_theme_peak_promoted_to_stage2_actionable", "price_source": "Songdaiki/stock-web", "notes": "투자경고 속 시총 10조와 52주 신고가가 나온 2차전지 테마 고점권. SM Lab 투자 narrative는 있었지만 listed issuer money-road가 가격보다 늦었다."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_001570_20230726_THEME_PEAK", "case_id": "C14_L216_001570_KUMYANG_BATTERY_THEME_PEAK", "symbol": "001570", "company_name": "금양", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage4B-Watch", "trigger_date": "2023-07-26", "entry_date": "2023-07-26", "entry_price": 152200.0, "evidence_available_at_that_date": "투자경고 속 시총 10조와 52주 신고가가 나온 2차전지 테마 고점권. SM Lab 투자 narrative는 있었지만 listed issuer money-road가 가격보다 늦었다.", "evidence_source": "https://www.yeongnam.com/web/view.php?key=20230726001019031", "stage2_evidence_fields": ["battery_material_theme_peak_and_SMLab_investment"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_blowoff_or_event_cap", "high_MAE_or_bridge_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv|atlas/ohlcv_tradable_by_symbol_year/001/001570/2024.csv", "profile_path": "atlas/symbol_profiles/001/001570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.46, "MAE_30D_pct": -30.75, "MFE_90D_pct": 27.46, "MAE_90D_pct": -45.47, "MFE_180D_pct": 27.46, "MAE_180D_pct": -52.5, "peak_date": "2023-07-26", "peak_price": 194000.0, "drawdown_after_peak_pct": -62.73, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "risk_signal_success_theme_blowoff", "current_profile_verdict": "current_profile_false_positive_if_battery_theme_peak_promoted_to_stage2_actionable", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|001570|Stage4B-Watch|2023-07-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C14_L216_234920_ZAIGLE_LFP_FINANCING_GAP", "symbol": "234920", "company_name": "자이글", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "counterexample_stage2_theme_with_future_mfe_but_no_money_road", "positive_or_counterexample": "counterexample", "best_trigger": "T_C14_L216_234920_20230511_LFP_FINANCING_GAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_should_require_capex_funding_customer_calloff_or_revenue_bridge", "current_profile_verdict": "stage2_should_require_capex_funding_customer_calloff_or_revenue_bridge", "price_source": "Songdaiki/stock-web", "notes": "LFP 배터리 진출 포부와 주가 200% 폭등이 있었지만, 2년 연속 적자와 투자 여력 부족이 같이 확인된 케이스."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_234920_20230511_LFP_FINANCING_GAP", "case_id": "C14_L216_234920_ZAIGLE_LFP_FINANCING_GAP", "symbol": "234920", "company_name": "자이글", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2023-05-11", "entry_date": "2023-05-11", "entry_price": 15500.0, "evidence_available_at_that_date": "LFP 배터리 진출 포부와 주가 200% 폭등이 있었지만, 2년 연속 적자와 투자 여력 부족이 같이 확인된 케이스.", "evidence_source": "https://marketin.edaily.co.kr/News/Read?newsId=03545686635607936", "stage2_evidence_fields": ["LFP_business_plan_vs_losses_and_funding_gap"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/234/234920/2023.csv|atlas/ohlcv_tradable_by_symbol_year/234/234920/2024.csv", "profile_path": "atlas/symbol_profiles/234/234920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 67.42, "MAE_30D_pct": -9.42, "MFE_90D_pct": 67.42, "MAE_90D_pct": -13.23, "MFE_180D_pct": 67.42, "MAE_180D_pct": -60.65, "peak_date": "2023-05-22", "peak_price": 25950.0, "drawdown_after_peak_pct": -76.49, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "counterexample_stage2_theme_with_future_mfe_but_no_money_road", "current_profile_verdict": "stage2_should_require_capex_funding_customer_calloff_or_revenue_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|234920|Stage2-FalsePositive|2023-05-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C14_L216_234920_ZAICELL_US_LFP_JV", "symbol": "234920", "company_name": "자이글", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "counterexample_high_mfe_then_collapse", "positive_or_counterexample": "counterexample", "best_trigger": "T_C14_L216_234920_20230807_ZAICELL_JV", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_too_early_but_stage2_actionable_also_too_loose", "current_profile_verdict": "hard_4c_too_early_but_stage2_actionable_also_too_loose", "price_source": "Songdaiki/stock-web", "notes": "자이셀 지분 취득과 미국 LFP 공장 계획이 재점화됐지만 funding/call-off/revenue bridge는 약했다. 이후 큰 MFE가 있었으나 drawdown도 매우 깊다."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_234920_20230807_ZAICELL_JV", "case_id": "C14_L216_234920_ZAICELL_US_LFP_JV", "symbol": "234920", "company_name": "자이글", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage4B-Watch", "trigger_date": "2023-08-07", "entry_date": "2023-08-07", "entry_price": 16250.0, "evidence_available_at_that_date": "자이셀 지분 취득과 미국 LFP 공장 계획이 재점화됐지만 funding/call-off/revenue bridge는 약했다. 이후 큰 MFE가 있었으나 drawdown도 매우 깊다.", "evidence_source": "https://www.thebigdata.co.kr/view.php?ud=202308070634164211cd1e7f0bdf_23", "stage2_evidence_fields": ["ZAICELL_JV_US_LFP_plan_but_funding_execution_uncertain"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_blowoff_or_event_cap", "high_MAE_or_bridge_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/234/234920/2023.csv|atlas/ohlcv_tradable_by_symbol_year/234/234920/2024.csv", "profile_path": "atlas/symbol_profiles/234/234920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 45.23, "MAE_30D_pct": -12.37, "MFE_90D_pct": 45.23, "MAE_90D_pct": -58.34, "MFE_180D_pct": 45.23, "MAE_180D_pct": -62.46, "peak_date": "2023-09-07", "peak_price": 23600.0, "drawdown_after_peak_pct": -74.15, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "counterexample_high_mfe_then_collapse", "current_profile_verdict": "hard_4c_too_early_but_stage2_actionable_also_too_loose", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|234920|Stage4B-Watch|2023-08-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C14_L216_131400_EV_ADVANCED_MATERIAL_THEME_HALT", "symbol": "131400", "company_name": "이브이첨단소재", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "risk_signal_success_price_only_blowoff", "positive_or_counterexample": "positive", "best_trigger": "T_C14_L216_131400_20230419_THEME_HALT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_blowoff_should_block_positive_stage", "current_profile_verdict": "price_only_blowoff_should_block_positive_stage", "price_source": "Songdaiki/stock-web", "notes": "2차전지 테마 열풍 속 투자주의·경고·위험종목 지정과 거래정지 가능성이 동반된 가격-only blowoff."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_131400_20230419_THEME_HALT", "case_id": "C14_L216_131400_EV_ADVANCED_MATERIAL_THEME_HALT", "symbol": "131400", "company_name": "이브이첨단소재", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage4B-Watch", "trigger_date": "2023-04-19", "entry_date": "2023-04-19", "entry_price": 11660.0, "evidence_available_at_that_date": "2차전지 테마 열풍 속 투자주의·경고·위험종목 지정과 거래정지 가능성이 동반된 가격-only blowoff.", "evidence_source": "https://www.etnews.com/20230419000027", "stage2_evidence_fields": ["secondary_battery_lithium_theme_and_investment_warning"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_blowoff_or_event_cap", "high_MAE_or_bridge_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/131/131400/2023.csv|atlas/ohlcv_tradable_by_symbol_year/131/131400/2024.csv", "profile_path": "atlas/symbol_profiles/131/131400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 52.49, "MAE_30D_pct": -56.86, "MFE_90D_pct": 52.49, "MAE_90D_pct": -64.24, "MFE_180D_pct": 52.49, "MAE_180D_pct": -73.97, "peak_date": "2023-04-19", "peak_price": 17780.0, "drawdown_after_peak_pct": -82.93, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "risk_signal_success_price_only_blowoff", "current_profile_verdict": "price_only_blowoff_should_block_positive_stage", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|131400|Stage4B-Watch|2023-04-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C14_L216_093370_FOOSUNG_LIPF6_HALT", "symbol": "093370", "company_name": "후성", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "risk_signal_success_actual_supply_utilization_break", "positive_or_counterexample": "positive", "best_trigger": "T_C14_L216_093370_20230418_LIPF6_HALT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_thesis_break_routes_to_4c_worked", "current_profile_verdict": "hard_4c_thesis_break_routes_to_4c_worked", "price_source": "Songdaiki/stock-web", "notes": "울산 LiPF6 생산중단은 전해질 소재 수요/가격/가동률 축이 실제로 꺾인 hard C14 샘플."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_093370_20230418_LIPF6_HALT", "case_id": "C14_L216_093370_FOOSUNG_LIPF6_HALT", "symbol": "093370", "company_name": "후성", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage4C", "trigger_date": "2023-04-18", "entry_date": "2023-04-18", "entry_price": 14920.0, "evidence_available_at_that_date": "울산 LiPF6 생산중단은 전해질 소재 수요/가격/가동률 축이 실제로 꺾인 hard C14 샘플.", "evidence_source": "https://dealsite.co.kr/articles/102284/025116", "stage2_evidence_fields": ["LiPF6_production_halt_and_battery_material_downcycle"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["actual_supply_utilization_or_thesis_break"], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/093/093370/2023.csv|atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv", "profile_path": "atlas/symbol_profiles/093/093370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.89, "MAE_30D_pct": -15.95, "MFE_90D_pct": 3.89, "MAE_90D_pct": -26.27, "MFE_180D_pct": 3.89, "MAE_180D_pct": -35.99, "peak_date": "2023-04-18", "peak_price": 15500.0, "drawdown_after_peak_pct": -38.39, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "risk_signal_success_actual_supply_utilization_break", "current_profile_verdict": "hard_4c_thesis_break_routes_to_4c_worked", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|093370|Stage4C|2023-04-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C14_L216_005420_COSMO_RECYCLING_INDEX_SPIKE", "symbol": "005420", "company_name": "코스모화학", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "counterexample_high_mfe_event_cap_not_hard4c", "positive_or_counterexample": "counterexample", "best_trigger": "T_C14_L216_005420_20230403_RECYCLING_SPIKE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "local_4b_exit_guard_better_than_hard_4c", "current_profile_verdict": "local_4b_exit_guard_better_than_hard_4c", "price_source": "Songdaiki/stock-web", "notes": "폐배터리 관련주와 코스피200 편입 가능성이 가격을 밀어올린 이벤트성 4B. 단기 MFE가 커서 즉시 hard 4C는 과했다."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_005420_20230403_RECYCLING_SPIKE", "case_id": "C14_L216_005420_COSMO_RECYCLING_INDEX_SPIKE", "symbol": "005420", "company_name": "코스모화학", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage4B-Watch", "trigger_date": "2023-04-03", "entry_date": "2023-04-03", "entry_price": 64800.0, "evidence_available_at_that_date": "폐배터리 관련주와 코스피200 편입 가능성이 가격을 밀어올린 이벤트성 4B. 단기 MFE가 커서 즉시 hard 4C는 과했다.", "evidence_source": "https://www.g-enews.com/article/Securities/2023/04/20230403104218991590369a393b_1", "stage2_evidence_fields": ["recycling_related_theme_and_index_inclusion_expectation"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_blowoff_or_event_cap", "high_MAE_or_bridge_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005420/2023.csv|atlas/ohlcv_tradable_by_symbol_year/005/005420/2024.csv", "profile_path": "atlas/symbol_profiles/005/005420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 45.99, "MAE_30D_pct": -25.08, "MFE_90D_pct": 45.99, "MAE_90D_pct": -30.48, "MFE_180D_pct": 45.99, "MAE_180D_pct": -52.24, "peak_date": "2023-04-10", "peak_price": 94600.0, "drawdown_after_peak_pct": -67.28, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "counterexample_high_mfe_event_cap_not_hard4c", "current_profile_verdict": "local_4b_exit_guard_better_than_hard_4c", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|005420|Stage4B-Watch|2023-04-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C14_L216_290670_DAEBO_MAGNETIC_TAKEOVER_PEAK", "symbol": "290670", "company_name": "대보마그네틱", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "risk_signal_success_ownership_and_battery_theme_blowoff", "positive_or_counterexample": "positive", "best_trigger": "T_C14_L216_290670_20230419_TAKEOVER_PEAK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_actionable_should_not_fire_on_takeover_premium_after_battery_blowoff", "current_profile_verdict": "stage2_actionable_should_not_fire_on_takeover_premium_after_battery_blowoff", "price_source": "Songdaiki/stock-web", "notes": "2차전지 급등 후 경영권 매각가격 갭이 생기며 매각 일정이 중단된 고점권 4B. 이후 가격경로가 C14/4B guard를 지지했다."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_290670_20230419_TAKEOVER_PEAK", "case_id": "C14_L216_290670_DAEBO_MAGNETIC_TAKEOVER_PEAK", "symbol": "290670", "company_name": "대보마그네틱", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage4B-Watch", "trigger_date": "2023-04-19", "entry_date": "2023-04-19", "entry_price": 77500.0, "evidence_available_at_that_date": "2차전지 급등 후 경영권 매각가격 갭이 생기며 매각 일정이 중단된 고점권 4B. 이후 가격경로가 C14/4B guard를 지지했다.", "evidence_source": "https://www.mk.co.kr/news/stock/10716698", "stage2_evidence_fields": ["EMF_battery_equipment_takeover_price_gap_after_theme_rally"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_blowoff_or_event_cap", "high_MAE_or_bridge_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/290/290670/2023.csv|atlas/ohlcv_tradable_by_symbol_year/290/290670/2024.csv|atlas/ohlcv_tradable_by_symbol_year/290/290670/2025.csv", "profile_path": "atlas/symbol_profiles/290/290670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.58, "MAE_30D_pct": -31.61, "MFE_90D_pct": 6.58, "MAE_90D_pct": -47.81, "MFE_180D_pct": 6.58, "MAE_180D_pct": -67.23, "peak_date": "2023-04-19", "peak_price": 82600.0, "drawdown_after_peak_pct": -69.25, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "risk_signal_success_ownership_and_battery_theme_blowoff", "current_profile_verdict": "stage2_actionable_should_not_fire_on_takeover_premium_after_battery_blowoff", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|290670|Stage4B-Watch|2023-04-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C14_L216_008730_YULCHON_POUCH_FILM_VISIBILITY_GAP", "symbol": "008730", "company_name": "율촌화학", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "counterexample_early_mfe_then_deep_mae_visibility_gap", "positive_or_counterexample": "counterexample", "best_trigger": "T_C14_L216_008730_20240529_POUCH_FILM_GAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_watch_with_exit_guard_not_clean_actionable", "current_profile_verdict": "stage2_watch_with_exit_guard_not_clean_actionable", "price_source": "Songdaiki/stock-web", "notes": "파우치필름 기대와 투자가 있었지만 전자소재 매출 감소와 가시성 논란이 남은 케이스. 30D MFE는 있었지만 90/180D MAE가 깊다."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_008730_20240529_POUCH_FILM_GAP", "case_id": "C14_L216_008730_YULCHON_POUCH_FILM_VISIBILITY_GAP", "symbol": "008730", "company_name": "율촌화학", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage2-Watch", "trigger_date": "2024-05-29", "entry_date": "2024-05-29", "entry_price": 34100.0, "evidence_available_at_that_date": "파우치필름 기대와 투자가 있었지만 전자소재 매출 감소와 가시성 논란이 남은 케이스. 30D MFE는 있었지만 90/180D MAE가 깊다.", "evidence_source": "https://www.ibtomato.com/ExternalView.aspx?no=12290&type=1", "stage2_evidence_fields": ["pouch_film_investment_but_visible_revenue_gap"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_blowoff_or_event_cap", "high_MAE_or_bridge_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008730/2024.csv|atlas/ohlcv_tradable_by_symbol_year/008/008730/2025.csv", "profile_path": "atlas/symbol_profiles/008/008730.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.22, "MAE_30D_pct": -7.48, "MFE_90D_pct": 25.22, "MAE_90D_pct": -40.76, "MFE_180D_pct": 25.22, "MAE_180D_pct": -43.4, "peak_date": "2024-06-13", "peak_price": 42700.0, "drawdown_after_peak_pct": -54.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "counterexample_early_mfe_then_deep_mae_visibility_gap", "current_profile_verdict": "stage2_watch_with_exit_guard_not_clean_actionable", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|008730|Stage2-Watch|2024-05-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C14_L216_089980_SANG_A_BATTERY_CAP_DELAYED", "symbol": "089980", "company_name": "상아프론테크", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "case_type": "risk_signal_success_delayed_battery_visibility", "positive_or_counterexample": "positive", "best_trigger": "T_C14_L216_089980_20240708_BATTERY_CAP_DELAYED", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "watch_only_until_customer_calloff_or_revenue_timing_confirmed", "current_profile_verdict": "watch_only_until_customer_calloff_or_revenue_timing_confirmed", "price_source": "Songdaiki/stock-web", "notes": "2차전지 부품/모듈 성과는 2025년 하반기 이후 기대라는 지연 구조였다. trigger 시점의 near-term call-off/margin bridge가 약했고 가격경로도 낮은 MFE와 깊은 MAE를 보였다."}
{"row_type": "trigger", "trigger_id": "T_C14_L216_089980_20240708_BATTERY_CAP_DELAYED", "case_id": "C14_L216_089980_SANG_A_BATTERY_CAP_DELAYED", "symbol": "089980", "company_name": "상아프론테크", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "C14_BATTERY_PROXY_BLOWOFF_DEMAND_SLOWDOWN_AND_FALSE_4C_GATE_V5", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery", "trigger_type": "Stage2-Watch", "trigger_date": "2024-07-08", "entry_date": "2024-07-08", "entry_price": 25950.0, "evidence_available_at_that_date": "2차전지 부품/모듈 성과는 2025년 하반기 이후 기대라는 지연 구조였다. trigger 시점의 near-term call-off/margin bridge가 약했고 가격경로도 낮은 MFE와 깊은 MAE를 보였다.", "evidence_source": "https://w4.kirs.or.kr/download/research/240708_%EC%83%81%EC%95%84%ED%94%84%EB%A1%A0%ED%85%8C%ED%81%AC.pdf", "stage2_evidence_fields": ["2025_plus_battery_component_expectation_without_near_term_conversion"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_blowoff_or_event_cap", "high_MAE_or_bridge_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089980/2024.csv|atlas/ohlcv_tradable_by_symbol_year/089/089980/2025.csv", "profile_path": "atlas/symbol_profiles/089/089980.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.66, "MAE_30D_pct": -30.64, "MFE_90D_pct": 3.66, "MAE_90D_pct": -34.41, "MFE_180D_pct": 3.66, "MAE_180D_pct": -47.32, "peak_date": "2024-07-11", "peak_price": 26900.0, "drawdown_after_peak_pct": -49.18, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "risk_signal_success_delayed_battery_visibility", "current_profile_verdict": "watch_only_until_customer_calloff_or_revenue_timing_confirmed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_this_md_batch_verify_profile", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|089980|Stage2-Watch|2024-07-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14_L216_001570_KUMYANG_BATTERY_THEME_PEAK", "trigger_id": "T_C14_L216_001570_20230726_THEME_PEAK", "symbol": "001570", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"ev_demand_slowdown_score": 50, "calloff_or_utilization_break_score": 25, "proxy_theme_risk_score": 45, "margin_bridge_score": 20, "source_quality_score": 55, "positioning_overheat_score": 70}, "weighted_score_before": 72, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"ev_demand_slowdown_score": 60, "calloff_or_utilization_break_score": 35, "proxy_theme_risk_score": 80, "margin_bridge_score": 25, "source_quality_score": 65, "positioning_overheat_score": 85}, "weighted_score_after": 66, "stage_label_after": "Stage4B-Watch", "changed_components": ["proxy_theme_risk_score", "calloff_or_utilization_break_score", "positioning_overheat_score"], "component_delta_explanation": "C14 candidate guard separates direct utilization/call-off break from proxy/theme vocabulary and applies 4B exit guard to high-MFE/high-MAE rows.", "MFE_90D_pct": 27.46, "MAE_90D_pct": -45.47, "score_return_alignment_label": "current_profile_false_positive_if_battery_theme_peak_promoted_to_stage2_actionable", "current_profile_verdict": "current_profile_false_positive_if_battery_theme_peak_promoted_to_stage2_actionable"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14_L216_234920_ZAIGLE_LFP_FINANCING_GAP", "trigger_id": "T_C14_L216_234920_20230511_LFP_FINANCING_GAP", "symbol": "234920", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"ev_demand_slowdown_score": 50, "calloff_or_utilization_break_score": 25, "proxy_theme_risk_score": 45, "margin_bridge_score": 20, "source_quality_score": 55, "positioning_overheat_score": 70}, "weighted_score_before": 72, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"ev_demand_slowdown_score": 60, "calloff_or_utilization_break_score": 35, "proxy_theme_risk_score": 80, "margin_bridge_score": 25, "source_quality_score": 65, "positioning_overheat_score": 50}, "weighted_score_after": 58, "stage_label_after": "Stage4B-Watch", "changed_components": ["proxy_theme_risk_score", "calloff_or_utilization_break_score", "positioning_overheat_score"], "component_delta_explanation": "C14 candidate guard separates direct utilization/call-off break from proxy/theme vocabulary and applies 4B exit guard to high-MFE/high-MAE rows.", "MFE_90D_pct": 67.42, "MAE_90D_pct": -13.23, "score_return_alignment_label": "stage2_should_require_capex_funding_customer_calloff_or_revenue_bridge", "current_profile_verdict": "stage2_should_require_capex_funding_customer_calloff_or_revenue_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14_L216_234920_ZAICELL_US_LFP_JV", "trigger_id": "T_C14_L216_234920_20230807_ZAICELL_JV", "symbol": "234920", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"ev_demand_slowdown_score": 50, "calloff_or_utilization_break_score": 25, "proxy_theme_risk_score": 45, "margin_bridge_score": 20, "source_quality_score": 55, "positioning_overheat_score": 70}, "weighted_score_before": 72, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"ev_demand_slowdown_score": 60, "calloff_or_utilization_break_score": 35, "proxy_theme_risk_score": 80, "margin_bridge_score": 25, "source_quality_score": 65, "positioning_overheat_score": 85}, "weighted_score_after": 58, "stage_label_after": "Stage4B-Watch", "changed_components": ["proxy_theme_risk_score", "calloff_or_utilization_break_score", "positioning_overheat_score"], "component_delta_explanation": "C14 candidate guard separates direct utilization/call-off break from proxy/theme vocabulary and applies 4B exit guard to high-MFE/high-MAE rows.", "MFE_90D_pct": 45.23, "MAE_90D_pct": -58.34, "score_return_alignment_label": "hard_4c_too_early_but_stage2_actionable_also_too_loose", "current_profile_verdict": "hard_4c_too_early_but_stage2_actionable_also_too_loose"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C14_L216_131400_EV_ADVANCED_MATERIAL_THEME_HALT", "trigger_id": "T_C14_L216_131400_20230419_THEME_HALT", "symbol": "131400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"ev_demand_slowdown_score": 50, "calloff_or_utilization_break_score": 25, "proxy_theme_risk_score": 45, "margin_bridge_score": 20, "source_quality_score": 55, "positioning_overheat_score": 70}, "weighted_score_before": 72, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"ev_demand_slowdown_score": 60, "calloff_or_utilization_break_score": 35, "proxy_theme_risk_score": 80, "margin_bridge_score": 25, "source_quality_score": 65, "positioning_overheat_score": 85}, "weighted_score_after": 66, "stage_label_after": "Stage4B-Watch", "changed_components": ["proxy_theme_risk_score", "calloff_or_utilization_break_score", "positioning_overheat_score"], "component_delta_explanation": "C14 candidate guard separates direct utilization/call-off break from proxy/theme vocabulary and applies 4B exit guard to high-MFE/high-MAE rows.", "MFE_90D_pct": 52.49, "MAE_90D_pct": -64.24, "score_return_alignment_label": "price_only_blowoff_should_block_positive_stage", "current_profile_verdict": "price_only_blowoff_should_block_positive_stage"}
{"row_type": "residual_contribution", "round": "R3", "loop": "216", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "new_independent_case_count": 9, "reused_case_count": 0, "new_symbol_count": 8, "new_trigger_family_count": 9, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["battery_proxy_theme_false_positive", "high_mfe_high_mae_event_cap", "hard_4c_too_early_without_second_confirmation", "actual_utilization_break_protection"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Apply C14 candidate rules only as shadow/canonical-specific candidates until batch validation confirms them.
- Do not loosen Stage3-Green thresholds.
- Treat high-MFE/high-MAE C14 rows as staged-entry/exit-guard evidence, not clean positives.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 216
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing; original Index Priority 0
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|C11_BATTERY_ORDERBOOK_RERATING|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Prompt source: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Evidence URLs are listed in Section 9 and in machine-readable trigger rows.
