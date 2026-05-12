import logging
from .server import MCPServer

logger = logging.getLogger(__name__)


def create_github_server() -> MCPServer:
    server = MCPServer(name="github-issues", port=8001)

    @server.register_tool("create_issue", "Create a GitHub issue")
    def create_issue(title: str, body: str, labels: list = None) -> dict:
        """Create a new GitHub issue for a mission task."""
        logger.info(f"Creating issue: {title}")
        return {
            "url": "https://github.com/quantumworld-dpdns-io/mission-dao-citizen-space-exploration/issues/1",
            "title": title,
            "status": "created",
        }

    @server.register_tool("list_issues", "List GitHub issues by state")
    def list_issues(state: str = "open") -> list:
        """List GitHub issues filtered by state."""
        logger.info(f"Listing issues with state: {state}")
        return [{"number": 1, "title": "Sample issue", "state": state}]

    return server
