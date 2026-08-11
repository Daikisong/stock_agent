"""Deterministic static audit for the canonical E2R v6 production surface.

The audit starts from an exact roster of production CLI entrypoints, follows
only local ``e2r`` imports, discovers referenced production configuration
files, and hashes every scanned file.  Findings are recomputed from Python AST
and parsed configuration values; a caller supplied count is never trusted.

The scanner deliberately distinguishes executable production constructs from
audit/denylist vocabulary.  Merely naming a prohibited provider in an audit
constant is not a runtime provider route, while importing or constructing such
a provider is.
"""

from __future__ import annotations

import ast
from collections import defaultdict
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from typing import Any, Iterable, Mapping, Sequence

from e2r.production.metadata import stable_hash


PRODUCTION_STATIC_AUDIT_SCHEMA = "e2r_v6_production_static_audit_v1"
PRODUCTION_STATIC_AUDIT_PASS = "E2R_V6_PRODUCTION_STATIC_AUDIT_PASS"
PRODUCTION_STATIC_AUDIT_FAIL = "E2R_V6_PRODUCTION_STATIC_AUDIT_FAIL"
PRODUCTION_STATIC_AUDIT_LEAF = "production_static_audit.json"
SCANNER_VERSION = "E2R_V6_PRODUCTION_AST_DATAFLOW_STATIC_AUDIT_V1"

# This is the non-negotiable production surface.  Test mode may replace it to
# exercise individual detectors, but production callers cannot shrink it.
CANONICAL_PRODUCTION_ENTRYPOINTS = (
    "src/e2r/cli/compile_e2r_v6_artifact_lifecycle.py",
    "src/e2r/cli/compile_e2r_v6_cross_archetype_canaries.py",
    "src/e2r/cli/compile_e2r_v6_current_krx_census.py",
    "src/e2r/cli/compile_e2r_v6_operational_self_repair.py",
    "src/e2r/cli/compile_e2r_v6_production_static_audit.py",
    "src/e2r/cli/compile_e2r_v6_provider_runtime_audit.py",
    "src/e2r/cli/compile_e2r_v6_tracked_readiness.py",
    "src/e2r/cli/export_e2r_v6_tracked_receipts.py",
    "src/e2r/cli/materialize_e2r_v6_issuer_business_profiles.py",
    "src/e2r/cli/publish_e2r_v6_operational_cutover.py",
    "src/e2r/cli/run_e2r_census_mode.py",
    "src/e2r/cli/run_e2r_current_operation.py",
    "src/e2r/cli/run_e2r_researcher_mode_until_pass.py",
    "src/e2r/cli/run_e2r_v6_current_krx_deep_receipts_until_pass.py",
    "src/e2r/cli/run_e2r_v6_current_live_canaries_until_pass.py",
    "src/e2r/cli/run_e2r_v6_operational_acceptance_until_pass.py",
    "src/e2r/cli/run_e2r_v6_selected_source_tasks.py",
    "src/e2r/cli/select_e2r_v6_cross_archetype_canaries.py",
    "src/e2r/cli/verify_e2r_v6_operational_cutover_publication.py",
    "src/e2r/cli/verify_e2r_v6_tracked_receipts.py",
)
# Shell helpers, dependency locks, and CI workflows are not Python imports, so
# they have an explicit extensible roster.  A future v6 workflow must be added
# here in the same change that makes it canonical; a missing listed path is a
# hard failure rather than an implicitly skipped optional check.
CANONICAL_PRODUCTION_AUXILIARY_PATHS = (
    ".github/workflows/e2r_v6_operational_cutover_verify.yml",
    "requirements/e2r_v6_clean_clone_py310_linux_x86_64.lock",
    "scripts/run_e2r_v6_clean_clone_reproduction.py",
    "scripts/verify_e2r_v6_tracked_readiness.py",
)
CANONICAL_PRODUCTION_CONFIGS = (
    "configs/e2r_census_selective_deep_v1.json",
    "configs/e2r_issuer_official_domains_v1.json",
    "configs/e2r_live_materialization_v1.json",
    "configs/e2r_production_daily_v1.json",
    "configs/e2r_targeted_live_smoke_v1.json",
)

TARGET_CONDITIONED_BRANCH = "target_conditioned_branch_count"
FIXED_EXPECTED_SCORE = "fixed_expected_score_count"
FIXED_EXPECTED_STAGE = "fixed_expected_stage_count"
GOLD_PRODUCTION_INPUT = "gold_production_input_count"
AUTOMATIC_LOCAL_FALLBACK = "automatic_local_fallback_count"
EXECUTABLE_LOCAL_PROVIDER = "executable_local_provider_count"
ABSOLUTE_REVIEWER_IDENTITY = "absolute_reviewer_path_identity_count"
SECRET_LITERAL = "secret_literal_count"
OUTPUT_ONLY_READINESS = "output_only_readiness_dependency_count"

REQUIRED_ZERO_COUNT_KEYS = (
    TARGET_CONDITIONED_BRANCH,
    FIXED_EXPECTED_SCORE,
    FIXED_EXPECTED_STAGE,
    GOLD_PRODUCTION_INPUT,
    AUTOMATIC_LOCAL_FALLBACK,
    EXECUTABLE_LOCAL_PROVIDER,
    ABSOLUTE_REVIEWER_IDENTITY,
    SECRET_LITERAL,
    OUTPUT_ONLY_READINESS,
)

_INTEGRITY_COUNT_KEYS = (
    "missing_scope_path_count",
    "scope_symlink_count",
    "unreadable_scope_file_count",
    "python_syntax_error_count",
    "invalid_config_count",
    "unresolved_local_import_count",
)
_AUDIT_KEYS = frozenset(
    {
        "all_required_counts_recomputed",
        "all_required_counts_zero",
        "audit_hash",
        "auxiliary_path_count",
        "caller_attestation_trusted",
        "config_path_count",
        "critical_count_sum",
        "critical_counts",
        "file_roster",
        "file_roster_hash",
        "findings",
        "integrity_findings",
        "production_readiness_authority",
        "scanner_version",
        "schema_version",
        "score_or_stage_authority",
        "scanned_file_count",
        "scope_definition",
        "scope_definition_hash",
        "source_path_count",
        "status",
        "test_mode",
        "unresolved_local_imports",
    }
)

