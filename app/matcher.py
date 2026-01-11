# app/matcher.py
import asyncio
import random

async def match_driver(ride):
    await asyncio.sleep(1)  # simulate geo lookup
    return {
        "ride_id": ride["rider_id"],
        "driver_id": random.randint(1000, 9999)
    }
