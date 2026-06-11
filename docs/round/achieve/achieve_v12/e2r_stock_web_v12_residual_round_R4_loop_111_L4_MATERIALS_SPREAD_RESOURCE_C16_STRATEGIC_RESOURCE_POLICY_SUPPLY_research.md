# E2R Stock-Web v12 Residual Calibration — R4 Loop 111 — C16 Strategic Resource Policy Supply

## 0. Execution contract

- main_execution_prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
- no_repeat_index: `docs/core/V12_Research_No_Repeat_Index.md`
- selected_round: `R4`
- selected_loop: `111`
- large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`
- canonical_archetype_id: `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`
- fine_archetype_id: `CRITICAL_MINERAL_COPPER_LITHIUM_RARE_EARTH_SUPPLY_CHAIN_OFFTAKE_BRIDGE_VS_RESOURCE_LABEL_HIGH_MAE_BLOWOFF`
- price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- stock_web_manifest_max_date: `2026-02-20`
- selection_basis: visible `V12_Research_No_Repeat_Index.md` coverage gap plus registry loop continuity
- loop_objective: `coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_supply_guardrail | canonical_archetype_compression`

## 1. Why this loop exists

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` remains an under-covered materials/resource archetype in the visible No-Repeat Index. The current row count is materially below 30/50-row coverage targets, while R13 is reserved for cross-archetype red-team only. Existing registry continuity shows C16 already reached `R4 loop 110`; therefore this handoff uses `R4 loop 111`.

This loop tests a narrow question:

> When does a strategic-resource headline become a real C16 rerating signal?

The answer is not “lithium/copper/rare-earth appeared in the article.” C16 should require a bridge from strategic-resource language into one or more of:
- named supply/offtake/customer;
- production, refining, or processing capacity;
- visible company-level margin/revision/cash conversion;
- durable supply-chain control rather than thematic price beta.

## 2. Case table

| case_id | symbol | name | entry_date | entry_price | classification | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict |
|---|---:|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| C16_LS_006260_2024_04_26_COPPER_CRITICAL_SUPPLY_CHAIN | 006260 | LS | 2024-04-26 | 127800 | positive_with_local_4b_watch | 52.43 | -6.1 | 52.43 | -26.45 | 52.43 | -33.88 | positive_but_high_MAE_watch |
| C16_POSCOINTL_047050_2024_06_17_RARE_EARTH_MAGNET_SUPPLY | 047050 | 포스코인터내셔널 | 2024-06-17 | 68400 | counterexample | 5.12 | -27.7 | 5.12 | -35.67 | 5.12 | -45.32 | stage2_block_without_direct_cash_margin_bridge |
| C16_KUMYANG_001570_2024_02_15_LITHIUM_RESOURCE_THEME | 001570 | 금양 | 2024-02-15 | 94800 | counterexample | 41.46 | -8.02 | 41.46 | -18.25 | 41.46 | -62.97 | resource_label_price_only_blowoff_high_MAE |

## 3. Case notes

### 3.1 LS / 006260 — positive, but local 4B watch

LS is not a pure “resource word” case. The group has an electrical/materials/copper supply-chain bridge through LS Cable-type infrastructure and LS MnM-type copper refining/smelting exposure. The price path validated that the market initially paid for the bridge: entry close was 127,800 on 2024-04-26, and the 30D high reached 194,800.  

But this is not a clean Green without guardrails. The same path later touched 94,000 on 2024-08-05 and 84,500 on 2024-11-18. Therefore C16 should treat the initial signal as positive only when the non-price evidence includes real supply-chain execution, and should still activate a local 4B watch after a vertical MFE.

Mechanism: copper/materials supply bridge can light the furnace, but if margin conversion and order durability do not keep feeding it, the price flame cools.

### 3.2 POSCO International / 047050 — named rare-earth magnet supply visibility, but direct cash bridge too weak

The Reuters rare-earth supply-chain map named POSCO International as a supplier of permanent magnets to automakers from 2025. That is a real non-price strategic-resource supply-chain clue, not a random keyword. However, the listed parent’s price path did not validate a durable C16 rerating at the chosen trigger date.

Entry close was 68,400 on 2024-06-17. The 30D high was only 71,900, while the 30D low already fell to 49,450. The 180D low reached 37,400. This makes it a useful C16 counterexample: a named supply-chain role still needs direct margin/revision/cash conversion before Stage2-Actionable or Green.

Mechanism: the article opens a door, but the company-level P&L bridge must walk through it.

### 3.3 Kumyang / 001570 — lithium/resource label blowoff guardrail

Kumyang is a lithium/resource-theme high-MAE guardrail case. Entry close was 94,800 on 2024-02-15 after a renewed lithium/resource narrative. The 30D high reached 134,100, but the 180D low reached 35,100.

