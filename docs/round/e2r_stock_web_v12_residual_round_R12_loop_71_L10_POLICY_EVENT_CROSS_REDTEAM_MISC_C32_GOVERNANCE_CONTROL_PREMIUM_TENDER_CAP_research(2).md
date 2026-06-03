# E2R Stock-Web v12 Residual Research — R12 Loop 71

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R12
completed_loop: 71
next_round: R13
next_loop: 71
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTESTED_TENDER_CONTROL_PREMIUM_CAP_INVERSION
output_file: e2r_stock_web_v12_residual_round_R12_loop_71_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution gate

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as the active execution procedure.  
`docs/core/V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance ledger.

This is not a live stock-discovery run, not a trading recommendation, and not a `stock_agent` code patch.  
The only output is a standalone historical calibration / residual-research Markdown artifact.

### Round resolution

The immediately preceding automation artifact was:

```text
completed_round = R11
completed_loop  = 71
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Therefore:

```text
scheduled_round = R12
scheduled_loop  = 71
```

R12 permits `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or relevant under-covered service/agri/event sectors.  
This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

This is a valid R12 pairing.

---

## 1. Price atlas validation

### Stock-Web manifest snapshot

```json
{
  "price_atlas_repo": "Songdaiki/stock-web",
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "research_pack_default_price_basis": "tradable_raw"
}
```

Manifest notes used in this run:

```text
- OHLC is raw/unadjusted.
- Calibration shards exclude zero-volume and invalid OHLC rows.
- Corporate-action-contaminated windows are blocked by default.
- Forward windows are judged against manifest max_date = 2026-02-20.
```

### Candidate symbol profile checks

| symbol | name in event window | profile status | corporate-action candidate overlap with tested 180 calendar-day window | calibration usable |
|---|---|---|---|---|
| `000670` | 영풍 | active_like | no; profile lists 2025-04-25, outside Sep 2024→Mar 2025 180-calendar-day window | true |
| `036560` | 영풍정밀 | active_like | no; profile lists 2008-04-14 only | true |
| `010130` | 고려아연 | active_like | no corporate-action candidates | true, but reuse-only / anchor case |

---

## 2. No-repeat and novelty check

The no-repeat ledger defines the hard duplicate key as:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C32 is already well covered overall. The ledger snapshot shows:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:
  rows: 122
  symbols: 20
  date_range: 2020-11-16~2024-12-06
  good/bad S2: 45/23
  4B/4C: 35/11
  top covered symbols: 010130(31), 041510(26), 011200(11), 008930(9), UNKNOWN_SYMBOL(8), 000240(5)
```

Therefore this run avoids treating `010130` as a new independent case.  
`010130` is included only as the tender target anchor / holdout validation case because it is the central contested target needed to interpret the control-premium cap behavior.

Targeted hard-duplicate searches performed before writing:

```text
000670 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP + 2024-09-19 -> no direct match found
036560 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP + 2024-10-14 -> no direct match found
010130 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> high repetition risk; reuse only
```

Novelty accounting:

```json
{
  "new_independent_case_count": 2,
  "reuse_case_count": 1,
  "minimum_new_symbol_count": 2,
  "minimum_counterexample_count": 1,
  "minimum_positive_case_count": 1,
  "minimum_new_independent_case_ratio": 0.67,
  "duplicate_status": "pass_with_010130_reuse_only"
}
```

---

## 3. Evidence event

### Event cluster

```text
event_cluster = Korea Zinc / Young Poong / MBK / Bain contested tender-control battle
primary_trigger_date = 2024-09-13
secondary_trigger_date = 2024-10-11
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CONTESTED_TENDER_CONTROL_PREMIUM_CAP_INVERSION
```

### External evidence summary

Public coverage described the following control-premium event chain:

1. On 2024-09-13, MBK Partners and Young Poong launched a tender offer for Korea Zinc, seeking a 6.98%~14.61% stake at KRW 660,000 per share. Reuters reported Korea Zinc opposed the offer as a hostile takeover attempt and that Young Poong was Korea Zinc’s largest shareholder with a 25.4% stake. Reuters also reported Korea Zinc shares jumped and Young Poong shares hit the daily limit after the announcement.

2. On 2024-10-04, MBK/Young Poong raised their Korea Zinc tender offer to KRW 830,000 per share, matching a counteroffer as the control fight intensified. Reuters framed the event as a governance and capital-market test case, with minority shareholders and the National Pension Service relevant to the outcome.

