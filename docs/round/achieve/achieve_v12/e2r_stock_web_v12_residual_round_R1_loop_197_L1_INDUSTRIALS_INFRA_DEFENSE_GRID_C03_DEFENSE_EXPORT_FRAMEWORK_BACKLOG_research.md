# E2R v12 residual research — R1 / L1 / C03 defense export framework backlog — loop 197

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata
```json
{
  "selected_round": "R1",
  "selected_loop": 197,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "fine_archetype_id": "mixed_c03_framework_execution_supply_chain_theme_beta_leaf_set",
  "selected_priority_bucket": "Priority 2 quality-repair after session-aware P0/P1/R13 clearing",
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "round_schedule_status": "coverage_index_selected_not_sequential",
  "round_sector_consistency": "pass",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "new_independent_case_count": 10,
  "usable_trigger_row_count": 10,
  "representative_trigger_count": 10,
  "positive_case_count": 8,
  "counterexample_count": 2,
  "stage4b_watch_or_overlay_count": 8,
  "current_profile_error_count": 8,
  "index_baseline_coverage_before": "C03 rows 62",
  "index_baseline_coverage_after_if_accepted": "C03 rows 72",
  "session_aware_note": "loop163 already covered prime Poland/Romania/Saudi/Iraq contracts and theme-only 2022 names. This loop uses new trigger dates and new supply-chain/export-momentum leaves; no hard duplicate key is reused."
}
```

### Selection rationale
- The original No-Repeat Index places C03 above the 50-row floor, so this is not a shortage-fill run. It is a Priority 2 quality-repair pass focused on URL-backed direct contract evidence, supply-chain export leaves, and theme-beta false positives.
- The previous C03 pass used Hyundai Rotem 2022 K2, KAI 2022 FA-50, Hanwha Aerospace 2023 K9, LIG Nex1 2024 Saudi/Iraq, Hanwha Systems 2024 MFR, and 2022 Victek/Firstec. This loop avoids those exact entry keys and expands into 2024~2025 contract execution, ammunition/transmission/small-arms supply-chain leaves, and June 2024 theme-only counterexamples.
- The C03 residual question is whether the evidence is a hard export/backlog bridge or merely a defense-theme vibration. The former can be Stage2-Actionable; the latter should stay Stage2-Watch or local 4B.

## 2. Price atlas validation
```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
MFE/MAE formula = max high / min low from entry row through N tradable rows versus entry close
entry_price_rule = next tradable close after trigger_date
```

Window contamination check:

| code | profile corporate-action candidates relevant to sample | decision |
|---:|---|---|
| 012450 | old 1996/1997/1999/2009 candidates only | usable |
| 064350 | 2020-08-14 candidate before sampled windows | usable |
| 047810 | no profile corporate-action candidates | usable |
| 103140 | no profile corporate-action candidates | usable |
| 003570 | old 1998/2000/2003/2006 candidates only | usable |
| 064960 | no sampled 2025~D180 overlap found in stock-web profile view | usable |
| 065450 / 010820 | old candidates only in prior profile checks; no 2024 D180 overlap | usable |

## 3. Case table

