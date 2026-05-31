# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R12
scheduled_loop = 15
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK
output_file = e2r_stock_web_v12_residual_round_R12_loop_15_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 5 new independent cases, 3 counterexamples, and 5 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The tested residual is not “Stage2 can be early.” The tested residual is narrower: in C32, an ownership-control headline can behave like a spring under a locked door. If the buyer route, tender price, financing, and regulatory close path are explicit, the spring can release into a real control-premium rally. If the headline lacks close certainty, the same spring snaps back into high MAE.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK
loop_objective = coverage_gap_fill, counterexample_mining, residual_false_positive_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test
```

R12 allows L10 cross-event work or under-covered service/agri work. This MD uses L10/C32 because the observed residual is event-ownership specific rather than sector-product specific.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were checked only at the registry/report level, not through source code. The registry visible in `data/e2r/calibration/md_registry.jsonl` contains prior R12 agriculture/life-services historical calibration files and R11 policy/geopolitics files, but no current v12 R12/loop15 C32 result was found in the checked artifact surface.

```text
stock_agent_code_opened = false
stock_agent_src_e2r_opened = false
allowed_artifact_checked = data/e2r/calibration/md_registry.jsonl
previous_round_state_used = prior conversation output: R11 / loop 15 -> next_round R12 / loop 15
same_symbol_same_trigger_reuse = none
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The OHLC basis is raw and unadjusted. The calculation therefore treats corporate-action candidate windows as blocked; all representative windows used below are clean for the 180D window.

## 5. Historical Eligibility Gate

|case_id|symbol|entry_date in tradable shard|180D forward available|180D corporate-action contamination|calibration_usable|
|---|---:|---|---|---|---|
|R12L15_C32_SM_20230210_HYBE_KAKAO_TENDER_BATTLE|041510|yes|yes|no|true|
|R12L15_C32_KOREAZINC_20240913_CONTROL_CONTEST|010130|yes|yes|no|true|
|R12L15_C32_NAMYANG_20210528_CONTROL_SALE_LITIGATION|003920|yes|yes|no|true|
|R12L15_C32_HANSSEM_20210714_CONTROL_STAKE_IMM|009240|yes|yes|no|true|
|R12L15_C32_YTN_20231024_PUBLIC_STAKE_SALE|040300|yes|yes|no|true|

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK

subroutes:
- explicit_tender_offer_with_price_cap
- control_contest_counterbid
- controlling_stake_sale_headline_without_close_certainty
- public_stake_sale_regulatory_close_risk
- event_premium_fully_priced_at_entry
```

Compression rule: the same C32 label must not treat all ownership-change headlines alike. Tender-price + financing + close path is the load-bearing beam. A loose “buyer appears” headline is wallpaper.

## 7. Case Selection Summary

|case_id|symbol|company|case role|why selected|
|---|---:|---|---|---|
|SM tender battle|041510|에스엠|structural_success|explicit tender/counter-tender route; 4B cap visible near event premium peak|
|Korea Zinc control contest|010130|고려아연|structural_success|control contest produced real MFE, then violent blow-off drawdown|
|Namyang control sale litigation|003920|남양유업|failed_rerating|headline control sale generated MFE but legal close risk erased premium|
|Hanssem control-stake sale|009240|한샘|failed_rerating|control premium was priced immediately, then operating/financing cycle dominated|
|YTN public stake sale|040300|YTN|failed_rerating|preferred-bidder/regulatory route had high MAE and no durable rerating|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
calibration_usable_case_count = 5
4B_case_count = 5
4C_case_count = 3
```

Positive cases show that C32 should not be globally blocked. Counterexamples show that C32 should not be promoted on headline evidence alone. The proposed rule is a gate, not a throttle: it opens only when route congruence is explicit.

## 9. Evidence Source Map

