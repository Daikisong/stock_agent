# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 35
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This file is historical calibration research only. It is not a current stock scan, not a live watchlist, and not an investment recommendation. The research question is whether content-IP global monetization cycles need a C27-specific shadow guard after the first Stock-Web global calibration.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The current profile already improved the broad Stage2/Green/4B/4C calibration. This loop does not repeat that global proof. It asks a more surgical question: in C27 content-IP cycles, when does “global hit” become repeatable monetization, and when is it just an event cap wearing a growth mask?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 35
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION
loop_objective = holdout_validation | residual_false_positive_mining | yellow_threshold_stress_test | green_strictness_stress_test | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill
```

Canonical compression:

- **C27_CONTENT_IP_GLOBAL_MONETIZATION** covers drama/movie/game/content IP whose economics rerate only when public interest becomes repeatable platform/customer monetization.
- This loop deliberately mixes positive cases and counterexample cases. The mechanism is not “content hit = buy signal.” The mechanism is “content hit + repeatable monetization bridge + credible customer/platform channel = Stage2/Stage3 candidate.”

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifact access was used only for coverage and duplication context. The ingest summary shows 107 parsed result MDs, 1,940 validated trigger rows, 1,376 aggregate representative rows, and all R1~R13 sectors already covered. This loop therefore uses a new v12 taxonomy pair and does not re-materialize an existing R1~R13 prompt loop.

No exact C27 canonical row was found in the prior artifact search. The cases below are treated as new independent cases for v12 residual research.

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest confirms:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema basis:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative triggers in this loop satisfy:

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
OHLCV_present = true
MFE_30D_90D_180D_and_MAE_30D_90D_180D_computed = true
corporate_action_contaminated_180D_window = false
```

Symbol profile caveats:

|symbol|company|profile summary|corporate-action status for tested window|
|---|---|---|---|
|253450|스튜디오드래곤|2017-11-24~2026-02-20, 2,020 tradable rows, no corporate-action candidates|clean_180D_window|
|293490|카카오게임즈|2020-09-10~2026-02-20, 1,333 tradable rows, no corporate-action candidates|clean_180D_window|
|036420|콘텐트리중앙|2000-03-23~2026-02-20, corporate-action candidates end before tested 2021/2022 window|clean_180D_window|
|160550|NEW|2014-12-23~2026-02-20, corporate-action candidates in 2015 only; tested 2016 window is after them|clean_180D_window|

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION
```

Compression rule:

- **Positive structural route**: global/platform customer evidence, repeatable IP or game/content monetization route, early revenue/revision route, and clean 180D price response.
- **Counterexample route**: single-title/event-driven excitement, weak repeatability, no durable customer or margin bridge, and poor forward MFE/MAE if labelled Green after the hit.
- **4B route**: valuation/positioning/event cap once the cycle is priced around the title/release rather than around durable library economics.
- **4C route**: the event/release thesis breaks, not necessarily the whole company. In content names the thesis can break without a formal cancellation event.

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|notes|
|---|---|---|---|---|---|---|---|
|C27_253450_STUDIO_DRAGON_2020|253450|스튜디오드래곤|structural_success|positive|C27_253450_20200508_S2_NETFLIX_SCALE|current_profile_correct|Clean 180D window; no corporate-action dates in profile.|
|C27_293490_KAKAOGAMES_ODIN_2021|293490|카카오게임즈|structural_success|positive|C27_293490_20210629_S2_ODIN_LAUNCH|current_profile_correct|Clean 180D window; no corporate-action dates in profile.|
|C27_036420_CONTENTREE_2021|036420|콘텐트리중앙|structural_success|positive|C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE|current_profile_correct|No profile corporate-action candidates after 2019; 2021/2022 window clean by profile rule.|
|C27_160550_NEW_SINGLE_HIT_2016|160550|NEW|false_positive_green|counterexample|C27_160550_20160324_GREEN_FALSE_POSITIVE|current_profile_false_positive|2016 window is after 2015 corporate-action candidates; clean 180D by profile rule.|


## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 3
counterexample_or_failed_rerating = 1
4B_or_4C_case_count = 3
minimum_calibration_usable_case_count = 4
new_independent_case_ratio = 1.00
```

The balance is intentionally tilted toward “what makes C27 work” while keeping one clean false-positive guard. The counterexample is important: content-IP charts can look like structural rerating for a few weeks, but without repeatable monetization the signal is more like a firework than a furnace.

## 9. Evidence Source Map

|case_id|evidence family|Stage2 evidence|Stage3 evidence|4B/4C evidence|source type|
|---|---|---|---|---|---|
|C27_253450_STUDIO_DRAGON_2020|OTT/global drama studio route|customer/platform demand, global content route|later financial/revision confirmation|valuation near Jan 2021 peak|public news/filings + stock-web OHLC|
|C27_293490_KAKAOGAMES_ODIN_2021|game IP platform monetization|launch/top-grossing route, relative strength|later revenue/revision confirmation|valuation and one-title concentration|public news/filings + stock-web OHLC|
|C27_036420_CONTENTREE_2021|OTT drama route plus event cap|global release route and momentum|financial visibility mixed|release-week event cap, reversal, 4C protection|public news/filings + stock-web OHLC|
|C27_160550_NEW_SINGLE_HIT_2016|single-title hit counterexample|hit buzz and relative strength|weak repeatability, no durable bridge|event cap and fade|public news/filings + stock-web OHLC|