_TARGET_IDENTIFIERS = frozenset(
    {
        "company_name",
        "corp_code",
        "corp_name",
        "issuer_id",
        "issuer_name",
        "stock_code",
        "symbol",
        "target_id",
        "target_name",
        "ticker",
    }
)
_SCORE_FIELDS = frozenset(
    {
        "expected_score",
        "expected_total_score",
        "fixed_score",
        "fixed_total_score",
        "gold_score",
        "gold_total_score",
    }
)
_STAGE_FIELDS = frozenset(
    {
        "expected_canonical_stage",
        "expected_stage",
        "fixed_canonical_stage",
        "fixed_stage",
        "gold_canonical_stage",
        "gold_stage",
    }
)
_INPUT_FIELD_MARKERS = (
    "corpus",
    "document",
    "evidence",
    "input",
    "path",
    "query",
    "source",
)
_NON_INPUT_CONTEXT_MARKERS = (
    "audit",
    "blocked",
    "comparison",
    "count",
    "deny",
    "disallowed",
    "failure",
    "file",
    "forbidden",
    "missed",
    "output",
    "prohibited",
    "result",
    "status",
    "visibility",
)
_LOCAL_PROVIDER_MARKERS = (
    "llama_cpp",
    "llamacpp",
    "lm_studio",
    "lmstudio",
    "ollama",
    "qwen",
)
_EXECUTABLE_LOCAL_ROUTE_MARKERS = (
    *_LOCAL_PROVIDER_MARKERS,
    "local_llm",
    "local_model",
    "local_provider",
    "localprovider",
)
_AUDIT_REFERENCE_MARKERS = (
    "audit",
    "contains",
    "deny",
    "detect",
    "forbid",
    "marker",
    "scan",
    "validate",
    "verify",
)
_FALLBACK_FIELDS = frozenset(
    {
        "automatic_local_fallback",
        "fallback_model",
        "fallback_provider",
        "local_fallback",
        "local_provider_fallback",
    }
)
_REVIEWER_FIELDS = frozenset(
    {
        "reviewer",
        "reviewer_id",
        "reviewer_identity",
        "reviewer_name",
    }
)
_SECRET_FIELDS = frozenset(
    {
        "access_token",
        "api_key",
        "apikey",
        "client_secret",
        "credential",
        "credentials",
        "password",
        "private_key",
        "secret",
        "secret_key",
        "token",
    }
)
_READINESS_FIELDS = frozenset(
    {
        "acceptance_pass",
        "operational_ready",
        "production_ready",
        "ready",
        "readiness",
    }
)
_ABSOLUTE_PATH = re.compile(
    r"(?:^|[\s\"'=:(])/(?:home|mnt|root|tmp)(?:/|\b)|(?:^|[\s\"'=:(])[A-Za-z]:[\\/]"
)
_CONFIG_LITERAL = re.compile(
    r"\Aconfigs/[A-Za-z0-9_./-]+\.(?:json|jsonl|ya?ml)\Z"
)
_AUXILIARY_LITERAL = re.compile(
    r"\A(?:\.github/workflows|requirements|scripts)/[A-Za-z0-9_./-]+"
    r"\.(?:bash|in|json|lock|py|sh|txt|ya?ml)\Z"
)
_ENV_NAME = re.compile(r"[A-Z][A-Z0-9_]{2,}\Z")
_CANONICAL_STAGE = re.compile(
    r"(?:0|1|2|3-(?:Green|Yellow|Red)|4A|4B|4C|5)\Z"
)


def _normalize_relative(value: str | Path) -> str | None:
    raw = Path(value).as_posix()
    path = PurePosixPath(raw)
    if (
        not raw
        or path.is_absolute()
        or raw != path.as_posix()
        or any(part in {"", ".", ".."} for part in path.parts)
    ):
        return None
    return raw


def _has_symlink(repo: Path, relative: str) -> bool:
    current = repo
    for part in PurePosixPath(relative).parts:
        current /= part
        if current.is_symlink():
            return True
    return False


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _module_name(relative: str) -> str | None:
    prefix = "src/"
    if not relative.startswith(prefix) or not relative.endswith(".py"):
        return None
    module = relative[len(prefix) : -3].replace("/", ".")
    if module.endswith(".__init__"):
        module = module[: -len(".__init__")]
    return module if module.startswith("e2r") else None


def _module_path(repo: Path, module: str) -> str | None:
    if not module.startswith("e2r"):
        return None
    stem = module.replace(".", "/")
    choices = (f"src/{stem}.py", f"src/{stem}/__init__.py")
    for relative in choices:
        if (repo / relative).is_file():
            return relative
    return None


def _package_initializer_paths(repo: Path, relative: str) -> tuple[str, ...]:
    path = PurePosixPath(relative)
    if len(path.parts) < 3 or path.parts[:2] != ("src", "e2r"):
        return ()
    result: list[str] = []
    for stop in range(2, len(path.parts)):
        candidate = PurePosixPath(*path.parts[:stop], "__init__.py").as_posix()
        if (repo / candidate).is_file():
            result.append(candidate)
    return tuple(result)


def _local_import_modules(
    tree: ast.AST,
    *,
    module: str | None,
    is_package: bool,
) -> tuple[tuple[str, bool], ...]:
    imports: dict[str, bool] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("e2r"):
                    imports[alias.name] = True
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0:
                resolved = node.module or ""
            elif module:
                base = module.split(".") if is_package else module.split(".")[:-1]
                climb = max(0, node.level - 1)
                if climb:
                    base = base[:-climb]
                if node.module:
                    base.extend(node.module.split("."))
                resolved = ".".join(base)
            else:
                resolved = ""
            if resolved.startswith("e2r"):
                imports[resolved] = True
                for alias in node.names:
                    if alias.name != "*":
                        imports.setdefault(f"{resolved}.{alias.name}", False)
    return tuple(sorted(imports.items()))


