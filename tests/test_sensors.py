import carla
 import time
 
 client = carla.Client('192.168.1.18', 2000)
 try:
     world = client.get_world()
 except RuntimeError:
     print("Please run carla first")
     raise
 
 def test_spawn_ego():
     try:
         vehicle = world.get_blueprint_library().find('vehicle.dodge.charger_2020')
         vehicle.set_attribute('role_name', 'hero')
 
         spawn = world.get_map().get_spawn_points()[0]
         ego = world.spawn_actor(vehicle, spawn)
 
         time.sleep(.5)
     finally:
         ego.destroy()
 
 def test_camera():
     try:
         vehicle = world.get_blueprint_library().find('vehicle.dodge.charger_2020') 
         vehicle.set_attribute('role_name', 'hero')
         
         spawn = world.get_map().get_spawn_points()[0]
         ego = world.spawn_actor(vehicle, spawn)
         
         # Create a transform to place the camera on top of the vehicle
         camera_init_trans = carla.Transform(carla.Location(x=1.6,z=1.5))
         
         # We create the camera through a blueprint that defines its properties
         camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')
         
         # We spawn the camera and attach it to our ego vehicle
         camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to=ego)
         
         camera.listen(lambda image: image.save_to_disk("out/last.png"))
         time.sleep(.5)
     finally:
         ego.destroy()
 
 def test_gps():
     try:
         vehicle = world.get_blueprint_library().find('vehicle.dodge.charger_2020') 
         vehicle.set_attribute('role_name', 'hero')
         
         spawn = world.get_map().get_spawn_points()[0]
         ego = world.spawn_actor(vehicle, spawn)
         
         transform = carla.Transform()
         
         gps_bp = world.get_blueprint_library().find('sensor.other.gnss')
         
         # We spawn the camera and attach it to our ego vehicle
         gps = world.spawn_actor(gps_bp, transform, attach_to=ego)
         
         gps.listen(lambda measurement: measurement.latitude)
         time.sleep(.5)
     finally:
         ego.destroy()
