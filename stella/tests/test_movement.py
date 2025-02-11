import pytest
import time

"""what is CARLA_movement_interface?? doesn't show up in any docs -usymmij"""
# from CARLA_movement_interface import CARLAInterface
 
@pytest.mark.skip(reason="CARLA_movement_interface fails plz fix @dbazinag")
def test_movement():
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
    
