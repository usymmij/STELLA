import carla

def opendrive_to_gnss(world: carla.World, road_id: int, lane_id: int, s: float, offset: float = 0.0):
    carla_map = world.get_map()
    
    waypoint = carla_map.get_waypoint_xodr(road_id, lane_id, s)
    
    if waypoint is None:
        raise ValueError("Invalid OpenDRIVE coordinates")

    location = waypoint.transform.location
    location.y += offset

    gnss_location = carla_map.transform_to_geolocation(location)
    
    return {
        "latitude": gnss_location.latitude,
        "longitude": gnss_location.longitude,
        "altitude": gnss_location.altitude
    }

