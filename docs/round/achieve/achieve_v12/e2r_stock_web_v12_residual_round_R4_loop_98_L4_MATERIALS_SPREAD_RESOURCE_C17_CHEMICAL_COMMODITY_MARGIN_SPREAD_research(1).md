# E2R Stock-Web v12 Residual Research — R4 Loop 98 / L4 / C17

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 98
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: NCC_ETHYLENE_PETROCHEM_SPREAD_REBOUND_VS_SPECIALTY_RUBBER_LATEX_MARGIN_BRIDGE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - high_MAE_guardrail
  - commodity_spread_bridge_test
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
do_not_promote_without_exact_non_price_urls: true
```

## 1. Execution scope

This run follows the v12 stock-web residual research mode. It does **not** patch `stock_agent`, does **not** change production scoring, and does **not** run live discovery.

The selected canonical is `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`. The aim is to separate:

```text
commodity / feedstock / chemical rebound label
    from
actual product-spread → utilization → gross margin / OPM → FCF / revision bridge
```

The core failure pattern is simple: the market often treats lower naphtha, restocking, China stimulus, solar/polysilicon rebound, or generic petrochemical spread as a rerating trigger. C17 should only promote that path when the spread is captured by the company rather than leaking into inventory losses, weak utilization, or delayed cash conversion.

## 2. Price source validation

```json
{
  "price_source": "Songdaiki/stock-web",
  "source_basis": "FinanceData/marcap transformed into assistant-readable symbol-year CSV shards",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "manifest_max_date": "2026-02-20",
  "corporate_action_policy": "block contaminated windows by default",
  "current_file_uses_corporate_action_window": false
}
```

The selected 2024 windows avoid the listed corporate-action candidate dates in the relevant symbol profiles. Some symbols have old historical discontinuities, but not inside the selected 2024 trigger windows except where explicitly blocked in the profile caveat.

## 3. Novelty / no-repeat check

Registry scan shows C17 was already represented through R4 loop 97 with earlier fine labels around chlor-alkali, potash/solar chemical, polypropylene, silicone/paint, semiconductor chemicals, and oil-product event caps. This file uses a narrower fine split:

```text
NCC / ethylene petrochemical spread rebound
vs
synthetic rubber / latex specialty spread margin bridge
vs
solar chemical policy rebound without cash bridge
```

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No row in this file intentionally repeats a known prior C17 trigger family/date combination. Exact row-level hard-duplicate validation should still be rerun by the batch ingest script after this MD is added to `docs/round`.

## 4. Case table

| case | symbol | name | trigger | entry | peak high | MFE | trough low | MAE | reading |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| C17-R4L98-001 | 011170 | 롯데케미칼 | petrochemical_spread_rebound_label_without_margin_bridge | 128,700 | 140,800 | 9.4% | 76,500 | -40.56% | counterexample |
| C17-R4L98-002 | 006650 | 대한유화 | ncc_margin_spread_price_only_rebound | 148,000 | 161,000 | 8.78% | 91,500 | -38.18% | counterexample |
| C17-R4L98-003 | 011780 | 금호석유화학 | synthetic_rubber_latex_spread_margin_bridge | 130,200 | 167,000 | 28.26% | 120,700 | -7.3% | positive_asymmetry |
| C17-R4L98-004 | 009830 | 한화솔루션 | solar_chemical_policy_rebound_without_spread_cash_bridge | 32,250 | 34,300 | 6.36% | 24,900 | -22.79% | counterexample |

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 98, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NCC_ETHYLENE_PETROCHEM_SPREAD_REBOUND_VS_EARNINGS_MARGIN_BRIDGE_FAILURE", "case_id": "C17-R4L98-001", "symbol": "011170", "name": "롯데케미칼", "trigger_type": "petrochemical_spread_rebound_label_without_margin_bridge", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 128700, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "forward_window": "post_entry_observed_to_2024-10-31_or_available_segment", "peak_date": "2024-02-01", "peak_high": 140800, "mfe_pct": 9.4, "trough_date": "2024-09-09/2024-09-10", "trough_low": 76500, "mae_pct": -40.56, "classification": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "do_not_promote_without_exact_non_price_urls": true, "novelty_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|petrochemical_spread_rebound_label_without_margin_bridge|2024-01-24"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 98, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "PURE_NCC_SPREAD_RESTOCKING_BOUNCE_VS_UTILIZATION_MARGIN_FCF_BREAK", "case_id": "C17-R4L98-002", "symbol": "006650", "name": "대한유화", "trigger_type": "ncc_margin_spread_price_only_rebound", "trigger_date": "2024-04-11", "entry_date": "2024-04-11", "entry_price": 148000, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "forward_window": "post_entry_observed_to_2024-10-31_or_available_segment", "peak_date": "2024-05-20", "peak_high": 161000, "mfe_pct": 8.78, "trough_date": "2024-09-10", "trough_low": 91500, "mae_pct": -38.18, "classification": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "do_not_promote_without_exact_non_price_urls": true, "novelty_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|006650|ncc_margin_spread_price_only_rebound|2024-04-11"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 98, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_LATEX_SPREAD_MARGIN_BRIDGE_VS_GENERIC_CHEMICAL_LABEL", "case_id": "C17-R4L98-003", "symbol": "011780", "name": "금호석유화학", "trigger_type": "synthetic_rubber_latex_spread_margin_bridge", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 130200, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "forward_window": "post_entry_observed_to_2024-10-31_or_available_segment", "peak_date": "2024-07-15", "peak_high": 167000, "mfe_pct": 28.26, "trough_date": "2024-08-05", "trough_low": 120700, "mae_pct": -7.3, "classification": "positive_asymmetry", "source_proxy_only": true, "evidence_url_pending": true, "do_not_promote_without_exact_non_price_urls": true, "novelty_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|synthetic_rubber_latex_spread_margin_bridge|2024-04-25"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 98, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SOLAR_CHEMICAL_POLICY_REBOUND_VS_POLYSILICON_MODULE_MARGIN_CASH_BRIDGE_FAILURE", "case_id": "C17-R4L98-004", "symbol": "009830", "name": "한화솔루션", "trigger_type": "solar_chemical_policy_rebound_without_spread_cash_bridge", "trigger_date": "2024-05-23", "entry_date": "2024-05-23", "entry_price": 32250, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_source": "Songdaiki/stock-web", "forward_window": "post_entry_observed_to_2024-10-31_or_available_segment", "peak_date": "2024-06-12", "peak_high": 34300, "mfe_pct": 6.36, "trough_date": "2024-07-18", "trough_low": 24900, "mae_pct": -22.79, "classification": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "do_not_promote_without_exact_non_price_urls": true, "novelty_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|009830|solar_chemical_policy_rebound_without_spread_cash_bridge|2024-05-23"}
```

