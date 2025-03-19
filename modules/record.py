import os
import cv2
import carla
import numpy as np
import time
import datetime
import argparse
from argparse import RawTextHelpFormatter

FRAMERATE = 20

def track_cam(world):
    actor = None
    while actor == None: 
        for t_a in world.get_actors():
            if t_a.type_id == "sensor.camera.rgb":
                return t_a

path = '/mnt/scratch/saves/videos'
vid = None
def init_vid(w, h):
    global path
    path = os.path.join(path, str(datetime.datetime.now()).replace(' ', '-')[:19]+'.avi')
    fourcc = cv2.VideoWriter_fourcc(*'MP42') 
    video = cv2.VideoWriter(path, fourcc, FRAMERATE, (w, h))
    return video

def handle_cam(image):
    global vid
    if vid is None:
        print('first frame')
        vid = init_vid(image.width, image.height)
    im=np.frombuffer(image.raw_data, dtype=np.uint8).reshape((image.height, 
                                                             image.width, -1))
    print('a')
    cv2.imshow('a', im)
    cv2.waitKey(1)
    vid.write(im)

def main():

    parser = argparse.ArgumentParser(description="stella", formatter_class=RawTextHelpFormatter)
    parser.add_argument('--host', default='localhost',
                        help='IP of the host server (default: localhost)')
    parser.add_argument('--port', default=2000, type=int,
                        help='TCP port to listen to (default: 2000)')
    parser.add_argument('--path', default='/mnt/scratch/saves/videos',
                        help='')

    global path
    args = parser.parse_args()
    path = args.path

    client = carla.Client(args.host, args.port)
    world = client.get_world()

    cam = track_cam(world)
    print(f'found camera {cam}')
    id = cam.id
    cam.listen(handle_cam)

    global vid
    while cam.is_alive:
        pass
    print('complete')
    vid.release()
    
if __name__ == "__main__":
    main()
