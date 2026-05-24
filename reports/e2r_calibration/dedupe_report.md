# E2R Calibration Dedupe Report

Repeated loops are lab-notebook revisions, not independent samples.
대표 예시: 같은 `same_entry_group_id`가 여러 loop에 반복되면 raw row는 보존하지만 aggregate에는 대표 1개만 씁니다.

- raw_trigger_rows: `4951`
- aggregate_representative_trigger_rows: `1376`
- representative selection: same_entry_group_id > JSONL > explicit dedupe_for_aggregate > complete MFE/MAE > latest loop
- fallback dedupe key: round, sector, symbol, archetype, trigger_type, trigger/entry date, rounded entry price, company
