"""Audit the canonical E2R v5 Phase 84 Researcher Mode boundary."""

from __future__ import annotations

import argparse

from e2r.research_brain.researcher_mode import (
    compile_phase84_researcher_mode_audit,
    write_phase84_researcher_mode_audit,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    audit = compile_phase84_researcher_mode_audit(args.repo_root)
    path = write_phase84_researcher_mode_audit(
        repo_root=args.repo_root, output_path=args.output
    )
    print(
        f"{audit['status']} roles={len(audit['researcher_roles'])} "
        f"modules={len(audit['required_modules'])} "
        f"critical={audit['critical_count_sum']} output={path}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
