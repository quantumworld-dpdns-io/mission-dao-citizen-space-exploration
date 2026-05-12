from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Proposal(BaseModel):
    proposal_id: str
    title: str
    description: str
    author: str
    status: str = "draft"
    created_at: datetime
    updated_at: datetime
    review_notes: Optional[str] = None
    votes_for: int = 0
    votes_against: int = 0
    execution_result: Optional[str] = None
