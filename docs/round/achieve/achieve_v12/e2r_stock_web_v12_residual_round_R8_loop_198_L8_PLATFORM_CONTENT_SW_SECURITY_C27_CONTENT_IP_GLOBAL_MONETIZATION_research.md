# E2R Stock-Web v12 Residual Research — R8 Loop 198 — C27 Content/IP Global Monetization

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R8
selected_loop = 198
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
live_candidate_mode = false
```

## 1. Selection Rationale

The raw No-Repeat Index still lists C27 at 48 rows / need to 50 = 2, while this live session has already added loop 156 and loop 181. Instead of adding another large-cap K-pop or already-used game cluster, this pass isolates a different C27 leaf: **game launch/liveops, single-title demos, kids IP merchandise/movie conversion, and theatrical distributor economics**.

This is a quality-repair pass, not a current stock scan. Round R8 and L8 are used because C26~C28 map to `L8_PLATFORM_CONTENT_SW_SECURITY`. The selected filename, metadata, and canonical scope are intentionally aligned.

```text
index_baseline_coverage_before = C27 rows 48
index_baseline_coverage_after_if_accepted = C27 rows 56
session_aware_after_loop156_loop181_loop198_if_accepted ≈ C27 rows 71
new_independent_case_count = 8
positive_case_count = 4
counterexample_count = 4
current_profile_error_count = 5
4B_or_high_MAE_guard_count = 6
```

## 2. Price Source Validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_price_rule = close price on entry_date, or next tradable date if trigger date was not tradable
MFE/MAE_rule = max high / min low over the next N tradable rows after entry_date
```

The trigger windows below have at least 180 forward tradable rows in the local stock-web shard cache used for calculation. Corporate-action candidate dates visible in symbol profiles are outside the relevant D+180 windows, so all listed trigger rows are `calibration_usable=true`.

## 3. Case Table

| case_id | symbol | company | trigger | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | polarity |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| C27_L198_01_225570 | 225570 | 넥슨게임즈 | Stage2-Actionable | 2024-07-03 | 17,900 | 72.91% | -28.10% | 72.91% | -33.52% | positive |
| C27_L198_02_225570 | 225570 | 넥슨게임즈 | Stage4B | 2024-08-09 | 28,850 | 2.77% | -56.67% | 2.77% | -60.31% | counterexample |
| C27_L198_03_263750 | 263750 | 펄어비스 | Stage2 | 2024-07-26 | 44,650 | 4.03% | -28.56% | 4.03% | -40.09% | counterexample |
| C27_L198_04_036570 | 036570 | 엔씨소프트 | Stage2 | 2024-10-28 | 210,500 | 17.81% | -25.27% | 17.81% | -36.06% | counterexample |
| C27_L198_05_182360 | 182360 | 큐브엔터 | Stage2-Actionable | 2024-05-14 | 14,630 | 8.89% | -25.22% | 23.10% | -25.22% | positive |
| C27_L198_06_419530 | 419530 | SAMG엔터 | Stage2-Actionable | 2024-07-12 | 9,740 | 101.54% | -0.31% | 264.48% | -0.31% | positive |
| C27_L198_07_086980 | 086980 | 쇼박스 | Stage2-Actionable | 2024-02-23 | 3,840 | 18.36% | -17.06% | 31.51% | -17.06% | positive |
| C27_L198_08_078340 | 078340 | 컴투스 | Stage2 | 2025-02-13 | 49,050 | 2.75% | -27.52% | 2.75% | -33.23% | counterexample |

## 4. Case Notes

### 4.1 Nexon Games / The First Descendant — early launch success vs late headline trap

`225570 / 2024-07-03` is the cleanest game-liveops positive in this pass: the title had a global launch, top-seller evidence, and a measurable global player bridge. The 30D MFE of `+72.91%` shows the signal was not imaginary. But the same signal also teaches the exit rule: by the post-earnings late trigger on `2024-08-09`, the remaining MFE was only `+2.77%` while the 180D MAE reached `-60.31%`. The same IP can be a Stage2 signal before the fire catches, and a Stage4B warning after the oxygen is gone.

### 4.2 Pearl Abyss / Crimson Desert — demo-only evidence is not monetization

`263750 / 2024-07-26` had strong attention evidence: first public playable demo at gamescom. But a public demo is a shop window, not the cash register. There was no release, preorder conversion, MAU/retention, paid unit sales, platform economics, or margin bridge at trigger time. The price path, `MFE180 +4.03% / MAE180 -40.09%`, marks this as a C27 demo-only false positive.

### 4.3 NCsoft / Throne and Liberty — user count bridge needs retention and monetization

