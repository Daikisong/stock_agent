"""Freeze one completed repair-heavy V2 run before fresh-session validation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.pro_first.fresh_session import OldRunFreezeService
from e2r.pro_first.job_store import ProFirstJobStore


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtime-root", required=True)
    parser.add_argument("--job-id", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args(argv)
    runtime_root = Path(args.runtime_root).resolve()
    job_root = runtime_root / "jobs" / args.job_id
    if not job_root.is_dir():
        raise FileNotFoundError(f"job runtime root does not exist: {job_root}")
    store = ProFirstJobStore(runtime_root / "pro_first.sqlite3")
    receipt = OldRunFreezeService(store).freeze(
        job_id=args.job_id,
        run_id=args.run_id,
        job_root=job_root,
    )
    print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
