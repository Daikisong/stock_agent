# E2R v12 Residual Research — R5 / L5 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R5
selected_loop = 114
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_BRIDGE_VS_BRAND_LABEL_FALSE_POSITIVE
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection and no-repeat check

`V12_Research_No_Repeat_Index.md` marks `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` as Priority 0 with only 6 rows, needing 24 more rows to reach the 30-row minimum. This run adds four new independent trigger rows, so the static-index view becomes `C20 rows 6 → 10 if accepted`.

Conversation-local ledger check: earlier generated files in this session covered C21, C22, C25, C03, C16, C17, C23, C05, C24, C13, C12, C28, C19, C27, C02, C18, C26, C29, C30, C31, C32, C04, and C15. No C20 file has been generated in this session. The selected no-repeat keys are new at the conversation-local level:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|257720|Stage3-Yellow|2024-03-20
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|192820|Stage3-Yellow|2024-04-01
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|161890|Stage2-Actionable|2024-04-01
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|4B|2024-04-30
```

## 2. Research thesis

C20 is not simply “K-beauty/K-food went up.” The useful distinction is whether the story moves through the business plumbing:

```text
channel/global_distribution → sell-through/reorder → ODM or distributor revenue conversion → OPM/revision/FCF
```

A retailer-like channel signal is a pipe. A brand headline is a signboard. The signboard may bring traffic, but only the pipe tells us whether repeat orders and margin pressure can carry cash through the system. This run therefore tests both sides:

- positive distributor/ODM cases where price follow-through was backed by a plausible repeat-order or margin-bridge proxy;
- a large-brand false positive where local price strength failed to survive the 90/180D path and should remain capped at 4B unless non-price evidence proves sell-through/revision persistence.

## 3. Validation scope

```text
primary_price_source = Songdaiki/stock-web
validated_price_rows = 2024 1D OHLCV symbol-year CSV shards
profile_status_check = symbol_profiles JSON
non_price_evidence_status = source_proxy_only / evidence_url_pending=true
calibration_caveat = raw_unadjusted_marcap; corporate action candidate windows blocked by default
deduplication = canonical_archetype_id + symbol + trigger_type + entry_date
```

Profile notes:

| symbol | name | profile status | caveat |
|---|---|---|---|
| 257720 | 실리콘투 | active_like | 2024 rows used; prior 2022 corporate-action candidate exists, not inside 2024 trigger window |
| 192820 | 코스맥스 | active_like | no major raw discontinuity in profile |
| 161890 | 한국콜마 | active_like | no major raw discontinuity in profile |
| 090430 | 아모레퍼시픽 | active_like | old corporate-action candidate exists; 2024 trigger window used |

## 4. Case-level result table

| case | symbol | entry | trigger_type | outcome | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---:|---|---:|---|---|---:|---:|---:|---|
| 1 | 257720 실리콘투 | 10,750 | Stage3-Yellow | positive | +44.19 / -9.77 | +404.19 / -9.77 | +404.19 / -9.77 | distributor/reorder bridge was the missing axis; price path was not merely theme beta |
| 2 | 192820 코스맥스 | 130,000 | Stage3-Yellow | mixed_positive | +32.46 / -7.46 | +60.00 / -7.46 | +60.00 / -10.77 | ODM/customer-mix bridge works, but peak-after-bridge high-MAE guard is still needed |
| 3 | 161890 한국콜마 | 51,500 | Stage2-Actionable | positive_slow_burn | +7.18 / -7.38 | +45.63 / -7.38 | +52.82 / -7.38 | early path was quiet; C20 needs a slow-burn ODM margin bridge so this is not under-scored |
| 4 | 090430 아모레퍼시픽 | 169,500 | 4B | counterexample | +18.29 / -4.78 | +18.29 / -13.92 | +18.29 / -37.58 | brand-label local breakout failed; cap at 4B unless sell-through/revision bridge is explicit |

## 5. Price evidence excerpts

The price rows are from stock-web `atlas/ohlcv_tradable_by_symbol_year`. They are included here so later ingestion can verify the trigger and peak/trough anchors without re-opening the chat.

### 257720 실리콘투

Profile confirms `257720` is `실리콘투`, KOSDAQ, active-like, with 2024 row file available. The 2024 trigger path shows the break beginning near 2024-03-20 and expanding through 2024-06-19:

```text
2024-03-20,9730.0,10750.0,9700.0,10750.0,...
2024-04-01,11940.0,13200.0,11940.0,12900.0,...
2024-05-02,14940.0,15500.0,14740.0,14850.0,...
2024-05-10,22000.0,26250.0,21550.0,26250.0,...
2024-06-19,50900.0,54200.0,48300.0,50700.0,...
```

The path behaves like a repeat-demand rerating: the first leg gave +44.19% 30D MFE, then the 90D path carried all the way to +404.19%. In C20, this is the cleanest case for separating “global distribution channel” from generic beauty theme.

### 192820 코스맥스

Profile confirms `192820` is `코스맥스`, KOSPI, active-like, with no profile-level major raw discontinuity. The 2024 path:

```text
2024-04-01,122000.0,131000.0,121000.0,130000.0,...
2024-04-04,126400.0,129500.0,120300.0,128700.0,...
2024-05-14,161700.0,172200.0,158900.0,160500.0,...
2024-06-14,191400.0,208000.0,184900.0,184900.0,...
2024-08-13,134500.0,134500.0,116000.0,117700.0,...
```

The 90D upside was strong, but the later drawdown says the model should not blindly upgrade every ODM name after the first price thrust. The needed rule is not “beauty ODM + up”; it is “ODM customer mix and margin revision still alive after the first peak.”

### 161890 한국콜마

Profile confirms `161890` is `한국콜마`, KOSPI, active-like, with no profile-level major raw discontinuity. The 2024 path:

```text
2024-04-01,46600.0,51900.0,46400.0,51500.0,...
2024-04-11,48700.0,49300.0,47700.0,48650.0,...
2024-05-10,51700.0,55200.0,49400.0,55200.0,...
2024-06-19,71600.0,75000.0,67600.0,68600.0,...
2024-09-30,78600.0,78700.0,72600.0,74400.0,...
```

This was not an immediate 30D rip like 실리콘투. It was a slow-burn path: modest 30D MFE but very strong 90/180D MFE. That is exactly why C20 needs a bridge that can keep slow ODM winners from being thrown away merely because the first month is not explosive.

### 090430 아모레퍼시픽

Profile confirms `090430` is `아모레퍼시픽`, KOSPI, active-like. The 2024 path:

```text
2024-04-30,163000.0,170000.0,161300.0,169500.0,...
2024-05-31,191300.0,200500.0,188000.0,194200.0,...
2024-07-04,150200.0,150700.0,145900.0,148700.0,...
2024-10-31,119300.0,120100.0,114600.0,116600.0,...
2024-11-15,107700.0,112200.0,105800.0,108100.0,...
```

This is the counterexample. It had a local 30D peak, but the 90D and 180D paths deteriorated badly. In C20, large-brand K-beauty label alone should be treated as a signboard, not a cash-flow bridge.

## 6. Score-return alignment

| bucket | observation | scoring implication |
|---|---|---|
| distributor/reorder winner | 실리콘투 had huge 90/180D MFE with manageable early MAE | add positive shadow axis when distributor sell-through/reorder evidence is present |
| ODM/margin winner | 코스맥스 and 한국콜마 show that ODM names can work through different tempo: one fast, one slow | add ODM/customer-mix/OPM bridge, not just sector beta |
| brand-label false positive | 아모레퍼시픽 had 30D local MFE but severe 180D MAE | keep brand-label + price-only breakout capped at 4B unless revision and sell-through persist |

## 7. Current calibrated profile stress test

Current calibrated profile already has:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual errors found:

1. **C20-specific under-scoring of distribution/ODM conversion.**  
   Global rules can recognize that price and volume improved, but they do not tell whether a K-beauty/K-food channel is actually converting into repeat order, OPM, revision, or FCF. 실리콘투 and 한국콜마 show the missing positive axis.

2. **C20-specific over-scoring of brand-label rebounds.**  
   아모레퍼시픽 shows that a familiar brand plus local MFE can still be a 4B-only structure. Without a C20 cap, the model may confuse a signboard with a pipe.

3. **Tempo mismatch.**  
   한국콜마 shows the model should not discard slow early paths when the business bridge is margin/revision based; 코스맥스 shows the opposite risk, where a fast initial rerating needs peak-after-bridge MAE guard.

## 8. Machine-readable rows

### 8.1 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_BRIDGE_VS_BRAND_LABEL_FALSE_POSITIVE", "symbol": "257720", "name": "실리콘투", "market": "KOSDAQ", "entry_date": "2024-03-20", "entry_price": 10750, "trigger_type": "Stage3-Yellow", "mfe_30_pct": 44.19, "mae_30_pct": -9.77, "peak_30_date": "2024-05-02", "peak_30_price": 15500, "trough_30_date": "2024-03-20", "trough_30_price": 9700, "mfe_90_pct": 404.19, "mae_90_pct": -9.77, "peak_90_date": "2024-06-19", "peak_90_price": 54200, "trough_90_date": "2024-03-20", "trough_90_price": 9700, "mfe_180_pct": 404.19, "mae_180_pct": -9.77, "peak_180_date": "2024-06-19", "peak_180_price": 54200, "trough_180_date": "2024-03-20", "trough_180_price": 9700, "outcome_bucket": "positive", "current_profile_error": "underweights distributor sell-through/reorder bridge; treats part of move as price-only beta unless C20 bridge exists", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "price_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_BRIDGE_VS_BRAND_LABEL_FALSE_POSITIVE", "symbol": "192820", "name": "코스맥스", "market": "KOSPI", "entry_date": "2024-04-01", "entry_price": 130000, "trigger_type": "Stage3-Yellow", "mfe_30_pct": 32.46, "mae_30_pct": -7.46, "peak_30_date": "2024-05-14", "peak_30_price": 172200, "trough_30_date": "2024-04-04", "trough_30_price": 120300, "mfe_90_pct": 60.0, "mae_90_pct": -7.46, "peak_90_date": "2024-06-14", "peak_90_price": 208000, "trough_90_date": "2024-04-04", "trough_90_price": 120300, "mfe_180_pct": 60.0, "mae_180_pct": -10.77, "peak_180_date": "2024-06-14", "peak_180_price": 208000, "trough_180_date": "2024-08-13", "trough_180_price": 116000, "outcome_bucket": "mixed_positive", "current_profile_error": "recognizes beauty recovery but lacks ODM/customer-mix/capacity bridge and later high-MAE guard", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "price_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_BRIDGE_VS_BRAND_LABEL_FALSE_POSITIVE", "symbol": "161890", "name": "한국콜마", "market": "KOSPI", "entry_date": "2024-04-01", "entry_price": 51500, "trigger_type": "Stage2-Actionable", "mfe_30_pct": 7.18, "mae_30_pct": -7.38, "peak_30_date": "2024-05-10", "peak_30_price": 55200, "trough_30_date": "2024-04-11", "trough_30_price": 47700, "mfe_90_pct": 45.63, "mae_90_pct": -7.38, "peak_90_date": "2024-06-19", "peak_90_price": 75000, "trough_90_date": "2024-04-11", "trough_90_price": 47700, "mfe_180_pct": 52.82, "mae_180_pct": -7.38, "peak_180_date": "2024-09-30", "peak_180_price": 78700, "trough_180_date": "2024-04-11", "trough_180_price": 47700, "outcome_bucket": "positive_slow_burn", "current_profile_error": "slow-burn ODM margin bridge would be left below Stage3 without C20-specific sell-through/revision axis", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "price_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_BRIDGE_VS_BRAND_LABEL_FALSE_POSITIVE", "symbol": "090430", "name": "아모레퍼시픽", "market": "KOSPI", "entry_date": "2024-04-30", "entry_price": 169500, "trigger_type": "4B", "mfe_30_pct": 18.29, "mae_30_pct": -4.78, "peak_30_date": "2024-05-31", "peak_30_price": 200500, "trough_30_date": "2024-05-07", "trough_30_price": 161400, "mfe_90_pct": 18.29, "mae_90_pct": -13.92, "peak_90_date": "2024-05-31", "peak_90_price": 200500, "trough_90_date": "2024-07-04", "trough_90_price": 145900, "mfe_180_pct": 18.29, "mae_180_pct": -37.58, "peak_180_date": "2024-05-31", "peak_180_price": 200500, "trough_180_date": "2024-11-15", "trough_180_price": 105800, "outcome_bucket": "counterexample", "current_profile_error": "large-brand K-beauty label and local price breakout can look actionable but lacks reorder/OPM/revision persistence; should remain 4B not Stage3", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "price_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv"}
```