`036570 / 2024-10-28` had real adoption evidence after the Amazon Games launch and reported 4m global users. But user-count evidence alone does not prove retained economics. `MFE90 +17.81%` did not reach a clean 20% hit, while `MAE180 -36.06%` makes it a high-MAE Stage2-Watch, not a Stage3 case.

### 4.4 Cube, SAMG, Showbox — retained economics can appear outside classic games

`182360 / Cube` confirms that album/IP sales plus operating-profit conversion can support Stage2-Actionable, but the 90D drawdown means Green requires repeat confirmation. `419530 / SAMG` is the strongest positive: movie IP + MD + China distribution connected attention, products, and channel economics, producing `MFE180 +264.48%` with only `-0.31%` MAE. `086980 / Showbox` shows theatrical distributor economics can work, but film hits naturally need event-cap exits.

### 4.5 Com2uS — profit turnaround without growth bridge is low-alpha

`078340 / 2025-02-13` had operating-profit turnaround language, but revenue was down and net loss remained large. The path had `MFE180 +2.75% / MAE180 -33.23%`, a classic C27 false-positive where accounting improvement lacks renewed IP monetization.

## 5. Current Calibrated Profile Stress Test

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

The current profile already blocks pure price-only 4B and asks for non-price bridge. The remaining C27 errors are more specific: it can still overweight **user-count evidence**, **demo attendance**, **one-quarter operating turnaround**, and **late post-launch headlines** when the evidence has not yet become retained economics. The shadow rule should not simply raise or lower C27 weight. It should split C27 evidence into two layers:

1. **attention layer**: demo, trailer, opening weekend, headline players, single-quarter profit rebound;
2. **retained-economics layer**: liveops retention/revenue, box-office share, MD/reorder, platform take-rate, repeat monetization, operating-profit conversion.

Only the second layer should allow Stage2-Actionable. The first layer should remain Stage2-Watch or local 4B if price has already moved.

## 6. Proposed Shadow Rule Candidate

```text
canonical_archetype_rule_candidate = C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_AND_EVENT_CAP_GATE_V3
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
new_axis_proposed = c27_retained_economics_liveops_revenue_bridge_and_event_cap_gate_v3
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_should_not_fire_on_demo_only_or_single_title_drawdown_without_irreversible_thesis_break
```

Rule shape:

```text
If C27 evidence is only demo/trailer/opening-week/user-count/turnaround vocabulary:
    max_stage = Stage2-Watch
    require event-cap or high-MAE guard if MFE30 already > 30% or MAE90 <= -20%

If C27 has retained-economics bridge:
    allow Stage2-Actionable
    examples: liveops revenue retention, paid-unit sales, box-office distributor economics, MD/reorder, platform take-rate, repeat monetization, OP/margin conversion

If a single-title hit has strong MFE but finite event nature:
    keep positive classification but add Stage4B exit overlay

If a drawdown follows demo-only or user-count evidence:
    do not escalate to hard 4C unless irreversible IP/contract/trust break is confirmed
```

## 7. Machine-readable Case Rows

