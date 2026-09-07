#!/usr/bin/env python3
"""Compile the reviewed 36-contract V2 research catalog deterministically."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BLUEPRINT = ROOT / "configs/e2r_archetype_research_blueprints_v2.json"
DEFAULT_OUTPUT = ROOT / "configs/e2r_archetype_research_contracts_v2.json"
EVIDENCE_CONTRACTS = ROOT / "configs/e2r_archetype_evidence_contracts_v12.json"
AGENTIC_CONTRACTS = ROOT / "configs/e2r_agentic_evidence_contracts_v2.json"
TERMINAL_STATUSES = [
    "SUPPORTED_SCORING",
    "PARTIALLY_SUPPORTED_SCORING",
    "SUPPORTED_NON_SCORING",
    "COUNTER_SUPPORTED",
    "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
    "LIKELY_NONPUBLIC",
    "FUTURE_EVENT_ONLY",
    "NOT_APPLICABLE_WITH_REASON",
]
CANONICAL_COMPONENTS = (
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
)
FINANCIAL_TERMS = (
    "fcf", "cash", "현금", "margin", "마진", "opm", "eps", "이익",
    "운전자본", "working capital", "수금", "roe", "csm", "충당금",
    "희석", "runway", "자본", "비용",
)
COUNTER_TERMS = (
    "counter", "risk", "취소", "지연", "원가초과", "둔화", "손실",
    "하락", "실패", "상실", "oversupply", "과잉", "default", "소송",
    "reversal", "break", "오인", "false positive", "철회", "분쟁",
)
LIFECYCLE_TERMS = (
    "현재", "상태", "해소", "재개", "악화", "변경", "supersed",
    "open", "resolved", "완료", "유효", "timeline", "일정", "phase",
    "milestone", "과거", "후속", "유지", "종결",
)
VALUATION_TERMS = (
    "valuation", "밸류에이션", "pbr", "multiple", "peer", "revision",
    "consensus", "컨센서스", "기대", "rerating", "리레이팅", "event spread",
)
SOURCE_FAMILY_RULES = (
    (("감사", "회계", "restatement", "auditor"), ("AUDITOR_FILING", "REGULATOR_OFFICIAL")),
    (("법원", "소송", "법안", "규제", "permit", "승인", "정책"), ("REGULATOR_OFFICIAL", "ISSUER_OFFICIAL")),
    (("clinical", "trial", "임상", "endpoint", "safety"), ("TRIAL_REGISTRY", "REGULATOR_OFFICIAL", "ISSUER_FILING")),
    (("고객", "customer", "oem", "partner", "발주처"), ("ISSUER_OFFICIAL", "CUSTOMER_PARTNER_OFFICIAL")),
    (("fcf", "cash", "현금", "margin", "마진", "eps", "실적"), ("ISSUER_EARNINGS", "OFFICIAL_FILING")),
    (("valuation", "revision", "consensus", "pbr", "밸류에이션"), ("CURRENT_MARKET_DATA", "LAWFUL_REVISION_DATA")),
)
PRIMITIVE_HINTS = {
    "order": ("order", "수주", "주문"),
    "backlog": ("backlog", "잔고", "수주"),
    "customer": ("customer", "고객", "발주", "oem", "partner"),
    "contract": ("contract", "계약", "call-off", "offtake", "tender"),
    "delivery": ("delivery", "납품", "출하", "shipment", "일정"),
    "margin": ("margin", "마진", "opm", "spread", "이익"),
    "fcf": ("fcf", "cash", "현금", "운전자본"),
    "capacity": ("capacity", "capa", "증설", "가동", "utilization"),
    "pricing": ("pricing", "asp", "가격", "spread"),
    "price": ("price", "가격", "valuation"),
    "qualification": ("qualification", "인증", "승인", "수율"),
    "revision": ("revision", "consensus", "컨센서스", "valuation", "밸류에이션"),
    "valuation": ("valuation", "밸류에이션", "pbr", "multiple"),
    "inventory": ("inventory", "재고"),
    "policy": ("policy", "정책", "법안", "보조금"),
    "regulatory": ("regulatory", "규제", "승인", "법률"),
    "approval": ("approval", "승인", "규제"),
    "permit": ("permit", "허가", "승인"),
    "risk": ("risk", "위험", "counter", "실패", "둔화"),
    "quality": ("quality", "질", "품질", "신뢰"),
    "supply": ("supply", "공급", "증설", "shortage"),
    "demand": ("demand", "수요", "판매", "출하"),
    "utilization": ("utilization", "가동률", "가동"),
    "revenue": ("revenue", "매출", "sales", "수익"),
    "repeat": ("repeat", "반복", "reorder", "renewal"),
    "retention": ("retention", "renewal", "churn", "nrr", "grr"),
    "export": ("export", "수출", "해외"),
    "capital": ("capital", "자본", "capex", "투자"),
    "accounting": ("accounting", "회계", "감사"),
    "trial": ("trial", "임상", "endpoint", "safety"),
    "bio": ("임상", "승인", "상업화", "partner"),
    "cash": ("cash", "현금", "fcf", "수금"),
}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--master-goal")
    parser.add_argument("--blueprint", default=str(DEFAULT_BLUEPRINT))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    args = parser.parse_args(argv)
    blueprint_path = Path(args.blueprint).resolve()
    if args.master_goal:
        blueprint = import_master_goal(Path(args.master_goal).resolve())
        _write_json(blueprint_path, blueprint)
    else:
        blueprint = _read_json(blueprint_path)
    catalog = compile_catalog(blueprint)
    _write_json(Path(args.output).resolve(), catalog)
    return 0


def import_master_goal(path: Path) -> Mapping[str, Any]:
    raw = path.read_text(encoding="utf-8")
    start = raw.index("# 5. 전 36 canonical contract별")
    end = raw.index("# 6. Prompt compiler", start)
    section = raw[start:end]
    contracts = []
    pattern = re.compile(
        r"^## 5\.\d+ `([^`]+)`\n(.*?)(?=^## 5\.|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    for match in pattern.finditer(section):
        archetype_id, body = match.groups()
        role = _required_match(body, r"contract_role: `([^`]+)`")
        mechanism = _required_match(body, r"economic mechanism: (.+)")
        questions = [value.strip() for value in re.findall(r"^\d+\. (.+)$", body, re.MULTILINE)]
        source_roles = _required_match(body, r"권장 source roles: (.+)")
        false_positive_guard = _required_match(body, r"false-positive / guard: (.+)")
        contracts.append(
            {
                "archetype_id": archetype_id,
                "contract_role": role,
                "economic_mechanism": mechanism,
                "questions": questions,
                "recommended_source_roles": source_roles,
                "false_positive_guard": false_positive_guard,
            }
        )
    if len(contracts) != 36:
        raise ValueError(f"master goal must define exactly 36 blueprints, got {len(contracts)}")
    return {
        "schema_version": "e2r_archetype_research_blueprints_v2",
        "master_goal_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "contract_count": len(contracts),
        "question_family_count": sum(len(row["questions"]) for row in contracts),
        "contracts": contracts,
    }


def compile_catalog(blueprint: Mapping[str, Any]) -> Mapping[str, Any]:
    evidence_payload = _read_json(EVIDENCE_CONTRACTS)
    agentic_payload = _read_json(AGENTIC_CONTRACTS)
    evidence = {
        str(row["canonical_archetype_id"]): row
        for row in evidence_payload["contracts"]
    }
    agentic = {str(row["archetype_id"]): row for row in agentic_payload["contracts"]}
    blueprints = {str(row["archetype_id"]): row for row in blueprint["contracts"]}
    if set(evidence) != set(agentic) or set(evidence) != set(blueprints):
        raise ValueError("canonical, agentic, and research blueprint rosters differ")
    contracts = [
        _compile_contract(
            {
                **blueprints[archetype_id],
                "master_goal_sha256": blueprint["master_goal_sha256"],
            },
            evidence[archetype_id],
            agentic[archetype_id],
        )
        for archetype_id in evidence
    ]
    return {
        "schema_version": "e2r_archetype_research_contract_catalog_v2",
        "contract_count": len(contracts),
        "question_family_count": sum(len(row["question_families"]) for row in contracts),
        "generated_from": {
            "blueprint_schema": blueprint["schema_version"],
            "master_goal_sha256": blueprint["master_goal_sha256"],
            "canonical_evidence_contracts": EVIDENCE_CONTRACTS.name,
            "agentic_evidence_contracts": AGENTIC_CONTRACTS.name,
        },
        "contracts": contracts,
    }


def _compile_contract(
    blueprint: Mapping[str, Any],
    evidence: Mapping[str, Any],
    agentic: Mapping[str, Any],
) -> Mapping[str, Any]:
    archetype_id = str(blueprint["archetype_id"])
    questions = tuple(str(value) for value in blueprint["questions"])
    required = tuple(dict.fromkeys(str(value) for value in evidence["required_primitives"]))
    green = tuple(dict.fromkeys(_primitive_values(agentic.get("green_gate"))))
    guard = tuple(
        dict.fromkeys(
            [*(str(value) for value in evidence.get("guard_primitives") or ()),
             *(str(value) for value in (agentic.get("guard_modes") or {}))]
        )
    )
    role_sets = _question_roles(
        questions,
        cross_guard=blueprint["contract_role"] == "CROSS_GUARD",
    )
    primitive_map: list[list[str]] = [[] for _ in questions]
    all_primitives = tuple(dict.fromkeys((*required, *green, *guard)))
    for primitive in all_primitives:
        if primitive in guard:
            candidates = [
                index
                for index, roles in enumerate(role_sets)
                if set(roles).intersection(
                    {"COUNTER_HARD_BREAK", "LIFECYCLE_SUPERSESSION", "GUARD_ONLY"}
                )
            ]
            selected = max(candidates or range(len(questions)), key=lambda index: _primitive_question_score(primitive, questions[index]))
        else:
            selected = max(range(len(questions)), key=lambda index: _primitive_question_score(primitive, questions[index]))
        primitive_map[selected].append(primitive)
    component_by_primitive: dict[str, set[str]] = {}
    for component_id, primitives in (agentic.get("score_rubric") or {}).items():
        for primitive in primitives:
            component_by_primitive.setdefault(str(primitive), set()).add(str(component_id))
    question_rows = []
    for index, (text, roles) in enumerate(zip(questions, role_sets), 1):
        role = _primary_question_role(roles)
        primitives = tuple(dict.fromkeys(primitive_map[index - 1]))
        affected = sorted(
            {
                component
                for primitive in primitives
                for component in component_by_primitive.get(primitive, ())
            }
        )
        if blueprint["contract_role"] == "CROSS_GUARD":
            affected = []
        elif not affected:
            affected = list(_fallback_components(role))
        source_families = _source_families(text)
        freshness_days = _question_freshness(primitives, agentic.get("freshness") or {})
        supersession_rule = _question_supersession(primitives, agentic.get("freshness") or {})
        question_id = f"{archetype_id}_Q{index:02d}"
        material_counter = role in {"COUNTER_HARD_BREAK", "LIFECYCLE_SUPERSESSION", "GUARD_ONLY"}
        question_rows.append(
            {
                "question_family_id": question_id,
                "question_role": role,
                "question_roles": list(roles),
                "question_text": text,
                "economic_need": f"{blueprint['economic_mechanism']}에서 다음 연결을 검증: {text}",
                "mandatory_for_full_thesis": True,
                "required_primitives": list(primitives),
                "support_predicates": list(primitives) or [f"{question_id}:DIRECT_ECONOMIC_SUPPORT"],
                "partial_support_predicates": [f"{question_id}:PARTIAL_DIRECT_BRIDGE"],
                "counter_predicates": [f"{question_id}:COUNTER_OR_SUPERSESSION"],
                "non_scoring_predicates": [f"{question_id}:SOURCE_PROXY_OR_HEADLINE_ONLY"],
                "required_source_roles": list(source_families),
                "preferred_source_families": list(source_families),
                "required_independence": {
                    "min_official": 1,
                    "min_independent": int(role in {"COUNTER_HARD_BREAK", "EXPECTATION_VALUATION", "GUARD_ONLY"}),
                },
                "freshness_days": freshness_days,
                "supersession_rule": supersession_rule,
                "affected_component_ids": affected,
                "could_change_score": role != "GUARD_ONLY",
                "could_change_stage": role in {"COUNTER_HARD_BREAK", "LIFECYCLE_SUPERSESSION", "EXPECTATION_VALUATION", "GUARD_ONLY"},
                "could_change_hard_break": material_counter,
                "allowed_terminal_statuses": TERMINAL_STATUSES,
                "adequate_search_requirements": {
                    "official_route_attempt_required": True,
                    "minimum_distinct_source_routes": 2 if material_counter else 1,
                    "independent_no_new_route_confirmations_for_absence": 2,
                    "provider_and_parser_must_be_normal": True,
                    "accepted_fact_delta_must_be_zero_for_fixpoint": True,
                },
                "false_positive_guards": [str(blueprint["false_positive_guard"])],
            }
        )
    has_valuation = any("EXPECTATION_VALUATION" in roles for roles in role_sets)
    return {
        "schema_version": "e2r_archetype_research_contract_v2",
        "archetype_id": archetype_id,
        "contract_role": blueprint["contract_role"],
        "large_sector_id": evidence["large_sector_id"],
        "runtime_bridge_group": evidence["runtime_bridge_group"],
        "economic_mechanism": blueprint["economic_mechanism"],
        "required_primitives": list(required),
        "green_gate_primitives": list(green),
        "guard_primitives": list(guard),
        "required_bridge_axes": list(evidence["required_bridge_axes"]),
        "question_families": question_rows,
        "source_role_policy": {
            "recommended_routes": blueprint["recommended_source_roles"],
            "official_first": True,
            "source_proxy_is_non_scoring": True,
            "llm_only_inference_is_diagnostic": True,
        },
        "source_quorum": agentic["source_quorum"],
        "freshness_policy": agentic["freshness"],
        "supersession_policy": {
            "append_only": True,
            "latest_authoritative_current_status_wins": True,
            "primitive_rules": agentic["freshness"],
        },
        "false_positive_guards": [blueprint["false_positive_guard"]],
        "hard_break_policy": {
            "current_open_issuer_scoped_required": True,
            "official_quorum_required": True,
            "price_or_theme_only_forbidden": True,
            "resolved_or_superseded_claim_forbidden": True,
        },
        "component_mapping": agentic["score_rubric"],
        "adequate_search_policy": {
            "question_level_not_fact_count": True,
            "official_first": True,
            "public_searchable_material_gap_must_close": True,
            "semantic_fixpoint_min_independent_confirmations": 2,
            "same_fact_snapshot_and_lineage_required": True,
            "provider_parser_normal_required": True,
            "transport_limit_is_pending_not_complete": True,
        },
        "valuation_research_policy": (
            {"status": "QUESTION_FAMILY_PRESENT"}
            if has_valuation
            else {
                "status": "NOT_APPLICABLE_WITH_REASON",
                "reason": "이 아키타입의 master 질문에는 독립 valuation family가 없으며 공통 deterministic valuation component가 별도 처리한다.",
            }
        ),
        "historical_contract_lineage": [
            evidence.get("source_matrix"),
            agentic.get("generated_from_v1_contract"),
            f"master_goal_sha256:{blueprint.get('master_goal_sha256', 'catalog-level')}",
        ],
        "prompt_contract_version": "v2",
        "score_authority": False,
        "stage_authority": False,
    }


def _question_roles(
    questions: Sequence[str],
    *,
    cross_guard: bool,
) -> list[tuple[str, ...]]:
    if cross_guard:
        return [("GUARD_ONLY", "COUNTER_HARD_BREAK") for _ in questions]
    roles: list[list[str]] = [["ECONOMIC_BRIDGE"] for _ in questions]
    semantic_terms = (
        ("COUNTER_HARD_BREAK", COUNTER_TERMS),
        ("LIFECYCLE_SUPERSESSION", LIFECYCLE_TERMS),
        ("FINANCIAL_CASH_CONVERSION", FINANCIAL_TERMS),
        ("EXPECTATION_VALUATION", VALUATION_TERMS),
    )
    for index, question in enumerate(questions):
        normalized = question.casefold()
        for role, terms in semantic_terms:
            if any(term in normalized for term in terms):
                roles[index].append(role)
    required_roles = (
        ("COUNTER_HARD_BREAK", COUNTER_TERMS),
        ("LIFECYCLE_SUPERSESSION", LIFECYCLE_TERMS),
        ("FINANCIAL_CASH_CONVERSION", FINANCIAL_TERMS),
    )
    for role, terms in required_roles:
        if not any(role in row for row in roles):
            selected = _best_index(questions, terms)
            assert selected is not None
            roles[selected].append(role)
    return [tuple(dict.fromkeys(row)) for row in roles]


def _primary_question_role(roles: Sequence[str]) -> str:
    for role in (
        "GUARD_ONLY",
        "COUNTER_HARD_BREAK",
        "LIFECYCLE_SUPERSESSION",
        "FINANCIAL_CASH_CONVERSION",
        "EXPECTATION_VALUATION",
        "ECONOMIC_BRIDGE",
    ):
        if role in roles:
            return role
    raise ValueError("question has no semantic role")


def _best_index(
    questions: Sequence[str],
    terms: Sequence[str],
    *,
    excluded: set[int] | None = None,
    require_match: bool = False,
) -> int | None:
    excluded = excluded or set()
    choices = [index for index in range(len(questions)) if index not in excluded]
    if not choices:
        raise ValueError("question role allocation exhausted")
    scores = {index: sum(term in questions[index].casefold() for term in terms) for index in choices}
    best = max(choices, key=lambda index: (scores[index], index))
    if require_match and scores[best] == 0:
        return None
    return best


def _primitive_question_score(primitive: str, question: str) -> int:
    normalized = question.casefold()
    score = 0
    for token in primitive.split("_"):
        if token and token in normalized:
            score += 4
        for hint in PRIMITIVE_HINTS.get(token, (token,)):
            if hint in normalized:
                score += 2
    return score


def _source_families(question: str) -> tuple[str, ...]:
    normalized = question.casefold()
    values: list[str] = []
    for terms, families in SOURCE_FAMILY_RULES:
        if any(term in normalized for term in terms):
            values.extend(families)
    if not values:
        values.extend(("ISSUER_OFFICIAL", "OFFICIAL_FILING"))
    return tuple(dict.fromkeys(values))


def _fallback_components(role: str) -> tuple[str, ...]:
    if role == "FINANCIAL_CASH_CONVERSION":
        return ("eps_fcf_explosion", "capital_allocation", "information_confidence")
    if role == "EXPECTATION_VALUATION":
        return ("market_mispricing", "valuation_rerating", "information_confidence")
    if role in {"COUNTER_HARD_BREAK", "LIFECYCLE_SUPERSESSION"}:
        return ("earnings_visibility", "information_confidence")
    return ("earnings_visibility", "information_confidence")


def _question_freshness(primitives: Sequence[str], freshness: Mapping[str, Any]) -> int | None:
    values = [
        row.get("max_age_days")
        for primitive in primitives
        if isinstance((row := freshness.get(primitive)), Mapping)
        and isinstance(row.get("max_age_days"), int)
    ]
    return min(values) if values else 365


def _question_supersession(primitives: Sequence[str], freshness: Mapping[str, Any]) -> str:
    values = [
        str(row.get("supersession_rule"))
        for primitive in primitives
        if isinstance((row := freshness.get(primitive)), Mapping)
        and row.get("supersession_rule")
    ]
    return values[0] if values else "latest_authoritative_update"


def _primitive_values(value: Any) -> list[str]:
    values: list[str] = []
    if isinstance(value, Mapping):
        primitive = value.get("primitive")
        if isinstance(primitive, str):
            values.append(primitive)
        for child in value.values():
            values.extend(_primitive_values(child))
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        for child in value:
            values.extend(_primitive_values(child))
    return values


def _required_match(text: str, pattern: str) -> str:
    match = re.search(pattern, text)
    if not match:
        raise ValueError(f"master blueprint field missing: {pattern}")
    return match.group(1).strip()


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    raise SystemExit(main())
