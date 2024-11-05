@echo off
REM
REM Windows BATCH script to build docker container
REM
@echo on
docker rmi serverless-client
docker build -t serverless-client .
