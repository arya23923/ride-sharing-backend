# app/rate_limiter.py
import time
import redis

r = redis.Redis(decode_responses=True)

RATE_LIMIT = 5
WINDOW = 60  # seconds

def rate_limit(key: str):
    now = int(time.time())

    pipe = r.pipeline()
    pipe.zadd(key, {now: now})
    pipe.zremrangebyscore(key, 0, now - WINDOW)
    pipe.zcard(key)
    pipe.expire(key, WINDOW)
    _, _, count, _ = pipe.execute()

    if count > RATE_LIMIT:
        raise Exception("Rate limit exceeded")
