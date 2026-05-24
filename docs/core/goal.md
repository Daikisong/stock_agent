You are Codex working inside:

https://github.com/Songdaiki/stock_agent

Repository local path:
 /home/eorb915/projects/stock_agent

Primary MD input root:
 /home/eorb915/projects/stock_agent/docs/round

GOAL:
Ingest all E2R Stock-Web historical calibration result Markdown files, deduplicate repeated loops, aggregate evidence→return calibration results, and APPLY the validated cumulative calibration to stock_agent's default E2R scoring/stage logic.

This is no longer a shadow-only archive task.

The historical MDs were generated with:
- production_scoring_changed=false
- shadow_weight_only=true

That was correct for the research phase.

But this implementation phase is explicitly authorized to promote validated cumulative calibration into the default stock_agent scoring configuration.

Explicit authorization:
apply_calibrated_profile_to_default = true
production_default_scoring_patch_allowed = true
production_default_scoring_changed_expected = true
auto_trading_allowed = false
brokerage_api_allowed = false
current_stock_scan_allowed = false

Important:
"production" here means stock_agent's default E2R scoring/stage classification logic.
It does NOT mean brokerage order execution.
Do NOT implement auto-trading.
Do NOT connect to Kiwoom/KIS/broker APIs.
Do NOT generate live buy/sell recommendations.
Do NOT scan current stocks.

The goal is:
1. Parse all historical calibration MDs.
2. Exclude prompt/spec files.
3. Validate machine-readable rows and Markdown table rows.
4. Deduplicate repeated loop rematerializations.
5. Aggregate valid evidence→return outcomes.
6. Derive calibrated scoring/gate changes from the deduped cumulative ledger.
7. Apply validated changes to the default E2R scoring/stage profile.
8. Preserve the old baseline profile for rollback and comparison.
9. Add tests proving default scoring intentionally changed and baseline is still available.
10. Produce reports explaining what changed and why.

Do not stop at shadow_profile_current.json.
That is insufficient.
The final default E2R scoring config must be patched unless validation/coverage fails.

If validation is too weak to promote any axis, fail loudly and explain:
- which axis lacked evidence
- which rows were rejected
- what minimum evidence is missing

Do not silently leave everything shadow-only.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0. Critical distinction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The v11 prompt/spec file is NOT an ingest target.
Do NOT ingest prompt/spec files as calibration evidence.

Exclude files whose names or titles contain:
- prompt
- 프롬프트
- calibration_prompt
- historical_calibration_prompt
- 최종프롬프트
- E2R Historical Calibration Prompt
- E2R Post-OHLC Breakthrough Historical Calibration Prompt
- 단일 프롬프트 시작

Ingest only generated research result MDs matching:
- e2r_stock_web_historical_calibration_round_R*_loop_*_research*.md
- e2r_stock_web_historical_calibration_round_*_loop_*_*.md
- *stock_web_historical_calibration_round_R*_loop_*.md

Expected input count:
around 107 generated result MD files across R1~R13.

Primary input folder:
 /home/eorb915/projects/stock_agent/docs/round

Search this folder recursively first.
Only search the rest of the repository if this folder has fewer than 100 generated result MDs.
Do not ask where the files are.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Full coverage hard gate
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before promotion:
- discovered_result_md_count must be >= 100 unless the report explains the exact missing count.
- rounds_covered must include R1 through R13.
- every accepted MD must have a registry row.
- every registry row must include:
  file_path
  sha256
  round
  loop
  sector
  extraction_status
  parsed_trigger_row_count
  rejected_row_count
- every prompt/spec file must be listed separately with exclusion_reason=prompt_spec_file_excluded.
- failed_document_count and metadata_only_document_count must be reported.

If discovered_result_md_count < 100, or if any of R1~R13 is missing:
- do NOT promote calibrated scoring.
- stop after ingest/validation.
- write reports/e2r_calibration/coverage_failure_report.md.
- final output must set:
  production_default_scoring_changed=false
  promotion_status=blocked_by_coverage_failure

