"""Audit v12 bridge-spec vocabulary against runtime parser/feature fields."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Mapping
import ast
import json
import re

from .v12_runtime_fixture_candidates import ARCHETYPE_RUNTIME_BRIDGE_SPECS


DEFAULT_FEATURE_SOURCE_PATH = Path("src/e2r/features.py")
DEFAULT_REPORT_PARSER_SOURCE_PATH = Path("src/e2r/research/report_parser.py")
DEFAULT_SIGNAL_AUDIT_PATH = Path("docs/0619/v12_archetype_signal_runtime_translation_audit_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_bridge_spec_runtime_field_audit_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_bridge_spec_runtime_field_audit_2026-06-19.md")

FIELD_SOURCE_METHODS = {
    "any_bool",
    "first_text",
    "max_number",
    "max_number_for_scoring",
    "max_percent",
    "max_percent_for_scoring",
    "values",
    "values_for_scoring",
}

SNAKE_FIELD_RE = re.compile(r"[a-z][a-z0-9_]{2,}")

DERIVED_RUNTIME_METRICS = {
    "actual_profit_conversion_score",
    "asp_pricing_power",
    "backlog_rpo_visibility",
    "bottleneck_raw_deficit_to_green",
    "capa_constraint",
    "contract_quality",
    "current_score",
    "current_stage",
    "domain_specific_evidence_score",
    "fcf_quality_score",
    "green_gate_deficit_summary",
    "medium_term_revision_visibility",
    "one_off_shortage_risk",
    "price_stage_score",
    "revision_score",
    "sector_bottleneck_score",
    "sector_visibility_score",
    "structural_shortage",
    "structural_visibility_quality",
    "valuation_score",
}

AXIS_KEYWORDS: dict[str, tuple[str, ...]] = {
    "margin": ("margin", "opm", "spread", "pricing", "price", "asp", "leverage", "mix", "profit"),
    "customer": ("customer", "hyperscaler", "nvidia", "partner", "distribution", "channel", "client"),
    "backlog": ("backlog", "rpo", "orderbook", "order", "preorder", "pre_sold", "sold", "allocation"),
    "contract": ("contract", "renewal", "retention", "take_or_pay", "offtake", "lta"),
    "capacity": ("capacity", "capa", "utilization", "lead_time", "bottleneck", "shortage"),
    "revision": ("revision", "estimate", "guidance"),
    "valuation_repricing": ("valuation", "rerating", "pbr", "multiple", "target", "premium"),
    "capital_return": ("capital_return", "shareholder", "buyback", "cancellation", "dividend", "treasury"),
    "insurance_quality": ("csm", "k_ics", "reserve", "loss_ratio", "underwriting"),
    "bio_commercialization": ("approval", "revenue", "royalty", "commercialization", "reimbursement", "trial"),
    "software_retention": ("arr", "nrr", "retention", "renewal", "subscription", "saas", "seat"),
    "consumer_sell_through": ("sell_through", "reorder", "repeat", "export", "distribution", "channel"),
    "guard_risk": (
        "risk",
        "overheat",
        "blowoff",
        "unresolved",
        "decline",
        "delay",
        "cancelled",
        "headline",
        "thesis_break",
        "trust",
        "mae",
    ),
}


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _snake_literals(source_text: str) -> set[str]:
    tree = ast.parse(source_text)
    values: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            value = node.value.strip()
            if SNAKE_FIELD_RE.fullmatch(value):
                values.add(value)
    return values


class _FieldMethodVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.stack: list[str] = []
        self.score_method_keys: set[str] = set()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.stack.append(node.name)
        self.generic_visit(node)
        self.stack.pop()

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Attribute) and node.func.attr in FIELD_SOURCE_METHODS:
            if not self.stack or self.stack[-1] != "_research_axis_bridge_diagnostics":
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.score_method_keys.add(arg.value)
        self.generic_visit(node)


class _ParserOutputVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.parser_output_keys: set[str] = set()

    def visit_Subscript(self, node: ast.Subscript) -> None:
        if isinstance(node.value, ast.Name) and node.value.id == "fields":
            key = _constant_string(node.slice)
            if key:
                self.parser_output_keys.add(key)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "setdefault"
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id in {"fields", "parsed"}
            and node.args
        ):
            key = _constant_string(node.args[0])
            if key:
                self.parser_output_keys.add(key)
        self.generic_visit(node)


def _constant_string(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _parser_alias_keys(source_text: str) -> set[str]:
    tree = ast.parse(source_text)
    keys: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if not any(isinstance(target, ast.Name) and target.id == "aliases" for target in node.targets):
                continue
            try:
                aliases = ast.literal_eval(node.value)
            except (SyntaxError, ValueError):
                continue
            if isinstance(aliases, dict):
                keys.update(str(key) for key in aliases)
    return keys


def _bridge_diagnostic_group_keys(source_text: str) -> set[str]:
    tree = ast.parse(source_text)
    keys: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef) or node.name != "_research_axis_bridge_diagnostics":
            continue
        for child in ast.walk(node):
            if not isinstance(child, ast.Assign):
                continue
            if not any(isinstance(target, ast.Name) and target.id == "groups" for target in child.targets):
                continue
            try:
                groups = ast.literal_eval(child.value)
            except (SyntaxError, ValueError):
                continue
            if not isinstance(groups, dict):
                continue
            for payload in groups.values():
                if not isinstance(payload, tuple) or len(payload) != 2:
                    continue
                numeric_keys, bool_keys = payload
                keys.update(str(key) for key in numeric_keys)
                keys.update(str(key) for key in bool_keys)
    return keys


def build_runtime_field_inventory(
    *,
    feature_source_text: str | None = None,
    parser_source_text: str | None = None,
    feature_source_path: str | Path = DEFAULT_FEATURE_SOURCE_PATH,
    parser_source_path: str | Path = DEFAULT_REPORT_PARSER_SOURCE_PATH,
) -> dict[str, Any]:
    """Collect source-backed field vocabulary from feature and parser code."""

    feature_text = feature_source_text
    if feature_text is None:
        feature_text = Path(feature_source_path).read_text(encoding="utf-8")
    parser_text = parser_source_text
    if parser_text is None:
        parser_text = Path(parser_source_path).read_text(encoding="utf-8")

    feature_tree = ast.parse(feature_text)
    field_visitor = _FieldMethodVisitor()
    field_visitor.visit(feature_tree)
    parser_tree = ast.parse(parser_text)
    parser_visitor = _ParserOutputVisitor()
    parser_visitor.visit(parser_tree)
    parser_keys = set(parser_visitor.parser_output_keys)
    parser_keys.update(_parser_alias_keys(parser_text))

    return {
        "feature_literal_keys": sorted(_snake_literals(feature_text)),
        "feature_method_arg_keys": sorted(field_visitor.score_method_keys),
        "bridge_diagnostic_group_keys": sorted(_bridge_diagnostic_group_keys(feature_text)),
        "parser_output_keys": sorted(parser_keys),
        "derived_runtime_metrics": sorted(DERIVED_RUNTIME_METRICS),
    }


def _primitive_axes(primitive: str) -> list[str]:
    tokens = set(re.split(r"[^a-z0-9]+", primitive.lower()))
    compact = primitive.lower()
    axes: list[str] = []
    for axis, keywords in AXIS_KEYWORDS.items():
        if any(keyword in tokens or keyword in compact for keyword in keywords):
            axes.append(axis)
    return sorted(set(axes))


def _support_status(primitive: str, inventory: Mapping[str, Any]) -> tuple[str, list[str]]:
    sources: list[str] = []
    feature_method = set(inventory.get("feature_method_arg_keys", ()))
    feature_literal = set(inventory.get("feature_literal_keys", ()))
    parser_output = set(inventory.get("parser_output_keys", ()))
    bridge_diag = set(inventory.get("bridge_diagnostic_group_keys", ()))
    derived = set(inventory.get("derived_runtime_metrics", ()))
    if primitive in feature_method:
        sources.append("score_method_arg")
    if primitive in feature_literal:
        sources.append("feature_literal")
    if primitive in parser_output:
        sources.append("parser_output")
    if primitive in bridge_diag:
        sources.append("bridge_diagnostic_group")
    if primitive in derived:
        sources.append("derived_runtime_metric")
    if "score_method_arg" in sources and "parser_output" in sources:
        return "score_and_parser_exact", sources
    if "score_method_arg" in sources:
        return "score_input_exact_parser_missing", sources
    if "derived_runtime_metric" in sources:
        return "derived_runtime_metric", sources
    if "feature_literal" in sources and "parser_output" in sources:
        return "feature_and_parser_literal_exact", sources
    if "feature_literal" in sources:
        return "feature_literal_exact_parser_missing", sources
    if "parser_output" in sources:
        return "parser_output_exact_score_missing", sources
    if "bridge_diagnostic_group" in sources:
        return "bridge_diagnostic_only_exact", sources
    return "missing_feature_parser_contract", sources


def _signal_rows_by_archetype(payload: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): dict(row) for row in payload.get("rows", [])}


def _axis_contract_statuses(
    *,
    required_axes: list[str],
    missing_required_axes: list[str],
    primitive_axes: set[str],
) -> list[dict[str, str]]:
    missing = set(missing_required_axes)
    statuses: list[dict[str, str]] = []
    for axis in required_axes:
        if axis in missing and axis not in primitive_axes:
            status = "required_by_gate_but_absent_from_bridge_spec"
        elif axis in missing:
            status = "bridge_spec_axis_present_but_runtime_field_missing_or_too_weak"
        elif axis in primitive_axes:
            status = "covered_by_bridge_spec_and_runtime"
        else:
            status = "runtime_present_but_not_explicit_in_bridge_spec"
        statuses.append({"axis": axis, "status": status})
    return statuses


def build_v12_bridge_spec_runtime_field_audit(
    *,
    bridge_specs: Mapping[str, Mapping[str, Any]] | None = None,
    signal_audit_payload: Mapping[str, Any] | None = None,
    feature_source_text: str | None = None,
    parser_source_text: str | None = None,
) -> dict[str, Any]:
    """Build a current-state vocabulary contract audit for v12 bridge specs."""

    specs = dict(bridge_specs or ARCHETYPE_RUNTIME_BRIDGE_SPECS)
    signal_payload = dict(signal_audit_payload or _read_json(DEFAULT_SIGNAL_AUDIT_PATH))
    signal_by_archetype = _signal_rows_by_archetype(signal_payload)
    inventory = build_runtime_field_inventory(
        feature_source_text=feature_source_text,
        parser_source_text=parser_source_text,
    )
    rows: list[dict[str, Any]] = []
    support_counts: Counter[str] = Counter()
    axis_contract_counts: Counter[str] = Counter()
    group_missing_counts: Counter[str] = Counter()

    for archetype, spec in sorted(specs.items()):
        primitives = [str(item) for item in spec.get("expected_runtime_primitives", ())]
        primitive_rows: list[dict[str, Any]] = []
        primitive_axis_set: set[str] = set()
        missing_primitives: list[str] = []
        for primitive in primitives:
            status, sources = _support_status(primitive, inventory)
            axes = _primitive_axes(primitive)
            primitive_axis_set.update(axes)
            support_counts[status] += 1
            if status == "missing_feature_parser_contract":
                missing_primitives.append(primitive)
                group_missing_counts[str(spec.get("runtime_bridge_group") or "")] += 1
            primitive_rows.append(
                {
                    "primitive": primitive,
                    "support_status": status,
                    "support_sources": sources,
                    "primitive_axes": axes,
                }
            )

        signal_row = signal_by_archetype.get(archetype, {})
        required_axes = [str(axis) for axis in signal_row.get("required_bridge_axes", ())]
        missing_required_axes = [str(axis) for axis in signal_row.get("missing_required_bridge_axes", ())]
        axis_statuses = _axis_contract_statuses(
            required_axes=required_axes,
            missing_required_axes=missing_required_axes,
            primitive_axes=primitive_axis_set,
        )
        for item in axis_statuses:
            axis_contract_counts[item["status"]] += 1
        supported_count = len(primitives) - len(missing_primitives)
        rows.append(
            {
                "canonical_archetype_id": archetype,
                "runtime_bridge_group": str(spec.get("runtime_bridge_group") or ""),
                "expected_primitive_count": len(primitives),
                "supported_or_derived_primitive_count": supported_count,
                "missing_feature_parser_contract_count": len(missing_primitives),
                "missing_feature_parser_contract_primitives": missing_primitives,
                "expected_runtime_primitives": primitive_rows,
                "expected_primitive_axes": sorted(primitive_axis_set),
                "required_bridge_axes": required_axes,
                "missing_required_bridge_axes": missing_required_axes,
                "axis_contract_statuses": axis_statuses,
                "runtime_gap_status": signal_row.get("runtime_gap_status"),
                "diagnosis": signal_row.get("diagnosis"),
                "runtime_candidate_count": signal_row.get("runtime_candidate_count"),
                "runtime_max_score": signal_row.get("runtime_max_score"),
                "research_clean_green_count": signal_row.get("research_clean_green_count"),
                "research_raw_stage3_green_count": signal_row.get("research_raw_stage3_green_count"),
            }
        )

    rows.sort(
        key=lambda row: (
            row["missing_feature_parser_contract_count"],
            len(row["missing_required_bridge_axes"]),
            row["research_clean_green_count"] or 0,
        ),
        reverse=True,
    )
    return {
        "summary": {
            "archetype_count": len(rows),
            "expected_primitive_rows": sum(row["expected_primitive_count"] for row in rows),
            "primitive_support_status_counts": _counter_dict(support_counts),
            "axis_contract_status_counts": _counter_dict(axis_contract_counts),
            "bridge_group_missing_primitive_counts": _counter_dict(group_missing_counts),
            "archetypes_with_missing_feature_parser_contract": sum(
                1 for row in rows if row["missing_feature_parser_contract_count"] > 0
            ),
            "archetypes_with_required_axis_contract_mismatch": sum(
                1
                for row in rows
                if any(
                    item["status"] == "required_by_gate_but_absent_from_bridge_spec"
                    for item in row["axis_contract_statuses"]
                )
            ),
            "source_inventory_counts": {
                "feature_literal_keys": len(inventory["feature_literal_keys"]),
                "feature_method_arg_keys": len(inventory["feature_method_arg_keys"]),
                "bridge_diagnostic_group_keys": len(inventory["bridge_diagnostic_group_keys"]),
                "parser_output_keys": len(inventory["parser_output_keys"]),
                "derived_runtime_metrics": len(inventory["derived_runtime_metrics"]),
            },
        },
        "rows": rows,
    }


def render_v12_bridge_spec_runtime_field_audit(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Bridge Spec Runtime Field Audit",
        "",
        "이 문서는 아키타입 bridge spec이 요구하는 primitive가 현재 parser/feature/scorer 필드 언어와 맞는지 점검한다.",
        "점수 기준을 바꾸는 문서가 아니라, 누적 연구가 runtime 점수판까지 내려오지 못하는 어휘/계약 불일치를 찾는 장부다.",
        "",
        "## Summary",
        "",
        f"- archetype_count: `{summary.get('archetype_count')}`",
        f"- expected_primitive_rows: `{summary.get('expected_primitive_rows')}`",
        f"- primitive_support_status_counts: `{summary.get('primitive_support_status_counts')}`",
        f"- axis_contract_status_counts: `{summary.get('axis_contract_status_counts')}`",
        f"- bridge_group_missing_primitive_counts: `{summary.get('bridge_group_missing_primitive_counts')}`",
        f"- archetypes_with_missing_feature_parser_contract: `{summary.get('archetypes_with_missing_feature_parser_contract')}`",
        f"- archetypes_with_required_axis_contract_mismatch: `{summary.get('archetypes_with_required_axis_contract_mismatch')}`",
        f"- source_inventory_counts: `{summary.get('source_inventory_counts')}`",
        "",
        "## Archetype Matrix",
        "",
        "| archetype | runtime gap | research Green clean/raw | primitive support | missing primitive contract | required axes | axis contract warnings |",
        "| --- | --- | ---: | ---: | --- | --- | --- |",
    ]
    for row in rows:
        axis_warnings = [
            f"{item['axis']}:{item['status']}"
            for item in row.get("axis_contract_statuses", [])
            if item["status"] != "covered_by_bridge_spec_and_runtime"
        ]
        missing_primitives = row.get("missing_feature_parser_contract_primitives", [])
        lines.append(
            f"| {row.get('canonical_archetype_id')} | "
            f"{row.get('runtime_gap_status') or ''} / {row.get('diagnosis') or ''} | "
            f"{row.get('research_clean_green_count')}/{row.get('research_raw_stage3_green_count')} | "
            f"{row.get('supported_or_derived_primitive_count')}/{row.get('expected_primitive_count')} | "
            f"{', '.join(missing_primitives[:6]) if missing_primitives else 'none'}"
            f"{' ...' if len(missing_primitives) > 6 else ''} | "
            f"{', '.join(row.get('required_bridge_axes', [])) or 'none'} | "
            f"{'; '.join(axis_warnings) if axis_warnings else 'none'} |"
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- `missing_feature_parser_contract`: bridge spec에는 primitive가 있는데 현재 feature/parser 코드에서 같은 이름의 field contract를 찾지 못했다.",
            "- `derived_runtime_metric`: 입력 field가 아니라 feature 계산 뒤 생기는 metric이다. 예: `contract_quality`, `medium_term_revision_visibility`.",
            "- `required_by_gate_but_absent_from_bridge_spec`: Green gate/audit는 그 축을 요구하는데, 해당 아키타입 bridge spec primitive에는 그 축이 명시돼 있지 않다.",
            "- `bridge_spec_axis_present_but_runtime_field_missing_or_too_weak`: bridge spec에는 축이 있는데 실제 runtime row에서는 그 축 점수가 0이거나 부족하다.",
            "- 쉬운 예: C10 삼성은 runtime 후보와 리포트가 있지만 customer/backlog/contract 축이 약해 parser-feature bridge 점검 대상이다.",
            "- 쉬운 예: C01/C19/R13은 후보 row의 입력 가족이 약하므로 parser-feature bridge 실패로 단정하기 전에 replay 입력을 보강해야 한다.",
            "- 쉬운 예: C26/C27/C30/C31처럼 missing primitive가 많은 아키타입은 연구 장부의 언어와 feature/parser 언어가 아직 크게 어긋나 있다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_bridge_spec_runtime_field_audit(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_bridge_spec_runtime_field_audit()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_bridge_spec_runtime_field_audit(payload), encoding="utf-8")
    return {
        "json_path": str(json_path),
        "md_path": str(md_path),
        "summary": payload["summary"],
    }


if __name__ == "__main__":
    result = write_v12_bridge_spec_runtime_field_audit()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
