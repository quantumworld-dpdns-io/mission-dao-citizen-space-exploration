from langgraph.graph import StateGraph, START
from .state import ProposalState
from .nodes import (
    submit_proposal,
    review_proposal,
    start_voting,
    tally_votes,
    execute_proposal,
)


def should_execute(state: ProposalState) -> str:
    return "execute" if state["status"] == "approved" else "end"


def build_proposal_graph() -> StateGraph:
    workflow = StateGraph(ProposalState)

    workflow.add_node("submit", submit_proposal)
    workflow.add_node("review", review_proposal)
    workflow.add_node("vote", start_voting)
    workflow.add_node("tally", tally_votes)
    workflow.add_node("execute", execute_proposal)

    workflow.add_edge(START, "submit")
    workflow.add_edge("submit", "review")
    workflow.add_edge("review", "vote")
    workflow.add_edge("vote", "tally")
    workflow.add_conditional_edges("tally", should_execute, {"execute": "execute", "end": "__end__"})
    workflow.add_edge("execute", "__end__")

    return workflow.compile()


# Singleton instance
proposal_graph = build_proposal_graph()
