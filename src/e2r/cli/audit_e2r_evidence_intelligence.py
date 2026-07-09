"""Audit canonical E2R evidence intelligence from leaf artifacts."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.runtime.command_status import reconstruction_pending_payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-root")
    parser.add_argument("--fail-on-critical", default="true")
    args = parser.parse_args(argv)
    print(
        json.dumps(
            reconstruction_pending_payload(
                command="audit_e2r_evidence_intelligence",
                required_phase=14,
                inputs=vars(args),
            ),
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
