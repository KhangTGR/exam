#!/bin/bash

docker-compose down
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -q)
docker network prune
docker volume prune
