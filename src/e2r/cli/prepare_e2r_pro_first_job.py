"""Create an explicit canary or prepare an existing Pro job packet."""

from __future__ import annotations

import argparse
import json

from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.operations import build_job_packet, create_forced_validation_canary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--job-id")
    parser.add_argument("--symbol")
    parser.add_argument("--company-name")
    parser.add_argument("--as-of-date")
    parser.add_argument("--archetype-id", action="append", default=[])
    args = parser.parse_args(argv)
    config = load_pro_first_local_config(args.config)
    store = ProFirstJobStore(config.database_path)
    if args.job_id:
        job_id = args.job_id
    else:
        if not all((args.symbol, args.company_name, args.as_of_date)):
            parser.error("--job-id or --symbol/--company-name/--as-of-date is required")
        job_id = create_forced_validation_canary(
            store,
            symbol=args.symbol,
            company_name=args.company_name,
            as_of_date=args.as_of_date,
            archetype_ids=tuple(args.archetype_id),
        ).job_id
    job, bundle, prompt = build_job_packet(
        store,
        job_id=job_id,
        runtime_root=config.runtime_root,
        config_hash=config.config_hash,
        repo_root=args.repo_root,
    )
    print(
        json.dumps(
            {
                "status": job.status,
                "job_id": job.job_id,
                "selection_mode": job.mode,
                "target": {"symbol": job.symbol, "company_name": job.company_name},
                "as_of_date": job.as_of_date,
                "packet_path": str(bundle.research_packet_json),
                "packet_hash": bundle.packet_hash,
                "prompt_hash": prompt.prompt_hash,
                "submit_count": job.submit_count,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