| case_id | ticker | name | trigger | entry | trigger_type | label | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE |
|---|---:|---|---:|---:|---|---|---:|---:|---:|
| C03-197-01 | 012450 | Hanwha Aerospace | 2024-04-25 | 2024-04-26 @ 235,000 | Stage2-Actionable | financing_conditional_chunmoo_positive_with_4b_guard | 6.17/-17.45 | 55.11/-17.45 | 184.26/-17.45 |
| C03-197-02 | 012450 | Hanwha Aerospace | 2024-07-09 | 2024-07-10 @ 256,500 | Stage2-Actionable | romania_k9_contract_clean_positive | 28.65/-3.7 | 65.69/-3.7 | 246.98/-3.7 |
| C03-197-03 | 064350 | Hyundai Rotem | 2024-07-29 | 2024-07-30 @ 49,600 | Stage2-Actionable | k2_poland_delivery_earnings_positive_with_mae_guard | 12.5/-17.34 | 40.12/-17.34 | 138.71/-17.34 |
| C03-197-04 | 064350 | Hyundai Rotem | 2024-10-25 | 2024-10-28 @ 63,600 | Stage2-Watch | k2_localization_near_deal_high_mae_watch_positive | 9.28/-28.07 | 61.16/-31.37 | 246.7/-31.37 |
| C03-197-05 | 047810 | Korea Aerospace Industries | 2024-02-02 | 2024-02-05 @ 49,200 | Stage2-Actionable | fa50_poland_earnings_conversion_low_mae_positive | 12.6/-2.44 | 20.93/-2.44 | 22.97/-2.44 |
| C03-197-06 | 103140 | Poongsan | 2024-02-06 | 2024-02-07 @ 39,250 | Stage2-Watch | 155mm_ammunition_mass_production_supply_chain_positive | 30.7/-4.33 | 101.02/-4.33 | 101.02/-4.33 |
| C03-197-07 | 003570 | SNT Dynamics | 2024-09-09 | 2024-09-10 @ 20,000 | Stage2-Watch | altay_transmission_export_option_positive_with_high_mae_guard | 41.0/-3.25 | 41.0/-18.7 | 175.0/-18.7 |
| C03-197-08 | 064960 | SNT Motiv | 2025-05-15 | 2025-05-16 @ 29,950 | Stage2-Watch | small_arms_export_momentum_watch_positive | 9.02/-5.51 | 33.39/-5.51 | 36.23/-5.51 |
| C03-197-09 | 065450 | Victek | 2024-06-20 | 2024-06-21 @ 5,310 | Stage2-Watch | ukraine_assistance_theme_only_false_positive | 2.07/-11.77 | 9.79/-16.57 | 9.79/-30.13 |
| C03-197-10 | 010820 | Firstec | 2024-06-20 | 2024-06-21 @ 3,305 | Stage2-Watch | theme_beta_high_mae_counterexample | 2.27/-7.87 | 18.61/-22.69 | 32.22/-22.69 |

## 4. Case notes and residual interpretation

### C03-197-01 — Hanwha Aerospace / Poland 72 Chunmoo follow-on deal with financing condition
- evidence_url: https://www.reuters.com/business/aerospace-defense/skoreas-hanwha-aerospace-deal-supply-more-rocket-launchers-poland-2024-04-25/
- evidence_family: Poland 72 Chunmoo follow-on deal with financing condition
- price path: entry 2024-04-26 close 235,000; 30D 6.17/-17.45; 90D 55.11/-17.45; 180D 184.26/-17.45.
- interpretation: Follow-on Chunmoo contract was hard enough to show export franchise depth, but financing completion condition means this is Actionable with guard, not immediate Green.
- residual read: the thesis is not false, but entry quality and bridge maturity require Stage2-Watch or local 4B/high-MAE guard rather than immediate Green.

### C03-197-02 — Hanwha Aerospace / Romania K9/K10 contract, $1bn, delivery to 2029
- evidence_url: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/
- evidence_family: Romania K9/K10 contract, $1bn, delivery to 2029
- price path: entry 2024-07-10 close 256,500; 30D 28.65/-3.7; 90D 65.69/-3.7; 180D 246.98/-3.7.
- interpretation: Sovereign buyer, platform count, support vehicles, ammunition and backlog context make this a clean C03 positive.
- residual read: hard export/backlog evidence and stock-web MFE/MAE align well enough to anchor the positive side of C03.

