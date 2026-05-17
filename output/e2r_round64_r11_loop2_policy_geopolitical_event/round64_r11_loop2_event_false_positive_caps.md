# Round-64 R11 Loop-2 Event False-Positive Caps

- `EVENT_PREMIUM`: news moved price, but actual revenue, contract, or budget is missing.
- `EVENT_TO_CONTRACT`: event moved into government contract, stockpile, financing, construction, or recognized revenue.
- `EVENT_TO_INFRA_CROSSOVER`: disaster/climate event crossed into grid, cooling, VPP, ESS, or rebuild capex.
- `PRICE_MOVED_WITHOUT_EVIDENCE`: policy, SNS, or paper moved price without cash-flow evidence.
- `SPECULATIVE_SCIENCE_FAILURE`: replication failure or no product/customer breaks the thesis.
- `ONE_OFF_REVENUE`: revenue happened, but demand normalized after the event.
- `POLICY_RELIEF_ONLY`: policy existed, but budget, contract, construction, or revenue did not.
- `NORTH_KOREA_HARD_RED`: sanctions, military tension, facility dismantling, road/rail destruction, or hostile rhetoric block unsafe escalation.

Simple example: a heatwave can route research to grid or HVAC names. If `cooling_order_flag`, `vpp_program_flag`, and `revenue_recognized_flag` are empty, the case stays Watch/Event, not Stage 3-Green.
