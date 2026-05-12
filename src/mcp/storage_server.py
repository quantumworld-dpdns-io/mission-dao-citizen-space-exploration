import logging
from .server import MCPServer

logger = logging.getLogger(__name__)


def create_storage_server() -> MCPServer:
    server = MCPServer(name="ipfs-arweave-storage", port=8002)

    @server.register_tool("store_data", "Store data on IPFS/Arweave")
    def store_data(data: str, protocol: str = "ipfs") -> dict:
        """Store mission data on decentralized storage."""
        logger.info(f"Storing data via {protocol}")
        return {
            "cid": f"QmSimulatedCID{hash(data) % 10**8}",
            "protocol": protocol,
            "size_bytes": len(data),
        }

    @server.register_tool("retrieve_data", "Retrieve data from IPFS/Arweave")
    def retrieve_data(cid: str) -> dict:
        """Retrieve mission data by content identifier."""
        logger.info(f"Retrieving data: {cid}")
        return {"cid": cid, "data": f"simulated_mission_data_for_{cid}"}

    return server
