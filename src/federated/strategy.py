"""Federated learning strategies for telemetry model training."""

from typing import Dict, List, Optional, Tuple, Callable
import flwr as fl
from flwr.common import Metrics, Parameters, Scalar
from flwr.server.strategy import FedAvg, FedAdagrad


def _weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]
    return {"accuracy": sum(accuracies) / sum(examples)}


def get_fedavg_strategy(
    fraction_fit: float = 1.0,
    fraction_evaluate: float = 1.0,
    min_fit_clients: int = 2,
    min_evaluate_clients: int = 2,
    min_available_clients: int = 2,
    config: Optional[Dict] = None,
) -> FedAvg:
    return FedAvg(
        fraction_fit=fraction_fit,
        fraction_evaluate=fraction_evaluate,
        min_fit_clients=min_fit_clients,
        min_evaluate_clients=min_evaluate_clients,
        min_available_clients=min_available_clients,
        evaluate_metrics_aggregation_fn=_weighted_average,
        fit_metrics_aggregation_fn=_weighted_average,
        on_fit_config_fn=lambda r: {
            "local_epochs": config.get("local_epochs", 5) if config else 5,
            "learning_rate": config.get("learning_rate", 0.001) if config else 0.001,
        },
    )


def get_fedadagrad_strategy(
    fraction_fit: float = 1.0,
    fraction_evaluate: float = 1.0,
    min_fit_clients: int = 2,
    min_evaluate_clients: int = 2,
    min_available_clients: int = 2,
    eta: float = 0.01,
    eta_l: float = 0.001,
) -> FedAdagrad:
    return FedAdagrad(
        fraction_fit=fraction_fit,
        fraction_evaluate=fraction_evaluate,
        min_fit_clients=min_fit_clients,
        min_evaluate_clients=min_evaluate_clients,
        min_available_clients=min_available_clients,
        evaluate_metrics_aggregation_fn=_weighted_average,
        eta=eta,
        eta_l=eta_l,
    )
