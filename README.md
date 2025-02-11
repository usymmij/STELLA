![](docs/imgs/STELLA-colour.png)

# Documents
- all documents were written in Typst 0.11 / 0.12

| Document                                          | Source                      |
|---------------------------------------------------|-----------------------------|
| [Project Proposal](docs/proposal/proposal.pdf)    | [Source](docs/proposal/)    |
| [Walkthrough](docs/walkthrough/walkthrough.pdf)   | [Source](docs/walkthrough/) |
| [Sprint Plans](docs/sprint-plans/sprint-plans.pdf)| [Source](docs/sprint-plans/)|


# Setting up CARLA

> this is for carla version 0.9.15

1. `cd` into the repository
2. install docker and the carla container
3. `docker cp <container id>:/home/carla/PythonAPI ./`
4. (optional) create and activate a new python environment with Python 3.7
    - if not using a venv, make sure python is version 3.7
5. `. ./toolscripts/install.sh`

# Building and Installing STELLA

1. `pip install -r stella/requirements.txt`
2. `pip install ./stella`
 
## Running STELLA
- if using docker, first run 
```bash
docker run --privileged \
 -p 2000-2002:2000-2002 \
 --gpus all \
 -e DISPLAY=$DISPLAY \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -it \
 carlasim/carla:0.9.15 \
 /bin/bash
```
- then, inside the container

`./CarlaUE4.sh -quality-level=Low -fps=10`

### future usage
- to restart the container, use `toolscripts/start.sh`

# Downloading data

download to the "data" folder

[https://github.com/OpenDriveLab/DriveLM/tree/DriveLM-CARLA?tab=readme-ov-file#custom_dataset_and_pdm_lite](https://github.com/OpenDriveLab/DriveLM/tree/DriveLM-CARLA?tab=readme-ov-file#custom_dataset_and_pdm_lite)

