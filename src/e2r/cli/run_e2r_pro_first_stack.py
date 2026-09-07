"""Start the local Pro-first scheduler, dashboard, browser worker and reconciler."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.runtime import ProFirstLocalStack


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    config = load_pro_first_local_config(args.config)
    stack = ProFirstLocalStack(config, repo_root=args.repo_root)
    print(json.dumps(stack.readiness_snapshot(), ensure_ascii=False, indent=2, sort_keys=True))
    if args.check:
        return 0
    asyncio.run(stack.run_forever())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
