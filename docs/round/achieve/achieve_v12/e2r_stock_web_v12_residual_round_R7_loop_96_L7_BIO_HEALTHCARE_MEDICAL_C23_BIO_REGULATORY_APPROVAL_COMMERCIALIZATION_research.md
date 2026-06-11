# E2R Stock-Web v12 Residual Research — R7 loop 96 / L7 / C23

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 96
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: REGULATORY_APPROVAL_COMMERCIAL_REVENUE_BRIDGE_VS_APPROVAL_LABEL_EVENT_CAP
loop_contribution_label: canonical_archetype_rule_candidate
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
price_source_repo: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
evidence_url_status: pending_exact_url_verification
source_quality: source_proxy_only
do_not_promote_without_url: true
```

## 1. Selection / novelty check

- `V12_Research_No_Repeat_Index.md` still marks `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` as Priority 0 with `rows=29`, `need_to_30=1`, and the stated research point: approval after commercialization, revenue conversion, insurance/channel/price counterexamples.
- Registry check shows existing C23 files through `R7 loop 95`, so this standalone research uses `R7 loop 96`.
- This file uses the canonical as a compression bucket, not a new runtime enum. The fine sub-archetype is explanatory only.
- Hard duplicate avoidance key used here: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Exact non-price source URL verification was not completed in this run. Every trigger row is therefore marked `source_proxy_only` and `evidence_url_pending`; no production patch should be promoted from this MD alone.

## 2. Price-source validation

Stock-Web basis used:

```text
primary_price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Symbol profile caveats:

| symbol | name | profile status | caveat used in this MD |
|---|---:|---|---|
| 000100 | 유한양행 | active_like | has historical corporate-action candidates, but 2024 trigger window is not inside those dates |
| 326030 | SK바이오팜 | active_like | no corporate-action candidate in profile |
| 068270 | 셀트리온 | active_like | historical discontinuity exists; 2024 trigger window treated as tradable shard only |
| 145020 | 휴젤 | active_like | historical corporate-action candidates exist; 2024 trigger window outside listed candidate dates |

## 3. Research thesis

C23 should not behave like a generic “bio good news” bucket.

The useful signal is narrower:

```text
regulatory approval / label expansion / partner commercialization
  → named product launch or royalty route
  → reimbursement/channel/sales ramp
  → margin or revision bridge
  → price path confirms with controlled MAE
```

The failure mode is:

```text
approval headline or regulatory optionality
  → no verified channel launch / revenue conversion / margin bridge
  → price spike fades
  → Stage2 false positive or local 4B event-cap
```

## 4. Trigger-level cases

| symbol | name | trigger / entry | entry price | peak | trough | MFE | MAE | classification |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 000100 | 유한양행 | 2024-08-21 | 94,300 | 166,900 | 91,500 | +77.0% | -3.0% | positive Green candidate |
| 326030 | SK바이오팜 | 2024-07-17 | 85,100 | 130,000 | 82,900 | +52.8% | -2.6% | positive Yellow→Green candidate |
| 068270 | 셀트리온 | 2024-04-30 | 189,000 | 197,000 | 173,500 | +4.2% | -8.2% | event-cap / Yellow-only counterexample |
| 145020 | 휴젤 | 2024-06-11 | 242,000 | 253,000 | 215,000 | +4.5% | -11.2% | approval headline event-cap counterexample |

### 4.1 Positive path — 000100 유한양행

The price path behaves like approval plus commercialization bridge rather than pure binary-event noise. Entry was set at 2024-08-21 close 94,300. The next trading windows include a contained initial trough at 91,500 and a later peak at 166,900.

Interpretation:

- Approval alone is not enough; this case becomes useful because the commercial path is attached to a named product / partner / royalty-revenue route.
- Current calibrated profile should allow C23 to move from Stage2 to Yellow/Green only when the revenue bridge is explicit.
- This is a possible residual lateness case if the current profile treats the event as generic bio optionality.

### 4.2 Positive path — 326030 SK바이오팜

Entry was set at 2024-07-17 close 85,100. The path later reaches 130,000 by 2024-10-16 with only shallow initial MAE.

Interpretation:

- This is not a new-approval spike. It is closer to “already approved product commercialization / revenue run-rate inflection.”
- C23 should score this differently from clinical optionality because sales conversion is already visible in the market narrative.
- The proposed rule is a Stage2-to-Yellow bridge bonus only when commercial revenue run-rate or operating leverage is present.

### 4.3 Counterexample — 068270 셀트리온

Entry was set at 2024-04-30 close 189,000. The window gives only a weak MFE near 197,000 while the trough reaches 173,500.

Interpretation:

- Large-cap biosimilar regulatory expansion can be directionally valid but still not enough for Green if margin/revision follow-through is not visible.
- This row supports a C23 event-cap guardrail: approval/launch vocabulary alone should not produce full Green.
- Treat as Yellow-only unless revenue, pricing, channel share, or OPM/revision bridge is explicit.

