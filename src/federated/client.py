"""Flower federated learning client for telemetry model training."""

from typing import Dict, List, Tuple, Optional
import flwr as fl
import torch
import numpy as np


class TelemetryFlowerClient(fl.client.NumPyClient):
    def __init__(
        self,
        model: torch.nn.Module,
        cid: str,
        train_data: Optional[torch.utils.data.Dataset] = None,
        val_data: Optional[torch.utils.data.Dataset] = None,
        device: str = "cpu",
    ):
        self.model = model
        self.cid = cid
        self.train_data = train_data
        self.val_data = val_data
        self.device = torch.device(device)

    def get_parameters(self, config: Dict) -> List[np.ndarray]:
        return [val.cpu().numpy() for _, val in self.model.state_dict().items()]

    def fit(
        self, parameters: List[np.ndarray], config: Dict
    ) -> Tuple[List[np.ndarray], int, Dict]:
        self._set_parameters(parameters)
        epochs = config.get("local_epochs", 5)
        lr = config.get("learning_rate", 0.001)

        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        self.model.train()
        self.model.to(self.device)

        if self.train_data:
            loader = torch.utils.data.DataLoader(self.train_data, batch_size=32, shuffle=True)
            for epoch in range(epochs):
                for batch in loader:
                    x, y = batch
                    x, y = x.to(self.device), y.to(self.device)
                    optimizer.zero_grad()
                    loss = self._compute_loss(x, y)
                    loss.backward()
                    optimizer.step()

        return self.get_parameters({}), len(self.train_data) if self.train_data else 0, {}

    def evaluate(
        self, parameters: List[np.ndarray], config: Dict
    ) -> Tuple[float, int, Dict]:
        self._set_parameters(parameters)
        self.model.eval()
        self.model.to(self.device)

        total_loss = 0.0
        correct = 0
        total = 0

        if self.val_data:
            loader = torch.utils.data.DataLoader(self.val_data, batch_size=32)
            with torch.no_grad():
                for batch in loader:
                    x, y = batch
                    x, y = x.to(self.device), y.to(self.device)
                    loss = self._compute_loss(x, y)
                    total_loss += loss.item() * len(x)
                    preds = self._predict(x)
                    correct += (preds == y).sum().item()
                    total += len(y)

        avg_loss = total_loss / total if total > 0 else 0.0
        accuracy = correct / total if total > 0 else 0.0
        return float(avg_loss), total, {"accuracy": float(accuracy)}

    def _set_parameters(self, parameters: List[np.ndarray]) -> None:
        params_dict = zip(self.model.state_dict().keys(), parameters)
        state_dict = {k: torch.tensor(v) for k, v in params_dict}
        self.model.load_state_dict(state_dict, strict=True)

    def _compute_loss(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        return torch.nn.functional.mse_loss(self.model(x), y)

    def _predict(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x).argmax(dim=1)
