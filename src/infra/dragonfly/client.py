"""Dragonfly Redis-compatible cache client for real-time mission telemetry."""

import os
import json
from typing import Any, Dict, List, Optional, Union
import redis.asyncio as aioredis


class DragonflyCache:
    def __init__(self, url: Optional[str] = None):
        self.url = url or os.getenv("DRAGONFLY_URL", "redis://localhost:6379")
        self._client: Optional[aioredis.Redis] = None

    async def connect(self):
        if self._client is None:
            self._client = await aioredis.from_url(self.url, decode_responses=True)

    async def close(self):
        if self._client:
            await self._client.close()

    async def set_telemetry(self, satellite_id: str, data: Dict, ttl: int = 300) -> None:
        await self.connect()
        key = f"telemetry:{satellite_id}"
        await self._client.setex(key, ttl, json.dumps(data))

    async def get_telemetry(self, satellite_id: str) -> Optional[Dict]:
        await self.connect()
        data = await self._client.get(f"telemetry:{satellite_id}")
        return json.loads(data) if data else None

    async def cache_mission_summary(self, mission_id: str, summary: Dict, ttl: int = 600) -> None:
        await self.connect()
        key = f"mission:{mission_id}:summary"
        await self._client.setex(key, ttl, json.dumps(summary))

    async def get_mission_summary(self, mission_id: str) -> Optional[Dict]:
        await self.connect()
        data = await self._client.get(f"mission:{mission_id}:summary")
        return json.loads(data) if data else None

    async def add_active_agent(self, agent_id: str) -> None:
        await self.connect()
        await self._client.sadd("agents:active", agent_id)

    async def remove_active_agent(self, agent_id: str) -> None:
        await self.connect()
        await self._client.srem("agents:active", agent_id)

    async def get_active_agents(self) -> List[str]:
        await self.connect()
        return list(await self._client.smembers("agents:active"))

    async def increment_proposal_votes(self, proposal_id: str) -> int:
        await self.connect()
        return await self._client.incr(f"proposal:{proposal_id}:vote_count")

    async def get_proposal_votes(self, proposal_id: str) -> int:
        await self.connect()
        val = await self._client.get(f"proposal:{proposal_id}:vote_count")
        return int(val) if val else 0

    async def health_check(self) -> bool:
        try:
            await self.connect()
            return await self._client.ping()
        except Exception:
            return False
