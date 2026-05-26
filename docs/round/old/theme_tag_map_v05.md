# Theme Tag Map v0.5

`theme_tag_map_v05.csv` is the Round 18 normalized map for raw Korean market
themes.

It is not a production scoring file. It is a routing and audit file.

Example:

- `HBM` maps to the memory/HBM research route.
- The tag itself does not create score.
- Score still needs EPS/FCF revision, memory price evidence, capacity or supply discipline, and valuation rerating evidence.

Another example:

- `엠폭스` maps to an event-demand route.
- The tag is useful for RedTeam and one-off demand checks.
- It cannot create Stage 3-Green without recurring non-event demand.

## Files

- `data/sector_taxonomy/raw_theme_tags_v05.txt`
- `data/sector_taxonomy/raw_theme_tags_v05.csv`
- `data/sector_taxonomy/theme_tag_map_v05.csv`
- `data/sector_taxonomy/theme_aliases_v05.yml`
- `output/theme_tag_coverage_v05/theme_coverage_report.md`

## Current Audit

- total_raw_tags: 208
- mapped_tags: 208
- unmatched_tags: 0
- ambiguous_tags: 6

Ambiguous tags are kept for manual context review. For example, `화재` can mean
insurance, a disaster event, or EV fire depending context.

## Guardrails

- Theme tags are not score evidence.
- Theme tags are not production candidate labels.
- Red/event/speculative tags remain RedTeam-first unless actual EPS/FCF evidence exists.