### C03-197-03 — Hyundai Rotem / Q2 2024 beat driven by K2 Poland deliveries and defense solutions revenue
- evidence_url: https://www.asiae.co.kr/en/article/2024072907583561098
- evidence_family: Q2 2024 beat driven by K2 Poland deliveries and defense solutions revenue
- price path: entry 2024-07-30 close 49,600; 30D 12.5/-17.34; 90D 40.12/-17.34; 180D 138.71/-17.34.
- interpretation: Deliveries had already crossed into revenue and operating profit; early Aug market drawdown still requires high-MAE/staged-entry guard.
- residual read: the thesis is not false, but entry quality and bridge maturity require Stage2-Watch or local 4B/high-MAE guard rather than immediate Green.

### C03-197-04 — Hyundai Rotem / Poland and Seoul close to K2 local production deal
- evidence_url: https://www.reuters.com/world/europe/warsaw-seoul-close-deal-on-producing-k2-tanks-in-poland-duda-says-2024-10-25/
- evidence_family: Poland and Seoul close to K2 local production deal
- price path: entry 2024-10-28 close 63,600; 30D 9.28/-28.07; 90D 61.16/-31.37; 180D 246.7/-31.37.
- interpretation: Negotiation progress had strong future value but was not yet a final executive contract; price path later worked, but the 90D MAE shows why Watch/staged entry is safer.
- residual read: the thesis is not false, but entry quality and bridge maturity require Stage2-Watch or local 4B/high-MAE guard rather than immediate Green.

### C03-197-05 — Korea Aerospace Industries / 2023 record earnings driven by FA-50 exports to Poland
- evidence_url: https://www.kedglobal.com/aerospace-defense/newsView/ked202402020012
- evidence_family: 2023 record earnings driven by FA-50 exports to Poland
- price path: entry 2024-02-05 close 49,200; 30D 12.6/-2.44; 90D 20.93/-2.44; 180D 22.97/-2.44.
- interpretation: FA-50 export revenue had already appeared in earnings; clean low-MAE path supports C03 earnings-conversion positive.
- residual read: hard export/backlog evidence and stock-web MFE/MAE align well enough to anchor the positive side of C03.

### C03-197-06 — Poongsan / DAPA plan to sign mass-production contract with Poongsan for 155mm extended-range projectile
- evidence_url: https://en.yna.co.kr/view/AEN20240206002400315
- evidence_family: DAPA plan to sign mass-production contract with Poongsan for 155mm extended-range projectile
- price path: entry 2024-02-07 close 39,250; 30D 30.7/-4.33; 90D 101.02/-4.33; 180D 101.02/-4.33.
- interpretation: Ammunition is a supply-chain leaf rather than prime-platform export, but named DAPA/Poongsan mass-production route and 155mm/K9 linkage make it C03-adjacent positive.
- residual read: the thesis is not false, but entry quality and bridge maturity require Stage2-Watch or local 4B/high-MAE guard rather than immediate Green.

### C03-197-07 — SNT Dynamics / Altay MBT transmission export contract significance and additional export expectation
- evidence_url: https://www.asiae.co.kr/en/print.htm?idxno=2024090908133222315
- evidence_family: Altay MBT transmission export contract significance and additional export expectation
- price path: entry 2024-09-10 close 20,000; 30D 41.0/-3.25; 90D 41.0/-18.7; 180D 175.0/-18.7.
- interpretation: The original Turkey BMC transmission contract was hard export evidence; 2024 additional-expectation trigger needs Watch/MAE guard because the bridge is option/backlog expansion rather than a fresh signed order.
- residual read: the thesis is not false, but entry quality and bridge maturity require Stage2-Watch or local 4B/high-MAE guard rather than immediate Green.

### C03-197-08 — SNT Motiv / SNT Motiv small-arms exports and defense-sales share rising
- evidence_url: https://www.asiae.co.kr/en/article/2025051410203122508
- evidence_family: SNT Motiv small-arms exports and defense-sales share rising
- price path: entry 2025-05-16 close 29,950; 30D 9.02/-5.51; 90D 33.39/-5.51; 180D 36.23/-5.51.
- interpretation: Defense sales and export momentum exist, but no single sovereign framework/contract amount is cited; treat as Watch positive, not full C03 Green.
- residual read: the thesis is not false, but entry quality and bridge maturity require Stage2-Watch or local 4B/high-MAE guard rather than immediate Green.

