# Round-33 Score-Weight v1.8 Summary

- source_round: `docs/round/round_33.md`
- target_count: 8
- case_candidate_count: 32
- success_candidate_count: 10
- counterexample_or_risk_count: 22
- stage4b_case_count: 0
- stage4c_case_count: 6
- green_possible_count: 1
- watch_yellow_first_count: 4
- redteam_first_count: 3
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Interpretation
- Round 33 adds v1.8 calibration cases and target weights only.
- Example: streaming ad platforms can be candidates when ad ARPU, owned ad platform, inventory, and OPM are visible; traditional media ad cycles remain capped.
- Example: AI software can be Green-possible with recurring subscription/API revenue, but copyright, licensing, data privacy, and compute cost are hard gates.
- Example: NFT/metaverse and livestock disease/price events stay RedTeam-first because price or volume spikes are usually not recurring FCF.
- Theme names, case IDs, regulation headlines, app features, and price rallies are not score evidence by themselves.