Do not partially read a few MDs and pretend the full calibration was applied.
This task requires full-folder ingest coverage.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. Required phase model
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run these phases in order:

PHASE A — ingest
- discover MD files
- exclude prompt/spec files
- build md registry with sha256
- parse JSONL rows and Markdown tables

PHASE B — validate
- validate price source, price basis, MFE/MAE, forward window, evidence type
- reject invalid rows with explicit reasons

PHASE C — dedupe
- repeated loops are lab-notebook revisions, not independent samples
- keep raw extracted rows
- select aggregate representatives

PHASE D — aggregate
- aggregate valid representative rows by round, sector, archetype, trigger type, evidence family
- compute score-return alignment and before/after effects

PHASE E — promote
- convert validated aggregate results into calibrated scoring/gate changes
- apply accepted changes to the default E2R scoring/stage profile
- preserve old baseline profile

PHASE F — test/report
- tests must verify default scoring changed intentionally when promotion passes
- tests must verify baseline rollback/comparison still exists
- reports must explain changed axes, evidence, sample counts, and guardrails

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. Input MD semantics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated MDs were historical calibration outputs using:

price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year

They are not live recommendations.
They are historical trigger-level calibration experiments.

They often contain:
- metadata
- price_source_validation rows
- case rows
- trigger rows
- score_simulation rows
- profile_comparison rows
- shadow_weight rows
- optimization_decision rows
- aggregate_metric rows
- narrative_only rows
- Markdown tables if JSONL is incomplete

Parser priority:
1. exact JSONL row_type rows
2. Markdown tables with recognizable headers
3. conservative metadata/prose fallback only for document registry

Do not hallucinate missing fields.
If required numeric fields are missing or unparseable, reject that row for promotion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. Parse row types
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Inspect the existing repo structure first.
Use the repo's existing conventions where possible.

If no calibration package exists, create:

src/e2r/calibration/
  __init__.py
  md_discovery.py
  md_parser.py
  validation.py
  dedupe.py
  aggregate.py
  promotion.py
  scoring_profile.py
  cli.py

Create/update data outputs:

data/e2r/calibration/
  md_registry.jsonl
  price_source_validations.jsonl
  extracted_cases.jsonl
  extracted_triggers_raw.jsonl
  trigger_rows_validated.jsonl
  trigger_rows_representative.jsonl
  score_simulation_rows.jsonl
  profile_comparison_rows.jsonl
  shadow_weight_events.jsonl
  optimization_decisions.jsonl
  aggregate_metric_rows.jsonl
  narrative_only_rows.jsonl
  rejected_rows.jsonl
  dedupe_map.jsonl
  shadow_weight_aggregate.json
  calibrated_weight_aggregate.json
  applied_weight_changes.json
  rejected_promotion_candidates.json

Recognize row types:
- price_source_validation
- case
- trigger
- score_simulation
- profile_comparison
- shadow_weight
- optimization_decision
- aggregate_metric
- narrative_only

Normalize columns:
- MFE90, MFE_90D, MFE_90D_pct -> MFE_90D_pct
- MAE90, MAE_90D, MAE_90D_pct -> MAE_90D_pct
- MFE180, MFE_180D, MFE_180D_pct -> MFE_180D_pct
- MAE180, MAE_180D, MAE_180D_pct -> MAE_180D_pct
- type, trigger_type -> trigger_type
- entry, entry_date @ price -> entry_date and entry_price
- price, entry_price -> entry_price
- outcome, trigger_outcome_label -> trigger_outcome_label
- dedupe, dedupe_for_aggregate -> dedupe_for_aggregate
- agg_role, aggregate_role, group_role -> aggregate_group_role

Preserve:
- source_file
- source_sha256
- source_line_range if easy
- raw_source_snippet for audit

