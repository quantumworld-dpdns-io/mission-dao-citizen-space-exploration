import logging
from .server import MCPServer

logger = logging.getLogger(__name__)


def create_telemetry_server() -> MCPServer:
    server = MCPServer(name="telemetry-api", port=8004)

    @server.register_tool("query_telemetry", "Query satellite telemetry data")
    def query_telemetry(satellite_id: str, parameter: str = "all") -> dict:
        """Query telemetry data for a specific satellite."""
        logger.info(f"Querying telemetry for satellite {satellite_id}")
        return {
            "satellite_id": satellite_id,
            "parameter": parameter,
            "samples": [{"timestamp": "2026-01-01T00:00:00Z", "value": 42.0}],
        }

    @server.register_tool("verify_telemetry_proof", "Verify a ZK proof for telemetry data")
    def verify_telemetry_proof(proof_cid: str, commitment: str) -> dict:
        """Verify a zero-knowledge proof of telemetry data integrity."""
        logger.info(f"Verifying telemetry proof: {proof_cid}")
        return {"proof_cid": proof_cid, "valid": True, "verified_at": "2026-01-01T00:00:00Z"}

    return server