3. On 2024-10-11, Korea Zinc raised its own buyback offer to KRW 890,000 per share and also raised its offer for Young Poong Precision / 영풍정밀 to KRW 35,000 per share. The event converted `036560` from a thematic affiliate into a direct tender-cap test case.

4. On 2024-10-21, Reuters reported a Korean court had rejected Young Poong’s request to block Korea Zinc’s buyback plan. Korea Zinc shares closed near the KRW 890,000 offer price, and MBK/Young Poong had secured more than 5% through their offer, setting up a continuing board-control fight.

### Why this is useful for C32 calibration

C32 usually treats tender price / control premium as a cap-like reference.  
This cluster shows that the cap rule is conditional:

```text
single-bid tender:
  tender price behaves like a near-term valuation ceiling and 4B watch anchor

contested-control tender:
  the first tender cap can be broken when counter-bids, buybacks, legal rulings, and board-control stakes keep repricing the control premium

affiliate or acquirer-side vehicle:
  can show explosive MFE but often has severe MAE and lower clean-cashflow visibility
```

---

## 4. Case design

| case_id | symbol | role in control battle | research role |
|---|---|---|---|
| `R12L71_C32_000670_20240919` | `000670` 영풍 | major shareholder / MBK-allied control vehicle | new independent counterexample + acquirer-side high-MAE guard |
| `R12L71_C32_036560_20241014` | `036560` 영풍정밀 | direct tender target in Korea Zinc defense/counteroffer mechanics | new independent tender-cap counterexample |
| `R12L71_C32_010130_20240919` | `010130` 고려아연 | contested tender target / anchor case | reuse-only holdout validation; do not count as new case |

Research objective:

```text
C32 tender-control events should not use one generic tender-cap rule.
The model needs a tender-control tier router:
- target-company contested tender with real counter-bid mechanics
- direct affiliate tender target with hard price cap / failed post-offer path
- acquirer-side or shareholder-control vehicle with event-driven squeeze and high-MAE risk
```

---

## 5. Stock-Web OHLC excerpts and backtest results

### 5.1 `000670` 영풍 — acquirer-side / large-shareholder control vehicle

Event interpretation:

```text
trigger_date = 2024-09-13
trigger_family = contested_control_bid_acquirer_side_vehicle
entry_rule = next_tradable_open_after_event
entry_date = 2024-09-19
entry_price = 487500.0
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-12,293000.0,299000.0,290500.0,297000.0,2625.0,772663000.0,547085880000.0,1842040,KOSPI
2024-09-13,363000.0,386000.0,362000.0,386000.0,33816.0,12951229500.0,711027440000.0,1842040,KOSPI
2024-09-19,487500.0,501000.0,487000.0,501000.0,24086.0,11904668500.0,922862040000.0,1842040,KOSPI
2024-09-20,620000.0,649000.0,533000.0,570000.0,195343.0,115622888000.0,1049962800000.0,1842040,KOSPI
2024-10-08,346000.0,346000.0,335500.0,336500.0,18092.0,6104147000.0,619846460000.0,1842040,KOSPI
2025-03-10,464000.0,544000.0,464000.0,489000.0,64676.0,33242063500.0,900757560000.0,1842040,KOSPI
2025-03-18,485500.0,503000.0,482000.0,489500.0,5525.0,2719376250.0,901678580000.0,1842040,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 649000 | 2024-09-20 | 335500 | 2024-10-08 | +33.13% | -31.18% |
| 90 calendar days | 649000 | 2024-09-20 | 335500 | 2024-10-08 | +33.13% | -31.18% |
| 180 calendar days | 649000 | 2024-09-20 | 335500 | 2024-10-08 | +33.13% | -31.18% |

Interpretation:

```text
000670 had real governance relevance as the major shareholder / MBK-allied control vehicle.
However, it was not the tender target cash-price instrument. Its huge one-day repricing and subsequent -31% MAE argue for an acquirer-side governance-vehicle guard, not clean Stage3-Green.
```

### 5.2 `036560` 영풍정밀 — direct affiliate tender-cap target

Event interpretation:

```text
trigger_date = 2024-10-11
trigger_family = target_affiliate_counter_tender_price_raise
entry_rule = next_tradable_open_after_offer_raise
entry_date = 2024-10-14
entry_price = 30500.0
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-13,12180.0,12180.0,12180.0,12180.0,310079.0,3776762220.0,191835000000.0,15750000,KOSDAQ
2024-10-04,29900.0,32850.0,29850.0,31850.0,4695834.0,144751357450.0,501637500000.0,15750000,KOSDAQ
2024-10-11,31250.0,31250.0,28300.0,29200.0,1908864.0,56473993500.0,459900000000.0,15750000,KOSDAQ
2024-10-14,30500.0,31400.0,30100.0,30750.0,1974665.0,60672934200.0,484312500000.0,15750000,KOSDAQ
2024-10-25,31200.0,32700.0,21100.0,22700.0,2888203.0,81884563050.0,357525000000.0,15750000,KOSDAQ
2024-11-13,16050.0,16260.0,15190.0,15220.0,189485.0,2948301750.0,239715000000.0,15750000,KOSDAQ
2025-01-02,12310.0,12690.0,12310.0,12600.0,20737.0,258215360.0,198450000000.0,15750000,KOSDAQ
2025-04-07,10410.0,11010.0,10260.0,10290.0,29357.0,304742730.0,162067500000.0,15750000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 32700 | 2024-10-25 | 15190 | 2024-11-13 | +7.21% | -50.20% |
| 90 calendar days | 32700 | 2024-10-25 | 12310 | 2025-01-02 | +7.21% | -59.64% |
| 180 calendar days | 32700 | 2024-10-25 | 10260 | 2025-04-07 | +7.21% | -66.36% |

