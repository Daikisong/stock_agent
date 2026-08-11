#!/usr/bin/env python3
"""Produce the canonical Phase-102/103 proof from a real clean clone.

This bootstrap intentionally imports only the Python standard library.  It
does not import mutable-worktree E2R code.  The first E2R import happens in a
separate ``python -I -S`` process after a no-local clone has been bound to the
trusted ``origin/main`` commit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import shlex
import subprocess
import sys
import tempfile
from typing import Any, Callable, Mapping, Sequence
from urllib import request as urllib_request


FINAL_ROOT_RELATIVE = Path("docs/operational/e2r_v6_operational_cutover")
RECEIPT_ROOT_RELATIVE = FINAL_ROOT_RELATIVE / "canary_receipts/2026-07-12"
BOOTSTRAP_RELATIVE_PATH = Path(
    "scripts/run_e2r_v6_clean_clone_reproduction.py"
)
DEPENDENCY_LOCK_RELATIVE_PATH = Path(
    "requirements/e2r_v6_clean_clone_py310_linux_x86_64.lock"
)
CLEAN_CLONE_DIRECTORY_NAME = "clean_clone"
CLEAN_CLONE_CHILD_NAMES = (
    "receipt_recompute_result.json",
    "tracked_readiness_result.json",
    "test_result.json",
)
REPRODUCTION_RESULT_NAME = "clean_clone_reproduction.json"
CANARY_RECEIPT_DATE = "2026-07-12"
EXPECTED_TARGET_IDS = ("005930", "000660")

TRUSTED_ORIGIN_IDENTITY = "github.com/Daikisong/stock_agent"
TRUSTED_CLONE_URL = "https://github.com/Daikisong/stock_agent.git"
TRUSTED_BASELINE_COMMIT_SHA = "575228b95a070beda8145c1623efcce26ddaa0e9"
ISOLATED_PYTHON = Path("/usr/bin/python3")
ISOLATED_GIT = Path("/usr/bin/git")
PIP_BOOTSTRAP_URL = (
    "https://files.pythonhosted.org/packages/3a/eb/"
    "fea4d1d51c49832120f7f285d07306db3960f423a2612c6057caf3e8196f/"
    "pip-26.1.1-py3-none-any.whl"
)
PIP_BOOTSTRAP_SHA256 = (
    "99cb1c2899893b075ff56e4ed0af55669a955b49ad7fb8d8603ecdaf4ed653fb"
)
PIP_BOOTSTRAP_NAME = "pip-26.1.1-py3-none-any.whl"
PIP_BOOTSTRAP_MAX_BYTES = 10 * 1024 * 1024
REQUIRED_TEST_DEPENDENCIES = ("jsonschema", "pdfplumber", "pypdf", "requests")
EXPECTED_LOCKED_PACKAGES = frozenset(
    {
        "attrs",
        "certifi",
        "cffi",
        "charset-normalizer",
        "cryptography",
        "idna",
        "jsonschema",
        "jsonschema-specifications",
        "pdfminer-six",
        "pdfplumber",
        "pillow",
        "pycparser",
        "pypdf",
        "pypdfium2",
        "referencing",
        "requests",
        "rpds-py",
        "typing-extensions",
        "urllib3",
    }
)

VERIFICATION_SCHEMA = "e2r_v6_receipt_only_verification_v1"
VERIFICATION_PASS = "E2R_V6_RECEIPT_ONLY_REPRODUCTION_PASS"
TRACKED_READINESS_SCHEMA = "e2r_v6_tracked_readiness_v1"
TRACKED_READINESS_PASS = "E2R_V6_TRACKED_READINESS_PASS"
CLEAN_CLONE_TEST_SCHEMA = "e2r_v6_clean_clone_test_result_v1"
CLEAN_CLONE_TEST_PASS = "E2R_V6_CLEAN_CLONE_TEST_PASS"
CLEAN_CLONE_REPRODUCTION_SCHEMA = "e2r_v6_clean_clone_reproduction_v1"
CLEAN_CLONE_REPRODUCTION_PASS = "E2R_V6_CLEAN_CLONE_REPRODUCTION_PASS"

_HEX_40 = re.compile(r"[0-9a-f]{40}\Z")
_HEX_64 = re.compile(r"[0-9a-f]{64}\Z")
_TEST_SUMMARY = re.compile(r"^Ran\s+([0-9]+)\s+tests?\s+in\s+.+$", re.MULTILINE)
_TEST_OK = re.compile(r"^OK(?:\s+\(.*\))?\s*$", re.MULTILINE)
_LOCK_ROW = re.compile(
    r"([A-Za-z0-9][A-Za-z0-9_.-]*)==([A-Za-z0-9][A-Za-z0-9_.+!-]*)"
    r"\s+--hash=sha256:([0-9a-f]{64})\Z"
)
_FORBIDDEN_CLONE_PATHS = (
    Path("output"),
    Path(".env"),
    Path("cache"),
    Path("data/cache"),
    Path("journal"),
    Path("collaboration_journal"),
)
_TEST_RESULT_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "executed_test_count",
        "failed_test_count",
        "error_test_count",
        "critical_count_sum",
        "production_readiness_authority",
    }
)
_REPRODUCTION_RESULT_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "as_of_date",
        "receipt_recompute_result_hash",
        "tracked_readiness_result_hash",
        "test_result_hash",
        "critical_count_sum",
        "production_readiness_authority",
    }
)


class CleanCloneReproductionError(RuntimeError):
    """A fail-closed Phase-102/103 precondition or replay failure."""


E2R_REPLAY_WORKER_SOURCE = r"""
import json
from pathlib import Path
import sys
import types

source_root = Path(sys.argv[1])
repo_root = Path(sys.argv[2])
receipt_root = Path(sys.argv[3])
mode = sys.argv[4]

for package_name, relative_path in (
    ("e2r", "e2r"),
    ("e2r.agentic", "e2r/agentic"),
    ("e2r.calibration", "e2r/calibration"),
    ("e2r.production", "e2r/production"),
    ("e2r.research_brain", "e2r/research_brain"),
    ("e2r.research_brain.planning", "e2r/research_brain/planning"),
    ("e2r.research_brain.scoring", "e2r/research_brain/scoring"),
    ("e2r.research_brain.researcher_mode", "e2r/research_brain/researcher_mode"),
):
    package = types.ModuleType(package_name)
    package.__package__ = package_name
    package.__path__ = [str(source_root / relative_path)]
    sys.modules[package_name] = package

