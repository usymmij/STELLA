#! /bin/bash

docker pull carlasim/carla:0.9.15

sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.15 /bin/bash