def _literal_value(node: ast.AST, constants: Mapping[str, Any] | None = None) -> Any:
    constants = constants or {}
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name) and node.id in constants:
        return constants[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        operand = _literal_value(node.operand, constants)
        if isinstance(operand, (int, float)) and not isinstance(operand, bool):
            return operand if isinstance(node.op, ast.UAdd) else -operand
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        values = [_literal_value(item, constants) for item in node.elts]
        if all(value is not _MISSING for value in values):
            return tuple(values)
    if isinstance(node, ast.Dict):
        keys = [_literal_value(item, constants) for item in node.keys]
        values = [_literal_value(item, constants) for item in node.values]
        if all(value is not _MISSING for value in (*keys, *values)):
            return dict(zip(keys, values))
    if isinstance(node, ast.JoinedStr):
        pieces: list[str] = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                pieces.append(value.value)
            else:
                pieces.append("{dynamic}")
        return "".join(pieces)
    return _MISSING


_MISSING = object()


def _field_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id.casefold()
    if isinstance(node, ast.Attribute):
        return node.attr.casefold()
    if isinstance(node, ast.Subscript):
        value = _literal_value(node.slice)
        return value.casefold() if isinstance(value, str) else None
    return None


def _qualified_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _qualified_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def _contains_marker(value: str, markers: Iterable[str]) -> bool:
    normalized = value.casefold().replace("-", "_").replace(" ", "_")
    return any(marker in normalized for marker in markers)


def _is_executable_local_reference(value: str) -> bool:
    normalized = value.casefold().replace("-", "_").replace(" ", "_")
    leaf = normalized.rsplit(".", 1)[-1]
    if leaf.startswith(("_is_", "is_")) or any(
        marker in normalized for marker in _AUDIT_REFERENCE_MARKERS
    ):
        return False
    if any(marker in normalized for marker in _LOCAL_PROVIDER_MARKERS):
        return True
    return any(
        marker in normalized
        for marker in ("local_llm", "local_model", "local_provider", "localprovider")
    ) and any(
        action in normalized
        for action in ("client", "provider", "runtime", "transport", "generate", "chat")
    )


def _is_local_provider_value(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    normalized = value.casefold().replace("-", "_").replace(" ", "_")
    return normalized in {
        "local",
        "local_llm",
        "local_model",
        "local_provider",
    } or _contains_marker(normalized, _LOCAL_PROVIDER_MARKERS)


def _is_loopback_endpoint(value: Any) -> bool:
    return isinstance(value, str) and bool(
        re.search(
            r"(?i)https?://(?:127\.0\.0\.1|localhost|\[::1\])(?::\d+)?(?:/|\Z)",
            value,
        )
    )


def _is_concrete_literal(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return True
    if isinstance(value, tuple):
        return bool(value) and all(_is_concrete_literal(item) for item in value)
    return False


def _target_specific_literal(field: str, value: Any, *, affix: bool = False) -> bool:
    if isinstance(value, Mapping):
        return any(
            _target_specific_literal(field, item, affix=affix)
            for item in value
        )
    if isinstance(value, tuple):
        return any(_target_specific_literal(field, item, affix=affix) for item in value)
    if not isinstance(value, str) or not value.strip():
        return False
    normalized = value.strip()
    if field in {"symbol", "stock_code", "ticker", "target_id", "issuer_id", "corp_code"}:
        return len(normalized) >= 4
    # A one-character suffix such as the Korean preferred-share marker is an
    # instrument-type rule, not a hardcoded company identity.
    return len(normalized) >= (3 if affix else 2)


def _target_literal_compare(node: ast.AST, constants: Mapping[str, Any]) -> bool:
    if isinstance(node, ast.Compare):
        operands = (node.left, *node.comparators)
        for left, right in zip(operands, operands[1:]):
            left_field = _field_name(left)
            right_field = _field_name(right)
            left_value = _literal_value(left, constants)
            right_value = _literal_value(right, constants)
            if (
                left_field in _TARGET_IDENTIFIERS
                and right_value is not _MISSING
                and _target_specific_literal(left_field, right_value)
            ) or (
                right_field in _TARGET_IDENTIFIERS
                and left_value is not _MISSING
                and _target_specific_literal(right_field, left_value)
            ):
                return True
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
        if (
            node.func.attr in {"endswith", "startswith"}
            and _field_name(node.func.value) in _TARGET_IDENTIFIERS
            and any(
                _target_specific_literal(
                    str(_field_name(node.func.value)),
                    _literal_value(arg, constants),
                    affix=True,
                )
                for arg in node.args
            )
        ):
            return True
    return any(
        _target_literal_compare(child, constants)
        for child in ast.iter_child_nodes(node)
    )


def _truthy_literal(value: Any) -> bool:
    return value is True or (
        isinstance(value, (str, int, float))
        and not isinstance(value, bool)
        and bool(value)
    )


def _is_secret_literal(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    normalized = value.strip()
    if (
        normalized.casefold() in {"none", "placeholder", "redacted", "unset"}
        or "{dynamic}" in normalized
        or normalized.startswith(("${", "env:", "ENV[", "<"))
        or _ENV_NAME.fullmatch(normalized)
    ):
        return False
    return True


def _is_secret_field(field: str) -> bool:
    normalized = field.casefold().replace("-", "_")
    return normalized in _SECRET_FIELDS or any(
        normalized.endswith(f"_{suffix}")
        for suffix in (
            "access_token",
            "api_key",
            "client_secret",
            "credential",
            "credentials",
            "password",
            "private_key",
            "secret_key",
            "token",
        )
    )


def _is_reviewer_field(field: str) -> bool:
    normalized = field.casefold().replace("-", "_")
    return normalized in _REVIEWER_FIELDS or (
        normalized.startswith("reviewer_")
        and normalized.endswith(("_id", "_identity", "_name", "_path"))
    )


def _is_expected_score_field(field: str) -> bool:
    normalized = field.casefold().replace("-", "_")
    return normalized in _SCORE_FIELDS or (
        normalized.startswith(("expected_", "fixed_", "gold_"))
        and normalized.endswith("score")
    )


def _is_expected_stage_field(field: str) -> bool:
    normalized = field.casefold().replace("-", "_")
    return normalized in _STAGE_FIELDS or (
        normalized.startswith(("expected_", "fixed_", "gold_"))
        and normalized.endswith("stage")
    )


def _is_absolute_identity(value: Any) -> bool:
    return isinstance(value, str) and bool(_ABSOLUTE_PATH.search(value))


def _is_gold_input(field: str, value: Any) -> bool:
    if not isinstance(value, str) or "gold" not in value.casefold():
        return False
    normalized = field.casefold()
    if value.casefold().endswith("_count"):
        return False
    if any(marker in normalized for marker in _NON_INPUT_CONTEXT_MARKERS):
        return False
    return (
        "gold" in normalized
        and any(marker in normalized for marker in _INPUT_FIELD_MARKERS)
    ) or (
        "production" in normalized
        and any(marker in normalized for marker in (*_INPUT_FIELD_MARKERS, "fact"))
        and any(token in value.casefold() for token in ("gold/", "gold_", "gold:", "gold."))
    )


def _iter_literal_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, Mapping):
        for item in value.values():
            yield from _iter_literal_strings(item)
    elif isinstance(value, (tuple, list, set)):
        for item in value:
            yield from _iter_literal_strings(item)


def _positive_readiness(node: ast.AST, constants: Mapping[str, Any]) -> bool:
    if isinstance(node, ast.Return):
        value = _literal_value(node.value, constants) if node.value else None
        return value is True or (
            isinstance(value, str) and value.upper().endswith("PASS")
        )
    if isinstance(node, (ast.Assign, ast.AnnAssign)):
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        value_node = node.value
        value = _literal_value(value_node, constants) if value_node else None
        return any(_field_name(target) in _READINESS_FIELDS for target in targets) and (
            value is True or isinstance(value, str) and value.upper().endswith("PASS")
        )
    return False


def _output_path_expression(node: ast.AST, constants: Mapping[str, Any]) -> bool:
    value = _literal_value(node, constants)
    if isinstance(value, str):
        normalized = value.replace("\\", "/").casefold()
        return normalized == "output" or normalized.startswith("output/")
    field = _field_name(node)
    if field and (
        field in {"output", "output_dir", "output_path", "output_root"}
        or field.startswith("output_")
    ):
        return True
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        return _output_path_expression(node.left, constants)
    if isinstance(node, ast.Call):
        qualified = _qualified_name(node.func).casefold()
        if qualified in {"path", "pathlib.path"} and node.args:
            return _output_path_expression(node.args[0], constants)
        if isinstance(node.func, ast.Attribute) and node.func.attr in {"resolve", "absolute"}:
            return _output_path_expression(node.func.value, constants)
    return False


def _readiness_signals(
    node: ast.AST,
    constants: Mapping[str, Any],
    aliases: Mapping[str, frozenset[str]],
) -> frozenset[str]:
    if isinstance(node, ast.Name) and node.id in aliases:
        return aliases[node.id]
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"exists", "is_dir", "is_file"}
        and _output_path_expression(node.func.value, constants)
    ):
        return frozenset({"OUTPUT_EXISTENCE"})
    children = tuple(ast.iter_child_nodes(node))
    if not children:
        return frozenset({"OTHER"})
    signals: set[str] = set()
    for child in children:
        signals.update(_readiness_signals(child, constants, aliases))
    return frozenset(signals or {"OTHER"})


class _PythonScanner(ast.NodeVisitor):
    def __init__(self, relative_path: str, tree: ast.AST) -> None:
        self.relative_path = relative_path
        self.tree = tree
        self.constants: dict[str, Any] = {}
        self.condition_aliases: set[str] = set()
        self.target_dispatch_maps: set[str] = set()
        self.readiness_aliases: dict[str, frozenset[str]] = {}
        self.findings: list[dict[str, Any]] = []
        self._collect_aliases()

    def _collect_aliases(self) -> None:
        assignments = [
            node
            for node in ast.walk(self.tree)
            if isinstance(node, (ast.Assign, ast.AnnAssign))
        ]
        for node in assignments:
            targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
            value_node = node.value
            if value_node is None:
                continue
            value = _literal_value(value_node, self.constants)
            for target in targets:
                if (
                    isinstance(target, ast.Name)
                    and target.id.isupper()
                    and value is not _MISSING
                ):
                    self.constants[target.id] = value
                if isinstance(target, ast.Name) and isinstance(value_node, ast.Dict):
                    keys = [
                        _literal_value(key, self.constants)
                        for key in value_node.keys
                    ]
                    if any(
                        isinstance(key, str) and len(key.strip()) >= 4
                        for key in keys
                    ):
                        self.target_dispatch_maps.add(target.id)
        for _iteration in range(max(1, len(assignments) + 1)):
            next_aliases: dict[str, frozenset[str]] = {}
            for node in assignments:
                targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
                value_node = node.value
                if value_node is None:
                    continue
                target_names = [target.id for target in targets if isinstance(target, ast.Name)]
                if _target_literal_compare(value_node, self.constants):
                    for name in target_names:
                        if name not in self.condition_aliases:
                            self.condition_aliases.add(name)
                            changed = True
                signals = _readiness_signals(
                    value_node,
                    self.constants,
                    self.readiness_aliases,
                )
                for name in target_names:
                    next_aliases[name] = frozenset(
                        set(next_aliases.get(name, frozenset())) | set(signals)
                    )
            if next_aliases == self.readiness_aliases:
                break
            self.readiness_aliases = next_aliases

    def _add(self, finding_class: str, node: ast.AST, rule: str) -> None:
        self.findings.append(
            {
                "finding_class": finding_class,
                "path": self.relative_path,
                "line": int(getattr(node, "lineno", 0) or 0),
                "column": int(getattr(node, "col_offset", 0) or 0),
                "rule": rule,
            }
        )

    def _field_value(self, field: str | None, value_node: ast.AST, node: ast.AST) -> None:
        if not field:
            return
        value = _literal_value(value_node, self.constants)
        if _is_expected_score_field(field) and isinstance(value, (int, float)) and not isinstance(value, bool):
            self._add(FIXED_EXPECTED_SCORE, node, "FIXED_EXPECTED_SCORE_LITERAL")
        if _is_expected_stage_field(field) and isinstance(value, str) and _CANONICAL_STAGE.fullmatch(value):
            self._add(FIXED_EXPECTED_STAGE, node, "FIXED_EXPECTED_STAGE_LITERAL")
        if value is not _MISSING:
            for literal in _iter_literal_strings(value):
                if _is_gold_input(field, literal):
                    self._add(GOLD_PRODUCTION_INPUT, node, "GOLD_VALUE_WIRED_TO_PRODUCTION_INPUT")
                    break
        local_toggle_enabled = value is True or (
            isinstance(value, str)
            and value.casefold() in {"enabled", "on", "true", "yes"}
        )
        if field in _FALLBACK_FIELDS and (
            (
                field in {"automatic_local_fallback", "local_fallback", "local_provider_fallback"}
                and local_toggle_enabled
            )
            or _is_local_provider_value(value)
        ):
            self._add(AUTOMATIC_LOCAL_FALLBACK, node, "AUTOMATIC_LOCAL_FALLBACK_ENABLED")
        if field in {"client", "model", "provider", "provider_name", "runtime", "transport"} and _is_local_provider_value(value):
            self._add(EXECUTABLE_LOCAL_PROVIDER, node, "LOCAL_PROVIDER_SELECTED")
        if field in {"base_url", "endpoint", "provider_endpoint", "provider_url"} and _is_loopback_endpoint(value):
            self._add(EXECUTABLE_LOCAL_PROVIDER, node, "LOOPBACK_PROVIDER_ENDPOINT")
        if _is_reviewer_field(field) and _is_absolute_identity(value):
            self._add(ABSOLUTE_REVIEWER_IDENTITY, node, "ABSOLUTE_REVIEWER_IDENTITY_LITERAL")
        if _is_secret_field(field) and _is_secret_literal(value):
            self._add(SECRET_LITERAL, node, "SECRET_LITERAL_IN_PRODUCTION_FIELD")
        if field in _READINESS_FIELDS:
            signals = _readiness_signals(
                value_node,
                self.constants,
                self.readiness_aliases,
            )
            if signals == frozenset({"OUTPUT_EXISTENCE"}):
                self._add(OUTPUT_ONLY_READINESS, node, "READINESS_ASSIGNED_FROM_OUTPUT_EXISTENCE_ONLY")

    def visit_Assign(self, node: ast.Assign) -> None:
        for target in node.targets:
            self._field_value(_field_name(target), node.value, node)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if node.value is not None:
            self._field_value(_field_name(node.target), node.value, node)
        self.generic_visit(node)

    def visit_Dict(self, node: ast.Dict) -> None:
        for key_node, value_node in zip(node.keys, node.values):
            key = _literal_value(key_node, self.constants)
            if isinstance(key, str):
                self._field_value(key.casefold(), value_node, node)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        for keyword in node.keywords:
            if keyword.arg:
                self._field_value(keyword.arg.casefold(), keyword.value, node)
        qualified = _qualified_name(node.func).casefold().replace("-", "_")
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr in {"get", "pop", "setdefault"}
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id in self.target_dispatch_maps
            and node.args
            and _field_name(node.args[0]) in _TARGET_IDENTIFIERS
        ):
            self._add(
                TARGET_CONDITIONED_BRANCH,
                node,
                "TARGET_LITERAL_MAP_CONTROLS_DISPATCH",
            )
        executable_name = _is_executable_local_reference(qualified)
        provider_action = any(
            token in qualified
            for token in ("client", "provider", "runtime", "transport", "generate", "chat", "pull")
        )
        if executable_name and provider_action:
            self._add(EXECUTABLE_LOCAL_PROVIDER, node, "LOCAL_PROVIDER_CALL")
        if qualified in {"subprocess.call", "subprocess.check_call", "subprocess.check_output", "subprocess.popen", "subprocess.run"}:
            literal = _literal_value(node.args[0], self.constants) if node.args else _MISSING
            if literal is not _MISSING and any(
                _contains_marker(value, _EXECUTABLE_LOCAL_ROUTE_MARKERS)
                for value in _iter_literal_strings(literal)
            ):
                self._add(EXECUTABLE_LOCAL_PROVIDER, node, "LOCAL_PROVIDER_SUBPROCESS")
        for keyword in node.keywords:
            if keyword.arg and keyword.arg.casefold() in {
                "base_url",
                "endpoint",
                "provider_endpoint",
                "provider_url",
            }:
                value = _literal_value(keyword.value, self.constants)
                if _is_loopback_endpoint(value):
                    self._add(EXECUTABLE_LOCAL_PROVIDER, node, "LOOPBACK_PROVIDER_ENDPOINT")
        if node.args and qualified in {"open", "path", "pathlib.path"}:
            value = _literal_value(node.args[0], self.constants)
            if isinstance(value, str) and _is_gold_input("input_path", value):
                self._add(GOLD_PRODUCTION_INPUT, node, "GOLD_PATH_OPENED_AS_PRODUCTION_INPUT")
        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> None:
        if (
            isinstance(node.value, ast.Name)
            and node.value.id in self.target_dispatch_maps
            and _field_name(node.slice) in _TARGET_IDENTIFIERS
        ):
            self._add(
                TARGET_CONDITIONED_BRANCH,
                node,
                "TARGET_LITERAL_MAP_CONTROLS_SUBSCRIPT",
            )
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            if _is_executable_local_reference(alias.name):
                self._add(EXECUTABLE_LOCAL_PROVIDER, node, "LOCAL_PROVIDER_IMPORT")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        names = (node.module or "", *(alias.name for alias in node.names))
        if any(_is_executable_local_reference(name) for name in names):
            self._add(EXECUTABLE_LOCAL_PROVIDER, node, "LOCAL_PROVIDER_IMPORT")
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        normalized = node.name.casefold().replace("-", "_")
        if _is_executable_local_reference(normalized) and any(
            marker in normalized for marker in ("client", "provider", "runtime", "transport")
        ):
            self._add(EXECUTABLE_LOCAL_PROVIDER, node, "EXECUTABLE_LOCAL_PROVIDER_CLASS")
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        positional = (*node.args.posonlyargs, *node.args.args)
        defaults = node.args.defaults
        for argument, default in zip(positional[-len(defaults) :], defaults):
            self._field_value(argument.arg.casefold(), default, node)
        for argument, default in zip(node.args.kwonlyargs, node.args.kw_defaults):
            if default is not None:
                self._field_value(argument.arg.casefold(), default, node)
        self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef

    def _visit_branch(self, node: ast.AST, condition: ast.AST) -> None:
        alias_branch = any(
            isinstance(child, ast.Name) and child.id in self.condition_aliases
            for child in ast.walk(condition)
        )
        if alias_branch or _target_literal_compare(condition, self.constants):
            self._add(TARGET_CONDITIONED_BRANCH, node, "TARGET_LITERAL_CONTROLS_BRANCH")
        signals = _readiness_signals(
            condition,
            self.constants,
            self.readiness_aliases,
        )
        body = getattr(node, "body", ())
        if signals == frozenset({"OUTPUT_EXISTENCE"}) and any(
            _positive_readiness(statement, self.constants) for statement in body
        ):
            self._add(OUTPUT_ONLY_READINESS, node, "OUTPUT_EXISTENCE_ALONE_AUTHORIZES_READINESS")

    def visit_If(self, node: ast.If) -> None:
        self._visit_branch(node, node.test)
        self.generic_visit(node)

    def visit_IfExp(self, node: ast.IfExp) -> None:
        if _target_literal_compare(node.test, self.constants) or any(
            isinstance(child, ast.Name) and child.id in self.condition_aliases
            for child in ast.walk(node.test)
        ):
            self._add(TARGET_CONDITIONED_BRANCH, node, "TARGET_LITERAL_CONTROLS_TERNARY")
        self.generic_visit(node)

    def visit_While(self, node: ast.While) -> None:
        self._visit_branch(node, node.test)
        self.generic_visit(node)

    def visit_Match(self, node: ast.Match) -> None:  # Python 3.10+
        if _field_name(node.subject) in _TARGET_IDENTIFIERS:
            for case in node.cases:
                literals = [
                    child.value
                    for child in ast.walk(case.pattern)
                    if isinstance(child, ast.Constant)
                ]
                if any(_is_concrete_literal(value) for value in literals):
                    self._add(TARGET_CONDITIONED_BRANCH, node, "TARGET_LITERAL_CONTROLS_MATCH")
                    break
        self.generic_visit(node)

    def visit_Return(self, node: ast.Return) -> None:
        if node.value is not None and _readiness_signals(
            node.value,
            self.constants,
            self.readiness_aliases,
        ) == frozenset({"OUTPUT_EXISTENCE"}):
            self._add(OUTPUT_ONLY_READINESS, node, "RETURNED_OUTPUT_EXISTENCE_AS_READINESS")
        self.generic_visit(node)


