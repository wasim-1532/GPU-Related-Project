import asyncio
import uuid
from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.gpu_workers import parking_zones
from app.load_balancer import get_best_available_zone

app = FastAPI(title="Smart GPU Parking System")

app.mount("/static", StaticFiles(directory="static"), name="static")

tasks_db = {}

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/api/zones-status")
async def get_zones_status():
    return [zone.get_status() for zone in parking_zones]

@app.post("/api/book-parking")
async def book_parking(vehicle_number: str, background_tasks: BackgroundTasks):
    selected_zone = get_best_available_zone()
    
    if not selected_zone:
        raise HTTPException(
            status_code=400, 
            detail="All GPUs are busy (Max 4 requests per GPU) or Parking Zones are FULL. Please wait!"
        )

    job_id = str(uuid.uuid4())[:8]
    selected_zone.active_gpu_requests += 1

    tasks_db[job_id] = {
        "job_id": job_id,
        "vehicle": vehicle_number,
        "assigned_zone": selected_zone.name,
        "gpu_id": selected_zone.zone_id,
        "status": "PROCESSING"
    }

    # Background Execution with Error Safety
    async def process_allocation(zone, j_id):
        try:
            await asyncio.sleep(2) # GPU simulation delay
            zone.add_occupancy()
            tasks_db[j_id]["status"] = "CONFIRMED & ALLOCATED"
        except Exception as e:
            print(f"Error processing allocation: {e}")
        finally:
            zone.active_gpu_requests = max(0, zone.active_gpu_requests - 1)

    background_tasks.add_task(process_allocation, selected_zone, job_id)

    return {
        "message": "Request Accepted!",
        "job_id": job_id,
        "assigned_zone_name": selected_zone.name,
        "gpu_assigned": selected_zone.zone_id,
        "free_spots_remaining": selected_zone.free_spots
    }

@app.post("/api/reset-data")
async def reset_data():
    for zone in parking_zones:
        zone.occupied_spots = 0
        zone.active_gpu_requests = 0
    tasks_db.clear()
    return {"message": "All parking data and GPU requests reset successfully!"}