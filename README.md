#  Ride sharing application Backend

RideFlow is a scalable, production-ready backend for a ride-sharing platform built with **FastAPI** and **Redis**. It implements **rate-limiting, asynchronous FIFO ride queueing, and parallel worker-based driver assignment**, demonstrating modern backend engineering and distributed systems design.

---

##  Features

- **FastAPI REST API**  
  Modern, type-safe endpoints for ride requests and management.

- **Redis-backed FIFO queue**  
  Ensures rides are processed in order and allows decoupling of API and worker processes.

- **Async Worker Pool**  
  Multiple workers process queued rides in parallel for real-time driver assignment.

- **Rate Limiting**  
  Per-client IP rate limiting to prevent abuse.

- **Non-blocking Architecture**  
  API endpoints remain responsive even under heavy load.

- **Clean Project Structure**  
  Absolute imports, modular architecture, and best practices for maintainable backend code.

---

##  Technologies Used

| Layer | Technology |
|-------|------------|
| Backend Framework | FastAPI |
| Queue & Caching | Redis |
| Async Workers | Python asyncio + Redis |
| Data Format | JSON |
| Server | Uvicorn ASGI |

---

##  Project Structure
```
ride-sharing-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── ride_queue.py        # Redis-based enqueue/dequeue
│   ├── workers.py           # Async worker logic
│   ├── worker_runner.py     # Worker entrypoint
│   ├── matcher.py           # Driver matching logic
│   ├── rate_limiter.py      # Redis-based rate limiting
│   └── schemas.py           # Pydantic request/response schemas
├── .venv/                   # Python virtual environment
└── requirements.txt
```

---

##  Quick Start 

###  Install Dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

###  Start Redis
```bash
redis-server
```

###  Run FastAPI Server
```bash
uvicorn app.main:app --reload
```

### Start Worker Pool (Separate Terminal)
```bash
python app/worker_runner.py
```

###  Access Swagger UI

Open in browser:
```
http://127.0.0.1:8000/docs
```

---

##  Testing

### Sample Ride Request

**POST** `/request-ride` with JSON:
```json
{
  "rider_id": 1,
  "pickup_lat": 12.97,
  "pickup_lng": 77.59,
  "dest_lat": 13.01,
  "dest_lng": 77.60
}
```

**Expected outcome:**
- API responds with `"Ride queued successfully"`
- Worker terminal prints driver assignment:
```
Worker 0 → Driver 4821 assigned
```

---

##  Architecture Overview

1. **API receives ride requests** → validated with Pydantic schemas.
2. **Rate limiter checks client IP** → prevents abuse.
3. **Ride queued in Redis FIFO list** → decouples API and processing.
4. **Async worker pool continuously dequeues rides** → assigns available drivers.
5. **Drivers assigned** → response printed/logged (can be extended to WebSockets or DB).

### Diagram:
```
[Rider Request] → [FastAPI API] → [Redis Queue] → [Async Workers] → [Driver Assignment]
```

---

##  Dependencies
```txt
fastapi
uvicorn[standard]
redis
pydantic
```

---

