"""Google Universal Commerce Protocol (UCP) client for mission funding checkout."""

import os
import httpx
from typing import Dict, Optional
from dataclasses import dataclass


@dataclass
class UCPProduct:
    id: str
    title: str
    description: str
    price_usd: float
    currency: str = "USD"


class UCPClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("UCP_API_KEY", "")
        self.base_url = os.getenv("UCP_BASE_URL", "https://ucp.googleapis.com/v1")
        self._client = httpx.Client(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
        )

    def create_checkout_session(
        self,
        product: UCPProduct,
        buyer_address: str,
        success_url: str,
        cancel_url: str,
    ) -> Dict:
        payload = {
            "product": {
                "id": product.id,
                "title": product.title,
                "description": product.description,
                "price": {"amount": product.price_usd, "currency": product.currency},
            },
            "buyer": {"address": buyer_address},
            "redirects": {
                "success_url": success_url,
                "cancel_url": cancel_url,
            },
        }
        resp = self._client.post("/checkout/sessions", json=payload)
        resp.raise_for_status()
        return resp.json()

    def get_session_status(self, session_id: str) -> Dict:
        resp = self._client.get(f"/checkout/sessions/{session_id}")
        resp.raise_for_status()
        return resp.json()

    def list_products(self) -> list:
        resp = self._client.get("/products")
        resp.raise_for_status()
        return resp.json().get("products", [])


MISSION_FUNDING_PRODUCTS = {
    "athena-1-launch": UCPProduct(
        id="athena-1-launch",
        title="Athena-1 Launch Contribution",
        description="Contribute to the Athena-1 CubeSat launch campaign",
        price_usd=50.0,
    ),
    "pioneer-1-payload": UCPProduct(
        id="pioneer-1-payload",
        title="Pioneer-1 Sensor Package",
        description="Fund a multispectral imaging sensor for Pioneer-1",
        price_usd=100.0,
    ),
}
