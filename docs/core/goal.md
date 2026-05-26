You are Codex working inside:

https://github.com/Songdaiki/stock_agent

Repository local path:
/home/eorb915/projects/stock_agent

Primary MD input root:
/home/eorb915/projects/stock_agent/docs/round

GOAL:
Run the accumulated E2R Stock-Web v12 residual research Markdown files through one command that validates the research, deduplicates it, builds stage-transition evidence, creates safe scope-limited patch specs, and applies those patches to the active E2R 2.2 rolling scoring profile.

This is a v12 residual-calibration task.
It is not a v11 global promotion task.

Current observed v12 batch:
- v12 result MD files in `docs/round`: 87
- large sectors represented: 10
- canonical archetypes represented: 27
- primary schema family: `v12_sector_archetype_residual`

The expected outcome is:
1. v12 files are discovered and parsed.
2. v12 trigger rows are validated with explicit rejection reasons.
3. repeated or duplicate rows are deduped without collapsing new symbols inside the same archetype.
4. stage transition summaries are regenerated.
5. sector/archetype rolling calibration ledgers are regenerated.
6. `e2r_2_2_candidate_profile.json` and `configs/e2r_scoring_profile_v2_2.yaml` are regenerated.
7. promotion readiness is reported with explicit apply/hold/block decisions.
8. the active default scoring profile becomes `e2r_2_2_rolling_calibrated` after run-v12-calibration.

Important:
Do promote safe v12 `apply_next_patch` specs to the active E2R 2.2 rolling profile in this task.
Do update `configs/e2r_scoring_profile_active.yaml` to `active_profile: e2r_2_2`.
Do NOT overwrite `configs/e2r_scoring_profile_calibrated.yaml`.
Do NOT delete `e2r_2_1_stock_web_calibrated`; keep it as rollback. The one-command default applies E2R 2.2 rolling calibration.
Do NOT implement auto-trading.
Do NOT connect to brokerage APIs.
Do NOT scan current/live stocks.
Do NOT fetch current market data.
Do NOT output buy/sell recommendation wording.

Production/default scoring change is authorized here, but only through safe scope-limited v12 patches:

```text
production_default_scoring_changed = true
active_default_profile_after_apply = e2r_2_2_rolling_calibrated
v12_rolling_ledger_generation_required = true
e2r_2_2_candidate_generation_required = true
explicit_default_promotion_authorized = true
```

Simple example:

```text
If a v12 file says C20 K-beauty needs a reorder/channel bridge,
do not globally lower every Stage2 or Stage3 threshold.
Instead, create/apply a C20 scoped rolling patch:
`canonical_archetype:C20...` gets a bounded bridge rule or small Stage2 bonus only when non-price evidence exists.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0. Critical distinction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The old v11 calibration prompt asked the agent to apply a validated global calibration into the default profile.

The current task is not another passive ledger-only task.

The current input files are v12 residual files. They may contain older wording such as:

```text
production_scoring_changed = false
shadow_weight_only = true
not production; post-calibrated residual
```

So the correct behavior is:

```text
v12 research MDs
-> ingest / validate / dedupe / aggregate
-> stage transition summary
-> apply / hold / block decision
-> safe patch specs
-> configs/e2r_scoring_profile_v2_2.yaml
-> configs/e2r_scoring_profile_active.yaml points to e2r_2_2
-> tests and reports
```

Do not treat raw v12 rows as direct production scoring instructions; only deduped, validated `apply_next_patch` specs can change scoring.

Example:

```text
Wrong:
  "C31 policy event bridge appeared in one loop, so patch Stage2 now."

Correct:
  "C31 policy event bridge becomes a scoped rolling patch only if validation says apply_next_patch.
   If evidence is weak, it becomes a bridge guard or hold/block decision instead."
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0A. When research becomes scoring
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Do not keep saying "collect more research" forever.

Do not wait for one giant final batch before scoring changes either.

The intended architecture is rolling micro-calibration:

```text
new non-overlapping research MDs arrive
-> source ledger is regenerated
-> archetype evidence state is updated
-> candidate score deltas are recomputed
-> safe small patches are proposed
-> accepted patches become the new calibrated state
-> later research can strengthen, weaken, cap, or roll back that state
```

