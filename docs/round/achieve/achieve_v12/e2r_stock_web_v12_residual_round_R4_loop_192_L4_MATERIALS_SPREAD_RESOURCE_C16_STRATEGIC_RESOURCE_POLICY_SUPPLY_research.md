# E2R v12 residual research — R4 / L4 / C16 strategic resource policy supply — loop 192

```text
selected_round: R4
selected_loop: 192
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: mixed_c16_east_sea_gas_policy_nickel_lithium_proxy_blowoff_leaf_set
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_patch_allowed: false
live_candidate_mode: false
```

## 1. Selection and novelty check

The original No-Repeat Index shows C16 as a Priority 2 quality-repair archetype with 82 representative rows. This pass is not a count-chasing run and is selected after the session moved through C13; it returns to C16 because the direct-resource/proxy distinction still benefits from URL-backed quality repair. It is a second dedicated C16 pass after the earlier POSCO Holdings / Korea Zinc / copper proxy set, using a different leaf: **East Sea oil-and-gas policy shock plus nickel/lithium direct-commercial bridge vs proxy blowoff**.

Novelty guard:

```text
avoided_prior_C16_loop170_symbols: 005490, 010130, 025820, 012800, 103140
new_symbols_this_loop: 036460, 018670, 117580, 008970, 002360, 001120, 011810
hard_duplicate_check: no repeated canonical_archetype_id + symbol + trigger_type + entry_date from this session
```

## 2. Price source validation

```text
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
entry_price_rule: entry_date close c
mfe_mae_rule: entry 이후 30/90/180 tradable rows의 max high / min low를 entry_price와 비교
```

Profile caveats checked:

```text
036460: corporate_action_candidate_count=0; entry~D180 clean
117580: corporate_action_candidate_count=0; entry~D180 clean
018670: corporate_action_candidate_count=0; entry~D180 clean
001120: older corporate-action candidates only; 2023-11-10~D180 clean
002360: old corporate-action candidates only; 2024-06-04~D180 clean
008970: 2025-09/2025-12 candidates are outside 2024-06-04~D180 window
011810: 2024-01-05 corporate-action candidate is before 2024-01-10 entry; use with caveat, but not overlapping entry~D180
```

## 3. Case table

| case_id | ticker | trigger leaf | entry | MFE90 | MAE90 | MFE180 | MAE180 | classification |
|---|---:|---|---:|---:|---:|---:|---:|---|
| C16_L192_01_036460 | 036460 | C16_EAST_SEA_DIRECT_EXPLORATION_POLICY_BRIDGE | 2024-06-04 @ 39400 | 63.71 | -7.36 | 63.71 | -24.87 | positive_with_4b_exit_guard |
| C16_L192_02_018670 | 018670 | C16_EAST_SEA_ENERGY_PROXY_LOW_MAE_CONTROL | 2024-06-04 @ 175200 | 4.74 | -8.68 | 43.26 | -8.68 | positive_control_but_not_direct_c16 |
| C16_L192_03_117580 | 117580 | C16_CITY_GAS_THEME_PROXY_FALSE_POSITIVE | 2024-06-04 @ 12500 | 3.44 | -31.92 | 3.44 | -38.56 | counterexample |
| C16_L192_04_008970 | 008970 | C16_PIPELINE_THEME_EVENT_CAP_4B | 2024-06-04 @ 1175 | 42.81 | -31.06 | 42.81 | -50.64 | counterexample_4b |
| C16_L192_05_002360 | 002360 | C16_SHALE_RESOURCE_SEGMENT_TINY_PROXY_FALSE_POSITIVE | 2024-06-04 @ 683 | 2.05 | -27.67 | 2.05 | -34.26 | counterexample |
| C16_L192_06_001120 | 001120 | C16_NICKEL_MINE_DIRECT_ACQUISITION_COMMERCIAL_BRIDGE | 2023-11-10 @ 28150 | 14.74 | -8.35 | 27.71 | -9.77 | positive |
| C16_L192_07_011810 | 011810 | C16_LITHIUM_NICKEL_RESOURCE_OPTIONALITY_CAPITAL_RISK | 2024-01-10 @ 11420 | 4.2 | -38.09 | 4.2 | -57.97 | counterexample |


