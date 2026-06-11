# E2R v12 Residual Research — R8 loop 98 / L8 / C27 Content IP Global Monetization

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 98
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_KPOP_DRAMA_IP_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_AND_TRUST_BREAK
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - high_MAE_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_allowed: false
current_stock_discovery_allowed: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
source_proxy_only: true
evidence_url_pending: true
promotion_ready: false
```

## 1. Selection and novelty check

This loop uses `V12_Research_No_Repeat_Index.md` only as the duplicate-prevention and coverage ledger. C27 remains in Priority 0 with 24 rows and still needs six rows to reach the minimum 30-row stability band. The prior registry already has R8/C27 through loop 97, so this output uses loop 98.

Novelty target:

```text
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
selected_round = R8
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
selected_loop = 98
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

This file intentionally avoids making a production scoring patch. It adds new trigger families for:

```text
- game IP live-ops monetization bridge
- same-IP late extension local 4B watch
- launch-day hit risk without recurring monetization bridge
- game pipeline optionality event cap
- K-pop IP trust/governance break override
- drama studio windowing spike without repeat global platform monetization
```

## 2. Price source validation

```yaml
price_atlas_repo: Songdaiki/stock-web
manifest_checked: atlas/manifest.json
schema_checked: atlas/schema.json
source_name: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
calculation_basis: high/low from entry_date forward
mfe_formula: (max high from entry_date through N tradable rows / entry_price - 1) * 100
mae_formula: (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Profile-level caveats:

```text
259960 Krafton: active_like, no corporate-action candidate in profile window.
251270 Netmarble: active_like, no corporate-action candidate in profile window.
263750 Pearl Abyss: active_like, corporate-action candidate only historical 2021 window; 2024 path treated usable with caveat.
352820 HYBE: active_like, no corporate-action candidate in profile window.
253450 Studio Dragon: active_like, no corporate-action candidate in profile window.
```

## 3. Thesis compression

C27 should not reward the mere existence of IP. In this sector, IP is an engine, but monetization is the gearbox. A hit title, drama release, artist fandom, or webtoon optionality can make the engine roar for a week; the rerating only earns a durable Stage3 path when that roar is coupled to repeat revenue, live-ops retention, platform distribution, licensing windows, margin expansion, and revision evidence.

Therefore the proposed C27 compression is:

```text
C27 Green candidate =
  global IP or platform distribution
  + repeat monetization evidence
  + margin / revision bridge
  + price path not already in local/full 4B extension

C27 event-cap / Yellow =
  one-off hit, trailer, launch, lineup, label, or fanbase
  + no repeat monetization bridge yet
  + MFE exists but MAE is high or post-spike retention is weak

C27 4C / Red override =
  IP strength exists
  + governance/trust break, channel breakdown, cancellation, or monetization failure
  + price path confirms drawdown or lower-high behavior
