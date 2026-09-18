from app.gpu_workers import parking_zones

def get_best_available_zone():
    """
    Load Balancer Rules:
    1. Zone me free spots hone chahiye (free_spots > 0).
    2. Active GPU requests 4 se kam hone chahiye (active_gpu_requests < 4).
    3. Sabse kam active GPU requests wale zone ko priority milegi.
    """
    eligible_zones = [
        zone for zone in parking_zones 
        if zone.free_spots > 0 and zone.active_gpu_requests < 4
    ]

    if not eligible_zones:
        return None

    # Pick node with min active requests and max free spots
    best_zone = min(
        eligible_zones, 
        key=lambda z: (z.active_gpu_requests, -z.free_spots)
    )

    return best_zone