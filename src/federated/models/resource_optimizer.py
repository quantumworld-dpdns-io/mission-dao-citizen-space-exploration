"""Resource optimization model for federated learning."""

import torch
import torch.nn as nn


class ResourceOptimizer(nn.Module):
    def __init__(
        self,
        input_dim: int = 8,
        hidden_dim: int = 128,
        output_dim: int = 4,
    ):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, output_dim),
            nn.Sigmoid(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)
