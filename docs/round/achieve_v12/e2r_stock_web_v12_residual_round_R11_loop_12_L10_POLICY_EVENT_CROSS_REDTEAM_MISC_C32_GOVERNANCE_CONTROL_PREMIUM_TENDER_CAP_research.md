# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R11
scheduled_loop: "12"
completed_round: R11
completed_loop: "12"
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP
output_file: e2r_stock_web_v12_residual_round_R11_loop_12_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
price_route_hunt_allowed: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

## 1. Current Calibrated Profile Assumption

Current proxy profile:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question is not whether price-only blowoff should be blocked. It is whether C32 control-premium events need their own polarity map: confirmed cash tender and competing counterbid on one side; non-binding preferred bidder, unresolved financing, family shareholder vote, or legal contest on the other.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 12 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| fine_archetype_id | CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| loop_objective | coverage_gap_fill, counterexample_mining, residual_false_positive_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test |

R11 is treated as a policy/event/cross-redteam round. C32 belongs here because public tender offers, court decisions, sale negotiations, governance battles, and control-premium caps are discrete event structures rather than ordinary operating-cycle reratings.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact scope was used only for duplicate avoidance. No `stock_agent` source code was opened. The previous local v12 state completed R10/loop12, so the sequential scheduler resolves this run to R11/loop12. The accessible representative trigger artifact was empty in the fetched state; therefore this MD treats the four selected C32 symbols as new independent cases and does not reuse any prior case row.

Duplicate gate:

| Check | Result |
|---|---|
| Same symbol + trigger_date + entry_date repeated | no |
| Same canonical allowed? | yes |
| New symbol count | 4 |
| New trigger family count | 4 |
| New independent case ratio | 1.00 |
| Wrong round penalty | 0 |
| Schema rematerialization penalty | 0 |

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Manifest fields confirmed:

| Field | Value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 5. Historical Eligibility Gate

| Case | Entry row exists | Forward 180D available | 180D corporate action window | Calibration usable |
|---|---:|---:|---|---:|
| SM 2023 | yes | yes | clean | true |
| Korea Zinc 2024 | yes | yes | clean | true |
| HMM 2023 | yes | yes | clean for candidate-rule purposes; 2023-11-10 candidate before entry | true |
| Hanmi Science 2024 | yes | yes | clean | true |
| Osstem Implant 2023 | yes | no | blocked by delisting/tender profile end and 2023-08-03 candidate | false / narrative_only |

## 6. Canonical Archetype Compression Map

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  ├─ confirmed cash tender / counter-tender
  │    ├─ SM 2023: HYBE tender → Kakao higher tender → hard event cap
  │    └─ Korea Zinc 2024: hostile tender → counter-buyback/legal escalation
  ├─ preferred bidder / non-binding sale process
  │    └─ HMM 2023: preferred bidder pop → negotiation failure
  ├─ family/governance vote with uncertain control transfer
  │    └─ Hanmi Science 2024: integration announcement → governance contest reversal
  └─ tender/delisting cap, insufficient 180D
       └─ Osstem Implant 2023: narrative-only