```jsonl
{"row_type": "case", "case_id": "C27_L198_01_225570", "symbol": "225570", "company_name": "넥슨게임즈", "trigger_date": "2024-07-03", "case_role": "structural_success_4b_exit_guard", "case_polarity": "positive", "current_profile_error": false, "evidence_summary": "Nexon parent disclosed that The First Descendant launched globally on July 2 and quickly became a Steam top-seller with North America the largest player region and console users about 60% of the base. This was a real global launch bridge, but D+90/D+180 drawdown demands exit guard.", "evidence_url": "https://www.businesswire.com/news/home/20240808320361/en/Nexon-Releases-Earnings-for-Second-Quarter-2024"}
{"row_type": "case", "case_id": "C27_L198_02_225570", "symbol": "225570", "company_name": "넥슨게임즈", "trigger_date": "2024-08-09", "case_role": "late_entry_counterexample", "case_polarity": "counterexample", "current_profile_error": true, "evidence_summary": "The same TFD evidence became a late headline after the rerating. Entry near the local oxygen burn had only +2.77% MFE and a -60.31% 180D MAE, so this is a 4B exit/timing counterexample rather than a clean new positive.", "evidence_url": "https://www.businesswire.com/news/home/20240808320361/en/Nexon-Releases-Earnings-for-Second-Quarter-2024"}
{"row_type": "case", "case_id": "C27_L198_03_263750", "symbol": "263750", "company_name": "펄어비스", "trigger_date": "2024-07-26", "case_role": "demo_only_false_positive", "case_polarity": "counterexample", "current_profile_error": true, "evidence_summary": "Pearl Abyss announced the first public playable Crimson Desert demo at gamescom 2024. This was strong attention evidence, but no launch, preorder, revenue, platform economics, or margin bridge existed at the trigger.", "evidence_url": "https://crimsondesert.pearlabyss.com/it-IT/News/Notice/Detail?_boardNo=27"}
{"row_type": "case", "case_id": "C27_L198_04_036570", "symbol": "036570", "company_name": "엔씨소프트", "trigger_date": "2024-10-28", "case_role": "user_growth_with_retention_monetization_risk", "case_polarity": "counterexample", "current_profile_error": true, "evidence_summary": "Throne and Liberty passed 4m global users after the Amazon Games launch. User adoption was real, but monetization/retention quality and later drawdown make it a Stage2-Watch or high-MAE case, not Stage3.", "evidence_url": "https://www.koreajoongangdaily.com/business/ncsofts-change-on-display-with-throne-and-liberty/10552706"}
{"row_type": "case", "case_id": "C27_L198_05_182360", "symbol": "182360", "company_name": "큐브엔터", "trigger_date": "2024-05-14", "case_role": "ip_monetization_positive", "case_polarity": "positive", "current_profile_error": true, "evidence_summary": "Cube reported record Q1 2024 sales and operating profit, tied to (G)I-DLE album/IP sales and subsidiary distribution. It is a usable positive, but 90D MAE warns against Green without second-quarter confirmation.", "evidence_url": "https://www.mk.co.kr/en/stock/11014513"}
{"row_type": "case", "case_id": "C27_L198_06_419530", "symbol": "419530", "company_name": "SAMG엔터", "trigger_date": "2024-07-12", "case_role": "kids_ip_md_movie_positive", "case_polarity": "positive", "current_profile_error": false, "evidence_summary": "The Heartsping/Teenieping movie + toy MD + China release setup had a clean IP-to-products-to-distribution bridge, and the price path shows extreme MFE with negligible early MAE.", "evidence_url": "https://www.asiae.co.kr/en/article/2024071110021997503"}
{"row_type": "case", "case_id": "C27_L198_07_086980", "symbol": "086980", "company_name": "쇼박스", "trigger_date": "2024-02-23", "case_role": "film_hit_distribution_positive", "case_polarity": "positive", "current_profile_error": false, "evidence_summary": "Exhuma had the strongest 2024 opening-day box office in Korea at the trigger. This is a real film-distribution hit bridge, but the event still needs an event-cap/4B overlay because film hits are naturally finite.", "evidence_url": "https://www.koreajoongangdaily.com/entertainment/exhuma-summons-record-number-of-moviegoers-for-release-day-in-2024/11743973"}
{"row_type": "case", "case_id": "C27_L198_08_078340", "symbol": "078340", "company_name": "컴투스", "trigger_date": "2025-02-13", "case_role": "profit_turnaround_low_alpha_counterexample", "case_polarity": "counterexample", "current_profile_error": true, "evidence_summary": "Com2uS returned to operating profit in 2024, but annual revenue declined and net loss remained large. The path had low MFE and deep MAE, showing that profit-turnaround vocabulary alone is not enough for C27.", "evidence_url": "https://pulse.mk.co.kr/news/english/11239998"}
```

## 8. Machine-readable Trigger Rows