|case|trigger_date|stage2 evidence|stage3 evidence|4B/4C risk evidence|
|---|---|---|---|---|
|에스엠|2023-02-10|public tender/control-contest disclosure; strong relative move|multiple public sources; later counter-tender price cap|event premium cap; post-contest reversal|
|고려아연|2024-09-13|public control-contest/tender route; relative strength|multiple public sources; event premium continuation|valuation blow-off; positioning overheat; post-peak drawdown|
|남양유업|2021-05-28|public controlling-stake-sale headline|multiple public sources, but weak close certainty|legal/contract close dispute; thesis break|
|한샘|2021-07-14|public control-stake-sale headline|public buyer route, but no operating revision confirmation|event premium fully priced; operating/financing risk|
|YTN|2023-10-24|public stake-sale/preferred-bidder route|public event sources, but regulatory uncertainty|regulatory close risk; high-MAE reversal|

## 10. Price Data Source Map

|symbol|company|price_shard_path|profile_path|profile status|
|---:|---|---|---|---|
|041510|에스엠|atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv|atlas/symbol_profiles/041/041510.json|usable; corporate-action dates outside tested window|
|010130|고려아연|atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/symbol_profiles/010/010130.json|usable; no corporate-action candidates|
|003920|남양유업|atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv|atlas/symbol_profiles/003/003920.json|usable; later 2024 corporate-action candidate outside tested window|
|009240|한샘|atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv|atlas/symbol_profiles/009/009240.json|usable; no corporate-action candidates|
|040300|YTN|atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv|atlas/symbol_profiles/040/040300.json|usable; no corporate-action candidates|

## 11. Case-by-Case Trigger Grid

|case|symbol|trigger|entry|MFE30/90/180|MAE30/90/180|peak|current verdict|role|
|---|---:|---|---:|---:|---:|---|---|---|
|R12L15_C32_SM_20230210_HYBE_KAKAO_TENDER_BATTLE|041510|2023-02-10 Stage2-Actionable|114,700|40.54 / 40.54 / 40.54|-9.24 / -23.63 / -23.63|2023-03-08 161,200|current_profile_too_late|positive|
|R12L15_C32_KOREAZINC_20240913_CONTROL_CONTEST|010130|2024-09-13 Stage2-Actionable|666,000|131.68 / 261.41 / 261.41|-1.65 / -1.65 / -3.45|2024-12-06 2,407,000|current_profile_4B_too_late|positive|
|R12L15_C32_NAMYANG_20210528_CONTROL_SALE_LITIGATION|003920|2021-05-28 Stage2-Actionable|570,000|42.63 / 42.63 / 42.63|-5.26 / -32.98 / -34.91|2021-07-01 813,000|current_profile_false_positive|counterexample|
|R12L15_C32_HANSSEM_20210714_CONTROL_STAKE_IMM|009240|2021-07-14 Stage2-Actionable|146,500|1.71 / 1.71 / 1.71|-27.99 / -32.22 / -52.97|2021-07-14 149,000|current_profile_false_positive|counterexample|
|R12L15_C32_YTN_20231024_PUBLIC_STAKE_SALE|040300|2023-10-24 Stage2-Actionable|7,800|23.08 / 23.08 / 23.08|-30.64 / -41.22 / -62.76|2023-10-25 9,600|current_profile_false_positive|counterexample|

## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry_date|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
|041510|2023-02-10|114,700|40.54|-9.24|40.54|-23.63|40.54|-23.63|2023-03-08|161,200|-45.66|
|010130|2024-09-13|666,000|131.68|-1.65|261.41|-1.65|261.41|-3.45|2024-12-06|2,407,000|-73.29|
|003920|2021-05-28|570,000|42.63|-5.26|42.63|-32.98|42.63|-34.91|2021-07-01|813,000|-54.37|
|009240|2021-07-14|146,500|1.71|-27.99|1.71|-32.22|1.71|-52.97|2021-07-14|149,000|-53.76|
|040300|2023-10-24|7,800|23.08|-30.64|23.08|-41.22|23.08|-62.76|2023-10-25|9,600|-69.74|

## 13. Current Calibrated Profile Stress Test