```

The compression rule is simple: C32 is not “M&A theme.” It is a contract-like event ladder. A live tender price or legally cleared buyback is closer to a cash-flow boundary; a preferred bidder or family dispute is only a story with optionality.

## 7. Case Selection Summary

| case_id | symbol | company_name | role | trigger_family | new_independent_case | current_profile_verdict |
|---|---|---|---|---|---:|---|
| R11L12_C32_SM_2023_KAKAO_HYBE_TENDER_BATTLE | 041510 | 에스엠 | positive / 4B overlay | competing tender offers | true | current_profile_4B_too_late |
| R11L12_C32_KOREAZINC_2024_MBK_YOUNGPOONG_TENDER | 010130 | 고려아연 | positive / high-MFE control premium | hostile tender + counter-buyback | true | current_profile_missed_structural |
| R11L12_C32_HMM_2023_HARIM_PREFERRED_BIDDER | 011200 | HMM | counterexample | preferred bidder without closing path | true | current_profile_false_positive |
| R11L12_C32_HANMISCIENCE_2024_OCI_GOVERNANCE_BATTLE | 008930 | 한미사이언스 | counterexample | family governance / shareholder vote | true | current_profile_false_positive |
| R11L12_C32_OSSTEM_2023_PRIVATE_EQUITY_TENDER_NARRATIVE | 048260 | 오스템임플란트 | narrative_only | tender/delisting cap | false | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

| Type | Count | Cases |
|---|---:|---|
| Positive structural/event success | 2 | SM, Korea Zinc |
| Counterexample or failed rerating | 2 | HMM, Hanmi Science |
| Narrative-only blocked | 1 | Osstem Implant |
| 4B or 4C cases | 4 usable + 1 narrative |
| Calibration usable cases | 4 |

This satisfies the minimum: positive_case_count >= 1, counterexample_count >= 1, calibration_usable_case_count >= 3, new_independent_case_ratio >= 0.60.

## 9. Evidence Source Map

| Case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| SM | HYBE tender / Kakao counter tender | multi-source public control premium | explicit tender cap and overheat | watch only after tender battle ends |
| Korea Zinc | hostile tender at 660k | competing buyback/court/legal escalation | event cap + legal/regulatory overhang | watch only |
| HMM | preferred bidder selected | insufficient; financing/creditor approval unresolved | contract delay + event cap | sale negotiation failure |
| Hanmi Science | integration/governance announcement | insufficient; vote and family dispute unresolved | legal/governance cap | thesis evidence broken |
| Osstem | tender offer | insufficient forward window | delisting cap | blocked |

## 10. Price Data Source Map

| Symbol | Company | Price shard | Profile |
|---|---|---|---|
| 041510 | 에스엠 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json |
| 010130 | 고려아연 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv / 2025.csv | atlas/symbol_profiles/010/010130.json |
| 011200 | HMM | atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv / 2024.csv | atlas/symbol_profiles/011/011200.json |
| 008930 | 한미사이언스 | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | atlas/symbol_profiles/008/008930.json |
| 048260 | 오스템임플란트 | atlas/ohlcv_tradable_by_symbol_year/048/048260/2023.csv | atlas/symbol_profiles/048/048260.json |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | trigger_date | entry_date | entry_price | polarity | current_profile_verdict | outcome |
|---|---|---|---|---|---:|---|---|---|
| R11L12_C32_SM_2023_KAKAO_HYBE_TENDER_BATTLE | 041510 | 에스엠 | 2023-02-10 | 2023-02-10 | 114,700 | positive | current_profile_4B_too_late | control_premium_success_then_event_cap_drawdown |
| R11L12_C32_KOREAZINC_2024_MBK_YOUNGPOONG_TENDER | 010130 | 고려아연 | 2024-09-13 | 2024-09-13 | 666,000 | positive | current_profile_missed_structural | control_premium_success_extreme_high_mae_after_peak |
| R11L12_C32_HMM_2023_HARIM_PREFERRED_BIDDER | 011200 | HMM | 2023-12-18 | 2023-12-18 | 17,540 | counterexample | current_profile_false_positive | preferred_bidder_pop_failed_rerating |
| R11L12_C32_HANMISCIENCE_2024_OCI_GOVERNANCE_BATTLE | 008930 | 한미사이언스 | 2024-01-12 | 2024-01-15 | 43,300 | counterexample | current_profile_false_positive | governance_premium_reversal |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R11L12_C32_SM_2023_T1 | 041510 | 2023-02-10 | 114,700 | 40.54 | -9.24 | 40.54 | -23.63 | 40.54 | -23.63 | 2023-03-08 | 161,200 | -45.66 |
| R11L12_C32_KZINC_2024_T1 | 010130 | 2024-09-13 | 666,000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 | 2,407,000 | -73.29 |
| R11L12_C32_HMM_2023_T1 | 011200 | 2023-12-18 | 17,540 | 32.84 | -9.92 | 32.84 | -18.76 | 32.84 | -18.76 | 2023-12-20 | 23,300 | -38.84 |
| R11L12_C32_HANMI_2024_T1 | 008930 | 2024-01-15 | 43,300 | 29.79 | -10.62 | 29.79 | -28.41 | 29.79 | -29.79 | 2024-01-16 | 56,200 | -45.91 |

Notes:
- Metrics are computed from stock-web tradable raw OHLC rows.
- 180D is the primary quantitative calibration horizon.
- 1Y/2Y values are intentionally not used for new weight proposal in this MD because C32 event caps are short-to-mid horizon structures.

## 13. Current Calibrated Profile Stress Test

| Case | P0 likely decision | Actual OHLC verdict | Residual |
|---|---|---|---|
| SM | Stage2/Yellow allowed, 4B late unless event-cap recognized | +40.54% MFE but -45.66% drawdown after peak | 4B too late |
| Korea Zinc | Price-only blowoff guard may under-recognize non-price tender evidence | +261.41% 90/180D MFE with later -73.29% drawdown | missed structural event premium + 4B escalation |
| HMM | Preferred bidder may be over-promoted as control premium | +32.84% spike, then -38.84% post-peak drawdown | false positive |
| Hanmi Science | Governance event may be over-promoted | +29.79% one-day high, then -45.91% post-peak drawdown | false positive |

Answers to required stress questions:

1. **How would current calibrated profile judge the case?** It would generally allow Stage2-Actionable for public non-price events, but lacks a C32 polarity rule to separate confirmed cash tender from unresolved preferred bidder/governance fight.
2. **Did that match MFE/MAE?** Partially. SM and Korea Zinc needed a positive event-premium route; HMM and Hanmi needed a guard.
3. **Was Stage2 bonus excessive or insufficient?** Excessive for HMM/Hanmi unless paired with transaction-close confidence; insufficient for Korea Zinc because non-price tender evidence was not just price action.
4. **Was Yellow 75 excessive or insufficient?** Reasonable globally, but C32 needs event-cap overlay before Yellow becomes Green.
5. **Was Green 87 / revision 55 excessive or insufficient?** Green should require confirmed tender/counterbid or executed control transfer, not just event momentum.
6. **Was price-only blowoff guard appropriate?** Kept, but not enough; control-premium evidence can be non-price and still blow off.
7. **Was full 4B non-price requirement appropriate?** Strengthened. C32 event-cap evidence is a valid non-price 4B route.
8. **Was hard 4C routing too late or too harsh?** Kept; HMM/Hanmi show 4C should route when the transaction thesis breaks.

## 14. Stage2 / Yellow / Green Comparison

C32 is different from an EPS revision archetype. The price often jumps before operating evidence exists because the market is discounting a cash bid or control transfer. Therefore:

```text
Stage2-Actionable:
  public event + credible party + disclosed price/offer/ownership path

