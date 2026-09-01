"""Contract-driven Pro-first V2 research planning surface."""

from .loader import (
    CROSS_GUARD_IDS,
    ContractBundle,
    load_all_research_contracts,
    load_research_contract,
    select_contract_bundle,
)
from .totality_audit import compile_contract_totality_audit
from .validator import ContractValidationError, validate_contract_catalog
from .prompt_compiler import CompiledProResearchPromptV2, ProResearchPromptCompilerV2
from .prompt_compiler_v3 import (
    CompiledProResearchPromptV3,
    ProResearchPromptCompilerV3,
)
from .question_planner import (
    PlannedQuestion,
    ResearchQuestionPlan,
    build_research_question_plan,
    validate_archetype_reselection,
)
from .snapshot_audit import compile_prompt_snapshot_audit
from .snapshot_audit_v3 import (
    compile_initial_prompt_v3_snapshot_audit,
    render_initial_prompt_v3_audit_markdown,
)

__all__ = [
    "CROSS_GUARD_IDS",
    "ContractBundle",
    "ContractValidationError",
    "CompiledProResearchPromptV2",
    "CompiledProResearchPromptV3",
    "PlannedQuestion",
    "ProResearchPromptCompilerV2",
    "ProResearchPromptCompilerV3",
    "ResearchQuestionPlan",
    "build_research_question_plan",
    "compile_contract_totality_audit",
    "compile_prompt_snapshot_audit",
    "compile_initial_prompt_v3_snapshot_audit",
    "load_all_research_contracts",
    "load_research_contract",
    "select_contract_bundle",
    "render_initial_prompt_v3_audit_markdown",
    "validate_archetype_reselection",
    "validate_contract_catalog",
]
