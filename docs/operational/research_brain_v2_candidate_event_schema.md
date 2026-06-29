# Research Brain v2 CandidateEventV2 Schema

CandidateEventV2는 종목 row가 아니라 사건 row다.

쉬운 예: 한 종목에 공급계약, 신규시설투자, 가격 급등이 동시에 있으면 하나의 종목 후보가 아니라 `supply_contract`, `facility_investment`, `price_relative_strength` 세 사건으로 나눈다.

## Required Fields

- `candidate_event_id`: deterministic hash id
- `symbol`, `company_name`
- `event_date`, `detected_at`
- `source_family`, `source_id`
- `event_type`, `raw_reason_codes`
- `event_title`, `event_summary`
- `magnitude`
- `issuer_directness`
- `initial_evidence_document_ids`
- `structured_payload`, `price_context`

Research Brain은 이 event를 라우팅하고 조사 task를 만들 수 있지만, score/stage를 직접 확정하지 않는다.
