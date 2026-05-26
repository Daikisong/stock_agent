# V12 Residual Calibration Ingest Summary

v12는 sector/archetype shadow profile 생성용입니다. 기본 active profile은 변경하지 않습니다.

- md_input_root: `docs/example`
- v12_result_md_count: `2`
- v12_parsed_document_count: `2`
- v12_failed_document_count: `0`
- v12_raw_trigger_rows: `37`
- v12_validated_trigger_rows: `30`
- v12_representative_trigger_rows: `30`
- v12_rejected_rows: `20`
- large_sectors_covered: `['L5_CONSUMER_BRAND_DISTRIBUTION', 'L6_FINANCIAL_CAPITAL_RETURN_DIGITAL']`
- canonical_archetypes_covered: `['C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION', 'C22_INSURANCE_RATE_CYCLE_RESERVE']`
- stage_transition_summary_rows: `14`
- evidence_url_pending_count: `16`
- source_proxy_only_count: `30`
- active_default_profile_preserved: `True`
- production_default_scoring_changed: `False`

## Rejected Rows By Reason
- missing_required_mfe_mae: 7
- not_representative_for_aggregate: 11
- not_usable_for_promotion: 8
- price_only_no_evidence: 1