if mode == "receipt":
    from e2r.research_brain.researcher_mode.tracked_receipts import verify_receipts
    result = verify_receipts(receipt_root)
elif mode == "readiness":
    from e2r.research_brain.researcher_mode.tracked_readiness import compile_tracked_readiness
    result = compile_tracked_readiness(receipt_root, repo_root=repo_root)
else:
    raise SystemExit("unknown clean-clone replay mode")

print(json.dumps(result, ensure_ascii=False, sort_keys=True, allow_nan=False))
raise SystemExit(0)
"""


PIP_BOOTSTRAP_WORKER_SOURCE = r"""
import runpy
import sys

wheel = sys.argv.pop(1)
sys.path.insert(0, wheel)
sys.argv[0] = "pip"
runpy.run_module("pip", run_name="__main__")
"""


DEPENDENCY_SMOKE_WORKER_SOURCE = r"""
import importlib
from importlib import metadata
import json
from pathlib import Path
import sys

source_root = Path(sys.argv[1]).resolve()
dependency_root = Path(sys.argv[2]).resolve()
sys.path.insert(0, str(source_root))
sys.path.insert(1, str(dependency_root))
expected = json.loads(sys.argv[3])
rows = []
for module_name, expected_version in sorted(expected.items()):
    row = {
        "module": module_name,
        "expected_version": expected_version,
        "version": None,
        "origin": None,
        "inside_dependency_root": False,
        "error": None,
    }
    try:
        module = importlib.import_module(module_name)
        origin = Path(module.__file__).resolve()
        version = metadata.version(module_name)
        row["version"] = version
        row["origin"] = str(origin)
        row["inside_dependency_root"] = (
            origin == dependency_root or dependency_root in origin.parents
        )
        if version != expected_version:
            row["error"] = "VERSION_MISMATCH"
        elif not row["inside_dependency_root"]:
            row["error"] = "IMPORT_OUTSIDE_DEPENDENCY_ROOT"
    except BaseException as exc:
        row["error"] = f"{type(exc).__name__}:{exc}"
    rows.append(row)
print(json.dumps({"rows": rows}, ensure_ascii=False, sort_keys=True))
raise SystemExit(0 if all(row["error"] is None for row in rows) else 2)
"""


NESTED_PYTHON_WORKER_SOURCE = r"""
from pathlib import Path
import runpy
import sys

source_root = Path(sys.argv[1])
repo_root = Path(sys.argv[2])
tests_root = Path(sys.argv[3])
dependency_root = Path(sys.argv[4])
wrapper = sys.argv[5]
arguments = list(sys.argv[6:])
sys.path[:0] = [
    str(source_root),
    str(repo_root),
    str(tests_root),
    str(dependency_root),
]
sys.executable = wrapper
while arguments and arguments[0] in {"-I", "-S", "-B", "-E", "-s", "-u"}:
    arguments.pop(0)
while len(arguments) >= 2 and arguments[0] == "-X":
    del arguments[:2]
if not arguments:
    raise SystemExit("isolated nested Python requires a script, -c, -m, or stdin")
mode = arguments.pop(0)
if mode == "-c":
    if not arguments:
        raise SystemExit("isolated nested Python -c requires source")
    source = arguments.pop(0)
    sys.argv = ["-c", *arguments]
    namespace = {"__name__": "__main__", "__package__": None}
    exec(compile(source, "<string>", "exec"), namespace, namespace)
elif mode == "-m":
    if not arguments:
        raise SystemExit("isolated nested Python -m requires a module")
    module = arguments.pop(0)
    sys.argv = [module, *arguments]
    runpy.run_module(module, run_name="__main__")
elif mode == "-":
    sys.argv = ["-", *arguments]
    source = sys.stdin.read()
    namespace = {"__name__": "__main__", "__package__": None}
    exec(compile(source, "<stdin>", "exec"), namespace, namespace)
else:
    sys.argv = [mode, *arguments]
    runpy.run_path(mode, run_name="__main__")
"""


FULL_TEST_WORKER_SOURCE = r"""
from pathlib import Path
import runpy
import sys

