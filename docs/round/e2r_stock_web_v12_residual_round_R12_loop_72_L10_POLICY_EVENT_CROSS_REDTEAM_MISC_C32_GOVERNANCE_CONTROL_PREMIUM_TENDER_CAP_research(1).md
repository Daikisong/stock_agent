# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 72
completed_round = R12
completed_loop = 72
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP
output_file = e2r_stock_web_v12_residual_round_R12_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 3 counterexamples, and 4 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.
## 1. Current Calibrated Profile Assumption
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

The residual tested here is C32-specific. Governance and control-premium headlines can move price like a flare, but the flare is not the same thing as a new engine. The proxy profile must separate a signed/control-close bridge from a pure contest premium.
## 2. Round / Large Sector / Canonical Archetype Scope
```text
scheduled_round = R12
scheduled_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP
loop_objective = residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill
```

R12 allows L10 policy/event/cross-redteam/misc or under-covered service/agri. C32 is retained from prior C32 work but uses different symbols and trigger families: proxy fight, family/activist contest, activist stake, and signed control-sale legal 4C.
## 3. Previous Coverage / Duplicate Avoidance Check
No hard duplicate is intentionally reused. The local prior R12/L10/C32 coverage used SM, Korea Zinc, Hanmi Science, and YTN. This loop avoids those symbols and adds four new C32 symbols.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
```

Selected symbols:

```text
180640 한진칼       = proxy_fight_without_control_close
011780 금호석유화학 = proxy_fight_confounded_by_operating_cycle
000990 DB하이텍     = activist_stake_without_tender_floor
003920 남양유업     = signed_control_sale_agreement_then_legal_dispute
```
## 4. Stock-Web OHLC Input / Price Source Validation
```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The manifest and schema were checked before case work. All quantitative rows use `tradable_raw`; raw shards are not used for weight calibration.
## 5. Historical Eligibility Gate
| case_id | symbol | profile_path | corporate_action_window_status | forward_window_trading_days | calibration_usable | block_reasons |
|---|---:|---|---|---:|---|---|
| C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF | 180640 | atlas/symbol_profiles/180/180640.json | clean_180D_window | 180 | true | [] |
| C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE | 011780 | atlas/symbol_profiles/011/011780.json | clean_180D_window | 180 | true | [] |
| C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP | 000990 | atlas/symbol_profiles/000/000990.json | clean_180D_window | 180 | true | [] |
| C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C | 003920 | atlas/symbol_profiles/003/003920.json | clean_180D_window | 180 | true | [] |

## 6. Canonical Archetype Compression Map
```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP

fine_archetype:
- proxy_fight_without_control_close
- proxy_fight_confounded_by_operating_cycle
- activist_stake_without_tender_floor
- signed_control_sale_agreement_then_legal_dispute

compressed rule family:
- control premium can create explosive MFE
- without tender price, signed control sale, or closing bridge, governance-event premium is not Stage3 operating rerating
- if the price move is actually from another operating cycle, C32 must not claim the return
- signed sale can be a valid positive C32 Stage2, but legal/closing dispute should route to 4C-watch
```
## 7. Case Selection Summary
| case_id | symbol | trigger | entry | entry_price | MFE_30/90/180 | MAE_30/90/180 | peak | verdict |
|---|---:|---|---|---:|---:|---:|---|---|
| C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF | 180640 | 2020-02-26 Stage2-Actionable | 2020-02-26 | 60,000 | 60.0/85.0/85.0 | -35.17/-35.17/-35.17 | 2020-04-20 111,000 | current_profile_false_positive |
| C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE | 011780 | 2021-01-27 Stage2-Actionable | 2021-01-27 | 225,000 | 30.44/32.67/32.67 | -11.11/-11.11/-21.33 | 2021-05-06 298,500 | current_profile_false_positive |
| C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP | 000990 | 2023-03-30 Stage2-Actionable | 2023-03-31 | 72,300 | 15.63/15.63/15.63 | -24.48/-25.73/-34.3 | 2023-04-04 83,600 | current_profile_false_positive |
| C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C | 003920 | 2021-05-27 Stage2-Actionable | 2021-05-28 | 570,000 | 42.63/42.63/42.63 | -5.26/-29.82/-34.91 | 2021-07-01 813,000 | current_profile_4C_too_late |

