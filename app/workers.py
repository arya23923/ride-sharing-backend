import asyncio
from app.ride_queue import dequeue_ride
from matcher import match_driver

async def worker(worker_id: int):
    print(f"Worker {worker_id} started")
    while True:
        ride = dequeue_ride()
        result = await match_driver(ride)
        print(f"Worker {worker_id} → Driver {result['driver_id']} assigned")

async def start_workers(count=4):
    await asyncio.gather(*(worker(i) for i in range(count)))
