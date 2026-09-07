"""Run the four production-path Pro-first golden E2E acceptance tests."""

from __future__ import annotations

import argparse
import json

from e2r.pro_first.acceptance import OFFLINE_E2E_TEST_NAMES, run_named_tests, write_receipt


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    run = run_named_tests(OFFLINE_E2E_TEST_NAMES, label="PRO_FIRST_OFFLINE_E2E")
    payload = run.to_dict()
    if args.output:
        write_receipt(args.output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if run.successful else 2


if __name__ == "__main__":
    raise SystemExit(main())
