# E2R Stock-Web v12 Residual Research — R4 Loop 89 — L4 Materials / C15 Material Spread Supercycle

```yaml
scheduled_round: R4
scheduled_loop: 89
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_CABLE_STEEL_POLYSILICON_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FADE
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Executive summary

This R4 / loop 89 residual study selects `C15_MATERIAL_SPREAD_SUPERCYCLE` rather than repeating the previous R4 loop's C17 chemical spread route. The research question is narrow:

> In material spread/cycle names, when does commodity beta become a real Stage2-Actionable trigger, and when is it only a price-and-macro mirage?

The result is **one positive-with-local-4B case and two counterexamples**:

- `006260 LS`: copper/power-cable spread and grid/cable demand beta produced a strong MFE path, but the later drawdown says C15 needs a **local 4B watch** once spread/copper enthusiasm outruns explicit order / margin / cash-conversion evidence.
- `004020 Hyundai Steel`: steel spread recovery and China-stimulus narratives did not become a durable rerating; weak construction demand and steel competition kept the path in high-MAE counterexample territory.
- `010060 OCI Holdings`: polysilicon / solar-material spread beta lacked enough realized margin bridge and collapsed into a deep 180D drawdown; this is a clean C15 Stage2 false-positive guard.

No global weight delta is proposed. The useful contribution is a **canonical C15 guardrail**: do not open Stage2-Actionable on commodity price / spread beta alone unless the company-specific bridge includes realized spread capture, volume/utilization, inventory discipline, contract/customer visibility, and EPS/FCF translation.

---

## 1. Schedule and No-Repeat check

### 1.1 Round scheduler

Previous local artifact completed `R3 / loop 89`, so this execution resolves to:

```text
scheduled_round = R4
scheduled_loop = 89
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`; therefore the round-sector gate passes.

### 1.2 No-Repeat Index use

The No-Repeat Index shows C15 as:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE
rows = 28
symbols = 11
date range = 2024-01-10~2024-05-21
good/bad S2 = 13/0
4B/4C = 3/0
URL pending/proxy = 9/9
top covered symbols = 103140(6), 012800(5), 025820(5), 004560(3), 021050(3), 001780(1)
```

To avoid hard repeats, this run avoids the top-covered symbols above and uses:

```text
006260 LS
004020 Hyundai Steel
010060 OCI Holdings
```

Hard duplicate key check:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No known hard duplicate was used from the inspected No-Repeat summary. Some symbols may appear elsewhere under other canonical routes, but the C15 row keys below are new for this run.

---

## 2. Stock-Web manifest / profile validation

Stock-web manifest snapshot used:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Profile validation:

| symbol | name | profile status | corporate action candidates | 2024~entry+180D contamination |
|---|---|---|---|---|
| `006260` | LS | active_like | 1996-01-04, 1996-12-04, 1999-06-11 | none |
| `004020` | Hyundai Steel | active_like | 1997-01-03, 1997-10-16, 1999-03-25, 1999-07-14, 2000-04-12, 2014-01-24 | none |
| `010060` | OCI Holdings | active_like | 1999-04-16, 2001-05-18, 2023-05-30, 2023-10-13 | none for 2024 entries |

All three use `tradable_raw / raw_unadjusted_marcap`. The `has_major_raw_discontinuity` flag exists for all three due to historical corporate action candidates, but none overlap the selected 2024 entry-to-D+180 windows.

---

## 3. Case selection logic

### C15 sub-archetype tested

```text
fine_archetype_id = COPPER_CABLE_STEEL_POLYSILICON_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FADE
```

C15 often begins as a commodity spread signal. The issue is that commodity price movement is an upstream wind; a company only rerates if the wind turns its own turbine. The bridge needs to show:

```text
commodity/spread beta
  -> company-specific realized spread capture
  -> volume/utilization or backlog/order visibility
  -> margin / EPS / FCF translation
  -> lower chance of inventory or price-only reversal
```

The three cases below deliberately split this chain:

1. **LS**: spread and demand beta were enough to create large MFE, but the later full-window drawdown shows why 4B watch is needed.
2. **Hyundai Steel**: spread recovery headline did not beat steel-cycle oversupply / weak demand.
3. **OCI Holdings**: polysilicon/solar material rebound narrative lacked a durable realized margin bridge.

---

## 4. Trigger-level backtest rows

### 4.1 Human-readable table

| trigger_id | symbol | name | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | outcome |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| C15_R4L89_LS_20240412 | 006260 | LS | copper_cable_spread_capacity_beta | 2024-04-12 | 122100 | +59.5% | -8.2% | +59.5% | -8.2% | +59.5% | -30.8% | positive_with_local_4B |
| C15_R4L89_HYUNDAISTEEL_20240207 | 004020 | Hyundai Steel | steel_spread_recovery_headline | 2024-02-07 | 37000 | +1.4% | -12.8% | +1.4% | -22.7% | +1.4% | -35.8% | counterexample |
| C15_R4L89_OCI_20240110 | 010060 | OCI Holdings | polysilicon_spread_rebound_headline | 2024-01-10 | 113700 | +2.4% | -20.0% | +2.4% | -19.4% | +2.4% | -42.9% | counterexample_hard_4c_candidate |

