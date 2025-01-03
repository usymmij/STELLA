#! /usr/bin/env python

# @usymmij

import carla

import random
import time

def connect():

    # taken from carla's tutorial.py

    # connect and get the world
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    bp = random.choice(blueprint_library.filter('vehicle'))

    # Now we need to give an initial transform to the vehicle. We choose a
    # random transform from the list of recommended spawn points of the map.
    transform = random.choice(world.get_map().get_spawn_points())

    vehicle = world.spawn_actor(bp, transform)


    actor_list.append(vehicle)
    print('created %s' % vehicle.type_id)
                                                                                       
    # Let's put the vehicle to drive around.
    vehicle.set_autopilot(True)
                                                                                       
    # Let's add now a "depth" camera attached to the vehicle. Note that the
    # transform we give here is now relative to the vehicle.
    camera_bp = blueprint_library.find('sensor.camera.depth')
    camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
    camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)
    actor_list.append(camera)
    print('created %s' % camera.type_id)
                                                                                       
    # Now we register the function that will be called each time the sensor
    # receives an image. In this example we are saving the image to disk
    # converting the pixels to gray-scale.
    cc = carla.ColorConverter.LogarithmicDepth
    camera.listen(lambda image: image.save_to_disk('_out/%06d.png' % image.frame, cc))
                                                                                       
    # Oh wait, I don't like the location we gave to the vehicle, I'm going
    # to move it a bit forward.
    location = vehicle.get_location()
    location.x += 40
    vehicle.set_location(location)
    print('moved vehicle to %s' % location)
                                                                                       
    # But the city now is probably quite empty, let's add a few more
    # vehicles.
    transform.location += carla.Location(x=40, y=-3.2)
    transform.rotation.yaw = -180.0
    for _ in range(0, 10):
        transform.location.x += 8.0
                                                                                       
        bp = random.choice(blueprint_library.filter('vehicle'))
                                                                                       
        # This time we are using try_spawn_actor. If the spot is already
        # occupied by another object, the function will return None.
        npc = world.try_spawn_actor(bp, transform)
        if npc is not None:
            actor_list.append(npc)
            npc.set_autopilot(True)
            print('created %s' % npc.type_id)
                                                                                       
    time.sleep(5)

def main():
    connect()
    pass

if __name__=="__main__":
    main()
