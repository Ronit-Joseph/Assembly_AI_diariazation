#!/bin/bash
docker run -it --network=host --gpus='"device=0"' --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -v $PWD:/workspace clarity:latest