### C03-197-09 — Victek / Defense stocks rose on Korea re-evaluating Ukraine arms assistance
- evidence_url: https://pulse.mk.co.kr/news/english/11047594
- evidence_family: Defense stocks rose on Korea re-evaluating Ukraine arms assistance
- price path: entry 2024-06-21 close 5,310; 30D 2.07/-11.77; 90D 9.79/-16.57; 180D 9.79/-30.13.
- interpretation: Theme basket had geopolitical relevance but no named export framework/backlog for Victek; low 180D MFE and deep MAE block C03 Actionable.
- residual read: this is a defense-sector vibration without direct sovereign contract/backlog conversion; C03 should block Actionable despite non-price news.

### C03-197-10 — Firstec / Same Ukraine-assistance defense-theme basket without direct export bridge
- evidence_url: https://pulse.mk.co.kr/news/english/11047594
- evidence_family: Same Ukraine-assistance defense-theme basket without direct export bridge
- price path: entry 2024-06-21 close 3,305; 30D 2.27/-7.87; 90D 18.61/-22.69; 180D 32.22/-22.69.
- interpretation: Firstec has defense components, but the trigger was policy/geopolitical theme beta. Without direct framework/order/backlog evidence, this remains Stage2-Watch/false-positive guard.
- residual read: this is a defense-sector vibration without direct sovereign contract/backlog conversion; C03 should block Actionable despite non-price news.

