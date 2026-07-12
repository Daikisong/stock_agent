"""Compile the E2R v5 economic-fact Component Anchor Atlas."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.researcher_mode import (
    compile_component_anchor_atlas_from_files,
    write_component_anchor_atlas,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--atlas-root", default="output/researcher_parity/judgment_atlas"
    )
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_v5_component_anchor_atlas.json",
    )
    args = parser.parse_args(argv)
    atlas = compile_component_anchor_atlas_from_files(atlas_root=args.atlas_root)
    path = write_component_anchor_atlas(atlas, output_path=args.output)
    print(
        json.dumps(
            {
                "status": atlas["status"],
                "critical_count_sum": atlas["critical_count_sum"],
                "component_anchor_count": atlas["component_anchor_count"],
                "exact_anchor_count": atlas["exact_anchor_count"],
                "counter_anchor_count": atlas["counter_anchor_count"],
                "output": str(path),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if atlas["critical_count_sum"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