## 10. Price Data Source Map

|trigger_id|symbol|entry_date|entry_price|price_shard_path|profile_path|corporate_action_window_status|
|---|---|---|---|---|---|---|
|C27_253450_20200508_S2_NETFLIX_SCALE|253450|2020-05-08|78200|atlas/ohlcv_tradable_by_symbol_year/253/253450/2020.csv|atlas/symbol_profiles/253/253450.json|clean_180D_window|
|C27_253450_20210120_GREEN_LATE|253450|2021-01-20|106900|atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv|atlas/symbol_profiles/253/253450.json|clean_180D_window|
|C27_293490_20210629_S2_ODIN_LAUNCH|293490|2021-06-29|59700|atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv|atlas/symbol_profiles/293/293490.json|clean_180D_window|
|C27_293490_20211116_4B_VALUATION_POSITIONING|293490|2021-11-16|108700|atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv|atlas/symbol_profiles/293/293490.json|clean_180D_window|
|C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE|036420|2021-09-24|46700|atlas/ohlcv_tradable_by_symbol_year/036/036420/2021.csv|atlas/symbol_profiles/036/036420.json|clean_180D_window|
|C27_036420_20211118_4B_EVENT_CAP|036420|2021-11-18|71900|atlas/ohlcv_tradable_by_symbol_year/036/036420/2021.csv|atlas/symbol_profiles/036/036420.json|clean_180D_window|
|C27_036420_20211123_4C_EVENT_REVERSAL|036420|2021-11-23|58300|atlas/ohlcv_tradable_by_symbol_year/036/036420/2021.csv|atlas/symbol_profiles/036/036420.json|clean_180D_window|
|C27_160550_20160324_GREEN_FALSE_POSITIVE|160550|2016-03-24|16150|atlas/ohlcv_tradable_by_symbol_year/160/160550/2016.csv|atlas/symbol_profiles/160/160550.json|clean_180D_window|


## 11. Case-by-Case Trigger Grid

|trigger_id|case_id|symbol|trigger_type|trigger_date|entry_date|entry_price|evidence_available_at_that_date|trigger_outcome_label|current_profile_verdict|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|---|---|
|C27_253450_20200508_S2_NETFLIX_SCALE|C27_253450_STUDIO_DRAGON_2020|253450|Stage2-Actionable|2020-05-08|2020-05-08|78200|Netflix/global OTT demand plus repeatable drama studio library; clear platform monetization route but revision confirmation not yet full Green.|structural_upside_realized|current_profile_correct|representative|
|C27_253450_20210120_GREEN_LATE|C27_253450_STUDIO_DRAGON_2020|253450|Stage3-Green|2021-01-20|2021-01-20|106900|Later confirmation after valuation had already repriced; used only as Green lateness comparison.|late_green_low_forward_upside|current_profile_too_late|label_comparison_only|
|C27_293490_20210629_S2_ODIN_LAUNCH|C27_293490_KAKAOGAMES_ODIN_2021|293490|Stage2-Actionable|2021-06-29|2021-06-29|59700|Odin domestic launch/top-grossing route: a single game IP with direct platform monetization and visible revenue acceleration route.|structural_upside_realized_high_MFE|current_profile_correct|representative|
|C27_293490_20211116_4B_VALUATION_POSITIONING|C27_293490_KAKAOGAMES_ODIN_2021|293490|Stage4B|2021-11-16|2021-11-16|108700|Post-launch valuation/positioning blowoff with one-title concentration; upside near full-window peak but thesis not yet broken.|4B_overlay_protected_from_full_cycle_drawdown|current_profile_correct|4B_overlay_only|
|C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE|C27_036420_CONTENTREE_2021|036420|Stage2-Actionable|2021-09-24|2021-09-24|46700|Global OTT drama route visible before full earnings conversion; IP momentum plus theater reopening optionality but execution risk remains.|high_MFE_high_event_risk|current_profile_correct|representative|
|C27_036420_20211118_4B_EVENT_CAP|C27_036420_CONTENTREE_2021|036420|Stage4B|2021-11-18|2021-11-18|71900|Event-cap/valuation overlay before/around global-content release week; 4B overlay, not automatic thesis break.|4B_overlay_reduced_drawdown_but_not_peak_timed|current_profile_4B_too_late|4B_overlay_only|
|C27_036420_20211123_4C_EVENT_REVERSAL|C27_036420_CONTENTREE_2021|036420|Stage4C|2021-11-23|2021-11-23|58300|Post-event reversal: price response and event-cap evidence showed monetization expectations had been over-discounted; thesis not cancelled but rerating thesis damaged.|4C_protection_success|current_profile_4C_too_late|4C_overlay_only|
|C27_160550_20160324_GREEN_FALSE_POSITIVE|C27_160550_NEW_SINGLE_HIT_2016|160550|Stage3-Green|2016-03-24|2016-03-24|16150|Single-title hit after the move; lacked repeatable IP pipeline, durable customer confirmation, and margin bridge. Outcome shows Green should not be granted on hit buzz alone.|false_positive_green_single_hit_fade|current_profile_false_positive|representative|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|calibration_usable|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C27_253450_20200508_S2_NETFLIX_SCALE|78200|8.95|20.2|44.5|-3.71|-3.71|-3.71|2021-01-21|113000|-28.5|True|
|C27_253450_20210120_GREEN_LATE|106900|5.71|5.71|5.71|-14.87|-14.87|-28.5|2021-01-21|113000|-28.5|True|
|C27_293490_20210629_S2_ODIN_LAUNCH|59700|77.55|77.55|94.3|-6.87|-6.87|-6.87|2021-11-17|116000|-53.19|True|
|C27_293490_20211116_4B_VALUATION_POSITIONING|108700|6.72|6.72|6.72|-21.07|-41.21|-50.05|2021-11-17|116000|-53.19|True|
|C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE|46700|53.53|83.94|83.94|-0.32|-3.0|-13.92|2021-11-22|85900|-53.2|True|
|C27_036420_20211118_4B_EVENT_CAP|71900|19.47|19.47|19.47|-36.99|-43.12|-44.09|2021-11-22|85900|-53.2|True|
|C27_036420_20211123_4C_EVENT_REVERSAL|58300|2.4|11.49|11.49|-22.3|-30.87|-31.05|2022-01-21|65000|-38.15|True|
|C27_160550_20160324_GREEN_FALSE_POSITIVE|16150|5.88|5.88|5.88|-27.24|-35.29|-35.29|2016-03-24|17100|-38.89|True|


