"""Approval Gate.

Routes runs touching restricted material to a human approver before release.
"""

from permission_aware_retrieval.components.approval_gate.adapter import ROLE, build
from permission_aware_retrieval.components.approval_gate.config import CONFIG, ApprovalGateConfig
from permission_aware_retrieval.components.approval_gate.errors import ApprovalGateError
from permission_aware_retrieval.components.approval_gate.service import ApprovalGateService

__all__ = ["CONFIG", "ROLE", "build", "ApprovalGateConfig", "ApprovalGateError", "ApprovalGateService"]