```jsonl
{"row_type": "trigger", "case_id": "C27_L198_01_225570", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "symbol": "225570", "company_name": "넥슨게임즈", "company_name_en": "Nexon Games", "trigger_date": "2024-07-03", "trigger_type": "Stage2-Actionable", "trigger_family": "TFD global launch / top-seller early live-service traction", "case_role": "structural_success_4b_exit_guard", "case_polarity": "positive", "current_profile_error": false, "evidence_url": "https://www.businesswire.com/news/home/20240808320361/en/Nexon-Releases-Earnings-for-Second-Quarter-2024", "evidence_summary": "Nexon parent disclosed that The First Descendant launched globally on July 2 and quickly became a Steam top-seller with North America the largest player region and console users about 60% of the base. This was a real global launch bridge, but D+90/D+180 drawdown demands exit guard.", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-03", "entry_price": 17900.0, "MFE_30D_pct": 72.91, "MAE_30D_pct": -3.91, "MFE_90D_pct": 72.91, "MAE_90D_pct": -28.1, "MFE_180D_pct": 72.91, "MAE_180D_pct": -33.52, "forward_window_trading_days": 180, "peak_180D_date": "2024-08-09", "peak_180D_price": 30950.0, "trough_180D_date": "2025-03-12", "trough_180D_price": 11900.0, "corporate_action_window_status": "not_contaminated_180D", "corporate_action_profile_note": "profile_corporate_actions_outside_180D_window: candidates 2017-06-12, 2018-05-09, 2022-04-15", "calibration_usable": true, "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION|225570|Stage2-Actionable|2024-07-03", "reuse_reason": "same symbol as another row but different trigger family", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "high_mae_guard_needed": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_prediction": "Stage2-Actionable", "proposed_shadow_profile_prediction": "Stage2-Actionable + mandatory 4B exit after launch spike", "raw_component_score_breakdown": {"eps_fcf_explosion": 42, "earnings_visibility": 55, "bottleneck_pricing_power": 38, "market_mispricing": 62, "valuation_rerating": 65, "capital_allocation": 24, "information_confidence": 64, "total_proxy": 76}}
{"row_type": "trigger", "case_id": "C27_L198_02_225570", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "symbol": "225570", "company_name": "넥슨게임즈", "company_name_en": "Nexon Games", "trigger_date": "2024-08-09", "trigger_type": "Stage4B", "trigger_family": "post-earnings top-seller late-entry after rerating", "case_role": "late_entry_counterexample", "case_polarity": "counterexample", "current_profile_error": true, "evidence_url": "https://www.businesswire.com/news/home/20240808320361/en/Nexon-Releases-Earnings-for-Second-Quarter-2024", "evidence_summary": "The same TFD evidence became a late headline after the rerating. Entry near the local oxygen burn had only +2.77% MFE and a -60.31% 180D MAE, so this is a 4B exit/timing counterexample rather than a clean new positive.", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-09", "entry_price": 28850.0, "MFE_30D_pct": 2.77, "MAE_30D_pct": -48.84, "MFE_90D_pct": 2.77, "MAE_90D_pct": -56.67, "MFE_180D_pct": 2.77, "MAE_180D_pct": -60.31, "forward_window_trading_days": 180, "peak_180D_date": "2024-08-12", "peak_180D_price": 29650.0, "trough_180D_date": "2025-04-09", "trough_180D_price": 11450.0, "corporate_action_window_status": "not_contaminated_180D", "corporate_action_profile_note": "profile_corporate_actions_outside_180D_window: candidates 2017-06-12, 2018-05-09, 2022-04-15", "calibration_usable": true, "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION|225570|Stage4B|2024-08-09", "reuse_reason": "same symbol as another row but different trigger family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "high_mae_guard_needed": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_prediction": "Stage2-Actionable if launch success overweighted", "proposed_shadow_profile_prediction": "Stage4B late-entry/high-MAE block", "raw_component_score_breakdown": {"eps_fcf_explosion": 35, "earnings_visibility": 44, "bottleneck_pricing_power": 36, "market_mispricing": 58, "valuation_rerating": 70, "capital_allocation": 18, "information_confidence": 66, "total_proxy": 64}}
{"row_type": "trigger", "case_id": "C27_L198_03_263750", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "symbol": "263750", "company_name": "펄어비스", "company_name_en": "Pearl Abyss", "trigger_date": "2024-07-26", "trigger_type": "Stage2", "trigger_family": "Crimson Desert gamescom playable demo without revenue timing", "case_role": "demo_only_false_positive", "case_polarity": "counterexample", "current_profile_error": true, "evidence_url": "https://crimsondesert.pearlabyss.com/it-IT/News/Notice/Detail?_boardNo=27", "evidence_summary": "Pearl Abyss announced the first public playable Crimson Desert demo at gamescom 2024. This was strong attention evidence, but no launch, preorder, revenue, platform economics, or margin bridge existed at the trigger.", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-26", "entry_price": 44650.0, "MFE_30D_pct": 4.03, "MAE_30D_pct": -28.56, "MFE_90D_pct": 4.03, "MAE_90D_pct": -28.56, "MFE_180D_pct": 4.03, "MAE_180D_pct": -40.09, "forward_window_trading_days": 180, "peak_180D_date": "2024-07-29", "peak_180D_price": 46450.0, "trough_180D_date": "2024-12-27", "trough_180D_price": 26750.0, "corporate_action_window_status": "not_contaminated_180D", "corporate_action_profile_note": "profile_corporate_actions_outside_180D_window: candidate 2021-04-16", "calibration_usable": true, "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION|263750|Stage2|2024-07-26", "reuse_reason": "new symbol or new trigger family inside C27", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "high_mae_guard_needed": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_prediction": "Stage2-Watch, but price momentum can over-promote", "proposed_shadow_profile_prediction": "Stage2-Watch only; demo-only cannot be Actionable", "raw_component_score_breakdown": {"eps_fcf_explosion": 22, "earnings_visibility": 26, "bottleneck_pricing_power": 31, "market_mispricing": 55, "valuation_rerating": 57, "capital_allocation": 18, "information_confidence": 56, "total_proxy": 61}}
{"row_type": "trigger", "case_id": "C27_L198_04_036570", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "symbol": "036570", "company_name": "엔씨소프트", "company_name_en": "NCsoft", "trigger_date": "2024-10-28", "trigger_type": "Stage2", "trigger_family": "Throne and Liberty 4m global users after launch", "case_role": "user_growth_with_retention_monetization_risk", "case_polarity": "counterexample", "current_profile_error": true, "evidence_url": "https://www.koreajoongangdaily.com/business/ncsofts-change-on-display-with-throne-and-liberty/10552706", "evidence_summary": "Throne and Liberty passed 4m global users after the Amazon Games launch. User adoption was real, but monetization/retention quality and later drawdown make it a Stage2-Watch or high-MAE case, not Stage3.", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-28", "entry_price": 210500.0, "MFE_30D_pct": 17.81, "MAE_30D_pct": -10.45, "MFE_90D_pct": 17.81, "MAE_90D_pct": -25.27, "MFE_180D_pct": 17.81, "MAE_180D_pct": -36.06, "forward_window_trading_days": 180, "peak_180D_date": "2024-12-03", "peak_180D_price": 248000.0, "trough_180D_date": "2025-04-09", "trough_180D_price": 134600.0, "corporate_action_window_status": "not_contaminated_180D", "corporate_action_profile_note": "profile_corporate_actions_outside_180D_window: candidates 2003-07-30, 2003-08-13", "calibration_usable": true, "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION|036570|Stage2|2024-10-28", "reuse_reason": "new symbol or new trigger family inside C27", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "high_mae_guard_needed": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_prediction": "Stage2-Actionable risk if user-count overweighted", "proposed_shadow_profile_prediction": "Stage2-Watch until retention/monetization revenue appears", "raw_component_score_breakdown": {"eps_fcf_explosion": 32, "earnings_visibility": 39, "bottleneck_pricing_power": 36, "market_mispricing": 52, "valuation_rerating": 50, "capital_allocation": 18, "information_confidence": 58, "total_proxy": 65}}
{"row_type": "trigger", "case_id": "C27_L198_05_182360", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "symbol": "182360", "company_name": "큐브엔터", "company_name_en": "Cube Entertainment", "trigger_date": "2024-05-14", "trigger_type": "Stage2-Actionable", "trigger_family": "Q1 record result from (G)I-DLE album/IP + distribution subsidiary", "case_role": "ip_monetization_positive", "case_polarity": "positive", "current_profile_error": true, "evidence_url": "https://www.mk.co.kr/en/stock/11014513", "evidence_summary": "Cube reported record Q1 2024 sales and operating profit, tied to (G)I-DLE album/IP sales and subsidiary distribution. It is a usable positive, but 90D MAE warns against Green without second-quarter confirmation.", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-14", "entry_price": 14630.0, "MFE_30D_pct": 8.89, "MAE_30D_pct": -6.77, "MFE_90D_pct": 8.89, "MAE_90D_pct": -25.22, "MFE_180D_pct": 23.1, "MAE_180D_pct": -25.22, "forward_window_trading_days": 180, "peak_180D_date": "2024-12-02", "peak_180D_price": 18010.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 10940.0, "corporate_action_window_status": "not_contaminated_180D", "corporate_action_profile_note": "profile_corporate_actions_outside_180D_window: candidates before 2022 only", "calibration_usable": true, "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION|182360|Stage2-Actionable|2024-05-14", "reuse_reason": "new symbol or new trigger family inside C27", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "high_mae_guard_needed": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_prediction": "Stage2-Actionable", "proposed_shadow_profile_prediction": "Stage2-Actionable, Green blocked until repeat tour/album margin confirmation", "raw_component_score_breakdown": {"eps_fcf_explosion": 59, "earnings_visibility": 60, "bottleneck_pricing_power": 44, "market_mispricing": 49, "valuation_rerating": 43, "capital_allocation": 20, "information_confidence": 69, "total_proxy": 74}}
{"row_type": "trigger", "case_id": "C27_L198_06_419530", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "symbol": "419530", "company_name": "SAMG엔터", "company_name_en": "SAMG Entertainment", "trigger_date": "2024-07-12", "trigger_type": "Stage2-Actionable", "trigger_family": "Teenieping movie MD + China distribution setup", "case_role": "kids_ip_md_movie_positive", "case_polarity": "positive", "current_profile_error": false, "evidence_url": "https://www.asiae.co.kr/en/article/2024071110021997503", "evidence_summary": "The Heartsping/Teenieping movie + toy MD + China release setup had a clean IP-to-products-to-distribution bridge, and the price path shows extreme MFE with negligible early MAE.", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 9740.0, "MFE_30D_pct": 47.74, "MAE_30D_pct": -0.31, "MFE_90D_pct": 101.54, "MAE_90D_pct": -0.31, "MFE_180D_pct": 264.48, "MAE_180D_pct": -0.31, "forward_window_trading_days": 180, "peak_180D_date": "2025-04-11", "peak_180D_price": 35500.0, "trough_180D_date": "2024-07-15", "trough_180D_price": 9710.0, "corporate_action_window_status": "not_contaminated_180D", "corporate_action_profile_note": "profile_corporate_actions_clean: no candidates", "calibration_usable": true, "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION|419530|Stage2-Actionable|2024-07-12", "reuse_reason": "new symbol or new trigger family inside C27", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "high_mae_guard_needed": false, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_prediction": "Stage2-Actionable", "proposed_shadow_profile_prediction": "Stage3-Yellow with event-cap exit guard after MD/reorder confirmation", "raw_component_score_breakdown": {"eps_fcf_explosion": 52, "earnings_visibility": 67, "bottleneck_pricing_power": 41, "market_mispricing": 64, "valuation_rerating": 57, "capital_allocation": 25, "information_confidence": 72, "total_proxy": 78}}
{"row_type": "trigger", "case_id": "C27_L198_07_086980", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "symbol": "086980", "company_name": "쇼박스", "company_name_en": "Showbox", "trigger_date": "2024-02-23", "trigger_type": "Stage2-Actionable", "trigger_family": "Exhuma opening-day record theatrical hit", "case_role": "film_hit_distribution_positive", "case_polarity": "positive", "current_profile_error": false, "evidence_url": "https://www.koreajoongangdaily.com/entertainment/exhuma-summons-record-number-of-moviegoers-for-release-day-in-2024/11743973", "evidence_summary": "Exhuma had the strongest 2024 opening-day box office in Korea at the trigger. This is a real film-distribution hit bridge, but the event still needs an event-cap/4B overlay because film hits are naturally finite.", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 3840.0, "MFE_30D_pct": 18.36, "MAE_30D_pct": -5.86, "MFE_90D_pct": 18.36, "MAE_90D_pct": -17.06, "MFE_180D_pct": 31.51, "MAE_180D_pct": -17.06, "forward_window_trading_days": 180, "peak_180D_date": "2024-11-04", "peak_180D_price": 5050.0, "trough_180D_date": "2024-07-04", "trough_180D_price": 3185.0, "corporate_action_window_status": "not_contaminated_180D", "corporate_action_profile_note": "profile_corporate_actions_outside_180D_window: candidate 2011-05-17", "calibration_usable": true, "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION|086980|Stage2-Actionable|2024-02-23", "reuse_reason": "new symbol or new trigger family inside C27", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "high_mae_guard_needed": false, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_prediction": "Stage2-Actionable", "proposed_shadow_profile_prediction": "Stage2-Actionable + explicit event-cap 4B overlay", "raw_component_score_breakdown": {"eps_fcf_explosion": 47, "earnings_visibility": 58, "bottleneck_pricing_power": 34, "market_mispricing": 51, "valuation_rerating": 49, "capital_allocation": 22, "information_confidence": 68, "total_proxy": 73}}
{"row_type": "trigger", "case_id": "C27_L198_08_078340", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "symbol": "078340", "company_name": "컴투스", "company_name_en": "Com2uS", "trigger_date": "2025-02-13", "trigger_type": "Stage2", "trigger_family": "FY2024 operating profit turnaround but revenue down/net loss and weak forward path", "case_role": "profit_turnaround_low_alpha_counterexample", "case_polarity": "counterexample", "current_profile_error": true, "evidence_url": "https://pulse.mk.co.kr/news/english/11239998", "evidence_summary": "Com2uS returned to operating profit in 2024, but annual revenue declined and net loss remained large. The path had low MFE and deep MAE, showing that profit-turnaround vocabulary alone is not enough for C27.", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-02-13", "entry_price": 49050.0, "MFE_30D_pct": 2.75, "MAE_30D_pct": -15.39, "MFE_90D_pct": 2.75, "MAE_90D_pct": -27.52, "MFE_180D_pct": 2.75, "MAE_180D_pct": -33.23, "forward_window_trading_days": 180, "peak_180D_date": "2025-02-20", "peak_180D_price": 50400.0, "trough_180D_date": "2025-11-07", "trough_180D_price": 32750.0, "corporate_action_window_status": "not_contaminated_180D", "corporate_action_profile_note": "profile_corporate_actions_outside_180D_window: candidate 2007-07-18", "calibration_usable": true, "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION|078340|Stage2|2025-02-13", "reuse_reason": "new symbol or new trigger family inside C27", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "high_mae_guard_needed": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_prediction": "Stage2-Watch", "proposed_shadow_profile_prediction": "Stage2-Watch or false-positive block until revenue growth/net income bridge", "raw_component_score_breakdown": {"eps_fcf_explosion": 38, "earnings_visibility": 35, "bottleneck_pricing_power": 32, "market_mispricing": 45, "valuation_rerating": 42, "capital_allocation": 20, "information_confidence": 62, "total_proxy": 60}}
```

