"""Recompute the canonical archetype scoring-contract audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.runtime.scoring_contracts import (
    audit_scoring_contract_catalog,
    load_scoring_contract_catalog,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="docs/operational/e2r_canonical_scoring_contract_audit.json")
    args = parser.parse_args(argv)
    catalog = load_scoring_contract_catalog()
    base = audit_scoring_contract_catalog(catalog)
    c06 = catalog.get("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
    if c06 is None:
        raise ValueError("canonical C06 scoring contract is missing")
    result = {
        **base,
        "as_of_date": "2026-07-11",
        "c06_contract": {
            "archetype_id": c06.archetype_id,
            "config_hash": c06.config_hash,
            "edge_catalog_status": c06.edge_catalog_status,
            "component_max_points": dict(c06.component_max_points),
            "primitive_to_component_allowed_edges": {
                key: list(values)
                for key, values in c06.primitive_to_component_allowed_edges.items()
            },
        },
        "explicit_edge_archetype_ids": sorted(
            key
            for key, contract in catalog.contracts.items()
            if contract.edge_catalog_status == "EXPLICIT"
        ),
    }
    write_json(Path(args.output), result)
    print(json.dumps({"status":result["status"],"critical_count_sum":result["critical_count_sum"]},sort_keys=True))
    return 0 if result["critical_count_sum"] == 0 else 2


if __name__ == "__main__": raise SystemExit(main())
