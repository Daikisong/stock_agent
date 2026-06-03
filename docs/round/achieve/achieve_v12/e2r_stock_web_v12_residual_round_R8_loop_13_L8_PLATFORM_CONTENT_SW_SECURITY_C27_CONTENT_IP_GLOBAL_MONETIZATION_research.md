# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R8
scheduled_loop: 13
completed_round: R8
completed_loop: 13
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R8_loop_13_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption

The active proxy is `e2r_2_1_stock_web_calibrated_proxy`; the old `e2r_2_0_baseline_reference` is retained only as rollback context.

Already-applied global axes are not re-proposed as global changes. This MD stress-tests them inside C27 content IP monetization:

- `stage2_actionable_evidence_bonus = +2.0`
- `stage3_yellow_total_min = 75.0`
- `stage3_green_total_min = 87.0`
- `stage3_green_revision_min = 55.0`
- `stage3_cross_evidence_green_buffer = +1.5`
- `price_only_blowoff_blocks_positive_stage = true`
- `full_4b_requires_non_price_evidence = true`
- `hard_4c_thesis_break_routes_to_4c = true`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R8
loop = 13
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE
round_sector_consistency = pass
```

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`, and C27 is the scheduled-round-compatible content/IP canonical archetype. This is not an R13 cross-archetype red-team file.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact inspection was limited to calibration registry / by-round summaries. The repository registry shows older R8 historical calibration files through at least R8 loop 7/8, but no v12 residual filename matching `e2r_stock_web_v12_residual_round_R8_loop_*` was found in the repo search. The previous generated v12 next-state indicated `R8 / loop 13`, so this file uses that scheduled state.

Duplicate-avoidance stance:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
selected_symbols = 259960, 251270, 194480
new_independent_case_count = 3
reused_case_count = 0
new_trigger_family_count = 5
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields verified from `Songdaiki/stock-web/atlas/manifest.json`:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema basis:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Important caveat: OHLC is raw/unadjusted. Corporate-action-contaminated windows are not used for weight calibration.

## 5. Historical Eligibility Gate

|symbol|company|profile_path|entry rows|forward window|corporate_action_candidate_count|180D window status|calibration_usable|
|---|---|---|---|---|---:|---|---|
|259960|크래프톤|atlas/symbol_profiles/259/259960.json|2023-11-08 / 2024-02-13|504D available by manifest max date|0|clean_180D_window|true|
|251270|넷마블|atlas/symbol_profiles/251/251270.json|2024-05-08|180D available by manifest max date|0|clean_180D_window|true|
|194480|데브시스터즈|atlas/symbol_profiles/194/194480.json|2024-06-26 / 2024-07-04|180D available by manifest max date|0|clean_180D_window|true|

All representative cases have actual stock-web tradable rows and at least 180 forward trading days.

## 6. Canonical Archetype Compression Map

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
  ├─ GAME_IP_GLOBAL_LAUNCH
  ├─ WEBTOON_OR_ANIME_IP_TO_GAME_CONVERSION
  ├─ LIVE_SERVICE_IP_RETENTION_AND_ARPU
  ├─ LAUNCH_DAY_TRAFFIC_WITHOUT_RETENTION
  └─ POST_LAUNCH_REVERSAL_THESIS_BREAK
```

Compression finding: C27 should not treat "global launch / popular IP / download rank" as the same evidence family as "recurring monetization / retention / margin bridge." The first is an option; the second is the conversion.

## 7. Case Selection Summary

|case_id|symbol|company|case_role|positive_or_counterexample|best_trigger|current_profile_verdict|
|---|---|---|---|---|---|---|
|R8L13_C27_KRAFTON_BGMI_OPERATING_LEVERAGE_2023Q3|259960|크래프톤|structural_success|positive|3Q23 earnings and BGMI/PUBG live-service monetization bridge|current_profile_correct|
|R8L13_C27_NETMARBLE_SOLOLEVELING_LAUNCH_2024|251270|넷마블|stage2_promote_candidate|counterexample|Solo Leveling: ARISE global launch spike|current_profile_too_early|
|R8L13_C27_DEVSISTERS_COOKIE_TOWER_LAUNCH_2024|194480|데브시스터즈|false_positive_green|counterexample|CookieRun: Tower of Adventures launch-day spike|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
current_profile_error_count = 2
4B_case_count = 2
4C_case_count = 1
```