|case|P0 likely judgment|actual alignment|verdict|
|---|---|---|---|
|에스엠|Stage3-Yellow or late Green after confirmed counterbid|Good MFE, but Green near the cap is late; 4B should bind quickly|current_profile_too_late|
|고려아연|Stage3-Green but slow 4B due non-price confirmation requirement|Good MFE, but post-peak drawdown shows 4B too late if blow-off route is ignored|current_profile_4B_too_late|
|남양유업|Stage3-Yellow from headline control sale + RS|MFE existed, but high MAE and legal close risk made it a false positive|current_profile_false_positive|
|한샘|Stage3-Yellow from control-stake sale headline|Almost no MFE after entry; large 180D MAE|current_profile_false_positive|
|YTN|Stage3-Yellow from preferred bidder/policy route|Short-lived MFE; high regulatory-close MAE|current_profile_false_positive|

## 14. Stage2 / Yellow / Green Comparison

In this archetype, Stage2-Actionable is useful only when it means “control-premium route exists.” Stage3-Green must mean “route is closing or tender price is explicit,” not simply “headline is famous.”

```text
Stage2 bonus: kept, but only after route classification.
Yellow threshold 75: too permissive for headline-only control premium.
Green threshold 87 / revision 55: not directly comparable; C32 requires close-route confirmation rather than EPS revision.
price_only_blowoff guard: strengthened.
full_4B non-price requirement: kept but made archetype-specific; explicit tender cap/control premium can be non-price 4B evidence.
hard_4C routing: strengthened when legal/regulatory close route breaks.
```

## 15. 4B Local vs Full-window Timing Audit

|case|4B evidence type|four_b_local_peak_proximity|four_b_full_window_peak_proximity|timing verdict|
|---|---|---:|---:|---|
|에스엠|control_premium_or_event_premium, valuation_blowoff, explicit_event_cap|0.753|0.753|good_full_window_4B_timing|
|고려아연|valuation_blowoff, positioning_overheat, control_premium_or_event_premium|0.766|0.766|good_full_window_4B_timing|
|남양유업|legal_or_regulatory_block, contract_delay|0.000|0.000|price_move_without_close_confirmation|
|한샘|valuation_blowoff, control_premium_or_event_premium|1.000|1.000|event_premium_fully_priced_at_entry|
|YTN|legal_or_regulatory_block, explicit_event_cap|1.000|1.000|event_premium_fully_priced_at_entry_plus_regulatory_block|

## 16. 4C Protection Audit

|case|4C evidence|label|protection interpretation|
|---|---|---|---|
|남양유업|legal/contract dispute after sale headline|hard_4c_success|4C would have prevented a long tail after the initial event premium failed to close.|
|한샘|operating/financing cycle overwhelmed control premium|hard_4c_success|4C or 4B cap would have avoided treating an already-priced premium as structural rerating.|
|YTN|regulatory close risk and policy overhang|hard_4c_success|4C routing fits once regulatory path no longer supports ownership premium.|

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = C32 cuts across content, materials, consumer, and media; L10-wide rule would be too broad.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
axis = c32_control_premium_route_congruence_guard
baseline_value = absent
tested_value = require route_congruence_score >= 7 and regulatory_close_risk_score <= 5 for Stage3-Yellow/Green promotion
counterexample_guard = if event premium is already fully priced and close risk is unresolved, cap at Stage2-Watch or 4B overlay
```

Proposed shadow rule:

```text
if canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:
    positive promotion requires:
        explicit tender price or binding buyer route
        AND financing/settlement route not materially uncertain
        AND regulatory/legal close risk not high
    if headline-only control sale or public-stake sale without close certainty:
        cap stage at Stage2-Watch or Stage2-Actionable
    if event premium already reaches tender/control cap:
        add 4B overlay even if price-only blowoff would otherwise be blocked
    if legal/regulatory close route breaks:
        route to hard_4c_thesis_break_routes_to_4c
