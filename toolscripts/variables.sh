#! /bin/bash

#export CARLA_ROOT=/path/to/CARLA/root
#export WORK_DIR=/path/to/carla_garage
#export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla
#export SCENARIO_RUNNER_ROOT=${WORK_DIR}/scenario_runner
#export LEADERBOARD_ROOT=${WORK_DIR}/leaderboard
#export PYTHONPATH="${CARLA_ROOT}/PythonAPI/carla/":"${SCENARIO_RUNNER_ROOT}":"${LEADERBOARD_ROOT}":${PYTHONPATH}

export CARLA_ROOT=/mnt/scratch/stella/carla_garage/carla/
export WORK_DIR=/mnt/scratch/stella/carla_garage/
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI
export SCENARIO_RUNNER_ROOT=${WORK_DIR}/scenario_runner
export LEADERBOARD_ROOT=${WORK_DIR}/leaderboard
export PYTHONPATH="${CARLA_ROOT}/PythonAPI/carla/":"${SCENARIO_RUNNER_ROOT}":"${LEADERBOARD_ROOT}":${PYTHONPATH}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/software/anaconda3/lib
