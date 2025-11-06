from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
import os

# Initialize tracer provider
provider = TracerProvider()
trace.set_tracer_provider(provider)

# Configure OTLP exporter
otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317")
otlp_headers = os.getenv("OTEL_EXPORTER_OTLP_HEADERS", "")

if otlp_headers:
    headers = dict(item.split("=") for item in otlp_headers.split(","))
    span_exporter = OTLPSpanExporter(
        endpoint=otlp_endpoint,
        headers=headers
    )
else:
    span_exporter = OTLPSpanExporter(endpoint=otlp_endpoint)

# Add span processor
span_processor = BatchSpanProcessor(span_exporter)
provider.add_span_processor(span_processor)

# Initialize tracer
tracer = trace.get_tracer(__name__)

def instrument_app(app):
    """Instrument the FastAPI application for tracing"""
    FastAPIInstrumentor.instrument_app(app)
    HTTPXClientInstrumentor().instrument()
    SQLAlchemyInstrumentor().instrument()
    RequestsInstrumentor().instrument()
    
    # OpenAI instrumentation if available
    try:
        OpenAIInstrumentor().instrument()
    except:
        pass  # OpenAI may not be installed

def trace_agent_execution(agent_type: str, tenant_id: str, lead_id: str):
    """Decorator to trace agent execution"""
    def decorator(func):
        async def wrapper(*args, **kwargs):
            with tracer.start_as_current_span(f"agent_execution_{agent_type}") as span:
                span.set_attribute("agent.type", agent_type)
                span.set_attribute("tenant.id", tenant_id)
                span.set_attribute("lead.id", lead_id)
                
                try:
                    result = await func(*args, **kwargs)
                    span.set_attribute("execution.success", True)
                    return result
                except Exception as e:
                    span.set_attribute("execution.success", False)
                    span.set_attribute("execution.error", str(e))
                    raise
        return wrapper
    return decorator

def trace_step(step_name: str):
    """Decorator to trace individual agent steps"""
    def decorator(func):
        async def wrapper(*args, **kwargs):
            with tracer.start_as_current_span(f"agent_step_{step_name}") as span:
                span.set_attribute("step.name", step_name)
                
                try:
                    result = await func(*args, **kwargs)
                    span.set_attribute("step.success", True)
                    return result
                except Exception as e:
                    span.set_attribute("step.success", False)
                    span.set_attribute("step.error", str(e))
                    raise
        return wrapper
    return decorator