## 5. Machine-readable trigger rows JSONL
```jsonl
{"case_id":"C03-197-01","ticker":"012450","name":"Hanwha Aerospace","trigger_date":"2024-04-25","trigger_type":"Stage2-Actionable","intended_label":"positive","result_label":"financing_conditional_chunmoo_positive_with_4b_guard","evidence_title":"Poland 72 Chunmoo follow-on deal with financing condition","evidence_url":"https://www.reuters.com/business/aerospace-defense/skoreas-hanwha-aerospace-deal-supply-more-rocket-launchers-poland-2024-04-25/","notes":"Follow-on Chunmoo contract was hard enough to show export franchise depth, but financing completion condition means this is Actionable with guard, not immediate Green.","entry_date":"2024-04-26","entry_price":235000.0,"MFE_30D_pct":6.17,"MAE_30D_pct":-17.45,"peak_30D_date":"2024-04-26","trough_30D_date":"2024-05-23","MFE_90D_pct":55.11,"MAE_90D_pct":-17.45,"peak_90D_date":"2024-10-08","trough_90D_date":"2024-05-23","MFE_180D_pct":184.26,"MAE_180D_pct":-17.45,"peak_180D_date":"2025-02-21","trough_180D_date":"2024-05-23","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|Stage2-Actionable|2024-04-26","raw_component_score_breakdown":{"eps_fcf_explosion":62,"visibility":85,"bottleneck_pricing":76,"mispricing":58,"valuation_rerating":68,"capital_allocation":46,"information_confidence":88,"total":86},"current_profile_error":true}
{"case_id":"C03-197-02","ticker":"012450","name":"Hanwha Aerospace","trigger_date":"2024-07-09","trigger_type":"Stage2-Actionable","intended_label":"positive","result_label":"romania_k9_contract_clean_positive","evidence_title":"Romania K9/K10 contract, $1bn, delivery to 2029","evidence_url":"https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/","notes":"Sovereign buyer, platform count, support vehicles, ammunition and backlog context make this a clean C03 positive.","entry_date":"2024-07-10","entry_price":256500.0,"MFE_30D_pct":28.65,"MAE_30D_pct":-3.7,"peak_30D_date":"2024-07-30","trough_30D_date":"2024-08-05","MFE_90D_pct":65.69,"MAE_90D_pct":-3.7,"peak_90D_date":"2024-11-12","trough_90D_date":"2024-08-05","MFE_180D_pct":246.98,"MAE_180D_pct":-3.7,"peak_180D_date":"2025-05-07","trough_180D_date":"2024-08-05","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|Stage2-Actionable|2024-07-10","raw_component_score_breakdown":{"eps_fcf_explosion":62,"visibility":85,"bottleneck_pricing":76,"mispricing":58,"valuation_rerating":68,"capital_allocation":46,"information_confidence":88,"total":86},"current_profile_error":false}
{"case_id":"C03-197-03","ticker":"064350","name":"Hyundai Rotem","trigger_date":"2024-07-29","trigger_type":"Stage2-Actionable","intended_label":"positive","result_label":"k2_poland_delivery_earnings_positive_with_mae_guard","evidence_title":"Q2 2024 beat driven by K2 Poland deliveries and defense solutions revenue","evidence_url":"https://www.asiae.co.kr/en/article/2024072907583561098","notes":"Deliveries had already crossed into revenue and operating profit; early Aug market drawdown still requires high-MAE/staged-entry guard.","entry_date":"2024-07-30","entry_price":49600.0,"MFE_30D_pct":12.5,"MAE_30D_pct":-17.34,"peak_30D_date":"2024-08-28","trough_30D_date":"2024-08-05","MFE_90D_pct":40.12,"MAE_90D_pct":-17.34,"peak_90D_date":"2024-11-20","trough_90D_date":"2024-08-05","MFE_180D_pct":138.71,"MAE_180D_pct":-17.34,"peak_180D_date":"2025-04-18","trough_180D_date":"2024-08-05","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|Stage2-Actionable|2024-07-30","raw_component_score_breakdown":{"eps_fcf_explosion":62,"visibility":68,"bottleneck_pricing":76,"mispricing":58,"valuation_rerating":68,"capital_allocation":46,"information_confidence":88,"total":86},"current_profile_error":true}
{"case_id":"C03-197-04","ticker":"064350","name":"Hyundai Rotem","trigger_date":"2024-10-25","trigger_type":"Stage2-Watch","intended_label":"positive","result_label":"k2_localization_near_deal_high_mae_watch_positive","evidence_title":"Poland and Seoul close to K2 local production deal","evidence_url":"https://www.reuters.com/world/europe/warsaw-seoul-close-deal-on-producing-k2-tanks-in-poland-duda-says-2024-10-25/","notes":"Negotiation progress had strong future value but was not yet a final executive contract; price path later worked, but the 90D MAE shows why Watch/staged entry is safer.","entry_date":"2024-10-28","entry_price":63600.0,"MFE_30D_pct":9.28,"MAE_30D_pct":-28.07,"peak_30D_date":"2024-11-20","trough_30D_date":"2024-12-06","MFE_90D_pct":61.16,"MAE_90D_pct":-31.37,"peak_90D_date":"2025-03-12","trough_90D_date":"2024-12-10","MFE_180D_pct":246.7,"MAE_180D_pct":-31.37,"peak_180D_date":"2025-06-23","trough_180D_date":"2024-12-10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|Stage2-Watch|2024-10-28","raw_component_score_breakdown":{"eps_fcf_explosion":62,"visibility":85,"bottleneck_pricing":76,"mispricing":58,"valuation_rerating":68,"capital_allocation":46,"information_confidence":88,"total":76},"current_profile_error":true}
{"case_id":"C03-197-05","ticker":"047810","name":"Korea Aerospace Industries","trigger_date":"2024-02-02","trigger_type":"Stage2-Actionable","intended_label":"positive","result_label":"fa50_poland_earnings_conversion_low_mae_positive","evidence_title":"2023 record earnings driven by FA-50 exports to Poland","evidence_url":"https://www.kedglobal.com/aerospace-defense/newsView/ked202402020012","notes":"FA-50 export revenue had already appeared in earnings; clean low-MAE path supports C03 earnings-conversion positive.","entry_date":"2024-02-05","entry_price":49200.0,"MFE_30D_pct":12.6,"MAE_30D_pct":-2.44,"peak_30D_date":"2024-03-11","trough_30D_date":"2024-02-05","MFE_90D_pct":20.93,"MAE_90D_pct":-2.44,"peak_90D_date":"2024-05-28","trough_90D_date":"2024-02-05","MFE_180D_pct":22.97,"MAE_180D_pct":-2.44,"peak_180D_date":"2024-10-30","trough_180D_date":"2024-02-05","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|047810|Stage2-Actionable|2024-02-05","raw_component_score_breakdown":{"eps_fcf_explosion":62,"visibility":68,"bottleneck_pricing":76,"mispricing":58,"valuation_rerating":68,"capital_allocation":46,"information_confidence":88,"total":86},"current_profile_error":false}
{"case_id":"C03-197-06","ticker":"103140","name":"Poongsan","trigger_date":"2024-02-06","trigger_type":"Stage2-Watch","intended_label":"positive","result_label":"155mm_ammunition_mass_production_supply_chain_positive","evidence_title":"DAPA plan to sign mass-production contract with Poongsan for 155mm extended-range projectile","evidence_url":"https://en.yna.co.kr/view/AEN20240206002400315","notes":"Ammunition is a supply-chain leaf rather than prime-platform export, but named DAPA/Poongsan mass-production route and 155mm/K9 linkage make it C03-adjacent positive.","entry_date":"2024-02-07","entry_price":39250.0,"MFE_30D_pct":30.7,"MAE_30D_pct":-4.33,"peak_30D_date":"2024-03-07","trough_30D_date":"2024-02-08","MFE_90D_pct":101.02,"MAE_90D_pct":-4.33,"peak_90D_date":"2024-05-14","trough_90D_date":"2024-02-08","MFE_180D_pct":101.02,"MAE_180D_pct":-4.33,"peak_180D_date":"2024-05-14","trough_180D_date":"2024-02-08","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|103140|Stage2-Watch|2024-02-07","raw_component_score_breakdown":{"eps_fcf_explosion":62,"visibility":85,"bottleneck_pricing":76,"mispricing":58,"valuation_rerating":68,"capital_allocation":46,"information_confidence":88,"total":76},"current_profile_error":true}
{"case_id":"C03-197-07","ticker":"003570","name":"SNT Dynamics","trigger_date":"2024-09-09","trigger_type":"Stage2-Watch","intended_label":"positive","result_label":"altay_transmission_export_option_positive_with_high_mae_guard","evidence_title":"Altay MBT transmission export contract significance and additional export expectation","evidence_url":"https://www.asiae.co.kr/en/print.htm?idxno=2024090908133222315","notes":"The original Turkey BMC transmission contract was hard export evidence; 2024 additional-expectation trigger needs Watch/MAE guard because the bridge is option/backlog expansion rather than a fresh signed order.","entry_date":"2024-09-10","entry_price":20000.0,"MFE_30D_pct":41.0,"MAE_30D_pct":-3.25,"peak_30D_date":"2024-10-23","trough_30D_date":"2024-09-11","MFE_90D_pct":41.0,"MAE_90D_pct":-18.7,"peak_90D_date":"2024-10-23","trough_90D_date":"2024-12-09","MFE_180D_pct":175.0,"MAE_180D_pct":-18.7,"peak_180D_date":"2025-06-13","trough_180D_date":"2024-12-09","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|003570|Stage2-Watch|2024-09-10","raw_component_score_breakdown":{"eps_fcf_explosion":62,"visibility":85,"bottleneck_pricing":76,"mispricing":58,"valuation_rerating":68,"capital_allocation":46,"information_confidence":88,"total":76},"current_profile_error":true}
{"case_id":"C03-197-08","ticker":"064960","name":"SNT Motiv","trigger_date":"2025-05-15","trigger_type":"Stage2-Watch","intended_label":"positive","result_label":"small_arms_export_momentum_watch_positive","evidence_title":"SNT Motiv small-arms exports and defense-sales share rising","evidence_url":"https://www.asiae.co.kr/en/article/2025051410203122508","notes":"Defense sales and export momentum exist, but no single sovereign framework/contract amount is cited; treat as Watch positive, not full C03 Green.","entry_date":"2025-05-16","entry_price":29950.0,"MFE_30D_pct":9.02,"MAE_30D_pct":-5.51,"peak_30D_date":"2025-06-17","trough_30D_date":"2025-06-04","MFE_90D_pct":33.39,"MAE_90D_pct":-5.51,"peak_90D_date":"2025-09-17","trough_90D_date":"2025-06-04","MFE_180D_pct":36.23,"MAE_180D_pct":-5.51,"peak_180D_date":"2025-12-08","trough_180D_date":"2025-06-04","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064960|Stage2-Watch|2025-05-16","raw_component_score_breakdown":{"eps_fcf_explosion":62,"visibility":68,"bottleneck_pricing":76,"mispricing":58,"valuation_rerating":68,"capital_allocation":46,"information_confidence":88,"total":76},"current_profile_error":true}
{"case_id":"C03-197-09","ticker":"065450","name":"Victek","trigger_date":"2024-06-20","trigger_type":"Stage2-Watch","intended_label":"counterexample","result_label":"ukraine_assistance_theme_only_false_positive","evidence_title":"Defense stocks rose on Korea re-evaluating Ukraine arms assistance","evidence_url":"https://pulse.mk.co.kr/news/english/11047594","notes":"Theme basket had geopolitical relevance but no named export framework/backlog for Victek; low 180D MFE and deep MAE block C03 Actionable.","entry_date":"2024-06-21","entry_price":5310.0,"MFE_30D_pct":2.07,"MAE_30D_pct":-11.77,"peak_30D_date":"2024-06-24","trough_30D_date":"2024-07-29","MFE_90D_pct":9.79,"MAE_90D_pct":-16.57,"peak_90D_date":"2024-08-07","trough_90D_date":"2024-09-09","MFE_180D_pct":9.79,"MAE_180D_pct":-30.13,"peak_180D_date":"2024-08-07","trough_180D_date":"2024-12-09","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|065450|Stage2-Watch|2024-06-21","raw_component_score_breakdown":{"eps_fcf_explosion":20,"visibility":30,"bottleneck_pricing":32,"mispricing":38,"valuation_rerating":34,"capital_allocation":24,"information_confidence":48,"total":54},"current_profile_error":true}
{"case_id":"C03-197-10","ticker":"010820","name":"Firstec","trigger_date":"2024-06-20","trigger_type":"Stage2-Watch","intended_label":"counterexample","result_label":"theme_beta_high_mae_counterexample","evidence_title":"Same Ukraine-assistance defense-theme basket without direct export bridge","evidence_url":"https://pulse.mk.co.kr/news/english/11047594","notes":"Firstec has defense components, but the trigger was policy/geopolitical theme beta. Without direct framework/order/backlog evidence, this remains Stage2-Watch/false-positive guard.","entry_date":"2024-06-21","entry_price":3305.0,"MFE_30D_pct":2.27,"MAE_30D_pct":-7.87,"peak_30D_date":"2024-06-21","trough_30D_date":"2024-07-03","MFE_90D_pct":18.61,"MAE_90D_pct":-22.69,"peak_90D_date":"2024-10-24","trough_90D_date":"2024-09-09","MFE_180D_pct":32.22,"MAE_180D_pct":-22.69,"peak_180D_date":"2025-03-06","trough_180D_date":"2024-09-09","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"c03_defense_export_framework_to_execution_supply_chain_vs_theme_beta_leaf","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_status":"no_candidate_overlap_entry_to_D180_from_profile_or_prior_profile_check","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|010820|Stage2-Watch|2024-06-21","raw_component_score_breakdown":{"eps_fcf_explosion":20,"visibility":30,"bottleneck_pricing":32,"mispricing":38,"valuation_rerating":34,"capital_allocation":24,"information_confidence":48,"total":54},"current_profile_error":true}
```