```

## 19. Before / After Backtest Comparison

|profile|scope|eligible triggers|avg MFE90|avg MAE90|avg MFE180|avg MAE180|FP rate|missed structural|late Green|verdict|
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current global proxy|5|73.87|-26.34|73.87|-35.54|0.60|0|2|too much promotion for headline-only control premium; too slow 4B on blow-off events|
|P0b e2r_2_0_baseline_reference|rollback reference|5|73.87|-26.34|73.87|-35.54|0.60|0|1|baseline also fails because it has no close-risk subtraction|
|P1 sector_specific_candidate_profile|L10 only|5|150.98|-12.64|150.98|-13.54|0.40|0|1|better, but sector scope too broad; use canonical rule not L10-wide|
|P2 canonical_archetype_candidate_profile|C32 only|5|150.98|-12.64|150.98|-13.54|0.00|0|1|best alignment: promote only tender/close-confirmed routes; demote sale headlines with legal/regulatory close risk|
|P3 counterexample_guard_profile|C32 guard|5|22.47|-35.47|22.47|-50.21|0.00|0|0|blocks Namyang/Hanssem/YTN headline-only Green promotions|

## 20. Score-Return Alignment Matrix

|case|weighted_score_before|stage_before|weighted_score_after|stage_after|score-return alignment|
|---|---:|---|---:|---|---|
|에스엠|86|Stage3-Yellow|90|Stage3-Green_with_4B_overlay|after better: allows true tender route but caps upside near explicit premium|
|고려아연|88|Stage3-Green|91|Stage3-Green_with_4B_overlay|after better: keeps positive but adds faster blow-off overlay|
|남양유업|82|Stage3-Yellow|64|Stage2-Watch_or_4C_risk|after better: prevents legal-close false positive|
|한샘|78|Stage3-Yellow|60|Stage2-Watch_or_4B_overlay|after better: recognizes event premium fully priced at entry|
|YTN|80|Stage3-Yellow|59|Stage2-Watch_or_4C_risk|after better: blocks regulatory-close false positive|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK|2|3|5|3|5|0|5|5|5|false|true|C32 now has positive tender-route examples plus failed headline/regulatory-close counterexamples; needs future non-Korea holdout before any global promotion.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_too_late
  - current_profile_4B_too_late
new_axis_proposed: c32_control_premium_route_congruence_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema basis
- symbol profile availability and corporate-action candidate status
- entry_date and entry_price from stock-web tradable shard rows
- MFE/MAE 30D/90D/180D using raw/unadjusted OHLC extrema visible in stock-web windows
- positive/counterexample balance
- same_entry_group dedupe: one representative trigger per case
```

Not validated:

