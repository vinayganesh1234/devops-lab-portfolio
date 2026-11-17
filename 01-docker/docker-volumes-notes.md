# Docker Volumes - Day 2

## Problem
Data inside container is lost when container is deleted.
Container filesystem lives and dies with the container.

## Three Types of Docker Storage

### 1. Volume (Docker managed)
# Create volume
docker volume create bankdata

# Use volume
docker run -it --name container1 -v bankdata:/bankdata ubuntu bash

# Inspect volume location on EC2
docker volume inspect bankdata
# Mountpoint: /var/lib/docker/volumes/bankdata/_data

# List all volumes
docker volume ls

# Delete volume
docker volume rm bankdata

- Docker manages location: /var/lib/docker/volumes/bankdata/_data
- Best for databases and persistent data
- Survives container deletion
- Must create with docker volume create first

### 2. Bind Mount (You manage location)
# Basic bind mount
docker run -it --name container1 \
  -v /home/ec2-user/mydata:/bankdata \
  ubuntu bash

# With read only (container can read but not write)
docker run -it --name container1 \
  -v /home/ec2-user/mydata:/bankdata:ro \
  ubuntu bash

- You control exact path on EC2
- No pre-creation needed (Docker creates dir automatically)
- Best for development and config files
- Left side = EC2 path, Right side = container path

### 3. tmpfs (RAM only)
# Basic tmpfs
docker run -it --name container1 \
  --tmpfs /bankdata \
  ubuntu bash

# With size limit
docker run -it --name container1 \
  --tmpfs /bankdata:size=100m \
  ubuntu bash

# With multiple options
docker run -it --name container1 \
  --tmpfs /bankdata:size=100m,mode=1777 \
  ubuntu bash

- Stored in RAM only
- Lost when container stops or EC2 reboots
- Fastest performance
- Best for sensitive temporary data (passwords, tokens)
- Never touches disk

## Comparison
Feature          Volume      Bind Mount    tmpfs
Survives reboot  YES         YES           NO
Location control Docker      You           RAM
Pre-creation     Required    Not needed    Not needed
Performance      Good        Good          Best
Use case         DB data     Dev/Config    Secrets

## Proved Data Persistence
1. Created volume: docker volume create bankdata
2. Ran container1 with volume mounted
3. Wrote "10000 customer records" to /bankdata/records.txt
4. Deleted container1
5. Ran fresh container with same volume
6. Data survived ✅

## Volume location on EC2
docker volume inspect bankdata
Mountpoint: /var/lib/docker/volumes/bankdata/_data
Data lives on EC2 host disk - not inside container