Parsing must tolerate:
- Korean names
- comma thousands separators
- percentage symbols
- unavailable
- n/a
- not_applicable
- None
- null
- unavailable_not_needed_for_delta
- insufficient_forward_window_in_stock_web

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. Validation rules
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A row is price_path_valid if:
- price_source or price_data_source is Songdaiki/stock-web
- price_basis is tradable_raw
- price_adjustment_status is raw_unadjusted_marcap
- entry_date exists
- entry_price > 0
- MFE_30D_pct, MFE_90D_pct, MFE_180D_pct are numeric
- MAE_30D_pct, MAE_90D_pct, MAE_180D_pct are numeric
- forward_window_trading_days >= 180 if field exists
- no 180D corporate-action contamination is indicated

A row is usable_for_weight_calibration if:
- price_path_valid
- calibration_usable=true or inferred true from complete 30/90/180D MFE/MAE
- aggregate_group_role=representative
- dedupe_for_aggregate=true or inferred true for representative rows
- trigger_type in Stage2, Stage2-Actionable, Stage3-Yellow, Stage3-Green
- evidence source is non-price public evidence
- not narrative_only
- not label_comparison_only
- not 4B_overlay_only
- not 4C_overlay_only
- not price_only_no_evidence_run
- not false_positive_score unless used for negative guardrail
- not blocked_by_corporate_action

Positive stage promotion rows:
- Stage2
- Stage2-Actionable
- Stage3-Yellow
- Stage3-Green
- non-price evidence
- no false_positive_score
- clean 180D MFE/MAE

4B rows:
- may calibrate overheat/risk overlays
- must not train positive Stage2/Stage3 entry weights

4C rows:
- may calibrate thesis-break/protection logic
- must not train positive entry weights

Rejected reasons must be recorded:
- duplicate_content
- duplicate_loop_same_case
- label_comparison_only
- narrative_only
- price_only_no_evidence
- missing_required_mfe_mae
- insufficient_forward_window
- corporate_action_contaminated
- raw_all_basis
- 4b_overlay_only_not_entry
- 4c_overlay_only_not_entry
- false_positive_not_positive_promotion
- unparseable_numeric
- no_non_price_evidence
- not_representative_for_aggregate
- prompt_spec_file_excluded

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. Deduplication rules
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Do NOT count repeated loops as fresh independent evidence.

Document dedupe:
- exact sha256 duplicate -> keep one parsed copy, record duplicates

Primary trigger dedupe:
- same_entry_group_id if present

Fallback trigger dedupe:
- round
- sector_slug
- symbol
- primary_archetype
- trigger_type
- trigger_date
- entry_date
- rounded entry_price
- normalized company_name

Case dedupe fallback:
- round
- symbol
- primary_archetype
- canonical trigger family

When duplicate rows exist:
- keep all raw extracted rows
- select one aggregate representative
- prefer latest loop if it has richer v11 fields
- prefer exact JSONL over table parse
- prefer explicit same_entry_group_id
- prefer explicit dedupe_for_aggregate=true
- prefer row with more complete MFE/MAE/component fields
- record superseded_by_trigger_id and duplicate_reason

Repeated loop files can improve extraction confidence, but not independent sample count.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. Aggregation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Build aggregates from deduped representative rows.

Aggregate by:
- global
- round R1~R13
- sector
- sector_slug
- primary_archetype
- trigger_type
- evidence family
- case_type
- outcome label

For positive entry rows compute:
- count
- unique_case_count
- unique_symbol_count
- avg_MFE_30D_pct
- avg_MFE_90D_pct
- avg_MFE_180D_pct
- median_MFE_90D_pct
- median_MFE_180D_pct
- avg_MAE_30D_pct
- avg_MAE_90D_pct
- avg_MAE_180D_pct
- median_MAE_90D_pct
- median_MAE_180D_pct
- hit_rate_MFE90_ge_20
- hit_rate_MFE180_ge_30
- drawdown_risk_rate_MAE90_le_minus_20
- drawdown_risk_rate_MAE180_le_minus_30
- positive_asymmetry_score
- green_lateness_ratio where available
- Stage2 vs Stage3-Green paired comparison
- Stage2-Actionable vs Stage3-Green paired comparison
- Stage3-Yellow vs Stage3-Green paired comparison

