# To run this file: "python -m tests.test_movement" from src directory
import time
import sys
import os
import pygame

from modules.movement import CARLAInterface

if __name__ == "__main__":
    
    interface = CARLAInterface()
    interface.spawn_vehicle()
    time.sleep(2)
    print("Moving forward...")
    interface.move_forward(throttle=0.7)
    time.sleep(5)

    print("Slamming brakes...")
    interface.brake(1.0)
    time.sleep(5)
    
    print("Moving forward...")
    interface.move_forward(throttle=0.1)
    time.sleep(5)

    print("Stopping...")
    interface.stop()

    status = interface.get_status()
    print("Vehicle Status:", status)





#from modules.movement import CARLAInterface

# if __name__ == "__main__":
    
#     interface = CARLAInterface()
#     interface.spawn_vehicle()
#     time.sleep(2)
#     print("Moving forward...")
#     interface.move_forward(throttle=0.7)
#     time.sleep(5)

#     print("Slamming brakes...")
#     interface.brake(1.0)
#     time.sleep(5)
    
#     print("Moving forward...")
#     interface.move_forward(throttle=0.1)
#     time.sleep(5)

#     print("Stopping...")
#     interface.stop()

#     status = interface.get_status()
#     print("Vehicle Status:", status)