def _scan_python(relative: str, text: str) -> tuple[dict[str, Any], ...]:
    tree = ast.parse(text, filename=relative)
    scanner = _PythonScanner(relative, tree)
    scanner.visit(tree)
    unique = {
        (
            row["finding_class"],
            row["path"],
            row["line"],
            row["column"],
            row["rule"],
        ): row
        for row in scanner.findings
    }
    return tuple(unique[key] for key in sorted(unique))


def _config_findings(relative: str, payload: Any) -> tuple[dict[str, Any], ...]:
    findings: list[dict[str, Any]] = []

    def add(finding_class: str, pointer: str, rule: str) -> None:
        findings.append(
            {
                "finding_class": finding_class,
                "path": relative,
                "line": 0,
                "column": 0,
                "json_pointer_hash": _sha256_bytes(pointer.encode("utf-8")),
                "rule": rule,
            }
        )

    def walk(
        value: Any,
        pointer: str = "",
        field: str = "",
        parent_fields: tuple[str, ...] = (),
    ) -> None:
        normalized = field.casefold()
        context_field = "_".join((*parent_fields, normalized)).strip("_")
        if _is_expected_score_field(normalized) and isinstance(value, (int, float)) and not isinstance(value, bool):
            add(FIXED_EXPECTED_SCORE, pointer, "FIXED_EXPECTED_SCORE_CONFIG")
        if _is_expected_stage_field(normalized) and isinstance(value, str) and _CANONICAL_STAGE.fullmatch(value):
            add(FIXED_EXPECTED_STAGE, pointer, "FIXED_EXPECTED_STAGE_CONFIG")
        if isinstance(value, str) and _is_gold_input(context_field, value):
            add(GOLD_PRODUCTION_INPUT, pointer, "GOLD_VALUE_IN_PRODUCTION_CONFIG")
        local_toggle_enabled = value is True or (
            isinstance(value, str)
            and value.casefold() in {"enabled", "on", "true", "yes"}
        )
        if normalized in _FALLBACK_FIELDS and (
            normalized in {"automatic_local_fallback", "local_fallback", "local_provider_fallback"}
            and local_toggle_enabled
            or _is_local_provider_value(value)
        ):
            add(AUTOMATIC_LOCAL_FALLBACK, pointer, "AUTOMATIC_LOCAL_FALLBACK_CONFIG")
        if (
            normalized in {"client", "model", "provider", "provider_name", "runtime", "transport"}
            and _is_local_provider_value(value)
        ):
            add(EXECUTABLE_LOCAL_PROVIDER, pointer, "LOCAL_PROVIDER_SELECTED_IN_CONFIG")
        if (
            normalized in {"base_url", "endpoint", "provider_endpoint", "provider_url"}
            and _is_loopback_endpoint(value)
        ):
            add(EXECUTABLE_LOCAL_PROVIDER, pointer, "LOOPBACK_PROVIDER_ENDPOINT_CONFIG")
        if _is_reviewer_field(normalized) and _is_absolute_identity(value):
            add(ABSOLUTE_REVIEWER_IDENTITY, pointer, "ABSOLUTE_REVIEWER_IDENTITY_CONFIG")
        if _is_secret_field(normalized) and _is_secret_literal(value):
            add(SECRET_LITERAL, pointer, "SECRET_LITERAL_IN_PRODUCTION_CONFIG")
        if isinstance(value, Mapping):
            for key, child in sorted(value.items(), key=lambda item: str(item[0])):
                escaped = str(key).replace("~", "~0").replace("/", "~1")
                walk(
                    child,
                    f"{pointer}/{escaped}",
                    str(key),
                    (*parent_fields, normalized) if normalized else parent_fields,
                )
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{pointer}/{index}", field, parent_fields)

    walk(payload)
    return tuple(findings)


