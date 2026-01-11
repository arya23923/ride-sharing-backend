from fastapi import FastAPI, Request, HTTPException
import asyncio

from schemas import RideRequest
from rate_limiter import rate_limit
from app.ride_queue import enqueue_ride
from workers import start_workers

app = FastAPI(title="RideFlow Backend")

@app.on_event("startup")
async def startup():
    asyncio.create_task(start_workers(4))

@app.post("/request-ride")
async def request_ride(ride: RideRequest, request: Request):
    try:
        rate_limit(f"ride:{request.client.host}")
    except Exception as e:
        raise HTTPException(status_code=429, detail=str(e))

    enqueue_ride(ride.dict())
    return {"status": "Ride queued successfully"}