### 4.4 Counterexample — 145020 휴젤

Entry was set at 2024-06-11 close 242,000. The path reaches 253,000 but also drops to 215,000.

Interpretation:

- Botulinum toxin approval/commercialization headlines can be quickly priced.
- Without verified channel launch timing, litigation clearance, reimbursement/channel path, and revenue bridge, this should remain event-cap or local 4B watch.
- This row contributes to a high-MAE guardrail for C23.

## 5. Usable trigger JSONL

```jsonl
{"canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "current_profile_alignment": "profile_should_allow_green_only_when_approval_is_tied_to_named_partner_launch_or_royalty_revenue_bridge", "do_not_promote_without_url": true, "entry_date": "2024-08-21", "entry_price": 94300, "evidence_family": "approval_to_partner_launch_royalty_revenue", "evidence_url_status": "pending_exact_url_verification", "fine_archetype_id": "REGULATORY_APPROVAL_COMMERCIAL_REVENUE_BRIDGE_VS_APPROVAL_LABEL_EVENT_CAP", "forward_window_trading_days": 50, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "mae_pct": -3.0, "mfe_pct": 77.0, "name": "유한양행", "peak_price_in_window": 166900, "post_entry_max_drawdown_pct": -12.8, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source_repo": "Songdaiki/stock-web", "research_round": "R7", "residual_error_type": "possible_green_lateness_if_regulatory_approval_bridge_is_treated_as_generic_bio_event", "result_bucket": "positive_stage3_green_candidate", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 96, "source_quality": "source_proxy_only", "symbol": "000100", "trigger_date": "2024-08-21", "trigger_family": "FDA_APPROVAL_ROYALTY_REVENUE_CONVERSION", "trigger_type": "regulatory_approval_with_partner_commercialization_bridge", "trough_price_in_window": 91500}
{"canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "current_profile_alignment": "commercialized_product_revenue_bridge_should_score_above_binary_approval_event", "do_not_promote_without_url": true, "entry_date": "2024-07-17", "entry_price": 85100, "evidence_family": "approved_product_sales_growth_operating_leverage", "evidence_url_status": "pending_exact_url_verification", "fine_archetype_id": "EXISTING_APPROVED_PRODUCT_REVENUE_INFLECTION_VS_BIO_LABEL_SPIKE", "forward_window_trading_days": 65, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "mae_pct": -2.6, "mfe_pct": 52.8, "name": "SK바이오팜", "peak_price_in_window": 130000, "post_entry_max_drawdown_pct": -12.2, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source_repo": "Songdaiki/stock-web", "research_round": "R7", "residual_error_type": "stage2_to_yellow_lateness_if_sales_runrate_is_not_separated_from_pipeline_optionalities", "result_bucket": "positive_stage3_yellow_to_green_candidate", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 96, "source_quality": "source_proxy_only", "symbol": "326030", "trigger_date": "2024-07-17", "trigger_family": "COMMERCIALIZATION_REVENUE_RAMP_AFTER_APPROVAL", "trigger_type": "approved_product_revenue_runrate_inflection", "trough_price_in_window": 82900}
{"canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "current_profile_alignment": "large_cap_biosimilar_approval_requires_revenue_margin_revision_bridge", "do_not_promote_without_url": true, "entry_date": "2024-04-30", "entry_price": 189000, "evidence_family": "regulatory_expansion_channel_margin_revision", "evidence_url_status": "pending_exact_url_verification", "fine_archetype_id": "BIOSIMILAR_REGULATORY_EXPANSION_COMMERCIALIZATION_BRIDGE_VS_LARGE_CAP_EVENT_CAP", "forward_window_trading_days": 45, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "mae_pct": -8.2, "mfe_pct": 4.2, "name": "셀트리온", "peak_price_in_window": 197000, "post_entry_max_drawdown_pct": -8.2, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source_repo": "Songdaiki/stock-web", "research_round": "R7", "residual_error_type": "false_stage2_if_approval_expansion_is_counted_without_revision_or_margin_bridge", "result_bucket": "counterexample_event_cap_or_yellow_only", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 96, "source_quality": "source_proxy_only", "symbol": "068270", "trigger_date": "2024-04-30", "trigger_family": "BIOSIMILAR_APPROVAL_LAUNCH_REVENUE_BRIDGE", "trigger_type": "biosimilar_commercialization_expansion_without_revision_followthrough", "trough_price_in_window": 173500}
{"canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "current_profile_alignment": "approval_headline_should_be_capped_until_channel_launch_and_margin_bridge_are_verified", "do_not_promote_without_url": true, "entry_date": "2024-06-11", "entry_price": 242000, "evidence_family": "US_approval_channel_launch_litigation_reimbursement", "evidence_url_status": "pending_exact_url_verification", "fine_archetype_id": "BOTULINUM_TOXIN_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_SPIKE_EVENT_CAP", "forward_window_trading_days": 35, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "mae_pct": -11.2, "mfe_pct": 4.5, "name": "휴젤", "peak_price_in_window": 253000, "post_entry_max_drawdown_pct": -11.2, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source_repo": "Songdaiki/stock-web", "research_round": "R7", "residual_error_type": "high_mae_after_approval_headline_without_commercial_bridge", "result_bucket": "counterexample_approval_headline_event_cap", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 96, "source_quality": "source_proxy_only", "symbol": "145020", "trigger_date": "2024-06-11", "trigger_family": "TOXIN_APPROVAL_COMMERCIAL_CHANNEL_BRIDGE", "trigger_type": "botulinum_toxin_approval_event_cap_without_verified_channel_revenue", "trough_price_in_window": 215000}
```

