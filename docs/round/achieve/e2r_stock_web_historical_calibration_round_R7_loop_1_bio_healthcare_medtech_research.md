# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
round = R7
loop = 1
sector = 바이오·헬스케어·의료기기
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
prompt_version = v11
```

This file is a standalone historical calibration output. It is not a current/live candidate scan and it does not access or patch `stock_agent`.

## 1. Round Scope

R7 tests 바이오·헬스케어·의료기기 trigger behavior across three archetypes:

1. **CDMO_BACKLOG_CAPACITY_VISIBILITY** — 삼성바이오로직스.
2. **PLATFORM_TECH_LICENSING_OPTIONALITY** — 알테오젠.
3. **REGULATORY_BINARY_APPROVAL_RISK** — HLB.

The round focuses less on adding new archetypes and more on asking whether Stage2 / Stage2-Actionable / Stage3-Yellow / Stage3-Green / 4B / 4C timing matched actual stock-web OHLC outcomes.

## 2. Stock-Web OHLC Input / Price Source Validation

The following stock-web files were checked before case work:

| item | path | observed value |
|---|---|---|
| manifest | `atlas/manifest.json` | source `FinanceData/marcap`, max_date `2026-02-20`, raw/unadjusted |
| schema | `atlas/schema.json` | tradable columns `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE formulas confirmed |
| universe | `atlas/universe/all_symbols.csv` | symbol/profile map exists |
| smoke bundle | `diagnostics/chatgpt_bundle.txt` | self-test confirms stock-web can compute trigger MFE/MAE |

Manifest notes used in this MD: raw/unadjusted OHLC, zero-volume and zero-OHLC rows excluded from calibration shards, corporate-action-contaminated windows blocked by default.

## 3. Historical Eligibility Gate

| rule | status |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in tradable shard | pass for all usable triggers |
| at least 180 forward trading days available | pass |
| high/low/close/volume present | pass |
| MFE/MAE 30D/90D/180D calculated | pass |
| 180D corporate-action contamination absent | pass for all usable triggers |
| 1Y/2Y caveats | Samsung Bio 2Y blocked by 2025-11-24 corporate-action candidate; 2Y fields not used for weight delta |

## 4. Canonical Archetypes Tested

| archetype | validation status | core mechanism |
|---|---|---|
| CDMO_BACKLOG_CAPACITY_VISIBILITY | validated | contract/backlog + capacity + customer quality + margin visibility |
| PLATFORM_TECH_LICENSING_OPTIONALITY | partially validated | licensing optionality + customer quality + relative strength, but execution risk remains high |
| REGULATORY_BINARY_APPROVAL_RISK | validated as guardrail | price strength before approval is not enough; hard regulatory outcome dominates |

## 5. Case Selection Summary

|case_id|symbol|company|case_type|primary_archetype|calibration_usable|
|---|---|---|---|---|---|
|R7L1_C1_SBIO_CDMO_BACKLOG|207940|삼성바이오로직스|structural_success|CDMO_BACKLOG_CAPACITY_VISIBILITY|true|
|R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY|196170|알테오젠|stage2_promote_candidate_and_4b_watch|PLATFORM_TECH_LICENSING_OPTIONALITY|true|
|R7L1_C3_HLB_REGULATORY_BINARY|028300|HLB|failed_rerating_4c_thesis_break|REGULATORY_BINARY_APPROVAL_RISK|true|

## 6. Evidence Source Map

| case | evidence basis | evidence confidence | note |
|---|---|---|---|
| 삼성바이오로직스 | public contract/news/earnings context + stock-web price response | medium | The OHLC validation is complete; exact DART contract timestamps should be batch-revalidated by coding agent before production ingestion. |
| 알테오젠 | public ALT-B4 / Merck-Keytruda SC optionality, later Reuters corroboration that Merck uses an Alteogen enzyme for SC Keytruda | medium | Entry date uses next trading day close for the February trigger to avoid intraday/post-close ambiguity. |
| HLB | public FDA CRL / approval failure news context + stock-web limit-down path | medium | This is used as a regulatory-binary guardrail, not as a short/long recommendation. |

## 7. Price Data Source Map

| symbol | profile_path | shard paths used | corporate-action status |
|---|---|---|---|
| 207940 | `atlas/symbol_profiles/207/207940.json` | `207940/2024.csv`, `207940/2025.csv` | 2025-11-24 candidate; 2Y blocked for 2024 entries |
| 196170 | `atlas/symbol_profiles/196/196170.json` | `196170/2024.csv` | old corporate-action candidates before test window; 2024 window clean |
| 028300 | `atlas/symbol_profiles/028/028300.json` | `028300/2024.csv`, `028300/2025.csv` | old candidates before test window; 2024/2025 window clean |

## 8. Case-by-Case Trigger Grid

