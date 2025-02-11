#! /bin/bash
RED='\033[0;31m'

if ! [[ $(python3 --version | grep "Python 3.7") ]]; then
  
  printf "${RED}python version: please change to python 3.7"
  return
fi

cd carla
pip3 install -r requirements.txt

pip3 install dist/carla-0.9.15-cp37-cp37m-manylinux_2_27_x86_64.whl  
