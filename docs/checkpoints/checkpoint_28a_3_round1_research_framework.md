# Checkpoint 28A-3: Round-1 Research Framework Alignment

## What Changed

This patch aligns the repo with the analyst Round-1 synthesis:

- Round-1 core frame: 25 archetypes
- Three blocks:
  - structural E2R candidates
  - cyclical/spread guardrailed
  - Red/Yellow guardrail
- Current detailed archetypes remain available as extensions.
- Extension archetypes roll up to a Round-1 core bucket for reporting.

No production scoring changed.

## Why Not Delete the Extra Archetypes?

Checkpoint 28A-2 had 35 enum values. Round-1 describes 25 core archetypes.

Deleting the extra 10 immediately would lose useful detail. Example:

```text
BIOTECH_ROYALTY_COMMERCIALIZATION
-> too specific for Round-1 core
-> still useful as a subcase detail
-> rolls up to BIOTECH_REGULATORY
```

So the repo now treats those 10 as extension/refinement archetypes.

## Generated Reports

- `output/e2r_research_framework/round1_framework_summary.md`
- `output/e2r_research_framework/round1_archetype_blocks.csv`
- `output/e2r_research_framework/round1_case_mapping.csv`
- `output/e2r_research_framework/round1_score_weight_draft.md`

## Current Numbers

The framework report records:

- round1_core_archetype_count: 25
- current_archetype_enum_count: 35
- extension_archetype_count: 10

This explains why the previous answer said 35: the code had extension
archetypes mixed into the canonical enum. The Round-1 layer now makes that
distinction explicit.

## Guardrails

- Score-weight draft is report-only.
- StageClassifier thresholds are unchanged.
- Case records are not production input.
- Later analyst rounds can refine the 25/extension split without breaking
  existing case data.