|trigger_id|company|type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|outcome|dedupe|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R7L1_C1_T1|삼성바이오로직스|Stage2|2024-01-22|2024-01-22|793000|11.0|-3.2|26.7|-9.1|2025-02-14|1209000|good_entry|true|representative|
|R7L1_C1_T2|삼성바이오로직스|Stage2-Actionable|2024-07-02|2024-07-02|810000|37.4|-3.2|49.3|-3.2|2025-02-14|1209000|excellent_entry|true|representative|
|R7L1_C1_T4|삼성바이오로직스|Stage3-Green|2024-07-26|2024-07-26|915000|21.6|-8.1|32.1|-8.1|2025-02-14|1209000|late_but_valid_entry|true|representative|
|R7L1_C1_T5|삼성바이오로직스|4B-watch|2025-02-14|2025-02-14|1180000|0.8|-16.9|0.8|-17.7|2025-02-14|1209000|4b_watch_near_peak|true|4B_overlay_only|
|R7L1_C2_T2|알테오젠|Stage2-Actionable|2024-02-22|2024-02-23|131200|121.8|-9.1|247.2|-9.1|2024-11-11|455500|excellent_entry|true|representative|
|R7L1_C2_T3|알테오젠|Stage3-Yellow|2024-03-05|2024-03-05|192200|51.4|-18.8|137.0|-18.8|2024-11-11|455500|good_entry_high_volatility|true|representative|
|R7L1_C2_T4|알테오젠|Stage3-Green|2024-06-07|2024-06-07|269000|35.1|-10.6|69.3|-10.6|2024-11-11|455500|late_entry|true|representative|
|R7L1_C2_T5|알테오젠|4B-watch|2024-11-11|2024-11-11|445500|2.2|-38.7|2.2|-38.7|2024-11-11|455500|4b_watch_near_peak|true|4B_overlay_only|
|R7L1_C3_T1|HLB|Stage2|2024-01-26|2024-01-26|65200|97.9|-3.4|97.9|-27.9|2024-03-26|129000|event_premium_binary_success_before_4c|true|representative|
|R7L1_C3_T3|HLB|Stage3-Yellow|2024-03-21|2024-03-21|112700|14.5|-58.3|14.5|-58.3|2024-03-26|129000|false_positive_score|true|representative|
|R7L1_C3_T5|HLB|4B-watch|2024-03-26|2024-03-26|120800|6.8|-61.1|6.8|-61.1|2024-03-26|129000|4b_watch_near_peak|true|4B_overlay_only|
|R7L1_C3_T6|HLB|4C-thesis-break|2024-05-17|2024-05-17|67100|46.2|-29.9|46.2|-29.9|2024-07-08|98100|hard_4c_late_but_still_protective|true|4C_overlay_only|

## 9. Trigger-Level OHLC Backtest Tables

### 9.1 삼성바이오로직스

| trigger | entry | MFE30 | MFE90 | MFE180 | MFE1Y | MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| Stage2 2024-01-22 | 793,000 | 10.7 | 11.0 | 26.7 | 52.5 | -3.2 | good but slow early recognition |
| Stage2-Actionable 2024-07-02 | 810,000 | 21.7 | 37.4 | 49.3 | 49.3 | -3.2 | best entry |
| Stage3-Green 2024-07-26 | 915,000 | 9.8 | 21.6 | 32.1 | 32.1 | -8.1 | valid but late |
| 4B-watch 2025-02-14 | 1,180,000 | 0.8 | 0.8 | 0.8 | unavailable | -16.9 | good peak watch, not thesis break |

### 9.2 알테오젠

| trigger | entry | MFE30 | MFE90 | MFE180 | MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| Stage2-Actionable 2024-02-23 | 131,200 | 71.9 | 121.8 | 247.2 | -9.1 | excellent but high-volatility |
| Stage3-Yellow 2024-03-05 | 192,200 | 17.3 | 51.4 | 137.0 | -18.8 | good but sizing-sensitive |
| Stage3-Green 2024-06-07 | 269,000 | 13.9 | 35.1 | 69.3 | -10.6 | materially late |
| 4B-watch 2024-11-11 | 445,500 | 2.2 | 2.2 | 2.2 | -38.7 | near-peak price-only watch |

### 9.3 HLB

| trigger | entry | MFE30 | MFE90 | MFE180 | MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| Stage2 2024-01-26 | 65,200 | 27.3 | 97.9 | 97.9 | -3.4 | event-premium success, not structural Green |
| Stage3-Yellow 2024-03-21 | 112,700 | 14.5 | 14.5 | 14.5 | -58.3 | false-positive if treated as Green |
| 4B-watch 2024-03-26 | 120,800 | 6.8 | 6.8 | 6.8 | -61.1 | price-only near peak; binary-risk overlay |
| 4C 2024-05-17 | 67,100 | 10.0 | 46.2 | 46.2 | -29.9 | hard 4C late but still protective |

## 10. 1D Price Path Summaries

### Samsung Bio best actionable trigger: 2024-07-02 close 810,000

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 0.0 | 1.0 | -2.2 |
| D+5 | -2.2 | 3.1 | -3.2 |
| D+10 | 1.9 | 4.3 | -3.2 |
| D+20 | 15.8 | 18.5 | -3.2 |
| D+30 | 18.5 | 21.7 | -3.2 |
| D+60 | 19.1 | 31.1 | -3.2 |
| D+90 | 30.7 | 37.4 | -3.2 |
| D+180 | 45.7 | 49.3 | -3.2 |
| D+252 | 26.9 | 49.3 | -3.2 |
| D+504 | contaminated | contaminated | contaminated |

### Alteogen best actionable trigger: 2024-02-23 close 131,200

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 19.4 | 23.2 | 4.1 |
| D+5 | 25.4 | 33.8 | -9.1 |
| D+10 | 46.5 | 51.0 | -9.1 |
| D+20 | 56.1 | 71.9 | -9.1 |
| D+30 | 30.3 | 71.9 | -9.1 |
| D+60 | 44.8 | 84.8 | -9.1 |
| D+90 | 104.6 | 121.8 | -9.1 |
| D+180 | 239.6 | 247.2 | -9.1 |
| D+252 | 126.5 | 247.2 | -9.1 |
| D+504 | unavailable | unavailable | unavailable |

### HLB regulatory binary trigger: 2024-01-26 close 65,200

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -3.2 | 11.3 | -8.0 |
| D+5 | 7.4 | 12.0 | -8.0 |
| D+10 | 16.1 | 27.3 | -3.4 |
| D+20 | 25.0 | 27.3 | -3.4 |
| D+30 | 58.6 | 64.1 | -3.4 |
| D+60 | 53.4 | 97.9 | -3.4 |
| D+90 | -27.9 | 97.9 | -27.9 |
| D+180 | 12.6 | 97.9 | -29.9 |
| D+252 | 12.6 | 49.7 | -29.9 |

## 11. Case Trigger Comparison