Interpretation:

```text
036560 is a direct tender-price target, but the entry after the tender raise sat close to the cap zone.
The subsequent path is a strong C32 counterexample:
- limited post-entry upside
- severe MAE
- no durable earnings/FCF bridge
- tender mechanics dominate the price path
```

This is not Stage3-Green. It is a 4B / cap-zone / event-mechanics guardrail case.

### 5.3 `010130` 고려아연 — overcovered anchor / reuse-only holdout

No-repeat status:

```text
010130 is the top-covered C32 symbol in the ledger.
It is included only as anchor context and holdout validation, not as a new independent case.
do_not_count_as_new_case = true
reuse_reason = contested target anchor needed to calibrate cap-inversion behavior
```

Event interpretation:

```text
trigger_date = 2024-09-13
trigger_family = contested_target_tender_offer_with_counter_bid_mechanics
entry_rule = next_tradable_open_after_event
entry_date = 2024-09-19
entry_price = 679000.0
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-12,549000.0,556000.0,522000.0,556000.0,87429.0,47650810000.0,11511025348000.0,20703283,KOSPI
2024-09-13,660000.0,690000.0,655000.0,666000.0,586718.0,392258844000.0,13788386478000.0,20703283,KOSPI
2024-09-19,679000.0,720000.0,667000.0,707000.0,518279.0,361212476000.0,14637221081000.0,20703283,KOSPI
2024-10-04,751000.0,791000.0,748000.0,776000.0,1230027.0,942359157000.0,16065747608000.0,20703283,KOSPI
2024-10-21,827000.0,889000.0,761000.0,877000.0,638694.0,553742244000.0,18156779191000.0,20703283,KOSPI
2024-12-05,1731000.0,2000000.0,1711000.0,2000000.0,95215.0,174160189000.0,41406566000000.0,20703283,KOSPI
2024-12-06,2124000.0,2407000.0,1736000.0,1813000.0,250745.0,524696751000.0,37535052079000.0,20703283,KOSPI
2024-12-18,1123000.0,1136000.0,1066000.0,1066000.0,51163.0,56260089000.0,22069699678000.0,20703283,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 838000 | 2024-10-18 | 664000 | 2024-10-02 | +23.42% | -2.21% |
| 90 calendar days | 2407000 | 2024-12-06 | 664000 | 2024-10-02 | +254.49% | -2.21% |
| 180 calendar days | 2407000 | 2024-12-06 | 664000 | 2024-10-02 | +254.49% | -2.21% |

Interpretation:

```text
010130 is the rare C32 cap-inversion anchor:
the first tender cap did not behave as a ceiling because the situation evolved into a live contested-control auction with counteroffers, buyback mechanics, legal rulings, and board-control stakes.
```

This anchor should not be used to loosen all C32 cases. It should instead define the exception branch.

---

## 6. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R12L71_C32_TENDER_CAP_INVERSION","round":"R12","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTESTED_TENDER_CONTROL_PREMIUM_CAP_INVERSION","symbol":"000670","name":"영풍","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"contested_control_bid_acquirer_side_vehicle","trigger_date":"2024-09-13","entry_date":"2024-09-19","entry_price":487500.0,"entry_price_type":"next_tradable_open_after_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":33.13,"mae_30d_pct":-31.18,"mfe_90d_pct":33.13,"mae_90d_pct":-31.18,"mfe_180d_pct":33.13,"mae_180d_pct":-31.18,"peak_price_180d":649000.0,"peak_date_180d":"2024-09-20","trough_price_180d":335500.0,"trough_date_180d":"2024-10-08","calibration_usable":true,"case_polarity":"counterexample","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"medium","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_or_4B-local-watch","residual_error_type":"acquirer_side_control_vehicle_high_mae_should_not_green","do_not_count_as_new_case":false}
{"row_type":"trigger","research_id":"R12L71_C32_TENDER_CAP_INVERSION","round":"R12","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTESTED_TENDER_CONTROL_PREMIUM_CAP_INVERSION","symbol":"036560","name":"영풍정밀","trigger_type":"Stage4B-CapGuard","trigger_family":"target_affiliate_counter_tender_price_raise","trigger_date":"2024-10-11","entry_date":"2024-10-14","entry_price":30500.0,"entry_price_type":"next_tradable_open_after_offer_raise","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.21,"mae_30d_pct":-50.20,"mfe_90d_pct":7.21,"mae_90d_pct":-59.64,"mfe_180d_pct":7.21,"mae_180d_pct":-66.36,"peak_price_180d":32700.0,"peak_date_180d":"2024-10-25","trough_price_180d":10260.0,"trough_date_180d":"2025-04-07","calibration_usable":true,"case_polarity":"counterexample","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"medium","price_only_blowoff":false,"expected_stage_current_profile":"Stage4B-CapGuard","residual_error_type":"direct_tender_target_post_cap_severe_drawdown","do_not_count_as_new_case":false}
{"row_type":"trigger","research_id":"R12L71_C32_TENDER_CAP_INVERSION","round":"R12","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTESTED_TENDER_CONTROL_PREMIUM_CAP_INVERSION","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Actionable-HoldoutValidation","trigger_family":"contested_target_tender_offer_with_counter_bid_mechanics","trigger_date":"2024-09-13","entry_date":"2024-09-19","entry_price":679000.0,"entry_price_type":"next_tradable_open_after_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":23.42,"mae_30d_pct":-2.21,"mfe_90d_pct":254.49,"mae_90d_pct":-2.21,"mfe_180d_pct":254.49,"mae_180d_pct":-2.21,"peak_price_180d":2407000.0,"peak_date_180d":"2024-12-06","trough_price_180d":664000.0,"trough_date_180d":"2024-10-02","calibration_usable":true,"case_polarity":"holdout_positive_anchor","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"high","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_with_C32_cap_inversion_exception","residual_error_type":"overcovered_anchor_do_not_generalize_to_all_tenders","reuse_reason":"C32 top-covered symbol; included only to contrast contested target cap-inversion against newer 000670 and 036560 paths","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

---

## 7. Score simulation and raw component breakdown

This is shadow-only. Production scoring is not changed.

### Simulated components

| symbol | EPS/FCF | visibility | bottleneck/pricing | market mispricing | valuation rerating | capital allocation | information confidence | shadow total | intended stage route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `000670` | 2 | 6 | 5 | 11 | 9 | 8 | 12 | 53 | Stage2-Actionable-Guarded or local 4B watch only |
| `036560` | 1 | 7 | 3 | 9 | 8 | 5 | 11 | 44 | Stage4B-CapGuard / event-mechanics counterexample |
| `010130` | 8 | 15 | 12 | 14 | 18 | 14 | 16 | 97 | holdout anchor; cap-inversion exception, not general C32 loosening |

### Stress-test result

The current calibrated profile should not read `036560` or `000670` as Green simply because the event produced explosive MFE.  
The right mechanism is a C32 tier-router:

```text
- 010130: contested target with counterbid/buyback mechanics -> tender cap can invert upward
- 036560: direct tender-affiliate target near cap -> 4B/cap guard, severe post-cap MAE
- 000670: acquirer-side control vehicle -> event relevance exists, but high-MAE and uncertain direct return path block Green
```

---

## 8. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R12L71_C32_TENDER_CAP_INVERSION",
  "round": "R12",
  "loop": 71,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "CONTESTED_TENDER_CONTROL_PREMIUM_CAP_INVERSION",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "new_independent_case_count": 2,
  "reuse_case_count": 1,
  "positive_anchor_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 2,
  "avg_mfe_90d_pct_all": 98.28,
  "avg_mae_90d_pct_all": -31.01,
  "avg_mfe_90d_pct_new_independent_only": 20.17,
  "avg_mae_90d_pct_new_independent_only": -45.41,
  "worst_mae_180d_pct": -66.36
}
```

