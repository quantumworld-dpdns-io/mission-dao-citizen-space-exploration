"""SGLang runtime client for high-throughput structured generation."""

import httpx
from typing import Dict, List, Optional


class SGLangClient:
    def __init__(self, base_url: str = "http://localhost:30000"):
        self.base_url = base_url.rstrip("/")
        self._client = httpx.Client(base_url=self.base_url, timeout=300)

    def generate(
        self,
        model: str,
        prompt: str,
        max_tokens: int = 512,
        temperature: float = 0.7,
        top_p: float = 0.95,
    ) -> Dict:
        payload = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
        }
        resp = self._client.post("/v1/completions", json=payload)
        resp.raise_for_status()
        return resp.json()

    def generate_structured(
        self,
        model: str,
        prompt: str,
        json_schema: Dict,
        temperature: float = 0.1,
    ) -> Dict:
        payload = {
            "model": model,
            "prompt": prompt,
            "temperature": temperature,
            "response_format": {"type": "json_object", "schema": json_schema},
            "max_tokens": 1024,
        }
        resp = self._client.post("/v1/completions", json=payload)
        resp.raise_for_status()
        return resp.json()

    def chat(self, model: str, messages: List[Dict], temperature: float = 0.7) -> Dict:
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        resp = self._client.post("/v1/chat/completions", json=payload)
        resp.raise_for_status()
        return resp.json()

    def get_server_info(self) -> Dict:
        resp = self._client.get("/v1/models")
        resp.raise_for_status()
        return resp.json()

    def close(self):
        self._client.close()