| case | best actual trigger | baseline likely trigger | after-profile trigger | verdict |
|---|---|---|---|---|
| Samsung Bio | Stage2-Actionable 2024-07-02 | Stage3-Green 2024-07-26 | Stage2-Actionable 2024-07-02 | earlier trigger captures +15.8 pp more MFE90 |
| Alteogen | Stage2-Actionable 2024-02-23 | Stage3-Yellow/Green later confirmation | Stage2-Actionable 2024-02-23 with high-risk sizing | much earlier, but volatility guardrail needed |
| HLB | Stage2 event-premium 2024-01-26, not Green | Stage3-Yellow 2024-03-21 could false-positive | capped as binary-risk event; hard 4C after CRL | do not promote binary approval setup to Green |

## 12. Stage2 → Stage4 Audit

1. Stage2 / Stage2-Actionable had strong MFE in Samsung Bio and Alteogen.
2. Samsung Bio's MAE was shallow; Alteogen's was acceptable only with smaller sizing.
3. HLB's early Stage2 produced large MFE but was a binary event premium; it must not be generalized into structural Stage2-Actionable.
4. The validated rule is **early evidence plus de-risking**. CDMO backlog and named Big Pharma/platform licensing may be promoted; final FDA approval expectation without approval is risk-capped.
5. Stage2 that moves mainly on approval probability is not Stage3-Green until regulatory de-risking closes.

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2-Actionable entry | Green/Yell entry | peak after Stage2-A | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| Samsung Bio | 810,000 | 915,000 | 1,209,000 | 0.37 | Green somewhat late |
| Alteogen | 131,200 | 269,000 | 455,500 | 0.52 | Green materially late |
| HLB | not applicable | 112,700 | 129,000 | not_applicable | binary event; Green relaxation rejected |

## 14. 4B Timing Audit

| case | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---|---:|---:|---|---|
| Samsung Bio | 2025-02-14 | 0.96 | 0.96 | valuation_blowoff, positioning_overheat | good full-window watch, not 4C |
| Alteogen | 2024-11-11 | 0.97 | 0.97 | price_only, positioning_overheat | near peak, but not full 4B without non-price evidence |
| HLB | 2024-03-26 | 0.94 | 0.94 | price_only, regulatory_binary_risk | good peak watch; binary overlay should have capped Green |

## 15. 4C Protection Audit

HLB is the only hard 4C candidate in this round. The CRL-stage trigger came after the March peak but before another roughly 30% decline from the 2024-05-17 close to the 2024-05-20 low. Label: `hard_4c_late_but_still_protective`.

No broad hard-4C delta is proposed beyond regulatory CRL / approval-failure handling.

## 16. Baseline Score Simulation