def _yaml_detection_payload(text: str) -> Mapping[str, Any]:
    """Parse the key/scalar subset needed by the security detectors.

    The canonical YAML files contain scoring tables, not executable objects.
    A full YAML object loader would add an unnecessary runtime dependency; the
    audit only needs field names and literal scalar/list values to identify the
    prohibited classes.
    """

    payload: dict[str, Any] = {}
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if line.startswith("- "):
            line = line[2:].strip()
        if not line or line == "-" or ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip().strip("\"'")
        raw_value = raw_value.strip()
        if not key or not raw_value:
            continue
        try:
            value = json.loads(raw_value)
        except json.JSONDecodeError:
            value = raw_value.strip("\"'")
        payload[key] = value
    return payload


def _referenced_configs(tree: ast.AST) -> tuple[str, ...]:
    values = {
        value.value
        for value in ast.walk(tree)
        if isinstance(value, ast.Constant)
        and isinstance(value.value, str)
        and _CONFIG_LITERAL.fullmatch(value.value)
    }
    return tuple(sorted(values))


def _referenced_production_paths(text: str) -> tuple[str, ...]:
    candidates = re.findall(
        r"(?:\.github/workflows|configs|requirements|scripts)/"
        r"[A-Za-z0-9_./-]+\.(?:bash|in|json|jsonl|lock|py|sh|txt|ya?ml)",
        text,
    )
    return tuple(
        sorted(
            {
                value
                for value in candidates
                if _CONFIG_LITERAL.fullmatch(value)
                or _AUXILIARY_LITERAL.fullmatch(value)
            }
        )
    )