The sample is deliberately counterexample-heavy because C27's residual risk is not that good IP is ignored; it is that launch-day IP excitement can masquerade as monetization conversion.

## 9. Evidence Source Map

|symbol|evidence family|evidence available at trigger|stage evidence interpretation|
|---|---|---|---|
|259960|earnings + recurring live-service IP|3Q23 earnings / BGMI return / PUBG monetization context|Stage2-Actionable became valid because content IP tied to margin and revision bridge|
|251270|global game launch using major webtoon/anime IP|Solo Leveling: ARISE global launch / market attention|Stage2-Actionable only; retention and margin bridge not confirmed at entry|
|194480|new CookieRun title launch-day spike|CookieRun: Tower of Adventures release and launch-day price reaction|Launch-only evidence; not Green; quick 4C needed after reversal|

## 10. Price Data Source Map

Representative stock-web rows used:

```text
KRAFTON entry        2023-11-08,181200.0,193900.0,180300.0,190800.0,945555.0,178284086000.0,9227611364400.0,48362743,KOSPI
KRAFTON 30D peak     2023-12-04,217000.0,221500.0,216000.0,218000.0,83716.0,18329444000.0,10543077974000.0,48362743,KOSPI
KRAFTON 90D peak     2024-02-16,243000.0,243500.0,236000.0,237500.0,64520.0,15397264000.0,11486567087500.0,48364493,KOSPI
KRAFTON 180D peak    2024-07-30,289500.0,302000.0,289500.0,292500.0,99829.0,29478915000.0,14007942877500.0,47890403,KOSPI
KRAFTON low          2023-12-22,208500.0,208500.0,177000.0,178500.0,616485.0,115078583400.0,8632749625500.0,48362743,KOSPI
NETMARBLE entry      2024-05-08,59500.0,62600.0,58700.0,60700.0,422968.0,25711010200.0,5217377571400.0,85953502,KOSPI
NETMARBLE peak       2024-05-10,68500.0,72400.0,66500.0,69400.0,1732775.0,120218412400.0,5965173038800.0,85953502,KOSPI
NETMARBLE low        2024-06-24,53800.0,54500.0,52400.0,52800.0,119371.0,6345910000.0,4538344905600.0,85953502,KOSPI
DEVSISTERS entry     2024-06-26,65800.0,76300.0,65000.0,75700.0,2903920.0,212476711200.0,909412866000.0,12013380,KOSDAQ
DEVSISTERS 30D low   2024-07-04,50500.0,51600.0,48650.0,48700.0,459948.0,22883634950.0,585051606000.0,12013380,KOSDAQ
DEVSISTERS 90D low   2024-10-23,34850.0,35350.0,33800.0,34900.0,50119.0,1732133350.0,420038252000.0,12035480,KOSDAQ
DEVSISTERS 180D low  2024-11-14,30700.0,30850.0,28700.0,29300.0,134079.0,3970576600.0,352791045000.0,12040650,KOSDAQ
```

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_90D|MAE_90D|MFE_180D|MAE_180D|verdict|aggregate|
|---|---|---|---|---|---|---|---|---|---|---|
|R8L13_C27_KRAFTON_T1_STAGE2A_2023Q3|259960|Stage2-Actionable|2023-11-08|190800|27.62|-7.23|58.28|-7.23|current_profile_correct|representative|
|R8L13_C27_KRAFTON_T2_STAGE3G_20240213|259960|Stage3-Green|2024-02-13|230000|26.3|-6.09|54.35|-6.09|current_profile_correct|label_comparison_only|
|R8L13_C27_NETMARBLE_T1_STAGE2A_20240508|251270|Stage2-Actionable|2024-05-08|60700|19.28|-13.67|19.28|-13.67|current_profile_too_early|representative|
|R8L13_C27_DEVSISTERS_T1_STAGE2A_20240626|194480|Stage2-Actionable|2024-06-26|75700|0.79|-55.35|0.79|-62.09|current_profile_false_positive|representative|
|R8L13_C27_DEVSISTERS_T2_4C_20240704|194480|4C|2024-07-04|48700|14.58|-30.6|14.58|-41.07|current_profile_4C_too_late|4C_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger backtest

