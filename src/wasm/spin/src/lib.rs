use spin_sdk::http::{IntoResponse, Request, Response};
use spin_sdk::http_component;

/// Mission status endpoint: returns current mission count and statuses
#[http_component]
fn mission_status(_req: Request) -> anyhow::Result<impl IntoResponse> {
    let status = serde_json::json!({
        "missions": [
            {"id": "athena-1", "name": "Athena-1", "status": "active", "orbit": "LEO 550km"},
            {"id": "pioneer-1", "name": "Pioneer-1", "status": "funding", "orbit": "LEO 400km"}
        ],
        "total": 2
    });
    Ok(Response::builder()
        .status(200)
        .header("content-type", "application/json")
        .body(serde_json::to_string(&status)?)
        .build())
}

/// Funding calculator: computes required funding based on mission parameters
#[http_component]
fn funding_calculator(req: Request) -> anyhow::Result<impl IntoResponse> {
    let body = req.body();
    let params: serde_json::Value = serde_json::from_slice(body)?;

    let base_cost = params["base_cost"].as_f64().unwrap_or(10000.0);
    let duration_months = params["duration_months"].as_f64().unwrap_or(12.0);
    let team_size = params["team_size"].as_f64().unwrap_or(3.0);

    let total = base_cost * (1.0 + duration_months * 0.05 + team_size * 0.1);

    let result = serde_json::json!({
        "estimated_total": total,
        "base_cost": base_cost,
        "operations_cost": base_cost * duration_months * 0.05,
        "team_cost": base_cost * team_size * 0.1,
        "currency": "USD"
    });

    Ok(Response::builder()
        .status(200)
        .header("content-type", "application/json")
        .body(serde_json::to_string(&result)?)
        .build())
}

/// Telemetry summary: returns a summary of recent telemetry data
#[http_component]
fn telemetry_summary(_req: Request) -> anyhow::Result<impl IntoResponse> {
    let summary = serde_json::json!({
        "total_readings": 15420,
        "satellites": 2,
        "avg_temperature_c": 22.5,
        "avg_voltage_v": 4.2,
        "anomalies_detected": 3,
        "last_updated": "2026-05-12T00:00:00Z"
    });
    Ok(Response::builder()
        .status(200)
        .header("content-type", "application/json")
        .body(serde_json::to_string(&summary)?)
        .build())
}

/// Health check endpoint
#[http_component]
fn health_check(_req: Request) -> anyhow::Result<impl IntoResponse> {
    Ok(Response::builder()
        .status(200)
        .header("content-type", "application/json")
        .body(r#"{"status": "healthy", "version": "0.1.0"}"#)
        .build())
}
