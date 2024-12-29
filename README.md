![](docs/imgs/STELLA-colour.png)

# Documents
- all documents were written in Typst 0.11 / 0.12

| Document                                          | Source                      |
|---------------------------------------------------|-----------------------------|
| [Project Proposal](docs/proposal/proposal.pdf)    | [Source](docs/proposal/)    |
| [Walkthrough](docs/walkthrough/walkthrough.pdf)   | [Source](docs/walkthrough/) |
| [Sprint Plans](docs/sprint-plans/sprint-plans.pdf)| [Source](docs/sprint-plans/)|

# Installation (Docker)

> this is for carla version 0.9.15

1. `cd` into the repository
2. install docker and the carla container
3. `docker cp <container id>:/home/carla/PythonAPI ./PythonAPI`
4. (optional) create and activate a new python environment with Python 3.7
    - if not using a venv, make sure python is version 3.7
5. `. ./toolscripts/install.sh`


# Downloading data

download to the "data" folder

[https://huggingface.co/datasets/autonomousvision/PDM_Lite_Carla_LB2](https://huggingface.co/datasets/autonomousvision/PDM_Lite_Carla_LB2)