## 8. Positive vs Counterexample Balance
```text
positive_case_count = 1
counterexample_count = 3
4B_case_count = 4
4C_case_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
```

This loop is deliberately counterexample-heavy. The positive row is the signed control-sale case where C32 can recognize event premium. The other three rows are the guardrail: proxy fight, activist stake, or governance contest can flash like lightning, but without a closing/tender bridge it should not be scored like a durable sunrise.
## 9. Evidence Source Map
| case_id | evidence_available_at_that_date | stage2_evidence | stage3_evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|
| C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF | Public proxy fight / control-premium contest became the dominant driver, but no clean tender-price floor or durable operating bridge was available at entry. | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | multiple_public_sources | valuation_blowoff, positioning_overheat, explicit_event_cap | thesis_evidence_broken |
| C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE | Public proxy/shareholder-return contest overlapped a powerful chemical spread margin cycle; C32 should not claim the whole rerating without an independent control-close bridge. | public_event_or_disclosure, relative_strength | multiple_public_sources, financial_visibility | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | thesis_evidence_broken |
| C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP | Activist-stake/governance pressure generated a short event premium, but no tender price, control close, or earnings revision bridge supported Stage3 promotion. | public_event_or_disclosure, relative_strength | multiple_public_sources | valuation_blowoff, positioning_overheat, explicit_event_cap | thesis_evidence_broken |
| C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C | Signed control-sale agreement created a valid C32 Stage2 event premium, but later legal dispute/closing uncertainty should route to 4C-watch rather than keep a stale positive label. | public_event_or_disclosure, customer_or_order_quality, relative_strength | multiple_public_sources, durable_customer_confirmation | valuation_blowoff, legal_or_regulatory_block, explicit_event_cap | legal_or_regulatory_block, thesis_evidence_broken |

## 10. Price Data Source Map
| symbol | company | price_shard_path | profile_path |
|---:|---|---|---|
| 180640 | 한진칼 | atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv | atlas/symbol_profiles/180/180640.json |
| 011780 | 금호석유화학 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv | atlas/symbol_profiles/011/011780.json |
| 000990 | DB하이텍 | atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv | atlas/symbol_profiles/000/000990.json |
| 003920 | 남양유업 | atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv; atlas/ohlcv_tradable_by_symbol_year/003/003920/2022.csv | atlas/symbol_profiles/003/003920.json |

## 11. Case-by-Case Trigger Grid
Representative triggers are the first dates when the governance/control event became public enough to affect entry. When event timing was unclear or post-close, the next tradable close is used.

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | outcome | dedupe_for_aggregate |
|---|---:|---|---|---|---:|---|---|
| C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF | 180640 | Stage2-Actionable | 2020-02-26 | 2020-02-26 | 60,000 | high_mae_event_premium_counterexample | true |
| C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE | 011780 | Stage2-Actionable | 2021-01-27 | 2021-01-27 | 225,000 | confounded_governance_false_attribution | true |
| C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP | 000990 | Stage2-Actionable | 2023-03-30 | 2023-03-31 | 72,300 | activist_stake_event_cap_failed_rerating | true |
| C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C | 003920 | Stage2-Actionable | 2021-05-27 | 2021-05-28 | 570,000 | control_sale_positive_but_legal_4C_needed | true |

