import carla 

class Sensors: 
    def __init__(self, world, vehicle):
        self.world = world
        self.vehicle = vehicle
        self.sensors = [] # to keep track of attached sensors (can remove if we want just good for cleanup)

    def add_gps_sensor(self):
        blueprint_library = self.world.get_blueprint_library()
        gps_bp = blueprint_library.find('sensor.other.gnss')
        spawn_point = carla.Transform(carla.Location(x=0, z=2.0)) # can adjust position if we need
        gps_sensor = self.world.spawn_actor(gps_bp, spawn_point, attach_to=self.vehicle)
        gps_sensor.listen(self.process_gps_data)
        self.sensors.append(gps_sensor)
        print("GPS sensor attached.")
        return gps_sensor
    
    def process_gps_data(self, gps):
        print(f"GPS Data: Latitude {gps.latitude}, Longitude {gps.longitude}, Altitude {gps.altitude}")
        # we can save or log this data to a file or something if we want?