For 4B:
- local_peak_proximity average
- full_window_peak_proximity average
- price_only_4B count
- non_price_4B count
- good_4B_timing rate
- too_early_4B rate
- post_4B_MAE/MFE

For 4C:
- thesis_break evidence count
- late_4C count
- useful_protection rate
- post_trigger_MAE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8. Promotion policy — apply to default scoring
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is the key difference from shadow-only ingest.

Create a calibrated profile from aggregate results:

profile_id = e2r_2_1_stock_web_calibrated
profile_basis = deduped_stock_web_historical_calibration_md
profile_status = default_enabled
previous_default_profile = e2r_2_0_baseline or current existing default

Promotion rules:

A. Apply to default scoring if:
- unique_case_count >= 4
- unique_round_count >= 2 OR sector-specific rule with strong same-sector evidence
- before/after profile improvement is present
- avg MFE improves or missed-structural count falls
- MAE does not worsen beyond guardrail
- false_positive rate does not rise materially
- evidence is non-price
- not driven by duplicate loops
- at least one counterexample or guardrail case considered

B. Apply sector-specific default scoring if:
- evidence is strong but concentrated in one round/sector
- unique_case_count >= 3
- logic should not become global

C. Keep as shadow-only if:
- unique_case_count < 3
- one-off case
- narrative-only
- unclear evidence source
- only price action
- 4B/4C overlay not relevant to entry
- missing before/after effect

D. Negative guardrails can be promoted if:
- repeated false-positive evidence exists
- price-only/no-evidence blowoff is identified
- Stage3-Green false confirmation has poor MFE/MAE
- 4B local/full split improves risk labeling

Promotion targets may include:
- Stage2-Actionable gate
- Stage3-Yellow gate
- Stage3-Green confirmation threshold
- Green lateness penalty
- relative strength confirmation gate
- customer/capacity/order quality gate
- backlog/margin bridge requirement
- price-only blowoff rejection
- false Green valuation/crowding guard
- 4B non-price evidence requirement
- 4B local-vs-full classification
- 4C thesis-break guard
- high-MAE position-size/risk guard

Do not apply:
- one-off low-confidence axes
- narrative-only axes
- pure price-only positive axes
- 4B rows as positive entry score
- 4C rows as positive entry score

If no axis meets promotion threshold:
- do not fabricate changes
- set promotion_status=no_axis_met_promotion_threshold
- production_default_scoring_changed=false
- report exactly why no axis passed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. Files to create or update
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create data outputs:

data/e2r/calibration/
  md_registry.jsonl
  price_source_validations.jsonl
  extracted_cases.jsonl
  extracted_triggers_raw.jsonl
  trigger_rows_validated.jsonl
  trigger_rows_representative.jsonl
  score_simulation_rows.jsonl
  profile_comparison_rows.jsonl
  shadow_weight_events.jsonl
  optimization_decisions.jsonl
  aggregate_metric_rows.jsonl
  narrative_only_rows.jsonl
  rejected_rows.jsonl
  dedupe_map.jsonl
  shadow_weight_aggregate.json
  calibrated_weight_aggregate.json
  applied_weight_changes.json
  rejected_promotion_candidates.json

Create or update config:

configs/e2r_scoring_profile_baseline.yaml
configs/e2r_scoring_profile_calibrated.yaml
configs/e2r_scoring_profile_active.yaml

Required behavior:
- baseline file preserves previous/default scoring
- calibrated file contains applied calibrated weights/gates
- active file points to calibrated profile by default if promotion succeeds
- rollback path is documented

If existing repo has a different config layout, adapt to it, but preserve these logical artifacts.

Patch code so stock_agent default scoring uses the calibrated profile unless a config/env override selects baseline.