## 12. Trigger-Level OHLC Backtest Tables
| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 180640 | 2020-02-26 | 60,000 | 60.0 | -35.17 | 85.0 | -35.17 | 85.0 | -35.17 | 2020-04-20 | 111,000 | -39.46 |
| 011780 | 2021-01-27 | 225,000 | 30.44 | -11.11 | 32.67 | -11.11 | 32.67 | -21.33 | 2021-05-06 | 298,500 | -40.7 |
| 000990 | 2023-03-31 | 72,300 | 15.63 | -24.48 | 15.63 | -25.73 | 15.63 | -34.3 | 2023-04-04 | 83,600 | -43.18 |
| 003920 | 2021-05-28 | 570,000 | 42.63 | -5.26 | 42.63 | -29.82 | 42.63 | -34.91 | 2021-07-01 | 813,000 | -54.37 |

## 13. Current Calibrated Profile Stress Test
| case_id | current_profile_verdict | interpretation |
|---|---|---|
| C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF | current_profile_false_positive | Proxy fight plus RS looks like Yellow, but the high MAE and absent tender floor mean it should be 4B event-cap watch. |
| C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE | current_profile_false_positive | Governance proxy signal is confounded by a separate margin-spread cycle; C32 should not claim the operating rerating. |
| C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP | current_profile_false_positive | Activist-stake headline produced a short local peak and then large MAE; Stage3 promotion would be a false positive. |
| C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C | current_profile_4C_too_late | Current profile can accept the signed control-sale event, but hard 4C routing is too late once legal/closing dispute becomes the thesis break. |

The already-applied `price_only_blowoff_blocks_positive_stage` remains correct, but C32 needs a more specific reason code. Price-only blowoff is the smoke; the missing control-close/tender-price bridge is the fire alarm.

## 14. Stage2 / Yellow / Green Comparison
Stage2 is allowed for C32 when public event + relative strength appear. Yellow/Green is not allowed unless the event has a structural bridge. For this loop:

```text
Stage2 allowed: public control/proxy/activist/sale event + tradable row
Stage3-Yellow allowed: event bridge plus execution visibility
Stage3-Green allowed: signed/tender/control-close bridge plus legal/closing risk contained
4B overlay allowed: event cap / valuation blowoff / positioning overheat / missing tender floor
4C route allowed: legal or contract dispute breaks the control-sale thesis
```

No Stage3-Green trigger is assigned to the representative rows, so `green_lateness_ratio = not_applicable`.
## 15. 4B Local vs Full-window Timing Audit
| case_id | local_peak_proximity | full_window_peak_proximity | 4B verdict |
|---|---:|---:|---|
| C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF | 0.78 | 0.7 | event_cap_watch_required_but_not_positive_stage3 |
| C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE | 0.88 | 0.88 | confounded_operating_cycle_requires_non_c32_bridge |
| C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP | 0.96 | 0.96 | activist_headline_local_peak_too_early_for_stage3 |
| C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C | 0.72 | 0.72 | positive_control_sale_requires_legal_4C_watch |

## 16. 4C Protection Audit
| case_id | four_c_protection_label | reason |
|---|---|---|
| C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF | thesis_break_watch_only | event premium failed to convert into durable bridge; watch-only 4C protects against stale positive labels |
| C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE | false_break_or_wrong_axis_if_governance_only | event premium failed to convert into durable bridge; watch-only 4C protects against stale positive labels |
| C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP | hard_4c_late_if_waiting_for_price_break_only | event premium failed to convert into durable bridge; watch-only 4C protects against stale positive labels |
| C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C | hard_4c_late | legal/closing dispute breaks signed-control-sale thesis |

## 17. Sector-Specific Rule Candidate
```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
axis = L10_event_premium_requires_event_close_bridge
candidate_delta = +1 guard
```

Within L10, event premium should be treated like a bridge with missing planks. A trader can step onto Stage2 when the event is public, but Stage3 requires proof that the bridge reaches the other side: tender price, signed sale, approval/closing visibility, or cashflow/shareholder-return bridge.

## 18. Canonical-Archetype Rule Candidate
```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
axis = C32_control_close_or_tender_price_bridge_required
axis = C32_proxy_fight_without_control_close_cap
axis = C32_legal_dispute_4C_watch_after_signed_control_sale
```