## 9. Machine-readable Score Simulation Rows

```jsonl
{"row_type": "score_simulation", "case_id": "C27_L198_01_225570", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "current_profile_prediction": "Stage2-Actionable", "proposed_shadow_profile_prediction": "Stage2-Actionable + mandatory 4B exit after launch spike", "raw_component_score_breakdown": {"eps_fcf_explosion": 42, "earnings_visibility": 55, "bottleneck_pricing_power": 38, "market_mispricing": 62, "valuation_rerating": 65, "capital_allocation": 24, "information_confidence": 64, "total_proxy": 76}, "score_return_alignment": "good"}
{"row_type": "score_simulation", "case_id": "C27_L198_02_225570", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "current_profile_prediction": "Stage2-Actionable if launch success overweighted", "proposed_shadow_profile_prediction": "Stage4B late-entry/high-MAE block", "raw_component_score_breakdown": {"eps_fcf_explosion": 35, "earnings_visibility": 44, "bottleneck_pricing_power": 36, "market_mispricing": 58, "valuation_rerating": 70, "capital_allocation": 18, "information_confidence": 66, "total_proxy": 64}, "score_return_alignment": "residual_error_or_guard_needed"}
{"row_type": "score_simulation", "case_id": "C27_L198_03_263750", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "current_profile_prediction": "Stage2-Watch, but price momentum can over-promote", "proposed_shadow_profile_prediction": "Stage2-Watch only; demo-only cannot be Actionable", "raw_component_score_breakdown": {"eps_fcf_explosion": 22, "earnings_visibility": 26, "bottleneck_pricing_power": 31, "market_mispricing": 55, "valuation_rerating": 57, "capital_allocation": 18, "information_confidence": 56, "total_proxy": 61}, "score_return_alignment": "residual_error_or_guard_needed"}
{"row_type": "score_simulation", "case_id": "C27_L198_04_036570", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "current_profile_prediction": "Stage2-Actionable risk if user-count overweighted", "proposed_shadow_profile_prediction": "Stage2-Watch until retention/monetization revenue appears", "raw_component_score_breakdown": {"eps_fcf_explosion": 32, "earnings_visibility": 39, "bottleneck_pricing_power": 36, "market_mispricing": 52, "valuation_rerating": 50, "capital_allocation": 18, "information_confidence": 58, "total_proxy": 65}, "score_return_alignment": "residual_error_or_guard_needed"}
{"row_type": "score_simulation", "case_id": "C27_L198_05_182360", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "current_profile_prediction": "Stage2-Actionable", "proposed_shadow_profile_prediction": "Stage2-Actionable, Green blocked until repeat tour/album margin confirmation", "raw_component_score_breakdown": {"eps_fcf_explosion": 59, "earnings_visibility": 60, "bottleneck_pricing_power": 44, "market_mispricing": 49, "valuation_rerating": 43, "capital_allocation": 20, "information_confidence": 69, "total_proxy": 74}, "score_return_alignment": "good"}
{"row_type": "score_simulation", "case_id": "C27_L198_06_419530", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "current_profile_prediction": "Stage2-Actionable", "proposed_shadow_profile_prediction": "Stage3-Yellow with event-cap exit guard after MD/reorder confirmation", "raw_component_score_breakdown": {"eps_fcf_explosion": 52, "earnings_visibility": 67, "bottleneck_pricing_power": 41, "market_mispricing": 64, "valuation_rerating": 57, "capital_allocation": 25, "information_confidence": 72, "total_proxy": 78}, "score_return_alignment": "good"}
{"row_type": "score_simulation", "case_id": "C27_L198_07_086980", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "current_profile_prediction": "Stage2-Actionable", "proposed_shadow_profile_prediction": "Stage2-Actionable + explicit event-cap 4B overlay", "raw_component_score_breakdown": {"eps_fcf_explosion": 47, "earnings_visibility": 58, "bottleneck_pricing_power": 34, "market_mispricing": 51, "valuation_rerating": 49, "capital_allocation": 22, "information_confidence": 68, "total_proxy": 73}, "score_return_alignment": "good"}
{"row_type": "score_simulation", "case_id": "C27_L198_08_078340", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_GATE_V3_shadow", "rollback_reference_profile_id": "e2r_2_0_baseline_reference", "current_profile_prediction": "Stage2-Watch", "proposed_shadow_profile_prediction": "Stage2-Watch or false-positive block until revenue growth/net income bridge", "raw_component_score_breakdown": {"eps_fcf_explosion": 38, "earnings_visibility": 35, "bottleneck_pricing_power": 32, "market_mispricing": 45, "valuation_rerating": 42, "capital_allocation": 20, "information_confidence": 62, "total_proxy": 60}, "score_return_alignment": "residual_error_or_guard_needed"}
```

