import math
import carla
from waypoint import Waypoint

class Navigator:
    def __init__(self, world, vehicle):
        self.world = world
        self.vehicle = vehicle

    def gps_to_waypoint(self, waypoint):
        """Converts a Waypoint object to a CARLA waypoint."""
        map = self.world.get_map()
        geolocation = waypoint.to_geolocation()
        world_location = map.transform_to_geolocation(geolocation).location
        return map.get_waypoint(world_location, project_to_road=True)

    def move_to_waypoint(self, target_waypoint, throttle=0.5):
        """Moves the vehicle to the specified Waypoint."""
        if not self.vehicle:
            print("No vehicle assigned.")
            return

        carla_waypoint = self.gps_to_waypoint(target_waypoint)
        current_waypoint = self.world.get_map().get_waypoint(self.vehicle.get_location())

        while current_waypoint != carla_waypoint:
            # Calculate direction and distance
            target_location = carla_waypoint.transform.location
            current_location = self.vehicle.get_location()
            direction = target_location - current_location
            distance = math.sqrt(direction.x**2 + direction.y**2 + direction.z**2)

            if distance < 2.0:  # Stop within 2 meters
                self.stop_vehicle()
                print("Reached target waypoint.")
                return

            # Apply control
            control = carla.VehicleControl()
            control.throttle = throttle
            control.steer = max(-1.0, min(1.0, direction.y / (direction.x + 1e-5)))
            self.vehicle.apply_control(control)

            # Update current waypoint
            current_waypoint = self.world.get_map().get_waypoint(self.vehicle.get_location())

            # Allow the world to tick
            self.world.wait_for_tick()

    def stop_vehicle(self):
        """Stop the vehicle."""
        control = carla.VehicleControl()
        control.brake = 1.0
        self.vehicle.apply_control(control())


# Example usage
# Initialize your CARLA world and vehicle
world = carla.Client('localhost', 2000).get_world()
vehicle = world.get_actors().filter('vehicle.*')[0]  # Get the first vehicle (you can spawn one if needed)

# Create a Waypoint and Navigator
waypoint = Waypoint(37.7749, -122.4194)  # Example coordinates
navigator = Navigator(world, vehicle)

# Move the vehicle to the waypoint
navigator.move_to_waypoint(waypoint, throttle=0.7)