This v12 task is an ingest/readiness task, but it must decide which scoring changes are ready for the next promotion patch and which existing candidate axes should move up/down as new positives and counterexamples arrive.

Simple example:

```text
Round A:
  C20 K-beauty has 3 positives and 2 counterexamples.
  It earns a bounded Stage2 bridge candidate.

Patch A:
  Add a small C20 Stage2 bridge only.
  Do not change Green.

Round B:
  More C20 research adds two inventory/channel-stuffing counterexamples.

Patch B:
  Do not remove all C20 logic.
  Keep the Stage2 bridge, but add a stronger inventory/receivable RedTeam guard.
```

So the system should behave like a calibration ledger, not a one-time thesis memo.

After the current v12 batch is ingested, every candidate axis must be classified as one of:

```text
apply_next_patch
hold_for_more_evidence
blocked_by_data_quality
blocked_by_logic_risk
```

The next engineering task after this ingest should not be "run more research" by default.
It should be:

```text
If any axis is apply_next_patch:
  implement a limited E2R 2.2 scoring patch for those axes only.

If no axis is apply_next_patch:
  fix the named blocker first, not blindly add more rounds.
```

This does not mean research stops.
It means research and patching run in parallel cadence:

```text
research cadence:
  keep adding non-overlapping sector/archetype cases.

calibration cadence:
  after each meaningful batch, recompute promotion decisions.

patch cadence:
  apply only the axes that clear the gate, in small reversible deltas.
```

Required rolling state files:

```text
data/e2r/calibration/v12/v12_archetype_evidence_state.json
data/e2r/calibration/v12/v12_promotion_decisions.jsonl
data/e2r/calibration/v12/v12_patch_specs.jsonl
reports/e2r_calibration/v12/rolling_calibration_state.md
reports/e2r_calibration/v12/apply_next_patch_plan.md
```

The evidence state must preserve:

```text
large_sector_id
canonical_archetype_id
unique_positive_symbols
unique_success_candidate_symbols
unique_counterexample_symbols
unique_4b_cases
unique_4c_cases
latest_positive_case_ids
latest_counterexample_case_ids
common_positive_evidence_fields
common_failure_evidence_fields
current_patch_state
last_patch_version
next_delta_recommendation
```

Patch specs must be small and reversible:

```text
patch_id
patch_type
scope
axis
old_value
new_value
max_delta
evidence_support_ids
counterexample_guard_ids
rollback_condition
```

Example patch spec:

```text
patch_id = e2r_2_2_C20_stage2_bridge_v1
patch_type = Stage2 bridge
scope = canonical_archetype:C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
axis = export_channel_reorder_stage2_bridge_bonus
old_value = 0.0
new_value = 1.0
max_delta = 1.0
rollback_condition = C20 false_positive_stage2_rate worsens or inventory counterexamples dominate
```

This is different from a one-shot global profile rewrite.

```text
Wrong:
  "We gathered 300 files. Rewrite all Stage thresholds."

Correct:
  "C20 clears a Stage2 bridge gate. Add +1.0 only for C20 bridge evidence.
   C14 battery overheat has counterexamples. Add a stricter Green guard.
   C03 defense is still under-covered. Hold."
```

Simple example:

```text
Bad loop:
  "C20 K-beauty has 87 more rows. Let's keep researching."

Correct loop:
  "C20 K-beauty has enough source-verified positives and counterexamples
   for a Stage2/Yellow bridge. Patch that bridge next.
   Do not wait for another 100 files."
```

Promotion is not all-or-nothing. Use three promotion types:

```text
Type 1. Safety guardrail promotion
Type 2. Stage2 / Stage3-Yellow observation promotion
Type 3. Stage3-Green conviction promotion
```

Type 1 safety guardrail promotion can move fastest.

Examples:

```text
price-only rally cannot create Green
full 4B requires non-price evidence
hard 4C thesis break routes to 4C
```

Minimum gate:

```text
independent_bad_case_count >= 3
counterexample_or_false_positive_rows >= 2
source_proxy_only_support_rows = 0, unless the rule is purely defensive
evidence_url_pending_support_rows = 0, unless the rule is purely defensive
no known unsafe side effect in validation rows
```