```

## 4. Trigger rows

| row | symbol | name | trigger date | trigger family | entry | peak used | trough used | MFE90 | MAE90 | interpretation |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | 259960 | 크래프톤 | 2024-03-27 | game IP live-ops monetization bridge | 257000 | 302000 | 225000 | 17.51 | -12.45 | Positive C27 bridge candidate. Live-ops monetization can carry a Stage3 path, but only with revision/margin evidence. |
| 2 | 259960 | 크래프톤 | 2024-08-13 | late live-ops rerating extension | 331000 | 355000 | 308000 | 7.25 | -6.95 | Same IP, but late extension. Should not receive a new Green unless a fresh monetization bridge appears. |
| 3 | 251270 | 넷마블 | 2024-05-10 | new game launch hit-risk event | 69400 | 72400 | 52400 | 4.32 | -24.50 | Event spike with high MAE. Needs event-cap / no Green without repeat sales retention. |
| 4 | 263750 | 펄어비스 | 2024-05-10 | game pipeline optionality | 37300 | 47650 | 34500 | 27.75 | -7.51 | MFE exists, but optionality is not monetization. Keep as Yellow/event-cap until revenue bridge. |
| 5 | 352820 | 하이브 | 2024-04-18 | K-pop IP label before trust break | 228500 | 232000 | 178700 | 1.53 | -21.79 | IP label cannot override governance/trust break. 4C/Red override candidate. |
| 6 | 253450 | 스튜디오드래곤 | 2024-05-09 | drama windowing content spike | 46400 | 47350 | 39900 | 2.05 | -14.01 | Content windowing label failed to sustain without repeat platform monetization or margin bridge. |

## 5. JSONL trigger rows

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R8", "loop": 98, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_LIVEOPS_GLOBAL_MONETIZATION_MARGIN_BRIDGE_VS_ONE_OFF_CONTENT_HIT_EVENT_CAP", "symbol": "259960", "name": "크래프톤", "trigger_date": "2024-03-27", "entry_date": "2024-03-27", "entry_price": 257000, "trigger_type": "game_ip_liveops_global_monetization_bridge", "evidence_family": "source_proxy_only__pubg_liveops_global_revenue_margin_bridge", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 5.45, "mae_30d_pct": -12.45, "mfe_90d_pct": 17.51, "mae_90d_pct": -12.45, "mfe_180d_pct": 38.13, "mae_180d_pct": -12.45, "peak_price_used": 355000, "trough_price_used": 225000, "current_profile_expected_stage": "Stage3-Yellow_to_Stage3-Green_candidate", "observed_alignment": "positive_asymmetry_after_visible_monetization_bridge", "residual_label": "positive_control", "source_proxy_only": true, "evidence_url_pending": true, "do_not_count_for_promotion_until_url_verified": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R8", "loop": 98, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_LIVEOPS_LATE_EXTENSION_LOCAL_4B_WATCH", "symbol": "259960", "name": "크래프톤", "trigger_date": "2024-08-13", "entry_date": "2024-08-13", "entry_price": 331000, "trigger_type": "late_liveops_rerating_extension", "evidence_family": "source_proxy_only__same_ip_monetization_but_price_extension", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 7.25, "mae_30d_pct": -6.95, "mfe_90d_pct": 7.25, "mae_90d_pct": -6.95, "mfe_180d_pct": 7.25, "mae_180d_pct": -6.95, "peak_price_used": 355000, "trough_price_used": 308000, "current_profile_expected_stage": "Stage3-Yellow_or_4B_local_watch", "observed_alignment": "positive_but_late_extension_should_not_get_fresh_green_without_new_bridge", "residual_label": "local_4b_watch_guard", "source_proxy_only": true, "evidence_url_pending": true, "do_not_count_for_promotion_until_url_verified": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R8", "loop": 98, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "MOBILE_GAME_LAUNCH_HIT_RISK_VS_RECURRING_GLOBAL_MONETIZATION", "symbol": "251270", "name": "넷마블", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 69400, "trigger_type": "new_game_launch_hit_risk_event", "evidence_family": "source_proxy_only__launch_day_spike_without_repeat_monetization_bridge", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 4.32, "mae_30d_pct": -24.5, "mfe_90d_pct": 4.32, "mae_90d_pct": -24.5, "mfe_180d_pct": 4.32, "mae_180d_pct": -24.5, "peak_price_used": 72400, "trough_price_used": 52400, "current_profile_expected_stage": "Stage2_or_Stage3-Yellow_event_cap", "observed_alignment": "counterexample_high_mae_after_launch_spike", "residual_label": "event_cap_required", "source_proxy_only": true, "evidence_url_pending": true, "do_not_count_for_promotion_until_url_verified": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R8", "loop": 98, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "OPENWORLD_GAME_OPTIONALITY_EVENT_CAP_VS_GLOBAL_RECURRING_MONETIZATION", "symbol": "263750", "name": "펄어비스", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 37300, "trigger_type": "game_pipeline_optionality_price_spike", "evidence_family": "source_proxy_only__pipeline_optionality_without_liveops_revenue_bridge", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 15.28, "mae_30d_pct": -7.51, "mfe_90d_pct": 27.75, "mae_90d_pct": -7.51, "mfe_180d_pct": 27.75, "mae_180d_pct": -7.51, "peak_price_used": 47650, "trough_price_used": 34500, "current_profile_expected_stage": "Stage3-Yellow_with_event_cap", "observed_alignment": "mfe_available_but_should_stay_event_cap_until_launch_revenue_bridge", "residual_label": "mfe_without_monetization_bridge", "source_proxy_only": true, "evidence_url_pending": true, "do_not_count_for_promotion_until_url_verified": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R8", "loop": 98, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_IP_GOVERNANCE_TRUST_BREAK_VS_GLOBAL_FANDOM_LABEL", "symbol": "352820", "name": "하이브", "trigger_date": "2024-04-18", "entry_date": "2024-04-18", "entry_price": 228500, "trigger_type": "kpop_ip_global_fandom_label_pre_break", "evidence_family": "source_proxy_only__ip_label_but_governance_trust_break_overrides", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 1.53, "mae_30d_pct": -18.73, "mfe_90d_pct": 1.53, "mae_90d_pct": -21.79, "mfe_180d_pct": 1.53, "mae_180d_pct": -21.79, "peak_price_used": 232000, "trough_price_used": 178700, "current_profile_expected_stage": "4C_or_Stage3-Red_after_trust_break", "observed_alignment": "hard_counterexample_ip_strength_overridden_by_trust_break", "residual_label": "trust_break_override", "source_proxy_only": true, "evidence_url_pending": true, "do_not_count_for_promotion_until_url_verified": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R8", "loop": 98, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "DRAMA_STUDIO_WINDOWING_EVENT_CAP_VS_REPEAT_GLOBAL_PLATFORM_MONETIZATION", "symbol": "253450", "name": "스튜디오드래곤", "trigger_date": "2024-05-09", "entry_date": "2024-05-09", "entry_price": 46400, "trigger_type": "content_studio_windowing_spike", "evidence_family": "source_proxy_only__drama_windowing_label_without_repeat_margin_bridge", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 2.05, "mae_30d_pct": -11.53, "mfe_90d_pct": 2.05, "mae_90d_pct": -14.01, "mfe_180d_pct": 2.05, "mae_180d_pct": -14.01, "peak_price_used": 47350, "trough_price_used": 39900, "current_profile_expected_stage": "Stage2_or_Yellow_only", "observed_alignment": "content_label_spike_failed_to_hold_without_repeat_monetization", "residual_label": "content_windowing_false_stage2", "source_proxy_only": true, "evidence_url_pending": true, "do_not_count_for_promotion_until_url_verified": true}
```

