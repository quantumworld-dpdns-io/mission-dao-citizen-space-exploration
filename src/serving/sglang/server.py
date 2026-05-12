"""SGLang server launch configuration for mission data inference."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class SGLangServerConfig:
    model_path: str = "meta-llama/Llama-3.1-8B-Instruct"
    host: str = "0.0.0.0"
    port: int = 30000
    max_total_tokens: int = 16384
    max_running_requests: int = 64
    enable_flashinfer: bool = True
    enable_metrics: bool = True
    dp_size: int = 1
    tp_size: int = 1

    def to_launch_args(self) -> list:
        args = [
            "python", "-m", "sglang.launch_server",
            "--model-path", self.model_path,
            "--host", self.host,
            "--port", str(self.port),
            "--max-total-tokens", str(self.max_total_tokens),
            "--max-running-requests", str(self.max_running_requests),
        ]
        if self.enable_flashinfer:
            args.append("--enable-flashinfer")
        if self.enable_metrics:
            args.append("--enable-metrics")
        if self.dp_size > 1:
            args.extend(["--dp-size", str(self.dp_size)])
        if self.tp_size > 1:
            args.extend(["--tp-size", str(self.tp_size)])
        return args

    def to_yaml(self) -> str:
        return f"""model_path: {self.model_path}
host: {self.host}
port: {self.port}
max_total_tokens: {self.max_total_tokens}
max_running_requests: {self.max_running_requests}
enable_flashinfer: {self.enable_flashinfer}
enable_metrics: {self.enable_metrics}
"""