This is the classic C16 trap: strategic-resource words create a fast MFE, but without production/offtake/cash conversion the signal behaves like a blowoff rather than a rerating. In E2R terms this should remain Stage2-blocked or local-4B-capped unless the missing non-price bridge appears.

Mechanism: a resource story is a map; offtake and cash conversion are the truck actually moving ore.

## 4. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R4", "selected_loop": "111", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_COPPER_LITHIUM_RARE_EARTH_SUPPLY_CHAIN_OFFTAKE_BRIDGE_VS_RESOURCE_LABEL_HIGH_MAE_BLOWOFF", "symbol": "006260", "name": "LS", "trigger_type": "strategic_resource_supply_chain_execution_bridge", "trigger_family": "copper_smelting_cable_materials_group_execution", "entry_date": "2024-04-26", "entry_price": 127800, "MFE_30D_pct": 52.43, "MFE_90D_pct": 52.43, "MFE_180D_pct": 52.43, "MAE_30D_pct": -6.1, "MAE_90D_pct": -26.45, "MAE_180D_pct": -33.88, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "classification": "positive_with_local_4b_watch", "profile_verdict": "positive_but_high_MAE_watch", "non_price_evidence_family": "strategic_resource_policy_supply_offtake_cash_bridge", "current_profile_error": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R4", "selected_loop": "111", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_COPPER_LITHIUM_RARE_EARTH_SUPPLY_CHAIN_OFFTAKE_BRIDGE_VS_RESOURCE_LABEL_HIGH_MAE_BLOWOFF", "symbol": "047050", "name": "포스코인터내셔널", "trigger_type": "rare_earth_magnet_supply_chain_visibility", "trigger_family": "permanent_magnet_supply_to_automakers", "entry_date": "2024-06-17", "entry_price": 68400, "MFE_30D_pct": 5.12, "MFE_90D_pct": 5.12, "MFE_180D_pct": 5.12, "MAE_30D_pct": -27.7, "MAE_90D_pct": -35.67, "MAE_180D_pct": -45.32, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "classification": "counterexample", "profile_verdict": "stage2_block_without_direct_cash_margin_bridge", "non_price_evidence_family": "strategic_resource_policy_supply_offtake_cash_bridge", "current_profile_error": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R4", "selected_loop": "111", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_COPPER_LITHIUM_RARE_EARTH_SUPPLY_CHAIN_OFFTAKE_BRIDGE_VS_RESOURCE_LABEL_HIGH_MAE_BLOWOFF", "symbol": "001570", "name": "금양", "trigger_type": "lithium_resource_policy_supply_theme", "trigger_family": "lithium_resource_label_and_battery_material_theme", "entry_date": "2024-02-15", "entry_price": 94800, "MFE_30D_pct": 41.46, "MFE_90D_pct": 41.46, "MFE_180D_pct": 41.46, "MAE_30D_pct": -8.02, "MAE_90D_pct": -18.25, "MAE_180D_pct": -62.97, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "classification": "counterexample", "profile_verdict": "resource_label_price_only_blowoff_high_MAE", "non_price_evidence_family": "strategic_resource_policy_supply_offtake_cash_bridge", "current_profile_error": true}
```

## 5. Residual contribution

```json
{
  "row_type": "residual_contribution",
  "selected_round": "R4",
  "selected_loop": "111",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "CRITICAL_MINERAL_COPPER_LITHIUM_RARE_EARTH_SUPPLY_CHAIN_OFFTAKE_BRIDGE_VS_RESOURCE_LABEL_HIGH_MAE_BLOWOFF",
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count_visible_index_basis": 3,
  "same_archetype_new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": false,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": null,
  "existing_axis_strengthened": [
    "C16_named_supply_or_offtake_bridge_requirement",
    "C16_direct_margin_revision_cash_conversion_requirement",
    "C16_resource_label_stage2_block_without_execution_bridge",
    "C16_vertical_MFE_local_4B_watch"
  ],
  "existing_axis_weakened": null,
  "next_recommended_archetypes": [
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
    "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
    "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL"
  ]
}
```

## 6. Weight / rule implication

No global weight change is proposed. The correct patch shape is local and defensive:

- Keep C16 from granting Stage2 solely on strategic-resource vocabulary.
- Require at least one of named offtake/customer, processing capacity, or company-level cash/revision conversion.
- If the signal creates large early MFE without the cash bridge, route to local 4B watch rather than Green.
- If the signal is only a lithium/copper/rare-earth label with no direct company bridge, block Stage2-Actionable.

## 7. Price-source validation

```json
{
  "row_type": "price_source_validation",
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "symbols_checked": ["006260", "047050", "001570"],
  "forward_windows": ["30D", "90D", "180D"],
  "required_mfe_mae_fields_present": true,
  "corporate_action_window_block": "no selected 2024 entry window hit listed corporate-action candidate dates in the fetched symbol profiles",
  "calibration_usable": true
}
```