### 4.2 Price path notes

#### `006260 LS`

The selected entry is `2024-04-12`, when LS closed at 122,100 after a copper/cable material spread surge. The path quickly peaked at 194,800 on `2024-05-21`, but later fell to 84,500 on `2024-11-18`.

Interpretation:

```text
Good C15 signal:
- commodity / copper beta moved into cable/electrical equipment demand
- near-term MFE confirms market recognized the spread-cycle bridge

Residual error:
- +59.5% MFE without enough explicit forward conversion evidence should trigger local 4B watch
- later -30%+ drawdown means this cannot be promoted as a clean durable Green archetype without margin/order/FCF confirmation
```

#### `004020 Hyundai Steel`

The selected entry is `2024-02-07`, when Hyundai Steel closed at 37,000. The route was a steel-spread / China-stimulus / plate-demand recovery setup. The price never created meaningful MFE and eventually fell into a deep drawdown.

Interpretation:

```text
Bad C15 signal:
- headline was sector spread beta, not company-level spread realization
- weak construction demand and competition/oversupply made the bridge fragile
- this is a Stage2 false-positive guard against steel-cycle macro headlines
```

#### `010060 OCI Holdings`

The selected entry is `2024-01-10`, when OCI Holdings closed at 113,700 after an early polysilicon/solar-material rebound path. The subsequent price path fell below 70,000 by August.

Interpretation:

```text
Bad C15 signal:
- upstream polysilicon/solar material headline did not convert to durable margin/EPS bridge
- the 30D path already showed weak MFE and large MAE
- by 180D the case should be routed toward 4C-style thesis-break watch if the spread thesis is not repaired
```

---

