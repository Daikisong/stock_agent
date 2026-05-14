# Round 17 Theme Absorption Audit

Round 17 converts the v0.5 theme coverage discussion into an explicit audit.
The goal is not to change scoring. The goal is to answer a simpler question:

> Did the raw market theme tags land in a known E2R research bucket?

Current result:

- total_theme_tags: 151
- mapped_theme_tags: 151
- unmatched_theme_tags: 0
- large_sector_count: 12
- archetype_count: 73
- production_scoring_changed: false
- theme_tags_are_score_input: false
- scoring_ready: false

## How To Read It

Theme tags are routing labels. They decide where research should start, not
what score a company receives.

Example:

- `초전도체` maps to `SPECULATIVE_SCIENCE_THEME`.
- That means the system should run speculative-theme and RedTeam checks.
- It does not mean the company receives EPS/FCF, contract, or visibility score.

Another example:

- `전력설비` maps to `CONTRACT_BACKLOG_INDUSTRIAL`.
- That can lead to contract/backlog research.
- Stage 3 still needs actual contract quality, backlog, margin path, and revision evidence.

## Policy Buckets

Round 17 keeps the raw policy labels from the analyst note:

- `green_allowed`: Green may be possible after strict evidence checks.
- `watch_to_green`: start as Watch, promote only with strong evidence.
- `watch_only`: useful for monitoring or case mining, not enough by itself.
- `red_watch`: monitor with RedTeam-first posture.
- `event_watch`: event-driven research only.
- `event_only`: event tag, not structural evidence.
- `red_flag`: likely overheat, one-off, or speculative-risk route.

## Output Files

- `data/sector_taxonomy/theme_tag_map_v05.csv`
- `data/sector_taxonomy/theme_aliases_round17.yml`
- `output/e2r_round17_theme_absorption_audit/theme_coverage_report.md`
- `output/e2r_round17_theme_absorption_audit/round17_theme_coverage_audit.json`
- `output/e2r_round17_theme_absorption_audit/theme_coverage_matrix.csv`
- `output/e2r_round17_theme_absorption_audit/unmatched_theme_tags.csv`
- `output/e2r_round17_theme_absorption_audit/green_policy_distribution.csv`

## What This Does Not Prove

This audit proves structural absorption of the theme map. It does not prove
that each archetype's future score weight is correct.

Before production scoring changes, the next layer still needs:

- success/counterexample case coverage
- price-path validation
- MFE/MAE and 4B/4C lifecycle checks
- evidence-to-score alignment tests

## Guardrails

- Do not lower Stage 3-Green thresholds to improve theme coverage.
- Do not use theme names as score evidence.
- Do not use case or benchmark labels as candidate-generation input.
- Do not treat event, policy, or speculative science tags as structural E2R without EPS/FCF evidence.
