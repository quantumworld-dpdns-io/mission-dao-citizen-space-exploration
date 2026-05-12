"""Ollama API client for local model inference."""

import httpx
from typing import Dict, List, Optional, Iterator


class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip("/")
        self._client = httpx.Client(base_url=self.base_url, timeout=120)

    def generate(
        self,
        model: str,
        prompt: str,
        system: Optional[str] = None,
        stream: bool = False,
        options: Optional[Dict] = None,
    ) -> Dict:
        payload = {"model": model, "prompt": prompt, "stream": stream}
        if system:
            payload["system"] = system
        if options:
            payload["options"] = options
        resp = self._client.post("/api/generate", json=payload)
        resp.raise_for_status()
        return resp.json()

    def chat(self, model: str, messages: List[Dict], stream: bool = False) -> Dict:
        payload = {"model": model, "messages": messages, "stream": stream}
        resp = self._client.post("/api/chat", json=payload)
        resp.raise_for_status()
        return resp.json()

    def list_models(self) -> List[Dict]:
        resp = self._client.get("/api/tags")
        resp.raise_for_status()
        return resp.json().get("models", [])

    def pull_model(self, model: str) -> None:
        resp = self._client.post("/api/pull", json={"name": model})
        resp.raise_for_status()

    def close(self):
        self._client.close()
