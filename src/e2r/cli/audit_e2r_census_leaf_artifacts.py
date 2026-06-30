"""Audit Census v3 leaf artifacts."""

from __future__ import annotations

import argparse

from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts
from e2r.production.metadata import write_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--write", default="true")
    args = parser.parse_args(argv)
    audit = audit_leaf_artifacts(args.output_root)
    if str(args.write).lower() == "true":
        from pathlib import Path

        write_json(Path(args.output_root) / "leaf_artifact_audit.json", audit)
    print(audit["verdict"])
    return 0 if audit["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
