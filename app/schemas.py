# app/schemas.py
from pydantic import BaseModel, Field

class RideRequest(BaseModel):
    rider_id: int
    pickup_lat: float = Field(..., ge=-90, le=90)
    pickup_lng: float = Field(..., ge=-180, le=180)
    dest_lat: float = Field(..., ge=-90, le=90)
    dest_lng: float = Field(..., ge=-180, le=180)
