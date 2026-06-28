# Research Brain v1 Known Regressions

- source_proxy_only memory recall must never become production score contribution.
- evidence_url_pending memory can be ontology/source-gap only until URL repair.
- MFE/MAE and future outcome labels are forbidden from extraction prompts.
- Research Brain plan output must not contain score/stage/current_score_eligible.
- FCF/cash gaps must route to DART/CompanyGuide/IR before news/general search.
- Candidate discovery dry run must use `targeted_smoke_only=false` and record provider/source gaps instead of fabricating candidates.
