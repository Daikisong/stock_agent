# V12 Promotion Readiness Report

- active_profile_preserved: `true`
- production_default_scoring_changed: `false`
- default_promotion_ready: `False`
- stage_transition_summary_rows: `14`

## Blockers
- evidence_url_pending: 16 / v12 rows can support shadow analysis but need exact public evidence URLs before default promotion. / needed: Attach verified DART/IR/report/news URLs or mark rows as evidence-verified.
- source_proxy_only: 30 / Some evidence is source-name-level historical event proxy, not verified production evidence. / needed: Replace proxy rows with verified as-of evidence records.
- rejected_rows: 20 / Some rows failed validation or were not usable for shadow calibration. / needed: Fix missing sector/archetype IDs, price fields, or evidence flags.