## 6. Case notes

### C17-R4L98-001 — 011170 롯데케미칼

The January rebound looked like a classic petrochemical low-base / spread turn. Price gave a short MFE, but the later path shows why generic NCC beta should not be enough for Stage3-Green. The observed path was:

```text
entry close 128,700 → peak high 140,800 → trough low 76,500
MFE +9.40%, MAE -40.56%
```

Interpretation:

```text
commodity spread headline alone = not enough
need: spread capture + utilization + quarterly margin bridge + FCF/revision
otherwise: Stage2-watch or Yellow/event-cap only
```

### C17-R4L98-002 — 006650 대한유화

This is the cleaner pure-NCC stress test. The local rebound created tradable MFE, but the future low was much deeper than the upside. This is a classic residual error if the profile rewards chemical restocking too early.

```text
entry close 148,000 → peak high 161,000 → trough low 91,500
MFE +8.78%, MAE -38.18%
```

Shadow reading:

```text
Stage2 bonus must require realized utilization and margin bridge.
If the evidence is only "spread/restocking/beta", block Green and route to 4B watch.
```

### C17-R4L98-003 — 011780 금호석유화학

This is the positive asymmetry case. Synthetic rubber / latex / specialty product spread behaved better than generic petrochemical beta. C17 should avoid flattening all chemical spread cases into one bucket.

```text
entry close 130,200 → peak high 167,000 → trough low 120,700
MFE +28.26%, MAE -7.30%
```

Shadow reading:

```text
specialty product spread + product mix + inventory discipline can deserve Stage2→Yellow.
Green still requires revision and cash-flow confirmation.
```

### C17-R4L98-004 — 009830 한화솔루션

This case catches solar/chemical policy rebound leakage. The chart produced a local MFE, but without module/polysilicon spread capture and cash conversion the path quickly turned against the entry.

```text
entry close 32,250 → peak high 34,300 → trough low 24,900
MFE +6.36%, MAE -22.79%
```

Shadow reading:

```text
solar/chemical policy rebound is event-cap unless margin and cash conversion bridge are visible.
```

## 7. Aggregate metrics

```json
{
  "row_count": 4,
  "positive_asymmetry_rows": 1,
  "counterexample_rows": 3,
  "avg_mfe_pct": 13.2,
  "avg_mae_pct": -27.21,
  "median_mfe_pct": 9.09,
  "median_mae_pct": -30.48,
  "best_mfe_pct": 28.26,
  "worst_mae_pct": -40.56
}
```