def _text_auxiliary_findings(
    relative: str,
    text: str,
) -> tuple[dict[str, Any], ...]:
    """Scan shell, lock, and workflow command text without exposing literals."""

    findings: list[dict[str, Any]] = []

    def add(finding_class: str, line: int, rule: str) -> None:
        findings.append(
            {
                "finding_class": finding_class,
                "path": relative,
                "line": line,
                "column": 0,
                "rule": rule,
            }
        )

    assignment = re.compile(
        r"(?i)\b([A-Za-z_][A-Za-z0-9_-]*)\s*[:=]\s*"
        r"(?:[\"']([^\"']*)[\"']|([^\s#]+))"
    )
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        for match in assignment.finditer(line):
            field = match.group(1).casefold().replace("-", "_")
            value = match.group(2) if match.group(2) is not None else match.group(3)
            if _is_secret_field(field) and _is_secret_literal(value):
                add(SECRET_LITERAL, line_number, "SECRET_LITERAL_IN_AUXILIARY_TEXT")
            if field in _FALLBACK_FIELDS and _truthy_literal(value) and (
                field in {"automatic_local_fallback", "local_fallback", "local_provider_fallback"}
                or _is_local_provider_value(value)
            ):
                add(AUTOMATIC_LOCAL_FALLBACK, line_number, "AUTOMATIC_LOCAL_FALLBACK_IN_AUXILIARY_TEXT")
            if _is_reviewer_field(field) and _is_absolute_identity(value):
                add(ABSOLUTE_REVIEWER_IDENTITY, line_number, "ABSOLUTE_REVIEWER_IDENTITY_IN_AUXILIARY_TEXT")
            if _is_gold_input(field, value):
                add(GOLD_PRODUCTION_INPUT, line_number, "GOLD_INPUT_IN_AUXILIARY_TEXT")
            if (
                field in {"client", "model", "provider", "provider_name", "runtime", "transport"}
                and _is_local_provider_value(value)
            ):
                add(EXECUTABLE_LOCAL_PROVIDER, line_number, "LOCAL_PROVIDER_SELECTED_IN_AUXILIARY_TEXT")
        normalized = line.casefold().replace("-", "_")
        if relative.startswith("requirements/") and re.match(
            r"(?:ollama|qwen|llama_cpp|lm_studio)(?:\[|\s|=|<|>|~|!|\Z)",
            normalized,
        ):
            add(
                EXECUTABLE_LOCAL_PROVIDER,
                line_number,
                "LOCAL_PROVIDER_DEPENDENCY_IN_LOCK",
            )
        if re.search(r"(?:^|[;&|]\s*|\brun:\s*)(?:ollama|qwen|llama_cpp|lm_studio)(?:\s|$)", normalized):
            add(EXECUTABLE_LOCAL_PROVIDER, line_number, "LOCAL_PROVIDER_EXECUTABLE_IN_AUXILIARY_TEXT")
        if (
            re.search(r"\bif\b", normalized)
            and any(identifier in normalized for identifier in _TARGET_IDENTIFIERS)
            and re.search(r"[\"'][A-Za-z0-9가-힣._-]{4,}[\"']", line)
        ):
            add(TARGET_CONDITIONED_BRANCH, line_number, "TARGET_LITERAL_BRANCH_IN_AUXILIARY_TEXT")
        if (
            re.search(r"\b(?:if|test)\b", normalized)
            and "output/" in normalized
            and re.search(r"\b(?:pass|ready|readiness)\b", normalized)
        ):
            add(OUTPUT_ONLY_READINESS, line_number, "OUTPUT_ONLY_READINESS_IN_AUXILIARY_TEXT")
    unique = {
        (row["finding_class"], row["path"], row["line"], row["rule"]): row
        for row in findings
    }
    return tuple(unique[key] for key in sorted(unique))