|case|entry|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak|drawdown_after_peak|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
|KRAFTON 3Q23 conversion|2023-11-08|190800|16.09|-5.50|27.62|-7.23|58.28|-7.23|2025-02-10 / 390000|-20.00|
|Netmarble launch spike|2024-05-08|60700|19.28|-3.29|19.28|-13.67|19.28|-13.67|2024-05-10 / 72400|-27.62|
|Devsisters launch spike|2024-06-26|75700|0.79|-26.95|0.79|-55.35|0.79|-62.09|2024-06-26 / 76300|-62.39|

### Aggregate representative metrics

```text
eligible_representative_trigger_count = 3
avg_MFE_90D_pct = 15.9
avg_MAE_90D_pct = -25.42
avg_MFE_180D_pct = 26.12
avg_MAE_180D_pct = -27.66
false_positive_rate = 0.67
```

## 13. Current Calibrated Profile Stress Test

|case|P0 likely label|actual price path|stress-test verdict|
|---|---|---|---|
|KRAFTON|Stage2-Actionable → later Green|High MFE with controlled MAE; conversion evidence existed|current_profile_correct|
|Netmarble|Possible Yellow/Green if IP launch + RS overcounted|Fast MFE, then MAE widened; no durable rerating|current_profile_too_early|
|Devsisters|Could be false Yellow/Green if launch spike overcounted|No follow-through; 180D drawdown exceeded -60%|current_profile_false_positive|

Applied axis audit:

```text
stage2_actionable_evidence_bonus: kept, but C27 launch-only entries need retention/margin guard.
yellow_threshold_75: too permissive when relative_strength + IP quality dominate without retention.
green_threshold_87/revision_55: correct for KRAFTON; too permissive if revision is inferred from launch traffic.
price_only_blowoff_blocks_positive_stage: strengthened for C27.
full_4b_requires_non_price_evidence: kept; price-only local peak remains overlay, not full 4B.
hard_4c_thesis_break_routes_to_4c: strengthened for post-launch reversal.
```

## 14. Stage2 / Yellow / Green Comparison

KRAFTON shows that a C27 Green can still be valid when Green follows revenue/margin confirmation. The Stage3-Green comparison trigger entered at 230000 vs Stage2-Actionable at 190800, while the full-window peak after Stage2 was 302000 inside the 180D window.

```text
green_lateness_ratio = (230000 - 190800) / (302000 - 190800) = 0.35
interpretation = Green somewhat later, but not peak-after-the-fact
```

Netmarble and Devsisters have no valid Stage3-Green trigger because retention / repeat monetization / margin bridge was not confirmed at entry. Their launch signals should remain Stage2-Actionable or be capped below Green.

## 15. 4B Local vs Full-window Timing Audit

|trigger|four_b_evidence_type|local_peak_proximity|full_window_peak_proximity|verdict|
|---|---|---:|---:|---|
|Netmarble 2024-05-08|price_only|1.00|1.00|price-only watch, not full 4B|
|Devsisters 2024-06-26|price_only / positioning_overheat|1.00|1.00|launch-day blowoff; should block positive Green|
|KRAFTON|none at Stage2|n/a|n/a|no 4B overlay at entry|

C27-specific nuance: launch-day 4B can arrive before evidence matures. It should prevent Green promotion, but it should not automatically imply full-cycle exit unless non-price evidence confirms that the IP monetization thesis is capped.

