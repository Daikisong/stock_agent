"""Compile canonical E2R research intelligence."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.runtime.command_status import reconstruction_pending_payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--strict", default="true")
    args = parser.parse_args(argv)
    print(
        json.dumps(
            reconstruction_pending_payload(
                command="compile_e2r_research_intelligence",
                required_phase=2,
                inputs={
                    "repo_root": args.repo_root,
                    "output_root": args.output_root,
                    "strict": args.strict,
                },
            ),
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
