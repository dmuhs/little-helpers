#!/usr/bin/env bash

for id in `docker ps -a | tail -n +2 | cut -d' ' -f1`; do
  docker rm $id
done
