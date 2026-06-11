# E2R Historical Calibration v12 — C02 Power Grid / Datacenter CAPEX Residual Expansion

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 0. Metadata

```yaml
selected_round: R1
selected_loop: 102
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_GRID_DATACENTER_SMALL_MIDCAP_CAPEX_ORDER_DELIVERY_BRIDGE_VS_WIRE_THEME_LATE_CHASE
result_filename: e2r_stock_web_v12_residual_round_R1_loop_102_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 2
counterexample_count: 2
local_4b_watch_count: 2
current_profile_error_count: 4
do_not_propose_new_weight_delta: false
loop_contribution_label: canonical_archetype_rule_candidate
```

---

## 1. Prompt compliance snapshot

The main execution prompt defines this as post-calibrated historical residual research, not live scanning or repository patching. It requires actual Songdaiki/stock-web OHLC rows, backtest results, score/return alignment, positive and counterexample balance, novelty checking, and complete 30/90/180 MFE/MAE fields for every trigger row.

The no-repeat index shows `C02_POWER_GRID_DATACENTER_CAPEX` at **24 rows / 15 symbols** with top-covered symbols `267260`, `010120`, `033100`, `037030`, `103590`, and `298040`. This run therefore avoids those dominant representatives and adds four lower-covered C02-adjacent symbols: `017510`, `147830`, `006340`, and `189860`.

The price atlas manifest used here is `Songdaiki/stock-web` with `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, and `max_date = 2026-02-20`.

---

## 2. Archetype thesis

C02 should not mean “anything that went up when power-grid stocks were fashionable.” The durable C02 mechanism is narrower:

```text
power_grid_or_datacenter_CAPEX
  -> company-level order/backlog or delivery visibility
  -> capacity / bottleneck / lead-time proof
  -> revenue and margin conversion
  -> price path with acceptable MAE
