# E2R Calibration Ingest Summary

- md_input_root: `docs/round`
- discovered_md_count: `398`
- discovered_result_md_count: `107`
- excluded_prompt_spec_count: `0`
- unique_document_count: `82`
- duplicate_document_count: `25`
- parsed_document_count: `107`
- failed_document_count: `0`
- metadata_only_document_count: `0`
- raw_trigger_rows: `4951`
- validated_trigger_rows: `1940`
- aggregate_representative_trigger_rows: `1376`
- rejected_rows: `3215`
- rounds_covered: `['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13']`
- loops_covered: `['1', '2', '3', '4', '5', '6', '7', '8', '9']`
- sectors_covered: `['2차전지·전기차·친환경', 'AI·반도체·전자부품', 'Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리', '건설·부동산·건자재', '금융·자본배분·디지털금융', '농업·생활서비스·기타', '모빌리티·운송·레저', '바이오·헬스케어·의료기기', '산업재·수주·인프라', '소비재·유통·브랜드', '소재·스프레드·전략자원', '정책·지정학·재난·이벤트', '플랫폼·콘텐츠·SW·보안']`

## Rejected Rows By Reason
- corporate_action_contaminated: 1
- false_positive_not_positive_promotion: 100
- insufficient_forward_window: 8
- invalid_price_adjustment_status: 2999
- invalid_price_source: 2927
- missing_entry_price: 5
- missing_price_basis: 2999
- missing_required_mfe_mae: 2207
- not_representative_for_aggregate: 1279
- not_usable_for_promotion: 26
- price_only_no_evidence: 1

## Price Source Validation Summary
- usable_for_historical_calibration: 146
- unknown: 7
