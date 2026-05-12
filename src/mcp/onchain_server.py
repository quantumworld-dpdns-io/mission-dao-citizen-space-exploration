import logging
from .server import MCPServer

logger = logging.getLogger(__name__)


def create_onchain_server() -> MCPServer:
    server = MCPServer(name="onchain-queries", port=8003)

    @server.register_tool("submit_proposal", "Submit a governance proposal on-chain")
    def submit_proposal(proposal_id: str, title: str, description: str, author: str) -> dict:
        """Submit a governance proposal to the DAO contract."""
        logger.info(f"Submitting proposal: {proposal_id}")
        return {
            "tx_hash": f"0xSimulatedTxHash{proposal_id}",
            "proposal_id": proposal_id,
            "status": "submitted",
        }

    @server.register_tool("query_votes", "Query votes for a DAO proposal")
    def query_votes(proposal_id: str) -> dict:
        """Query current vote tally for an on-chain proposal."""
        logger.info(f"Querying votes for: {proposal_id}")
        return {"proposal_id": proposal_id, "for": 42, "against": 7, "total": 49}

    return server
