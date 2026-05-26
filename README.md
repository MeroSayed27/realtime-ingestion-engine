# Real-Time MRV Ingestion Engine

A high-concurrency backend ingestion gateway built to process real-time environmental sensor telemetry data seamlessly.

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Data Validation:** Pydantic
- **Server:** Uvicorn

## 🚀 Features
- **Asynchronous Ingestion:** Built to handle concurrent JSON data streams from remote telemetry edge sensors.
- **Validation Layer:** Enforces data structural integrity at the point of entry using Pydantic baseline data types.
- **Threshold Anomaly Detection:** Instantly flags metric spikes (Carbon or Temperature values exceeding safety limits).
- **Observability:** Formats clean, production-ready terminal logs detailing metrics status, data payload values, and precise execution timestamps.