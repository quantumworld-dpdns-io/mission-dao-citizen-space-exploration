from datetime import datetime
from .state import ProposalState


def submit_proposal(state: ProposalState) -> dict:
    if not state.get("title") or not state.get("description"):
        raise ValueError("Proposal must have title and description")
    return {"status": ProposalState.__annotations__["status"].__args__[0].SUBMITTED,
            "updated_at": datetime.utcnow().isoformat()}


def review_proposal(state: ProposalState) -> dict:
    return {
        "status": "under_review",
        "review_notes": "Proposal meets minimum criteria",
        "updated_at": datetime.utcnow().isoformat(),
    }


def start_voting(state: ProposalState) -> dict:
    return {"status": "voting", "updated_at": datetime.utcnow().isoformat()}


def tally_votes(state: ProposalState) -> dict:
    total = state["votes_for"] + state["votes_against"]
    approval_rate = state["votes_for"] / total if total > 0 else 0
    return {"status": "approved" if approval_rate > 0.5 else "rejected",
            "updated_at": datetime.utcnow().isoformat()}


def execute_proposal(state: ProposalState) -> dict:
    if state["status"] != "approved":
        raise ValueError("Can only execute approved proposals")
    return {
        "status": "executed",
        "execution_result": f"Executed proposal: {state['proposal_id']}",
        "updated_at": datetime.utcnow().isoformat(),
    }