## 6. Aggregate metrics

```json
{
  "row_type": "aggregate_metric",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "trigger_row_count": 4,
  "positive_count": 2,
  "counterexample_count": 2,
  "avg_mfe_pct": 34.6,
  "avg_mae_pct": -6.3,
  "median_mfe_pct": 28.65,
  "median_mae_pct": -5.6,
  "high_mae_over_10pct_count": 1,
  "evidence_url_pending_count": 4,
  "promotion_ready": false
}
```

## 7. Raw component score simulation

Illustrative component profile, not production scoring:

| symbol | industrial / product bridge | regulatory quality | commercialization bridge | revision / margin bridge | price confirmation | trust / caveat | simulated Stage |
|---|---:|---:|---:|---:|---:|---:|---|
| 000100 | 18 | 20 | 19 | 15 | 20 | 7 | Stage3-Green candidate after URL verification |
| 326030 | 17 | 16 | 20 | 15 | 19 | 8 | Stage3-Yellow→Green candidate |
| 068270 | 16 | 17 | 12 | 9 | 8 | 8 | Stage2/Yellow only |
| 145020 | 15 | 18 | 9 | 8 | 7 | 7 | local 4B/event-cap watch |

## 8. Shadow rule candidates

### Candidate A — `c23_regulatory_approval_requires_commercial_bridge`

```json
{
  "row_type": "shadow_weight",
  "axis": "stage2_required_bridge",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "rule": "Do not allow Stage3-Green from regulatory approval vocabulary alone. Require at least two of: named product launch timing, partner royalty or revenue bridge, reimbursement/channel access, margin/revision confirmation, controlled post-entry MAE.",
  "supporting_rows": ["000100", "326030", "068270", "145020"],
  "promotion_ready": false,
  "blocker": "evidence_url_pending"
}
```

### Candidate B — `c23_approval_headline_event_cap`

```json
{
  "row_type": "shadow_weight",
  "axis": "local_4b_watch_guard",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "rule": "If approval or label-expansion headline lacks commercialization/revenue evidence, cap at Stage2/Yellow or local 4B watch even when MFE is positive.",
  "supporting_rows": ["068270", "145020"],
  "promotion_ready": false,
  "blocker": "evidence_url_pending"
}
```

### Candidate C — `c23_existing_product_revenue_bonus`

```json
{
  "row_type": "shadow_weight",
  "axis": "stage2_bonus_candidate_delta",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "rule": "Approved product with visible revenue run-rate and operating leverage can receive a C23 Stage2-to-Yellow bridge bonus, distinct from pipeline or binary approval events.",
  "supporting_rows": ["000100", "326030"],
  "promotion_ready": false,
  "blocker": "evidence_url_pending"
}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","contribution":"separates true approval-to-commercialization rerating from approval-label event caps","positive_rows":["000100","326030"],"counterexample_rows":["068270","145020"],"promotion_ready":false,"blocker":"source_proxy_only"}
{"row_type":"residual_contribution","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","contribution":"adds high-MAE guardrail when regulatory approval lacks verified channel/revenue bridge","high_mae_rows":["145020"],"promotion_ready":false,"blocker":"evidence_url_pending"}
```

## 10. Validation scope

- Validated price rows: yes, via Stock-Web 2024 tradable shards.
- Validated exact non-price URLs: no.
- Corporate action handling: no entry window intentionally placed on profile-listed corporate-action candidate dates.
- Production profile changed: no.
- Code accessed or patched: no.
- Promotion recommendation: hold until exact evidence URL verification.

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this in the research session.

```text
You are the later batch implementation agent for stock_agent.

Input MD:
docs/round/e2r_stock_web_v12_residual_round_R7_loop_96_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md

Tasks:
1. Ingest the trigger JSONL rows.
2. Verify exact non-price evidence URLs for each trigger.
3. Reject or mark pending any source_proxy_only row without URL support.
4. If URL verification passes, evaluate C23-specific patch candidates:
   - c23_regulatory_approval_requires_commercial_bridge
   - c23_approval_headline_event_cap
   - c23_existing_product_revenue_bonus
5. Do not apply production scoring directly from this MD.
6. Preserve C23 as the canonical runtime scope; keep fine_archetype_id explanatory only.
```
