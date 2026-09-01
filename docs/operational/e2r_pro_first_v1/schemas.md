# Schema 계약

추적 schema:

- `configs/e2r_pro_research_packet_v1.schema.json`
- `configs/e2r_pro_research_dossier_v1.schema.json`
- `configs/e2r_pro_research_prompt_v1.md`

`ResearchPacketV1`은 target, `as_of_date`, trigger, blind-safe historical digest, research objectives만 전달한다. `expected_score`, `expected_stage`, 미래 성과 같은 정답 필드는 재귀적으로 금지된다.

`ResearchDossierV1`의 material fact는 URL, 발행일, 짧은 exact excerpt, subject/segment/product 범위를 가져야 한다. Pro가 제안한 score range와 gap class는 제안일 뿐 authority가 아니다.

쉬운 예: `as_of_date=2023-07-27` packet에는 2023-07-28 공시를 넣을 수 없다. dossier가 그 공시를 가져오더라도 source verifier가 `REJECTED_FUTURE`로 격리한다.