Stage3-Yellow:
  event premium confirmed, but closing/legal/shareholder route still unresolved

Stage3-Green:
  requires one of:
    - successful tender/counter tender,
    - court-cleared buyback with actual financing,
    - binding sale agreement / regulatory clearance,
    - executed control transfer.
```

Green lateness ratio is marked `not_applicable` because the audited rows are event-premium cases rather than EPS-revision Green triggers. Applying Green only after full close would be too late for positive capture but correct for production-risk control. This is why C32 should use a separate event-premium Stage2/4B structure rather than pretend it is normal Stage3-Green.

## 15. 4B Local vs Full-window Timing Audit

| Case | 4B evidence type | local_peak_proximity | full_window_peak_proximity | timing verdict |
|---|---|---:|---:|---|
| SM | tender cap / overheat | 0.99 | 0.99 | good_full_window_4B_timing |
| Korea Zinc | tender escalation / legal risk | 0.61 | 0.61 | partial_4B_before_full_blowoff; escalation continued |
| HMM | preferred-bidder contract risk | 1.00 | 1.00 | good_full_window_4B_timing if contract risk used |
| Hanmi Science | governance/family vote risk | 1.00 | 1.00 | good_full_window_4B_timing if governance risk used |

C32 4B is not “주가가 많이 올랐다.” It is the point where the offer price, legal path, shareholder vote, financing package, or counter-bid ceiling becomes more important than ordinary valuation.

## 16. 4C Protection Audit

| Case | 4C label | Protection interpretation |
|---|---|---|
| SM | thesis_break_watch_only | tender battle ended; watch for post-event normalization rather than hard 4C |
| Korea Zinc | thesis_break_watch_only | control fight persisted; no hard thesis break inside entry window |
| HMM | hard_4c_success | sale negotiation failure should protect from preferred-bidder false rerating |
| Hanmi Science | hard_4c_success | control-transfer thesis failed/reversed into governance contest |

## 17. Sector-Specific Rule Candidate

### L10_EVENT_CAP_4B_ROUTER

```text
if large_sector_id == L10_POLICY_EVENT_CROSS_REDTEAM_MISC
and event premium is driven by tender offer / control premium / privatization / preferred bidder / court decision:
    require explicit event-cap evidence for full 4B
    do not allow price-only local peak to become full 4B
    if closing route is unresolved:
        cap Stage label at Stage2-Actionable or Stage3-Yellow
        add governance_execution_risk_score
        add legal_or_contract_risk_score
