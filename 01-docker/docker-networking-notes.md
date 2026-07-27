# Docker Networking - Day 2

## Custom Bridge Network Created
docker network create fintech-network

## Redis Container Launched
docker run -d \
  --name redis-cache \
  --network fintech-network \
  redis:alpine

## Proved Container Communication
docker run -it --rm \
  --network fintech-network \
  redis:alpine \
  redis-cli -h redis-cache ping
# Result: PONG

## Key Learnings
- Bridge network = containers communicate using container names
- No -p flag needed for internal container communication
- --rm flag auto-deletes container after it exits
- Custom bridge network has built-in DNS resolution
