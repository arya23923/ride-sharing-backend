# app/queue.py
import redis
import json

r = redis.Redis(decode_responses=True)
QUEUE = "ride_queue"

def enqueue_ride(ride: dict):
    r.rpush(QUEUE, json.dumps(ride))

def dequeue_ride():
    _, ride = r.blpop(QUEUE)
    return json.loads(ride)
