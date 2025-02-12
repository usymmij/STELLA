import carla 

class Sensors: 
    def __init__(self, world, vehicle):
        self.world = world
        self.vehicle = vehicle
        self.sensors = []

    def add_gps_sensor(self):
        blueprint_library = self.world.get_blueprint_library()
        gps_bp = blueprint_library.find('sensor.other.gnss')
        spawn_point = carla.Transform(carla.Location(x=0, z=2.0))
        gps_sensor = self.world.spawn_actor(gps_bp, spawn_point, attach_to=self.vehicle)
        gps_sensor.listen(self.process_gps_data)
        self.sensors.append(gps_sensor)
        print("GPS sensor attached.")
        return gps_sensor
    
    def process_gps_data(self, gps):
        gps_entry = {
            "latitude": gps.latitude,
            "longitude": gps.longitude,
            "altitude": gps.altitude
        }
        self.gps_data.append(gps_entry)
        print(f"Collected GPS Data: {gps_entry}")

    def get_collected_gps_data(self):
        return self.gps_data
