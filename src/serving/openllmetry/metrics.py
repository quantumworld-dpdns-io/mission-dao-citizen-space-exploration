"""Custom OpenTelemetry metrics for telemetry monitoring."""

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.resources import Resource

_meter = None


class TelemetryMetrics:
    def __init__(self, meter: metrics.Meter):
        self.model_inference_latency = meter.create_histogram(
            name="mission.dao.model.inference.latency",
            description="Latency of model inference calls",
            unit="ms",
        )
        self.anomaly_count = meter.create_counter(
            name="mission.dao.anomaly.count",
            description="Number of anomalies detected",
        )
        self.proposal_votes = meter.create_counter(
            name="mission.dao.proposal.votes",
            description="Number of votes cast on proposals",
        )
        self.telemetry_points_ingested = meter.create_counter(
            name="mission.dao.telemetry.ingested",
            description="Telemetry data points ingested",
        )
        self.active_agents = meter.create_up_down_counter(
            name="mission.dao.agents.active",
            description="Number of active agent instances",
        )
        self.model_inference_tokens = meter.create_histogram(
            name="mission.dao.model.inference.tokens",
            description="Tokens generated per inference call",
            unit="tokens",
        )


def create_telemetry_histogram(
    meter: metrics.Meter,
    name: str,
    description: str = "",
    unit: str = "1",
) -> metrics.Histogram:
    return meter.create_histogram(
        name=name,
        description=description,
        unit=unit,
    )


def setup_metrics(
    service_name: str = "mission-dao",
    otlp_endpoint: str = "http://localhost:4317",
) -> TelemetryMetrics:
    resource = Resource.create({"service.name": service_name})
    reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(endpoint=otlp_endpoint, insecure=True)
    )
    provider = MeterProvider(resource=resource, metric_readers=[reader])
    metrics.set_meter_provider(provider)
    meter = metrics.get_meter(service_name)
    return TelemetryMetrics(meter=meter)
