"""Dynamic, blind-safe compiler for contract-driven Pro research passes."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.pro_first.ids import canonical_hash

from .question_planner import ResearchQuestionPlan, build_research_question_plan
from .loader import load_research_contract


PASS_TEMPLATE_FILES = {
    "INITIAL_FULL_RESEARCH": "e2r_pro_v2_initial_full_research.md",
    "PUBLIC_GAP_CLOSURE": "e2r_pro_v2_public_gap_closure.md",
    "COUNTER_SUPERSESSION": "e2r_pro_v2_counter_supersession.md",
    "VERIFIER_REPAIR": "e2r_pro_v2_verifier_repair.md",
    "SATURATION_AUDIT": "e2r_pro_v2_saturation_audit.md",
    "DELTA_RESEARCH": "e2r_pro_v2_delta_research.md",
}
TERMINAL_STATUSES = (
    "SUPPORTED_SCORING",
    "PARTIALLY_SUPPORTED_SCORING",
    "SUPPORTED_NON_SCORING",
    "COUNTER_SUPPORTED",
    "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
    "LIKELY_NONPUBLIC",
    "FUTURE_EVENT_ONLY",
    "NOT_APPLICABLE_WITH_REASON",
)
NONTERMINAL_STATUSES = (
    "PUBLIC_SEARCHABLE",
    "UNKNOWN_ROUTE_NOT_YET_TESTED",
    "CONTRADICTED_UNRESOLVED",
    "SOURCE_PENDING",
    "PROVIDER_PENDING",
    "PARSER_PENDING",
    "VERIFIER_REPAIR_REQUIRED",
)


@dataclass(frozen=True)
class CompiledProResearchPromptV2:
    pass_name: str
    primary_archetype_ids: tuple[str, ...]
    contract_ids: tuple[str, ...]
    mandatory_question_ids: tuple[str, ...]
    prompt_text: str
    prompt_hash: str

    def to_receipt(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_compiled_pro_research_prompt_v2",
            "pass_name": self.pass_name,
            "primary_archetype_ids": list(self.primary_archetype_ids),
            "contract_ids": list(self.contract_ids),
            "mandatory_question_ids": list(self.mandatory_question_ids),
            "mandatory_question_count": len(self.mandatory_question_ids),
            "prompt_hash": self.prompt_hash,
            "score_authority": False,
            "stage_authority": False,
        }


class ProResearchPromptCompilerV2:
    def __init__(self, *, template_root: str | Path | None = None) -> None:
        self.template_root = (
            Path(template_root).resolve()
            if template_root
            else Path(__file__).resolve().parents[4] / "configs/prompts"
        )

    def compile(
        self,
        *,
        packet: Mapping[str, Any],
        primary_archetype_ids: Sequence[str],
        pass_name: str = "INITIAL_FULL_RESEARCH",
        existing_verified_ledger_digest: Mapping[str, Any] | None = None,
        unresolved_question_state: Sequence[Mapping[str, Any]] = (),
        pass_inputs: Mapping[str, Any] | None = None,
        conversation_id: str | None = None,
    ) -> CompiledProResearchPromptV2:
        if pass_name not in PASS_TEMPLATE_FILES:
            raise ValueError(f"unsupported Pro V2 research pass: {pass_name}")
        _assert_blind_safe(packet)
        _assert_blind_safe(existing_verified_ledger_digest or {})
        _assert_blind_safe(unresolved_question_state)
        _assert_blind_safe(pass_inputs or {})
        target = packet.get("target") or {}
        if not isinstance(target, Mapping):
            raise ValueError("ResearchPacket target must be an object")
        symbol = str(target.get("symbol") or target.get("target_id") or "")
        company_name = str(target.get("company_name") or "")
        as_of_date = str(packet.get("as_of_date") or "")
        if not symbol or not company_name or not as_of_date:
            raise ValueError("compiled prompt requires target symbol/company and as_of_date")
        plan = build_research_question_plan(primary_archetype_ids)
        declared = set(str(value) for value in packet.get("candidate_archetypes") or ())
        if declared and not set(primary_archetype_ids).issubset(declared):
            raise ValueError("compiled primary contracts escape packet candidate roster")
        context = self._render_context(
            packet=packet,
            plan=plan,
            pass_name=pass_name,
            existing_verified_ledger_digest=existing_verified_ledger_digest or {},
            unresolved_question_state=unresolved_question_state,
            pass_inputs=pass_inputs or {},
            conversation_id=conversation_id,
        )
        template_path = self.template_root / PASS_TEMPLATE_FILES[pass_name]
        template = template_path.read_text(encoding="utf-8")
        if template.count("{{COMPILED_CONTEXT}}") != 1:
            raise ValueError(f"prompt template requires one context slot: {template_path}")
        prompt = template.replace("{{COMPILED_CONTEXT}}", context).rstrip() + "\n"
        if "{{" in prompt or "}}" in prompt:
            raise ValueError("compiled prompt contains an unresolved template variable")
        return CompiledProResearchPromptV2(
            pass_name=pass_name,
            primary_archetype_ids=tuple(primary_archetype_ids),
            contract_ids=plan.bundle.contract_ids,
            mandatory_question_ids=plan.mandatory_question_ids,
            prompt_text=prompt,
            prompt_hash=canonical_hash({"prompt_text": prompt}),
        )

    def compile_contract_snapshot(
        self,
        *,
        packet: Mapping[str, Any],
        archetype_id: str,
    ) -> CompiledProResearchPromptV2:
        """Compile one contract in isolation for the 36-record CI audit.

        Primary snapshots use the real job compiler and therefore include all
        four mandatory cross guards.  A cross-guard unit snapshot contains only
        that guard; actual jobs still attach all four through ``compile``.
        """

        contract = load_research_contract(archetype_id)
        if contract["contract_role"] == "PRIMARY":
            return self.compile(
                packet=packet,
                primary_archetype_ids=(archetype_id,),
            )
        _assert_blind_safe(packet)
        template = (
            self.template_root / PASS_TEMPLATE_FILES["INITIAL_FULL_RESEARCH"]
        ).read_text(encoding="utf-8")
        context_lines = [
            "## CompiledProResearchPromptV2 contract-unit snapshot",
            "",
            "- pass_name: `INITIAL_FULL_RESEARCH`",
            f"- target: `{(packet.get('target') or {}).get('symbol')} {(packet.get('target') or {}).get('company_name')}`",
            f"- as_of_date: `{packet.get('as_of_date')}`",
            "- contract_unit_snapshot: `true`",
            "- actual_job_attachment_mode: `ALL_FOUR_R13_CROSS_GUARDS`",
            "- output_schema: `e2r_pro_research_dossier_v2`",
            "- score_authority: `false`",
            "- stage_authority: `false`",
            "- future_source_allowed: `false`",
            "",
            "## R13 cross-guard contract",
            "",
            *_render_contract(contract),
        ]
        prompt = template.replace(
            "{{COMPILED_CONTEXT}}",
            "\n".join(context_lines),
        ).rstrip() + "\n"
        mandatory_ids = tuple(
            str(row["question_family_id"])
            for row in contract["question_families"]
            if row["mandatory_for_full_thesis"] is True
        )
        return CompiledProResearchPromptV2(
            pass_name="INITIAL_FULL_RESEARCH",
            primary_archetype_ids=(),
            contract_ids=(archetype_id,),
            mandatory_question_ids=mandatory_ids,
            prompt_text=prompt,
            prompt_hash=canonical_hash({"prompt_text": prompt}),
        )

    def _render_context(
        self,
        *,
        packet: Mapping[str, Any],
        plan: ResearchQuestionPlan,
        pass_name: str,
        existing_verified_ledger_digest: Mapping[str, Any],
        unresolved_question_state: Sequence[Mapping[str, Any]],
        pass_inputs: Mapping[str, Any],
        conversation_id: str | None,
    ) -> str:
        target = packet["target"]
        lines = [
            "## CompiledProResearchPromptV2 authority",
            "",
            "- prompt_contract_version: `v2`",
            f"- pass_name: `{pass_name}`",
            f"- job_id: `{packet.get('job_id')}`",
            f"- run_id: `{packet.get('run_id')}`",
            f"- target: `{target.get('symbol') or target.get('target_id')} {target.get('company_name')}`",
            f"- as_of_date: `{packet.get('as_of_date')}`",
            f"- conversation_id: `{conversation_id or 'TO_BE_BOUND_BY_ORCHESTRATOR'}`",
            "- same_conversation_scope_required: `true`",
            "- output_schema: `e2r_pro_research_dossier_v2`",
            "- score_authority: `false`",
            "- stage_authority: `false`",
            "- future_source_allowed: `false`",
            "- investment_recommendation_allowed: `false`",
            "",
            "packet의 candidate 밖 ID가 더 적합하면 새 ID를 만들지 말고 `ARCHETYPE_RESELECTION_REQUIRED`와 registry ID 및 source-backed 근거를 반환한다.",
            "",
            "## 허용 question 상태",
            "",
            "Terminal: " + ", ".join(f"`{value}`" for value in TERMINAL_STATUSES),
            "",
            "Non-terminal: " + ", ".join(f"`{value}`" for value in NONTERMINAL_STATUSES),
            "",
            "## 선택된 primary research contracts",
            "",
        ]
        for contract in plan.bundle.primary_contracts:
            lines.extend(_render_contract(contract))
        lines.extend(["## 모든 job에 적용되는 R13 cross guards", ""])
        for contract in plan.bundle.cross_guard_contracts:
            lines.extend(_render_contract(contract))
        context_payload = {
            "packet_context": {
                "target": packet.get("target"),
                "as_of_date": packet.get("as_of_date"),
                "research_mode": packet.get("research_mode"),
                "trigger_summary": packet.get("trigger_summary"),
                "business_snapshot": packet.get("business_snapshot"),
                "structured_financial_snapshot": packet.get("structured_financial_snapshot"),
                "revision_valuation_snapshot": packet.get("revision_valuation_snapshot"),
                "known_positive_facts": packet.get("known_positive_facts"),
                "known_counterfacts": packet.get("known_counterfacts"),
            },
            "existing_verified_ledger_digest": existing_verified_ledger_digest,
            "unresolved_question_state": list(unresolved_question_state),
            "pass_inputs": pass_inputs,
        }
        lines.extend(
            [
                "## 현재 packet·ledger·gap context",
                "",
                "```json",
                json.dumps(context_payload, ensure_ascii=False, indent=2, sort_keys=True),
                "```",
                "",
                "이 JSON은 연구 입력이며 정답·score·Stage authority가 아니다. existing accepted fact는 append-only로 보존한다.",
            ]
        )
        return "\n".join(lines)


def _render_contract(contract: Mapping[str, Any]) -> list[str]:
    lines = [
        f"### `{contract['archetype_id']}`",
        "",
        f"- role: `{contract['contract_role']}`",
        f"- mechanism: {contract['economic_mechanism']}",
        f"- required_bridge_axes: {', '.join(contract['required_bridge_axes']) or 'GUARD_ONLY'}",
        f"- source roles: {contract['source_role_policy']['recommended_routes']}",
        f"- false-positive guard: {contract['false_positive_guards'][0]}",
        "- score_authority: `false`",
        "- stage_authority: `false`",
        "",
        "Mandatory question families:",
        "",
    ]
    for index, question in enumerate(contract["question_families"], 1):
        source_roles = ", ".join(question["required_source_roles"])
        primitives = ", ".join(question["required_primitives"]) or "QUESTION_SPECIFIC_DIRECT_PREDICATE"
        components = ", ".join(question["affected_component_ids"]) or "GUARD_ONLY"
        lines.extend(
            [
                f"{index}. `{question['question_family_id']}` — {question['question_text']}",
                f"   - roles: {', '.join(question['question_roles'])}",
                f"   - primitives: {primitives}",
                f"   - source roles: {source_roles}",
                f"   - affected components: {components}",
                f"   - adequate search: official-first, routes>={question['adequate_search_requirements']['minimum_distinct_source_routes']}, no-new-route confirmations=2",
                f"   - guard: {question['false_positive_guards'][0]}",
            ]
        )
    lines.append("")
    return lines


def _assert_blind_safe(value: Any, path: tuple[str, ...] = ()) -> None:
    forbidden = {
        "expected_score",
        "expected_stage",
        "gold_score",
        "gold_stage",
        "gold_answer",
        "future_outcome",
        "forward_return",
        "mfe",
        "mae",
    }
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalized = str(key).casefold().replace("-", "_")
            if normalized in forbidden:
                raise ValueError(f"forbidden answer field in prompt input: {'/'.join((*path, str(key)))}")
            _assert_blind_safe(child, (*path, str(key)))
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, child in enumerate(value):
            _assert_blind_safe(child, (*path, str(index)))


__all__ = [
    "CompiledProResearchPromptV2",
    "NONTERMINAL_STATUSES",
    "PASS_TEMPLATE_FILES",
    "ProResearchPromptCompilerV2",
    "TERMINAL_STATUSES",
]
