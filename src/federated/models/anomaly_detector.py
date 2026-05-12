"""Telemetry anomaly detection model for federated learning."""

import torch
import torch.nn as nn


class AnomalyDetector(nn.Module):
    def __init__(self, input_dim: int = 10, hidden_dim: int = 64, latent_dim: int = 16):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return reconstructed

    def anomaly_score(self, x: torch.Tensor) -> torch.Tensor:
        reconstructed = self.forward(x)
        return torch.mean((x - reconstructed) ** 2, dim=1)
