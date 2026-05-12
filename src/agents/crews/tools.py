def query_telemetry(satellite_id: str, parameter: str = "all") -> dict:
    """Query telemetry data from a satellite via MCP."""
    return {"satellite_id": satellite_id, "parameter": parameter, "status": "simulated"}


def submit_proposal_to_chain(proposal_data: dict) -> str:
    """Submit a governance proposal on-chain via MCP."""
    return f"proposal_{proposal_data.get('proposal_id', 'unknown')}_submitted"


def fetch_community_votes(proposal_id: str) -> dict:
    """Fetch current vote tally for a proposal via MCP."""
    return {"proposal_id": proposal_id, "for": 0, "against": 0}
