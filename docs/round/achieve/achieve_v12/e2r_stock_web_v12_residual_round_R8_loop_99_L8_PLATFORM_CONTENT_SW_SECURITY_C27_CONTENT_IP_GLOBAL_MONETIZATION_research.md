# E2R Stock-Web v12 Residual Research — R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 99
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: mixed_C27_global_ip_launch_tour_retention_ltv_set
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 / 48 rows / need to 50 = 2
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

Static No-Repeat Index shows `C27_CONTENT_IP_GLOBAL_MONETIZATION` at 48 representative rows, so this run targets the final gap to the 50-row practical calibration band. This session already added several Priority 0 passes for C02/C09/C14/C10/C06/C07/C11/C01, so this C27 run avoids rematerializing the same semiconductor/grid/battery loops and instead fills an unserved Priority 1 content-IP axis.

Existing high-frequency C27 symbols in the index include `293490`, `352820`, `035760`, `035900`, `036420`, and `041510`. This run avoids those top-covered symbols and uses six independent symbols: `122870`, `078340`, `259960`, `263750`, `194480`, `251270`.

Hard duplicate gate:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No row in this file intentionally repeats the same C27 symbol/trigger/entry-date combination from the static index or from this conversation's generated files.

## 2. Stock-Web price-source verification

Stock-Web manifest checked:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
schema_path = atlas/schema.json
```

The schema defines `MFE_N_pct` as max high from entry date through N tradable rows divided by entry price, minus one, and `MAE_N_pct` as min low from the same window divided by entry price, minus one. All six trigger rows have full 30D/90D/180D MFE·MAE and a full 180-trading-day forward window.

Profile contamination check:

| symbol | profile status | corporate-action candidate overlap in entry~D+180 | calibration usable |
|---|---|---:|---:|
| 122870 | active_like | none; profile candidates 2012/2014 only | true |
| 078340 | active_like | none; profile candidate 2007 only | true |
| 259960 | active_like | none | true |
| 263750 | active_like | none; profile candidate 2021 only | true |
| 194480 | active_like | none | true |
| 251270 | active_like | none | true |

## 3. Case set summary

| symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | classification |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 122870 | 와이지엔터테인먼트 | Stage2-Actionable | 2022-08-09 | 2022-08-10 | 58,000 | 9.14 | -16.72 | 9.14 | -31.98 | 14.14 | -31.98 | counterexample |
| 078340 | 컴투스 | 4B | 2023-03-09 | 2023-03-09 | 68,000 | 17.21 | -4.26 | 17.21 | -19.71 | 17.21 | -41.18 | counterexample |
| 259960 | 크래프톤 | Stage2-Actionable | 2023-05-19 | 2023-05-22 | 200,500 | 4.24 | -9.08 | 4.24 | -27.18 | 21.20 | -27.23 | positive_with_stage2_delay |
| 263750 | 펄어비스 | 4B | 2023-08-23 | 2023-08-24 | 45,650 | 11.94 | -2.63 | 17.42 | -20.26 | 17.42 | -41.73 | counterexample |
| 194480 | 데브시스터즈 | Stage2-Actionable | 2023-12-28 | 2023-12-28 | 48,500 | 13.40 | -29.69 | 21.44 | -29.69 | 57.32 | -29.69 | positive_with_local_4B_watch |
| 251270 | 넷마블 | 4B | 2024-05-08 | 2024-05-08 | 60,700 | 19.28 | -11.70 | 19.28 | -13.67 | 19.28 | -30.23 | counterexample_with_4B_watch |

## 4. Evidence notes by case

### 4.1 122870 와이지엔터테인먼트 — global tour IP monetization, but renewal/timing cap

BLACKPINK's BORN PINK tour schedule created a credible global tour monetization route. The issue is not whether the IP was global; the issue is whether a tour calendar alone should unlock C27 Stage3. The 180D path produced only +14.14% MFE and -31.98% MAE, so the better rule is Stage2-Actionable plus renewal/tour-settlement bridge, not Stage3-Yellow/Green.

Evidence URL: https://koreajoongangdaily.joins.com/2022/08/09/entertainment/kpop/Korea-Kpop-Blackpink/20220809112738814.html

### 4.2 078340 컴투스 — global game launch without retention/LTV bridge

Summoners War: Chronicles launched globally across PC/mobile platforms, but global availability did not prove retention, monetization durability, or margin leverage. It produced early +17.21% MFE but then -41.18% 180D MAE and -49.81% post-peak drawdown. This is a clean C27 false-positive guardrail case.

Evidence URL: https://www.cosmocover.com/newsroom/com2us-mmorpg-summoners-war-chronicles-launches-today-on-pc-and-mobile/

### 4.3 259960 크래프톤 — regulatory reopen of existing live-service monetization

BGMI approval after the India ban restored an existing live-service monetization route. The 90D path was noisy, but the 180D path reached +21.20% MFE. This is not immediate Green, but it is a delayed positive Stage2-Actionable case when regulatory clearance reconnects a large live-service user base.

Evidence URL: https://www.reuters.com/technology/krafton-gets-approval-resume-battle-royale-game-india-2023-05-19/

### 4.4 263750 펄어비스 — trailer optionality is not monetization

The Crimson Desert Gamescom trailer was high-information visibility for IP optionality, but no launch/revenue/preorder bridge existed at the trigger point. Price path confirms the distinction: +17.42% 180D MFE but -41.73% 180D MAE and -50.37% drawdown after peak.

Evidence URL: https://crimsondesert.pearlabyss.com/ko-kr/News/Notice/Detail?_boardNo=26

### 4.5 194480 데브시스터즈 — China launch positive, but local 4B watch after MFE

CookieRun: Kingdom's China launch is closer to real C27 commercialization than a trailer or generic publishing headline because it links IP, local partners, territory expansion, and live service. The 180D MFE of +57.32% supports positive recognition, but -29.69% MAE and -52.75% post-peak drawdown require a local 4B watch once the market front-runs the launch.

Evidence URL: https://www.devsisters.com/en/games/cookierun-kingdom

### 4.6 251270 넷마블 — global webtoon-IP launch with immediate peak-chase risk

Solo Leveling: ARISE was a real global IP launch, not a vague theme. However, entry on launch day caught an almost immediate local peak: +19.28% MFE but -30.23% 180D MAE and -41.51% drawdown after the 2024-05-10 peak. C27 should demand durable revenue/retention evidence before Stage3, and use 4B watch for launch-day overheat.

Evidence URL: https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=4808

## 5. Raw component score breakdown

C27 runtime weight proxy used for stress simulation:

```text
EPS/FCF 20, Visibility 18, Bottleneck 8, Mispricing 14, Valuation 12, Capital allocation 8, Information confidence 20
```

| symbol | company | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | total_pre_bonus | total_after_stage2_bonus |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 122870 | 와이지엔터테인먼트 | 38 | 45 | 50 | 42 | 40 | 30 | 70 | 46.78 | 48.78 |
| 078340 | 컴투스 | 42 | 45 | 45 | 50 | 35 | 35 | 68 | 47.70 | 47.70 |
| 259960 | 크래프톤 | 64 | 70 | 55 | 64 | 60 | 45 | 82 | 65.96 | 67.96 |
| 263750 | 펄어비스 | 35 | 32 | 48 | 60 | 38 | 30 | 72 | 46.36 | 46.36 |
| 194480 | 데브시스터즈 | 70 | 70 | 58 | 68 | 62 | 42 | 78 | 67.16 | 69.16 |
| 251270 | 넷마블 | 58 | 55 | 50 | 65 | 45 | 38 | 76 | 58.24 | 58.24 |

Interpretation:

- `194480` and `259960` are valid Stage2-Actionable/delayed-positive examples because there is actual launch/regulatory reopen evidence tied to a monetizable service.
- `078340`, `263750`, and `251270` show why global availability, trailer attention, and launch-day buzz require local 4B caps until retention/LTV or revenue/margin evidence confirms.
- `122870` shows a music/tour variant: global tour monetization is real, but Stage3 should wait for settlement/renewal or repeated earnings bridge rather than tour schedule alone.

## 6. Current calibrated profile stress test

Current profile already blocks price-only blowoff and requires non-price evidence for full 4B. C27 still needs a more specific bridge:

```text
C27_CONTENT_IP_MONETIZATION_REQUIRES_DURABLE_REVENUE_RETENTION_OR_TOUR_SETTLEMENT_BRIDGE_WITH_LAUNCH_4B_CAP
```

Residual errors this rule targets:

| error type | cases | mechanism |
|---|---|---|
| false positive if launch/trailer/tour headline unlocks Stage3 | 122870, 078340, 263750, 251270 | information confidence high, but monetization durability and margin bridge absent |
| too late if actual platform/regulatory/territory unlock ignored | 259960, 194480 | existing live service or China launch gave real route to monetization |
| local 4B needed after fast MFE | 078340, 263750, 194480, 251270 | post-peak drawdown > 40% in several cases |

## 7. Sector-specific / canonical rule candidate

```text
L8_C27_CONTENT_IP_LAUNCH_TOUR_AND_PLATFORM_CONVERSION_SPLIT
```

```text
C27_CONTENT_IP_MONETIZATION_REQUIRES_DURABLE_REVENUE_RETENTION_OR_TOUR_SETTLEMENT_BRIDGE_WITH_LAUNCH_4B_CAP
```

Rule detail:

1. Verified global launch, tour schedule, platform reopen, or trailer visibility may unlock Stage2-Actionable.
2. Stage3-Yellow requires at least one of: durable revenue evidence, retention/LTV evidence, platform settlement, tour settlement, royalty bridge, or explicit margin leverage.
3. A pre-release trailer, IP buzz, preregistration number, or launch-day spike without retention/revenue evidence should be capped at Stage2/4B-watch.
4. If 30D or 90D MFE is front-loaded and post-peak drawdown exceeds 35~40%, C27 should emit local 4B watch even if the IP remains structurally valuable.

## 8. Machine-readable rows

### 8.1 case rows

```jsonl
{"row_type": "case", "case_id": "C27_122870_2022_BORN_PINK_WORLD_TOUR_STAGE2_4B_COUNTEREXAMPLE", "symbol": "122870", "company_name": "와이지엔터테인먼트", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GLOBAL_TOUR_IP_MONETIZATION_RENEWAL_RISK_CAP", "case_summary": "BORN PINK world tour schedule established global IP monetization, but artist-contract/renewal and realization timing risk meant Stage3 should remain capped.", "case_classification": "counterexample", "calibration_usable": true, "representative_for_aggregate": true}
{"row_type": "case", "case_id": "C27_078340_2023_CHRONICLES_GLOBAL_LAUNCH_RETENTION_COUNTEREXAMPLE", "symbol": "078340", "company_name": "컴투스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GLOBAL_GAME_LAUNCH_RETENTION_LTV_GATE", "case_summary": "Summoners War: Chronicles global launch reached many countries/platforms, but launch surface area did not prove retention, LTV, or operating leverage.", "case_classification": "counterexample", "calibration_usable": true, "representative_for_aggregate": true}
{"row_type": "case", "case_id": "C27_259960_2023_BGMI_INDIA_RELAUNCH_DELAYED_POSITIVE", "symbol": "259960", "company_name": "크래프톤", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_REGULATORY_REOPEN_EXISTING_LIVE_SERVICE_MONETIZATION", "case_summary": "BGMI approval restored a large existing live-service monetization route, but 90D MAE shows it should unlock Stage2 first, not immediate Green.", "case_classification": "positive_with_stage2_delay", "calibration_usable": true, "representative_for_aggregate": true}
{"row_type": "case", "case_id": "C27_263750_2023_CRIMSON_DESERT_TRAILER_OPTIONALITY_COUNTEREXAMPLE", "symbol": "263750", "company_name": "펄어비스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_PRE_RELEASE_TRAILER_OPTIONALITY_4B_CAP", "case_summary": "Crimson Desert Gamescom trailer was strong IP optionality, but without launch date, paid conversion, or preorder bridge it behaved like a 4B optionality cap.", "case_classification": "counterexample", "calibration_usable": true, "representative_for_aggregate": true}
{"row_type": "case", "case_id": "C27_194480_2023_COOKIE_RUN_CHINA_LAUNCH_POSITIVE_WITH_4B", "symbol": "194480", "company_name": "데브시스터즈", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_CHINA_PARTNER_LAUNCH_MONETIZATION_WITH_PEAK_4B", "case_summary": "CookieRun: Kingdom China launch had actual platform/territory conversion and later large MFE, but the path included severe early MAE and post-peak drawdown.", "case_classification": "positive_with_local_4B_watch", "calibration_usable": true, "representative_for_aggregate": true}
{"row_type": "case", "case_id": "C27_251270_2024_SOLO_LEVELING_GLOBAL_LAUNCH_HIGH_MAE_COUNTEREXAMPLE", "symbol": "251270", "company_name": "넷마블", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GLOBAL_WEBTOON_IP_GAME_LAUNCH_DURABILITY_GATE", "case_summary": "Solo Leveling: ARISE global launch was real IP commercialization, but entry around launch peak required 4B cap until durable revenue/margin evidence appeared.", "case_classification": "counterexample_with_4B_watch", "calibration_usable": true, "representative_for_aggregate": true}
```

### 8.2 trigger rows

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "selected_round": "R8", "selected_loop": 99, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GLOBAL_TOUR_IP_MONETIZATION_RENEWAL_RISK_CAP", "case_id": "C27_122870_2022_BORN_PINK_WORLD_TOUR_STAGE2_4B_COUNTEREXAMPLE", "symbol": "122870", "company_name": "와이지엔터테인먼트", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-09", "entry_date": "2022-08-10", "entry_price": 58000, "MFE_30D_pct": 9.14, "MAE_30D_pct": -16.72, "MFE_90D_pct": 9.14, "MAE_90D_pct": -31.98, "MFE_180D_pct": 14.14, "MAE_180D_pct": -31.98, "peak_date": "2023-04-17", "peak_price": 66200, "drawdown_after_peak_pct": -12.24, "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://koreajoongangdaily.joins.com/2022/08/09/entertainment/kpop/Korea-Kpop-Blackpink/20220809112738814.html", "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "classification": "counterexample", "current_profile_error_type": "false_positive_if_tour_schedule_headline_unlocks_stage3"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "selected_round": "R8", "selected_loop": 99, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GLOBAL_GAME_LAUNCH_RETENTION_LTV_GATE", "case_id": "C27_078340_2023_CHRONICLES_GLOBAL_LAUNCH_RETENTION_COUNTEREXAMPLE", "symbol": "078340", "company_name": "컴투스", "trigger_type": "4B", "trigger_date": "2023-03-09", "entry_date": "2023-03-09", "entry_price": 68000, "MFE_30D_pct": 17.21, "MAE_30D_pct": -4.26, "MFE_90D_pct": 17.21, "MAE_90D_pct": -19.71, "MFE_180D_pct": 17.21, "MAE_180D_pct": -41.18, "peak_date": "2023-04-04", "peak_price": 79700, "drawdown_after_peak_pct": -49.81, "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://www.cosmocover.com/newsroom/com2us-mmorpg-summoners-war-chronicles-launches-today-on-pc-and-mobile/", "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "classification": "counterexample", "current_profile_error_type": "false_positive_if_global_launch_without_retention_and_ltv_bridge_gets_stage3"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "selected_round": "R8", "selected_loop": 99, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_REGULATORY_REOPEN_EXISTING_LIVE_SERVICE_MONETIZATION", "case_id": "C27_259960_2023_BGMI_INDIA_RELAUNCH_DELAYED_POSITIVE", "symbol": "259960", "company_name": "크래프톤", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-19", "entry_date": "2023-05-22", "entry_price": 200500, "MFE_30D_pct": 4.24, "MAE_30D_pct": -9.08, "MFE_90D_pct": 4.24, "MAE_90D_pct": -27.18, "MFE_180D_pct": 21.2, "MAE_180D_pct": -27.23, "peak_date": "2024-02-14", "peak_price": 243000, "drawdown_after_peak_pct": -6.79, "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://www.reuters.com/technology/krafton-gets-approval-resume-battle-royale-game-india-2023-05-19/", "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "classification": "positive_with_stage2_delay", "current_profile_error_type": "too_late_if_regulatory_reopen_and_live_service_scale_is_ignored"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "selected_round": "R8", "selected_loop": 99, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_PRE_RELEASE_TRAILER_OPTIONALITY_4B_CAP", "case_id": "C27_263750_2023_CRIMSON_DESERT_TRAILER_OPTIONALITY_COUNTEREXAMPLE", "symbol": "263750", "company_name": "펄어비스", "trigger_type": "4B", "trigger_date": "2023-08-23", "entry_date": "2023-08-24", "entry_price": 45650, "MFE_30D_pct": 11.94, "MAE_30D_pct": -2.63, "MFE_90D_pct": 17.42, "MAE_90D_pct": -20.26, "MFE_180D_pct": 17.42, "MAE_180D_pct": -41.73, "peak_date": "2023-11-08", "peak_price": 53600, "drawdown_after_peak_pct": -50.37, "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://crimsondesert.pearlabyss.com/ko-kr/News/Notice/Detail?_boardNo=26", "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "classification": "counterexample", "current_profile_error_type": "false_positive_if_trailer_or_gamescom_attention_is_treated_as_revenue_conversion"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "selected_round": "R8", "selected_loop": 99, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_CHINA_PARTNER_LAUNCH_MONETIZATION_WITH_PEAK_4B", "case_id": "C27_194480_2023_COOKIE_RUN_CHINA_LAUNCH_POSITIVE_WITH_4B", "symbol": "194480", "company_name": "데브시스터즈", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-28", "entry_date": "2023-12-28", "entry_price": 48500, "MFE_30D_pct": 13.4, "MAE_30D_pct": -29.69, "MFE_90D_pct": 21.44, "MAE_90D_pct": -29.69, "MFE_180D_pct": 57.32, "MAE_180D_pct": -29.69, "peak_date": "2024-06-26", "peak_price": 76300, "drawdown_after_peak_pct": -52.75, "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://www.devsisters.com/en/games/cookierun-kingdom", "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "classification": "positive_with_local_4B_watch", "current_profile_error_type": "too_late_if_china_platform_partner_and_actual_launch_are_ignored_but_false_positive_if_peak_chased_after_mfe"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "selected_round": "R8", "selected_loop": 99, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GLOBAL_WEBTOON_IP_GAME_LAUNCH_DURABILITY_GATE", "case_id": "C27_251270_2024_SOLO_LEVELING_GLOBAL_LAUNCH_HIGH_MAE_COUNTEREXAMPLE", "symbol": "251270", "company_name": "넷마블", "trigger_type": "4B", "trigger_date": "2024-05-08", "entry_date": "2024-05-08", "entry_price": 60700, "MFE_30D_pct": 19.28, "MAE_30D_pct": -11.7, "MFE_90D_pct": 19.28, "MAE_90D_pct": -13.67, "MFE_180D_pct": 19.28, "MAE_180D_pct": -30.23, "peak_date": "2024-05-10", "peak_price": 72400, "drawdown_after_peak_pct": -41.51, "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=4808", "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "classification": "counterexample_with_4B_watch", "current_profile_error_type": "false_positive_if_global_launch_and_preregistration_count_are_enough_for_stage3_without_durability"}
```

### 8.3 score_simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "C27_122870_2022_BORN_PINK_WORLD_TOUR_STAGE2_4B_COUNTEREXAMPLE", "symbol": "122870", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "weights": {"eps_fcf_explosion": 20, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 12, "capital_allocation": 8, "information_confidence": 20}, "component_scores": {"eps_fcf_explosion": 38, "earnings_visibility": 45, "bottleneck_pricing": 50, "market_mispricing": 42, "valuation_rerating": 40, "capital_allocation": 30, "information_confidence": 70}, "weighted_total_pre_bonus": 46.78, "weighted_total_stage2_actionable_bonus": 48.78, "simulated_stage_current_profile": "Stage1/Watch", "stress_test_note": "false_positive_if_tour_schedule_headline_unlocks_stage3"}
{"row_type": "score_simulation", "case_id": "C27_078340_2023_CHRONICLES_GLOBAL_LAUNCH_RETENTION_COUNTEREXAMPLE", "symbol": "078340", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "weights": {"eps_fcf_explosion": 20, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 12, "capital_allocation": 8, "information_confidence": 20}, "component_scores": {"eps_fcf_explosion": 42, "earnings_visibility": 45, "bottleneck_pricing": 45, "market_mispricing": 50, "valuation_rerating": 35, "capital_allocation": 35, "information_confidence": 68}, "weighted_total_pre_bonus": 47.7, "weighted_total_stage2_actionable_bonus": 47.7, "simulated_stage_current_profile": "4B", "stress_test_note": "false_positive_if_global_launch_without_retention_and_ltv_bridge_gets_stage3"}
{"row_type": "score_simulation", "case_id": "C27_259960_2023_BGMI_INDIA_RELAUNCH_DELAYED_POSITIVE", "symbol": "259960", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "weights": {"eps_fcf_explosion": 20, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 12, "capital_allocation": 8, "information_confidence": 20}, "component_scores": {"eps_fcf_explosion": 64, "earnings_visibility": 70, "bottleneck_pricing": 55, "market_mispricing": 64, "valuation_rerating": 60, "capital_allocation": 45, "information_confidence": 82}, "weighted_total_pre_bonus": 65.96, "weighted_total_stage2_actionable_bonus": 67.96, "simulated_stage_current_profile": "Stage2-Actionable", "stress_test_note": "too_late_if_regulatory_reopen_and_live_service_scale_is_ignored"}
{"row_type": "score_simulation", "case_id": "C27_263750_2023_CRIMSON_DESERT_TRAILER_OPTIONALITY_COUNTEREXAMPLE", "symbol": "263750", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "weights": {"eps_fcf_explosion": 20, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 12, "capital_allocation": 8, "information_confidence": 20}, "component_scores": {"eps_fcf_explosion": 35, "earnings_visibility": 32, "bottleneck_pricing": 48, "market_mispricing": 60, "valuation_rerating": 38, "capital_allocation": 30, "information_confidence": 72}, "weighted_total_pre_bonus": 46.36, "weighted_total_stage2_actionable_bonus": 46.36, "simulated_stage_current_profile": "4B", "stress_test_note": "false_positive_if_trailer_or_gamescom_attention_is_treated_as_revenue_conversion"}
{"row_type": "score_simulation", "case_id": "C27_194480_2023_COOKIE_RUN_CHINA_LAUNCH_POSITIVE_WITH_4B", "symbol": "194480", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "weights": {"eps_fcf_explosion": 20, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 12, "capital_allocation": 8, "information_confidence": 20}, "component_scores": {"eps_fcf_explosion": 70, "earnings_visibility": 70, "bottleneck_pricing": 58, "market_mispricing": 68, "valuation_rerating": 62, "capital_allocation": 42, "information_confidence": 78}, "weighted_total_pre_bonus": 67.16, "weighted_total_stage2_actionable_bonus": 69.16, "simulated_stage_current_profile": "Stage2-Actionable", "stress_test_note": "too_late_if_china_platform_partner_and_actual_launch_are_ignored_but_false_positive_if_peak_chased_after_mfe"}
{"row_type": "score_simulation", "case_id": "C27_251270_2024_SOLO_LEVELING_GLOBAL_LAUNCH_HIGH_MAE_COUNTEREXAMPLE", "symbol": "251270", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "weights": {"eps_fcf_explosion": 20, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 12, "capital_allocation": 8, "information_confidence": 20}, "component_scores": {"eps_fcf_explosion": 58, "earnings_visibility": 55, "bottleneck_pricing": 50, "market_mispricing": 65, "valuation_rerating": 45, "capital_allocation": 38, "information_confidence": 76}, "weighted_total_pre_bonus": 58.24, "weighted_total_stage2_actionable_bonus": 58.24, "simulated_stage_current_profile": "4B", "stress_test_note": "false_positive_if_global_launch_and_preregistration_count_are_enough_for_stage3_without_durability"}
```

### 8.4 aggregate / shadow_weight / residual_contribution / narrative_only rows

```jsonl
{"row_type": "aggregate", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "selected_round": "R8", "selected_loop": 99, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "static_no_repeat_rows_before": 48, "expected_rows_after_acceptance": 54, "new_independent_case_count": 6, "new_independent_symbol_count": 6, "calibration_usable_rows": 6, "positive_case_count": 2, "counterexample_count": 4, "local_4B_watch_case_count": 5, "hard_4C_case_count": 0, "current_profile_error_count": 6, "source_proxy_only_rows": 0, "evidence_url_pending_rows": 0, "average_MFE_180D_pct": 24.43, "average_MAE_180D_pct": -33.67, "rule_candidate": "C27_CONTENT_IP_MONETIZATION_REQUIRES_DURABLE_REVENUE_RETENTION_OR_TOUR_SETTLEMENT_BRIDGE_WITH_LAUNCH_4B_CAP"}
{"row_type": "shadow_weight", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "do_not_propose_new_weight_delta": false, "shadow_rule_candidate": "C27_CONTENT_IP_MONETIZATION_REQUIRES_DURABLE_REVENUE_RETENTION_OR_TOUR_SETTLEMENT_BRIDGE_WITH_LAUNCH_4B_CAP", "axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "suggested_runtime_effect": "Keep information_confidence high for verified global launch/approval, but cap Stage3 until revenue durability, retention/LTV, settlement, or margin bridge confirms."}
{"row_type": "residual_contribution", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "loop_contribution_label": "canonical_archetype_rule_candidate", "residual_error_reduced": "C27 launch/trailer/tour headline false positives and missed delayed positives", "novelty_basis": "six new symbols versus top-covered C27 symbols in No-Repeat Index; no same symbol+trigger_type+entry_date duplicate used"}
{"row_type": "narrative_only", "note": "C27 needs a bridge distinction: global IP availability is not the same as durable monetization. Launch/trailer/tour events are Stage2 unless retention/LTV, platform settlement, tour settlement, or margin bridge confirms; after fast MFE, local 4B watch remains necessary."}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

Later coding-agent task:
1. Ingest this Markdown as a standard v12 result file.
2. Validate all trigger rows for required fields: canonical_archetype_id, large_sector_id, trigger_type, entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add a candidate C27 shadow rule:
   C27_CONTENT_IP_MONETIZATION_REQUIRES_DURABLE_REVENUE_RETENTION_OR_TOUR_SETTLEMENT_BRIDGE_WITH_LAUNCH_4B_CAP
5. Treat this as shadow weight / rule-candidate evidence only. Do not directly patch production scoring from one file.
6. Compare against existing C27 rows, especially existing high-frequency symbols 293490, 352820, 035760, 035900, 036420, 041510.
```

## 10. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 11. Next research state

```text
completed_round = R8
completed_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / C27 rows 48 -> expected 54 after acceptance
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_followup_if_below_50 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
