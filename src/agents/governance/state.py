from typing import TypedDict, Optional
from enum import Enum


class ProposalStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    VOTING = "voting"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXECUTED = "executed"


class ProposalState(TypedDict):
    proposal_id: str
    title: str
    description: str
    author: str
    status: ProposalStatus
    created_at: str
    updated_at: str
    review_notes: Optional[str]
    votes_for: int
    votes_against: int
    execution_result: Optional[str]
