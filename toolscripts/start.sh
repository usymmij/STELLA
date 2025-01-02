#! /bin/bash

docker container restart $1
docker container attach $1