### 8.2 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "symbol": "257720", "current_proxy_stage": "Stage2-Actionable", "current_proxy_total": 78.5, "proposed_shadow_total": 84.0, "raw_component_score_breakdown": {"price_volume_path": 23.5, "sector_fit": 14.0, "evidence_breadth": 12.0, "revision_proxy": 15.0, "distribution_reorder_bridge": 16.0, "risk_penalty": -4.0}, "alignment": "positive MFE confirms that C20 distributor reorder bridge deserves a separate positive axis"}
{"row_type": "score_simulation", "symbol": "192820", "current_proxy_stage": "Stage2-Actionable", "current_proxy_total": 77.0, "proposed_shadow_total": 80.0, "raw_component_score_breakdown": {"price_volume_path": 19.0, "sector_fit": 14.0, "evidence_breadth": 12.0, "revision_proxy": 16.0, "ODM_customer_mix_bridge": 14.0, "risk_penalty": -5.0}, "alignment": "positive first leg but high later MAE requires peak-after-bridge guard"}
{"row_type": "score_simulation", "symbol": "161890", "current_proxy_stage": "Stage2", "current_proxy_total": 72.0, "proposed_shadow_total": 76.5, "raw_component_score_breakdown": {"price_volume_path": 14.0, "sector_fit": 14.0, "evidence_breadth": 11.0, "revision_proxy": 15.5, "ODM_margin_bridge": 15.0, "risk_penalty": -3.0}, "alignment": "slow early path but strong 90/180D MFE; C20 slow-burn ODM bridge should not be under-scored"}
{"row_type": "score_simulation", "symbol": "090430", "current_proxy_stage": "4B", "current_proxy_total": 74.0, "proposed_shadow_total": 67.0, "raw_component_score_breakdown": {"price_volume_path": 14.0, "sector_fit": 13.0, "evidence_breadth": 9.0, "revision_proxy": 8.0, "brand_label_bridge": 5.0, "risk_penalty": -18.0}, "alignment": "counterexample; local MFE exists but 180D MAE dominates; brand-label false positive must be capped"}
```

### 8.3 Aggregate row JSONL

```jsonl
{"row_type": "aggregate", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_count": 4, "trigger_count": 4, "positive_case_count": 2, "mixed_positive_count": 1, "counterexample_count": 1, "local_4b_watch_count": 1, "avg_mfe_30_pct": 25.53, "avg_mae_30_pct": -7.35, "avg_mfe_90_pct": 132.03, "avg_mae_90_pct": -9.63, "avg_mfe_180_pct": 133.82, "avg_mae_180_pct": -16.38, "coverage_gap_static_index_before": 6, "coverage_gap_static_index_after_if_accepted": 10, "need_to_30_after_if_accepted": 20}
```

### 8.4 Shadow weight rows JSONL

```jsonl
{"row_type": "shadow_weight", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "rule_id": "C20_sellthrough_reorder_OPM_revision_bridge_required", "direction": "positive_gate", "proposal": "+1.5 to +2.5 only when distributor/ODM/channel evidence links sell-through or reorder to OPM/revision", "production_scoring_changed": false}
{"row_type": "shadow_weight", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "rule_id": "C20_brand_label_price_only_4B_cap", "direction": "guardrail", "proposal": "cap at 4B when only K-beauty/K-food brand-label + price breakout exists without reorder/revision margin bridge", "production_scoring_changed": false}
```

### 8.5 Residual contribution rows JSONL

```jsonl
{"row_type": "residual_contribution", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "contribution": "distinguishes distributor/ODM repeat-demand winners from brand-label false positives", "new_axis_proposed": ["C20_sellthrough_reorder_OPM_revision_bridge_required", "C20_brand_label_price_only_4B_cap", "C20_post_peak_high_MAE_distribution_guard"], "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "high_MAE_guardrail"], "existing_axis_weakened": []}
```

### 8.6 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","message":"C20 should split distributor/ODM repeat-demand bridges from brand-label local price moves. The pipe, not the signboard, is the scoring object."}
```

## 9. Proposed shadow rules

### Rule A — C20 sell-through / reorder / OPM / revision bridge required

```text
rule_id = C20_sellthrough_reorder_OPM_revision_bridge_required
applies_to = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
direction = positive_gate
shadow_only = true

IF:
  global channel / export / distribution / ODM evidence exists
  AND evidence connects to sell-through, reorder, OPM, revision, or FCF
  AND price path is not only a one-day/local 4B blowoff
THEN:
  allow Stage2-Actionable → Stage3-Yellow bridge
  consider +1.5 to +2.5 sector-specific shadow score
ELSE:
  do not upgrade on K-beauty/K-food label alone
```

### Rule B — C20 brand-label price-only 4B cap

```text
rule_id = C20_brand_label_price_only_4B_cap
applies_to = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
direction = guardrail
shadow_only = true

IF:
  evidence is mainly brand label / K-beauty / K-food headline
  AND no sell-through/reorder/OPM/revision bridge is identified
  AND price already has local 4B-like expansion
THEN:
  cap trigger at 4B or Stage2 watch
  block Stage3-Yellow/Green
```

### Rule C — C20 post-peak high-MAE guard

```text
rule_id = C20_post_peak_high_MAE_distribution_guard
applies_to = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
direction = risk_guard
shadow_only = true

IF:
  30D MFE is positive
  BUT 90D/180D MAE expands faster than business-evidence confirmation
THEN:
  classify as local_4b_watch or mixed_positive
  require renewed non-price evidence before re-upgrade
```

## 10. Residual contribution summary

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 2
mixed_positive_count = 1
counterexample_count = 1
local_4b_watch_count = 1
current_profile_error_count = 4
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
auto_selected_coverage_gap_static_index = C20 rows 6 → 10 if accepted; still Priority 0, need 20 to 30
```

```text
new_axis_proposed =
  C20_sellthrough_reorder_OPM_revision_bridge_required
  C20_brand_label_price_only_4B_cap
  C20_post_peak_high_MAE_distribution_guard

existing_axis_strengthened =
  stage2_required_bridge
  price_only_blowoff_blocks_positive_stage
  full_4b_requires_non_price_evidence
  local_4b_watch_guard
  high_MAE_guardrail

existing_axis_weakened = null
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent. Do not execute this handoff unless explicitly instructed in a later coding session.

Task:
Batch-ingest this MD as one v12 residual calibration artifact.

Research artifact:
e2r_stock_web_v12_residual_round_R5_loop_114_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md

Scope:
- Do not change production scoring immediately.
- Parse machine-readable JSONL blocks.
- Add trigger rows to v12 calibration staging only.
- Register canonical_archetype_id=C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.
- Preserve source_proxy_only/evidence_url_pending flags.
- Treat shadow rules as candidates:
  1. C20_sellthrough_reorder_OPM_revision_bridge_required
  2. C20_brand_label_price_only_4B_cap
  3. C20_post_peak_high_MAE_distribution_guard
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Do not convert these rules to production weights without aggregate review across more C20 rows.
```