def _collect_scope(
    repo: Path,
    *,
    entrypoint_paths: Sequence[str],
    config_paths: Sequence[str],
    auxiliary_paths: Sequence[str],
) -> tuple[
    tuple[str, ...],
    tuple[str, ...],
    tuple[str, ...],
    tuple[str, ...],
    tuple[dict[str, Any], ...],
]:
    auxiliary = set(auxiliary_paths)
    pending = list(entrypoint_paths) + [
        path for path in auxiliary_paths if path.endswith(".py")
    ]
    source_paths: set[str] = set()
    referenced_configs = set(config_paths)
    unresolved: set[str] = set()
    integrity: list[dict[str, Any]] = []
    while pending:
        relative = pending.pop(0)
        if relative in source_paths:
            continue
        source_paths.add(relative)
        pending.extend(
            candidate
            for candidate in _package_initializer_paths(repo, relative)
            if candidate not in source_paths
        )
        path = repo / relative
        if not path.is_file() or _has_symlink(repo, relative):
            continue
        try:
            text = path.read_text(encoding="utf-8")
            tree = ast.parse(text, filename=relative)
        except (OSError, UnicodeError, SyntaxError):
            continue
        referenced_configs.update(_referenced_configs(tree))
        for referenced in _referenced_production_paths(text):
            if _CONFIG_LITERAL.fullmatch(referenced):
                referenced_configs.add(referenced)
            else:
                auxiliary.add(referenced)
                if referenced.endswith(".py"):
                    pending.append(referenced)
        module = _module_name(relative)
        is_package = relative.endswith("/__init__.py")
        for imported, required_module in _local_import_modules(
            tree,
            module=module,
            is_package=is_package,
        ):
            imported_path = _module_path(repo, imported)
            if imported_path:
                pending.append(imported_path)
            elif required_module:
                unresolved.add(imported)
            elif imported.startswith("e2r"):
                # ``from package import symbol`` produces a speculative
                # package.symbol candidate.  It is unresolved only when the
                # base package/module also cannot be found.
                base = imported.rsplit(".", 1)[0]
                if _module_path(repo, base) is None:
                    unresolved.add(imported)
    auxiliary_pending = list(sorted(auxiliary))
    auxiliary_seen: set[str] = set()
    while auxiliary_pending:
        relative = auxiliary_pending.pop(0)
        if relative in auxiliary_seen:
            continue
        auxiliary_seen.add(relative)
        path = repo / relative
        if not path.is_file() or _has_symlink(repo, relative):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for referenced in _referenced_production_paths(text):
            if _CONFIG_LITERAL.fullmatch(referenced):
                referenced_configs.add(referenced)
            elif referenced not in auxiliary:
                auxiliary.add(referenced)
                auxiliary_pending.append(referenced)
    for module in sorted(unresolved):
        integrity.append(
            {
                "integrity_class": "unresolved_local_import_count",
                "path": module,
                "rule": "LOCAL_E2R_IMPORT_UNRESOLVED",
            }
        )
    return (
        tuple(sorted(source_paths)),
        tuple(sorted(referenced_configs)),
        tuple(sorted(auxiliary)),
        tuple(sorted(unresolved)),
        tuple(integrity),
    )


def compile_production_static_audit(
    *,
    repo_root: str | Path = ".",
    entrypoint_paths: Sequence[str] = CANONICAL_PRODUCTION_ENTRYPOINTS,
    config_paths: Sequence[str] = CANONICAL_PRODUCTION_CONFIGS,
    auxiliary_paths: Sequence[str] = CANONICAL_PRODUCTION_AUXILIARY_PATHS,
    test_mode: bool = False,
) -> Mapping[str, Any]:
    """Recompute the static audit and exact path/hash roster.

    Custom scope is available only for bounded detector contract tests.  A
    production caller must scan the canonical seed roster and its full local
    import/config closure.
    """

    if not isinstance(test_mode, bool):
        raise TypeError("test_mode must be boolean")
    normalized_entries = tuple(_normalize_relative(path) for path in entrypoint_paths)
    normalized_configs = tuple(_normalize_relative(path) for path in config_paths)
    normalized_auxiliary = tuple(_normalize_relative(path) for path in auxiliary_paths)
    if any(
        path is None
        for path in (*normalized_entries, *normalized_configs, *normalized_auxiliary)
    ):
        raise ValueError("static audit scope paths must be canonical relative paths")
    entries = tuple(str(path) for path in normalized_entries)
    configs = tuple(str(path) for path in normalized_configs)
    auxiliary = tuple(str(path) for path in normalized_auxiliary)
    if not test_mode and (
        entries != CANONICAL_PRODUCTION_ENTRYPOINTS
        or configs != CANONICAL_PRODUCTION_CONFIGS
        or auxiliary != CANONICAL_PRODUCTION_AUXILIARY_PATHS
    ):
        raise ValueError("production static audit scope cannot be replaced or reduced")

    repo = Path(repo_root).resolve()
    (
        source_paths,
        discovered_configs,
        discovered_auxiliary,
        unresolved,
        integrity_seed,
    ) = _collect_scope(
        repo,
        entrypoint_paths=entries,
        config_paths=configs,
        auxiliary_paths=auxiliary,
    )
    all_paths = tuple(
        sorted(set(source_paths) | set(discovered_configs) | set(discovered_auxiliary))
    )
    roster: list[dict[str, Any]] = []
    findings: list[dict[str, Any]] = []
    integrity_findings: list[dict[str, Any]] = list(integrity_seed)
    for relative in all_paths:
        path = repo / relative
        kind = (
            "PYTHON_SOURCE"
            if relative.endswith(".py")
            else "PRODUCTION_CONFIG_OR_WORKFLOW"
            if Path(relative).suffix in {".json", ".jsonl", ".yaml", ".yml"}
            else "PRODUCTION_AUXILIARY"
        )
        if _has_symlink(repo, relative):
            integrity_findings.append(
                {
                    "integrity_class": "scope_symlink_count",
                    "path": relative,
                    "rule": "SCOPED_PATH_CONTAINS_SYMLINK",
                }
            )
            continue
        if not path.is_file():
            integrity_findings.append(
                {
                    "integrity_class": "missing_scope_path_count",
                    "path": relative,
                    "rule": "SCOPED_FILE_MISSING",
                }
            )
            continue
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except (OSError, UnicodeError):
            integrity_findings.append(
                {
                    "integrity_class": "unreadable_scope_file_count",
                    "path": relative,
                    "rule": "SCOPED_FILE_UNREADABLE",
                }
            )
            continue
        roster.append(
            {
                "path": relative,
                "kind": kind,
                "sha256": _sha256_bytes(raw),
                "size_bytes": len(raw),
            }
        )
        if kind == "PYTHON_SOURCE":
            try:
                findings.extend(_scan_python(relative, text))
            except SyntaxError as exc:
                integrity_findings.append(
                    {
                        "integrity_class": "python_syntax_error_count",
                        "path": relative,
                        "line": int(exc.lineno or 0),
                        "rule": "PYTHON_AST_PARSE_FAILED",
                    }
                )
        elif kind == "PRODUCTION_CONFIG_OR_WORKFLOW":
            try:
                if path.suffix in {".yaml", ".yml"}:
                    payload = _yaml_detection_payload(text)
                elif path.suffix == ".jsonl":
                    payload: Any = [
                        json.loads(line)
                        for line in text.splitlines()
                        if line.strip()
                    ]
                else:
                    payload = json.loads(text)
            except (json.JSONDecodeError, ValueError):
                integrity_findings.append(
                    {
                        "integrity_class": "invalid_config_count",
                        "path": relative,
                        "rule": "PRODUCTION_CONFIG_PARSE_FAILED",
                    }
                )
            else:
                findings.extend(_config_findings(relative, payload))
                if relative.startswith(".github/workflows/"):
                    findings.extend(_text_auxiliary_findings(relative, text))
        else:
            findings.extend(_text_auxiliary_findings(relative, text))

    finding_counts: dict[str, int] = defaultdict(int)
    for row in findings:
        finding_counts[str(row["finding_class"])] += 1
    integrity_counts: dict[str, int] = defaultdict(int)
    for row in integrity_findings:
        integrity_counts[str(row["integrity_class"])] += 1
    critical_counts = {
        **{key: int(finding_counts.get(key, 0)) for key in REQUIRED_ZERO_COUNT_KEYS},
        **{key: int(integrity_counts.get(key, 0)) for key in _INTEGRITY_COUNT_KEYS},
    }
    roster_sorted = tuple(sorted(roster, key=lambda row: str(row["path"])))
    findings_sorted = tuple(
        sorted(
            findings,
            key=lambda row: (
                str(row.get("finding_class") or ""),
                str(row.get("path") or ""),
                int(row.get("line") or 0),
                int(row.get("column") or 0),
                str(row.get("rule") or ""),
            ),
        )
    )
    integrity_sorted = tuple(
        sorted(
            integrity_findings,
            key=lambda row: (
                str(row.get("integrity_class") or ""),
                str(row.get("path") or ""),
                str(row.get("rule") or ""),
            ),
        )
    )
    critical_sum = sum(critical_counts.values())
    core = {
        "schema_version": PRODUCTION_STATIC_AUDIT_SCHEMA,
        "status": (
            PRODUCTION_STATIC_AUDIT_PASS
            if critical_sum == 0
            else PRODUCTION_STATIC_AUDIT_FAIL
        ),
        "scanner_version": SCANNER_VERSION,
        "scope_definition": {
            "entrypoint_paths": list(entries),
            "configured_paths": list(configs),
            "auxiliary_paths": list(auxiliary),
            "import_closure_enabled": True,
            "referenced_path_discovery_enabled": True,
            "production_scope_replaceable": False,
        },
        "scope_definition_hash": stable_hash(
            {
                "entrypoint_paths": entries,
                "configured_paths": configs,
                "auxiliary_paths": auxiliary,
            }
        ),
        "source_path_count": len(source_paths),
        "config_path_count": len(discovered_configs),
        "auxiliary_path_count": len(discovered_auxiliary),
        "scanned_file_count": len(roster_sorted),
        "file_roster": list(roster_sorted),
        "file_roster_hash": stable_hash(roster_sorted),
        "unresolved_local_imports": list(unresolved),
        "findings": list(findings_sorted),
        "integrity_findings": list(integrity_sorted),
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "all_required_counts_recomputed": set(REQUIRED_ZERO_COUNT_KEYS).issubset(
            critical_counts
        ),
        "all_required_counts_zero": all(
            critical_counts[key] == 0 for key in REQUIRED_ZERO_COUNT_KEYS
        ),
        "caller_attestation_trusted": False,
        "production_readiness_authority": False,
        "score_or_stage_authority": False,
        "test_mode": test_mode,
    }
    return {**core, "audit_hash": stable_hash(core)}


