"""Flower federated learning server for model aggregation."""

import flwr as fl
from typing import Dict, Optional
from .strategy import get_fedavg_strategy


def start_federated_server(
    num_rounds: int = 10,
    min_clients: int = 2,
    min_fit_clients: int = 2,
    min_evaluate_clients: int = 2,
    fraction_fit: float = 1.0,
    fraction_evaluate: float = 1.0,
    server_address: str = "0.0.0.0:8080",
    config: Optional[Dict] = None,
) -> fl.server.Server:
    strategy = get_fedavg_strategy(
        min_fit_clients=min_fit_clients,
        min_evaluate_clients=min_evaluate_clients,
        min_available_clients=min_clients,
        fraction_fit=fraction_fit,
        fraction_evaluate=fraction_evaluate,
        config=config or {},
    )

    fl.server.start_server(
        server_address=server_address,
        config=fl.server.ServerConfig(num_rounds=num_rounds),
        strategy=strategy,
    )
