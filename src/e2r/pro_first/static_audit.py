"""Semantic security/authority audit for the production Pro-first surface."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
from typing import Any, Iterable, Mapping


CRITICAL_KEYS = (
    "tampermonkey_runtime_dependency_count",
    "hidden_chatgpt_api_count",
    "login_automation_count",
    "credential_persistence_count",
    "cookie_export_count",
    "submit_without_approval_count",
    "duplicate_submit_path_count",
    "pro_score_authority_count",
    "pro_stage_authority_count",
    "full_research_restart_after_dossier_count",
    "corroboration_supplement_count",
    "monitoring_supplement_count",
    "deterministic_query_template_count",
    "raw_output_tracked_count",
)


@dataclass(frozen=True)
class StaticFinding:
    key: str
    path: str
    line: int
    reason: str

    def to_dict(self) -> Mapping[str, Any]:
        return self.__dict__


class _PythonSurfaceVisitor(ast.NodeVisitor):
    def __init__(self, *, relative_path: str) -> None:
        self.relative_path = relative_path
        self.findings: list[StaticFinding] = []
        self.scope: list[str] = []
        self.send_click_lines: list[int] = []

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        self.scope.append(node.name)
        self.generic_visit(node)
        self.scope.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        self.scope.append(node.name)
        self.generic_visit(node)
        self.scope.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> Any:
        self.scope.append(node.name)
        self.generic_visit(node)
        self.scope.pop()

    def visit_Import(self, node: ast.Import) -> Any:
        for alias in node.names:
            if "tampermonkey" in alias.name.casefold():
                self._add("tampermonkey_runtime_dependency_count", node, "runtime import")

    def visit_ImportFrom(self, node: ast.ImportFrom) -> Any:
        if "tampermonkey" in str(node.module or "").casefold():
            self._add("tampermonkey_runtime_dependency_count", node, "runtime import")

    def visit_Constant(self, node: ast.Constant) -> Any:
        if not isinstance(node.value, str):
            return
        value = node.value.casefold()
        if re.search(r"https?://(?:www\.)?chatgpt\.com/(?:backend-api|api/auth|conversation)", value):
            self._add("hidden_chatgpt_api_count", node, "private ChatGPT endpoint literal")

    def visit_Dict(self, node: ast.Dict) -> Any:
        for key_node, value_node in zip(node.keys, node.values):
            key = key_node.value if isinstance(key_node, ast.Constant) else None
            value = value_node.value if isinstance(value_node, ast.Constant) else None
            normalized = str(key or "").casefold()
            if normalized in {"score_authority", "pro_score_authority", "production_total_score_authority"} and value is True:
                self._add("pro_score_authority_count", value_node, "Pro score authority enabled")
            if normalized in {"stage_authority", "pro_stage_authority"} and value is True:
                self._add("pro_stage_authority_count", value_node, "Pro Stage authority enabled")
            if normalized == "full_research_restart" and value is True:
                self._add("full_research_restart_after_dossier_count", value_node, "full restart enabled")
            if normalized in {"planner_label", "gap_class"} and value in {"CORROBORATION_CAP", "MONITORING_GAP"}:
                if _dict_true_value(node, "supplemental_allowed"):
                    audit_key = (
                        "corroboration_supplement_count"
                        if value == "CORROBORATION_CAP"
                        else "monitoring_supplement_count"
                    )
                    self._add(audit_key, value_node, "nonblocking gap opens a supplement")
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> Any:
        name = _call_name(node.func)
        lowered = name.casefold()
        if lowered.endswith(".submit_once"):
            allowed_initial = (
                self.relative_path == "src/e2r/pro_first/approval.py"
                and "ExactlyOnceSubmitCoordinator" in self.scope
                and "submit" in self.scope
            )
            allowed_scoped_followup = (
                self.relative_path
                == "src/e2r/pro_first/multi_pass/orchestrator.py"
                and "ProMultiPassResearchOrchestrator" in self.scope
                and "submit_followup" in self.scope
            )
            allowed_intercepted_recovery = (
                self.relative_path
                == "src/e2r/pro_first/multi_pass/orchestrator.py"
                and "ProMultiPassResearchOrchestrator" in self.scope
                and "resume_intercepted_followup_submit" in self.scope
            )
            allowed = (
                allowed_initial
                or allowed_scoped_followup
                or allowed_intercepted_recovery
            )
            if not allowed:
                self._add(
                    "submit_without_approval_count",
                    node,
                    "submit_once outside initial/scoped exactly-once coordinator",
                )
        if _is_guarded_send_dispatch(node):
            self.send_click_lines.append(node.lineno)
        if lowered.endswith((".fill", ".type")):
            rendered = ast.unparse(node).casefold()
            if any(token in rendered for token in ("password", "passwd", "username", "email")):
                self._add("login_automation_count", node, "credential form automation")
        if "storage_state" in lowered or lowered.endswith(".cookies"):
            self._add("cookie_export_count", node, "browser credential export API")
        if lowered.endswith((".write_text", ".write_bytes", "json.dump", "pickle.dump")):
            rendered = ast.unparse(node).casefold()
            if any(token in rendered for token in ("cookie", "password", "passwd", "credential", "storage_state")):
                self._add("credential_persistence_count", node, "credential-like data persisted")
        self.generic_visit(node)

    def _add(self, key: str, node: ast.AST, reason: str) -> None:
        self.findings.append(
            StaticFinding(key=key, path=self.relative_path, line=int(getattr(node, "lineno", 0)), reason=reason)
        )


def compile_pro_first_static_audit(repo_root: str | Path) -> Mapping[str, Any]:
    root = Path(repo_root).expanduser().resolve()
    package = root / "src/e2r/pro_first"
    if not package.is_dir():
        raise ValueError("Pro-first production package is missing")
    findings: list[StaticFinding] = []
    send_clicks: list[tuple[str, int]] = []
    for path in sorted(package.rglob("*.py")):
        if "__pycache__" in path.parts or path.name == "static_audit.py":
            continue
        relative = path.relative_to(root).as_posix()
        source_findings, source_send_clicks = audit_python_source(
            path.read_text(encoding="utf-8"), relative_path=relative
        )
        findings.extend(source_findings)
        send_clicks.extend((relative, line) for line in source_send_clicks)

    expected_click = ("src/e2r/pro_first/browser/chatgpt_adapter.py", 208)
    # The line is reported, but ownership is semantic: exactly one click in the
    # adapter's guarded submit_once method is the entire allowed DOM send surface.
    if len(send_clicks) != 1 or send_clicks[0][0] != expected_click[0]:
        for path, line in send_clicks or [("src/e2r/pro_first/browser", 0)]:
            findings.append(
                StaticFinding(
                    key="duplicate_submit_path_count",
                    path=path,
                    line=line,
                    reason=f"expected one guarded send-click path, observed {len(send_clicks)}",
                )
            )

    findings.extend(_text_surface_findings(root))
    tracked_raw = _tracked_forbidden_runtime_paths(root)
    findings.extend(
        StaticFinding(
            key="raw_output_tracked_count",
            path=path,
            line=0,
            reason="runtime raw/cache/output path is tracked",
        )
        for path in tracked_raw
    )
    counts = {key: 0 for key in CRITICAL_KEYS}
    for finding in findings:
        counts[finding.key] += 1
    critical_sum = sum(counts.values())
    return {
        "schema_version": "e2r_pro_first_static_audit_v1",
        "status": "E2R_PRO_FIRST_STATIC_AUDIT_PASS" if critical_sum == 0 else "E2R_PRO_FIRST_STATIC_AUDIT_FAIL",
        "critical_counts": counts,
        "critical_count_sum": critical_sum,
        "findings": [row.to_dict() for row in findings],
        "audited_package": "src/e2r/pro_first",
        "guarded_dom_submit_path_count": len(send_clicks),
        "recorded_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }


def audit_python_source(
    source: str, *, relative_path: str
) -> tuple[tuple[StaticFinding, ...], tuple[int, ...]]:
    tree = ast.parse(source, filename=relative_path)
    visitor = _PythonSurfaceVisitor(relative_path=relative_path)
    visitor.visit(tree)
    return tuple(visitor.findings), tuple(visitor.send_click_lines)


def _is_guarded_send_dispatch(node: ast.Call) -> bool:
    """Recognize the one physical DOM send action independent of click API.

    Playwright's coordinate click and a locator-scoped native DOM click are
    two implementations of the same dispatch boundary.  The latter is used
    when an animated ChatGPT button never becomes coordinate-stable.  Both
    must count, so changing APIs can never make the exactly-one audit report
    a false zero.
    """

    if not isinstance(node.func, ast.Attribute):
        return False
    owner = _expression_name(node.func.value).casefold()
    if owner not in {"send", "send_button", "submit_button"}:
        return False
    method = node.func.attr.casefold()
    if method == "click":
        return True
    if method != "evaluate" or not node.args:
        return False
    expression = node.args[0]
    return (
        isinstance(expression, ast.Constant)
        and isinstance(expression.value, str)
        and re.search(r"\b[A-Za-z_$][\w$]*\.click\s*\(", expression.value)
        is not None
    )


def _text_surface_findings(root: Path) -> Iterable[StaticFinding]:
    paths = [root / "pyproject.toml", root / "scripts/start_e2r_pro_chrome.ps1"]
    for path in paths:
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            lowered = line.casefold()
            if "tampermonkey" in lowered and not lowered.lstrip().startswith("#"):
                yield StaticFinding("tampermonkey_runtime_dependency_count", relative, line_number, "runtime dependency literal")
            if re.search(r"--(?:password-store|load-extension)|cookie.*export|storage-state", lowered):
                yield StaticFinding("credential_persistence_count", relative, line_number, "browser credential persistence option")


def _tracked_forbidden_runtime_paths(root: Path) -> tuple[str, ...]:
    base = subprocess.run(
        ["git", "merge-base", "HEAD", "origin/main"],
        cwd=root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    if not base:
        base = subprocess.run(
            ["git", "rev-parse", "HEAD^"],
            cwd=root,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ).stdout.strip()
    completed = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", "-z", f"{base}...HEAD"],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    tracked = completed.stdout.decode("utf-8").split("\0")
    return tuple(
        sorted(
            path
            for path in tracked
            if path.startswith((".e2r_cache/", "data/cache/", "output/"))
        )
    )


def _dict_true_value(node: ast.Dict, wanted: str) -> bool:
    for key_node, value_node in zip(node.keys, node.values):
        if isinstance(key_node, ast.Constant) and key_node.value == wanted:
            return isinstance(value_node, ast.Constant) and value_node.value is True
    return False


def _call_name(node: ast.AST) -> str:
    return _expression_name(node)


def _expression_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = _expression_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    return ""


def write_static_audit(path: str | Path, result: Mapping[str, Any]) -> Path:
    destination = Path(path).expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.tmp")
    temporary.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(destination)
    return destination


__all__ = [
    "CRITICAL_KEYS",
    "audit_python_source",
    "compile_pro_first_static_audit",
    "write_static_audit",
]