source_root = Path(sys.argv.pop(1))
dependency_root = Path(sys.argv.pop(1))
python_wrapper = Path(sys.argv.pop(1))
repo_root = source_root.parent
tests_root = repo_root / "tests"
sys.path.insert(0, str(source_root))
sys.path.insert(1, str(repo_root))
sys.path.insert(2, str(tests_root))
sys.path.insert(3, str(dependency_root))
sys.executable = str(python_wrapper)
sys.argv[0] = "unittest"
runpy.run_module("unittest", run_name="__main__")
"""


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    return parser


def _assert_supported_isolated_platform(env: Mapping[str, str]) -> None:
    if not ISOLATED_PYTHON.is_file():
        raise CleanCloneReproductionError("canonical /usr/bin/python3 is missing")
    probe_source = (
        "import json,platform,sys;"
        "print(json.dumps([sys.implementation.name,*sys.version_info[:2],"
        "sys.platform,platform.machine()]))"
    )
    completed = subprocess.run(
        [str(ISOLATED_PYTHON), "-I", "-S", "-c", probe_source],
        env=dict(env),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    try:
        identity = json.loads(completed.stdout)
    except json.JSONDecodeError:
        identity = None
    if completed.returncode != 0 or identity != [
        "cpython",
        3,
        10,
        "linux",
        "x86_64",
    ]:
        raise CleanCloneReproductionError(
            "clean-clone dependencies require CPython 3.10 on Linux x86_64"
        )


def _normalized_origin_identity(value: str) -> str:
    text = value.strip().removesuffix("/").removesuffix(".git")
    if text.startswith("git@") and ":" in text:
        host, path = text[4:].split(":", 1)
        return f"{host.casefold()}/{path.strip('/')}"
    for prefix in ("https://", "http://", "ssh://git@"):
        if text.startswith(prefix):
            return text[len(prefix) :].strip("/")
    return text


def _path_or_parent_is_symlink(path: Path) -> bool:
    current = path.absolute()
    while True:
        try:
            if current.is_symlink():
                return True
        except OSError:
            return True
        if current == current.parent:
            return False
        current = current.parent


def _sanitized_environment(runtime_root: Path) -> dict[str, str]:
    home = runtime_root / "home"
    temporary = runtime_root / "tmp"
    xdg_config = runtime_root / "xdg-config"
    xdg_cache = runtime_root / "xdg-cache"
    for directory in (home, temporary, xdg_config, xdg_cache):
        directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    if not ISOLATED_GIT.is_file():
        raise CleanCloneReproductionError("canonical /usr/bin/git is unavailable")
    return {
        "PATH": "/usr/bin:/bin",
        "HOME": str(home),
        "TMPDIR": str(temporary),
        "XDG_CONFIG_HOME": str(xdg_config),
        "XDG_CACHE_HOME": str(xdg_cache),
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "TZ": "UTC",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_ASKPASS": os.devnull,
        "SSH_ASKPASS": os.devnull,
        "GIT_OPTIONAL_LOCKS": "0",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONNOUSERSITE": "1",
        "PIP_CONFIG_FILE": os.devnull,
        "PIP_DISABLE_PIP_VERSION_CHECK": "1",
        "PIP_NO_INPUT": "1",
    }


def _git_executable(env: Mapping[str, str]) -> str:
    del env
    if not ISOLATED_GIT.is_file():
        raise CleanCloneReproductionError("git executable is unavailable")
    return str(ISOLATED_GIT)


def _git_text(repo: Path, env: Mapping[str, str], *args: str) -> str:
    try:
        return subprocess.check_output(
            [_git_executable(env), *args],
            cwd=repo,
            env=dict(env),
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise CleanCloneReproductionError(
            "Git command failed: " + " ".join(args)
        ) from exc


def _git_bytes(repo: Path, env: Mapping[str, str], *args: str) -> bytes:
    try:
        return subprocess.check_output(
            [_git_executable(env), *args],
            cwd=repo,
            env=dict(env),
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise CleanCloneReproductionError(
            "Git command failed: " + " ".join(args)
        ) from exc


def _git_ok(repo: Path, env: Mapping[str, str], *args: str) -> bool:
    try:
        return (
            subprocess.run(
                [_git_executable(env), *args],
                cwd=repo,
                env=dict(env),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            ).returncode
            == 0
        )
    except OSError:
        return False


def _parse_git_roster(encoded: bytes, *, index: bool) -> dict[str, tuple[str, str]]:
    roster: dict[str, tuple[str, str]] = {}
    for raw in encoded.split(b"\0"):
        if not raw:
            continue
        try:
            header, raw_path = raw.split(b"\t", 1)
            fields = header.decode("ascii").split()
            path = raw_path.decode("utf-8", errors="surrogateescape")
        except (UnicodeDecodeError, ValueError) as exc:
            raise CleanCloneReproductionError("Git roster is malformed") from exc
        if index:
            if len(fields) != 3 or fields[2] != "0":
                raise CleanCloneReproductionError("Git index stage is noncanonical")
            mode, object_hash = fields[0], fields[1]
        else:
            if len(fields) != 3 or fields[1] != "blob":
                raise CleanCloneReproductionError("non-blob tracked entry is forbidden")
            mode, object_hash = fields[0], fields[2]
        if path in roster:
            raise CleanCloneReproductionError("Git roster path is duplicated")
        roster[path] = (mode, object_hash)
    return roster


def _worktree_matches_head(repo: Path, env: Mapping[str, str]) -> bool:
    try:
        tracked = tuple(
            raw.decode("utf-8", errors="surrogateescape")
            for raw in _git_bytes(repo, env, "ls-files", "-z").split(b"\0")
            if raw
        )
        if not tracked or any("\n" in path or "\r" in path for path in tracked):
            return False
        head = _parse_git_roster(
            _git_bytes(repo, env, "ls-tree", "-r", "-z", "HEAD"), index=False
        )
        index = _parse_git_roster(
            _git_bytes(repo, env, "ls-files", "-s", "-z"), index=True
        )
        if set(tracked) != set(head) or head != index:
            return False
        completed = subprocess.run(
            [_git_executable(env), "hash-object", "--stdin-paths"],
            cwd=repo,
            env=dict(env),
            input="".join(f"{path}\n" for path in tracked).encode(
                "utf-8", errors="surrogateescape"
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        worktree_hashes = tuple(completed.stdout.decode("ascii").splitlines())
    except (OSError, UnicodeDecodeError, CleanCloneReproductionError):
        return False
    return bool(
        completed.returncode == 0
        and len(worktree_hashes) == len(tracked)
        and all(
            head[path][1] == worktree_hash
            for path, worktree_hash in zip(tracked, worktree_hashes)
        )
    )


def _trusted_source_head(repo_root: str | Path, env: Mapping[str, str]) -> str:
    raw_repo = Path(repo_root).absolute()
    if _path_or_parent_is_symlink(raw_repo):
        raise CleanCloneReproductionError("repository path uses a symlink")
    repo = raw_repo.resolve()
    if not repo.is_dir():
        raise CleanCloneReproductionError("repository root is missing")
    top = Path(_git_text(repo, env, "rev-parse", "--show-toplevel")).resolve()
    if top != repo:
        raise CleanCloneReproductionError("repository root mismatch")
    origin = _git_text(repo, env, "remote", "get-url", "origin")
    if _normalized_origin_identity(origin) != TRUSTED_ORIGIN_IDENTITY:
        raise CleanCloneReproductionError("repository origin is untrusted")
    head = _git_text(repo, env, "rev-parse", "HEAD")
    remote_main = _git_text(repo, env, "rev-parse", "refs/remotes/origin/main")
    if not _HEX_40.fullmatch(head) or remote_main != head:
        raise CleanCloneReproductionError("HEAD is not the fetched origin/main SHA")
    if _git_bytes(repo, env, "status", "--porcelain=v1", "-z", "--untracked-files=all"):
        raise CleanCloneReproductionError("repository worktree is dirty")
    if not _worktree_matches_head(repo, env):
        raise CleanCloneReproductionError("tracked worktree bytes differ from HEAD")
    if not _git_ok(
        repo,
        env,
        "cat-file",
        "-e",
        f"{TRUSTED_BASELINE_COMMIT_SHA}^{{commit}}",
    ) or not _git_ok(
        repo,
        env,
        "merge-base",
        "--is-ancestor",
        TRUSTED_BASELINE_COMMIT_SHA,
        head,
    ):
        raise CleanCloneReproductionError("trusted baseline is not in HEAD history")
    for relative in (BOOTSTRAP_RELATIVE_PATH, DEPENDENCY_LOCK_RELATIVE_PATH):
        if not _git_ok(
            repo,
            env,
            "cat-file",
            "-e",
            f"HEAD:{relative.as_posix()}",
        ):
            raise CleanCloneReproductionError(
                f"required clean-clone input is not tracked at HEAD: {relative}"
            )
    return head


def _clone_command(git: str, destination: Path) -> list[str]:
    return [
        git,
        "clone",
        "--no-local",
        "--no-tags",
        "--single-branch",
        "--branch",
        "main",
        "--origin",
        "origin",
        "--",
        TRUSTED_CLONE_URL,
        str(destination),
    ]


def _clone_origin_main(
    *,
    scratch_root: Path,
    expected_sha: str,
    env: Mapping[str, str],
) -> Path:
    clone = scratch_root / "origin-main"
    if clone.exists() or clone.is_symlink():
        raise CleanCloneReproductionError("clean clone destination already exists")
    completed = subprocess.run(
        _clone_command(_git_executable(env), clone),
        cwd=scratch_root,
        env=dict(env),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise CleanCloneReproductionError(
            "git clone --no-local failed: " + completed.stderr[-1000:]
        )
    checkout = subprocess.run(
        [_git_executable(env), "checkout", "--detach", "--quiet", expected_sha],
        cwd=clone,
        env=dict(env),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if checkout.returncode != 0:
        raise CleanCloneReproductionError(
            "clean clone cannot check out final SHA: " + checkout.stderr[-1000:]
        )
    return clone


def _assert_forbidden_clone_inputs_absent(clone: Path) -> None:
    present = [
        relative.as_posix()
        for relative in _FORBIDDEN_CLONE_PATHS
        if (clone / relative).exists() or (clone / relative).is_symlink()
    ]
    if present:
        raise CleanCloneReproductionError(
            "clean clone contains forbidden runtime inputs: " + ",".join(present)
        )


def _clone_git_objects_are_private(clone: Path) -> bool:
    """Reject alternates, symlinked objects, and local-clone hard links."""

    objects = clone / ".git/objects"
    if objects.is_symlink() or not objects.is_dir():
        return False
    regular_count = 0
    try:
        for directory, directory_names, file_names in os.walk(
            objects, topdown=True, followlinks=False
        ):
            root = Path(directory)
            for name in tuple(directory_names):
                child = root / name
                if child.is_symlink():
                    return False
            for name in file_names:
                child = root / name
                if child.is_symlink() or not child.is_file():
                    return False
                regular_count += 1
                if child.stat().st_nlink != 1:
                    return False
    except OSError:
        return False
    return regular_count > 0


def _parse_dependency_lock(lock: Path) -> tuple[tuple[str, str, str], ...]:
    if lock.is_symlink() or not lock.is_file():
        raise CleanCloneReproductionError("tracked dependency lock is missing")
    try:
        if lock.stat().st_nlink != 1:
            raise CleanCloneReproductionError("dependency lock hardlink is forbidden")
        lines = lock.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise CleanCloneReproductionError("dependency lock cannot be read") from exc
    logical_rows: list[str] = []
    pending = ""
    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            if pending:
                raise CleanCloneReproductionError(
                    "dependency lock continuation is malformed"
                )
            continue
        if stripped.endswith("\\"):
            pending += stripped[:-1].strip() + " "
            continue
        logical_rows.append((pending + stripped).strip())
        pending = ""
    if pending:
        raise CleanCloneReproductionError("dependency lock continuation is incomplete")
    parsed: list[tuple[str, str, str]] = []
    for row in logical_rows:
        match = _LOCK_ROW.fullmatch(row)
        if match is None:
            raise CleanCloneReproductionError(
                "dependency lock requires one exact version and SHA256 per wheel"
            )
        parsed.append(match.groups())
    return tuple(parsed)


def _validate_dependency_lock(clone: Path) -> Path:
    lock = clone / DEPENDENCY_LOCK_RELATIVE_PATH
    parsed = _parse_dependency_lock(lock)
    normalized_names = tuple(
        name.casefold().replace("_", "-").replace(".", "-")
        for name, _version, _digest in parsed
    )
    hashes = tuple(digest for _name, _version, digest in parsed)
    if not (
        set(normalized_names) == EXPECTED_LOCKED_PACKAGES
        and len(set(normalized_names)) == len(normalized_names)
        and len(set(hashes)) == len(hashes)
    ):
        raise CleanCloneReproductionError("dependency lock wheel roster is not exact")
    return lock


def _required_dependency_versions(lock: Path) -> Mapping[str, str]:
    versions = {
        name.casefold().replace("_", "-").replace(".", "-"): version
        for name, version, _digest in _parse_dependency_lock(lock)
    }
    try:
        return {name: versions[name] for name in REQUIRED_TEST_DEPENDENCIES}
    except KeyError as exc:
        raise CleanCloneReproductionError(
            "dependency lock lacks a required import"
        ) from exc


def _validate_clean_clone(
    clone: Path,
    *,
    expected_sha: str,
    env: Mapping[str, str],
) -> None:
    if _path_or_parent_is_symlink(clone) or not clone.is_dir():
        raise CleanCloneReproductionError("clean clone path is unsafe")
    if not (clone / ".git").is_dir() or (clone / ".git").is_symlink():
        raise CleanCloneReproductionError("clean clone Git directory is unsafe")
    top = Path(_git_text(clone, env, "rev-parse", "--show-toplevel")).resolve()
    origin = _git_text(clone, env, "remote", "get-url", "origin")
    head = _git_text(clone, env, "rev-parse", "HEAD")
    remote_main = _git_text(clone, env, "rev-parse", "refs/remotes/origin/main")
    if top != clone.resolve():
        raise CleanCloneReproductionError("clean clone repository root mismatch")
    if _normalized_origin_identity(origin) != TRUSTED_ORIGIN_IDENTITY:
        raise CleanCloneReproductionError("clean clone origin is untrusted")
    if head != expected_sha or remote_main != expected_sha:
        raise CleanCloneReproductionError("clean clone is not the final origin/main SHA")
    if _git_text(clone, env, "rev-parse", "--is-shallow-repository") != "false":
        raise CleanCloneReproductionError("shallow clean clones are forbidden")
    if _git_bytes(clone, env, "status", "--porcelain=v1", "-z", "--untracked-files=all"):
        raise CleanCloneReproductionError("clean clone is dirty")
    if not _worktree_matches_head(clone, env):
        raise CleanCloneReproductionError("clean clone bytes differ from final SHA")
    alternates = clone / ".git/objects/info/alternates"
    if alternates.exists() or alternates.is_symlink():
        raise CleanCloneReproductionError("shared Git object alternates are forbidden")
    if not _clone_git_objects_are_private(clone):
        raise CleanCloneReproductionError(
            "clean clone Git objects are not private no-local copies"
        )
    if not _git_ok(
        clone,
        env,
        "merge-base",
        "--is-ancestor",
        TRUSTED_BASELINE_COMMIT_SHA,
        expected_sha,
    ):
        raise CleanCloneReproductionError("clean clone lacks the trusted baseline")
    _validate_dependency_lock(clone)
    _assert_forbidden_clone_inputs_absent(clone)


def _isolated_python_command(
    *,
    worker_source: str,
    arguments: Sequence[str],
) -> list[str]:
    return [
        str(ISOLATED_PYTHON),
        "-I",
        "-S",
        "-B",
        "-X",
        "utf8",
        "-c",
        worker_source,
        *map(str, arguments),
    ]


def _strict_json_object(encoded: str) -> dict[str, Any]:
    def reject_constant(value: str) -> None:
        raise ValueError(f"non-finite JSON constant is forbidden: {value}")

    value = json.loads(encoded, parse_constant=reject_constant)
    if not isinstance(value, dict):
        raise ValueError("worker JSON must be an object")
    return value


def _run_replay_worker(
    clone: Path,
    *,
    mode: str,
    env: Mapping[str, str],
) -> Mapping[str, Any]:
    if mode not in {"receipt", "readiness"}:
        raise ValueError("unsupported replay worker mode")
    completed = subprocess.run(
        _isolated_python_command(
            worker_source=E2R_REPLAY_WORKER_SOURCE,
            arguments=(
                str(clone / "src"),
                str(clone),
                str(clone / RECEIPT_ROOT_RELATIVE),
                mode,
            ),
        ),
        cwd=clone,
        env=dict(env),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise CleanCloneReproductionError(
            f"isolated {mode} replay failed: " + completed.stderr[-2000:]
        )
    try:
        return _strict_json_object(completed.stdout)
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise CleanCloneReproductionError(
            f"isolated {mode} replay returned invalid JSON"
        ) from exc


def _zero_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value == 0


def _validate_receipt_result(result: Mapping[str, Any]) -> None:
    targets = tuple(sorted(str(value) for value in result.get("target_ids") or ()))
    if not (
        result.get("schema_version") == VERIFICATION_SCHEMA
        and result.get("status") == VERIFICATION_PASS
        and result.get("offline") is True
        and _zero_int(result.get("critical_count_sum"))
        and result.get("target_count") == len(EXPECTED_TARGET_IDS)
        and targets == tuple(sorted(EXPECTED_TARGET_IDS))
    ):
        raise CleanCloneReproductionError("tracked receipt recomputation did not PASS")


def _stable_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _validate_readiness_result(
    result: Mapping[str, Any],
    *,
    receipt_result: Mapping[str, Any],
) -> None:
    targets = tuple(sorted(str(value) for value in result.get("target_ids") or ()))
    if not (
        result.get("schema_version") == TRACKED_READINESS_SCHEMA
        and result.get("status") == TRACKED_READINESS_PASS
        and result.get("ready") is True
        and result.get("offline") is True
        and result.get("production_readiness_authority") is False
        and _zero_int(result.get("critical_count"))
        and result.get("same_receipt_replay_variance") == 0
        and result.get("verification_status") == VERIFICATION_PASS
        and _zero_int(result.get("verification_critical_count_sum"))
        and result.get("receipt_verification_hash") == _stable_hash(receipt_result)
        and targets == tuple(sorted(EXPECTED_TARGET_IDS))
    ):
        raise CleanCloneReproductionError("tracked readiness replay did not PASS")


def _canonical_json_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _semantic_json_bytes(payload: object) -> bytes:
    return json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _download_pip_bootstrap(
    runtime_root: Path,
    *,
    opener: Callable[..., Any] = urllib_request.urlopen,
) -> Path:
    bootstrap_root = runtime_root / "pip-bootstrap"
    bootstrap_root.mkdir(mode=0o700)
    wheel = bootstrap_root / PIP_BOOTSTRAP_NAME
    temporary = bootstrap_root / f".{PIP_BOOTSTRAP_NAME}.{secrets.token_hex(16)}.tmp"
    digest = hashlib.sha256()
    byte_count = 0
    descriptor = os.open(
        temporary,
        os.O_WRONLY
        | os.O_CREAT
        | os.O_EXCL
        | getattr(os, "O_NOFOLLOW", 0),
        0o600,
    )
    try:
        with opener(PIP_BOOTSTRAP_URL, timeout=60) as response, os.fdopen(
            descriptor, "wb"
        ) as handle:
            descriptor = -1
            final_url = response.geturl()
            status = getattr(response, "status", 200)
            if final_url != PIP_BOOTSTRAP_URL or status != 200:
                raise CleanCloneReproductionError(
                    "pinned pip bootstrap download was redirected or rejected"
                )
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                byte_count += len(chunk)
                if byte_count > PIP_BOOTSTRAP_MAX_BYTES:
                    raise CleanCloneReproductionError(
                        "pinned pip bootstrap exceeds its size bound"
                    )
                digest.update(chunk)
                handle.write(chunk)
            handle.flush()
            os.fsync(handle.fileno())
        if byte_count <= 0 or digest.hexdigest() != PIP_BOOTSTRAP_SHA256:
            raise CleanCloneReproductionError(
                "pinned pip bootstrap SHA256 mismatch"
            )
        os.replace(temporary, wheel)
        directory_fd = os.open(bootstrap_root, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        return wheel
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def _pip_install_command(
    *,
    pip_wheel: Path,
    dependency_root: Path,
    lock: Path,
) -> list[str]:
    return [
        str(ISOLATED_PYTHON),
        "-I",
        "-S",
        "-B",
        "-X",
        "utf8",
        "-c",
        PIP_BOOTSTRAP_WORKER_SOURCE,
        str(pip_wheel),
        "install",
        "--require-hashes",
        "--no-deps",
        "--no-cache-dir",
        "--disable-pip-version-check",
        "--no-input",
        "--only-binary=:all:",
        "--index-url",
        "https://pypi.org/simple",
        "--target",
        str(dependency_root),
        "-r",
        str(lock),
    ]


def _dependency_tree_is_private(root: Path) -> bool:
    if root.is_symlink() or not root.is_dir():
        return False
    regular_count = 0
    try:
        for directory, directory_names, file_names in os.walk(
            root, topdown=True, followlinks=False
        ):
            parent = Path(directory)
            if any((parent / name).is_symlink() for name in directory_names):
                return False
            for name in file_names:
                path = parent / name
                if path.is_symlink() or not path.is_file() or path.stat().st_nlink != 1:
                    return False
                regular_count += 1
    except OSError:
        return False
    return regular_count > 0


def _install_test_dependencies(
    clone: Path,
    *,
    runtime_root: Path,
    env: Mapping[str, str],
    opener: Callable[..., Any] = urllib_request.urlopen,
) -> tuple[Path, Mapping[str, str]]:
    _assert_supported_isolated_platform(env)
    lock = _validate_dependency_lock(clone)
    expected_versions = _required_dependency_versions(lock)
    pip_wheel = _download_pip_bootstrap(runtime_root, opener=opener)
    dependency_root = runtime_root / "test-dependencies"
    dependency_root.mkdir(mode=0o700)
    completed = subprocess.run(
        _pip_install_command(
            pip_wheel=pip_wheel,
            dependency_root=dependency_root,
            lock=lock,
        ),
        cwd=clone,
        env=dict(env),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise CleanCloneReproductionError(
            "hashed clean-clone dependency install failed: "
            + (completed.stdout + "\n" + completed.stderr)[-3000:]
        )
    if not _dependency_tree_is_private(dependency_root):
        raise CleanCloneReproductionError(
            "installed dependency target contains a symlink or shared file"
        )
    return dependency_root, expected_versions


def _run_dependency_import_smoke(
    clone: Path,
    *,
    dependency_root: Path,
    expected_versions: Mapping[str, str],
    env: Mapping[str, str],
) -> Mapping[str, Any]:
    completed = subprocess.run(
        _isolated_python_command(
            worker_source=DEPENDENCY_SMOKE_WORKER_SOURCE,
            arguments=(
                str(clone / "src"),
                str(dependency_root),
                json.dumps(
                    dict(expected_versions),
                    ensure_ascii=False,
                    sort_keys=True,
                    allow_nan=False,
                ),
            ),
        ),
        cwd=clone,
        env=dict(env),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    try:
        result = _strict_json_object(completed.stdout)
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise CleanCloneReproductionError(
            "isolated dependency smoke returned invalid JSON"
        ) from exc
    rows = result.get("rows")
    if not (
        completed.returncode == 0
        and isinstance(rows, list)
        and len(rows) == len(expected_versions)
        and all(
            isinstance(row, Mapping)
            and row.get("error") is None
            and row.get("inside_dependency_root") is True
            and row.get("version") == expected_versions.get(str(row.get("module")))
            for row in rows
        )
    ):
        raise CleanCloneReproductionError(
            "isolated dependency import smoke failed: "
            + (completed.stdout + "\n" + completed.stderr)[-3000:]
        )
    return result


def _create_isolated_python_wrapper(
    runtime_root: Path,
    *,
    clone: Path,
    dependency_root: Path,
) -> Path:
    wrapper_root = runtime_root / "nested-python"
    wrapper_root.mkdir(mode=0o700)
    wrapper = wrapper_root / "python"
    command_arguments = (
        NESTED_PYTHON_WORKER_SOURCE,
        str(clone / "src"),
        str(clone),
        str(clone / "tests"),
        str(dependency_root),
    )
    command = " ".join(shlex.quote(value) for value in command_arguments)
    encoded = (
        "#!/bin/sh\n"
        + "exec /usr/bin/python3 -I -S -B -X utf8 -c "
        + command
        + ' "$0" "$@"\n'
    ).encode("utf-8")
    root_fd = os.open(wrapper_root, os.O_RDONLY | os.O_DIRECTORY)
    try:
        _write_new_file_at(root_fd, wrapper.name, encoded)
        os.chmod(wrapper.name, 0o700, dir_fd=root_fd, follow_symlinks=False)
        os.fsync(root_fd)
    finally:
        os.close(root_fd)
    if wrapper.is_symlink() or not wrapper.is_file() or wrapper.stat().st_nlink != 1:
        raise CleanCloneReproductionError("isolated nested Python wrapper is unsafe")
    return wrapper


def _run_full_test_suite(
    clone: Path,
    *,
    dependency_root: Path,
    python_wrapper: Path,
    env: Mapping[str, str],
) -> Mapping[str, Any]:
    completed = subprocess.run(
        _isolated_python_command(
            worker_source=FULL_TEST_WORKER_SOURCE,
            arguments=(
                str(clone / "src"),
                str(dependency_root),
                str(python_wrapper),
                "discover",
                "-s",
                "tests",
                "-v",
            ),
        ),
        cwd=clone,
        env=dict(env),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    transcript = completed.stdout + "\n" + completed.stderr
    summaries = tuple(_TEST_SUMMARY.finditer(transcript))
    executed = int(summaries[-1].group(1)) if summaries else 0
    tail = transcript[summaries[-1].end() :] if summaries else transcript
    if completed.returncode != 0 or executed <= 0 or not _TEST_OK.search(tail):
        raise CleanCloneReproductionError(
            "full unittest suite failed: " + transcript[-4000:]
        )
    return {
        "schema_version": CLEAN_CLONE_TEST_SCHEMA,
        "status": CLEAN_CLONE_TEST_PASS,
        "executed_test_count": executed,
        "failed_test_count": 0,
        "error_test_count": 0,
        "critical_count_sum": 0,
        "production_readiness_authority": False,
    }


def _validate_test_result(result: Mapping[str, Any]) -> None:
    if not (
        set(result) == _TEST_RESULT_KEYS
        and result.get("schema_version") == CLEAN_CLONE_TEST_SCHEMA
        and result.get("status") == CLEAN_CLONE_TEST_PASS
        and isinstance(result.get("executed_test_count"), int)
        and not isinstance(result.get("executed_test_count"), bool)
        and int(result["executed_test_count"]) > 0
        and all(
            _zero_int(result.get(key))
            for key in ("failed_test_count", "error_test_count", "critical_count_sum")
        )
        and result.get("production_readiness_authority") is False
    ):
        raise CleanCloneReproductionError("full unittest result contract is invalid")


def _open_existing_directory_no_symlinks(path: Path) -> int:
    absolute = path.absolute()
    descriptor = os.open(absolute.anchor, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in absolute.parts[1:]:
            if part in {"", ".", ".."}:
                raise CleanCloneReproductionError("unsafe directory component")
            child = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
                dir_fd=descriptor,
            )
            os.close(descriptor)
            descriptor = child
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _assert_pinned_directory(path: Path, descriptor: int) -> None:
    reopened = _open_existing_directory_no_symlinks(path)
    try:
        expected = os.fstat(descriptor)
        actual = os.fstat(reopened)
        if (expected.st_dev, expected.st_ino) != (actual.st_dev, actual.st_ino):
            raise CleanCloneReproductionError("published directory inode changed")
    finally:
        os.close(reopened)


def _entry_exists_at(parent_fd: int, name: str) -> bool:
    try:
        os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        return True
    except FileNotFoundError:
        return False


def _write_new_file_at(parent_fd: int, name: str, encoded: bytes) -> None:
    descriptor = os.open(
        name,
        os.O_WRONLY
        | os.O_CREAT
        | os.O_EXCL
        | getattr(os, "O_NOFOLLOW", 0),
        0o600,
        dir_fd=parent_fd,
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            descriptor = -1
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def _regular_file_bytes(path: Path) -> bytes | None:
    if path.is_symlink() or not path.is_file():
        return None
    try:
        if path.stat().st_nlink != 1:
            return None
        return path.read_bytes()
    except OSError:
        return None


def _reproduction_result(
    child_bytes: Mapping[str, bytes],
) -> Mapping[str, Any]:
    return {
        "schema_version": CLEAN_CLONE_REPRODUCTION_SCHEMA,
        "status": CLEAN_CLONE_REPRODUCTION_PASS,
        "as_of_date": CANARY_RECEIPT_DATE,
        "receipt_recompute_result_hash": hashlib.sha256(
            child_bytes["receipt_recompute_result.json"]
        ).hexdigest(),
        "tracked_readiness_result_hash": hashlib.sha256(
            child_bytes["tracked_readiness_result.json"]
        ).hexdigest(),
        "test_result_hash": hashlib.sha256(
            child_bytes["test_result.json"]
        ).hexdigest(),
        "critical_count_sum": 0,
        "production_readiness_authority": False,
    }


def _published_bundle_matches(
    repo_root: str | Path,
    *,
    expected_children: Mapping[str, bytes] | None = None,
    expected_result: Mapping[str, Any] | None = None,
) -> bool:
    raw_repo = Path(repo_root).absolute()
    if _path_or_parent_is_symlink(raw_repo):
        return False
    repo = raw_repo.resolve()
    final = repo / FINAL_ROOT_RELATIVE
    clean = final / CLEAN_CLONE_DIRECTORY_NAME
    if _path_or_parent_is_symlink(final) or _path_or_parent_is_symlink(clean):
        return False
    child_bytes = {
        name: _regular_file_bytes(clean / name) for name in CLEAN_CLONE_CHILD_NAMES
    }
    if any(value is None for value in child_bytes.values()):
        return False
    result_bytes = _regular_file_bytes(final / REPRODUCTION_RESULT_NAME)
    if result_bytes is None:
        return False
    try:
        children = {
            name: _strict_json_object(value.decode("utf-8"))
            for name, value in child_bytes.items()
            if value is not None
        }
        result = _strict_json_object(result_bytes.decode("utf-8"))
        _validate_receipt_result(children["receipt_recompute_result.json"])
        _validate_readiness_result(
            children["tracked_readiness_result.json"],
            receipt_result=children["receipt_recompute_result.json"],
        )
        _validate_test_result(children["test_result.json"])
    except (KeyError, UnicodeError, ValueError, CleanCloneReproductionError):
        return False
    if not (
        set(result) == _REPRODUCTION_RESULT_KEYS
        and result.get("schema_version") == CLEAN_CLONE_REPRODUCTION_SCHEMA
        and result.get("status") == CLEAN_CLONE_REPRODUCTION_PASS
        and result.get("as_of_date") == CANARY_RECEIPT_DATE
        and _zero_int(result.get("critical_count_sum"))
        and result.get("production_readiness_authority") is False
        and result.get("receipt_recompute_result_hash")
        == hashlib.sha256(child_bytes["receipt_recompute_result.json"] or b"").hexdigest()
        and result.get("tracked_readiness_result_hash")
        == hashlib.sha256(child_bytes["tracked_readiness_result.json"] or b"").hexdigest()
        and result.get("test_result_hash")
        == hashlib.sha256(child_bytes["test_result.json"] or b"").hexdigest()
    ):
        return False
    if expected_children is not None and any(
        child_bytes.get(name) != encoded for name, encoded in expected_children.items()
    ):
        return False
    return expected_result is None or dict(result) == dict(expected_result)


def _publish_artifacts(
    repo_root: str | Path,
    *,
    receipt_result: Mapping[str, Any],
    readiness_result: Mapping[str, Any],
    test_result: Mapping[str, Any],
    before_result_commit: Callable[[], None] | None = None,
) -> Mapping[str, Any]:
    _validate_receipt_result(receipt_result)
    _validate_readiness_result(readiness_result, receipt_result=receipt_result)
    _validate_test_result(test_result)
    repo = Path(repo_root).resolve()
    final = repo / FINAL_ROOT_RELATIVE
    children = {
        "receipt_recompute_result.json": _canonical_json_bytes(receipt_result),
        "tracked_readiness_result.json": _canonical_json_bytes(readiness_result),
        "test_result.json": _canonical_json_bytes(test_result),
    }
    result = _reproduction_result(children)
    result_bytes = _canonical_json_bytes(result)
    if _published_bundle_matches(
        repo, expected_children=children, expected_result=result
    ):
        return result

    final_fd = _open_existing_directory_no_symlinks(final)
    staging_name = f".clean-clone.{secrets.token_hex(16)}.staging"
    result_temporary_name = (
        f".{REPRODUCTION_RESULT_NAME}.{secrets.token_hex(16)}.tmp"
    )
    staging_fd = -1
    staging_created = False
    result_temporary_created = False
    directory_published = False
    result_published = False
    succeeded = False
    try:
        if _entry_exists_at(final_fd, CLEAN_CLONE_DIRECTORY_NAME) or _entry_exists_at(
            final_fd, REPRODUCTION_RESULT_NAME
        ):
            raise CleanCloneReproductionError(
                "canonical clean-clone artifacts already exist with different bytes"
            )
        os.mkdir(staging_name, mode=0o700, dir_fd=final_fd)
        staging_created = True
        staging_fd = os.open(
            staging_name,
            os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=final_fd,
        )
        for name in CLEAN_CLONE_CHILD_NAMES:
            _write_new_file_at(staging_fd, name, children[name])
        os.fsync(staging_fd)
        _write_new_file_at(final_fd, result_temporary_name, result_bytes)
        result_temporary_created = True
        _assert_pinned_directory(final, final_fd)
        if _entry_exists_at(final_fd, CLEAN_CLONE_DIRECTORY_NAME) or _entry_exists_at(
            final_fd, REPRODUCTION_RESULT_NAME
        ):
            raise CleanCloneReproductionError(
                "canonical clean-clone destination changed before publish"
            )
        os.rename(
            staging_name,
            CLEAN_CLONE_DIRECTORY_NAME,
            src_dir_fd=final_fd,
            dst_dir_fd=final_fd,
        )
        directory_published = True
        os.fsync(final_fd)
        if before_result_commit is not None:
            before_result_commit()
        _assert_pinned_directory(final, final_fd)
        _assert_pinned_directory(final / CLEAN_CLONE_DIRECTORY_NAME, staging_fd)
        os.replace(
            result_temporary_name,
            REPRODUCTION_RESULT_NAME,
            src_dir_fd=final_fd,
            dst_dir_fd=final_fd,
        )
        result_published = True
        os.fsync(final_fd)
        _assert_pinned_directory(final, final_fd)
        if not _published_bundle_matches(
            repo, expected_children=children, expected_result=result
        ):
            raise CleanCloneReproductionError(
                "published clean-clone bundle failed raw-hash verification"
            )
        succeeded = True
        return result
    finally:
        if not succeeded:
            if result_temporary_created:
                try:
                    os.unlink(result_temporary_name, dir_fd=final_fd)
                except FileNotFoundError:
                    pass
            if result_published:
                try:
                    os.unlink(REPRODUCTION_RESULT_NAME, dir_fd=final_fd)
                except FileNotFoundError:
                    pass
            if staging_fd >= 0:
                for name in CLEAN_CLONE_CHILD_NAMES:
                    try:
                        os.unlink(name, dir_fd=staging_fd)
                    except FileNotFoundError:
                        pass
            if staging_created:
                try:
                    os.rmdir(
                        CLEAN_CLONE_DIRECTORY_NAME
                        if directory_published
                        else staging_name,
                        dir_fd=final_fd,
                    )
                except FileNotFoundError:
                    pass
        if staging_fd >= 0:
            os.close(staging_fd)
        if result_temporary_created:
            try:
                os.unlink(result_temporary_name, dir_fd=final_fd)
            except FileNotFoundError:
                pass
        if staging_created and not directory_published:
            try:
                os.rmdir(staging_name, dir_fd=final_fd)
            except FileNotFoundError:
                pass
        os.close(final_fd)


def produce_clean_clone_reproduction(repo_root: str | Path) -> Mapping[str, Any]:
    raw_repo = Path(repo_root).absolute()
    with tempfile.TemporaryDirectory(prefix="e2r-v6-clean-clone-") as directory:
        runtime_root = Path(directory)
        env = _sanitized_environment(runtime_root)
        final_sha = _trusted_source_head(raw_repo, env)
        clone = _clone_origin_main(
            scratch_root=runtime_root,
            expected_sha=final_sha,
            env=env,
        )
        _validate_clean_clone(clone, expected_sha=final_sha, env=env)

        receipt = _run_replay_worker(clone, mode="receipt", env=env)
        _validate_receipt_result(receipt)
        _validate_clean_clone(clone, expected_sha=final_sha, env=env)

        readiness_first = _run_replay_worker(clone, mode="readiness", env=env)
        _validate_readiness_result(readiness_first, receipt_result=receipt)
        _validate_clean_clone(clone, expected_sha=final_sha, env=env)

        readiness_second = _run_replay_worker(clone, mode="readiness", env=env)
        _validate_readiness_result(readiness_second, receipt_result=receipt)
        if _semantic_json_bytes(readiness_first) != _semantic_json_bytes(readiness_second):
            raise CleanCloneReproductionError(
                "two independent tracked-readiness replays diverged"
            )
        _validate_clean_clone(clone, expected_sha=final_sha, env=env)

        dependency_root, expected_versions = _install_test_dependencies(
            clone,
            runtime_root=runtime_root,
            env=env,
        )
        _run_dependency_import_smoke(
            clone,
            dependency_root=dependency_root,
            expected_versions=expected_versions,
            env=env,
        )
        python_wrapper = _create_isolated_python_wrapper(
            runtime_root,
            clone=clone,
            dependency_root=dependency_root,
        )
        _validate_clean_clone(clone, expected_sha=final_sha, env=env)
        test_result = _run_full_test_suite(
            clone,
            dependency_root=dependency_root,
            python_wrapper=python_wrapper,
            env=env,
        )
        _validate_test_result(test_result)
        _validate_clean_clone(clone, expected_sha=final_sha, env=env)
        if _trusted_source_head(raw_repo, env) != final_sha:
            raise CleanCloneReproductionError(
                "source repository identity changed during clean-clone replay"
            )
        return _publish_artifacts(
            raw_repo,
            receipt_result=receipt,
            readiness_result=readiness_first,
            test_result=test_result,
        )


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = produce_clean_clone_reproduction(args.repo_root)
    except (CleanCloneReproductionError, OSError, subprocess.SubprocessError) as exc:
        print(
            "E2R_V6_CLEAN_CLONE_REPRODUCTION_FAIL: " + str(exc),
            file=sys.stderr,
        )
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