## 6. Aggregate / residual contribution JSON
```json
{
  "row_type": "v12_aggregate_residual_contribution",
  "selected_round": "R1",
  "selected_loop": 197,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "new_independent_case_count": 10,
  "new_symbol_count": 8,
  "positive_case_count": 8,
  "counterexample_count": 2,
  "stage4b_watch_or_overlay_count": 8,
  "current_profile_error_count": 8,
  "mean_MFE_90D_pct": 44.68,
  "mean_MAE_90D_pct": -14.01,
  "mean_MFE_180D_pct": 119.39,
  "mean_MAE_180D_pct": -15.37,
  "coverage_role": "Priority 2 quality-repair; framework-to-execution, supply-chain export leaf, and theme-beta false-positive separation",
  "proposed_shadow_axis": "C03_EXECUTION_CONTRACT_SUPPLY_CHAIN_AND_THEME_BETA_GATE_V2",
  "do_not_propose_new_weight_delta": false,
  "production_scoring_changed": false
}
```

## 7. Shadow rule candidate

```yaml
shadow_rule_candidate:
  id: C03_EXECUTION_CONTRACT_SUPPLY_CHAIN_AND_THEME_BETA_GATE_V2
  large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  production_scoring_changed: false
  do_not_propose_new_weight_delta: false
  rule_intent: >
    Separate defense export contracts and execution revenue from defense-theme beta. Promote C03 only when a sovereign/framework/executive contract, platform count, direct subcontract, funded mass-production route, or named export supply-chain bridge exists. Keep pure geopolitical theme baskets in Stage2-Watch/local 4B even when they have short MFE.
  positive_gate:
    require_any_hard_commercial_bridge:
      - sovereign buyer or named overseas customer
      - signed framework-to-executive contract or follow-on order
      - platform count, ammunition quantity, or delivery window
      - direct subcontract tied to a prime export
      - DAPA or customer-funded mass-production route for a named weapon system
    require_any_conversion_bridge:
      - deliveries already recognized in revenue / operating profit
      - backlog expansion with delivery schedule
      - supply-chain part with named platform and customer route
      - margin/revision or scale-economy bridge
  downgrade_gate:
    theme_only_or_policy_beta:
      stage: Stage2-Watch_or_local_4B
      conditions:
        - geopolitical tension without issuer-specific order
        - government policy statement without named contract
        - defense product exposure only, no backlog or delivery window
    late_or_unfinalized_export_headline:
      stage: Stage2-Watch_with_staged_entry_guard
      conditions:
        - near-deal / negotiation progress but no final contract
        - high 30D or 90D MAE despite later 180D MFE
        - financing condition or delivery long-tail not yet closed
  expected_batch_effect:
    - reduce C03 false positives from war-tension theme baskets
    - preserve prime and subsystem positives when direct commercial bridges exist
    - add high-MAE staged-entry treatment for correct but volatile defense export triggers
```

## 8. Deferred Coding Agent Handoff Prompt — do not execute in this research loop
```text
You are the later coding agent. Do not rerun this research. Ingest this MD as one v12 research artifact. Parse the JSONL trigger rows and aggregate block. If validation passes, consider C03_EXECUTION_CONTRACT_SUPPLY_CHAIN_AND_THEME_BETA_GATE_V2 only as a scoped shadow patch candidate for C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG. Do not loosen Stage3-Green. Do not treat defense-theme geopolitical news as C03 Actionable without issuer-specific contract/backlog conversion. Apply only if batch-level evidence confirms improved false-positive control while preserving hard-contract positives.
```

## 9. Next research state
```text
completed_round = R1
completed_loop = 197
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```