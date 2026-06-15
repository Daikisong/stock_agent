# E2R v12 residual research — R3 loop 135 — L3 / C13

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12

output_file = e2r_stock_web_v12_residual_round_R3_loop_135_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
selected_round = R3
selected_loop = 135
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = AMPC_IRA_JV_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_MATERIAL_SUBSIDIARY_OR_CUSTOMER_CONCENTRATION_FALSE_STAGE2

selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale

`C13_BATTERY_JV_UTILIZATION_AMPC_IRA` remains under-covered relative to the v12 target. The repository No-Repeat Index shows C13 at 15 rows / 12 symbols, below the 30-row minimum and far below the 50-row expansion target. The latest registry also already contains `R3 / C13 / loop 134`, so this run uses `selected_loop = 135`.

This run tests a narrow C13 question:

> Does the battery name have a real AMPC / IRA / JV utilization / cash-conversion bridge, or is it only wearing a localization, battery-material, or customer-label costume?

The loop is deliberately mixed:

- one positive-control / escape-hatch case where weak EV demand did not destroy the price path,
- two counterexamples where utilization or customer exposure broke the Stage2 thesis.

## 2. Price-source validation

```text
price_atlas_repo = Songdaiki/stock-web
manifest = atlas/manifest.json
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
max_date = 2026-02-20
```

Symbol profiles checked:

| symbol | company | profile status | corporate action caveat |
|---|---|---:|---|
| 373220 | LG에너지솔루션 | active_like | none in profile |
| 361610 | SK아이이테크놀로지 | active_like | none in profile |
| 006400 | 삼성SDI | active_like | old corporate-action candidates only; no 2024 window candidate |

All three trigger rows use `tradable_raw` shards and include complete 30D/90D/180D MFE/MAE.

## 3. Case table

| case | symbol | company | trigger date / entry | classification | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | residual read |
|---|---:|---|---|---|---:|---:|---:|---|
| C13-01 | 373220 | LG에너지솔루션 | 2024-07-25 / 332,500 | positive-control | +18.50 / -6.47 | +33.53 / -6.47 | +33.53 / -6.47 | demand warning was real, but diversified customer / AMPC / ESS bridge acted as escape hatch |
| C13-02 | 361610 | SK아이이테크놀로지 | 2024-05-16 / 57,600 | counterexample | +1.04 / -25.87 | +1.04 / -46.27 | +1.04 / -60.68 | separator label + parent financing stress, no utilization/cash bridge |
| C13-03 | 006400 | 삼성SDI | 2024-06-28 / 354,000 | counterexample | +10.17 / -16.81 | +11.16 / -16.81 | +11.16 / -33.47 | customer/geography concentration created limited MFE and later high-MAE fade |

## 4. Case notes

### 4.1 LG에너지솔루션 — positive-control / escape hatch

The trigger is intentionally not a clean bullish headline. LGES cut its 2024 revenue outlook and said it would ease capacity expansion because EV demand was weaker than expected. That is exactly the sort of headline that can push C12/C13 into a hard block.

But this price path did not behave like a broken Stage2. From the 2024-07-25 close of 332,500, the stock reached 394,000 by 2024-08-29 and 444,000 by 2024-10-08. The low used inside the window is 311,000 on 2024-08-05. The result is a positive-control case:

```text
MFE_30D = +18.50
MAE_30D = -6.47
MFE_90D = +33.53
MAE_90D = -6.47
MFE_180D = +33.53
MAE_180D = -6.47
```

C13 read: an EV-demand warning should not mechanically block Stage2 if the company has a plausible AMPC/IRA support layer, diversified customer base, and non-EV/ESS or mix bridge. This is an escape hatch, not a global bullish rule.

### 4.2 SK아이이테크놀로지 — counterexample