## 6. Aggregate metric

```json
{
  "row_type": "aggregate_metric",
  "round": "R8",
  "loop": 98,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "trigger_row_count": 6,
  "positive_control_count": 1,
  "counterexample_or_guardrail_count": 5,
  "avg_mfe_90d_pct": 10.07,
  "avg_mae_90d_pct": -14.53,
  "main_residual": "C27 should require repeat monetization/revision bridge; one-off IP labels create MFE but often carry high MAE or decay.",
  "production_patch_ready": false,
  "blocked_reason": "source_proxy_only and evidence_url_pending"
}
```

## 7. Current calibrated profile stress test

The current profile should already block many price-only blowoffs through 4B and should not promote source-proxy-only rows. The residual test here is narrower:

```text
Problem:
  C27 can still look deceptively strong when IP-language and MFE arrive together.
  In entertainment/game/content names, MFE can be produced by trailer, launch, fandom,
  or distribution headlines before repeat monetization is proven.

Stress-test result:
  - Krafton 2024-03-27 is the positive control: repeat live-ops monetization can justify Stage3.
  - Krafton 2024-08-13 is not the same evidence quality: same IP after rerating becomes local 4B watch unless new data arrives.
  - Netmarble 2024-05-10 and Studio Dragon 2024-05-09 show one-off hit/windowing events with insufficient retention bridge.
  - Pearl Abyss 2024-05-10 shows strong MFE, but the correct label is event-cap until launch revenue arrives.
  - HYBE 2024-04-18 shows that governance/trust break should dominate IP strength and route toward 4C/Red.
```

## 8. Shadow rule candidate

```yaml
shadow_rule_candidate:
  id: C27_REPEAT_MONETIZATION_BRIDGE_REQUIRED
  scope:
    large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
    canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
  condition:
    all:
      - content_ip_or_game_or_kpop_or_drama_label_present: true
      - repeat_monetization_or_margin_revision_bridge: false
  effect:
    max_stage_without_bridge: Stage3-Yellow
    green_allowed: false
    local_4b_watch_if_price_extension: true
  positive_exception:
    repeat_liveops_or_platform_revenue_bridge_present: true
    margin_or_revision_bridge_present: true
  hard_negative_override:
    governance_trust_break_or_channel_break: true
    route: 4C_or_Stage3-Red
  confidence: medium
  promotion_ready: false
  block_reason:
    - evidence_url_pending
    - source_proxy_only
```

## 9. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "round": "R8",
  "loop": 98,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "residual_error_found": true,
  "residual_error_type": [
    "one_off_hit_event_mfe_without_repeat_monetization_bridge",
    "same_ip_late_extension_false_green_risk",
    "ip_strength_overridden_by_governance_trust_break"
  ],
  "suggested_axis": [
    "C27_REPEAT_MONETIZATION_BRIDGE_REQUIRED",
    "C27_CONTENT_EVENT_CAP",
    "C27_TRUST_BREAK_OVERRIDE"
  ],
  "production_patch_ready": false,
  "why_not_ready": "Non-price evidence remains source-proxy-only and exact URL validation is pending."
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the current research session.

```text
You are a later coding agent. Ingest this MD only after exact non-price evidence URLs have been verified.
Parse all JSONL trigger rows. Add them to v12 calibration only if:
1. price_source == Songdaiki/stock-web,
2. price_basis == tradable_raw,
3. price_adjustment_status == raw_unadjusted_marcap,
4. source_proxy_only is false or evidence_url_pending has been resolved,
5. hard duplicate key canonical_archetype_id + symbol + trigger_type + entry_date is not already present.

If enough independently verified C27 rows support the same axis, consider a scoped shadow rule:
C27_REPEAT_MONETIZATION_BRIDGE_REQUIRED.
Do not create a global rule from this MD alone.
```

## 11. Next research state

```text
completed_round = R8
completed_loop = 98
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```