C32 should compress proxy fight, activist stake, tender, signed sale, and privatization into one canonical family, but the family needs an internal hinge: event premium without a legally executable bridge is not durable rerating.
## 19. Before / After Backtest Comparison
| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | all representative triggers | 43.98 | -25.46 | 43.98 | -31.43 | 0.75 | 0 | weak: high MFE coexists with high MAE and wrong attribution |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | all representative triggers | 43.98 | -25.46 | 43.98 | -31.43 | 1.0 | 0 | worse: governance event premiums look like durable rerating |
| P1_sector_specific_candidate_profile | sector_specific_L10 | 4 | Namyang positive; Hanjin/Kumho/DB as guard examples | 42.63 | -29.82 | 42.63 | -34.91 | 0.25 | 0 | better: admits signed sale but blocks proxy-only Stage3 |
| P2_canonical_archetype_candidate_profile | canonical_C32 | 4 | same as P1 | 42.63 | -29.82 | 42.63 | -34.91 | 0.25 | 0 | best canonical compression for this loop |
| P3_counterexample_guard_profile | counterexample_guard | 3 | Hanjin/Kumho/DB counterexamples | 44.43 | -24.0 | 44.43 | -30.27 | 0.0 | 0 | guard-only profile removes false promotion but is not a positive selector |

## 20. Score-Return Alignment Matrix
| case_id | weighted_before / label_before | weighted_after / label_after | MFE_90D | MAE_90D | alignment |
|---|---|---|---:|---:|---|
| C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF | 76 / Stage3-Yellow proxy-fight false promotion risk | 63 / Stage2-watch + C32 4B event-cap overlay | 85.0 | -35.17 | high_mae_event_premium_counterexample |
| C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE | 80 / Stage3-Yellow if governance and margin cycle are blended | 66 / C32 event-watch; positive attribution must move to C17 if margin bridge exists | 32.67 | -11.11 | confounded_governance_false_attribution |
| C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP | 75 / Stage3-Yellow false promotion risk | 58 / Stage2-watch / event-cap block | 15.63 | -25.73 | activist_stake_event_cap_failed_rerating |
| C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C | 83 / Stage3-Yellow control-sale success but legal-risk underweighted | 74 / Stage2-Actionable + C32 legal 4C watch | 42.63 | -29.82 | control_sale_positive_but_legal_4C_needed |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP | 1 | 3 | 4 | 4 | 4 | 0 | 4 | 4 | 4 | true | true | C32 now has proxy-fight, activist-stake, confounded-cycle, and legal-4C rows; more tender-offer holdouts remain useful. |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: proxy_fight_without_control_close_false_stage3, activist_stake_event_cap_failed_rerating, governance_event_confounded_by_operating_cycle, signed_control_sale_legal_4C_late
new_axis_proposed: C32_control_close_or_tender_price_bridge_required; C32_proxy_fight_without_control_close_cap; C32_legal_dispute_4C_watch_after_signed_control_sale
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
## 23. Validation Scope / Non-Validation Scope
Validation scope:

```text
- stock-web manifest/schema checked
- symbol profiles checked for 180640, 011780, 000990, 003920
- tradable_raw 1D OHLC rows used for representative trigger backtests
- 30D / 90D / 180D MFE and MAE computed from stock-web visible rows
- 4B local vs full-window proximity split included as research proxy
```

Non-validation scope:

```text
- no current/live candidate scan
- no investment recommendation
- no stock_agent code or production scoring patch
- no broker/API/autotrading work
- no claim that governance event alone explains all company fundamentals
```
## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_control_close_or_tender_price_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,absent,present,+1,Positive Stage3 promotion requires signed control sale, tender-price floor, closing visibility, or post-event cashflow bridge.,Keeps Namyang as event-positive but blocks Hanjin/Kumho/DB false Stage3 promotion,T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP,4,4,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C32_proxy_fight_without_control_close_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,absent,present,+1,Proxy fight or activist stake without tender/control close should be capped at Stage2-watch plus 4B overlay.,Reduces false positive rate from 0.75 to 0.25 in this loop,T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP,2,2,2,medium,guard_shadow_only,not production; post-calibrated residual
shadow_weight,C32_legal_dispute_4C_watch_after_signed_control_sale,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,weak,strong,+1,Once signed control-sale faces closing/legal dispute, route to 4C-watch before the full price unwind.,Improves Namyang 4C timing after event peak,T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C,1,1,0,medium_low,4C_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "symbol": "180640", "company_name": "한진칼", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mae_event_premium_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Public proxy fight / control-premium contest became the dominant driver, but no clean tender-price floor or durable operating bridge was available at entry."}
{"row_type": "case", "case_id": "C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "symbol": "011780", "company_name": "금호석유화학", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "confounded_governance_false_attribution", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Public proxy/shareholder-return contest overlapped a powerful chemical spread margin cycle; C32 should not claim the whole rerating without an independent control-close bridge."}
{"row_type": "case", "case_id": "C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "symbol": "000990", "company_name": "DB하이텍", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "activist_stake_event_cap_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Activist-stake/governance pressure generated a short event premium, but no tender price, control close, or earnings revision bridge supported Stage3 promotion."}
{"row_type": "case", "case_id": "C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "symbol": "003920", "company_name": "남양유업", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP", "case_type": "4C_late", "positive_or_counterexample": "positive", "best_trigger": "T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "control_sale_positive_but_legal_4C_needed", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Signed control-sale agreement created a valid C32 Stage2 event premium, but later legal dispute/closing uncertainty should route to 4C-watch rather than keep a stale positive label."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF", "case_id": "C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "symbol": "180640", "company_name": "한진칼", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP", "sector": "holding_company_airline_group", "primary_archetype": "proxy_fight_without_control_close", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-02-26", "evidence_available_at_that_date": "Public proxy fight / control-premium contest became the dominant driver, but no clean tender-price floor or durable operating bridge was available at entry.", "evidence_source": "Public historical disclosure/news narrative; stock-web 1D OHLC shards and symbol profile verified for the historical price path. This row is not a live recommendation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv", "profile_path": "atlas/symbol_profiles/180/180640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-02-26", "entry_price": 60000, "MFE_30D_pct": 60.0, "MFE_90D_pct": 85.0, "MFE_180D_pct": 85.0, "MFE_1Y_pct": 85.0, "MFE_2Y_pct": null, "MAE_30D_pct": -35.17, "MAE_90D_pct": -35.17, "MAE_180D_pct": -35.17, "MAE_1Y_pct": -35.17, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-04-20", "peak_price": 111000, "drawdown_after_peak_pct": -39.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "event_cap_watch_required_but_not_positive_stage3", "four_b_evidence_type": ["positioning_overheat", "valuation_blowoff", "control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_event_premium_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G180640_2020-02-26_60000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "case_id": "C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "symbol": "011780", "company_name": "금호석유화학", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP", "sector": "chemical_family_control_proxy_fight", "primary_archetype": "proxy_fight_confounded_by_operating_cycle", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-27", "evidence_available_at_that_date": "Public proxy/shareholder-return contest overlapped a powerful chemical spread margin cycle; C32 should not claim the whole rerating without an independent control-close bridge.", "evidence_source": "Public historical disclosure/news narrative; stock-web 1D OHLC shards and symbol profile verified for the historical price path. This row is not a live recommendation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-27", "entry_price": 225000, "MFE_30D_pct": 30.44, "MFE_90D_pct": 32.67, "MFE_180D_pct": 32.67, "MFE_1Y_pct": 32.67, "MFE_2Y_pct": null, "MAE_30D_pct": -11.11, "MAE_90D_pct": -11.11, "MAE_180D_pct": -21.33, "MAE_1Y_pct": -31.85, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -40.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "confounded_operating_cycle_requires_non_c32_bridge", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "false_break_or_wrong_axis_if_governance_only", "trigger_outcome_label": "confounded_governance_false_attribution", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G011780_2021-01-27_225000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP", "case_id": "C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "symbol": "000990", "company_name": "DB하이텍", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP", "sector": "semiconductor_foundry_governance", "primary_archetype": "activist_stake_without_tender_floor", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-30", "evidence_available_at_that_date": "Activist-stake/governance pressure generated a short event premium, but no tender price, control close, or earnings revision bridge supported Stage3 promotion.", "evidence_source": "Public historical disclosure/news narrative; stock-web 1D OHLC shards and symbol profile verified for the historical price path. This row is not a live recommendation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv", "profile_path": "atlas/symbol_profiles/000/000990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-31", "entry_price": 72300, "MFE_30D_pct": 15.63, "MFE_90D_pct": 15.63, "MFE_180D_pct": 15.63, "MFE_1Y_pct": 15.63, "MFE_2Y_pct": null, "MAE_30D_pct": -24.48, "MAE_90D_pct": -25.73, "MAE_180D_pct": -34.3, "MAE_1Y_pct": -34.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-04", "peak_price": 83600, "drawdown_after_peak_pct": -43.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "activist_headline_local_peak_too_early_for_stage3", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_late_if_waiting_for_price_break_only", "trigger_outcome_label": "activist_stake_event_cap_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G000990_2023-03-31_72300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "case_id": "C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "symbol": "003920", "company_name": "남양유업", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PROXY_FIGHT_CONTROL_SALE_ACTIVIST_EVENT_CAP", "sector": "consumer_control_sale", "primary_archetype": "signed_control_sale_agreement_then_legal_dispute", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-05-27", "evidence_available_at_that_date": "Signed control-sale agreement created a valid C32 Stage2 event premium, but later legal dispute/closing uncertainty should route to 4C-watch rather than keep a stale positive label.", "evidence_source": "Public historical disclosure/news narrative; stock-web 1D OHLC shards and symbol profile verified for the historical price path. This row is not a live recommendation.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv; atlas/ohlcv_tradable_by_symbol_year/003/003920/2022.csv", "profile_path": "atlas/symbol_profiles/003/003920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-28", "entry_price": 570000, "MFE_30D_pct": 42.63, "MFE_90D_pct": 42.63, "MFE_180D_pct": 42.63, "MFE_1Y_pct": 42.63, "MFE_2Y_pct": null, "MAE_30D_pct": -5.26, "MAE_90D_pct": -29.82, "MAE_180D_pct": -34.91, "MAE_1Y_pct": -34.91, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-01", "peak_price": 813000, "drawdown_after_peak_pct": -54.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.72, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "positive_control_sale_requires_legal_4C_watch", "four_b_evidence_type": ["control_premium_or_event_premium", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "control_sale_positive_but_legal_4C_needed", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G003920_2021-05-28_570000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_HANJINKAL_20200226_PROXY_FIGHT_BLOWOFF", "trigger_id": "T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF", "symbol": "180640", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 16, "execution_risk_score": 12, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow proxy-fight false promotion risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 10, "execution_risk_score": 18, "legal_or_contract_risk_score": 14, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-watch + C32 4B event-cap overlay", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "contract_score", "margin_bridge_score"], "component_delta_explanation": "C32 shadow profile rewards explicit signed control-sale/tender-price bridge, but caps proxy-only, activist-stake, and operating-cycle-confounded event premiums. Legal/closing dispute raises 4C-watch risk.", "MFE_90D_pct": 85.0, "MAE_90D_pct": -35.17, "score_return_alignment_label": "high_mae_event_premium_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_KUMHO_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "trigger_id": "T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE", "symbol": "011780", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 13, "execution_risk_score": 8, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow if governance and margin cycle are blended", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 11, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 9, "execution_risk_score": 13, "legal_or_contract_risk_score": 11, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "C32 event-watch; positive attribution must move to C17 if margin bridge exists", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "contract_score", "margin_bridge_score"], "component_delta_explanation": "C32 shadow profile rewards explicit signed control-sale/tender-price bridge, but caps proxy-only, activist-stake, and operating-cycle-confounded event premiums. Legal/closing dispute raises 4C-watch risk.", "MFE_90D_pct": 32.67, "MAE_90D_pct": -11.11, "score_return_alignment_label": "confounded_governance_false_attribution", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_DBHITEK_20230331_ACTIVIST_STAKE_EVENT_CAP", "trigger_id": "T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP", "symbol": "000990", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 14, "execution_risk_score": 10, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow false promotion risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 16, "legal_or_contract_risk_score": 11, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-watch / event-cap block", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "contract_score", "margin_bridge_score"], "component_delta_explanation": "C32 shadow profile rewards explicit signed control-sale/tender-price bridge, but caps proxy-only, activist-stake, and operating-cycle-confounded event premiums. Legal/closing dispute raises 4C-watch risk.", "MFE_90D_pct": 15.63, "MAE_90D_pct": -25.73, "score_return_alignment_label": "activist_stake_event_cap_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_NAMYANG_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "trigger_id": "T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C", "symbol": "003920", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 14, "execution_risk_score": 7, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83, "stage_label_before": "Stage3-Yellow control-sale success but legal-risk underweighted", "raw_component_scores_after": {"contract_score": 18, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 2, "policy_or_regulatory_score": 3, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + C32 legal 4C watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "contract_score", "margin_bridge_score"], "component_delta_explanation": "C32 shadow profile rewards explicit signed control-sale/tender-price bridge, but caps proxy-only, activist-stake, and operating-cycle-confounded event premiums. Legal/closing dispute raises 4C-watch risk.", "MFE_90D_pct": 42.63, "MAE_90D_pct": -29.82, "score_return_alignment_label": "control_sale_positive_but_legal_4C_needed", "current_profile_verdict": "current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_control_close_or_tender_price_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,absent,present,+1,Positive Stage3 promotion requires signed control sale, tender-price floor, closing visibility, or post-event cashflow bridge.,Keeps Namyang as event-positive but blocks Hanjin/Kumho/DB false Stage3 promotion,T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C|T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|T011780_STAGE2_20210127_PROXY_FIGHT_CONFOUNDED_MARGIN_CYCLE|T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP,4,4,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C32_proxy_fight_without_control_close_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,absent,present,+1,Proxy fight or activist stake without tender/control close should be capped at Stage2-watch plus 4B overlay.,Reduces false positive rate from 0.75 to 0.25 in this loop,T180640_STAGE2_20200226_PROXY_FIGHT_BLOWOFF|T000990_STAGE2_20230331_ACTIVIST_STAKE_EVENT_CAP,2,2,2,medium,guard_shadow_only,not production; post-calibrated residual
shadow_weight,C32_legal_dispute_4C_watch_after_signed_control_sale,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,weak,strong,+1,Once signed control-sale faces closing/legal dispute, route to 4C-watch before the full price unwind.,Improves Namyang 4C timing after event peak,T003920_STAGE2_20210528_CONTROL_SALE_AGREEMENT_LEGAL_4C,1,1,0,medium_low,4C_shadow_only,not production; post-calibrated residual
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 1, "counterexample_count": 3, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["proxy_fight_without_control_close_false_stage3", "activist_stake_event_cap_failed_rerating", "governance_event_confounded_by_operating_cycle", "signed_control_sale_legal_4C_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":"none","reason":"all selected representative rows are calibration_usable","usage":"not_applicable"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R12
completed_loop = 72
next_round = R13
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```
## 28. Source Notes
```text
stock_web_manifest_checked = atlas/manifest.json
stock_web_schema_checked = atlas/schema.json
symbol_profiles_checked = 180640, 011780, 000990, 003920
price_rows_checked = 180640/2020, 011780/2021, 000990/2023, 003920/2021 and 003920/2022
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
investment_recommendation_language = none
```

Historical evidence labels are used only to align known public event timing with stock-web OHLC rows. They are not current stock discovery and not a recommendation.