## 10. Aggregate / Shadow / Residual Rows

```jsonl
{"row_type": "aggregate", "selected_round": "R8", "selected_loop": 198, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "C27_GAME_MOVIE_KIDS_IP_LIVEOPS_RETAINED_ECONOMICS_LEAF_V3", "calibration_usable_trigger_count": 8, "representative_trigger_count": 8, "new_independent_case_count": 8, "positive_case_count": 4, "counterexample_count": 4, "current_profile_error_count": 5, "high_mae_guard_needed_count": 6, "index_baseline_coverage_before": "C27 rows 48", "index_baseline_coverage_after_if_accepted": "C27 rows 56", "session_aware_after_loop156_loop181_loop198_if_accepted": "about C27 rows 71", "loop_contribution_label": "canonical_archetype_rule_candidate", "rule_candidate": "C27_GAME_LIVEOPS_BOXOFFICE_RETAINED_ECONOMICS_AND_EVENT_CAP_GATE_V3"}
{"row_type": "shadow_weight_candidate", "selected_round": "R8", "selected_loop": 198, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "do_not_propose_new_weight_delta": false, "new_axis_proposed": "c27_retained_economics_liveops_revenue_bridge_and_event_cap_gate_v3", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_should_not_fire_on_demo_only_or_single_title_drawdown_without_irreversible_thesis_break", "proposal": "Require retained-economics bridge for C27 Actionable: liveops retention/revenue, box-office distributor economics, MD/reorder, platform share, or repeat monetization. Apply event-cap/high-MAE guard to one-hit launches, demos, and post-rerating earnings headlines."}
{"row_type": "residual_contribution", "selected_round": "R8", "selected_loop": 198, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "residual_error_found": true, "residual_error_count": 5, "main_false_positive_modes": ["demo_only_without_revenue_timing", "late_launch_success_after_price_rerating", "user_count_without_retention_monetization", "profit_turnaround_with_revenue_decline_net_loss"], "main_missed_or_underprotected_success_modes": ["kids_ip_md_movie_reorder_bridge", "film_hit_distribution_economics", "new_live-service_launch_with_clear_top-seller_traction"], "next_recommended_archetypes": ["C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM"]}
```