## 4. Findings

### 4.1 East Sea resource shock: direct bridge and proxy bridge must be separated

The 2024-06-03 East Sea oil/gas announcement is a clean C16 stress event because the policy/resource vocabulary was strong, but the commercial bridge differed sharply by listed company. 한국가스공사 had the closest state-resource bridge and produced a very large 30D/90D MFE, but the same row also shows a late 180D drawdown, so this is not a clean Stage3-Green unlock. It is better modeled as **Stage2-Watch → local 4B exit guard** until exploration probability, drilling result, reserve confirmation, and cost recovery become firmer.

대성에너지 and SH에너지화학 show the trap. The word “gas” created a price impulse, but the company-level money path was too thin. 대성에너지는 90D MFE가 only 3.44% while MAE90 was -31.92%; SH에너지화학 had MFE90 2.05% and MAE90 -27.67%. This is the archetypal C16 proxy false positive.

동양철관 is the 4B lesson. It produced a large first-wave MFE, but without a signed pipe order, delivery timing, or margin bridge, the same event became a 180D drawdown trap. This suggests C16 needs a **policy-proxy blowoff cap**, not just a policy-event recognition bonus.

### 4.2 Nickel/lithium direct bridge: ownership/control beats optionality vocabulary

LX인터내셔널 is the cleanest positive in this pass. The Indonesian nickel-mine acquisition had identifiable investment size, ownership/control, and strategic-resource direction. Its MFE180 was 27.71% with MAE180 -9.77%, a much better asymmetry than most proxies.