def validate_production_static_audit(
    audit: Mapping[str, Any],
    *,
    recomputed: Mapping[str, Any] | None = None,
    allow_test_mode: bool = False,
) -> bool:
    """Validate the leaf contract, optionally against a fresh recomputation."""

    counts = audit.get("critical_counts")
    if not isinstance(counts, Mapping):
        return False
    scope = audit.get("scope_definition")
    roster = audit.get("file_roster")
    if not isinstance(scope, Mapping) or not isinstance(roster, list):
        return False
    test_leaf = audit.get("test_mode") is True
    expected_scope = {
        "entrypoint_paths": list(CANONICAL_PRODUCTION_ENTRYPOINTS),
        "configured_paths": list(CANONICAL_PRODUCTION_CONFIGS),
        "auxiliary_paths": list(CANONICAL_PRODUCTION_AUXILIARY_PATHS),
        "import_closure_enabled": True,
        "referenced_path_discovery_enabled": True,
        "production_scope_replaceable": False,
    }
    scope_is_valid = (
        bool(allow_test_mode and test_leaf)
        or dict(scope) == expected_scope
    )
    roster_is_valid = bool(
        roster
        and roster == sorted(roster, key=lambda row: str(row.get("path") or ""))
        and len({str(row.get("path") or "") for row in roster}) == len(roster)
        and all(
            isinstance(row, Mapping)
            and set(row) == {"path", "kind", "sha256", "size_bytes"}
            and _normalize_relative(str(row.get("path") or ""))
            == row.get("path")
            and re.fullmatch(r"[0-9a-f]{64}", str(row.get("sha256") or ""))
            and isinstance(row.get("size_bytes"), int)
            and not isinstance(row.get("size_bytes"), bool)
            and row.get("size_bytes") >= 0
            for row in roster
        )
    )
    core = {key: value for key, value in audit.items() if key != "audit_hash"}
    valid = bool(
        set(audit) == _AUDIT_KEYS
        and set(counts) == set((*REQUIRED_ZERO_COUNT_KEYS, *_INTEGRITY_COUNT_KEYS))
        and audit.get("schema_version") == PRODUCTION_STATIC_AUDIT_SCHEMA
        and audit.get("status") == PRODUCTION_STATIC_AUDIT_PASS
        and audit.get("scanner_version") == SCANNER_VERSION
        and audit.get("production_readiness_authority") is False
        and audit.get("score_or_stage_authority") is False
        and audit.get("caller_attestation_trusted") is False
        and (allow_test_mode or audit.get("test_mode") is False)
        and scope_is_valid
        and roster_is_valid
        and audit.get("scope_definition_hash")
        == stable_hash(
            {
                "entrypoint_paths": tuple(scope.get("entrypoint_paths") or ()),
                "configured_paths": tuple(scope.get("configured_paths") or ()),
                "auxiliary_paths": tuple(scope.get("auxiliary_paths") or ()),
            }
        )
        and audit.get("all_required_counts_recomputed") is True
        and audit.get("all_required_counts_zero") is True
        and all(
            isinstance(counts.get(key), int)
            and not isinstance(counts.get(key), bool)
            and counts.get(key) == 0
            for key in (*REQUIRED_ZERO_COUNT_KEYS, *_INTEGRITY_COUNT_KEYS)
        )
        and audit.get("critical_count_sum") == 0
        and audit.get("scanned_file_count") == len(roster)
        and audit.get("file_roster_hash")
        == stable_hash(tuple(roster))
        and audit.get("findings") == []
        and audit.get("integrity_findings") == []
        and audit.get("unresolved_local_imports") == []
        and audit.get("audit_hash") == stable_hash(core)
    )
    if not valid:
        return False
    return recomputed is None or dict(audit) == dict(recomputed)


__all__ = [
    "ABSOLUTE_REVIEWER_IDENTITY",
    "AUTOMATIC_LOCAL_FALLBACK",
    "CANONICAL_PRODUCTION_AUXILIARY_PATHS",
    "CANONICAL_PRODUCTION_CONFIGS",
    "CANONICAL_PRODUCTION_ENTRYPOINTS",
    "EXECUTABLE_LOCAL_PROVIDER",
    "FIXED_EXPECTED_SCORE",
    "FIXED_EXPECTED_STAGE",
    "GOLD_PRODUCTION_INPUT",
    "OUTPUT_ONLY_READINESS",
    "PRODUCTION_STATIC_AUDIT_FAIL",
    "PRODUCTION_STATIC_AUDIT_LEAF",
    "PRODUCTION_STATIC_AUDIT_PASS",
    "PRODUCTION_STATIC_AUDIT_SCHEMA",
    "REQUIRED_ZERO_COUNT_KEYS",
    "SCANNER_VERSION",
    "SECRET_LITERAL",
    "TARGET_CONDITIONED_BRANCH",
    "compile_production_static_audit",
    "validate_production_static_audit",
]
