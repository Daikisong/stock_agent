# E2R Theme Tag Taxonomy Round 10

Round 10 separates three layers:

1. Large sector: broad folder for market coverage.
2. Sub-archetype/theme group: search and routing layer.
3. Canonical E2R archetype: owner of evidence interpretation and future scoring design.

Theme tags are not score inputs.

Easy example:

- `초전도체` is a theme tag.
- It maps to `SPECULATIVE_SCIENCE_THEME`.
- That maps to canonical `THEME_VALUATION_OVERHEAT`.
- The tag alone cannot create Stage 3-Green.

## Round 10 Structure

- large sectors: 12
- sub-archetypes: 65
- raw theme tags: written to `data/sector_taxonomy/theme_tag_map.csv`

## Guardrails

- Do not score from theme name alone.
- Do not lower Stage 3-Green thresholds.
- Do not use case or theme labels as candidate-generation evidence.
- Use theme tags for search query planning, taxonomy coverage, and case mining only.

## Output Files

- `data/sector_taxonomy/theme_tag_map.csv`
- `output/e2r_round10_theme_tag_taxonomy/round10_theme_taxonomy_summary.md`
- `output/e2r_round10_theme_tag_taxonomy/round10_large_sector_map.csv`
- `output/e2r_round10_theme_tag_taxonomy/round10_sub_archetype_map.csv`
- `output/e2r_round10_theme_tag_taxonomy/round10_posture_report.md`
- `output/e2r_round10_theme_tag_taxonomy/round10_case_record_candidate_plan.md`