Aggregate representative rows only:

```text
representative_trigger_count = 4
avg_MFE_90D_pct = 46.89
avg_MAE_90D_pct = -12.22
avg_MFE_180D_pct = 57.16
avg_MAE_180D_pct = -14.95
```

## 13. Current Calibrated Profile Stress Test

|question|stress-test answer|
|---|---|
|How would the current calibrated profile judge these cases?|It catches early Stage2 in StudioDragon/KakaoGames/Contentree, but still needs a C27 guard against single-title Green and event-cap 4B/4C lateness.|
|Did the judgment match MFE/MAE?|Mostly yes for Stage2; no for late Green / post-hit Green / event-cap 4C.|
|Was Stage2 bonus too high or too low?|Appropriate when platform/customer monetization route exists; too high if applied to content buzz without repeatability.|
|Was Yellow 75 too high or low?|Appropriate as a C27 waypoint. Yellow should hold ambiguous event-driven IP until repeatability is clear.|
|Was Green 87 / revision 55 too high or low?|Numerically fine, but C27 needs a qualitative Green guard: durable customer/platform monetization or margin bridge required.|
|Was price-only blowoff guard appropriate?|Yes, kept. This loop proposes non-price event-cap 4B, not price-only 4B.|
|Was full 4B non-price requirement appropriate?|Yes, strengthened. Event-cap / valuation / positioning count as non-price evidence.|
|Was hard 4C routing too late or too strict?|Too late if it waits for formal cancellation; C27 can break via event-cap rerating failure.|

Current profile verdict distribution:

```text
current_profile_correct = 3 trigger rows
current_profile_too_late = 1 trigger row
current_profile_4B_too_late = 1 trigger row
current_profile_4C_too_late = 1 trigger row
current_profile_false_positive = 1 trigger row
current_profile_error_count = 4
```

## 14. Stage2 / Yellow / Green Comparison

Stage2 worked when the evidence had a real channel into monetization:

- StudioDragon: platform/customer route was visible before full confirmation; Stage2 got the move early.
- KakaoGames: launch/top-grossing route turned into a strong 180D MFE, but it later demanded 4B risk control.
- Contentree: global content route produced a high MFE but also carried release-week event risk.

Green became dangerous when it arrived after the title had already been repriced:

- StudioDragon Green-like confirmation around 2021-01-20 had a green_lateness_ratio of **0.88**, near the observed 180D peak.
- NEW post-hit Green on 2016-03-24 had **5.88% MFE_90D** and **-35.29% MAE_90D**, a clear false-positive Green.

C27 implication:

```text
Do not lower global Green thresholds.
Add a C27 qualitative Green gate:
  durable customer/platform monetization OR repeatable IP library/portfolio evidence OR margin bridge must be present.
Single-title buzz + relative strength cannot become Green.
```

## 15. 4B Local vs Full-window Timing Audit

|trigger_id|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_timing_verdict|four_b_evidence_type|current_profile_verdict|
|---|---|---|---|---|---|
|C27_253450_20200508_S2_NETFLIX_SCALE|null|null|not_applicable||current_profile_correct|
|C27_253450_20210120_GREEN_LATE|null|null|late_green_near_peak_not_full_4B|valuation_blowoff|current_profile_too_late|
|C27_293490_20210629_S2_ODIN_LAUNCH|null|null|not_applicable||current_profile_correct|
|C27_293490_20211116_4B_VALUATION_POSITIONING|0.87|0.87|good_full_window_4B_timing|valuation_blowoff, positioning_overheat|current_profile_correct|
|C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE|null|null|not_applicable||current_profile_correct|
|C27_036420_20211118_4B_EVENT_CAP|0.64|0.64|non_price_4B_watch_slightly_early_vs_full_peak|valuation_blowoff, explicit_event_cap|current_profile_4B_too_late|
|C27_036420_20211123_4C_EVENT_REVERSAL|null|null|4C_after_event_reversal|explicit_event_cap|current_profile_4C_too_late|
|C27_160550_20160324_GREEN_FALSE_POSITIVE|0.95|0.95|good_4B_not_positive_promotion|valuation_blowoff, explicit_event_cap|current_profile_false_positive|


