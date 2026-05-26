from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Real-Time MRV Ingestion Engine")

class TelemetryData(BaseModel):
    sensor_id: str
    carbon_value: float
    temperature: float

@app.post("/ingest")
def ingest_metrics(data: TelemetryData):
    is_anomaly = bool(data.carbon_value > 500.0 or data.temperature > 45.0)
    status_text = "[ALERT] ANOMALY DETECTED" if is_anomaly else "[OK] VALID METRIC"

    print("=" * 55)
    print(f"[{datetime.now().strftime("%%Y-%%m-%%d %%H:%%M:%%S")}] INGESTION LOG")
    print(f" Sensor ID : {data.sensor_id}")
    print(f" Carbon    : {data.carbon_value} ppm")
    print(f" Temp      : {data.temperature} C")
    print(f" Status    : {status_text}")
    print("=" * 55)

    return {"status": "processed", "sensor_id": data.sensor_id, "anomaly_detected": is_anomaly}