```

## 18. Canonical-Archetype Rule Candidate

### C32_CONFIRMED_TENDER_POLARITY_GATE

```text
positive polarity:
  confirmed cash tender price,
  competing counterbid,
  court-cleared buyback/tender,
  disclosed ownership route,
  successful tender result.

negative / guard polarity:
  preferred bidder only,
  non-binding MOU,
  unresolved financing,
  shareholder vote/family dispute,
  regulatory or legal challenge,
  tender price below market or capped upside,
  transaction failure.

rule:
  C32 Stage3-Green requires positive polarity AND absence of unresolved-closing guard.
  If positive polarity exists but event cap is near, route 4B overlay rather than ordinary Green.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 91.15 | -18.11 | 91.15 | -18.91 | 0.5 | 1 | mixed; strong MFE but insufficient distinction between real tender premium and unresolved sale/family contest |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 91.15 | -18.11 | 91.15 | -18.91 | 0.75 | 0 | poor for HMM/Hanmi; event cap not separated |
| P1_sector_specific_candidate_profile | sector_specific | 4 | 150.98 | -12.64 | 150.98 | -13.54 | 0.0 | 0 | best alignment; positives kept as event premium, unresolved sale/governance battles routed to cap/risk |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 4 | 91.15 | -18.11 | 91.15 | -18.91 | 0.0 | 0 | good; C32-specific compression explains both positive and counterexample paths |
| P3_counterexample_guard_profile | counterexample_guard | 2 | 31.32 | -23.59 | 31.32 | -24.27 | 0.0 | 0 | prevents event-driven false Green |

## 20. Score-Return Alignment Matrix

| case_id | symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | current_profile_verdict | score_return_alignment |
|---|---|---:|---|---:|---|---|---|
| R11L12_C32_SM_2023_KAKAO_HYBE_TENDER_BATTLE | 041510 | 91.5 | Stage3-Green | 92.6 | Stage3-Green | current_profile_4B_too_late | control_premium_success_then_event_cap_drawdown |
| R11L12_C32_KOREAZINC_2024_MBK_YOUNGPOONG_TENDER | 010130 | 87.7 | Stage3-Green | 88.8 | Stage3-Green | current_profile_missed_structural | control_premium_success_extreme_high_mae_after_peak |
| R11L12_C32_HMM_2023_HARIM_PREFERRED_BIDDER | 011200 | 62.5 | Stage2-Actionable | 56.9 | 4B/4C-watch | current_profile_false_positive | preferred_bidder_pop_failed_rerating |
| R11L12_C32_HANMISCIENCE_2024_OCI_GOVERNANCE_BATTLE | 008930 | 62.5 | Stage2-Actionable | 56.9 | 4B/4C-watch | current_profile_false_positive | governance_premium_reversal |

## 20.1 Raw Component Score Breakdown

### R11L12_C32_SM_2023_KAKAO_HYBE_TENDER_BATTLE / R11L12_C32_SM_2023_T1

Before raw components:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 0,
  "revision_score": 0,
  "relative_strength_score": 70,
  "customer_quality_score": 0,
  "policy_or_regulatory_score": 65,
  "valuation_repricing_score": 78,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 35,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "control_premium_event_score": 85,
  "event_cap_score": 65,
  "governance_execution_risk_score": 35,
  "thesis_break_score": 0
}
```

After raw components:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 0,
  "revision_score": 0,
  "relative_strength_score": 70,
  "customer_quality_score": 0,
  "policy_or_regulatory_score": 65,
  "valuation_repricing_score": 78,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 40,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "control_premium_event_score": 91,
  "event_cap_score": 73,
  "governance_execution_risk_score": 35,
  "thesis_break_score": 0
}
```

Explanation: Shadow-only C32 profile lifts confirmed tender/control-premium evidence but routes unresolved financing, legal contest, or failed transaction into 4B/4C overlay instead of Stage3 promotion.

### R11L12_C32_KOREAZINC_2024_MBK_YOUNGPOONG_TENDER / R11L12_C32_KZINC_2024_T1

