#!/usr/bin/env python3
"""Run the E2R v6 receipt verifier from an isolated clean HEAD worktree.

Canonical invocation executes this bootstrap from Git, not from the mutable
worktree::

    set -o pipefail; \
      git show HEAD:scripts/verify_e2r_v6_tracked_readiness.py | \
      python3 -I -S - --repo-root . --output /tmp/readiness.json

This file intentionally imports only the Python standard library.  E2R is
imported later by a separate isolated interpreter whose source is checked out
directly from the trusted HEAD commit.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
import tempfile


RECEIPT_RELATIVE_ROOT = Path(
    "docs/operational/e2r_v6_operational_cutover/canary_receipts/2026-07-12"
)
BOOTSTRAP_RELATIVE_PATH = Path("scripts/verify_e2r_v6_tracked_readiness.py")
TRUSTED_ORIGIN_IDENTITY = "github.com/Daikisong/stock_agent"
TRUSTED_BASELINE_COMMIT_SHA = "575228b95a070beda8145c1623efcce26ddaa0e9"
PASS_STATUS = "E2R_V6_TRACKED_READINESS_PASS"
FAIL_STATUS = "E2R_V6_TRACKED_READINESS_FAIL"


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    return parser


def _git(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", *args],
        cwd=repo,
        text=True,
        stderr=subprocess.DEVNULL,
    ).strip()


def _normalized_origin_identity(value: str) -> str:
    text = value.strip().removesuffix("/").removesuffix(".git")
    if text.startswith("git@") and ":" in text:
        host, path = text[4:].split(":", 1)
        return f"{host.casefold()}/{path.strip('/')}"
    for prefix in ("https://", "http://", "ssh://git@"):
        if text.startswith(prefix):
            return text[len(prefix) :].strip("/")
    return text


def _trusted_head(repo: Path) -> str:
    try:
        if Path(_git(repo, "rev-parse", "--show-toplevel")).resolve() != repo:
            raise ValueError("repository root mismatch")
        if (
            _normalized_origin_identity(_git(repo, "remote", "get-url", "origin"))
            != TRUSTED_ORIGIN_IDENTITY
        ):
            raise ValueError("repository origin mismatch")
        head = _git(repo, "rev-parse", "HEAD")
        if len(head) != 40 or _git(repo, "rev-parse", "refs/remotes/origin/main") != head:
            raise ValueError("HEAD is not the fetched canonical main commit")
        if _git(repo, "status", "--porcelain=v1", "--untracked-files=all"):
            raise ValueError("repository worktree is not clean")
        for object_name in (
            f"{TRUSTED_BASELINE_COMMIT_SHA}^{{commit}}",
            f"HEAD:{BOOTSTRAP_RELATIVE_PATH.as_posix()}",
        ):
            if subprocess.run(
                ["git", "cat-file", "-e", object_name],
                cwd=repo,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            ).returncode:
                raise ValueError("required trusted Git object is missing")
        if subprocess.run(
            [
                "git",
                "merge-base",
                "--is-ancestor",
                TRUSTED_BASELINE_COMMIT_SHA,
                head,
            ],
            cwd=repo,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode:
            raise ValueError("trusted baseline is not an ancestor of HEAD")
        return head
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("repository trust preflight failed") from exc


def _open_or_create_directory_no_symlinks(path: Path) -> int:
    absolute = path.absolute()
    descriptor = os.open(absolute.anchor, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in absolute.parts[1:]:
            if part in {"", ".", ".."}:
                raise ValueError("unsafe output parent component")
            try:
                child = os.open(
                    part,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=descriptor,
                )
            except FileNotFoundError:
                try:
                    os.mkdir(part, mode=0o700, dir_fd=descriptor)
                except FileExistsError:
                    pass
                child = os.open(
                    part,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=descriptor,
                )
            os.close(descriptor)
            descriptor = child
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _write_json_atomic(path: Path, payload: object) -> None:
    encoded = (
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
            allow_nan=False,
        )
        + "\n"
    )
    parent_fd = _open_or_create_directory_no_symlinks(path.parent)
    temporary_name = f".{path.name}.{secrets.token_hex(16)}.tmp"
    descriptor = -1
    try:
        descriptor = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            descriptor = -1
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(
            temporary_name,
            path.name,
            src_dir_fd=parent_fd,
            dst_dir_fd=parent_fd,
        )
        os.fsync(parent_fd)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        try:
            os.unlink(temporary_name, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        os.close(parent_fd)


def _output_overlaps_receipts(output: Path, receipt_root: Path) -> bool:
    if output == receipt_root or receipt_root in output.parents or output.is_symlink():
        return True
    if output.exists():
        for path in receipt_root.rglob("*"):
            if path.is_file() and not path.is_symlink():
                try:
                    if os.path.samefile(output, path):
                        return True
                except OSError:
                    return True
    return False


def _run_clean_head_verifier(repo: Path, head: str) -> dict[str, object]:
    worker_source = (
        "import json,sys;"
        "sys.path.insert(0,sys.argv[1]);"
        "from e2r.research_brain.researcher_mode.tracked_readiness "
        "import compile_tracked_readiness;"
        "r=compile_tracked_readiness(sys.argv[2],repo_root=sys.argv[3]);"
        "print(json.dumps(r,ensure_ascii=False,sort_keys=True,allow_nan=False));"
        "raise SystemExit(0 if r.get('status')=="
        "'E2R_V6_TRACKED_READINESS_PASS' else 2)"
    )
    with tempfile.TemporaryDirectory(prefix="e2r-v6-readiness-") as directory:
        worktree = Path(directory) / "head"
        subprocess.run(
            ["git", "worktree", "add", "--detach", "--quiet", str(worktree), head],
            cwd=repo,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            completed = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-S",
                    "-c",
                    worker_source,
                    str(worktree / "src"),
                    str(worktree / RECEIPT_RELATIVE_ROOT),
                    str(worktree),
                ],
                cwd=worktree,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                env={
                    "PATH": os.environ.get("PATH", ""),
                    "LANG": os.environ.get("LANG", "C.UTF-8"),
                    "LC_ALL": os.environ.get("LC_ALL", "C.UTF-8"),
                },
            )
        finally:
            subprocess.run(
                ["git", "worktree", "remove", "--force", str(worktree)],
                cwd=repo,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
        if completed.returncode not in {0, 2}:
            raise RuntimeError(
                "isolated readiness verifier failed: " + completed.stderr[-1000:]
            )
        try:
            result = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("isolated verifier returned invalid JSON") from exc
    if (
        not isinstance(result, dict)
        or result.get("schema_version") != "e2r_v6_tracked_readiness_v1"
        or result.get("status") not in {PASS_STATUS, FAIL_STATUS}
        or result.get("offline") is not True
        or result.get("production_readiness_authority") is not False
        or (result.get("status") == PASS_STATUS and result.get("ready") is not True)
    ):
        raise RuntimeError("isolated verifier result contract is invalid")
    return result


def main() -> int:
    args = _parser().parse_args()
    repo = Path(args.repo_root).resolve()
    receipt_root = repo / RECEIPT_RELATIVE_ROOT
    if receipt_root.is_symlink():
        raise SystemExit("canonical receipt root cannot be a symlink")
    head_before = _trusted_head(repo)
    result = _run_clean_head_verifier(repo, head_before)
    if _trusted_head(repo) != head_before:
        raise SystemExit("repository identity changed during verification")
    if args.output:
        output = Path(args.output).absolute()
        if _output_overlaps_receipts(output, receipt_root):
            raise SystemExit("readiness output cannot overwrite a receipt input")
        _write_json_atomic(output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["status"] == PASS_STATUS else 2


if __name__ == "__main__":
    raise SystemExit(main())