SKIET is a strong false-positive template for C13. It had battery-material / separator vocabulary, but the actual utilization and cash-conversion path was weak. The Reuters-reported sale-review context around SK Innovation / SK On and weaker EV demand makes this a financing and utilization stress case rather than a Stage2 rerating.

From the 2024-05-16 close of 57,600, the best forward high used here is only 58,200, while the path hit 30,950 on 2024-08-05 and 22,650 on 2024-12-09.

```text
MFE_30D = +1.04
MAE_30D = -25.87
MFE_90D = +1.04
MAE_90D = -46.27
MFE_180D = +1.04
MAE_180D = -60.68
```

C13 read: material-subsidiary exposure is not a utilization bridge. If parent financing stress and weak customer pull-through are visible, Stage2-Actionable should be capped or blocked.

### 4.3 삼성SDI — counterexample with limited early MFE

Samsung SDI is already a known battery name, so this is not counted as a new symbol in the broad Korean market sense. It is included because the trigger family is distinct: European customer reliance and utilization/revision pressure, not generic battery orderbook rerating.

From the 2024-06-28 close of 354,000, the stock reached 390,000 in the first forward month and 393,500 by the 90D window, but it later fell to 235,500 on 2024-11-15.

```text
MFE_30D = +10.17
MAE_30D = -16.81
MFE_90D = +11.16
MAE_90D = -16.81
MFE_180D = +11.16
MAE_180D = -33.47
```

C13 read: moderate early MFE is not enough if utilization, customer mix, and revision bridge fail to refresh. This belongs under local 4B watch / Stage2 cap, not Green.

## 5. Trigger rows JSONL

```jsonl
{"schema_family": "v12_sector_archetype_residual", "row_type": "trigger", "selected_round": "R3", "selected_loop": 135, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "AMPC_IRA_JV_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_MATERIAL_SUBSIDIARY_OR_CUSTOMER_CONCENTRATION_FALSE_STAGE2", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol": "373220", "company": "LG에너지솔루션", "case_id": "C13_373220_2024-07-25_LGES_AMPC_ESS_DIVERSIFIED_CUSTOMER_ESCAPE_HATCH", "entry_date": "2024-07-25", "entry_price": 332500, "trigger_type": "Stage2", "MFE_30D_pct": 18.5, "MAE_30D_pct": -6.47, "MFE_90D_pct": 33.53, "MAE_90D_pct": -6.47, "MFE_180D_pct": 33.53, "MAE_180D_pct": -6.47, "verdict": "positive_control", "profile_error": "missed_or_underweighted_escape_hatch", "evidence_family": "AMPC_IRA_customer_diversification_ESS_or_non_EV_bridge", "notes": "EV demand warning was real, but price path held because the case had diversified customers, AMPC/IRA support, and a possible non-EV/ESS bridge. C13 should not hard-block all battery names on demand-warning headlines."}
{"schema_family": "v12_sector_archetype_residual", "row_type": "trigger", "selected_round": "R3", "selected_loop": 135, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "AMPC_IRA_JV_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_MATERIAL_SUBSIDIARY_OR_CUSTOMER_CONCENTRATION_FALSE_STAGE2", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol": "361610", "company": "SK아이이테크놀로지", "case_id": "C13_361610_2024-05-16_SKIET_SEPARATOR_UTILIZATION_FINANCING_STRESS", "entry_date": "2024-05-16", "entry_price": 57600, "trigger_type": "Stage2", "MFE_30D_pct": 1.04, "MAE_30D_pct": -25.87, "MFE_90D_pct": 1.04, "MAE_90D_pct": -46.27, "MFE_180D_pct": 1.04, "MAE_180D_pct": -60.68, "verdict": "counterexample", "profile_error": "false_stage2_if_material_subsidiary_label_used", "evidence_family": "separator_customer_pull_utilization_parent_financing_stress", "notes": "Separator capacity/material exposure did not become utilization/cash conversion. Sale-review and SK On stress pointed to weak pull-through."}
{"schema_family": "v12_sector_archetype_residual", "row_type": "trigger", "selected_round": "R3", "selected_loop": 135, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "AMPC_IRA_JV_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_MATERIAL_SUBSIDIARY_OR_CUSTOMER_CONCENTRATION_FALSE_STAGE2", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol": "006400", "company": "삼성SDI", "case_id": "C13_006400_2024-06-28_SDI_EUROPE_CUSTOMER_EXPOSURE_UTILIZATION_RISK", "entry_date": "2024-06-28", "entry_price": 354000, "trigger_type": "Stage2", "MFE_30D_pct": 10.17, "MAE_30D_pct": -16.81, "MFE_90D_pct": 11.16, "MAE_90D_pct": -16.81, "MFE_180D_pct": 11.16, "MAE_180D_pct": -33.47, "verdict": "counterexample", "profile_error": "stage2_bonus_too_generous_without_utilization_revision_bridge", "evidence_family": "europe_customer_reliance_slowing_ev_demand_utilization_revision", "notes": "Existing C13 symbol, but new trigger family: customer/geography concentration and utilization risk. Limited MFE could not compensate for later deep MAE."}
```