## 11. Batch Ingest Self-Audit

```text
expected_v12_result_file = true
filename_pattern_pass = true
metadata_filename_consistency = pass
jsonl_trigger_row_count = 8
calibration_usable_trigger_count = 8
representative_trigger_count = 8
new_weight_evidence_candidate_count = 8
guardrail_candidate_count = 6
narrative_only_or_rejected_count = 0
rows_missing_required_mfe_mae = 0
rows_missing_entry_price_or_date = 0
rows_with_noncanonical_trigger_type = 0
rows_with_compact_mfe_mae_alias_only = 0
ready_for_batch_ingest = true
```

## 12. Residual Contribution Summary

This loop adds 8 new independent C27 trigger rows, 4 counterexamples, and 5 residual errors for `R8 / L8_PLATFORM_CONTENT_SW_SECURITY / C27_CONTENT_IP_GLOBAL_MONETIZATION`.

The important new C27 compression is simple: **content/IP attention is not the same as retained economics**. A demo, trailer, opening weekend, or user-count headline is like a crowded lobby. It matters, but E2R should wait until the crowd buys tickets, repeats purchases, renews subscriptions, or lifts operating profit before opening Stage2-Actionable.

## 13. Deferred Coding Agent Handoff Prompt — Do Not Execute In This Research Session

```text
You are a coding agent working inside stock_agent after the research batch has been accepted.
Do not use this prompt unless the user explicitly starts a coding/refactor session.

Input artifact:
- e2r_stock_web_v12_residual_round_R8_loop_198_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md

Task:
1. Parse machine-readable trigger rows.
2. Validate filename, round, large_sector_id, canonical_archetype_id, entry_date, entry_price, MFE/MAE fields, and corporate_action_window_status.
3. Add the trigger rows to the v12 calibration ingest queue only if schema validation passes.
4. Consider a shadow-only C27 rule candidate:
   C27_RETAINED_ECONOMICS_LIVEOPS_REVENUE_BRIDGE_AND_EVENT_CAP_GATE_V3.
5. Do not globally change Stage2/Green thresholds.
6. Do not weaken 4B/4C global guards.
7. If implemented, scope the change to C27 only and require retained-economics evidence before Stage2-Actionable.
```

## 14. Next Research State

```text
completed_round = R8
completed_loop = 198
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