Before raw components:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 0,
  "revision_score": 0,
  "relative_strength_score": 70,
  "customer_quality_score": 0,
  "policy_or_regulatory_score": 65,
  "valuation_repricing_score": 78,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 45,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "control_premium_event_score": 85,
  "event_cap_score": 65,
  "governance_execution_risk_score": 55,
  "thesis_break_score": 0
}
```

After raw components:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 0,
  "revision_score": 0,
  "relative_strength_score": 70,
  "customer_quality_score": 0,
  "policy_or_regulatory_score": 65,
  "valuation_repricing_score": 78,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 50,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "control_premium_event_score": 91,
  "event_cap_score": 73,
  "governance_execution_risk_score": 55,
  "thesis_break_score": 0
}
```

Explanation: Shadow-only C32 profile lifts confirmed tender/control-premium evidence but routes unresolved financing, legal contest, or failed transaction into 4B/4C overlay instead of Stage3 promotion.

### R11L12_C32_HMM_2023_HARIM_PREFERRED_BIDDER / R11L12_C32_HMM_2023_T1

Before raw components:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 0,
  "revision_score": 0,
  "relative_strength_score": 68,
  "customer_quality_score": 0,
  "policy_or_regulatory_score": 55,
  "valuation_repricing_score": 60,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 75,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "control_premium_event_score": 65,
  "event_cap_score": 80,
  "governance_execution_risk_score": 78,
  "thesis_break_score": 72
}
```

After raw components:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 0,
  "revision_score": 0,
  "relative_strength_score": 68,
  "customer_quality_score": 0,
  "policy_or_regulatory_score": 55,
  "valuation_repricing_score": 60,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 75,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "control_premium_event_score": 53,
  "event_cap_score": 92,
  "governance_execution_risk_score": 88,
  "thesis_break_score": 80
}
```

Explanation: Shadow-only C32 profile lifts confirmed tender/control-premium evidence but routes unresolved financing, legal contest, or failed transaction into 4B/4C overlay instead of Stage3 promotion.

### R11L12_C32_HANMISCIENCE_2024_OCI_GOVERNANCE_BATTLE / R11L12_C32_HANMI_2024_T1

Before raw components:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 0,
  "revision_score": 0,
  "relative_strength_score": 68,
  "customer_quality_score": 0,
  "policy_or_regulatory_score": 55,
  "valuation_repricing_score": 60,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 75,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "control_premium_event_score": 65,
  "event_cap_score": 80,
  "governance_execution_risk_score": 78,
  "thesis_break_score": 72
}
```

After raw components:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 0,
  "revision_score": 0,
  "relative_strength_score": 68,
  "customer_quality_score": 0,
  "policy_or_regulatory_score": 55,
  "valuation_repricing_score": 60,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 75,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "control_premium_event_score": 53,
  "event_cap_score": 92,
  "governance_execution_risk_score": 88,
  "thesis_break_score": 80
}
```

Explanation: Shadow-only C32 profile lifts confirmed tender/control-premium evidence but routes unresolved financing, legal contest, or failed transaction into 4B/4C overlay instead of Stage3 promotion.


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP | 2 | 2 | 4 | 2 | 4 | 0 | 4 | 4 | 3 | true | true | reduced: C32 now has positive/counterexample/event-cap coverage |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_missed_structural
  - current_profile_4B_too_late