Reason:

```text
A defensive rule blocks bad promotions.
It does not create a new positive Stage3-Green candidate.
So it can be applied earlier than a positive scoring bonus.
```

Type 2 Stage2 / Stage3-Yellow observation promotion is allowed when an archetype has enough balanced evidence.

Examples:

```text
C20 K-beauty:
  export channel expansion + reorder evidence + OPM/EPS support
  may create a Stage2 bridge or Stage3-Yellow watch.

C22 insurance:
  reserve cycle + capital return + ROE/PBR support
  may create a financial Stage2 bridge.
```

Minimum gate:

```text
positive_independent_symbol_count >= 3
counterexample_independent_symbol_count >= 2
representative_trigger_rows >= 8
stage_transition_summary_rows >= 3
source_proxy_only_support_rate <= 0.25
evidence_url_pending_support_rate <= 0.25
bad_stage2_rate is not worse than current baseline
unsafe_green_count = 0
```

Allowed output:

```text
bounded Stage2/Stage3-Yellow bonus
archetype-specific bridge condition
report-facing sublabel or reason
```

Not allowed:

```text
lowering global Stage3-Green thresholds
turning one-off/theme rows into Green
stock-name-specific rule
```

Type 3 Stage3-Green conviction promotion is the strictest.

Minimum gate:

```text
positive_independent_symbol_count >= 5
counterexample_independent_symbol_count >= 3
full_stage_path_count >= 3
source_verified_support_rows >= 90%
evidence_url_pending_support_rate <= 0.10
source_proxy_only_support_rate <= 0.10
Stage3-Green false_positive_count = 0
one_off_or_theme_green_count = 0
RedTeam/Audit guard still blocks unsafe cases
```

Allowed output:

```text
sector/archetype-specific structural visibility gate
sector/archetype-specific score weights
Stage3-Green eligibility for that archetype only
```

Not allowed:

```text
global Green threshold loosening
case-library or benchmark-label leakage
future-data leakage
```

If an axis misses the gate, the report must say exactly why:

```text
not enough counterexamples
evidence_url_pending too high
source_proxy_only too high
stage transition missing
high MAE risk
false positive Green risk
logic conflicts with E2R philosophy
```

The promotion readiness report must include a table:

```text
axis|scope|decision|promotion_type|ready_for_next_patch|missing_to_promote|recommended_next_action
```

Examples:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|Stage2 bridge|apply_next_patch|Type2|true|none|implement bounded archetype bridge
C03_BATTERY_MATERIALS_CAPEX_OVERHEAT|Green bonus|blocked_by_logic_risk|Type3|false|unsafe Green risk|keep Green-restricted
C99_PRICE_ONLY_THEME|price-only Green block|apply_next_patch|Type1|true|none|implement defensive guardrail
```

No-more-research rule:

```text
If v12_result_md_count >= 80
and canonical_archetypes_covered >= 20
and any axis is apply_next_patch,
do not request more broad research before implementing the eligible patch.
```

This rule does not mean "stop researching".
It means "do not use more research as an excuse to avoid eligible micro-patches".

In this repository's current batch, that means the 87-file v12 batch must produce promotion decisions.
It is acceptable for many axes to remain blocked, but it is not acceptable to avoid the decision.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Input discovery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Search recursively under:

```text
docs/round
```

Include v12 result files matching:

```text
e2r_stock_web_v12_residual_round_*_loop_*_*_research*.md
*stock_web_v12_residual_round_*_research*.md
*v12_residual_round_*_research*.md
```

Keep v11 discovery support intact, but do not mix v11 and v12 flows.

Exclude prompt/spec files whose names or document titles contain:

```text
prompt
프롬프트
calibration_prompt
historical_calibration_prompt
최종프롬프트
E2R Historical Calibration Prompt
E2R Post-OHLC Breakthrough Historical Calibration Prompt
단일 프롬프트 시작
```

For every discovered v12 result MD, write a registry row with:

```text
file_path
filename
sha256
schema_family
round
loop
large_sector_id
canonical_archetype_id
fine_archetype_id
loop_objective
loop_contribution_label
extraction_status
parsed_trigger_row_count
rejected_row_count
```

Hard gate:
- If zero v12 result MDs are found, fail loudly.
- If v12 result MDs are found but no trigger rows are parsed, fail loudly.
- Do not silently fall back to v11.
- Do not require the old v11 `>=100 result MDs` coverage gate for v12.

Current batch expectation:

```text
v12_result_md_count should be around 87 for the current docs/round batch.
If the count differs, report the exact count and continue if files are valid.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. Required command
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run the v12 pipeline with:

