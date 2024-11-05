#!/bin/bash
#
# Linux/Mac BASH script to build docker container
#
docker rmi serverless-client
docker build -t serverless-client .
