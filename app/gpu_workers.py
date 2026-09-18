import asyncio

class ParkingGPUZone:
    def __init__(self, zone_id: str, name: str, total_spots: int):
        self.zone_id = zone_id          
        self.name = name                
        self.total_spots = total_spots  
        self.occupied_spots = 0         
        self.active_gpu_requests = 0    

    @property
    def free_spots(self):
        # Prevent negative values
        return max(0, self.total_spots - self.occupied_spots)

    def add_occupancy(self):
        # Strict total capacity check
        if self.occupied_spots < self.total_spots:
            self.occupied_spots += 1

    def get_status(self):
        return {
            "zone_id": self.zone_id,
            "name": self.name,
            "total_spots": self.total_spots,
            "occupied_spots": self.occupied_spots,
            "free_spots": self.free_spots,
            "active_gpu_requests": self.active_gpu_requests,
            "is_available": self.free_spots > 0
        }

# 3 GPU Parking Zones
parking_zones = [
    ParkingGPUZone("GPU-1", "Zone A (Ground Floor)", total_spots=10),
    ParkingGPUZone("GPU-2", "Zone B (First Floor)", total_spots=15),
    ParkingGPUZone("GPU-3", "Zone C (Second Floor)", total_spots=8),
]