Possible env/config:
E2R_SCORING_PROFILE=calibrated
E2R_SCORING_PROFILE=baseline

Default after successful promotion:
calibrated

Add optional comparison output:
- default_calibrated_stage
- baseline_stage
- calibration_adjustments
- historical_support_summary

Do not require internet at runtime.
Do not require stock-web at runtime.
Do not require original MD folder after ingest.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
10. Runtime scoring changes expected
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Expected practical changes:

1. Stage2 evidence is no longer underweighted when historical calibration supports early promotion.
2. Stage2-Actionable becomes a real default stage/tier if not already supported.
3. Stage3-Yellow can be selected before Green when evidence stack is strong but one gate remains.
4. Stage3-Green threshold becomes stricter against late/false Green.
5. Green lateness is explicitly penalized in sectors/archetypes where repeated.
6. Price-only blowoff cannot promote positive Stage2/Stage3.
7. 4B requires non-price evidence for full 4B unless explicitly marked price-only local watch.
8. 4B local peak and full-window peak are split.
9. 4C is thesis-break/protection only, not entry scoring.
10. High-MAE archetypes get position-size/risk guard output rather than clean promotion.

If current code lacks Stage2-Actionable or Stage3-Yellow enum support:
- add them carefully
- maintain backward compatibility
- add tests

If adding new enum values is too invasive:
- map them as sublabels/overlays while preserving existing Stage enum
- document this compromise in reports

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
11. Tests
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Add tests proving:

1. Prompt/spec files are excluded.
2. Generated MD files are discovered.
3. Full coverage hard gate works.
4. Parser extracts price_source_validation.
5. Parser extracts trigger rows from JSONL and Markdown tables.
6. Six-digit symbols are preserved.
7. MFE/MAE parser handles unavailable, n/a, None, not_applicable.
8. Repeated loop rows dedupe into one representative.
9. Stage2/Stage2-Actionable positive rows can contribute to default calibrated profile.
10. label_comparison_only cannot contribute to aggregate.
11. narrative_only cannot change scoring.
12. price-only blowoff cannot promote Stage2/Stage3.
13. 4B rows do not train positive entry score.
14. 4C rows do not train positive entry score.
15. corporate-action contaminated rows are rejected.
16. missing 180D rows are rejected.
17. false positive Green rows increase guardrail, not positive score.
18. calibrated profile differs from baseline when promotion succeeds.
19. active/default profile is calibrated after successful promotion.
20. baseline profile remains loadable by override.
21. calibrated profile loads without internet.
22. existing default-stage calls still run.
23. tests prove production/default scoring changed intentionally if promotion_status=applied.
24. tests prove production/default scoring stays unchanged if coverage or validation fails.
25. JSONL outputs are valid.
26. no NaN/Infinity in outputs.
27. compileall passes.

Run:
PYTHONPATH=src python -m pytest
PYTHONPATH=src python -m compileall -q src tests

Also run the repository's standard checks if pyproject/tox/nox exists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
12. Reports
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create:

reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/dedupe_report.md
reports/e2r_calibration/validation_report.md
reports/e2r_calibration/calibrated_profile_report.md
reports/e2r_calibration/applied_scoring_diff.md
reports/e2r_calibration/rejected_promotion_candidates.md
reports/e2r_calibration/coverage_failure_report.md if needed
reports/e2r_calibration/by_round/R1.md ... R13.md

ingest_summary.md must include:
- md_input_root
- discovered_md_count
- discovered_result_md_count
- excluded_prompt_spec_count
- unique_document_count
- duplicate_document_count
- parsed_document_count
- failed_document_count
- metadata_only_document_count
- raw_trigger_rows
- validated_trigger_rows
- aggregate_representative_trigger_rows
- rejected_rows_by_reason
- rounds covered
- loops covered
- sectors covered
- price_source_validation_summary

dedupe_report.md must explain:
- why repeated loops are not independent samples
- top repeated case families
- representative selection rules
- duplicate loop counts
- same_entry_group_id usage
- fallback dedupe keys

