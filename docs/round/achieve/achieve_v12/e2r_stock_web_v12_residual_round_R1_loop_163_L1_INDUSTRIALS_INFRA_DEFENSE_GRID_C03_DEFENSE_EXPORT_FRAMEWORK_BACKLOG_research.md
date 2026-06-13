# E2R v12 Residual Research — R1 / L1 / C03 Defense Export Framework Backlog

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 163
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: defense_export_framework_to_executive_contract_vs_theme_only_basket
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1 clearing
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 8
reused_case_count: 0
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 8
calibration_usable_case_count: 8
calibration_usable_trigger_count: 8
positive_case_count: 6
counterexample_count: 2
4B_watch_or_overlay_count: 4
4C_or_false4C_audit_count: 0
current_profile_error_count: 6
do_not_propose_new_weight_delta: false
```

## 1. Selection / No-Repeat rationale

C03 is already above the 50-row minimum in the current No-Repeat Index, so this is not a raw coverage-gap loop. It is a Priority 2 quality-repair loop: the goal is to replace generic defense-theme or source-proxy rows with URL-backed framework → executive-contract triggers, and to keep theme-only geopolitical rallies out of the C03 positive bucket. The session already cleared or quality-repaired C02, C09, C14, C10, C06, C07, C11, C01, C28, C12, C05, C23, C27, C08, C19, C25, C13, and C22, while C03 had not been touched in this session.

No hard duplicate was used. The cases below avoid the current-session symbol/trigger families and use distinct `canonical_archetype_id + symbol + trigger_type + entry_date` keys. Same-symbol reuse for LIG Nex1 is intentional because the Saudi and Iraq orders are separate sovereign-customer trigger families with different entry dates and different path behavior.

## 2. Price-source confirmation

| field | value |
|---|---|
| primary_price_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| manifest_max_date | 2026-02-20 |
| entry_price_rule | entry date close `c`; next trading day after public evidence unless evidence was before market and explicitly marked |
| MFE/MAE rule | after-entry forward 30/90/180 tradable rows, max high and min low versus entry close |

Corporate-action profile check: 064350 has an old 2020 candidate, 012450 has old 1996/1997/1999/2009 candidates, 272210 has a 2021 candidate, 065450 has 2004/2008/2009 candidates, and 010820 has 1999/2002/2003/2006 candidates. None overlap the selected entry→D180 windows. 047810 and 079550 show no corporate-action candidate dates in the relevant profile output.

## 3. Case table

| case | ticker | trigger | entry | trigger_type | class | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | read-through |
|---|---:|---:|---:|---|---|---:|---:|---:|---|
| C03-163-01 | 064350 | 2022-08-29 | 2022-08-30 @ 29,450 | Stage2-Actionable | positive_with_high_MAE_4B_guard | 4.41/-20.88 | 9.68/-21.73 | 28.35/-21.73 | signed K2 Poland executive contract translated into 180D upside, but the first 90D path carried a deep macro/entry MAE |
| C03-163-02 | 047810 | 2022-09-16 | 2022-09-19 @ 48,900 | Stage2-Actionable | positive_watch_not_green | 7.57/-18.2 | 7.57/-18.2 | 24.74/-18.2 | FA-50 Poland executive contract produced 180D MFE above 20%, but weak 30/90D tape argues for staged entry rather than Green |
| C03-163-03 | 012450 | 2023-12-04 | 2023-12-05 @ 135,100 | Stage2-Actionable | positive | 10.66/-9.1 | 81.35/-9.1 | 144.26/-9.1 | second K9 Poland executive contract plus technology-transfer/backlog visibility produced clean 90D/180D MFE with shallow MAE |
| C03-163-04 | 079550 | 2024-02-06 | 2024-02-07 @ 113,400 | Stage2-Actionable | positive | 68.69/-0.09 | 91.36/-0.09 | 137.65/-0.09 | Saudi Cheongung-II order had named country, system, battery count and ministry confirmation; price path showed high MFE with almost no MAE |
| C03-163-05 | 079550 | 2024-09-20 | 2024-09-23 @ 214,500 | Stage2-Watch | positive_with_late_high_MAE_guard | 25.87/-3.03 | 26.57/-21.31 | 203.03/-21.31 | Iraq Cheongung-II order extended system export geography, but 90D MAE was deep before the later 180D MFE; should be staged, not chase |
| C03-163-06 | 272210 | 2024-07-09 | 2024-07-10 @ 18,860 | Stage2-Actionable | positive | 24.07/-9.38 | 60.13/-12.35 | 130.12/-12.35 | Saudi MFR subcontract converted the larger LIG-led Cheongung-II order into a direct Hanwha Systems radar revenue bridge |
| C03-163-07 | 065450 | 2022-02-24 | 2022-02-25 @ 6,890 | Stage2-Watch | counterexample_theme_only | 11.76/-10.6 | 11.76/-30.91 | 11.76/-33.38 | geopolitical tension lifted defense-theme names but no export framework/backlog bridge existed; 180D MFE stayed low and MAE deepened |
| C03-163-08 | 010820 | 2022-02-24 | 2022-02-25 @ 4,780 | Stage2-Watch | counterexample_theme_only_high_MAE | 4.08/-22.07 | 23.85/-33.16 | 23.85/-45.5 | same war-tension basket produced temporary MFE but large 90D/180D MAE; price-only defense beta is not C03 framework backlog |

## 4. Evidence notes

- Hyundai Rotem: 4.499T KRW K2 Poland executive contract, 180 tanks, tied back to the July framework. The path says “right thesis, bad early entry risk”: C03 should not ignore MAE just because the contract is hard.
- KAI: FA-50 Poland executive contract was a clean framework-to-contract conversion, but price did not produce immediate follow-through. This is a Stage2-Actionable/Watch distinction, not a Green unlock.
- Hanwha Aerospace: second K9 Poland executive contract and technology-transfer route showed the best C03 structure in this pack: sovereign buyer, specific platform, clear backlog and localization path, and clean price path.
- LIG Nex1: Saudi order is the cleanest prime-contractor positive. Iraq order is also structurally positive but has a 90D drawdown before the later franchise repricing; C03 needs a late-order high-MAE guard rather than a thesis break.
- Hanwha Systems: the Saudi MFR order is a subsystem-supplier positive. C03 should not only recognize prime contractors when a direct signed subcontract has its own value, delivery, and margin bridge.
- Victek / Firstec: these are defense-beta basket counterexamples. They are real defense names, but the trigger was geopolitical fear, not a named sovereign framework, executive contract, funded order, or backlog conversion.

## 5. Machine-readable trigger rows JSONL

```jsonl
{"case_id":"C03-163-01","ticker":"064350","name":"Hyundai Rotem","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"defense_export_framework_to_executive_contract_vs_theme_only_basket","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-29","entry_date":"2022-08-30","entry_price":29450.0,"MFE_30D_pct":4.41,"MAE_30D_pct":-20.88,"MFE_90D_pct":9.68,"MAE_90D_pct":-21.73,"MFE_180D_pct":28.35,"MAE_180D_pct":-21.73,"peak_180D_date":"2023-04-25","trough_180D_date":"2022-10-27","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180","evidence_url":"https://en.yna.co.kr/view/AEN20220829002100320","evidence_family":"Poland K2 executive contract / 180 tanks / framework-to-contract conversion","classification":"positive_with_high_MAE_4B_guard","outcome":"signed K2 Poland executive contract translated into 180D upside, but the first 90D path carried a deep macro/entry MAE","current_profile_error":"would over-promote if high-MAE guard is ignored; should be Stage2-Actionable + 4B-watch overlay, not immediate Green","raw_component_score_breakdown":{"eps_fcf_explosion":58,"visibility":83,"bottleneck_pricing":67,"mispricing":55,"valuation_rerating":61,"capital_allocation":45,"information_confidence":86},"current_profile_stress_test":{"baseline_current_proxy":"e2r_2_1_stock_web_calibrated","expected_stage_after_shadow_rule":"Stage2-Actionable + local_4B_watch","profile_error_flag":true}}
{"case_id":"C03-163-02","ticker":"047810","name":"Korea Aerospace Industries","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"defense_export_framework_to_executive_contract_vs_theme_only_basket","trigger_type":"Stage2-Actionable","trigger_date":"2022-09-16","entry_date":"2022-09-19","entry_price":48900.0,"MFE_30D_pct":7.57,"MAE_30D_pct":-18.2,"MFE_90D_pct":7.57,"MAE_90D_pct":-18.2,"MFE_180D_pct":24.74,"MAE_180D_pct":-18.2,"peak_180D_date":"2023-04-25","trough_180D_date":"2022-10-13","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180","evidence_url":"https://en.yna.co.kr/view/AEN20220916008651325","evidence_family":"Poland FA-50 executive contract following July framework","classification":"positive_watch_not_green","outcome":"FA-50 Poland executive contract produced 180D MFE above 20%, but weak 30/90D tape argues for staged entry rather than Green","current_profile_error":"if only signed framework/executive language is read, it may miss the slow conversion and intermediate drawdown","raw_component_score_breakdown":{"eps_fcf_explosion":51,"visibility":78,"bottleneck_pricing":61,"mispricing":52,"valuation_rerating":55,"capital_allocation":43,"information_confidence":84},"current_profile_stress_test":{"baseline_current_proxy":"e2r_2_1_stock_web_calibrated","expected_stage_after_shadow_rule":"Stage2-Actionable","profile_error_flag":true}}
{"case_id":"C03-163-03","ticker":"012450","name":"Hanwha Aerospace","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"defense_export_framework_to_executive_contract_vs_theme_only_basket","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-04","entry_date":"2023-12-05","entry_price":135100.0,"MFE_30D_pct":10.66,"MAE_30D_pct":-9.1,"MFE_90D_pct":81.35,"MAE_90D_pct":-9.1,"MFE_180D_pct":144.26,"MAE_180D_pct":-9.1,"peak_180D_date":"2024-07-30","trough_180D_date":"2023-12-26","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180","evidence_url":"https://m.hanwhaaerospace.com/eng/media/newsroom/view.do?seq=374","evidence_family":"Poland K9 second executive contract / K9PL technology-transfer route","classification":"positive","outcome":"second K9 Poland executive contract plus technology-transfer/backlog visibility produced clean 90D/180D MFE with shallow MAE","current_profile_error":"none severe; useful positive anchor for C03 hard commercial bridge","raw_component_score_breakdown":{"eps_fcf_explosion":70,"visibility":88,"bottleneck_pricing":79,"mispricing":63,"valuation_rerating":76,"capital_allocation":49,"information_confidence":88},"current_profile_stress_test":{"baseline_current_proxy":"e2r_2_1_stock_web_calibrated","expected_stage_after_shadow_rule":"Stage2-Actionable","profile_error_flag":false}}
{"case_id":"C03-163-04","ticker":"079550","name":"LIG Nex1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"defense_export_framework_to_executive_contract_vs_theme_only_basket","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":113400.0,"MFE_30D_pct":68.69,"MAE_30D_pct":-0.09,"MFE_90D_pct":91.36,"MAE_90D_pct":-0.09,"MFE_180D_pct":137.65,"MAE_180D_pct":-0.09,"peak_180D_date":"2024-11-06","trough_180D_date":"2024-02-08","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180","evidence_url":"https://www.reuters.com/business/aerospace-defense/saudis-agree-32-bln-deal-buy-south-korean-missile-defence-system-ministry-2024-02-06/","evidence_family":"Saudi Cheongung-II export contract / 10 batteries / ministry-confirmed","classification":"positive","outcome":"Saudi Cheongung-II order had named country, system, battery count and ministry confirmation; price path showed high MFE with almost no MAE","current_profile_error":"missed structural-momentum risk if export contract evidence is treated as just a one-day defense headline","raw_component_score_breakdown":{"eps_fcf_explosion":72,"visibility":91,"bottleneck_pricing":83,"mispricing":66,"valuation_rerating":82,"capital_allocation":52,"information_confidence":90},"current_profile_stress_test":{"baseline_current_proxy":"e2r_2_1_stock_web_calibrated","expected_stage_after_shadow_rule":"Stage2-Actionable","profile_error_flag":true}}
{"case_id":"C03-163-05","ticker":"079550","name":"LIG Nex1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"defense_export_framework_to_executive_contract_vs_theme_only_basket","trigger_type":"Stage2-Watch","trigger_date":"2024-09-20","entry_date":"2024-09-23","entry_price":214500.0,"MFE_30D_pct":25.87,"MAE_30D_pct":-3.03,"MFE_90D_pct":26.57,"MAE_90D_pct":-21.31,"MFE_180D_pct":203.03,"MAE_180D_pct":-21.31,"peak_180D_date":"2025-06-23","trough_180D_date":"2024-12-10","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180","evidence_url":"https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/","evidence_family":"Iraq Cheongung-II export order / fourth operating country expansion","classification":"positive_with_late_high_MAE_guard","outcome":"Iraq Cheongung-II order extended system export geography, but 90D MAE was deep before the later 180D MFE; should be staged, not chase","current_profile_error":"could falsely downgrade after 90D drawdown although the system-level export franchise remained intact","raw_component_score_breakdown":{"eps_fcf_explosion":68,"visibility":86,"bottleneck_pricing":80,"mispricing":54,"valuation_rerating":73,"capital_allocation":50,"information_confidence":84},"current_profile_stress_test":{"baseline_current_proxy":"e2r_2_1_stock_web_calibrated","expected_stage_after_shadow_rule":"Stage2-Actionable + local_4B_watch","profile_error_flag":true}}
{"case_id":"C03-163-06","ticker":"272210","name":"Hanwha Systems","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"defense_export_framework_to_executive_contract_vs_theme_only_basket","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-09","entry_date":"2024-07-10","entry_price":18860.0,"MFE_30D_pct":24.07,"MAE_30D_pct":-9.38,"MFE_90D_pct":60.13,"MAE_90D_pct":-12.35,"MFE_180D_pct":130.12,"MAE_180D_pct":-12.35,"peak_180D_date":"2025-03-19","trough_180D_date":"2024-09-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180","evidence_url":"https://en.yna.co.kr/view/AEN20240709007700320","evidence_family":"Saudi Cheongung-II MFR direct subcontract / second >1T KRW MFR export","classification":"positive","outcome":"Saudi MFR subcontract converted the larger LIG-led Cheongung-II order into a direct Hanwha Systems radar revenue bridge","current_profile_error":"if C03 only recognizes prime contractors, it may miss subsystem suppliers with direct signed contracts","raw_component_score_breakdown":{"eps_fcf_explosion":63,"visibility":84,"bottleneck_pricing":76,"mispricing":59,"valuation_rerating":71,"capital_allocation":46,"information_confidence":87},"current_profile_stress_test":{"baseline_current_proxy":"e2r_2_1_stock_web_calibrated","expected_stage_after_shadow_rule":"Stage2-Actionable","profile_error_flag":true}}
{"case_id":"C03-163-07","ticker":"065450","name":"Victek","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"defense_export_framework_to_executive_contract_vs_theme_only_basket","trigger_type":"Stage2-Watch","trigger_date":"2022-02-24","entry_date":"2022-02-25","entry_price":6890.0,"MFE_30D_pct":11.76,"MAE_30D_pct":-10.6,"MFE_90D_pct":11.76,"MAE_90D_pct":-30.91,"MFE_180D_pct":11.76,"MAE_180D_pct":-33.38,"peak_180D_date":"2022-03-16","trough_180D_date":"2022-09-28","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180","evidence_url":"https://mbnmoney.mbn.co.kr/news/view?news_no=MM1004564510","evidence_family":"Russia-Ukraine defense-theme spike / no signed export backlog","classification":"counterexample_theme_only","outcome":"geopolitical tension lifted defense-theme names but no export framework/backlog bridge existed; 180D MFE stayed low and MAE deepened","current_profile_error":"source-proxy defense theme may still look like Stage2 if non-price bridge quality is not enforced","raw_component_score_breakdown":{"eps_fcf_explosion":22,"visibility":25,"bottleneck_pricing":31,"mispricing":45,"valuation_rerating":36,"capital_allocation":28,"information_confidence":46},"current_profile_stress_test":{"baseline_current_proxy":"e2r_2_1_stock_web_calibrated","expected_stage_after_shadow_rule":"Stage2-Watch/block","profile_error_flag":true}}
{"case_id":"C03-163-08","ticker":"010820","name":"Firstec","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"defense_export_framework_to_executive_contract_vs_theme_only_basket","trigger_type":"Stage2-Watch","trigger_date":"2022-02-24","entry_date":"2022-02-25","entry_price":4780.0,"MFE_30D_pct":4.08,"MAE_30D_pct":-22.07,"MFE_90D_pct":23.85,"MAE_90D_pct":-33.16,"MFE_180D_pct":23.85,"MAE_180D_pct":-45.5,"peak_180D_date":"2022-06-08","trough_180D_date":"2022-10-13","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180","evidence_url":"https://mbnmoney.mbn.co.kr/news/view?news_no=MM1004564510","evidence_family":"Russia-Ukraine defense-theme basket / no named export contract","classification":"counterexample_theme_only_high_MAE","outcome":"same war-tension basket produced temporary MFE but large 90D/180D MAE; price-only defense beta is not C03 framework backlog","current_profile_error":"would create false positive if market-tension rally is accepted as export backlog evidence","raw_component_score_breakdown":{"eps_fcf_explosion":24,"visibility":27,"bottleneck_pricing":30,"mispricing":42,"valuation_rerating":34,"capital_allocation":26,"information_confidence":44},"current_profile_stress_test":{"baseline_current_proxy":"e2r_2_1_stock_web_calibrated","expected_stage_after_shadow_rule":"Stage2-Actionable + local_4B_watch","profile_error_flag":true}}
```

## 6. Aggregate / residual contribution JSON
```json
{
  "row_type": "v12_aggregate_residual_contribution",
  "selected_round": "R1",
  "selected_loop": 163,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "new_independent_case_count": 8,
  "new_symbol_count": 7,
  "positive_case_count": 6,
  "counterexample_count": 2,
  "high_MAE_guard_count": 4,
  "current_profile_error_count": 6,
  "coverage_role": "Priority 2 quality-repair; URL-backed direct contract vs theme-only basket separation",
  "proposed_shadow_axis": "C03_FRAMEWORK_TO_EXECUTIVE_CONTRACT_AND_THEME_ONLY_BLOCK_GATE_V1",
  "do_not_propose_new_weight_delta": false,
  "production_scoring_changed": false
}
```

## 7. Shadow rule candidate

**C03_FRAMEWORK_TO_EXECUTIVE_CONTRACT_AND_THEME_ONLY_BLOCK_GATE_V1**

C03 should promote defense export cases only when the evidence moves through at least one hard commercial bridge and one conversion bridge.

Hard commercial bridge examples: signed sovereign executive contract, named country/customer, weapon system/platform count, contract value, funded follow-up order, direct subcontract tied to a prime export, or explicit localization/technology-transfer plan.

Conversion bridge examples: delivery schedule, backlog addition, production slot/CAPA lock, margin/revision bridge, recurring MRO/upgrade economics, or subsystem share of the prime contract.

Negative gate: geopolitical tension, “defense stocks rise,” war headline, or defense-product exposure alone must remain Stage2-Watch/block unless it later receives a signed contract/backlog bridge. This prevents Victek/Firstec-type price beta from contaminating C03 positives.

Exit/MAE overlay: even when a sovereign contract is hard, if 30D/90D MAE is below -20% while MFE is weak, classify as Stage2-Actionable + local_4B/high-MAE guard rather than Green. Hyundai Rotem 2022 and the LIG Nex1 Iraq order show why the thesis can be right while the entry path is rough.

## 8. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research. In the later batch implementation session, ingest this MD as a v12 standalone result. Parse JSONL trigger rows and aggregate rows. Use the proposed shadow axis only as a candidate C03-scoped rule. Do not loosen Stage3-Green. If implemented, add a C03-specific bridge requirement that distinguishes direct framework/executive export contracts from theme-only geopolitical defense baskets, and add a high-MAE overlay for late or macro-shocked signed-contract entries. Keep production scoring changes behind normal validation, promotion decision, and safe patch gates.
```

## 9. Next research state

```text
completed_round = R1
completed_loop = 163
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1 clearing
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C24_BIO_TRIAL_DATA_EVENT_RISK | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C15_MATERIAL_SPREAD_SUPERCYCLE | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```