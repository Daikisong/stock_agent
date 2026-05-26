# E2R Case Library Runbook

The case library is the evidence base for future sector-aware score design.
It is not used by the production pipeline.

Think of it as a training notebook:

```text
계약/수주형 성공 사례 2개 이상
계약/수주형 반례 2개 이상
-> 그 다음에야 계약/수주형 점수비중을 신뢰할 수 있음
```

## Files

```text
data/e2r_case_library/cases.jsonl
src/e2r/sector/case_library.py
output/e2r_case_library/case_coverage_summary.md
output/e2r_case_library/archetype_case_matrix.csv
output/e2r_case_library/recommended_score_weights.md
```

## Case Record

Each case stores:

- identity: `case_id`, `symbol`, `company_name`, `market`
- taxonomy: `sector_raw`, `primary_archetype`
- outcome group: `structural_success`, `cyclical_success`, `one_off`, `boom_bust`, `overheat`, `failed_rerating`
- lifecycle dates: Stage 1/2/3/4A/4B/4C and peak date when known
- evidence summary and key fields
- price path metrics when available
- data quality flags

Missing price/path values stay null. They are not filled by guesswork.

## Coverage Rule

An archetype is considered covered only when it has:

- at least 2 positive cases
- at least 2 counterexamples

If not, the report marks:

```text
insufficient_case_coverage
```

That means score weights should not be finalized for that archetype yet.

## Dry-Run Mining

```bash
PYTHONPATH=src python -m e2r.cli.mine_e2r_sector_cases \
  --market KR \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --dry-run
```

Dry-run writes planned searches only. It does not fetch pages and does not
create evidence.

## Guardrails

- The case library must not be imported by `features.py`, `staging.py`, or `red_team.py`.
- Do not use case labels as candidate-generation input.
- Do not claim fixture case success as blind discovery.
- Do not lower Stage 3-Green thresholds for recall.