```bash
PYTHONPATH=src python -m e2r.calibration.cli run-v12-calibration \
  --md-input-root docs/round \
  --data-directory data/e2r/calibration/v12 \
  --report-directory reports/e2r_calibration/v12
```

The command must:
1. discover v12 MDs
2. parse v12 MDs
3. validate v12 trigger rows
4. dedupe v12 trigger rows
5. aggregate v12 rows by sector and archetype
6. build stage transition summaries
7. build sector rolling calibration ledger
8. build archetype rolling calibration ledger
9. build `e2r_2_2_candidate_profile`
10. write reports
11. write `configs/e2r_scoring_profile_v2_2.yaml`
12. update active default profile to `e2r_2_2`

Expected summary fields:

```text
v12_result_md_count
v12_parsed_document_count
v12_failed_document_count
v12_raw_trigger_rows
v12_validated_trigger_rows
v12_representative_trigger_rows
v12_rejected_rows
large_sectors_covered
canonical_archetypes_covered
stage_transition_summary_rows
evidence_url_pending_count
source_proxy_only_count
default_promotion_ready
active_default_profile_preserved = false
production_default_scoring_changed = true
auto_trading_changed = false
brokerage_api_touched = false
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. V12 metadata and row semantics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

V12 files may contain metadata in fenced text blocks, bullet lines, JSONL rows, CSV fences, and Markdown tables.

Parse metadata fields when present:

```text
research_session
mode
round
loop
large_sector_id
canonical_archetype_id
fine_archetype_id
loop_objective
current_default_profile_proxy
previous_baseline_reference
new_independent_case_count
reused_case_count
new_symbol_count
same_archetype_new_symbol_count
same_archetype_new_trigger_family_count
positive_case_count
counterexample_count
4B_case_count
4C_case_count
current_profile_error_count
diversity_score_summary
loop_contribution_label
do_not_propose_new_weight_delta
auto_selected_coverage_gap
```

Recognize row types:

```text
price_source_validation
case
trigger
score_simulation
profile_comparison
shadow_weight
optimization_decision
aggregate_metric
narrative_only
residual_contribution
stage_transition_summary
coverage_matrix
sector_rule_candidate
canonical_archetype_rule_candidate
```

Parser priority:
1. exact JSONL row_type rows
2. CSV/TSV fenced tables
3. Markdown tables with recognizable headers
4. metadata fallback for registry/residual summary only

Do not hallucinate missing numeric fields.
If required fields are missing, reject the row for calibration and record why.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. Trigger and alias normalization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Normalize common aliases:

```text
Stage3-Green comparison -> Stage3-Green
Stage3-Green compare -> Stage3-Green
Stage3_Yellow -> Stage3-Yellow
Stage3_Green -> Stage3-Green
Stage4B local overlay -> Stage4B
Stage4B full-window overlay -> Stage4B
price-only-local-4B-overlay -> Stage4B
4B_false_positive_guardrail -> Stage4B
Stage4C protection watch -> Stage4C
Stage2 policy-only stress -> Stage2
Stage1/weak-watch -> Stage1
price-only-theme-breakout -> price_only_theme_breakout_guardrail
```

Important:
- `price-only-theme-breakout` is not a positive Stage2 signal.
- price-only 4B rows can support a watch/guardrail, not full evidence-based 4B.
- 4C rows are thesis-break/protection rows, not positive entry rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. Validation rules
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A row is price-path valid only if:

```text
price_source or price_data_source is Songdaiki/stock-web
price_basis is tradable_raw
price_adjustment_status is raw_unadjusted_marcap
entry_date exists
entry_price > 0
MFE_30D_pct / MFE_90D_pct / MFE_180D_pct are numeric
MAE_30D_pct / MAE_90D_pct / MAE_180D_pct are numeric
forward_window_trading_days >= 180 if present
no 180D corporate-action contamination is indicated
```

V12 shadow-calibration rows also require:

```text
large_sector_id
canonical_archetype_id
```

Set these flags:

```text
usable_for_global_promotion = false
usable_for_v12_shadow_calibration
usable_for_sector_shadow
usable_for_archetype_shadow
usable_for_new_weight_evidence
evidence_url_pending
source_proxy_only
residual_counterexample
current_profile_error
current_profile_false_positive
current_profile_missed_structural
current_profile_too_late
current_profile_4B_too_early
current_profile_4C_too_late
```

Rules:
- v12 rows are never usable for global default promotion in this task.
- missing `large_sector_id` rejects the row from v12 shadow calibration.
- missing `canonical_archetype_id` rejects the row from v12 shadow calibration.
- `do_not_count_as_new_case=true` excludes the row from new evidence weight.
- `independent_evidence_weight=0` excludes the row from new evidence weight.
- `duplicate_low_value_loop` excludes the row from new evidence weight.
- `schema_rematerialization_only` excludes the row from new evidence weight.
- 4B and 4C rows do not train positive entry weights.
- price-only rows do not train positive entry weights.
- `evidence_url_pending` and `source_proxy_only` can support shadow analysis but block default promotion.

Simple example:

```text
A Stage2 row with +80% MFE but evidence_source=price_only
is not a good positive Stage2 row.
It should become a guardrail example.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. V12 dedupe rules
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Do not collapse different symbols just because they share the same canonical archetype.