Key interpretation:

- KakaoGames 2021-11-16 had **four_b_full_window_peak_proximity = 0.87**, good full-window 4B timing. It was not price-only; evidence included valuation, positioning, and one-title concentration.
- Contentree 2021-11-18 had **0.64**, slightly early relative to the full-window peak, but useful as 4B watch because release-week event cap was non-price evidence.
- NEW 2016-03-24 is not a positive promotion. Its near-peak Green label should be rerouted to 4B-watch or no-positive-stage.

## 16. 4C Protection Audit

|case_id|4C trigger|label|interpretation|
|---|---|---|---|
|C27_036420_CONTENTREE_2021|C27_036420_20211123_4C_EVENT_REVERSAL|hard_4c_success|Event-cap rerating failure protected against a later drawdown without requiring formal cancellation.|
|C27_160550_NEW_SINGLE_HIT_2016|C27_160550_20160324_GREEN_FALSE_POSITIVE|hard_4c_success / 4B-watch|The title hit did not create durable monetization; a C27 guard would block Green before 4C.|
|C27_293490_KAKAOGAMES_ODIN_2021|C27_293490_20211116_4B_VALUATION_POSITIONING|thesis_break_watch_only|4B overlay was enough; hard 4C was not yet justified at the peak.|

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = l8_event_cap_non_price_4b_overlay
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
proposal_type = sector_shadow_only
production_scoring_changed = false
```

Rule candidate:

> In L8 platform/content names, a release-week or launch-week event cap can count as non-price 4B evidence when valuation/positioning is stretched and the upside now depends on one title or one launch.

Why sector-specific rather than global:

- In content and games, the public catalyst often culminates at release/launch, not at delivery/backlog recognition.
- A content release can be “known good news” and still mark the end of the rerating window if the repeat-monetization bridge is weak.
- This is different from industrial backlog or financial ROE cycles, where event-cap logic should not be imported blindly.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = c27_repeatable_ip_monetization_gate
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
proposal_type = canonical_shadow_only
production_scoring_changed = false
```

C27 Green gate proposal:

```text
if content_IP_signal is based mainly on single-title buzz:
    block Stage3-Green
    route to Stage2-watch or Stage4B-watch depending on valuation/positioning

if repeatable monetization evidence exists:
    allow Stage2-Actionable

if repeatable monetization + margin bridge + durable customer/platform confirmation exist:
    allow Stage3-Yellow/Green subject to existing thresholds
```

Evidence fields that should qualify:

- durable customer/platform confirmation
- repeat order, sequel, season, service contract, or library monetization
- visible margin bridge, revenue share, subscription/channel economics, or game revenue rank conversion
- low red-team risk after excluding one-title event cap

Evidence fields that should not qualify alone:

- one title trending
- chart rank / buzz without monetization bridge
- relative strength only
- price gap on release day

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|changed_thresholds|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_default|Global calibrated profile, no C27-specific residual rule.|none|none|4|46.89|-12.22|57.16|-14.95|1/4|0|1|0.94|0.82|0.82|good Stage2 capture; residual Green false-positive and late 4B/4C|
|P0b_e2r_2_0_baseline_reference|rollback_reference|Older profile likely over-promotes post-hit Green and underuses event-cap 4B.|rollback Stage2 bonus and 4B/4C guards|legacy|4|46.89|-12.22|57.16|-14.95|2/4 risk|1|2|1.0|0.7|0.7|worse; too much post-hit confirmation bias|
|P1_L8_sector_specific_candidate_profile|sector_specific|For L8 content/platform names, Stage2 may promote when platform monetization route and customer/channel quality are visible before revisions.|content_platform_monetization_route_bonus=+1; event_cap_4b_watch=+1|no production threshold change|4|46.89|-12.22|57.16|-14.95|1/4 before guard; 0/4 after guard|0|1|0.88|0.75|0.75|best sector fit; catches early route without promoting single-hit Green|
|P2_C27_archetype_candidate_profile|canonical_archetype_specific|C27 needs a repeatable-monetization gate: repeat customer/platform route + margin bridge > isolated buzz/ratings.|repeatable_ip_monetization_gate=required_for_Green; single_title_buzz_green_block=true|Green requires durable_customer_confirmation or margin_bridge; no numeric production change|4|46.89|-12.22|57.16|-14.95|0/4 after C27 guard|0|1|0.88|0.82|0.82|best canonical compression candidate|
|P3_counterexample_guard_profile|counterexample_guard|Any content-IP Green based on one title must be blocked unless repeat economics are proven.|single_title_event_cap_blocks_green=true; event_cap_routes_to_4B_or_4C=true|Green blocked if durable monetization unknown|4|46.89|-12.22|57.16|-14.95|0/4 on this loop|0|0|not_applicable|0.86|0.86|strong guard; risk is over-blocking early structural cases if applied globally|


