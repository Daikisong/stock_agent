# Round-116 R11 Loop-6 Event False-Positive Caps

- `EVENT_PREMIUM`: news moved price, but actual revenue, contract, or budget is missing.
- `EVENT_TO_CONTRACT`: event moved into government contract, stockpile, financing, construction, or recognized revenue.
- `GOVERNMENT_STOCKPILE_GUIDANCE_ALIGNED`: government stockpile contract lifted revenue or margin guidance, but repeat procurement still needs proof.
- `PROCUREMENT_REVERSAL_4C`: public-health funding or procurement was cancelled, withdrawn, delayed, or reversed.
- `CRITICAL_INFRA_FINANCING_ALIGNED`: reconstruction evidence includes critical infrastructure assets, financing, guarantees, or concession structure.
- `SUPPLY_CHAIN_EXPORT_CONTROL_EVENT`: export controls created a macro bottleneck, but company-level capacity and offtake are still missing.
- `EXPORT_CONTROL_TO_OFFTAKE_ESCALATION`: export-control pressure became alternative supply, offtake, price-floor, capacity, and revenue evidence.
- `EVENT_TO_INFRA_CROSSOVER`: disaster/climate event crossed into grid, cooling, VPP, ESS, or rebuild capex.
- `PRICE_MOVED_WITHOUT_EVIDENCE`: policy, SNS, or paper moved price without cash-flow evidence.
- `SPECULATIVE_SCIENCE_FAILURE`: replication failure or no product/customer breaks the thesis.
- `ONE_OFF_REVENUE`: revenue happened, but demand normalized after the event.
- `POLICY_RELIEF_ONLY`: policy existed, but budget, contract, construction, or revenue did not.
- `POLICY_MARKET_SHOCK`: tax, dividend, or regulatory comments hit crowded themes before company-level EPS impact is clear.
- `NORTH_KOREA_HARD_RED`: sanctions, military tension, facility dismantling, road/rail destruction, or hostile rhetoric block unsafe escalation.
- `DISCLOSURE_CONFIDENCE_CAPPED`: budget, contract, order, or construction-start detail is missing, so Stage 3 must be capped.

Simple example: a heatwave can route research to grid or HVAC names. If `cooling_order_flag`, `vpp_program_flag`, and `revenue_recognized_flag` are empty, the case stays Watch/Event, not Stage 3-Green.