V12 is meant to add more symbols, counterexamples, trigger families, and 4B/4C paths to the same archetype.

Strict duplicate key:

```text
symbol
canonical_archetype_id
trigger_type
trigger_date
entry_date
rounded entry_price
evidence_family or trigger_family or fine_archetype_id
```

Rules:
- same symbol + same archetype + same trigger + same entry = duplicate
- same canonical archetype + new symbol = independent
- same symbol + new trigger family may be retained with reduced independent weight
- duplicate rows remain in raw outputs
- only representative rows feed aggregate metrics

Example:

```text
C20 + 실리콘투 Stage2 2023-05-16 repeated twice = duplicate
C20 + 실리콘투 Stage2 and C20 + 브이티 Stage2 = two independent rows
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. Aggregation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Aggregate by:

```text
global_v12
large_sector_id
canonical_archetype_id
large_sector_id + canonical_archetype_id
fine_archetype_id
loop_objective
current_profile_verdict
positive_or_counterexample
loop_contribution_label
```

Compute at least:

```text
row_count
unique_case_count
unique_symbol_count
unique_round_count
new_independent_case_count
reused_case_count
same_archetype_new_symbol_count
same_archetype_new_trigger_family_count
positive_case_count
counterexample_count
4B_case_count
4C_case_count
current_profile_error_count
source_proxy_only_count
evidence_url_pending_count
good_stage2_count
bad_stage2_count
stage2_high_mae_count
avg_stage2_MFE90
avg_stage2_MAE90
stage2_hit_rate_MFE90_ge_20
stage2_bad_entry_rate_MAE90_le_minus_20
good_4b_timing_count
too_early_4b_count
price_only_4b_count
non_price_4b_count
4c_success_count
4c_late_count
watch_only_4c_count
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8. Stage transition summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Build stage transition summaries by:

```text
case_id
symbol
large_sector_id
canonical_archetype_id
```

Select:

```text
best Stage2 / Stage2-Actionable
best Stage3-Yellow
best Stage3-Green
best Stage4B
best Stage4C
peak price/date inferred from MFE rows when explicit peak is unavailable
```

Compute:

```text
stage2_to_yellow_return_pct
stage2_to_green_return_pct
stage2_to_4b_return_pct
stage2_to_peak_return_pct
green_to_peak_remaining_upside_pct
green_upside_capture_pct
stage4b_peak_capture_pct
stage4b_to_90d_low_return_pct
peak_to_4c_drawdown_pct
transition_verdict
```

