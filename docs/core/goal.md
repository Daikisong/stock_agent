You are Codex working inside:

https://github.com/Songdaiki/stock_agent

Repository local path:
/home/eorb915/projects/stock_agent

Primary MD input root:
/home/eorb915/projects/stock_agent/docs/round

GOAL:
Ingest the accumulated E2R Stock-Web v12 residual research Markdown files, validate them, deduplicate them, build stage-transition summaries, and generate sector/archetype shadow profiles plus an `e2r_2_2_candidate` profile.

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
5. sector shadow profile and archetype shadow profile are regenerated.
6. `e2r_2_2_candidate_profile.json` is regenerated.
7. promotion readiness is reported.
8. the active default scoring profile remains `e2r_2_1_stock_web_calibrated`.

Important:
Do NOT promote v12 to the default active profile in this task.
Do NOT modify `configs/e2r_scoring_profile_active.yaml`.
Do NOT overwrite `configs/e2r_scoring_profile_calibrated.yaml`.
Do NOT demote or replace `e2r_2_1_stock_web_calibrated`.
Do NOT implement auto-trading.
Do NOT connect to brokerage APIs.
Do NOT scan current/live stocks.
Do NOT fetch current market data.
Do NOT output buy/sell recommendation wording.

Production/default scoring change is not authorized here:

```text
production_default_scoring_changed = false
active_default_profile_must_remain = e2r_2_1_stock_web_calibrated
v12_shadow_profile_generation_required = true
e2r_2_2_candidate_generation_required = true
explicit_default_promotion_authorized = false
```

Simple example:

```text
If a v12 file says C20 K-beauty needs a reorder/channel bridge,
do not immediately change live scoring.
Instead, store it as a C20 archetype shadow candidate,
count supporting positives and counterexamples,
and report whether it is ready for a future explicit promotion.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0. Critical distinction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The old v11 calibration prompt asked the agent to apply a validated global calibration into the default profile.

That is not the current task.

The current input files are v12 residual files. They repeatedly state:

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
-> sector_shadow_profile
-> archetype_shadow_profile
-> e2r_2_2_candidate_profile
-> promotion_readiness_report
-> active profile unchanged
```

Do not treat v12 files as direct production scoring instructions.

Example:

```text
Wrong:
  "C31 policy event bridge appeared in one loop, so patch Stage2 now."

Correct:
  "C31 policy event bridge becomes a canonical_archetype shadow candidate.
   It needs verified evidence URLs, enough positive/counterexample balance,
   and a separate explicit promotion task before default scoring changes."
```

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
PYTHONPATH=src python -m e2r.calibration.cli run-v12-full \
  --md-input-root docs/round \
  --data-directory data/e2r/calibration/v12 \
  --report-directory reports/e2r_calibration/v12 \
  --preserve-global-profile
```

The command must:
1. discover v12 MDs
2. parse v12 MDs
3. validate v12 trigger rows
4. dedupe v12 trigger rows
5. aggregate v12 rows by sector and archetype
6. build stage transition summaries
7. build sector shadow profile
8. build archetype shadow profile
9. build `e2r_2_2_candidate_profile`
10. write reports
11. verify the active default profile did not change

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
active_default_profile_preserved = true
production_default_scoring_changed = false
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
production_default_scoring_changed = false
active_default_profile_must_remain = e2r_2_1_stock_web_calibrated
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
- v12 is shadow-only.
- `case_fixture` or historical research success is not proof of live discovery.
- default scoring did not change.
- exact evidence URL/source proxy limitations remain blockers if present.
- future active promotion requires a separate explicit task.

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
v12 full run preserves active default profile
sector shadow profile is generated
archetype shadow profile is generated
e2r_2_2 candidate is generated but not active
```

Hard verification:

```text
active_default_profile_preserved must be true
production_default_scoring_changed must be false
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

G. Do not promote `e2r_2_2_candidate` to active default here.

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
14. Write data outputs and reports.
15. Confirm active profile was preserved.
16. Run tests and compile check.
17. Commit and push if this environment allows it.

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
active_default_profile_preserved: true
production_default_scoring_changed: false
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
