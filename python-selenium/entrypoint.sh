#!/bin/bash
# set -e
while true
do
  echo "Start.."
  python sample.py
  echo "Finish.."
  sleep 10
done
# Then exec the container's main process (what's set as CMD in the Dockerfile).
