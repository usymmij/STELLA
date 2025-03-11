#! /bin/bash

#docker pull carlasim/carla:0.9.15

sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY \
    -p 2000-2002:2000-2002 \
    carlasim/carla:0.9.15 ./CarlaUE4.sh --Quality=Low -RenderOffScreen