new_axis_proposed:
  - C32_CONFIRMED_TENDER_POLARITY_GATE
  - L10_EVENT_CAP_4B_ROUTER
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- R11/loop12 schedule consistency.
- L10/C32 sector/archetype consistency.
- Stock-web manifest and schema fields.
- Per-symbol profile fields.
- Actual tradable OHLC entry rows.
- 30D/90D/180D MFE and MAE for four usable triggers.
- Positive/counterexample balance.
- Event-cap 4B vs thesis-break 4C distinction.
```

Not validated:

```text
- No live/current candidate scan.
- No auto-trading or brokerage API.
- No stock_agent source code.
- No production scoring patch.
- No price route discovery.
- No investment recommendation.
- 1Y/2Y calibration is intentionally not used for this C32 shadow proposal.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_CONFIRMED_TENDER_POLARITY_GATE,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Cash tender/counterbid or court-cleared buyback can create real control-premium repricing; preferred bidder without closing path should not be scored the same.","keeps SM/Korea Zinc positive while downgrading HMM/Hanmi to event-cap/4B watch","R11L12_C32_SM_2023_T1|R11L12_C32_KZINC_2024_T1|R11L12_C32_HMM_2023_T1|R11L12_C32_HANMI_2024_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L10_EVENT_CAP_4B_ROUTER,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Event premium peaks near explicit tender/offer/court thresholds; non-price event-cap evidence is needed before full 4B.","improves 4B timing for SM, HMM, Hanmi; flags Korea Zinc as escalation risk before full-window peak","R11L12_C32_SM_2023_T1|R11L12_C32_KZINC_2024_T1|R11L12_C32_HMM_2023_T1|R11L12_C32_HANMI_2024_T1",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L12_C32_SM_2023_KAKAO_HYBE_TENDER_BATTLE","symbol":"041510","company_name":"에스엠","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R11L12_C32_SM_2023_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"control_premium_success_then_event_cap_drawdown","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"clean_180D_window; no 2023 corporate-action candidate in profile."}
{"row_type":"case","case_id":"R11L12_C32_KOREAZINC_2024_MBK_YOUNGPOONG_TENDER","symbol":"010130","company_name":"고려아연","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R11L12_C32_KZINC_2024_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"control_premium_success_extreme_high_mae_after_peak","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"profile corporate_action_candidate_dates empty; clean_180D_window."}
{"row_type":"case","case_id":"R11L12_C32_HMM_2023_HARIM_PREFERRED_BIDDER","symbol":"011200","company_name":"HMM","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R11L12_C32_HMM_2023_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"preferred_bidder_pop_failed_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2023-11-10 corporate action candidate is before entry; no profile candidate in entry~180D."}
{"row_type":"case","case_id":"R11L12_C32_HANMISCIENCE_2024_OCI_GOVERNANCE_BATTLE","symbol":"008930","company_name":"한미사이언스","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R11L12_C32_HANMI_2024_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"governance_premium_reversal","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"profile corporate-action candidates are historical and not in 2024 window."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R11L12_C32_SM_2023_T1","case_id":"R11L12_C32_SM_2023_KAKAO_HYBE_TENDER_BATTLE","symbol":"041510","company_name":"에스엠","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","evidence_available_at_that_date":"HYBE tender/control-premium bid at 120,000 KRW followed by Kakao counter-bid at 150,000 KRW; event evidence existed before outcome.","evidence_source":"AP / Reuters-derived public report set: Hybe stake purchase, Kakao tender offer; stock-web OHLC rows 2023-02-10~2023-10-27.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["explicit_event_cap","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-10","entry_price":114700,"MFE_30D_pct":40.54,"MFE_90D_pct":40.54,"MFE_180D_pct":40.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.24,"MAE_90D_pct":-23.63,"MAE_180D_pct":-23.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["control_premium_or_event_premium","valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"control_premium_success_then_event_cap_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L12_C32_SM_2023_KAKAO_HYBE_TENDER_BATTLE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L12_C32_KZINC_2024_T1","case_id":"R11L12_C32_KOREAZINC_2024_MBK_YOUNGPOONG_TENDER","symbol":"010130","company_name":"고려아연","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","evidence_available_at_that_date":"MBK/Young Poong hostile tender at 660,000 KRW, followed by Korea Zinc/Bain counter-buyback and legal event chain.","evidence_source":"Reuters Sep/Oct 2024 reports; stock-web OHLC rows 2024-09-13~2025-04-09.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["explicit_event_cap","legal_or_regulatory_block","positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-13","entry_price":666000,"MFE_30D_pct":131.68,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-3.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.61,"four_b_full_window_peak_proximity":0.61,"four_b_timing_verdict":"partial_4B_before_full_blowoff; event_cap_escalated_after_counterbid","four_b_evidence_type":["control_premium_or_event_premium","legal_or_regulatory_block","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"control_premium_success_extreme_high_mae_after_peak","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L12_C32_KOREAZINC_2024_MBK_YOUNGPOONG_TENDER_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L12_C32_HMM_2023_T1","case_id":"R11L12_C32_HMM_2023_HARIM_PREFERRED_BIDDER","symbol":"011200","company_name":"HMM","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-18","evidence_available_at_that_date":"Harim/JKL consortium selected as preferred bidder for HMM sale; deal dependency on financing, state creditor approval and negotiation terms remained unresolved.","evidence_source":"Public reports on HMM sale and failed negotiations; stock-web OHLC rows 2023-12-18~2024-07-12.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","legal_or_regulatory_block","contract_delay","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv","profile_path":"atlas/symbol_profiles/011/011200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-18","entry_price":17540,"MFE_30D_pct":32.84,"MFE_90D_pct":32.84,"MFE_180D_pct":32.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.92,"MAE_90D_pct":-18.76,"MAE_180D_pct":-18.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-20","peak_price":23300,"drawdown_after_peak_pct":-38.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_contract_risk_used","four_b_evidence_type":["control_premium_or_event_premium","contract_delay","legal_or_regulatory_block","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"preferred_bidder_pop_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L12_C32_HMM_2023_HARIM_PREFERRED_BIDDER_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L12_C32_HANMI_2024_T1","case_id":"R11L12_C32_HANMISCIENCE_2024_OCI_GOVERNANCE_BATTLE","symbol":"008930","company_name":"한미사이언스","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_TENDER_BATTLE_EVENT_CAP","sector":"policy_event_cross_redteam_misc","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-12","evidence_available_at_that_date":"OCI/Hanmi integration and subsequent family governance contest created event premium, but durable control transfer and operating rerating were not confirmed at entry.","evidence_source":"Public reports on Hanmi/OCI integration and shareholder contest; stock-web OHLC rows 2024-01-15~2024-07-22.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","legal_or_regulatory_block","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv","profile_path":"atlas/symbol_profiles/008/008930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-15","entry_price":43300,"MFE_30D_pct":29.79,"MFE_90D_pct":29.79,"MFE_180D_pct":29.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.62,"MAE_90D_pct":-28.41,"MAE_180D_pct":-29.79,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":56200,"drawdown_after_peak_pct":-45.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_governance_risk_used","four_b_evidence_type":["control_premium_or_event_premium","legal_or_regulatory_block","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"governance_premium_reversal","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L12_C32_HANMISCIENCE_2024_OCI_GOVERNANCE_BATTLE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L12_C32_SM_2023_KAKAO_HYBE_TENDER_BATTLE","trigger_id":"R11L12_C32_SM_2023_T1","symbol":"041510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":78,"execution_risk_score":0,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_event_score":85,"event_cap_score":65,"governance_execution_risk_score":35,"thesis_break_score":0},"weighted_score_before":91.5,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":78,"execution_risk_score":0,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_event_score":91,"event_cap_score":73,"governance_execution_risk_score":35,"thesis_break_score":0},"weighted_score_after":92.6,"stage_label_after":"Stage3-Green","changed_components":["control_premium_event_score","event_cap_score","governance_execution_risk_score","thesis_break_score"],"component_delta_explanation":"Shadow-only C32 profile lifts confirmed tender/control-premium evidence but routes unresolved financing, legal contest, or failed transaction into 4B/4C overlay instead of Stage3 promotion.","MFE_90D_pct":40.54,"MAE_90D_pct":-23.63,"score_return_alignment_label":"control_premium_success_then_event_cap_drawdown","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L12_C32_KOREAZINC_2024_MBK_YOUNGPOONG_TENDER","trigger_id":"R11L12_C32_KZINC_2024_T1","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":78,"execution_risk_score":0,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_event_score":85,"event_cap_score":65,"governance_execution_risk_score":55,"thesis_break_score":0},"weighted_score_before":87.7,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":78,"execution_risk_score":0,"legal_or_contract_risk_score":50,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_event_score":91,"event_cap_score":73,"governance_execution_risk_score":55,"thesis_break_score":0},"weighted_score_after":88.8,"stage_label_after":"Stage3-Green","changed_components":["control_premium_event_score","event_cap_score","governance_execution_risk_score","thesis_break_score"],"component_delta_explanation":"Shadow-only C32 profile lifts confirmed tender/control-premium evidence but routes unresolved financing, legal contest, or failed transaction into 4B/4C overlay instead of Stage3 promotion.","MFE_90D_pct":261.41,"MAE_90D_pct":-1.65,"score_return_alignment_label":"control_premium_success_extreme_high_mae_after_peak","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L12_C32_HMM_2023_HARIM_PREFERRED_BIDDER","trigger_id":"R11L12_C32_HMM_2023_T1","symbol":"011200","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":60,"execution_risk_score":0,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_event_score":65,"event_cap_score":80,"governance_execution_risk_score":78,"thesis_break_score":72},"weighted_score_before":62.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":60,"execution_risk_score":0,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_event_score":53,"event_cap_score":92,"governance_execution_risk_score":88,"thesis_break_score":80},"weighted_score_after":56.9,"stage_label_after":"4B/4C-watch","changed_components":["control_premium_event_score","event_cap_score","governance_execution_risk_score","thesis_break_score"],"component_delta_explanation":"Shadow-only C32 profile lifts confirmed tender/control-premium evidence but routes unresolved financing, legal contest, or failed transaction into 4B/4C overlay instead of Stage3 promotion.","MFE_90D_pct":32.84,"MAE_90D_pct":-18.76,"score_return_alignment_label":"preferred_bidder_pop_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L12_C32_HANMISCIENCE_2024_OCI_GOVERNANCE_BATTLE","trigger_id":"R11L12_C32_HANMI_2024_T1","symbol":"008930","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":60,"execution_risk_score":0,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_event_score":65,"event_cap_score":80,"governance_execution_risk_score":78,"thesis_break_score":72},"weighted_score_before":62.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":60,"execution_risk_score":0,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_event_score":53,"event_cap_score":92,"governance_execution_risk_score":88,"thesis_break_score":80},"weighted_score_after":56.9,"stage_label_after":"4B/4C-watch","changed_components":["control_premium_event_score","event_cap_score","governance_execution_risk_score","thesis_break_score"],"component_delta_explanation":"Shadow-only C32 profile lifts confirmed tender/control-premium evidence but routes unresolved financing, legal contest, or failed transaction into 4B/4C overlay instead of Stage3 promotion.","MFE_90D_pct":29.79,"MAE_90D_pct":-28.41,"score_return_alignment_label":"governance_premium_reversal","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```jsonl
{"row_type":"shadow_weight","axis":"C32_CONFIRMED_TENDER_POLARITY_GATE","scope":"canonical_archetype_specific","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Cash tender/counterbid or court-cleared buyback can create real control-premium repricing; preferred bidder without closing path should not be scored the same.","backtest_effect":"keeps SM/Korea Zinc positive while downgrading HMM/Hanmi to event-cap/4B watch","trigger_ids":"R11L12_C32_SM_2023_T1|R11L12_C32_KZINC_2024_T1|R11L12_C32_HMM_2023_T1|R11L12_C32_HANMI_2024_T1","calibration_usable_count":4,"new_independent_case_count":4,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"L10_EVENT_CAP_4B_ROUTER","scope":"sector_specific","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Event premium peaks near explicit tender/offer/court thresholds; non-price event-cap evidence is needed before full 4B.","backtest_effect":"improves 4B timing for SM, HMM, Hanmi; flags Korea Zinc as escalation risk before full-window peak","trigger_ids":"R11L12_C32_SM_2023_T1|R11L12_C32_KZINC_2024_T1|R11L12_C32_HMM_2023_T1|R11L12_C32_HANMI_2024_T1","calibration_usable_count":4,"new_independent_case_count":4,"counterexample_count":2,"confidence":"medium","proposal_type":"sector_shadow_only","notes":"not production; post-calibrated residual"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_false_positive","current_profile_missed_structural","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"R11L12_C32_OSSTEM_2023_PRIVATE_EQUITY_TENDER_NARRATIVE","symbol":"048260","company_name":"오스템임플란트","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"Tender-offer cap exists, but stock-web profile ends 2023-08-11 and corporate_action_candidate_date 2023-08-03 overlaps the event/tender-delisting window; forward 180D is unavailable/contaminated.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R11
completed_loop = 12
next_round = R12
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes


- Stock-Web manifest fetched from `atlas/manifest.json`: generated_at 2026-05-21, source `FinanceData/marcap`, max_date `2026-02-20`, tradable_row_count `14,354,401`, price_adjustment_status `raw_unadjusted_marcap`.
- Stock-Web schema fetched from `atlas/schema.json`: tradable columns are `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE are computed from high/low relative to entry close; calibration requires 180 forward tradable rows and a clean corporate-action window.
- SM event evidence uses public reports that HYBE acquired Lee Soo-man's stake and launched a tender, and that Kakao made a KRW 150,000 tender offer for 35% of SM.
- Korea Zinc event evidence uses Reuters reports on the MBK/Young Poong tender offer, the court-cleared Korea Zinc buyback, and the later market-watchdog review of the new share issuance plan.
- HMM event evidence uses public reports on Harim/JKL becoming preferred bidder and the sale negotiations later breaking down.
- Hanmi Science event evidence uses public reports on OCI/Hanmi integration and the family/shareholder governance contest.
- Osstem Implant was retained only as narrative coverage because stock-web profile stops at 2023-08-11 and has a 2023-08-03 corporate-action candidate overlapping the tender/delisting window.

