"""Pro-first browser research platform.

ChatGPT Pro may propose research material, but deterministic E2R layers retain
all EvidenceFact, score, and canonical Stage authority.
"""

from .approval import ExactlyOnceSubmitCoordinator, ProApprovalService
from .job_store import ProFirstJobStore
from .models import (
    CandidateRecord,
    JobEvent,
    JobStatus,
    ProResearchJob,
    ResearchMode,
    ScanRunRecord,
    ScanWindow,
)
from .packet import PacketBuildInput, ResearchPacketBuilder, ResearchPacketV1
from .prompt_contract import ProResearchPromptContract
from .scheduler import FrozenClock, PersistentKrxScheduler, SystemClock
from .state_machine import ProJobStateMachine

__all__ = [
    "CandidateRecord",
    "JobEvent",
    "JobStatus",
    "ProFirstJobStore",
    "ProJobStateMachine",
    "ProResearchJob",
    "ResearchMode",
    "ScanRunRecord",
    "ScanWindow",
    "FrozenClock",
    "ExactlyOnceSubmitCoordinator",
    "PersistentKrxScheduler",
    "PacketBuildInput",
    "ProResearchPromptContract",
    "ProApprovalService",
    "ResearchPacketBuilder",
    "ResearchPacketV1",
    "SystemClock",
]
