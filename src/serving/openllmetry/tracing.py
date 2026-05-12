"""OpenTelemetry tracing setup for mission observability."""

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

_tracer = None


def setup_tracing(
    service_name: str = "mission-dao",
    otlp_endpoint: str = "http://localhost:4317",
    phoenix_endpoint: str = "http://localhost:6006",
) -> trace.Tracer:
    global _tracer
    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)

    # Primary OTLP exporter (e.g., Tempo, Jaeger)
    primary = OTLPSpanExporter(endpoint=otlp_endpoint, insecure=True)
    provider.add_span_processor(BatchSpanProcessor(primary))

    # Arize Phoenix exporter for LLM observability
    phoenix = OTLPSpanExporter(endpoint=f"{phoenix_endpoint}/v1/traces", insecure=True)
    provider.add_span_processor(BatchSpanProcessor(phoenix))

    trace.set_tracer_provider(provider)
    _tracer = trace.get_tracer(service_name)
    return _tracer


def get_tracer() -> trace.Tracer:
    global _tracer
    if _tracer is None:
        _tracer = setup_tracing()
    return _tracer
