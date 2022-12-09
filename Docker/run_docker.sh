#!/bin/bash

# Build the docker image first with "bash build_docker.sh"
docker run -it --rm -v $(pwd):/tmp/:Z py37_speech