```text
- live recommendation suitability
- current 2026 candidate scan
- brokerage execution
- stock_agent code behavior
- production scoring weights
- legal finality of historical tender/control events beyond event-date evidence labels
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_control_premium_route_congruence_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Promote only explicit tender/close-confirmed control premium; cap headline-only sale or regulatory-close risk.","Reduced false-positive Green in Namyang/Hanssem/YTN while preserving SM/Korea Zinc positive route.","R12L15_TR_SM_STAGE2_20230210|R12L15_TR_KZ_STAGE2_20240913|R12L15_TR_NAMYANG_STAGE2_20210528|R12L15_TR_HANSSEM_STAGE2_20210714|R12L15_TR_YTN_STAGE2_20231024",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_event_premium_fully_priced_4b_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"If event premium reaches tender/control cap, treat as 4B overlay even before later price collapse.","Improves 4B timing in SM/Korea Zinc/Hanssem/YTN.",5,5,3,medium,canonical_shadow_only,"not production; 4B overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L15_C32_SM_20230210_HYBE_KAKAO_TENDER_BATTLE", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L15_TR_SM_STAGE2_20230210", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_then_event_cap_reversal", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Explicit tender/counter-tender price anchors allowed promotion, but the same cap became a 4B overlay once upside was mostly priced."}
{"row_type": "case", "case_id": "R12L15_C32_KOREAZINC_20240913_CONTROL_CONTEST", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L15_TR_KZ_STAGE2_20240913", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_then_blowoff_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Control-premium route was real, but blow-off and governance/legal complexity required faster 4B overlay."}
{"row_type": "case", "case_id": "R12L15_C32_NAMYANG_20210528_CONTROL_SALE_LITIGATION", "symbol": "003920", "company_name": "남양유업", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L15_TR_NAMYANG_STAGE2_20210528", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_green_if_no_close_risk_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Headline control sale alone should not clear Green when closing risk and legal dispute probability are not resolved."}
{"row_type": "case", "case_id": "R12L15_C32_HANSSEM_20210714_CONTROL_STAKE_IMM", "symbol": "009240", "company_name": "한샘", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L15_TR_HANSSEM_STAGE2_20210714", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_after_control_premium", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Control premium was already in the entry price; without operating-revision confirmation the event should be capped, not promoted."}
{"row_type": "case", "case_id": "R12L15_C32_YTN_20231024_PUBLIC_STAKE_SALE", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L15_TR_YTN_STAGE2_20231024", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_green_if_regulatory_close_risk_ignored", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The policy/regulatory close-risk score must subtract from control-premium promotion, otherwise a sale headline becomes a Green false positive."}
{"row_type": "trigger", "trigger_id": "R12L15_TR_SM_STAGE2_20230210", "case_id": "R12L15_C32_SM_20230210_HYBE_KAKAO_TENDER_BATTLE", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "sector": "content/governance event", "primary_archetype": "control_premium_tender_offer_close_risk", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "sector_specific_rule_discovery", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "HYBE tender offer / control contest becomes public; later Kakao tender price created explicit event cap.", "evidence_source": "public tender-offer/control-contest event record; price row verified in stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": ["explicit_event_cap", "valuation_blowoff", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-10", "entry_price": 114700, "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": 40.54, "MFE_2Y_pct": 40.54, "MAE_30D_pct": -9.24, "MAE_90D_pct": -23.63, "MAE_180D_pct": -23.63, "MAE_1Y_pct": -23.63, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": 0.753, "four_b_local_peak_proximity": 0.753, "four_b_full_window_peak_proximity": 0.753, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "valuation_blowoff", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_then_event_cap_reversal", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L15_C32_SM_20230210_HYBE_KAKAO_TENDER_BATTLE::2023-02-10::114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L15_TR_KZ_STAGE2_20240913", "case_id": "R12L15_C32_KOREAZINC_20240913_CONTROL_CONTEST", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "sector": "materials/governance event", "primary_archetype": "control_premium_tender_offer_close_risk", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "sector_specific_rule_discovery", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "evidence_available_at_that_date": "Management-control tender battle created a visible event-premium route, then a blow-off phase as offer/proxy-control risk intensified.", "evidence_source": "public tender-offer/control-battle event record; price row verified in stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-13", "entry_price": 666000, "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": 261.41, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": -3.45, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.766, "four_b_full_window_peak_proximity": 0.766, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "structural_success_then_blowoff_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L15_C32_KOREAZINC_20240913_CONTROL_CONTEST::2024-09-13::666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L15_TR_NAMYANG_STAGE2_20210528", "case_id": "R12L15_C32_NAMYANG_20210528_CONTROL_SALE_LITIGATION", "symbol": "003920", "company_name": "남양유업", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "sector": "consumer/governance event", "primary_archetype": "control_premium_tender_offer_close_risk", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "sector_specific_rule_discovery", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2021-05-28", "evidence_available_at_that_date": "Controlling-stake sale headline created a sharp control-premium move, but closing/legal dispute risk later dominated.", "evidence_source": "public control-stake-sale/litigation event record; price row verified in stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["legal_or_regulatory_block", "contract_delay", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken", "legal_or_regulatory_block"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv", "profile_path": "atlas/symbol_profiles/003/003920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-28", "entry_price": 570000, "MFE_30D_pct": 42.63, "MFE_90D_pct": 42.63, "MFE_180D_pct": 42.63, "MFE_1Y_pct": 42.63, "MFE_2Y_pct": 42.63, "MAE_30D_pct": -5.26, "MAE_90D_pct": -32.98, "MAE_180D_pct": -34.91, "MAE_1Y_pct": -34.91, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-01", "peak_price": 813000, "drawdown_after_peak_pct": -54.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "price_move_without_close_confirmation", "four_b_evidence_type": ["legal_or_regulatory_block", "contract_delay", "control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green_if_no_close_risk_guard", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L15_C32_NAMYANG_20210528_CONTROL_SALE_LITIGATION::2021-05-28::570000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L15_TR_HANSSEM_STAGE2_20210714", "case_id": "R12L15_C32_HANSSEM_20210714_CONTROL_STAKE_IMM", "symbol": "009240", "company_name": "한샘", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "sector": "consumer/governance event", "primary_archetype": "control_premium_tender_offer_close_risk", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "sector_specific_rule_discovery", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2021-07-14", "evidence_available_at_that_date": "Control-stake sale premium was visible, but post-deal earnings/financing and housing-cycle risk erased the event premium.", "evidence_source": "public control-stake-sale event record; price row verified in stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "valuation_blowoff", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv", "profile_path": "atlas/symbol_profiles/009/009240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-07-14", "entry_price": 146500, "MFE_30D_pct": 1.71, "MFE_90D_pct": 1.71, "MFE_180D_pct": 1.71, "MFE_1Y_pct": 1.71, "MFE_2Y_pct": 1.71, "MAE_30D_pct": -27.99, "MAE_90D_pct": -32.22, "MAE_180D_pct": -52.97, "MAE_1Y_pct": -52.97, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-14", "peak_price": 149000, "drawdown_after_peak_pct": -53.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "event_premium_fully_priced_at_entry", "four_b_evidence_type": ["valuation_blowoff", "control_premium_or_event_premium", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating_after_control_premium", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L15_C32_HANSSEM_20210714_CONTROL_STAKE_IMM::2021-07-14::146500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L15_TR_YTN_STAGE2_20231024", "case_id": "R12L15_C32_YTN_20231024_PUBLIC_STAKE_SALE", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_OFFER_AND_REGULATORY_CLOSE_RISK", "sector": "media/policy ownership event", "primary_archetype": "control_premium_tender_offer_close_risk", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "sector_specific_rule_discovery", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-24", "evidence_available_at_that_date": "Public-stake sale/preferred-bidder control premium was visible, but regulatory approval and privatization overhang turned the event into a high-MAE false positive.", "evidence_source": "public stake-sale/preferred-bidder event record; price row verified in stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["legal_or_regulatory_block", "explicit_event_cap", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv", "profile_path": "atlas/symbol_profiles/040/040300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-10-24", "entry_price": 7800, "MFE_30D_pct": 23.08, "MFE_90D_pct": 23.08, "MFE_180D_pct": 23.08, "MFE_1Y_pct": 23.08, "MFE_2Y_pct": 23.08, "MAE_30D_pct": -30.64, "MAE_90D_pct": -41.22, "MAE_180D_pct": -62.76, "MAE_1Y_pct": -62.76, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-25", "peak_price": 9600, "drawdown_after_peak_pct": -69.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "event_premium_fully_priced_at_entry_plus_regulatory_block", "four_b_evidence_type": ["legal_or_regulatory_block", "control_premium_or_event_premium", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green_if_regulatory_close_risk_ignored", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L15_C32_YTN_20231024_PUBLIC_STAKE_SALE::2023-10-24::7800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C32_SM_20230210_HYBE_KAKAO_TENDER_BATTLE", "trigger_id": "R12L15_TR_SM_STAGE2_20230210", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 86, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 9, "execution_risk_score": 3, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1, "control_premium_route_score": 10, "regulatory_close_risk_score": 3}, "weighted_score_after": 90, "stage_label_after": "Stage3-Green_with_4B_overlay_after_counterbid", "changed_components": ["control_premium_route_score", "regulatory_close_risk_score", "valuation_repricing_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Explicit tender/counter-tender price anchors allowed promotion, but the same cap became a 4B overlay once upside was mostly priced.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -23.63, "score_return_alignment_label": "structural_success_then_event_cap_reversal", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C32_KOREAZINC_20240913_CONTROL_CONTEST", "trigger_id": "R12L15_TR_KZ_STAGE2_20240913", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 2, "accounting_trust_risk_score": 2}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 10, "execution_risk_score": 6, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 2, "control_premium_route_score": 10, "regulatory_close_risk_score": 5}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green_with_4B_overlay", "changed_components": ["control_premium_route_score", "regulatory_close_risk_score", "valuation_repricing_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Control-premium route was real, but blow-off and governance/legal complexity required faster 4B overlay.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "structural_success_then_blowoff_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C32_NAMYANG_20210528_CONTROL_SALE_LITIGATION", "trigger_id": "R12L15_TR_NAMYANG_STAGE2_20210528", "symbol": "003920", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 8, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 6, "control_premium_route_score": 5, "regulatory_close_risk_score": 10}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch_or_4C_risk", "changed_components": ["control_premium_route_score", "regulatory_close_risk_score", "valuation_repricing_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Headline control sale alone should not clear Green when closing risk and legal dispute probability are not resolved.", "MFE_90D_pct": 42.63, "MAE_90D_pct": -32.98, "score_return_alignment_label": "false_positive_green_if_no_close_risk_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C32_HANSSEM_20210714_CONTROL_STAKE_IMM", "trigger_id": "R12L15_TR_HANSSEM_STAGE2_20210714", "symbol": "009240", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 7, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 4, "execution_risk_score": 8, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 2, "control_premium_route_score": 4, "regulatory_close_risk_score": 4}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch_or_4B_overlay", "changed_components": ["control_premium_route_score", "regulatory_close_risk_score", "valuation_repricing_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Control premium was already in the entry price; without operating-revision confirmation the event should be capped, not promoted.", "MFE_90D_pct": 1.71, "MAE_90D_pct": -32.22, "score_return_alignment_label": "failed_rerating_after_control_premium", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C32_YTN_20231024_PUBLIC_STAKE_SALE", "trigger_id": "R12L15_TR_YTN_STAGE2_20231024", "symbol": "040300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": 7, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 3, "execution_risk_score": 9, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3, "control_premium_route_score": 3, "regulatory_close_risk_score": 10}, "weighted_score_after": 59, "stage_label_after": "Stage2-Watch_or_4C_risk", "changed_components": ["control_premium_route_score", "regulatory_close_risk_score", "valuation_repricing_score", "legal_or_contract_risk_score"], "component_delta_explanation": "The policy/regulatory close-risk score must subtract from control-premium promotion, otherwise a sale headline becomes a Green false positive.", "MFE_90D_pct": 23.08, "MAE_90D_pct": -41.22, "score_return_alignment_label": "false_positive_green_if_regulatory_close_risk_ignored", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_false_positive", "current_profile_too_late", "current_profile_4B_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R12
completed_loop = 15
next_round = R13
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest reports `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `symbol_count=5414`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.
- Stock-Web schema maps tradable columns as `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE formula is max high / min low over N tradable rows; calibration requires entry row, 180 forward tradable days, positive OHLCV, and no 180D corporate-action contamination.
- Profile checks:
  - `041510` 에스엠: last_date 2026-02-20; corporate-action candidate dates are old 2002/2005 windows, not 2023 trigger window.
  - `010130` 고려아연: last_date 2026-02-20; corporate_action_candidate_count=0.
  - `003920` 남양유업: 2024-11-20 corporate-action candidate exists, outside the 2021-05-28 through 180D window used here.
  - `009240` 한샘: corporate_action_candidate_count=0.
  - `040300` YTN: corporate_action_candidate_count=0.
- OHLC examples used as anchor rows include: 에스엠 2023-02-10 close 114,700 and 2023-03-08 high 161,200; 고려아연 2024-09-13 close 666,000 and 2024-12-06 high 2,407,000; 남양유업 2021-05-28 close 570,000 and 2021-07-01 high 813,000; 한샘 2021-07-14 close 146,500 and same-day high 149,000; YTN 2023-10-24 close 7,800 and 2023-10-25 high 9,600.

