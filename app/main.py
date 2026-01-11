from fastapi import FastAPI, Request, HTTPException
from app.schemas import RideRequest
from app.rate_limiter import rate_limit
from app.ride_queue import enqueue_ride

app = FastAPI(title="RideFlow Backend")

@app.post("/request-ride")
async def request_ride(ride: RideRequest, request: Request):
    try:
        rate_limit(f"ride:{request.client.host}")
    except Exception as e:
        raise HTTPException(status_code=429, detail=str(e))

    enqueue_ride(ride.dict())
    return {"status": "Ride queued successfully"}