---

## 9. Shadow rule candidate

### Proposed rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTESTED_TENDER_CONTROL_PREMIUM_CAP_INVERSION
rule_name: C32_contested_tender_tier_router
production_scoring_changed: false
shadow_weight_only: true
```

### Rule logic

```text
For C32 tender/control premium events, classify the event route before applying tender-cap logic.

Tier A: contested target with active counter-bid / buyback / legal-control mechanics
  Evidence:
    - target-company tender or buyback
    - credible competing control groups
    - repeated offer-price raises or board-control fight
  Routing:
    - allow Stage2-Actionable
    - do not automatically 4B at first tender cap
    - cap-inversion exception allowed
    - Green still requires durable non-price bridge or high-confidence governance/capital-return outcome

Tier B: direct affiliate / secondary tender target near cap
  Evidence:
    - explicit tender price exists
    - stock trades near/above offer cap
    - limited operating thesis beyond tender mechanics
  Routing:
    - Stage4B-CapGuard
    - do not give Stage3-Green
    - high MAE after tender mechanics should count as counterexample

Tier C: acquirer-side / shareholder-control vehicle
  Evidence:
    - owns relevant stake or participates in bid
    - price reprices due to control optionality
    - no direct tender cash price for that ticker
  Routing:
    - Stage2-Actionable-Guarded at most
    - block Green
    - high-MAE guard required
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c32_tender_control_tier_router",
  "scope": "canonical_archetype_id:C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "proposal": {
    "contested_target_cap_inversion_exception": true,
    "direct_affiliate_tender_cap_guard": true,
    "acquirer_side_vehicle_green_allowed": false,
    "acquirer_side_vehicle_high_mae_guard": true,
    "stage3_green_requires_post_tender_non_price_bridge": true
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "Two new independent C32 paths show that acquirer-side and affiliate-tender vehicles carry high MAE, while the overcovered 010130 target path shows a cap-inversion exception that should not be generalized."
}
```

---

## 10. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R12L71_C32_TENDER_CAP_INVERSION",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "contribution": "Adds a C32 tender-control tiering rule: contested target cap-inversion is different from affiliate tender-cap and acquirer-side control-vehicle repricing. This prevents high-MFE governance vehicles from contaminating Stage3-Green while preserving the special cap-inversion behavior of true contested targets.",
  "positive_case_added": 0,
  "holdout_positive_anchor_added": 1,
  "counterexample_case_added": 2,
  "new_independent_case_count": 2,
  "guardrail_added": "C32 acquirer-side and affiliate tender paths require 4B/cap-guard routing unless post-tender non-price evidence appears.",
  "4b_split": {
    "local_4b_watch": ["000670"],
    "stage4b_cap_guard": ["036560"],
    "cap_inversion_exception_anchor": ["010130"]
  }
}
```