## 6. Score / return alignment

| bucket | expected if profile is correct | observed | alignment |
|---|---|---|---|
| C13 positive-control with AMPC/IRA + diversified customer bridge | Stage2 allowed, but monitor demand warning | LGES produced +33.53% 90D/180D MFE with shallow MAE | aligned if escape hatch exists |
| C13 material-subsidiary / separator label without utilization bridge | Stage2 block or Watch only | SKIET produced only +1.04% MFE and -60.68% 180D MAE | false positive if scored Actionable |
| C13 customer/geography concentration with weak demand | Stage2 cap, no Green | Samsung SDI had limited MFE and -33.47% 180D MAE | false positive if promoted |

## 7. Proposed shadow rule

```text
rule_id = C13_AMPC_IRA_JV_UTILIZATION_BRIDGE_AND_FALSE_STAGE2_CAP

if canonical_archetype_id == C13_BATTERY_JV_UTILIZATION_AMPC_IRA
and trigger_type == Stage2
and (
    utilization_warning == true
    or parent_financing_stress == true
    or customer_geography_concentration_risk == true
)
and company_specific_AMPC_IRA_cash_conversion_bridge_refreshed == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
    local_4b_watch = true
```

Escape hatch:

```text
if canonical_archetype_id == C13_BATTERY_JV_UTILIZATION_AMPC_IRA
and diversified_customer_base == true
and AMPC_IRA_or_ESS_cash_bridge_visible == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    do_not_hard_block_stage2 = true
    keep_as_positive_control = true
```

## 8. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count_within_C13 = 1
same_archetype_new_symbol_count_visible_index_basis = 2
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_control_count = 1
counterexample_count = 2
current_profile_error_count = 2

sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = null
existing_axis_strengthened = C13_AMPC_IRA_cash_conversion_bridge_requirement; C13_utilization_warning_stage2_cap; C13_material_subsidiary_label_block; C13_diversified_customer_ESS_escape_hatch
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this during research.

When batch-applying v12 research artifacts, ingest this MD as a standalone v12 sector/archetype residual research file.

Focus:
- canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
- proposed shadow rule = C13_AMPC_IRA_JV_UTILIZATION_BRIDGE_AND_FALSE_STAGE2_CAP
- positive-control escape hatch = diversified customer base + AMPC/IRA/ESS cash bridge + strong MFE with shallow MAE
- false-positive block = utilization warning / parent financing stress / customer concentration without refreshed cash bridge

Use trigger rows only if price fields are complete and stock-web raw/unadjusted shard windows are valid.
Do not change production scoring directly from this file alone.
Use it as one piece of v12 rolling calibration evidence.
```

## 10. Next research state

```text
completed_round = R3
completed_loop = 135
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```
