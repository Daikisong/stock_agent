# E2R v12 Residual Research — R6 L6 C22 Insurance Rate Cycle / Reserve Quality / CSM / Capital Return

```yaml
selected_round: R6
selected_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_VS_RATE_CYCLE_LABEL_FALSE_POSITIVE
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
live_candidate_mode: false
current_stock_discovery_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still marks `C22_INSURANCE_RATE_CYCLE_RESERVE` as Priority 0 with only 6 validated rows and 24 rows needed to reach the 30-row floor. The investigation point is explicitly: insurance rate cycle, reserve quality, CSM, and capital return. This run therefore fills four new independent C22 rows.

This is not a live stock scan. This is historical trigger-level residual calibration using actual `Songdaiki/stock-web` 1D OHLCV rows.

## 2. Core residual question

Insurance looks deceptively close to the prior bank/value-up archetype, but the engine is different.

For banks, the bridge is mostly `ROE/PBR -> capital return execution -> rerating`.  
For insurers, the bridge is `rate cycle / CSM / reserve quality / loss ratio -> sustainable earnings quality -> capital return capacity -> rerating`.

The current calibrated profile can still be wrong in two opposite ways:

1. **False positive:** an insurance/rate-cycle label plus a short price spike gets promoted even though reserve quality or CSM durability is weak.
2. **Delayed positive:** a real insurer with CSM/reserve/capital-return bridge may suffer an initial drawdown but later re-rate, so a simple 30D-only window underestimates the archetype.

## 3. Validation scope and price-source notes

Allowed source scope:
- `stock_agent` research artifacts: coverage and no-repeat only.
- `Songdaiki/stock-web`: mandatory actual 1D OHLCV validation.

Disallowed:
- no stock_agent code inspection
- no patch
- no live/current recommendation
- no broker/API/trading logic

Price-source caveat:
- Raw/unadjusted FinanceData/marcap-derived OHLCV.
- Old corporate-action candidate windows are blocked by default.
- All selected entries are in 2024 and outside the old corporate-action candidate windows observed in profiles.

## 4. New independent case set

| case | symbol | name | entry | trigger_type | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | classification |
|---|---:|---|---:|---|---:|---:|---:|---|
| C22_000810_2024_04_26 | 000810 | 삼성화재 | 311,500 | Stage3_Yellow | +21.99 / -3.69 | +26.32 / -3.69 | +26.32 / -3.69 | positive |
| C22_005830_2024_04_26 | 005830 | DB손해보험 | 99,900 | Stage2_Actionable | +14.31 / -7.81 | +24.12 / -7.81 | +24.12 / -7.81 | mixed_positive |
| C22_001450_2024_05_14 | 001450 | 현대해상 | 34,200 | Stage2 | +2.34 / -9.36 | +7.16 / -9.36 | +7.16 / -20.32 | counterexample |
| C22_032830_2024_02_23 | 032830 | 삼성생명 | 95,600 | Stage3_Yellow | +12.76 / -6.59 | +12.76 / -19.87 | +16.11 / -19.87 | mixed_positive |

## 5. Case notes

### 5.1 000810 삼성화재 — positive C22 bridge

Entry close on 2024-04-26 was 311,500. The follow-through was clean: the 30D high reached 380,000 and the full 90D/180D high reached 393,500, while the early trough stayed near 300,000. That creates a strong MFE/MAE asymmetry: +26.32% MFE versus -3.69% MAE.

Interpretation:
- This is the archetype’s clean positive.
- A Stage3-Yellow path is justified if non-price evidence shows reserve quality, CSM durability, and capital return capacity.
- However, even here the rule should not be “insurance label equals Green”; the positive is the bridge, not the label.

### 5.2 005830 DB손해보험 — mixed positive with drawdown

Entry close on 2024-04-26 was 99,900. The stock reached 114,200 within 30D and 124,000 by 90D, but early drawdown reached -7.81%.

Interpretation:
- Good enough for Stage2_Actionable / Yellow when reserve and capital return bridge exists.
- Not an automatic Green because the 90D path required tolerating meaningful MAE.
- The archetype benefits from a high-MAE guard rather than a pure MFE rule.

### 5.3 001450 현대해상 — false-positive / reserve quality guard

Entry close on 2024-05-14 was 34,200. The path barely reached +2.34% at 30D and +7.16% at 90D/180D, while MAE deepened to -20.32% by 180D.

Interpretation:
- This is the main counterexample.
- The model should not promote a short insurance earnings/valuation spike without reserve-quality/CSM/capital-return confirmation.
- This is a direct guardrail row for `C22_RESERVE_STRENGTH_NOT_LABEL`.

### 5.4 032830 삼성생명 — life-insurance beta with deep drawdown recovery

Entry close on 2024-02-23 was 95,600. The initial 30D path reached +12.76%, but the 90D/180D trough fell to 76,600, a -19.87% MAE, before later recovering to 111,000.

Interpretation:
- This is not a clean immediate positive even though the 180D high eventually improved.
- The profile should avoid promoting life-insurance beta to Green solely on valuation or insurance-rate-cycle narrative.
- If the bridge exists, the row supports Stage2_Actionable with drawdown-aware sizing/capping; if the bridge is absent, it should be routed to local 4B watch.

## 6. Current calibrated profile stress test

Current profile assumptions:
- `stage2_actionable_evidence_bonus = +2.0`
- `stage3_yellow_total_min = 75.0`
- `stage3_green_total_min = 87.0`
- `stage3_green_revision_min = 55.0`
- `price_only_blowoff_blocks_positive_stage = true`
- `full_4b_requires_non_price_evidence = true`
- `hard_4c_thesis_break_routes_to_4c = true`

Residual findings:
- The global rules already block simple price-only blowoff, but C22 still needs a sector/archetype bridge.
- Insurance-specific evidence must distinguish:
  - durable CSM / reserve adequacy / rate-cycle earnings quality
  - one-off value-up or dividend label
  - weak reserve quality masked by short-term price action
- 90D and 180D MAE are essential because life-insurance and reserve-quality misses can recover late but still be bad Stage3 entries.

## 7. Proposed shadow rules

### Rule A — `C22_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_REQUIRED`

Do not upgrade C22 to Stage3-Green unless at least two of the following are present:
- reserve quality or reserve release/strength signal
- CSM sustainability / new business value support
- loss ratio or combined ratio improvement
- explicit capital-return execution or payout policy
- earnings revision that is not purely market beta

### Rule B — `C22_HIGH_MAE_INSURANCE_BETA_GUARD`

If 90D MAE < -15% and evidence is mostly rate-cycle/value-up label, cap the row at Stage2 or local 4B watch.  
This catches the 삼성생명 drawdown path and the 현대해상 false-positive path.

### Rule C — `C22_RESERVE_STRENGTH_NOT_LABEL`

Insurance sector label, dividend yield, or low PBR alone is insufficient. Require insurance-specific balance-sheet/CSM/reserve evidence.

## 8. Machine-readable trigger rows

```jsonl
{"source_row_type": "trigger_row", "case_id": "C22_000810_2024_04_26_stage3_yellow_csm_capital_return_positive", "symbol": "000810", "name": "삼성화재", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_VS_RATE_CYCLE_LABEL_FALSE_POSITIVE", "trigger_type": "Stage3_Yellow", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 311500, "entry_price_source": "stock-web atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv close", "mfe_30d_pct": 21.99, "mae_30d_pct": -3.69, "mfe_90d_pct": 26.32, "mae_90d_pct": -3.69, "mfe_180d_pct": 26.32, "mae_180d_pct": -3.69, "peak_30d_date": "2024-05-17", "peak_30d_price": 380000, "trough_30d_date": "2024-05-02", "trough_30d_price": 300000, "peak_90d_date": "2024-06-28", "peak_90d_price": 393500, "trough_90d_date": "2024-05-02", "trough_90d_price": 300000, "peak_180d_date": "2024-06-28", "peak_180d_price": 393500, "trough_180d_date": "2024-05-02", "trough_180d_price": 300000, "max_drawdown_from_peak_180d_pct": -17.53, "return_alignment": "positive_followthrough_with_low_initial_MAE", "profile_residual_error": "current calibrated profile under-specifies CSM/reserve/capital-return bridge but price validates when bridge exists", "evidence_confidence": "medium_price_high_nonprice_proxy_low", "evidence_url_pending": true, "source_proxy_only": true, "novelty_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|000810|Stage3_Yellow|2024-04-26"}
{"source_row_type": "trigger_row", "case_id": "C22_005830_2024_04_26_stage2_actionable_rate_cycle_mixed_positive", "symbol": "005830", "name": "DB손해보험", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_VS_RATE_CYCLE_LABEL_FALSE_POSITIVE", "trigger_type": "Stage2_Actionable", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 99900, "entry_price_source": "stock-web atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv close", "mfe_30d_pct": 14.31, "mae_30d_pct": -7.81, "mfe_90d_pct": 24.12, "mae_90d_pct": -7.81, "mfe_180d_pct": 24.12, "mae_180d_pct": -7.81, "peak_30d_date": "2024-05-16", "peak_30d_price": 114200, "trough_30d_date": "2024-05-02", "trough_30d_price": 92100, "peak_90d_date": "2024-08-22", "peak_90d_price": 124000, "trough_90d_date": "2024-05-02", "trough_90d_price": 92100, "peak_180d_date": "2024-08-22", "peak_180d_price": 124000, "trough_180d_date": "2024-05-02", "trough_180d_price": 92100, "max_drawdown_from_peak_180d_pct": -18.06, "return_alignment": "mixed_positive_high_MAE_before_rerating_continuation", "profile_residual_error": "Stage2_Actionable bonus can work, but should require reserve quality and capital return persistence before Green", "evidence_confidence": "medium_price_high_nonprice_proxy_low", "evidence_url_pending": true, "source_proxy_only": true, "novelty_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage2_Actionable|2024-04-26"}
{"source_row_type": "trigger_row", "case_id": "C22_001450_2024_05_14_stage2_reserve_quality_false_positive", "symbol": "001450", "name": "현대해상", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_VS_RATE_CYCLE_LABEL_FALSE_POSITIVE", "trigger_type": "Stage2", "trigger_date": "2024-05-14", "entry_date": "2024-05-14", "entry_price": 34200, "entry_price_source": "stock-web atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv close", "mfe_30d_pct": 2.34, "mae_30d_pct": -9.36, "mfe_90d_pct": 7.16, "mae_90d_pct": -9.36, "mfe_180d_pct": 7.16, "mae_180d_pct": -20.32, "peak_30d_date": "2024-05-16", "peak_30d_price": 35000, "trough_30d_date": "2024-06-18", "trough_30d_price": 31000, "peak_90d_date": "2024-08-20", "peak_90d_price": 36650, "trough_90d_date": "2024-06-18", "trough_90d_price": 31000, "peak_180d_date": "2024-08-20", "peak_180d_price": 36650, "trough_180d_date": "2024-11-15", "trough_180d_price": 27250, "max_drawdown_from_peak_180d_pct": -25.65, "return_alignment": "counterexample_price_spike_fails_when_reserve_quality_and_capital_return_bridge_absent", "profile_residual_error": "insurance label and short-term earnings reaction can unlock Stage2 but should not upgrade without reserve/CSM quality", "evidence_confidence": "medium_price_high_nonprice_proxy_low", "evidence_url_pending": true, "source_proxy_only": true, "novelty_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|001450|Stage2|2024-05-14"}
{"source_row_type": "trigger_row", "case_id": "C22_032830_2024_02_23_stage3_yellow_life_insurance_drawdown_recovery", "symbol": "032830", "name": "삼성생명", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_VS_RATE_CYCLE_LABEL_FALSE_POSITIVE", "trigger_type": "Stage3_Yellow", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 95600, "entry_price_source": "stock-web atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv close", "mfe_30d_pct": 12.76, "mae_30d_pct": -6.59, "mfe_90d_pct": 12.76, "mae_90d_pct": -19.87, "mfe_180d_pct": 16.11, "mae_180d_pct": -19.87, "peak_30d_date": "2024-03-05", "peak_30d_price": 107800, "trough_30d_date": "2024-04-09", "trough_30d_price": 89300, "peak_90d_date": "2024-03-05", "peak_90d_price": 107800, "trough_90d_date": "2024-04-19", "trough_90d_price": 76600, "peak_180d_date": "2024-11-18", "peak_180d_price": 111000, "trough_180d_date": "2024-04-19", "trough_180d_price": 76600, "max_drawdown_from_peak_180d_pct": -28.94, "return_alignment": "mixed_positive_recovery_after_deep_reserve_rate_cycle_drawdown", "profile_residual_error": "current profile may overpromote life-insurance beta; requires drawdown-aware cap until CSM/reserve quality confirms", "evidence_confidence": "medium_price_high_nonprice_proxy_low", "evidence_url_pending": true, "source_proxy_only": true, "novelty_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|032830|Stage3_Yellow|2024-02-23"}
```

## 9. Machine-readable aggregate row

```json
{
  "source_row_type": "aggregate",
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "case_count": 4,
  "trigger_count": 4,
  "positive_case_count": 1,
  "mixed_positive_count": 2,
  "counterexample_count": 1,
  "local_4b_watch_count": 2,
  "current_profile_error_count": 4,
  "median_mfe_90d_pct": 18.44,
  "median_mae_90d_pct": -8.59,
  "median_mfe_180d_pct": 20.12,
  "median_mae_180d_pct": -13.84,
  "coverage_gap_static_index": "C22 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30",
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 10. Machine-readable shadow-weight proposal

```json
{
  "source_row_type": "shadow_weight",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "proposal_type": "shadow_rule_only",
  "production_scoring_changed": false,
  "rules": [
    {
      "rule_id": "C22_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_REQUIRED",
      "effect": "block Stage3-Green unless CSM/reserve quality and capital return execution are both present; allow Stage2_Actionable when at least one bridge exists",
      "suggested_shadow_delta": {
        "revision_quality": 2.0,
        "execution": 1.5,
        "valuation": -0.5
      }
    },
    {
      "rule_id": "C22_HIGH_MAE_INSURANCE_BETA_GUARD",
      "effect": "if 90D MAE < -15% and non-price reserve evidence is weak, cap at Stage2/4B-local even when 180D MFE later recovers",
      "suggested_shadow_delta": {
        "risk": -2.0,
        "price_quality": -1.0
      }
    },
    {
      "rule_id": "C22_RESERVE_STRENGTH_NOT_LABEL",
      "effect": "insurance/rate-cycle label alone cannot unlock positive stage; require loss ratio, reserve adequacy, CSM sustainability, or explicit capital return plan",
      "suggested_shadow_delta": {
        "catalyst": -1.5,
        "financial_quality": 2.0
      }
    }
  ]
}
```

## 11. Score simulation summary

```jsonl
{"source_row_type":"score_simulation","case_id":"C22_000810_2024_04_26_stage3_yellow_csm_capital_return_positive","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":82.5,"stage_proxy_before_shadow":"Stage3_Yellow","stage_proxy_after_shadow":"Stage3_Yellow","green_allowed_after_shadow":false,"reason":"positive price path, but Green requires explicit reserve/CSM/capital-return bridge"}
{"source_row_type":"score_simulation","case_id":"C22_005830_2024_04_26_stage2_actionable_rate_cycle_mixed_positive","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":78.0,"stage_proxy_before_shadow":"Stage3_Yellow","stage_proxy_after_shadow":"Stage2_Actionable","green_allowed_after_shadow":false,"reason":"MFE validates direction but early MAE requires bridge confirmation"}
{"source_row_type":"score_simulation","case_id":"C22_001450_2024_05_14_stage2_reserve_quality_false_positive","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":72.0,"stage_proxy_before_shadow":"Stage2","stage_proxy_after_shadow":"4B_Local_Watch","green_allowed_after_shadow":false,"reason":"weak MFE and -20.32% 180D MAE; reserve-quality bridge absent"}
{"source_row_type":"score_simulation","case_id":"C22_032830_2024_02_23_stage3_yellow_life_insurance_drawdown_recovery","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":80.0,"stage_proxy_before_shadow":"Stage3_Yellow","stage_proxy_after_shadow":"Stage2_Actionable","green_allowed_after_shadow":false,"reason":"late recovery exists but 90D MAE below -15% triggers insurance beta guard"}
```

## 12. Residual contribution summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
mixed_positive_count: 2
counterexample_count: 1
local_4b_watch_count: 2
current_profile_error_count: 4
auto_selected_coverage_gap_static_index: C22 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
new_axis_proposed:
  - C22_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_REQUIRED
  - C22_HIGH_MAE_INSURANCE_BETA_GUARD
  - C22_RESERVE_STRENGTH_NOT_LABEL
existing_axis_strengthened:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
  - high_MAE_guardrail
existing_axis_weakened: null
next_recommended_archetypes:
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

## 13. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in this research run.

```text
You are the later batch implementation agent for stock_agent.

Input artifact:
- e2r_stock_web_v12_residual_round_R6_loop_102_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md

Task:
- Ingest the trigger_rows, aggregate row, score_simulation rows, and shadow_weight proposal.
- Do not blindly patch production scoring.
- Add or evaluate C22-specific shadow rules only after comparing this artifact with other C22 rows.
- Required candidate rules:
  1. C22_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_REQUIRED
  2. C22_HIGH_MAE_INSURANCE_BETA_GUARD
  3. C22_RESERVE_STRENGTH_NOT_LABEL
- Preserve all 30/90/180D MFE/MAE fields.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep evidence_url_pending/source_proxy_only rows in low-trust bucket until primary evidence URLs are attached.
```

## 14. Final note

This artifact adds four C22 rows but does not claim production readiness. The price paths are validated from stock-web OHLCV shards; the non-price event evidence is intentionally marked `source_proxy_only / evidence_url_pending=true` and should remain low-trust until primary filings, IR materials, or announcement URLs are attached.