## 16. 4C Protection Audit

Devsisters shows the cleanest 4C timing lesson:

```text
prior stage entry = 2024-06-26 close 75700
post-launch break trigger = 2024-07-04 close 48700
subsequent observed low = 28700
4C protection label = hard_4c_success
```

The 4C was not "bad news after a downtrend"; it was the market breaking the launch thesis. In C27, absence of post-launch retention can become thesis-break evidence faster than in capex/backlog sectors.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = evidence is specific to C27 content IP, not all R8 platform/content/SW cases
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

Proposed shadow-only rules:

1. `C27_retention_margin_bridge_required`: Green requires at least one of retention, recurring revenue, ARPU/paid conversion, or margin bridge after IP launch.
2. `C27_launch_only_green_cap`: launch/download/ranking/traffic evidence alone caps at Stage2-Actionable or Yellow, not Green.
3. `C27_fast_4C_after_post_launch_reversal`: if launch spike breaks below pre-event range without retention evidence, route to 4C thesis-break watch.

## 19. Before / After Backtest Comparison

|profile|scope|eligible triggers|avg_MFE_90D|avg_MAE_90D|avg_MFE_180D|avg_MAE_180D|false_positive_rate|score_return_alignment|
|---|---|---:|---:|---:|---:|---:|---:|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current global proxy|3|15.9|-25.42|26.12|-27.66|0.67|mixed; launch-only false positives remain|
|P0b e2r_2_0_baseline_reference|rollback reference|3|15.9|-25.42|26.12|-27.66|0.67|worse; more likely to overcount RS/launch|
|P1 sector_specific_candidate_profile|L8 only|3|15.9|-25.42|26.12|-27.66|0.67|too broad; not proposed|
|P2 canonical_archetype_candidate_profile|C27 only|3|27.62|-7.23|58.28|-7.23|0.00 for Green|best alignment: promotes only KRAFTON-like conversion|
|P3 counterexample_guard_profile|C27 guard|3|27.62|-7.23|58.28|-7.23|0.00 for Green|guards launch-only Netmarble/Devsisters|

## 20. Score-Return Alignment Matrix

|case|before score / label|after score / label|price outcome|alignment verdict|
|---|---|---|---|---|
|KRAFTON|86 / Stage3-Yellow|90 / Stage3-Green|180D MFE +58.28, MAE -7.23|aligned positive|
|Netmarble|76 / Stage3-Yellow|69 / Stage2-Actionable|180D MFE +19.28, MAE -13.67|after profile better, avoids Green|
|Devsisters|78 / Stage3-Yellow|54 / 4C/ThesisBreak|180D MFE +0.79, MAE -62.09|after profile much better|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L8_PLATFORM_CONTENT_SW_SECURITY|C27_CONTENT_IP_GLOBAL_MONETIZATION|GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE|1|2|2|1|3|0|5|3|2|false|true|C27 now has launch-only false-positive guard and one conversion-positive anchor|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
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
  - launch_only_ip_false_positive
  - green_without_retention_bridge
  - 4C_too_late_after_launch_reversal
