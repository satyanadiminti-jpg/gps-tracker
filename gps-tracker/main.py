from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# In-memory store
locations = {}

class GPSData(BaseModel):
    truck_id: str
    lat: float
    lon: float

@app.post("/gps")
def update_location(data: GPSData):
    locations[data.truck_id] = {"lat": data.lat, "lon": data.lon}
    return {"status": "ok"}

@app.get("/location/{truck_id}")
def get_location(truck_id: str):
    return locations.get(truck_id, {"error": "not found"})

# Serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")
