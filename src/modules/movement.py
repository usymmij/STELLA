import carla
import time
from sensors import Sensors

class CARLAInterface:
    def __init__(self, host='localhost', port=2000):
        self.client = carla.Client(host, port)
        self.client.set_timeout(10.0)
        self.world = self.client.get_world()
        self.vehicle = None
        print("Connected to CARLA server.")

    def spawn_vehicle(self, model='vehicle.tesla.model3', spawn_point_index=0):
        blueprint_library = self.world.get_blueprint_library()
        vehicle_bp = blueprint_library.filter(model)[0]
        spawn_points = self.world.get_map().get_spawn_points()
        self.vehicle = self.world.try_spawn_actor(vehicle_bp, spawn_points[spawn_point_index])
        if self.vehicle:
            print(f"Vehicle spawned: {self.vehicle.id}")
            
            # adding sensors to vehicle once spawned in 
            self.sensor_manager = Sensors(self.world, self.vehicle)
            self.add_camera() # adding camera 
            gps_transform = carla.Transform()
            self.sensor_manager.add_gps_sensor(gps_transform) # adding gps sensor with transform for position
        else:
            print("Failed to spawn vehicle.")
    
    def move_forward(self, throttle=0.5):
        if self.vehicle:
            control = carla.VehicleControl()
            control.throttle = throttle
            self.vehicle.apply_control(control)
        else:
            print("No vehicle spawned.")

    def stop(self):
        if self.vehicle:
            control = carla.VehicleControl()
            control.brake = 1.0
            self.vehicle.apply_control(control)

    def turn_left(self, throttle=0.3, steer=0.5):
        if self.vehicle:
            control = carla.VehicleControl()
            control.throttle = throttle
            control.steer = -steer
            self.vehicle.apply_control(control)

    def turn_right(self, throttle=0.3, steer=0.5):
        if self.vehicle:
            control = carla.VehicleControl()
            control.throttle = throttle
            control.steer = steer
            self.vehicle.apply_control(control)
            
    def get_status(self):
        if self.vehicle:
            velocity = self.vehicle.get_velocity()
            speed = 3.6 * (velocity.x**2 + velocity.y**2 + velocity.z**2)**0.5  # m/s to km/h
            location = self.vehicle.get_location()
            return {
                "speed_kmh": speed,
                "location": (location.x, location.y, location.z)
            }
        else:
            return {"error": "No vehicle spawned."}
        
    def brake(self, intensity=1.0):
        if self.vehicle:
            control = carla.VehicleControl()
            control.brake = max(0.0, min(1.0, intensity))  # Clamp intensity between 0.0 and 1.0
            self.vehicle.apply_control(control)
        else:
            print("No vehicle spawned.")

    def add_camera(self, attach_point=None, save_path = 'output/'):
        # checking if vehicle is spawned
        if not self.vehicle:
            print("Error: No vehicle to attach the camera to.")
            return None
        
        # creating camera
        blueprint_library = self.world.get_blueprint_library()
        camera_bp = blueprint_library.find('sensor.camera.rgb')

        # could set camera attributes necessary here

        # attaching camera to vehicle
        spawn_point = attach_point or carla.Transform(carla.Location(x=1.5, z=2.4))
        camera = self.world.spawn_actor(camera_bp, spawn_point, attach_to=self.vehicle)

        # start listening to camera
        camera.listen(lambda image: image.save_to_disk(f'{save_path}/%06d.png' % image.frame))
        print("Camera attached and saving images to: ", save_path)
        return camera

    def destroy_vehicle(self):
        if self.vehicle:
            self.vehicle.destroy()
            print("Vehicle destroyed.")

    def __del__(self):
        self.destroy_vehicle()