---

## 11. Validation scope

```yaml
validation_scope:
  price_source: Songdaiki/stock-web
  price_basis: tradable_raw
  price_adjustment_status: raw_unadjusted_marcap
  manifest_max_date: 2026-02-20
  forward_window_required: 180_calendar_days
  forward_window_available: true
  raw_shard_used_for_weight_calibration: false
  corporate_action_contaminated_180D_window:
    000670: false
    036560: false
    010130: false
  evidence_url_pending:
    000670: false
    036560: false
    010130: false
  source_proxy_only:
    000670: false
    036560: false
    010130: false
  reuse_policy:
    010130:
      reuse_reason: "overcovered C32 anchor; not counted as new independent case"
      independent_evidence_weight: 0.0
      do_not_count_as_new_case: true
```

Limitations:

```text
- This run does not attempt legal-outcome prediction.
- It does not verify all post-2024 board-control outcomes.
- It uses 010130 only as a holdout anchor because the no-repeat ledger marks it as highly covered.
- It should not trigger production scoring changes by itself.
```

---

## 12. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows.
2. Preserve R12 / loop 71 metadata.
3. Treat 010130 as reuse-only holdout validation with independent_evidence_weight = 0.0.
4. Treat 000670 and 036560 as new independent C32 examples if parser validation passes.
5. Add a shadow-only rule candidate named C32_contested_tender_tier_router.
6. Do not loosen Stage3-Green.
7. Do not generalize the 010130 cap-inversion path to all tender events.
8. Add guardrails:
   - acquirer-side control vehicle -> no Green; high-MAE guard
   - affiliate tender target near cap -> Stage4B-CapGuard
   - contested target with counter-bid mechanics -> cap-inversion exception possible, but Green requires post-tender non-price bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 13. Next round state

```text
completed_round = R12
completed_loop = 71
next_round = R13
next_loop = 71
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
next_allowed_scope = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW or R13_CROSS_ARCHETYPE_4B_4C_REDTEAM or R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION or R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