## 20. Score-Return Alignment Matrix

|trigger_id|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|C27_253450_20200508_S2_NETFLIX_SCALE|76.0|Stage2-Actionable|79.5|Stage2-Actionable+|20.2|-3.71|structural_upside_realized|current_profile_correct|
|C27_253450_20210120_GREEN_LATE|88.0|Stage3-Green|85.5|Stage3-Yellow/4B-watch|5.71|-14.87|late_green_low_forward_upside|current_profile_too_late|
|C27_293490_20210629_S2_ODIN_LAUNCH|78.0|Stage2-Actionable|82.0|Stage2-Actionable+|77.55|-6.87|structural_upside_realized_high_MFE|current_profile_correct|
|C27_293490_20211116_4B_VALUATION_POSITIONING|91.0|Stage3-Green|92.0|Stage4B-overlay|6.72|-41.21|4B_overlay_protected_from_full_cycle_drawdown|current_profile_correct|
|C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE|77.0|Stage2-Actionable|76.0|Stage2-Actionable with 4B-watch|83.94|-3.0|high_MFE_high_event_risk|current_profile_correct|
|C27_036420_20211118_4B_EVENT_CAP|89.0|Stage3-Green/overheat|91.0|Stage4B-overlay|19.47|-43.12|4B_overlay_reduced_drawdown_but_not_peak_timed|current_profile_4B_too_late|
|C27_036420_20211123_4C_EVENT_REVERSAL|70.0|Stage4B-watch|58.0|Stage4C|11.49|-30.87|4C_protection_success|current_profile_4C_too_late|
|C27_160550_20160324_GREEN_FALSE_POSITIVE|87.0|Stage3-Green false-positive|70.0|Stage4B-watch / no Green|5.88|-35.29|false_positive_green_single_hit_fade|current_profile_false_positive|


Component interpretation:

- The proposed C27 adjustment does not create a new global score. It changes how C27 evidence is interpreted.
- Repeatable monetization raises the reliability of Stage2/Yellow.
- Single-title event caps increase 4B/4C risk and block Green.
- Relative strength remains useful only when it is tied to a monetization bridge.

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L8_PLATFORM_CONTENT_SW_SECURITY|C27_CONTENT_IP_GLOBAL_MONETIZATION|K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION|3|1|3|2|4|0|8|4|4|true|true|Need additional C27 samples from music/animation/webtoon and non-Korean global IP to validate portability.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - single_title_hit_false_positive_green
  - event_cap_4B_too_late
  - event_cap_4C_too_late
  - green_confirmation_lateness_in_content_IP
new_axis_proposed:
  - c27_repeatable_ip_monetization_gate
  - c27_single_title_event_cap_blocks_green
  - l8_event_cap_non_price_4b_overlay
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c, with C27 event-cap thesis break interpretation
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web actual 1D OHLCV rows from tradable shards.
- Entry date / entry price separation.
- 30D / 90D / 180D MFE and MAE for all usable trigger rows.
- Corporate-action window status by symbol profile.
- C27-specific score-return alignment using research proxy component scores.

Not validated:

- No current/live candidate scan.
- No current recommendation.
- No stock_agent source code or production scoring file was opened.
- No broker/API/autotrading work.
- No patch was written.
- No global production weight change is proposed.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_repeatable_ip_monetization_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Green requires repeatable platform/customer monetization, not one-title buzz.",Blocks NEW false-positive while retaining StudioDragon/KakaoGames/Contentree Stage2 routes.,C27_253450_20200508_S2_NETFLIX_SCALE|C27_293490_20210629_S2_ODIN_LAUNCH|C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE|C27_160550_20160324_GREEN_FALSE_POSITIVE,4,4,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c27_single_title_event_cap_blocks_green,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,Single-title event caps should route to 4B-watch/4C if forward monetization is not durable.,Reduces false Green and improves 4C timing for NEW/Contentree-type event cycles.,C27_160550_20160324_GREEN_FALSE_POSITIVE|C27_036420_20211123_4C_EVENT_REVERSAL,2,2,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,l8_event_cap_non_price_4b_overlay,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"In platform/content names, a release-week event cap is non-price 4B evidence if valuation/positioning is already stretched.",Improves drawdown control in Contentree and KakaoGames without using price-only 4B.,C27_293490_20211116_4B_VALUATION_POSITIONING|C27_036420_20211118_4B_EVENT_CAP,2,2,0,low_medium,sector_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C27_253450_STUDIO_DRAGON_2020", "symbol": "253450", "company_name": "스튜디오드래곤", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C27_253450_20200508_S2_NETFLIX_SCALE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 aligned; Green confirmation was late versus 180D peak.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Clean 180D window; no corporate-action dates in profile."}
{"row_type": "case", "case_id": "C27_293490_KAKAOGAMES_ODIN_2021", "symbol": "293490", "company_name": "카카오게임즈", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C27_293490_20210629_S2_ODIN_LAUNCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Launch evidence aligned strongly with 180D MFE; later 4B overlay was necessary.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Clean 180D window; no corporate-action dates in profile."}
{"row_type": "case", "case_id": "C27_036420_CONTENTREE_2021", "symbol": "036420", "company_name": "콘텐트리중앙", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Early IP-route trigger aligned, but event-cap 4B/4C needed to avoid drawdown.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "No profile corporate-action candidates after 2019; 2021/2022 window clean by profile rule."}
{"row_type": "case", "case_id": "C27_160550_NEW_SINGLE_HIT_2016", "symbol": "160550", "company_name": "NEW", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C27_160550_20160324_GREEN_FALSE_POSITIVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Post-hit Green would have been false-positive; event-cap guard required.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2016 window is after 2015 corporate-action candidates; clean 180D by profile rule."}
{"row_type": "trigger", "trigger_id": "C27_253450_20200508_S2_NETFLIX_SCALE", "case_id": "C27_253450_STUDIO_DRAGON_2020", "symbol": "253450", "company_name": "스튜디오드래곤", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content IP global monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-05-08", "evidence_available_at_that_date": "Netflix/global OTT demand plus repeatable drama studio library; clear platform monetization route but revision confirmation not yet full Green.", "evidence_source": "stock-web 253450 2020/2021 shards; public OTT/customer evidence available by trigger date", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253450/2020.csv", "profile_path": "atlas/symbol_profiles/253/253450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-05-08", "entry_price": 78200, "MFE_30D_pct": 8.95, "MFE_90D_pct": 20.2, "MFE_180D_pct": 44.5, "MFE_1Y_pct": 44.5, "MFE_2Y_pct": 44.5, "MAE_30D_pct": -3.71, "MAE_90D_pct": -3.71, "MAE_180D_pct": -3.71, "MAE_1Y_pct": -3.71, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2021-01-21", "peak_price": 113000, "drawdown_after_peak_pct": -28.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_upside_realized", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_253450_20200508", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_253450_20210120_GREEN_LATE", "case_id": "C27_253450_STUDIO_DRAGON_2020", "symbol": "253450", "company_name": "스튜디오드래곤", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content IP global monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2021-01-20", "evidence_available_at_that_date": "Later confirmation after valuation had already repriced; used only as Green lateness comparison.", "evidence_source": "stock-web 253450 2021 shard; later revision/public-source confirmation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv", "profile_path": "atlas/symbol_profiles/253/253450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-20", "entry_price": 106900, "MFE_30D_pct": 5.71, "MFE_90D_pct": 5.71, "MFE_180D_pct": 5.71, "MFE_1Y_pct": 5.71, "MFE_2Y_pct": 5.71, "MAE_30D_pct": -14.87, "MAE_90D_pct": -14.87, "MAE_180D_pct": -28.5, "MAE_1Y_pct": -36.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-01-21", "peak_price": 113000, "drawdown_after_peak_pct": -28.5, "green_lateness_ratio": 0.88, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "late_green_near_peak_not_full_4B", "four_b_evidence_type": ["valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_low_forward_upside", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_253450_20210120", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_293490_20210629_S2_ODIN_LAUNCH", "case_id": "C27_293490_KAKAOGAMES_ODIN_2021", "symbol": "293490", "company_name": "카카오게임즈", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content IP global monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-06-29", "evidence_available_at_that_date": "Odin domestic launch/top-grossing route: a single game IP with direct platform monetization and visible revenue acceleration route.", "evidence_source": "stock-web 293490 2021/2022 shards; public game launch/revenue-rank evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv", "profile_path": "atlas/symbol_profiles/293/293490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-06-29", "entry_price": 59700, "MFE_30D_pct": 77.55, "MFE_90D_pct": 77.55, "MFE_180D_pct": 94.3, "MFE_1Y_pct": 94.3, "MFE_2Y_pct": 94.3, "MAE_30D_pct": -6.87, "MAE_90D_pct": -6.87, "MAE_180D_pct": -6.87, "MAE_1Y_pct": -9.05, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-17", "peak_price": 116000, "drawdown_after_peak_pct": -53.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_upside_realized_high_MFE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_293490_20210629", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_293490_20211116_4B_VALUATION_POSITIONING", "case_id": "C27_293490_KAKAOGAMES_ODIN_2021", "symbol": "293490", "company_name": "카카오게임즈", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content IP global monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2021-11-16", "evidence_available_at_that_date": "Post-launch valuation/positioning blowoff with one-title concentration; upside near full-window peak but thesis not yet broken.", "evidence_source": "stock-web 293490 2021/2022 shards; valuation/positioning overlay evidence", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv", "profile_path": "atlas/symbol_profiles/293/293490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-16", "entry_price": 108700, "MFE_30D_pct": 6.72, "MFE_90D_pct": 6.72, "MFE_180D_pct": 6.72, "MFE_1Y_pct": 6.72, "MFE_2Y_pct": 6.72, "MAE_30D_pct": -21.07, "MAE_90D_pct": -41.21, "MAE_180D_pct": -50.05, "MAE_1Y_pct": -60.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-17", "peak_price": 116000, "drawdown_after_peak_pct": -53.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_protected_from_full_cycle_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_293490_20211116", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE", "case_id": "C27_036420_CONTENTREE_2021", "symbol": "036420", "company_name": "콘텐트리중앙", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content IP global monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-09-24", "evidence_available_at_that_date": "Global OTT drama route visible before full earnings conversion; IP momentum plus theater reopening optionality but execution risk remains.", "evidence_source": "stock-web 036420 2021/2022 shards; public global drama/OTT evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036420/2021.csv", "profile_path": "atlas/symbol_profiles/036/036420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-24", "entry_price": 46700, "MFE_30D_pct": 53.53, "MFE_90D_pct": 83.94, "MFE_180D_pct": 83.94, "MFE_1Y_pct": 83.94, "MFE_2Y_pct": 83.94, "MAE_30D_pct": -0.32, "MAE_90D_pct": -3.0, "MAE_180D_pct": -13.92, "MAE_1Y_pct": -30.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-22", "peak_price": 85900, "drawdown_after_peak_pct": -53.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_MFE_high_event_risk", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_036420_20210924", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_036420_20211118_4B_EVENT_CAP", "case_id": "C27_036420_CONTENTREE_2021", "symbol": "036420", "company_name": "콘텐트리중앙", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content IP global monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2021-11-18", "evidence_available_at_that_date": "Event-cap/valuation overlay before/around global-content release week; 4B overlay, not automatic thesis break.", "evidence_source": "stock-web 036420 2021/2022 shards; global-release event-cap evidence", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036420/2021.csv", "profile_path": "atlas/symbol_profiles/036/036420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-18", "entry_price": 71900, "MFE_30D_pct": 19.47, "MFE_90D_pct": 19.47, "MFE_180D_pct": 19.47, "MFE_1Y_pct": 19.47, "MFE_2Y_pct": 19.47, "MAE_30D_pct": -36.99, "MAE_90D_pct": -43.12, "MAE_180D_pct": -44.09, "MAE_1Y_pct": -55.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-22", "peak_price": 85900, "drawdown_after_peak_pct": -53.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.64, "four_b_full_window_peak_proximity": 0.64, "four_b_timing_verdict": "non_price_4B_watch_slightly_early_vs_full_peak", "four_b_evidence_type": ["valuation_blowoff", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_reduced_drawdown_but_not_peak_timed", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_036420_20211118", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_036420_20211123_4C_EVENT_REVERSAL", "case_id": "C27_036420_CONTENTREE_2021", "symbol": "036420", "company_name": "콘텐트리중앙", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content IP global monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C", "trigger_date": "2021-11-23", "evidence_available_at_that_date": "Post-event reversal: price response and event-cap evidence showed monetization expectations had been over-discounted; thesis not cancelled but rerating thesis damaged.", "evidence_source": "stock-web 036420 2021/2022 shards; post-event rerating failure evidence", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036420/2021.csv", "profile_path": "atlas/symbol_profiles/036/036420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-23", "entry_price": 58300, "MFE_30D_pct": 2.4, "MFE_90D_pct": 11.49, "MFE_180D_pct": 11.49, "MFE_1Y_pct": 11.49, "MFE_2Y_pct": 11.49, "MAE_30D_pct": -22.3, "MAE_90D_pct": -30.87, "MAE_180D_pct": -31.05, "MAE_1Y_pct": -45.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-21", "peak_price": 65000, "drawdown_after_peak_pct": -38.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "4C_after_event_reversal", "four_b_evidence_type": ["explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_protection_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_036420_20211123", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_160550_20160324_GREEN_FALSE_POSITIVE", "case_id": "C27_160550_NEW_SINGLE_HIT_2016", "symbol": "160550", "company_name": "NEW", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_IP_GLOBAL_PLATFORM_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content IP global monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2016-03-24", "evidence_available_at_that_date": "Single-title hit after the move; lacked repeatable IP pipeline, durable customer confirmation, and margin bridge. Outcome shows Green should not be granted on hit buzz alone.", "evidence_source": "stock-web 160550 2016 shard; public single-hit content evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/160/160550/2016.csv", "profile_path": "atlas/symbol_profiles/160/160550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2016-03-24", "entry_price": 16150, "MFE_30D_pct": 5.88, "MFE_90D_pct": 5.88, "MFE_180D_pct": 5.88, "MFE_1Y_pct": 5.88, "MFE_2Y_pct": 5.88, "MAE_30D_pct": -27.24, "MAE_90D_pct": -35.29, "MAE_180D_pct": -35.29, "MAE_1Y_pct": -45.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2016-03-24", "peak_price": 17100, "drawdown_after_peak_pct": -38.89, "green_lateness_ratio": 1.0, "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_4B_not_positive_promotion", "four_b_evidence_type": ["valuation_blowoff", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green_single_hit_fade", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_160550_20160324", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_253450_STUDIO_DRAGON_2020", "trigger_id": "C27_253450_20200508_S2_NETFLIX_SCALE", "symbol": "253450", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 4, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 4, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 5, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79.5, "stage_label_after": "Stage2-Actionable+", "changed_components": ["customer_quality_score", "revision_score", "valuation_repricing_score"], "component_delta_explanation": "C27 shadow adjustment: reward repeatable platform monetization; penalize single-hit/event-cap or concentration risk. Scores are research proxy only.", "MFE_90D_pct": 20.2, "MAE_90D_pct": -3.71, "score_return_alignment_label": "structural_upside_realized", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_253450_STUDIO_DRAGON_2020", "trigger_id": "C27_253450_20210120_GREEN_LATE", "symbol": "253450", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 8, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 8, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 85.5, "stage_label_after": "Stage3-Yellow/4B-watch", "changed_components": ["valuation_repricing_score"], "component_delta_explanation": "C27 shadow adjustment: reward repeatable platform monetization; penalize single-hit/event-cap or concentration risk. Scores are research proxy only.", "MFE_90D_pct": 5.71, "MAE_90D_pct": -14.87, "score_return_alignment_label": "late_green_low_forward_upside", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_293490_KAKAOGAMES_ODIN_2021", "trigger_id": "C27_293490_20210629_S2_ODIN_LAUNCH", "symbol": "293490", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82.0, "stage_label_after": "Stage2-Actionable+", "changed_components": ["relative_strength_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "C27 shadow adjustment: reward repeatable platform monetization; penalize single-hit/event-cap or concentration risk. Scores are research proxy only.", "MFE_90D_pct": 77.55, "MAE_90D_pct": -6.87, "score_return_alignment_label": "structural_upside_realized_high_MFE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_293490_KAKAOGAMES_ODIN_2021", "trigger_id": "C27_293490_20211116_4B_VALUATION_POSITIONING", "symbol": "293490", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 5, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 91.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 5, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 92.0, "stage_label_after": "Stage4B-overlay", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C27 shadow adjustment: reward repeatable platform monetization; penalize single-hit/event-cap or concentration risk. Scores are research proxy only.", "MFE_90D_pct": 6.72, "MAE_90D_pct": -41.21, "score_return_alignment_label": "4B_overlay_protected_from_full_cycle_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_036420_CONTENTREE_2021", "trigger_id": "C27_036420_20210924_S2_GLOBAL_DRAMA_ROUTE", "symbol": "036420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76.0, "stage_label_after": "Stage2-Actionable with 4B-watch", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C27 shadow adjustment: reward repeatable platform monetization; penalize single-hit/event-cap or concentration risk. Scores are research proxy only.", "MFE_90D_pct": 83.94, "MAE_90D_pct": -3.0, "score_return_alignment_label": "high_MFE_high_event_risk", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_036420_CONTENTREE_2021", "trigger_id": "C27_036420_20211118_4B_EVENT_CAP", "symbol": "036420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 89.0, "stage_label_before": "Stage3-Green/overheat", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 91.0, "stage_label_after": "Stage4B-overlay", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C27 shadow adjustment: reward repeatable platform monetization; penalize single-hit/event-cap or concentration risk. Scores are research proxy only.", "MFE_90D_pct": 19.47, "MAE_90D_pct": -43.12, "score_return_alignment_label": "4B_overlay_reduced_drawdown_but_not_peak_timed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_036420_CONTENTREE_2021", "trigger_id": "C27_036420_20211123_4C_EVENT_REVERSAL", "symbol": "036420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70.0, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58.0, "stage_label_after": "Stage4C", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C27 shadow adjustment: reward repeatable platform monetization; penalize single-hit/event-cap or concentration risk. Scores are research proxy only.", "MFE_90D_pct": 11.49, "MAE_90D_pct": -30.87, "score_return_alignment_label": "4C_protection_success", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_160550_NEW_SINGLE_HIT_2016", "trigger_id": "C27_160550_20160324_GREEN_FALSE_POSITIVE", "symbol": "160550", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 3, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 87.0, "stage_label_before": "Stage3-Green false-positive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 9, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70.0, "stage_label_after": "Stage4B-watch / no Green", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C27 shadow adjustment: reward repeatable platform monetization; penalize single-hit/event-cap or concentration risk. Scores are research proxy only.", "MFE_90D_pct": 5.88, "MAE_90D_pct": -35.29, "score_return_alignment_label": "false_positive_green_single_hit_fade", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "35", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["single_title_hit_false_positive_green", "event_cap_4B_too_late", "event_cap_4C_too_late", "green_confirmation_lateness_in_content_IP"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R13_loop_36
suggested_large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
suggested_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
suggested_objective = coverage_gap_fill + counterexample_mining + canonical_archetype_compression
reason = L8 still needs non-content platform/SW contract-retention coverage after C26 and C27.
```

## 28. Source Notes

Price atlas files inspected:

- atlas/manifest.json
- atlas/schema.json
- reports/e2r_calibration/ingest_summary.md for duplicate/coverage context only
- atlas/symbol_profiles/253/253450.json
- atlas/symbol_profiles/293/293490.json
- atlas/symbol_profiles/036/036420.json
- atlas/symbol_profiles/160/160550.json
- atlas/ohlcv_tradable_by_symbol_year/253/253450/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/293/293490/2022.csv
- atlas/ohlcv_tradable_by_symbol_year/036/036420/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/036/036420/2022.csv
- atlas/ohlcv_tradable_by_symbol_year/160/160550/2016.csv

Evidence source limitation:

This v12 MD records evidence families as public historical event/filing/news categories and uses stock-web for quantitative OHLC validation. It does not perform live candidate discovery and does not alter production scoring.