```

The four rows below split the mechanism into two useful buckets.

1. **Early equipment/component rows** where the market accepted the grid CAPEX story before exhaustion.
2. **Late wire/switchgear theme rows** where price already behaved like a crowded shortcut, but the company-level order/margin bridge was missing.

The practical shadow rule candidate is simple: C02 can carry strong bottleneck/visibility weight only when the bridge reaches the company’s order, shipment, capacity, or margin line. Without that bridge, a high-MFE burst becomes local 4B watch at best, and a late entry after blowoff should be scored as a Stage2 false positive risk.

---

## 3. Source and data caveats

All price rows are from `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv`.

| symbol | name | status | caveat |
|---|---|---|---|
| 017510 | 세명전기 | active_like | historical corporate-action candidates exist, but not in the 2024 study window |
| 147830 | 제룡산업 | active_like | historical corporate-action candidates exist, but not in the 2024 study window |
| 006340 | 대원전선 | active_like | historical corporate-action candidates exist, but not in the 2024 study window |
| 189860 | 서전기전 | active_like | historical corporate-action candidate exists, but not in the 2024 study window |

`source_proxy_only = true` appears in all narrative evidence rows. That means the price paths are usable for calibration, but Green unlock should remain blocked unless a later batch can attach hard source URLs for backlog/order/capacity/margin evidence.

---

## 4. Trigger-level cases

### Case A — 017510 / 세명전기 / early component breakout, later local 4B watch

```text
symbol = 017510
entry_date = 2024-04-05
entry_price = 3710
trigger_type = Stage2_Actionable
case_polarity = positive_with_local_4b_watch
```

The first decisive 2024 move appears on 2024-04-05, when the stock closed at 3710 after trading as high as 3870. The next sessions showed continued high-volume follow-through: 2024-04-12 reached 4280, 2024-04-18 reached 4410, and the later grid-basket acceleration reached 7700 on 2024-05-13 and 10000 on 2024-07-10.

The price path validates the *early* C02 trigger, but not a Green unlock. The reason is mechanical: the OHLC tape proves crowd acceptance of the grid CAPEX theme, but the non-price bridge to backlog/delivery/margin is still pending.

| window | MFE | MAE | interpretation |
|---:|---:|---:|---|
| 30D | +107.55% | -8.89% | strong positive price alignment |
| 90D | +169.54% | -8.89% | large second-leg continuation |
| 180D | +169.54% | -8.89% | no later low exceeded the initial shakeout in this checked window |

### Case B — 147830 / 제룡산업 / cleaner equipment follow-through

```text
symbol = 147830
entry_date = 2024-04-26
entry_price = 5090
trigger_type = Stage2_Actionable
case_polarity = positive
```

The 2024-04-26 row is a cleaner C02 equipment row than most wire-name chases. It closed at 5090 after a high of 5240, then continued to 6590 on 2024-04-29, 9150 on 2024-05-08, and 11680 on 2024-07-11. The important feature is not only upside; it is that the initial MAE stayed shallow relative to the upside runway.

| window | MFE | MAE | interpretation |
|---:|---:|---:|---|
| 30D | +79.76% | -2.16% | early positive path with limited initial damage |
| 90D | +129.47% | -2.16% | second leg confirms crowd acceptance |
| 180D | +129.47% | -2.16% | the best risk-adjusted row in this sample |

This is a stronger Stage2/Yellow candidate than generic wire themes, but still should not become Stage3-Green unless backlog/order/delivery evidence is added.

### Case C — 006340 / 대원전선 / late wire chase false positive

```text
symbol = 006340
entry_date = 2024-05-13
entry_price = 4885
trigger_type = Stage2_False_Positive
case_polarity = counterexample
```

Dae Won Cable is a textbook warning for C02. The stock had already moved from the 1000s to the 4000s before this entry. Entering at the late 2024-05-13 close leaves very little durable MFE and a large subsequent drawdown. The path then moved down through the 3000s and later into the low 3000s/upper 2000s in early 2025.

| window | MFE | MAE | interpretation |
|---:|---:|---:|---|
| 30D | +7.68% | -32.75% | poor reward/drawdown after late entry |
| 90D | +7.68% | -32.75% | no meaningful second leg |
| 180D | +11.57% | -39.61% | high-MAE false positive persists |

This row argues for a C02 late-chase penalty when the evidence is only “wire/grid label + already vertical price.”

### Case D — 189860 / 서전기전 / switchgear spike false positive

```text
symbol = 189860
entry_date = 2024-05-28
entry_price = 7730
trigger_type = Stage2_False_Positive
case_polarity = counterexample
```

SeoJeon Electric shows the same failure mode in a switchgear-adjacent name. The 2024-05-28 close at 7730 came after an acceleration burst. The next day reached 8450, but the path then fell sharply: 2024-06-07 was already 5840, 2024-09-06 touched 4120, and 2025-01-02 touched 3790.

| window | MFE | MAE | interpretation |
|---:|---:|---:|---|
| 30D | +9.31% | -28.20% | late entry leaves too little remaining upside |
| 90D | +9.31% | -46.70% | high-MAE guardrail should fire |
| 180D | +9.31% | -50.97% | clear Stage2 false positive route |

---

## 5. Machine-readable trigger rows

```jsonl
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 102, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_GRID_DATACENTER_SMALL_MIDCAP_CAPEX_ORDER_DELIVERY_BRIDGE_VS_WIRE_THEME_LATE_CHASE", "symbol": "017510", "name": "세명전기", "entry_date": "2024-04-05", "entry_price": 3710.0, "trigger_type": "Stage2_Actionable", "trigger_family": "grid_components_breakout_after_capex_theme_broadening", "case_polarity": "positive_with_local_4b_watch", "MFE_30D_pct": 107.55, "MAE_30D_pct": -8.89, "MFE_90D_pct": 169.54, "MAE_90D_pct": -8.89, "MFE_180D_pct": 169.54, "MAE_180D_pct": -8.89, "peak_date_proxy": "2024-07-10", "trough_date_proxy": "2024-04-08", "evidence_source": "stock-web OHLC + source_proxy_only", "evidence_url_pending": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|017510|Stage2_Actionable|2024-04-05", "calibration_usable": true, "notes": "Early grid-component breakout produced exceptional MFE, but direct company-level backlog/order evidence is pending, so it is not a clean Green unlock."}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 102, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_GRID_DATACENTER_SMALL_MIDCAP_CAPEX_ORDER_DELIVERY_BRIDGE_VS_WIRE_THEME_LATE_CHASE", "symbol": "147830", "name": "제룡산업", "entry_date": "2024-04-26", "entry_price": 5090.0, "trigger_type": "Stage2_Actionable", "trigger_family": "distribution_grid_equipment_breakout_with_low_initial_mae", "case_polarity": "positive", "MFE_30D_pct": 79.76, "MAE_30D_pct": -2.16, "MFE_90D_pct": 129.47, "MAE_90D_pct": -2.16, "MFE_180D_pct": 129.47, "MAE_180D_pct": -2.16, "peak_date_proxy": "2024-07-11", "trough_date_proxy": "2024-04-29", "evidence_source": "stock-web OHLC + source_proxy_only", "evidence_url_pending": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|147830|Stage2_Actionable|2024-04-26", "calibration_usable": true, "notes": "The path is cleaner than generic wire chases: low initial MAE, repeated follow-through, and a later second leg."}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 102, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_GRID_DATACENTER_SMALL_MIDCAP_CAPEX_ORDER_DELIVERY_BRIDGE_VS_WIRE_THEME_LATE_CHASE", "symbol": "006340", "name": "대원전선", "entry_date": "2024-05-13", "entry_price": 4885.0, "trigger_type": "Stage2_False_Positive", "trigger_family": "wire_theme_late_chase_after_first_blowoff", "case_polarity": "counterexample", "MFE_30D_pct": 7.68, "MAE_30D_pct": -32.75, "MFE_90D_pct": 7.68, "MAE_90D_pct": -32.75, "MFE_180D_pct": 11.57, "MAE_180D_pct": -39.61, "peak_date_proxy": "2024-05-14/2025-01-13", "trough_date_proxy": "2025-01-08", "evidence_source": "stock-web OHLC + source_proxy_only", "evidence_url_pending": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|006340|Stage2_False_Positive|2024-05-13", "calibration_usable": true, "notes": "Wire label alone after a multi-week move failed: small remaining MFE, large MAE, and no confirmed order/margin bridge."}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 102, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_GRID_DATACENTER_SMALL_MIDCAP_CAPEX_ORDER_DELIVERY_BRIDGE_VS_WIRE_THEME_LATE_CHASE", "symbol": "189860", "name": "서전기전", "entry_date": "2024-05-28", "entry_price": 7730.0, "trigger_type": "Stage2_False_Positive", "trigger_family": "switchgear_theme_late_chase_after_spike", "case_polarity": "counterexample", "MFE_30D_pct": 9.31, "MAE_30D_pct": -28.2, "MFE_90D_pct": 9.31, "MAE_90D_pct": -46.7, "MFE_180D_pct": 9.31, "MAE_180D_pct": -50.97, "peak_date_proxy": "2024-05-29", "trough_date_proxy": "2025-01-02", "evidence_source": "stock-web OHLC + source_proxy_only", "evidence_url_pending": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|189860|Stage2_False_Positive|2024-05-28", "calibration_usable": true, "notes": "After the spike, the remaining upside was capped while drawdown expanded; this is a late-chase guardrail row."}
```

---

## 6. Score simulation rows

```jsonl
{"row_type": "score_simulation", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "symbol": "017510", "trigger_type": "Stage2_Actionable", "raw_component_score_breakdown": {"EPS": 13, "Visibility": 13, "Bottleneck": 17, "Mismatch": 11, "Valuation": 7, "Capacity": 3, "Info": 3, "Stage2_Actionable_Bonus": 2}, "simulated_total": 69, "current_profile_error": "Understates small-cap grid component convexity but still should block Green without direct backlog evidence."}
{"row_type": "score_simulation", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "symbol": "147830", "trigger_type": "Stage2_Actionable", "raw_component_score_breakdown": {"EPS": 14, "Visibility": 15, "Bottleneck": 18, "Mismatch": 12, "Valuation": 8, "Capacity": 3, "Info": 3, "Stage2_Actionable_Bonus": 2}, "simulated_total": 75, "current_profile_error": "Clean price alignment could reach Yellow, but Green needs non-price order/delivery/margin confirmation."}
{"row_type": "score_simulation", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "symbol": "006340", "trigger_type": "Stage2_False_Positive", "raw_component_score_breakdown": {"EPS": 8, "Visibility": 8, "Bottleneck": 15, "Mismatch": 8, "Valuation": 5, "Capacity": 1, "Info": 2, "Late_Chase_Penalty": -8}, "simulated_total": 39, "current_profile_error": "Theme/bottleneck label can over-score late wire chases unless high-MAE guardrail fires."}
{"row_type": "score_simulation", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "symbol": "189860", "trigger_type": "Stage2_False_Positive", "raw_component_score_breakdown": {"EPS": 7, "Visibility": 7, "Bottleneck": 14, "Mismatch": 9, "Valuation": 4, "Capacity": 1, "Info": 2, "Late_Chase_Penalty": -10}, "simulated_total": 34, "current_profile_error": "Switchgear label without company-level contract/retention evidence creates false Stage2 risk."}
```

---

## 7. Aggregate row

```json
{
  "row_type": "aggregate",
  "selected_round": "R1",
  "selected_loop": 102,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "POWER_GRID_DATACENTER_SMALL_MIDCAP_CAPEX_ORDER_DELIVERY_BRIDGE_VS_WIRE_THEME_LATE_CHASE",
  "case_count": 4,
  "trigger_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "local_4b_watch_count": 2,
  "new_symbol_count": 4,
  "reused_case_count": 0,
  "accepted_coverage_delta_if_ingested": "C02 rows 24 -> 28",
  "dominant_error": "C02 grid/wire label can over-score late chases unless company-level order/delivery/margin bridge and high-MAE guardrail are both checked.",
  "best_positive_row": "147830|2024-04-26",
  "worst_counterexample_row": "189860|2024-05-28"
}
```

---

## 8. Shadow rule proposal

```json
{
  "row_type": "shadow_weight_candidate",
  "production_scoring_changed": false,
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "new_axis_proposed": [
    "C02_company_level_order_delivery_margin_bridge_required",
    "C02_wire_switchgear_theme_late_chase_high_MAE_guard"
  ],
  "strengthen": [
    "stage2_required_bridge",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "candidate_rules": [
    {
      "rule": "If C02 evidence includes named order/backlog/delivery/capacity/margin bridge, allow Stage2_Actionable and possible Yellow when price path confirms.",
      "shadow_delta": "+2 visibility / +2 bottleneck / +1 mismatch",
      "reason": "017510 and 147830 show large upside with manageable early MAE when the market accepts equipment/component scarcity early."
    },
    {
      "rule": "If the row is wire/switchgear label only and entry occurs after a vertical move, cap at Local_4B_Watch or Stage2_False_Positive unless non-price evidence is attached.",
      "shadow_delta": "-4 visibility / -3 info / -3 valuation-lateness",
      "reason": "006340 and 189860 show low remaining MFE with high MAE after late entries."
    }
  ]
}
```

---

## 9. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
new_axis_proposed = C02_company_level_order_delivery_margin_bridge_required | C02_wire_switchgear_theme_late_chase_high_MAE_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
current_profile_error_count = 4
```

The useful discovery is not that power-grid names went up. The useful residual is that C02 has two faces:

```text
early equipment/component scarcity + low initial MAE
  -> viable Stage2/Yellow path

late wire/switchgear label after blowoff + no company-level bridge
  -> false positive / local 4B / high-MAE guardrail
```

So C02 should behave like a transformer with two windings: the primary winding is macro CAPEX; the secondary winding is company-specific backlog and margin conversion. If the secondary is not connected, the signal hums loudly but does not deliver usable current.

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for a later batch implementation session. Do not execute this handoff during the research run.

Input artifact:
e2r_stock_web_v12_residual_round_R1_loop_102_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md

Task:
1. Parse the JSONL trigger rows, score_simulation rows, aggregate row, and shadow_weight_candidate row.
2. Validate duplicate keys against the existing registry:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. If accepted, update only research/calibration artifacts, not production scoring directly.
4. Treat all `source_proxy_only` rows as low-trust evidence until hard source URLs are attached.
5. For C02_POWER_GRID_DATACENTER_CAPEX, test a shadow rule that:
   - requires company-level order/backlog/delivery/capacity/margin bridge for positive Stage2/Yellow upgrades;
   - caps wire/switchgear theme-only late chases at Local_4B_Watch or Stage2_False_Positive when MAE is high;
   - keeps full Stage3-Green blocked unless non-price evidence confirms conversion.
6. Do not alter live scanning, brokerage API, or production scoring in this batch unless a separate explicit implementation prompt authorizes it.
```

---

## 11. Final answer fields

```text
stock_web_v12_sector_archetype_residual_calibration_md_created = true
filename = e2r_stock_web_v12_residual_round_R1_loop_102_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round = R1
selected_loop = 102
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = POWER_GRID_DATACENTER_SMALL_MIDCAP_CAPEX_ORDER_DELIVERY_BRIDGE_VS_WIRE_THEME_LATE_CHASE
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 2
counterexample_count = 2
local_4b_watch_count = 2
current_profile_error_count = 4
auto_selected_coverage_gap = C02 rows 24 -> 28 if accepted; still Priority 0, need 2 to reach 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
new_axis_proposed = C02_company_level_order_delivery_margin_bridge_required | C02_wire_switchgear_theme_late_chase_high_MAE_guard
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX_second_pass_to_30, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
