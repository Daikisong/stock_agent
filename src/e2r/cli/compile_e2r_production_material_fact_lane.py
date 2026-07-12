"""Compile production material facts and blind-lane input lineage from a dossier."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.research_quality import (
    combine_production_material_fact_lanes,
    compile_production_material_fact_lane,
    write_production_material_fact_lane,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dossier-root", action="append", required=True)
    parser.add_argument("--target-id", action="append", required=True)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--output-root")
    args = parser.parse_args()
    if len(args.dossier_root) != len(args.target_id):
        parser.error("--dossier-root and --target-id counts must match")
    lanes = tuple(
        compile_production_material_fact_lane(
            dossier_root=dossier_root,
            target_id=target_id,
            as_of_date=args.as_of_date,
        )
        for dossier_root, target_id in zip(
            args.dossier_root, args.target_id, strict=True
        )
    )
    lane = (
        lanes[0]
        if len(lanes) == 1
        else combine_production_material_fact_lanes(lanes)
    )
    paths = write_production_material_fact_lane(
        lane,
        output_root=args.output_root or args.dossier_root[0],
    )
    print(
        json.dumps(
            {
                "status": "PRODUCTION_MATERIAL_FACT_LANE_COMPILED",
                "fact_count": len(lane.facts),
                "input_count": len(lane.inputs),
                "paths": {key: str(value) for key, value in paths.items()},
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