STX is the counterweight. Lithium/nickel resource optionality was real enough for a C16 watchlist, but the path lacked enough run-rate revenue, margin, and financing-quality confirmation. Entry after the January 2024 lithium-deposit news gave MFE90 4.2% and MAE90 -38.09%, then MAE180 -57.97%. C16 should not mistake “resource optionality” for “resource monetization.”

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "case_id": "C16_L192_01_036460", "ticker": "036460", "symbol_name": "한국가스공사", "symbol_name_en": "Korea Gas Corp", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_EAST_SEA_DIRECT_EXPLORATION_POLICY_BRIDGE", "trigger_type": "4B", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 39400.0, "MFE_30D_pct": 63.71, "MAE_30D_pct": -5.2, "MFE_90D_pct": 63.71, "MAE_90D_pct": -7.36, "MFE_180D_pct": 63.71, "MAE_180D_pct": -24.87, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|036460|4B|2024-06-04", "evidence_urls": ["https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/", "https://www.kedglobal.com/energy/newsView/ked202406030013"], "case_classification": "positive_with_4b_exit_guard", "thesis_summary": "Direct state gas buyer/exploration policy beneficiary; East Sea potential reserves created a real strategic-resource policy bridge, but commercial confirmation was still probabilistic, so late 4B exit guard is needed.", "current_profile_alignment": "residual_error_or_guardrail_candidate"}
{"row_type": "trigger", "case_id": "C16_L192_02_018670", "ticker": "018670", "symbol_name": "SK가스", "symbol_name_en": "SK Gas", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_EAST_SEA_ENERGY_PROXY_LOW_MAE_CONTROL", "trigger_type": "Stage2-Watch", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 175200.0, "MFE_30D_pct": 4.74, "MAE_30D_pct": -4.62, "MFE_90D_pct": 4.74, "MAE_90D_pct": -8.68, "MFE_180D_pct": 43.26, "MAE_180D_pct": -8.68, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|018670|Stage2-Watch|2024-06-04", "evidence_urls": ["https://report.az/en/energy/south-korea-s-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast", "https://www.reuters.com/business/energy/woodside-energy-inks-lng-supply-deal-with-south-korea-2024-02-27/"], "case_classification": "positive_control_but_not_direct_c16", "thesis_summary": "Energy-distribution proxy with low initial MAE and later large MFE; useful as a control case showing that a proxy can work, but it should not be promoted as East-Sea reserve direct exposure without a separate commercial bridge.", "current_profile_alignment": "partly_aligned_but_timing_guard_needed"}
{"row_type": "trigger", "case_id": "C16_L192_03_117580", "ticker": "117580", "symbol_name": "대성에너지", "symbol_name_en": "Daesung Energy", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_CITY_GAS_THEME_PROXY_FALSE_POSITIVE", "trigger_type": "Stage2", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 12500.0, "MFE_30D_pct": 3.44, "MAE_30D_pct": -28.88, "MFE_90D_pct": 3.44, "MAE_90D_pct": -31.92, "MFE_180D_pct": 3.44, "MAE_180D_pct": -38.56, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|117580|Stage2|2024-06-04", "evidence_urls": ["https://www.kedglobal.com/energy/newsView/ked202406030013", "https://asianews.network/south-korea-bets-big-on-gas-oil-prospects-in-east-sea/"], "case_classification": "counterexample", "thesis_summary": "City-gas proxy moved with the East Sea news, but no clear exploration/offtake/revenue bridge existed at company level; price path gave almost no follow-through and deep MAE.", "current_profile_alignment": "partly_aligned_but_timing_guard_needed"}
{"row_type": "trigger", "case_id": "C16_L192_04_008970", "ticker": "008970", "symbol_name": "동양철관", "symbol_name_en": "Dongyang Steel Pipe", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_PIPELINE_THEME_EVENT_CAP_4B", "trigger_type": "4B", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 1175.0, "MFE_30D_pct": 42.81, "MAE_30D_pct": -22.55, "MFE_90D_pct": 42.81, "MAE_90D_pct": -31.06, "MFE_180D_pct": 42.81, "MAE_180D_pct": -50.64, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|008970|4B|2024-06-04", "evidence_urls": ["https://asianews.network/south-korea-bets-big-on-gas-oil-prospects-in-east-sea/", "https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/"], "case_classification": "counterexample_4b", "thesis_summary": "Pipeline/steel-pipe proxy captured the first event-cap rally, but the strategic-resource bridge never became a signed pipe order or margin conversion; 180D MAE overwhelmed the initial MFE.", "current_profile_alignment": "residual_error_or_guardrail_candidate"}
{"row_type": "trigger", "case_id": "C16_L192_05_002360", "ticker": "002360", "symbol_name": "SH에너지화학", "symbol_name_en": "SH Energy & Chemical", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_SHALE_RESOURCE_SEGMENT_TINY_PROXY_FALSE_POSITIVE", "trigger_type": "Stage2", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 683.0, "MFE_30D_pct": 2.05, "MAE_30D_pct": -16.84, "MFE_90D_pct": 2.05, "MAE_90D_pct": -27.67, "MFE_180D_pct": 2.05, "MAE_180D_pct": -34.26, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|002360|Stage2|2024-06-04", "evidence_urls": ["https://www.marketscreener.com/quote/stock/SH-ENERGY-CHEMICAL-CO-LTD-20699876/company/", "https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/"], "case_classification": "counterexample", "thesis_summary": "Company has a resource-development/shale-gas label, but the listed-entity revenue bridge is dominated by chemicals/EPS; East-Sea vocabulary alone produced a poor price path.", "current_profile_alignment": "partly_aligned_but_timing_guard_needed"}
{"row_type": "trigger", "case_id": "C16_L192_06_001120", "ticker": "001120", "symbol_name": "LX인터내셔널", "symbol_name_en": "LX International", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_NICKEL_MINE_DIRECT_ACQUISITION_COMMERCIAL_BRIDGE", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-10", "entry_date": "2023-11-10", "entry_price": 28150.0, "MFE_30D_pct": 12.97, "MAE_30D_pct": 1.07, "MFE_90D_pct": 14.74, "MAE_90D_pct": -8.35, "MFE_180D_pct": 27.71, "MAE_180D_pct": -9.77, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001120|Stage2-Actionable|2023-11-10", "evidence_urls": ["https://www.lxinternational.com/en/news/press_view?seq=434", "https://www.kedglobal.com/corporate-investment/newsView/ked202502070006"], "case_classification": "positive", "thesis_summary": "Direct Indonesian nickel mine acquisition with ownership/management control gave a clearer critical-mineral supply-chain bridge than theme proxies; price path showed moderate MFE and controlled MAE.", "current_profile_alignment": "partly_aligned_but_timing_guard_needed"}
{"row_type": "trigger", "case_id": "C16_L192_07_011810", "ticker": "011810", "symbol_name": "STX", "symbol_name_en": "STX", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "C16_LITHIUM_NICKEL_RESOURCE_OPTIONALITY_CAPITAL_RISK", "trigger_type": "Stage2", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 11420.0, "MFE_30D_pct": 4.2, "MAE_30D_pct": -19.88, "MFE_90D_pct": 4.2, "MAE_90D_pct": -38.09, "MFE_180D_pct": 4.2, "MAE_180D_pct": -57.97, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "dedupe_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|011810|Stage2|2024-01-10", "evidence_urls": ["https://www.kedglobal.com/batteries/newsView/ked202401090008", "https://stx.co.kr/eng/business/information1_6"], "case_classification": "counterexample", "thesis_summary": "Lithium/nickel optionality was real at the narrative level, but execution/capital-market risk and weak run-rate conversion dominated; price path failed immediately.", "current_profile_alignment": "partly_aligned_but_timing_guard_needed"}
```

## 6. Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C16_L192_01_036460", "ticker": "036460", "component_score_breakdown": {"evidence_bridge": 74, "commercial_directness": 68, "conversion_visibility": 58, "valuation_timing": 52, "risk_penalty": -8, "price_path_alignment": 65}, "shadow_total_estimate": 61.8, "not_production_score": true}
{"row_type": "score_simulation", "case_id": "C16_L192_02_018670", "ticker": "018670", "component_score_breakdown": {"evidence_bridge": 74, "commercial_directness": 68, "conversion_visibility": 58, "valuation_timing": 52, "risk_penalty": -8, "price_path_alignment": 65}, "shadow_total_estimate": 61.8, "not_production_score": true}
{"row_type": "score_simulation", "case_id": "C16_L192_03_117580", "ticker": "117580", "component_score_breakdown": {"evidence_bridge": 36, "commercial_directness": 22, "conversion_visibility": 18, "valuation_timing": 20, "risk_penalty": -22, "price_path_alignment": 18}, "shadow_total_estimate": 18.4, "not_production_score": true}
{"row_type": "score_simulation", "case_id": "C16_L192_04_008970", "ticker": "008970", "component_score_breakdown": {"evidence_bridge": 46, "commercial_directness": 30, "conversion_visibility": 24, "valuation_timing": 18, "risk_penalty": -24, "price_path_alignment": 22}, "shadow_total_estimate": 23.2, "not_production_score": true}
{"row_type": "score_simulation", "case_id": "C16_L192_05_002360", "ticker": "002360", "component_score_breakdown": {"evidence_bridge": 36, "commercial_directness": 22, "conversion_visibility": 18, "valuation_timing": 20, "risk_penalty": -22, "price_path_alignment": 18}, "shadow_total_estimate": 18.4, "not_production_score": true}
{"row_type": "score_simulation", "case_id": "C16_L192_06_001120", "ticker": "001120", "component_score_breakdown": {"evidence_bridge": 74, "commercial_directness": 68, "conversion_visibility": 58, "valuation_timing": 52, "risk_penalty": -8, "price_path_alignment": 65}, "shadow_total_estimate": 61.8, "not_production_score": true}
{"row_type": "score_simulation", "case_id": "C16_L192_07_011810", "ticker": "011810", "component_score_breakdown": {"evidence_bridge": 36, "commercial_directness": 22, "conversion_visibility": 18, "valuation_timing": 20, "risk_penalty": -22, "price_path_alignment": 18}, "shadow_total_estimate": 18.4, "not_production_score": true}
```

## 7. Aggregate row

```json
{
  "row_type": "aggregate",
  "selected_round": "R4",
  "selected_loop": 192,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "new_independent_case_count": 7,
  "calibration_usable_trigger_count": 7,
  "positive_case_count": 3,
  "counterexample_count": 4,
  "stage4b_watch_or_overlay_count": 5,
  "current_profile_error_count": 5,
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "do_not_propose_new_weight_delta": false,
  "rule_candidate": "C16_DIRECT_RESOURCE_COMMERCIAL_BRIDGE_AND_POLICY_PROXY_BLOWOFF_GATE_V2"
}
```

## 8. Shadow rule candidate

```text
rule_candidate_id: C16_DIRECT_RESOURCE_COMMERCIAL_BRIDGE_AND_POLICY_PROXY_BLOWOFF_GATE_V2
scope: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
production_scoring_changed: false
shadow_weight_only: true
```

Proposed rule in plain language:

> In C16, policy/resource vocabulary is not enough. Require at least one **direct-resource bridge** and one **commercial-conversion bridge** before Stage2-Actionable. If the row is only a gas/pipeline/lithium/copper/nickel proxy, route it to Stage2-Watch or local 4B unless a signed offtake, mine ownership/control, production run-rate, drilling confirmation, reserve confirmation, supply contract, or margin/revenue conversion is present.

Operational gates:

```text
allow_stage2_actionable_if:
  - direct_resource_exposure in [mine ownership/control, state resource buyer/operator, signed offtake, confirmed production run-rate, named supply contract]
  - and commercial_conversion_bridge in [revenue timing, margin bridge, reserve confirmation, drilling result, cost recovery, shipment/run-rate]

route_to_stage2_watch_if:
  - policy/resource vocabulary exists
  - but company exposure is proxy-only or segment-tiny
  - or exploration probability is still unconfirmed

route_to_local4b_watch_if:
  - MFE30 >= 25 and MAE90 <= -20
  - and no commercial_conversion_bridge exists

block_stage3_green_if:
  - evidence is policy headline only
  - or proxy equity has no direct cash-flow bridge
  - or 90D/180D MAE asymmetry is severe
```

## 9. Residual contribution summary

```text
new_axis_proposed: c16_direct_resource_commercial_bridge_and_policy_proxy_blowoff_gate_v2
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|stage2_required_bridge
existing_axis_weakened: null
current_profile_error_count: 5
positive_case_count: 3
counterexample_count: 4
stage4b_watch_or_overlay_count: 5
```

This pass adds a sharper C16 distinction:

```text
policy_resource_event != listed_company_money_path
commodity_proxy != strategic_resource_supply_bridge
resource_optionality != resource_monetization
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this in the research session.

When batch-applying V12 MDs later, parse this MD as a standalone C16 residual calibration artifact.
Use trigger_rows JSONL as candidate v12 trigger rows.
Do not alter production scoring directly from this single file.
Aggregate with other C16 rows and test a shadow patch named:
C16_DIRECT_RESOURCE_COMMERCIAL_BRIDGE_AND_POLICY_PROXY_BLOWOFF_GATE_V2.

Expected implementation idea:
- For C16, add a scope-specific Stage2 bridge check requiring direct_resource_exposure + commercial_conversion_bridge.
- Penalize policy-proxy-only rows when MFE30 is high but MAE90/MAE180 deteriorates without new non-price evidence.
- Do not hard-block state-resource names with genuine operator/buyer exposure; use local 4B/staged-entry guards instead.
- Keep all changes behind shadow_weight_only until cross-file aggregate supports promotion.
```

## 11. Next research state

```text
completed_round: R4
completed_loop: 192
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
next_recommended_archetypes: C15_MATERIAL_SPREAD_SUPERCYCLE|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```