new_axis_proposed:
  - C27_retention_margin_bridge_required
  - C27_launch_only_green_cap
  - C27_fast_4C_after_post_launch_reversal
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web OHLC rows for selected entry / peak / low points
- manifest max_date = 2026-02-20
- clean 180D windows from symbol profiles
- representative trigger MFE/MAE
- current calibrated profile stress test
- C27 launch-only vs monetization-conversion distinction
```

Not validated:

```text
- no live scan
- no current candidate discovery
- no production scoring patch
- no stock_agent src/e2r access
- no broker/API/autotrading integration
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_retention_margin_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"IP launch/download evidence should not become Green unless retention or revenue/margin conversion is visible","Filtered DEVSISTERS false positive and kept KRAFTON positive",R8L13_C27_KRAFTON_T1_STAGE2A_2023Q3|R8L13_C27_DEVSISTERS_T1_STAGE2A_20240626,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_launch_only_green_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Launch-only IP events cap at Stage2-Actionable unless financial visibility appears","Reduced current_profile_false_positive on DEVSISTERS and too-early Netmarble",R8L13_C27_NETMARBLE_T1_STAGE2A_20240508|R8L13_C27_DEVSISTERS_T1_STAGE2A_20240626,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_fast_4C_after_post_launch_reversal,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"If launch spike breaks below pre-event range without retention evidence, route to 4C quickly","Improved protection label for DEVSISTERS launch failure",R8L13_C27_DEVSISTERS_T2_4C_20240704,1,1,1,low,canonical_shadow_only,"4C overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L13_C27_KRAFTON_BGMI_OPERATING_LEVERAGE_2023Q3", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable: 2023Q3 earnings / BGMI restart + PUBG live-service monetization visible", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Content IP was already tied to recurring revenue and margin bridge, not a trailer/download-only event.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Content IP was already tied to recurring revenue and margin bridge, not a trailer/download-only event."}
{"row_type": "case", "case_id": "R8L13_C27_NETMARBLE_SOLOLEVELING_LAUNCH_2024", "symbol": "251270", "company_name": "넷마블", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable: Solo Leveling: ARISE global launch / IP launch traction", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Launch IP strength produced a tradable pop but did not sustain a clean 180D rerating path without post-launch retention / margin confirmation.", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Launch IP strength produced a tradable pop but did not sustain a clean 180D rerating path without post-launch retention / margin confirmation."}
{"row_type": "case", "case_id": "R8L13_C27_DEVSISTERS_COOKIE_TOWER_LAUNCH_2024", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable/launch: CookieRun: Tower of Adventures launch-day spike", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Launch-day evidence without retention/revenue conversion was a false positive; 4C thesis-break route was needed quickly.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Launch-day evidence without retention/revenue conversion was a false positive; 4C thesis-break route was needed quickly."}
{"row_type": "trigger", "trigger_id": "R8L13_C27_KRAFTON_T1_STAGE2A_2023Q3", "case_id": "R8L13_C27_KRAFTON_BGMI_OPERATING_LEVERAGE_2023Q3", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-07", "entry_date": "2023-11-08", "entry_price": 190800, "evidence_available_at_that_date": "3Q23 earnings and live-service monetization showed BGMI / PUBG IP revenue conversion and operating leverage.", "evidence_source": "KRAFTON 3Q23 earnings release / public IR and press coverage at trigger date", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2023.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.09, "MFE_90D_pct": 27.62, "MFE_180D_pct": 58.28, "MFE_1Y_pct": 86.06, "MFE_2Y_pct": 104.4, "MAE_30D_pct": -5.5, "MAE_90D_pct": -7.23, "MAE_180D_pct": -7.23, "MAE_1Y_pct": -7.23, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-10", "peak_price": 390000, "drawdown_after_peak_pct": -20.0, "green_lateness_ratio": 0.35, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C27_259960_2023-11-08_190800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C27_KRAFTON_T2_STAGE3G_20240213", "case_id": "R8L13_C27_KRAFTON_BGMI_OPERATING_LEVERAGE_2023Q3", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill|counterexample_mining", "trigger_type": "Stage3-Green", "trigger_date": "2024-02-08", "entry_date": "2024-02-13", "entry_price": 230000, "evidence_available_at_that_date": "Follow-on earnings confirmation shifted the case from IP recovery to confirmed operating leverage.", "evidence_source": "KRAFTON FY2023/4Q23 earnings release / public IR", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.87, "MFE_90D_pct": 26.3, "MFE_180D_pct": 54.35, "MFE_1Y_pct": 69.57, "MFE_2Y_pct": 69.57, "MAE_30D_pct": -6.09, "MAE_90D_pct": -6.09, "MAE_180D_pct": -6.09, "MAE_1Y_pct": -6.09, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-10", "peak_price": 390000, "drawdown_after_peak_pct": -20.0, "green_lateness_ratio": 0.35, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "label_comparison_green_not_too_late", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C27_259960_2024-02-13_230000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same symbol but different trigger family: Stage3 confirmation timing audit", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C27_NETMARBLE_T1_STAGE2A_20240508", "case_id": "R8L13_C27_NETMARBLE_SOLOLEVELING_LAUNCH_2024", "symbol": "251270", "company_name": "넷마블", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-08", "entry_date": "2024-05-08", "entry_price": 60700, "evidence_available_at_that_date": "Solo Leveling: ARISE global launch converted a major webtoon/anime IP into a game launch with visible market attention.", "evidence_source": "Netmarble launch announcements / public game release coverage", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv", "profile_path": "atlas/symbol_profiles/251/251270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.28, "MFE_90D_pct": 19.28, "MFE_180D_pct": 19.28, "MFE_1Y_pct": 19.28, "MFE_2Y_pct": null, "MAE_30D_pct": -3.29, "MAE_90D_pct": -13.67, "MAE_180D_pct": -13.67, "MAE_1Y_pct": -13.67, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-10", "peak_price": 72400, "drawdown_after_peak_pct": -27.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "stage2_promote_candidate_with_high_MAE", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C27_251270_2024-05-08_60700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C27_DEVSISTERS_T1_STAGE2A_20240626", "case_id": "R8L13_C27_DEVSISTERS_COOKIE_TOWER_LAUNCH_2024", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 75700, "evidence_available_at_that_date": "CookieRun: Tower of Adventures launch-day spike; the event was IP/launch evidence but lacked confirmed retention or revenue conversion at entry.", "evidence_source": "Devsisters launch announcements / public game release coverage", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.79, "MFE_90D_pct": 0.79, "MFE_180D_pct": 0.79, "MFE_1Y_pct": 0.79, "MFE_2Y_pct": null, "MAE_30D_pct": -26.95, "MAE_90D_pct": -55.35, "MAE_180D_pct": -62.09, "MAE_1Y_pct": -62.09, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 76300, "drawdown_after_peak_pct": -62.39, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_late_to_save_stage2_entry", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C27_194480_2024-06-26_75700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L13_C27_DEVSISTERS_T2_4C_20240704", "case_id": "R8L13_C27_DEVSISTERS_COOKIE_TOWER_LAUNCH_2024", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_TO_RETENTION_AND_MARGIN_BRIDGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill|counterexample_mining", "trigger_type": "4C", "trigger_date": "2024-07-04", "entry_date": "2024-07-04", "entry_price": 48700, "evidence_available_at_that_date": "Post-launch reversal below the pre-spike range indicated launch thesis failure; no confirmed retention / monetization bridge.", "evidence_source": "Stock-web OHLC reversal plus public launch-monitoring context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.58, "MFE_90D_pct": 14.58, "MFE_180D_pct": 14.58, "MFE_1Y_pct": 14.58, "MFE_2Y_pct": null, "MAE_30D_pct": -17.86, "MAE_90D_pct": -30.6, "MAE_180D_pct": -41.07, "MAE_1Y_pct": -41.07, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 55800, "drawdown_after_peak_pct": -48.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L13_C27_194480_2024-07-04_48700", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": "same symbol but different trigger family: 4C thesis-break timing", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C27_shadow", "case_id": "R8L13_C27_KRAFTON_BGMI_OPERATING_LEVERAGE_2023Q3", "trigger_id": "R8L13_C27_KRAFTON_T1_STAGE2A_2023Q3", "symbol": "259960", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 70, "revision_score": 72, "relative_strength_score": 65, "customer_quality_score": 75, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 25, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "ip_monetization_score": 82, "retention_score": 75}, "weighted_score_before": 86.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 76, "revision_score": 78, "relative_strength_score": 68, "customer_quality_score": 78, "policy_or_regulatory_score": 45, "valuation_repricing_score": 58, "execution_risk_score": 22, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "ip_monetization_score": 86, "retention_score": 80}, "weighted_score_after": 90.0, "stage_label_after": "Stage3-Green", "changed_components": ["ip_monetization_score", "retention_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "P2 adds IP monetization durability and retention/margin bridge confirmation, allowing promotion only when revenue conversion is visible.", "MFE_90D_pct": 27.62, "MAE_90D_pct": -7.23, "score_return_alignment_label": "structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C27_shadow", "case_id": "R8L13_C27_KRAFTON_BGMI_OPERATING_LEVERAGE_2023Q3", "trigger_id": "R8L13_C27_KRAFTON_T2_STAGE3G_20240213", "symbol": "259960", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 70, "revision_score": 72, "relative_strength_score": 65, "customer_quality_score": 75, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 25, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "ip_monetization_score": 82, "retention_score": 75}, "weighted_score_before": 86.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 76, "revision_score": 78, "relative_strength_score": 68, "customer_quality_score": 78, "policy_or_regulatory_score": 45, "valuation_repricing_score": 58, "execution_risk_score": 22, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "ip_monetization_score": 86, "retention_score": 80}, "weighted_score_after": 90.0, "stage_label_after": "Stage3-Green", "changed_components": ["ip_monetization_score", "retention_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "P2 adds IP monetization durability and retention/margin bridge confirmation, allowing promotion only when revenue conversion is visible.", "MFE_90D_pct": 26.3, "MAE_90D_pct": -6.09, "score_return_alignment_label": "label_comparison_green_not_too_late", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C27_shadow", "case_id": "R8L13_C27_NETMARBLE_SOLOLEVELING_LAUNCH_2024", "trigger_id": "R8L13_C27_NETMARBLE_T1_STAGE2A_20240508", "symbol": "251270", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 42, "relative_strength_score": 72, "customer_quality_score": 68, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 48, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ip_monetization_score": 70, "retention_score": 35}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 32, "revision_score": 40, "relative_strength_score": 55, "customer_quality_score": 68, "policy_or_regulatory_score": 0, "valuation_repricing_score": 48, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ip_monetization_score": 62, "retention_score": 30}, "weighted_score_after": 69.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["ip_monetization_score", "retention_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "P2 penalizes launch-only IP without post-launch retention and margin bridge; the event remains watchlist/actionable rather than Green.", "MFE_90D_pct": 19.28, "MAE_90D_pct": -13.67, "score_return_alignment_label": "stage2_promote_candidate_with_high_MAE", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C27_shadow", "case_id": "R8L13_C27_DEVSISTERS_COOKIE_TOWER_LAUNCH_2024", "trigger_id": "R8L13_C27_DEVSISTERS_T1_STAGE2A_20240626", "symbol": "194480", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 35, "relative_strength_score": 85, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 72, "execution_risk_score": 65, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ip_monetization_score": 55, "retention_score": 15}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 25, "relative_strength_score": 20, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 80, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ip_monetization_score": 35, "retention_score": 5}, "weighted_score_after": 54.0, "stage_label_after": "4C/ThesisBreak", "changed_components": ["ip_monetization_score", "retention_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "P3 guard routes launch-day blowoff without retention/revenue bridge to 4C watch/break instead of positive Green.", "MFE_90D_pct": 0.79, "MAE_90D_pct": -55.35, "score_return_alignment_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R8", "loop": "13", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 5, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 5, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["launch_only_ip_false_positive", "green_without_retention_bridge", "4C_too_late_after_launch_reversal"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R8
completed_loop = 13
next_round = R9
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Price atlas: `Songdaiki/stock-web`.
- Price basis: `tradable_raw`.
- Price adjustment status: `raw_unadjusted_marcap`.
- Manifest max date: `2026-02-20`.
- Evidence source wording intentionally stays at source-family level because this MD is a calibration artifact, not a live recommendation memo.
- No investment recommendation is made or implied.
