"""Verify tracked Pro-first implementation gates without using live ChatGPT."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

from e2r.pro_first.acceptance import CORE_TEST_MODULES, run_named_tests, write_receipt
from e2r.pro_first.static_audit import compile_pro_first_static_audit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    parser.add_argument("--skip-tests", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.repo_root).expanduser().resolve()
    static = compile_pro_first_static_audit(root)
    core = None if args.skip_tests else run_named_tests(CORE_TEST_MODULES, label="PRO_FIRST_CORE_UNIT")
    required_paths = (
        ".github/workflows/e2r_pro_first_verify.yml",
        "configs/e2r_pro_first_local.example.yaml",
        "requirements/e2r_pro_first_py310_linux_x86_64.lock",
        "scripts/start_e2r_pro_chrome.ps1",
        "scripts/start_e2r_pro_first_stack.ps1",
        "scripts/run_e2r_pro_first_offline_ci.py",
        "docs/operational/e2r_pro_first_v1/README.md",
    )
    missing = [path for path in required_paths if not (root / path).is_file()]
    gates = {
        "static_critical_zero": int(static["critical_count_sum"]) == 0,
        "core_unit_pass": core is None or core.successful,
        "required_tracked_surface_complete": not missing,
        "live_login_not_required_for_implementation_gate": True,
    }
    passed = all(gates.values())
    payload = {
        "schema_version": "e2r_pro_first_readiness_v1",
        "status": "PRO_FIRST_PLATFORM_IMPLEMENTATION_READY" if passed else "PRO_FIRST_PLATFORM_IMPLEMENTATION_NOT_READY",
        "gates": gates,
        "missing_required_paths": missing,
        "core_unit": None if core is None else core.to_dict(),
        "static_audit": static,
        "recorded_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    if args.output:
        write_receipt(args.output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
