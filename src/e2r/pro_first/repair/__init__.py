"""Verifier-repair packet, delta, and deterministic reverification API."""

from .audit import compile_verifier_repair_contract_audit
from .delta import apply_repair_delta
from .models import (
    REJECTION_CATEGORIES,
    REPAIR_ACTIONS,
    RepairActionDecision,
    RepairApplication,
    RepairResolution,
    VerifierRejectionPacket,
    VerifierRepairReceipt,
)
from .rejection_packet import (
    compile_rejection_packets,
    load_fact_compilation_rejection_rows,
    load_verification_rows,
)
from .response_delta import derive_repair_delta_from_dossier_response
from .service import (
    ProVerifierRepairService,
    VerifierRepairPlan,
    VerifierRepairRun,
)
from .delta_v3 import (
    RepairDeltaV3ValidationError,
    RepairDeltaV3Validator,
    apply_repair_delta_v3,
)
from .models_v3 import (
    CompactRepairGroupV3,
    CompiledCompactRepairPromptV3,
    PRO_REPAIRABLE_ROOT_CAUSES,
    REPAIR_ACTIONS_V3,
    REPAIR_ACTION_CONTRACT,
    REPAIR_DELTA_V3_SCHEMA_VERSION,
    RepairActionOutcomeV3,
    RepairApplicationV3,
)
from .parser_v3 import (
    ParsedRepairDeltaV3,
    RepairDeltaV3ParseError,
    RepairDeltaV3Parser,
)
from .prompt_v3 import CompactRepairPromptCompilerV3
from .service_v3 import CompactRepairRunV3, CompactRepairServiceV3

__all__ = [
    "REJECTION_CATEGORIES",
    "REPAIR_ACTIONS",
    "REPAIR_ACTIONS_V3",
    "REPAIR_ACTION_CONTRACT",
    "REPAIR_DELTA_V3_SCHEMA_VERSION",
    "PRO_REPAIRABLE_ROOT_CAUSES",
    "CompactRepairGroupV3",
    "CompiledCompactRepairPromptV3",
    "CompactRepairPromptCompilerV3",
    "CompactRepairRunV3",
    "CompactRepairServiceV3",
    "ParsedRepairDeltaV3",
    "ProVerifierRepairService",
    "RepairActionDecision",
    "RepairApplication",
    "RepairResolution",
    "VerifierRejectionPacket",
    "VerifierRepairPlan",
    "VerifierRepairReceipt",
    "VerifierRepairRun",
    "RepairActionOutcomeV3",
    "RepairApplicationV3",
    "RepairDeltaV3ParseError",
    "RepairDeltaV3Parser",
    "RepairDeltaV3ValidationError",
    "RepairDeltaV3Validator",
    "apply_repair_delta",
    "apply_repair_delta_v3",
    "compile_rejection_packets",
    "compile_verifier_repair_contract_audit",
    "derive_repair_delta_from_dossier_response",
    "load_fact_compilation_rejection_rows",
    "load_verification_rows",
]
