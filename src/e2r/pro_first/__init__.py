"""Pro-first browser research platform.

ChatGPT Pro may propose research material, but deterministic E2R layers retain
all EvidenceFact, score, and canonical Stage authority.
"""

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
    "PersistentKrxScheduler",
    "SystemClock",
]
