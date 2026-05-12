import logging
from typing import Any, Callable, Dict
from jsonrpcserver import method, serve

logger = logging.getLogger(__name__)


class MCPServer:
    """Base MCP server implementing JSON-RPC 2.0 transport."""

    def __init__(self, name: str, host: str = "localhost", port: int = 8000):
        self.name = name
        self.host = host
        self.port = port
        self.tools: Dict[str, Callable] = {}

    def register_tool(self, name: str, description: str = ""):
        def decorator(fn: Callable) -> Callable:
            self.tools[name] = fn
            fn.__doc__ = description
            logger.info(f"Registered tool: {name}")
            return fn
        return decorator

    def list_tools(self) -> list:
        return [
            {"name": name, "description": getattr(fn, "__doc__", "")}
            for name, fn in self.tools.items()
        ]

    def start(self):
        logger.info(f"Starting MCP server '{self.name}' on {self.host}:{self.port}")
        serve(self.host, self.port)