## 5. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","schema_version":"v12","scheduled_round":"R4","scheduled_loop":89,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_CABLE_STEEL_POLYSILICON_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FADE","trigger_id":"C15_R4L89_LS_20240412","symbol":"006260","name":"LS","trigger_type":"copper_cable_spread_capacity_beta","trigger_family":"commodity_spread_to_company_margin_bridge","entry_date":"2024-04-12","entry_price":122100.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":59.5,"mae_30d_pct":-8.2,"mfe_90d_pct":59.5,"mae_90d_pct":-8.2,"mfe_180d_pct":59.5,"mae_180d_pct":-30.8,"peak_date_180d":"2024-05-21","peak_price_180d":194800.0,"trough_date_180d":"2024-11-18","trough_price_180d":84500.0,"stage2_result":"good_stage2_but_local_4b_required","case_verdict":"positive_with_local_4b_overlay","calibration_usable":true,"corporate_action_contaminated_180d_window":false,"non_price_evidence_strength":"medium_source_proxy_pending","source_url_status":"source_proxy_pending","do_not_propose_new_weight_delta":true}
{"row_type":"trigger","schema_version":"v12","scheduled_round":"R4","scheduled_loop":89,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_CABLE_STEEL_POLYSILICON_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FADE","trigger_id":"C15_R4L89_HYUNDAISTEEL_20240207","symbol":"004020","name":"Hyundai Steel","trigger_type":"steel_spread_recovery_headline","trigger_family":"commodity_spread_without_company_bridge","entry_date":"2024-02-07","entry_price":37000.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.4,"mae_30d_pct":-12.8,"mfe_90d_pct":1.4,"mae_90d_pct":-22.7,"mfe_180d_pct":1.4,"mae_180d_pct":-35.8,"peak_date_180d":"2024-02-13","peak_price_180d":37500.0,"trough_date_180d":"2024-09-12","trough_price_180d":23750.0,"stage2_result":"bad_stage2","case_verdict":"counterexample","calibration_usable":true,"corporate_action_contaminated_180d_window":false,"non_price_evidence_strength":"weak_source_proxy_pending","source_url_status":"source_proxy_pending","do_not_propose_new_weight_delta":true}
{"row_type":"trigger","schema_version":"v12","scheduled_round":"R4","scheduled_loop":89,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_CABLE_STEEL_POLYSILICON_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FADE","trigger_id":"C15_R4L89_OCI_20240110","symbol":"010060","name":"OCI Holdings","trigger_type":"polysilicon_spread_rebound_headline","trigger_family":"commodity_spread_without_company_bridge","entry_date":"2024-01-10","entry_price":113700.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.4,"mae_30d_pct":-20.0,"mfe_90d_pct":2.4,"mae_90d_pct":-19.4,"mfe_180d_pct":2.4,"mae_180d_pct":-42.9,"peak_date_180d":"2024-01-11","peak_price_180d":116400.0,"trough_date_180d":"2024-08-05","trough_price_180d":64900.0,"stage2_result":"bad_stage2","case_verdict":"counterexample_hard_4c_candidate","calibration_usable":true,"corporate_action_contaminated_180d_window":false,"non_price_evidence_strength":"weak_source_proxy_pending","source_url_status":"source_proxy_pending","do_not_propose_new_weight_delta":true}
```

---

## 6. Score / return alignment stress test

### 6.1 Raw component score simulation

This is not production scoring. It is a local score-return alignment simulation for later batch review.

| symbol | EPS/FCF explosion | visibility | bottleneck/pricing | mispricing | valuation rerating | capital allocation | info confidence | simulated total | corrected view |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 006260 | 13 | 13 | 17 | 12 | 12 | 3 | 3 | 73 | Stage2/Yellow, but +50% MFE should trigger local 4B watch |
| 004020 | 5 | 6 | 8 | 10 | 6 | 2 | 3 | 40 | Watch only; not Stage2 |
| 010060 | 5 | 5 | 8 | 8 | 5 | 2 | 3 | 36 | Watch/4C guard if spread thesis fails |

### 6.2 Current calibrated profile stress

Current calibrated profile already blocks price-only blowoff and requires non-price evidence for full 4B. This C15 sample supports that direction, but at the canonical level:

```text
C15-specific residual:
- commodity price beta can create fast MFE
- but without realized margin/order/FCF bridge, late buyers experience high MAE
- therefore a local 4B watch should activate earlier for spread names after large MFE if the non-price bridge stays weak
```

### 6.3 Local 4B vs full 4B split

| symbol | local 4B watch? | full 4B? | reason |
|---|---|---|---|
| 006260 | yes | no | MFE > +50% reached before durable full-window evidence; later drawdown validates local watch |
| 004020 | no | no | No meaningful MFE; Stage2 false-positive instead |
| 010060 | no | no | No meaningful MFE; hard 4C-style thesis-break candidate |

---

## 7. Aggregate rows

```jsonl
{"row_type":"aggregate_metric","schema_version":"v12","scheduled_round":"R4","scheduled_loop":89,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_CABLE_STEEL_POLYSILICON_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FADE","case_count":3,"calibration_usable_trigger_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"median_mfe_90d_pct":2.4,"median_mae_90d_pct":-19.4,"median_mfe_180d_pct":2.4,"median_mae_180d_pct":-35.8,"stage2_false_positive_count":2,"do_not_propose_new_weight_delta":true,"reason":"source_proxy_pending_and_counterexamples_dominate"}
{"row_type":"residual_contribution","schema_version":"v12","scheduled_round":"R4","scheduled_loop":89,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","contribution_type":"canonical_guardrail","contribution_label":"material_spread_beta_requires_company_specific_margin_bridge","positive_support_symbols":["006260"],"counterexample_symbols":["004020","010060"],"rule_candidate":"C15 Stage2-Actionable requires realized spread capture plus company-specific margin/EPS/FCF bridge; price-only commodity beta remains Watch. If MFE exceeds +35~50% while bridge remains weak, route to local 4B watch rather than Green.","promotion_recommendation":"hold_for_more_evidence","do_not_propose_new_weight_delta":true}
```

---

## 8. Proposed C15 shadow rule candidate

```text
Rule candidate name:
C15_MATERIAL_SPREAD_BETA_TO_MARGIN_BRIDGE_GUARD

Apply scope:
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE

Positive Stage2-Actionable bridge requires at least two of:
1. realized product-input spread improvement, not only commodity price movement
2. volume/utilization/backlog/order visibility
3. ASP or contract structure showing spread capture
4. EPS/OP/FCF upward revision or loss-narrowing
5. inventory discipline / working-capital control

Local 4B watch trigger:
- if MFE from trigger exceeds +35~50%
- and the above bridge remains weak or source_proxy_pending
- then mark local_4b_watch=true even if full 4B is not confirmed

4C / failed thesis watch:
- if MFE90 < +5% and MAE90 <= -15%
- or MFE180 < +10% and MAE180 <= -25%
- and the spread bridge remains absent
```

This is a **shadow rule only**. It should not be promoted until C15 direct source URLs are repaired and more non-proxy evidence is gathered.

---

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not apply this MD directly as a production scoring change.

Read this file as a v12 residual research artifact:
e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

Tasks:
1. Parse the machine-readable JSONL rows.
2. Validate schema fields for trigger / aggregate_metric / residual_contribution.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Confirm price source is Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
5. Do not change production scoring.
6. Treat the proposed C15 rule as hold_for_more_evidence unless direct source URLs are repaired.
7. If later promoted, implement only as a reversible canonical-archetype guard:
   C15 Stage2-Actionable requires realized spread capture + company-specific margin/EPS/FCF bridge.
8. Preserve local_4b_watch distinction from full 4B.
```

---

## 10. Final state block

```yaml
completed_round: R4
completed_loop: 89
next_round: R5
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_CABLE_STEEL_POLYSILICON_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FADE
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
loop_contribution_label: residual_error_found
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true
production_scoring_changed: false
shadow_weight_only: true
```