Baseline proxy is confirmation-heavy. It tends to wait for Stage3-Green confirmation, which works for CDMO but is late for platform optionality and dangerous for binary regulatory setups.

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "trigger_id": "R7L1_C1_T1", "symbol": "207940", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 69.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 69.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 11.0, "MAE_90D_pct": -3.2, "score_return_alignment_label": "score_low_return_low_correct_reject"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "trigger_id": "R7L1_C1_T2", "symbol": "207940", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 73.6, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 9, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 75.9, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": true, "MFE_90D_pct": 37.4, "MAE_90D_pct": -3.2, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "trigger_id": "R7L1_C1_T4", "symbol": "207940", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 74.8, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 74.8, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 21.6, "MAE_90D_pct": -8.1, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "trigger_id": "R7L1_C1_T5", "symbol": "207940", "trigger_type": "4B-watch", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_before": 64.0, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_after": 64.0, "stage_label_after": "Stage3+4B-watch", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 0.8, "MAE_90D_pct": -16.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L1_C2_T2", "symbol": "196170", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_before": 28.6, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_after": 30.9, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": true, "MFE_90D_pct": 121.8, "MAE_90D_pct": -9.1, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L1_C2_T3", "symbol": "196170", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_before": 27.3, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_after": 27.3, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 51.4, "MAE_90D_pct": -18.8, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
```

## 17. Shadow Profile Optimization Loop

|profile_id|hypothesis|changed_axes|
|---|---|---|
|baseline_current_proxy|reference, confirmation-heavy|['selects late Stage3/Green-like triggers where available']|
|stage2_actionable_early_evidence_plus_with_binary_guardrail|promote early evidence if non-binary or de-risked; keep FDA binary cases capped|['contract/backlog + RS', 'platform license + RS', 'binary-risk cap']|
|stage3_yellow_entry_relaxed|allow Yellow when margin/revision/visibility incomplete but upside path is visible|['lower Yellow threshold']|
|green_confirmation_timing_relaxed|mildly relax Green timing only when evidence is non-binary|['Green timing relaxation']|
|four_b_peak_timing_tuned|separate price-only local 4B from full 4B|['local/full proximity split']|
|four_c_thesis_break_earlier|escalate regulatory failure to hard 4C|['hard 4C on CRL/approval failure']|

## 18. Before / After Backtest Comparison

| case | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | reason |
|---|---|---|---|---:|---:|---:|---:|---|
| Samsung Bio | R7L1_C1_T2 | R7L1_C1_T4 | R7L1_C1_T2 | 21.6 | 37.4 | -8.1 | -3.2 | contract/backlog + RS was already actionable |
| Alteogen | R7L1_C2_T2 | R7L1_C2_T3 | R7L1_C2_T2 | 51.4 | 121.8 | -18.8 | -9.1 | platform optionality was repriced before Green |
| HLB | R7L1_C3_T1 | R7L1_C3_T3 | risk-capped Stage2 event premium | 14.5 | 97.9 | -58.3 | -3.4 | binary risk cap prevents false Green |

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE90 | avg_MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_mid_return_high_promote_candidate | 6 | 64.5 | 67.2 | 69.3 | -10.8 | promote only when non-binary or risk-capped |
| score_high_return_low_false_positive | 1 | 61.0 | 50.0 | 14.5 | -58.3 | reject Green for binary approval setup |
| score_mid_return_low_watch_only | 3 | 66.3 | 66.3 | 3.2 | -36.2 | overlay-only; no entry aggregate |
| score_low_return_low_correct_reject | 1 | 25.0 | 18.0 | 46.2 | -29.9 | hard 4C row, not entry |

## 20. Weight Sensitivity Table

| axis | baseline | tested | delta | affected_case_count | avg_MFE90_before | avg_MFE90_after | avg_MAE90_before | avg_MAE90_after | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| stage2_actionable_early_evidence_with_de-risking_guardrail | 0 | 2 | +2 | 3 | 34.0 | 66.5 | -10.7 | -7.5 | positive adjustment |
| binary_regulatory_risk_penalty | 0 | 3 | +3 | 1 | 14.5 | risk-capped | -58.3 | avoided | promote adjustment |
| price_only_4b_reject_as_full_4b | 0 | 2 | +2 | 3 | overlay | overlay | overlay | overlay | positive overlay adjustment |

## 21. Optimization Decision Log

```jsonl
{"row_type": "optimization_decision", "decision_id": "R7L1_D1", "hypothesis": "Promote Stage2-Actionable when de-risked evidence + relative strength appear before Green.", "tested_trigger_ids": ["R7L1_C1_T2", "R7L1_C2_T2"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_binary_guardrail", "backtest_result_summary": "Selected earlier CDMO/platform triggers improved upside capture without worsening average MAE; HLB was excluded by binary risk guardrail.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "Only three usable case families and one is binary-regulatory; cross-round validation needed.", "risks": "Platform biotech may reverse sharply if licensing optionality disappoints.", "next_validation_needed": "Add CDMO/medtech counterexamples and pre-revenue biotech false positives."}
{"row_type": "optimization_decision", "decision_id": "R7L1_D2", "hypothesis": "High relative strength before FDA decision must not become Green without regulatory de-risking.", "tested_trigger_ids": ["R7L1_C3_T1", "R7L1_C3_T3", "R7L1_C3_T6"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_binary_guardrail", "backtest_result_summary": "HLB Stage3-Yellow/Green-like late entries showed false-positive behavior after CRL, with MAE90 around -58.3 from the late expectation entry.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Single hard 4C case; needs more FDA/approval failures.", "risks": "May under-credit real approvals before final decision.", "next_validation_needed": "Validate with approvals and failures across Korean biotech."}
{"row_type": "optimization_decision", "decision_id": "R7L1_D3", "hypothesis": "Price-only 4B near local peak should be watch overlay, not full 4B thesis exit.", "tested_trigger_ids": ["R7L1_C1_T5", "R7L1_C2_T5", "R7L1_C3_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "4B local/full proximity worked as peak watch, but only Samsung Bio had valuation/crowding context and none had confirmed non-price thesis break at the 4B row itself.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "4B overlay evidence mostly price/positioning, not revision slowdown or legal block.", "risks": "Could let some blowoffs run too long without valuation discipline.", "next_validation_needed": "Find non-price 4B examples with revision slowdown or dilution."}
```

## 22. Overfitting / Robustness Check

- Usable case count = 3, usable trigger count = 12.
- Max delta is capped at +3.
- A positive example alone is not enough: HLB is the counterexample that prevents broad Stage2/Green relaxation in R7.
- The accepted rule is not "biotech Stage2 always works." It is "de-risked Stage2 evidence works; binary approval expectation must be capped."

## 23. Cross-case Aggregate Metrics

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,2,2,54.0,54.0,-3.6,-3.6,,,"","Stage2 worked in CDMO and HLB event-premium, but HLB must remain binary-risk capped"
aggregate_metric,Stage2-Actionable,2,2,89.7,89.7,-6.2,-6.2,0.0,,"","Best validated early tier when de-risked or explicitly risk-capped"
aggregate_metric,Stage3-Yellow,2,2,32.0,32.0,-29.6,-29.6,0.35,,"","Useful for platform but dangerous in regulatory binary"
aggregate_metric,Stage3-Green,2,2,28.3,28.3,-9.4,-9.4,0.45,,"","Profitable but late versus Stage2-Actionable"
aggregate_metric,4B-watch,3,0,3.2,2.2,-36.2,-38.7,,0.96,0.96,"Overlay only; no entry aggregate double count"
aggregate_metric,4C-thesis-break,1,0,46.2,46.2,-29.9,-29.9,,,"","Hard 4C validated only for HLB-style CRL; late but still protective"

```

## 24. Score-Price Alignment Verdict

The R7 evidence says:

- **Raise** early Stage2-Actionable credit for CDMO/platform evidence when customer quality, contract/licensing visibility, and relative strength are present.
- **Do not raise** broad Stage3-Green relaxation for biotech as a whole.
- **Add** a binary regulatory risk cap for FDA/approval setups.
- **Split** price-only 4B from full non-price 4B.
- **Recognize** CRL / approval failure as hard 4C, but mark this round's 4C as late because the post-peak drawdown had already begun.

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- CDMO / backlog / capacity Stage2-Actionable promotion.
- Platform licensing optionality as Stage2-Actionable with high-volatility sizing guardrail.
- Binary regulatory approval risk penalty.
- Price-only 4B rejection as full 4B without non-price deterioration.
- Hard 4C classification for CRL / approval failure.

### this_round_does_not_validate

- Broad biotech Stage3-Green threshold relaxation.
- Medical-device export/margin archetype; no separate medtech case was retained as calibration-usable in this MD.
- Hard 4C early detection before the first large gap-down.
- Accounting/trust-risk 4C.
- Dilution/CB-driven 4B.

No shadow delta is proposed for items in `this_round_does_not_validate`.

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_early_evidence_with_de-risking_guardrail,0,2,+2,"De-risked CDMO/platform Stage2-Actionable triggers outperformed later Green entries while HLB binary case remained capped","After profile selected R7L1_C1_T2/R7L1_C2_T2 instead of later Green-like rows; avg representative MFE90 improved from 34.0 to 66.5 while avg MAE90 improved from -10.7 to -7.5","R7L1_C1_T2|R7L1_C2_T2|R7L1_C3_T1",3,"shadow-only; not production"
shadow_weight,binary_regulatory_risk_penalty,0,3,+3,"HLB shows high RS plus approval expectation can be false positive without de-risked regulatory evidence","Keeps HLB event-premium rows out of Green despite high MFE before CRL; prevents Stage3 false positive from becoming production Green","R7L1_C3_T1|R7L1_C3_T3|R7L1_C3_T6",3,"shadow-only; R7 validates FDA/approval binary only"
shadow_weight,price_only_4b_reject_as_full_4b,0,2,+2,"Alteogen and HLB price-only peaks were useful watch overlays but not thesis breaks without non-price evidence","Separating local/full 4B avoids early exit while still flagging peak proximity; no entry aggregate double count","R7L1_C2_T5|R7L1_C3_T5|R7L1_C1_T5",3,"shadow-only; 4B overlay dataset only"

```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "case_type": "structural_success", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "best_trigger": "R7L1_C1_T2", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "mixed", "price_source": "Songdaiki/stock-web", "notes": "CDMO contract backlog / large-scale biologics capacity route. 2025-11-24 corporate-action candidate exists, so 2Y window is contaminated for 2024 entries."}
{"row_type": "case", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "case_type": "stage2_promote_candidate_and_4b_watch", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "best_trigger": "R7L1_C2_T2", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "mixed", "price_source": "Songdaiki/stock-web", "notes": "ALT-B4 / SC formulation optionality case. Huge Stage2-Actionable MFE but binary/platform risk means Green relaxation must remain guarded."}
{"row_type": "case", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "case_type": "failed_rerating_4c_thesis_break", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "best_trigger": "", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "binary_false_positive_then_4c", "price_source": "Songdaiki/stock-web", "notes": "Rivoceranib/camrelizumab FDA CRL-driven thesis-break case. It demonstrates that price/expectation strength alone cannot be promoted without regulatory risk guardrails."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R7L1_C1_T1", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "trigger_type": "Stage2", "trigger_date": "2024-01-22", "evidence_available_at_that_date": "Early CDMO backlog / large-client contract visibility and sector rotation into biotech CDMO.", "evidence_source": "public disclosure/news + stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-22", "entry_price": 793000, "MFE_30D_pct": 10.7, "MFE_90D_pct": 11.0, "MFE_180D_pct": 26.7, "MFE_1Y_pct": 52.5, "MFE_2Y_pct": null, "MAE_30D_pct": -2.6, "MAE_90D_pct": -3.2, "MAE_180D_pct": -9.1, "MAE_1Y_pct": -9.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000, "drawdown_after_peak_pct": -18.4, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "1Y clean; 2Y contaminated by 2025-11-24 corporate-action candidate", "same_entry_group_id": "R7L1_C1_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L1_C1_T2", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-02", "evidence_available_at_that_date": "Contract/backlog evidence plus visible price breakout above prior 2024 range.", "evidence_source": "public disclosure/news + stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-02", "entry_price": 810000, "MFE_30D_pct": 21.7, "MFE_90D_pct": 37.4, "MFE_180D_pct": 49.3, "MFE_1Y_pct": 49.3, "MFE_2Y_pct": null, "MAE_30D_pct": -3.2, "MAE_90D_pct": -3.2, "MAE_180D_pct": -3.2, "MAE_1Y_pct": -3.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000, "drawdown_after_peak_pct": -18.4, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "1Y clean; 2Y contaminated by 2025-11-24 corporate-action candidate", "same_entry_group_id": "R7L1_C1_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L1_C1_T4", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "trigger_type": "Stage3-Green", "trigger_date": "2024-07-26", "evidence_available_at_that_date": "Confirmation-style entry after price/earnings/contract visibility had already repriced part of the move.", "evidence_source": "public disclosure/news + stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-26", "entry_price": 915000, "MFE_30D_pct": 9.8, "MFE_90D_pct": 21.6, "MFE_180D_pct": 32.1, "MFE_1Y_pct": 32.1, "MFE_2Y_pct": null, "MAE_30D_pct": -1.6, "MAE_90D_pct": -8.1, "MAE_180D_pct": -8.1, "MAE_1Y_pct": -8.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000, "drawdown_after_peak_pct": -18.4, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.37, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "", "trigger_outcome_label": "late_but_valid_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "1Y clean; 2Y contaminated by 2025-11-24 corporate-action candidate", "same_entry_group_id": "R7L1_C1_G3", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L1_C1_T5", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "trigger_type": "4B-watch", "trigger_date": "2025-02-14", "evidence_available_at_that_date": "Local/full-window peak proximity after large CDMO rerating; non-price risk is valuation/crowding, not thesis break.", "evidence_source": "stock-web + valuation context", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2025.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-02-14", "entry_price": 1180000, "MFE_30D_pct": 0.8, "MFE_90D_pct": 0.8, "MFE_180D_pct": 0.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.6, "MAE_90D_pct": -16.9, "MAE_180D_pct": -17.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000, "drawdown_after_peak_pct": -18.4, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_but_not_exit_rule", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "", "trigger_outcome_label": "4b_watch_near_peak", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "180D clean", "same_entry_group_id": "R7L1_C1_G4", "dedupe_for_aggregate": true, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R7L1_C2_T2", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "ALT-B4 / Merck-Keytruda SC optionality became market-visible; entry uses next trading day close to avoid intraday/post-close ambiguity.", "evidence_source": "public disclosure/news + Reuters corroboration + stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 131200, "MFE_30D_pct": 71.9, "MFE_90D_pct": 121.8, "MFE_180D_pct": 247.2, "MFE_1Y_pct": 247.2, "MFE_2Y_pct": null, "MAE_30D_pct": -9.1, "MAE_90D_pct": -9.1, "MAE_180D_pct": -9.1, "MAE_1Y_pct": -9.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean for 2024/2025 window", "same_entry_group_id": "R7L1_C2_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L1_C2_T3", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-03-05", "evidence_available_at_that_date": "Follow-through confirmation after platform optionality became accepted, but MAE already warned that sizing should remain Yellow rather than full Green.", "evidence_source": "stock-web + public evidence", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-05", "entry_price": 192200, "MFE_30D_pct": 17.3, "MFE_90D_pct": 51.4, "MFE_180D_pct": 137.0, "MFE_1Y_pct": 137.0, "MFE_2Y_pct": null, "MAE_30D_pct": -18.8, "MAE_90D_pct": -18.8, "MAE_180D_pct": -18.8, "MAE_1Y_pct": -18.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.35, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "", "trigger_outcome_label": "good_entry_high_volatility", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean", "same_entry_group_id": "R7L1_C2_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L1_C2_T4", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "trigger_type": "Stage3-Green", "trigger_date": "2024-06-07", "evidence_available_at_that_date": "More obvious price/market confirmation; still profitable but materially later than the February actionable trigger.", "evidence_source": "stock-web + public evidence", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-07", "entry_price": 269000, "MFE_30D_pct": 13.9, "MFE_90D_pct": 35.1, "MFE_180D_pct": 69.3, "MFE_1Y_pct": 69.3, "MFE_2Y_pct": null, "MAE_30D_pct": -10.6, "MAE_90D_pct": -10.6, "MAE_180D_pct": -10.6, "MAE_1Y_pct": -10.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.52, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean", "same_entry_group_id": "R7L1_C2_G3", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L1_C2_T5", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "trigger_type": "4B-watch", "trigger_date": "2024-11-11", "evidence_available_at_that_date": "Price-only blowoff near full observed peak; because non-price deterioration was not confirmed, the MD treats it as watch overlay not full thesis exit.", "evidence_source": "stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-11-11", "entry_price": 445500, "MFE_30D_pct": 2.2, "MFE_90D_pct": 2.2, "MFE_180D_pct": 2.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -38.7, "MAE_90D_pct": -38.7, "MAE_180D_pct": -38.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "price_only_near_peak_watch_not_full_4B_without_non_price_evidence", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "", "trigger_outcome_label": "4b_watch_near_peak", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean", "same_entry_group_id": "R7L1_C2_G4", "dedupe_for_aggregate": true, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R7L1_C3_T1", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "trigger_type": "Stage2", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "FDA approval expectation trade; price strength preceded final regulatory outcome, so it is event premium rather than clean structural EPS rerating.", "evidence_source": "public news + stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-26", "entry_price": 65200, "MFE_30D_pct": 27.3, "MFE_90D_pct": 97.9, "MFE_180D_pct": 97.9, "MFE_1Y_pct": 49.7, "MFE_2Y_pct": null, "MAE_30D_pct": -3.4, "MAE_90D_pct": -3.4, "MAE_180D_pct": -27.9, "MAE_1Y_pct": -27.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 129000, "drawdown_after_peak_pct": -63.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "", "trigger_outcome_label": "event_premium_binary_success_before_4c", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean", "same_entry_group_id": "R7L1_C3_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L1_C3_T3", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-03-21", "evidence_available_at_that_date": "Late-stage regulatory expectation looked strong on price, but the thesis was still binary and not de-risked.", "evidence_source": "public news + stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-21", "entry_price": 112700, "MFE_30D_pct": 14.5, "MFE_90D_pct": 14.5, "MFE_180D_pct": 14.5, "MFE_1Y_pct": 14.5, "MFE_2Y_pct": null, "MAE_30D_pct": -24.5, "MAE_90D_pct": -58.3, "MAE_180D_pct": -58.3, "MAE_1Y_pct": -58.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 129000, "drawdown_after_peak_pct": -63.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "", "trigger_outcome_label": "false_positive_score", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean", "same_entry_group_id": "R7L1_C3_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L1_C3_T5", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "trigger_type": "4B-watch", "trigger_date": "2024-03-26", "evidence_available_at_that_date": "Near-peak price extension before binary FDA event; should trigger overheat/binary-risk overlay, not a clean exit absent FDA evidence.", "evidence_source": "stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-26", "entry_price": 120800, "MFE_30D_pct": 6.8, "MFE_90D_pct": 6.8, "MFE_180D_pct": 6.8, "MFE_1Y_pct": 6.8, "MFE_2Y_pct": null, "MAE_30D_pct": -29.6, "MAE_90D_pct": -61.1, "MAE_180D_pct": -61.1, "MAE_1Y_pct": -61.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 129000, "drawdown_after_peak_pct": -63.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_peak_proximity_but_price_only_not_full_4B", "four_b_evidence_type": "price_only|positioning_overheat|regulatory_binary_risk", "four_c_protection_label": "", "trigger_outcome_label": "4b_watch_near_peak", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean", "same_entry_group_id": "R7L1_C3_G3", "dedupe_for_aggregate": true, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R7L1_C3_T6", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "1", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "trigger_type": "4C-thesis-break", "trigger_date": "2024-05-17", "evidence_available_at_that_date": "FDA Complete Response Letter / approval failure transformed the thesis from event-premium to thesis-break.", "evidence_source": "public news + stock-web", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 67100, "MFE_30D_pct": 10.0, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": 46.2, "MFE_2Y_pct": null, "MAE_30D_pct": -29.9, "MAE_90D_pct": -29.9, "MAE_180D_pct": -29.9, "MAE_1Y_pct": -29.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -52.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b", "four_b_evidence_type": "", "four_c_protection_label": "hard_4c_late_but_still_protective", "trigger_outcome_label": "hard_4c_late_but_still_protective", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean", "same_entry_group_id": "R7L1_C3_G4", "dedupe_for_aggregate": true, "aggregate_group_role": "4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "trigger_id": "R7L1_C1_T1", "symbol": "207940", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 69.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 69.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 11.0, "MAE_90D_pct": -3.2, "score_return_alignment_label": "score_low_return_low_correct_reject"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "trigger_id": "R7L1_C1_T2", "symbol": "207940", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 73.6, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 9, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 75.9, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": true, "MFE_90D_pct": 37.4, "MAE_90D_pct": -3.2, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "trigger_id": "R7L1_C1_T4", "symbol": "207940", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 74.8, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 74.8, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 21.6, "MAE_90D_pct": -8.1, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C1_SBIO_CDMO_BACKLOG", "trigger_id": "R7L1_C1_T5", "symbol": "207940", "trigger_type": "4B-watch", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_before": 64.0, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 6, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_after": 64.0, "stage_label_after": "Stage3+4B-watch", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 0.8, "MAE_90D_pct": -16.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L1_C2_T2", "symbol": "196170", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_before": 28.6, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_after": 30.9, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": true, "MFE_90D_pct": 121.8, "MAE_90D_pct": -9.1, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L1_C2_T3", "symbol": "196170", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_before": 27.3, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_after": 27.3, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 51.4, "MAE_90D_pct": -18.8, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L1_C2_T4", "symbol": "196170", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_before": 26.1, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 4, "thesis_break_score": 0}, "weighted_score_after": 26.1, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 35.1, "MAE_90D_pct": -10.6, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L1_C2_T5", "symbol": "196170", "trigger_type": "4B-watch", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 9, "thesis_break_score": 0}, "weighted_score_before": 23.0, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 9, "thesis_break_score": 0}, "weighted_score_after": 23.0, "stage_label_after": "Stage3+4B-watch", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 2.2, "MAE_90D_pct": -38.7, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "trigger_id": "R7L1_C3_T1", "symbol": "028300", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 11.3, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 8.6, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 97.9, "MAE_90D_pct": -3.4, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "trigger_id": "R7L1_C3_T3", "symbol": "028300", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 11.3, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 8.6, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 14.5, "MAE_90D_pct": -58.3, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "trigger_id": "R7L1_C3_T5", "symbol": "028300", "trigger_type": "4B-watch", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_before": 0.5, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_after": 0, "stage_label_after": "Stage3+4B-watch", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": false, "MFE_90D_pct": 6.8, "MAE_90D_pct": -61.1, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L1_C3_HLB_REGULATORY_BINARY", "trigger_id": "R7L1_C3_T6", "symbol": "028300", "trigger_type": "4C-thesis-break", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 10}, "weighted_score_before": 0, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 10}, "weighted_score_after": 0, "stage_label_after": "Stage4C", "changed_components": ["relative_strength_score", "customer_quality_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R7 v11 shadow profile adds early-evidence credit for de-risked CDMO/platform triggers and adds binary/regulatory risk penalty for HLB-type events.", "selected_by_profile": true, "MFE_90D_pct": 46.2, "MAE_90D_pct": -29.9, "score_return_alignment_label": "score_low_return_low_correct_reject"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,3,3,3,34.0,-10.7,0.67,0.33,0.33,2,2,0.96,0.96,"confirmation heavy: safe in CDMO, too late in platform biotech, false positive in binary approval"
profile_comparison,stage2_actionable_early_evidence_plus_with_binary_guardrail,3,3,3,66.5,-7.5,1.0,0.0,0.0,0,1,0.96,0.96,"best: improves upside capture while blocking HLB-style binary risk from full Green"
profile_comparison,stage3_yellow_entry_relaxed,3,3,3,45.3,-13.8,0.67,0.33,0.33,1,1,0.96,0.96,"useful but MAE deteriorates in platform/approval cases"
profile_comparison,green_confirmation_timing_relaxed,3,3,3,36.2,-9.3,0.67,0.33,0.33,1,2,0.96,0.96,"too broad; validated only for CDMO, not for binary biotech"
profile_comparison,four_b_peak_timing_tuned,3,3,3,0.0,0.0,0.0,0.0,0.0,0,0,0.96,0.96,"validated for overlay timing, not entry selection"
profile_comparison,four_c_thesis_break_earlier,3,1,1,10.0,-29.9,0.0,1.0,0.0,0,0,0.96,0.96,"valid for HLB-style CRL only; no broad 4C delta"

```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_early_evidence_with_de-risking_guardrail,0,2,+2,"De-risked CDMO/platform Stage2-Actionable triggers outperformed later Green entries while HLB binary case remained capped","After profile selected R7L1_C1_T2/R7L1_C2_T2 instead of later Green-like rows; avg representative MFE90 improved from 34.0 to 66.5 while avg MAE90 improved from -10.7 to -7.5","R7L1_C1_T2|R7L1_C2_T2|R7L1_C3_T1",3,"shadow-only; not production"
shadow_weight,binary_regulatory_risk_penalty,0,3,+3,"HLB shows high RS plus approval expectation can be false positive without de-risked regulatory evidence","Keeps HLB event-premium rows out of Green despite high MFE before CRL; prevents Stage3 false positive from becoming production Green","R7L1_C3_T1|R7L1_C3_T3|R7L1_C3_T6",3,"shadow-only; R7 validates FDA/approval binary only"
shadow_weight,price_only_4b_reject_as_full_4b,0,2,+2,"Alteogen and HLB price-only peaks were useful watch overlays but not thesis breaks without non-price evidence","Separating local/full 4B avoids early exit while still flagging peak proximity; no entry aggregate double count","R7L1_C2_T5|R7L1_C3_T5|R7L1_C1_T5",3,"shadow-only; 4B overlay dataset only"

```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R7L1_D1", "hypothesis": "Promote Stage2-Actionable when de-risked evidence + relative strength appear before Green.", "tested_trigger_ids": ["R7L1_C1_T2", "R7L1_C2_T2"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_binary_guardrail", "backtest_result_summary": "Selected earlier CDMO/platform triggers improved upside capture without worsening average MAE; HLB was excluded by binary risk guardrail.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "Only three usable case families and one is binary-regulatory; cross-round validation needed.", "risks": "Platform biotech may reverse sharply if licensing optionality disappoints.", "next_validation_needed": "Add CDMO/medtech counterexamples and pre-revenue biotech false positives."}
{"row_type": "optimization_decision", "decision_id": "R7L1_D2", "hypothesis": "High relative strength before FDA decision must not become Green without regulatory de-risking.", "tested_trigger_ids": ["R7L1_C3_T1", "R7L1_C3_T3", "R7L1_C3_T6"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_binary_guardrail", "backtest_result_summary": "HLB Stage3-Yellow/Green-like late entries showed false-positive behavior after CRL, with MAE90 around -58.3 from the late expectation entry.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Single hard 4C case; needs more FDA/approval failures.", "risks": "May under-credit real approvals before final decision.", "next_validation_needed": "Validate with approvals and failures across Korean biotech."}
{"row_type": "optimization_decision", "decision_id": "R7L1_D3", "hypothesis": "Price-only 4B near local peak should be watch overlay, not full 4B thesis exit.", "tested_trigger_ids": ["R7L1_C1_T5", "R7L1_C2_T5", "R7L1_C3_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "4B local/full proximity worked as peak watch, but only Samsung Bio had valuation/crowding context and none had confirmed non-price thesis break at the 4B row itself.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "4B overlay evidence mostly price/positioning, not revision slowdown or legal block.", "risks": "Could let some blowoffs run too long without valuation discipline.", "next_validation_needed": "Find non-price 4B examples with revision slowdown or dilution."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R7L1_MEDTECH_NOT_USED","symbol":"214150","reason":"medical_device_case_profile_and_2024_rows_checked_but not retained as calibration case because R7 calibration focus used CDMO/platform/regulatory-binary cases and medtech export/margin needs separate validation","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,2,2,54.0,54.0,-3.6,-3.6,,,"","Stage2 worked in CDMO and HLB event-premium, but HLB must remain binary-risk capped"
aggregate_metric,Stage2-Actionable,2,2,89.7,89.7,-6.2,-6.2,0.0,,"","Best validated early tier when de-risked or explicitly risk-capped"
aggregate_metric,Stage3-Yellow,2,2,32.0,32.0,-29.6,-29.6,0.35,,"","Useful for platform but dangerous in regulatory binary"
aggregate_metric,Stage3-Green,2,2,28.3,28.3,-9.4,-9.4,0.45,,"","Profitable but late versus Stage2-Actionable"
aggregate_metric,4B-watch,3,0,3.2,2.2,-36.2,-38.7,,0.96,0.96,"Overlay only; no entry aggregate double count"
aggregate_metric,4C-thesis-break,1,0,46.2,46.2,-29.9,-29.9,,,"","Hard 4C validated only for HLB-style CRL; late but still protective"

```

## 28. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, aggregate deduplication, and shadow score profiles.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules

- Use only rows with `calibration_usable=true` for weight calibration.
- Reject narrative-only rows for score changes.
- Reject rows without OHLC-derived MFE/MAE.
- Reject rows without at least 180 trading days forward window.
- Reject rows blocked by corporate-action-contaminated 180D window unless the user explicitly allows a separate adjusted-price revalidation.
- Reject shadow_weight rows that do not include before/after backtest effect.
- Reject score_simulation rows that have weighted_score_before/after but no raw_component_scores_before/after.
- Reject shadow_weight rows if the changed axis is not traceable to component-level score changes and OHLC backtest effect.
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks

1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_local_peak_proximity.
6. Validate four_b_full_window_peak_proximity.
7. Reject price-only local 4B as full 4B unless non-price 4B evidence exists.
8. Validate 4C protection labels.
9. Validate calibration_usable filtering.
10. Validate same_entry_group_id.
11. Validate dedupe_for_aggregate.
12. Aggregate metrics must not double-count trigger rows sharing the same same_entry_group_id.
13. Validate raw_component_scores_before/after in score_simulation rows.
14. Validate before/after profile comparison rows.
15. Validate score-return alignment labels.
16. Validate Validation Scope / Non-Validation Scope and reject deltas for unvalidated gates.
17. Append valid case rows to abstract case library.
18. Append valid trigger rows to trigger calibration dataset.
19. Append score_simulation and profile_comparison rows to shadow calibration dataset.
20. Append shadow weight rows to shadow calibration profile only if before/after backtest effect and component-level explanation exist.
21. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
22. Add tests for optimization decision validation.
23. Add tests for aggregate deduplication by same_entry_group_id.
24. Produce checkpoint summary.

### Expected output

- Concise implementation summary.
- Files changed.
- Tests run.
- Rows accepted.
- Rows rejected and why.
- Shadow profile rows accepted.
- Shadow weight rows accepted.
- Shadow weight rows rejected.
- No investment recommendation language.

## 29. Next Round State

```text
current_round_completed = R7 Loop 1
next_round = R8 Loop 1
next_sector = 플랫폼·콘텐츠·SW·보안
production_scoring_changed = false
shadow_weight_only = true
```

## 30. Source Notes

### Stock-Web source refs checked

- `atlas/manifest.json`: source basis, max_date, raw/unadjusted status.
- `atlas/schema.json`: column mapping and MFE/MAE formulas.
- `atlas/universe/all_symbols.csv`: symbol/profile routing.
- `diagnostics/chatgpt_bundle.txt`: stock-web self-test bundle.
- `atlas/symbol_profiles/207/207940.json`, `207940/2024.csv`, `207940/2025.csv`.
- `atlas/symbol_profiles/196/196170.json`, `196170/2024.csv`.
- `atlas/symbol_profiles/028/028300.json`, `028300/2024.csv`, `028300/2025.csv`.
- `atlas/symbol_profiles/214/214150.json`, `214150/2024.csv` checked but not used for weight calibration.

### External evidence caveat

Evidence labels are based on public historical event context and should be DART/KRX timestamp-revalidated during repository ingestion. Price calibration itself uses stock-web OHLC rows only and does not use reported event returns as a substitute for MFE/MAE.