applied_scoring_diff.md must include:
- old baseline axis
- new calibrated axis
- delta
- scope
- confidence
- supporting cases
- rejected counterexamples
- reason
- test coverage

calibrated_profile_report.md must include:
- default profile now active if promotion succeeds
- baseline rollback method
- top applied Stage2/Stage2-Actionable changes
- Stage3-Green lateness changes
- 4B/4C guardrails
- false positive guards
- no auto-trading statement

by_round/R*.md must include:
- round-specific accepted axes
- rejected axes
- unique cases
- representative triggers
- sector profile recommendation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
13. Hard guardrails
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A. Do not apply the last MD directly.
Apply deduped cumulative aggregate.

B. Do not count repeated loop rematerializations as independent evidence.

C. calibration_usable=true is not enough.
Positive weighting requires representative, non-price, clean 180D, MFE/MAE rows.

D. 4B and 4C rows must not train positive entry weights.

E. Price-only blowoff rows must become rejection/guardrail logic, not positive promotion.

F. Default scoring should change in this task, but only through the validated calibrated aggregate.

G. Brokerage/API/auto-trading must not be touched.

H. The final system must allow rollback to baseline.

I. Do not leave production/default scoring unchanged silently.
If validation or coverage fails, explicitly report why promotion was blocked.
If validation passes and promotion axes exist, production_default_scoring_changed must be true.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
14. Implementation order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Inspect repo structure.
2. Search /home/eorb915/projects/stock_agent/docs/round recursively.
3. Exclude prompt/spec files.
4. Count generated result MD files.
5. Enforce full coverage hard gate.
6. Create parser tests against representative files from R1, R2, R3, R11.
7. Parse all MDs.
8. Build registry.
9. Validate rows.
10. Dedupe repeated loops.
11. Aggregate by round/archetype/trigger type/evidence family.
12. Derive calibrated profile.
13. Apply promotion if coverage and validation pass.
14. Preserve baseline profile and rollback.
15. Patch runtime config/profile loading.
16. Generate data outputs and reports.
17. Add tests.
18. Run tests and compile check.
19. Commit changes if this /goal environment allows committing; otherwise leave patch ready and report changed files.

Do not ask clarifying questions.
Make reasonable assumptions and record them in the report.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
15. Final output
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When done, respond exactly:

E2R_CALIBRATED_SCORING_PATCH_SUMMARY_BEGIN
repo:
md_input_root:
discovered_md_count:
discovered_result_md_count:
excluded_prompt_spec_count:
unique_document_count:
duplicate_document_count:
parsed_document_count:
failed_document_count:
metadata_only_document_count:
raw_trigger_rows:
validated_trigger_rows:
aggregate_representative_trigger_rows:
rejected_rows:
rounds_covered:
sectors_covered:
applied_scoring_axes_count:
shadow_only_axes_count:
rejected_promotion_axes_count:
baseline_profile_path:
calibrated_profile_path:
active_profile_path:
promotion_status:
production_default_scoring_changed: true/false
auto_trading_changed: false
brokerage_api_touched: false
tests:
compile_check:
E2R_CALIBRATED_SCORING_PATCH_SUMMARY_END

APPLIED_SCORING_AXES_BEGIN
axis|scope|old_value|new_value|delta|confidence|unique_case_count|unique_round_count|reason
...
APPLIED_SCORING_AXES_END

REJECTED_OR_SHADOW_ONLY_AXES_BEGIN
axis|scope|reason|needed_for_promotion
...
REJECTED_OR_SHADOW_ONLY_AXES_END

FILES_CHANGED_BEGIN
...
FILES_CHANGED_END

ROLLBACK_INSTRUCTIONS_BEGIN
How to switch back to baseline scoring:
...
ROLLBACK_INSTRUCTIONS_END

Do not include investment recommendation language.
Do not mention live trading.
Do not say production/default scoring is unchanged silently.
If unchanged, explain exact coverage/validation/promotion failure.