Interpretation:

```text
C17 is not a "chemical rebound = Stage2" bucket.
The average upside was +13.20%, but the average drawdown was -27.21%.
The only clean positive asymmetry came from product-spread/specialty-chemical bridge, not broad petrochemical beta.
```

## 8. Current calibrated profile stress test

| rule axis | observed residual | suggested shadow rule |
|---|---|---|
| Stage2 actionable evidence | Generic spread/rebound labels can pass too easily | Require at least one non-price bridge: product spread capture, utilization, margin guidance, inventory normalization, or FCF/revision |
| 4B local vs full window | Local MFE often appears before large drawdown | If MFE < 10% and MAE < -20%, route to 4B watch instead of Green |
| C17 scope split | Specialty rubber/latex behaves differently from broad NCC/solar | Add fine-archetype weighting: specialty product spread > generic NCC beta |
| high-MAE guardrail | Lotte/대한유화/한화솔루션 show deep future MAE | Require high-MAE guardrail before Stage3-Green promotion |

## 9. Raw component score sketches

These are **shadow-only** diagnostic sketches, not production scoring changes.

| component | 011170 | 006650 | 011780 | 009830 |
|---|---:|---:|---:|---:|
| industrial/sector relevance | 14 | 15 | 16 | 13 |
| non-price evidence bridge | 4 | 3 | 10 | 4 |
| revision / margin bridge | 3 | 3 | 9 | 3 |
| price confirmation | 8 | 8 | 13 | 7 |
| risk penalty | -14 | -15 | -4 | -13 |
| suggested stage | Stage2-watch | Stage2-watch / 4B-watch | Stage2→Yellow candidate | event-cap / 4B-watch |

## 10. Shadow weight candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":98,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"stage2_required_bridge","candidate_rule":"Require company-captured spread bridge before Stage2 bonus: product spread, utilization, margin guidance, inventory normalization, or FCF/revision.","supporting_cases":["C17-R4L98-001","C17-R4L98-002","C17-R4L98-004"],"source_proxy_only":true,"evidence_url_pending":true,"apply_now":false}
{"row_type":"shadow_weight","round":"R4","loop":98,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"local_4b_watch_guard","candidate_rule":"If chemical rebound label creates MFE < 10% while forward MAE exceeds -20%, classify as 4B-watch/event-cap unless non-price bridge appears.","supporting_cases":["C17-R4L98-001","C17-R4L98-002","C17-R4L98-004"],"source_proxy_only":true,"evidence_url_pending":true,"apply_now":false}
{"row_type":"shadow_weight","round":"R4","loop":98,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"fine_archetype_positive_split","candidate_rule":"Specialty rubber/latex product-spread cases may retain Stage2→Yellow when margin bridge is visible; do not collapse them into generic NCC beta.","supporting_cases":["C17-R4L98-003"],"source_proxy_only":true,"evidence_url_pending":true,"apply_now":false}
```

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "round": "R4",
  "loop": 98,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "contribution": "Adds C17 evidence that broad petrochemical spread rebound should be capped unless captured by company-specific spread/margin/FCF bridge; contrasts with a specialty rubber/latex positive asymmetry case.",
  "promotion_readiness": "not_ready",
  "blockers": ["source_proxy_only", "evidence_url_pending", "requires_exact_non_price_urls"],
  "expected_ingest_use": ["coverage_gap_fill", "counterexample_mining", "stage2_required_bridge_candidate", "local_4b_watch_guard_candidate"]
}
```

## 12. Validation scope

```text
Validation level:
- Price rows: checked from Songdaiki/stock-web symbol-year shards.
- Non-price evidence: intentionally source_proxy_only.
- Production patch: forbidden in this run.
- Promotion: blocked until exact non-price evidence URLs are added and duplicate ingest is rerun.
```

## 13. Deferred Coding Agent Handoff Prompt

Do not execute this in the research session.

```text
You are the later batch implementation/coding agent.

Input file:
docs/round/e2r_stock_web_v12_residual_round_R4_loop_98_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md

Task:
1. Run v12 MD discovery/parser/validation/dedupe on this file.
2. Confirm hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Keep all rows blocked from promotion while source_proxy_only/evidence_url_pending are true.
4. If exact non-price URLs are later provided, consider C17 shadow candidates:
   - stage2_required_bridge for chemical spread cases
   - local_4b_watch_guard for generic petrochemical rebound
   - fine_archetype_positive_split for specialty rubber/latex spread cases
5. Do not alter production scoring unless promotion planner validates row quality.
```