Important formula:

```text
stage4b_peak_capture_pct =
  (stage4b_price - stage2_price) / (peak_price - stage2_price) * 100
```

Example:

```text
Stage2 price = 1,000
peak price = 1,400
4B price = 1,350

Stage2 -> 4B return = +35%
4B peak capture = 87.5%
```

Do not confuse simple return with peak capture.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. Shadow profile generation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate:

```text
data/e2r/calibration/v12/sector_shadow_profile.json
data/e2r/calibration/v12/archetype_shadow_profile.json
data/e2r/calibration/v12/residual_error_ledger.jsonl
data/e2r/calibration/v12/v12_shadow_weight_candidates.jsonl
data/e2r/calibration/v12/e2r_2_2_candidate_profile.json
```

Candidate axes may include:

```text
stage2_bonus_candidate_delta
stage2_required_bridge
high_mae_guard_candidate
bad_stage2_guard_candidate
full_4b_overlay_candidate
local_4b_watch_guard
earlier_thesis_break_watch
hard_4c_confirmation
```

Promotion readiness must be conservative.

Default promotion is blocked if:

```text
evidence_url_pending_count > 0
source_proxy_only_count > 0
positive/counterexample balance is weak
stage transition coverage is insufficient
rows are mostly duplicate/rematerialized
explicit user approval is missing
```

The candidate profile must state:

```text
profile_status = candidate_not_active
production_default_scoring_changed = true
active_default_profile_after_apply = e2r_2_2_rolling_calibrated
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
10. Required outputs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Data outputs:

```text
data/e2r/calibration/v12/v12_md_registry.jsonl
data/e2r/calibration/v12/v12_extracted_cases.jsonl
data/e2r/calibration/v12/v12_extracted_triggers_raw.jsonl
data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl
data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl
data/e2r/calibration/v12/rejected_v12_rows.jsonl
data/e2r/calibration/v12/v12_dedupe_map.jsonl
data/e2r/calibration/v12/v12_aggregate_metrics.json
data/e2r/calibration/v12/stage_transition_summary.jsonl
data/e2r/calibration/v12/v12_residual_contribution_rows.jsonl
data/e2r/calibration/v12/v12_coverage_matrix_rows.jsonl
data/e2r/calibration/v12/sector_shadow_profile.json
data/e2r/calibration/v12/archetype_shadow_profile.json
data/e2r/calibration/v12/residual_error_ledger.jsonl
data/e2r/calibration/v12/v12_shadow_weight_candidates.jsonl
data/e2r/calibration/v12/e2r_2_2_candidate_profile.json
```

Reports:

```text
reports/e2r_calibration/v12/ingest_summary.md
reports/e2r_calibration/v12/coverage_matrix.md
reports/e2r_calibration/v12/sector_shadow_profile_report.md
reports/e2r_calibration/v12/archetype_shadow_profile_report.md
reports/e2r_calibration/v12/residual_error_report.md
reports/e2r_calibration/v12/stage_transition_report.md
reports/e2r_calibration/v12/evidence_url_pending_report.md
reports/e2r_calibration/v12/promotion_readiness_report.md
reports/e2r_calibration/v12/e2r_2_2_candidate_profile_report.md
reports/e2r_calibration/v12/by_archetype_stage_transition/*.md
```

Reports must clearly say:
- v12 is rolling calibration.
- `case_fixture` or historical research success is not proof of live discovery.
- default scoring changed only through scope-limited safe patches.
- exact evidence URL/source proxy limitations remain blockers if present.
- `e2r_2_1_stock_web_calibrated` remains rollback.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
11. Tests and verification
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

At minimum run:

```bash
PYTHONPATH=src python -m unittest tests.test_calibration_v12_pipeline -v
PYTHONPATH=src python -m unittest tests.test_calibration_pipeline -v
PYTHONPATH=src python -m pytest
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m compileall -q src tests
```

Also run:

```bash
git diff --check
```

Tests must cover:

```text
v12 file discovery
v12 metadata parsing
large sector / canonical archetype parsing
trigger alias normalization
same archetype + new symbol is not duplicate
same symbol + same entry is duplicate
evidence_url_pending blocks default promotion
source_proxy_only blocks default promotion
price-only row cannot train positive Stage2/Stage3
4B rows do not train positive entry weights
4C rows do not train positive entry weights
stage transition summary computes peak capture correctly
v12 calibration run updates active default profile to e2r_2_2
sector rolling ledger is generated
archetype rolling ledger is generated
e2r_2_2 rolling profile is generated and active after run-v12-calibration
```

Hard verification:

```text
active_default_profile_after_apply must be e2r_2_2_rolling_calibrated
production_default_scoring_changed must be true
auto_trading_changed must be false
brokerage_api_touched must be false
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
12. Hard guardrails
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A. Do not apply the latest v12 MD directly.
Use deduped aggregate evidence.

B. Do not count repeated loop rematerializations as independent evidence.

C. Do not treat same archetype/new symbol as duplicate.

D. Do not use case labels or benchmark labels as production candidate-generation input.

E. Do not train positive entry weights from 4B/4C rows.

F. Do not train positive entry weights from price-only rows.

G. Promote safe `e2r_2_2_candidate` patches to active default here.

H. Do not touch brokerage/API/auto-trading code.

I. Do not output investment recommendation wording.

J. Do not silently ignore validation failures.
Every rejection needs a reason.

K. Do not confuse simple return with peak-capture ratio.

Example:

```text
Stage2 -> 4B return and 4B peak capture are different metrics.
Both can be useful, but they answer different questions.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
13. Implementation order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Inspect repo structure.
2. Search `docs/round` recursively for v12 result MDs.
3. Exclude prompt/spec files.
4. Count v12 result MDs and report the count.
5. Parse all v12 MDs.
6. Build registry.
7. Validate rows.
8. Dedupe rows.
9. Aggregate rows.
10. Build stage transition summaries.
11. Build sector shadow profile.
12. Build archetype shadow profile.
13. Build `e2r_2_2_candidate_profile`.
14. Build `configs/e2r_scoring_profile_v2_2.yaml`.
15. Write data outputs and reports.
16. Confirm active profile was updated to e2r_2_2 and calibrated remains rollback.
17. Run tests and compile check.
18. Commit and push if this environment allows it.

Do not ask clarifying questions.
Make reasonable assumptions and record them in the reports.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
14. Final output
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When done, respond exactly:

```text
V12_FULL_INGEST_SHADOW_PROFILE_SUMMARY_BEGIN
repo:
md_input_root:
v12_result_md_count:
v12_parsed_document_count:
v12_failed_document_count:
v12_raw_trigger_rows:
v12_validated_trigger_rows:
v12_representative_trigger_rows:
v12_rejected_rows:
large_sectors_covered:
canonical_archetypes_covered:
stage_transition_summary_rows:
sector_shadow_profile_path:
archetype_shadow_profile_path:
residual_error_ledger_path:
e2r_2_2_candidate_profile_path:
promotion_readiness_report_path:
default_promotion_ready:
active_default_profile_after_apply: e2r_2_2_rolling_calibrated
production_default_scoring_changed: true
auto_trading_changed: false
brokerage_api_touched: false
tests:
compile_check:
V12_FULL_INGEST_SHADOW_PROFILE_SUMMARY_END

TOP_SECTOR_SHADOW_CANDIDATES_BEGIN
large_sector_id|axis|direction|confidence|positive_case_count|counterexample_count|reason
...
TOP_SECTOR_SHADOW_CANDIDATES_END

TOP_ARCHETYPE_SHADOW_CANDIDATES_BEGIN
canonical_archetype_id|axis|direction|confidence|positive_case_count|counterexample_count|reason
...
TOP_ARCHETYPE_SHADOW_CANDIDATES_END

PROMOTION_BLOCKERS_BEGIN
blocker|count|reason|needed_to_clear
...
PROMOTION_BLOCKERS_END

FILES_CHANGED_BEGIN
...
FILES_CHANGED_END
```

Do not include investment recommendation language.
Do not mention live trading as if it is enabled.
If default scoring remains unchanged, that is correct for this v12 task.
