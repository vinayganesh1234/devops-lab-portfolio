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

## Network Namespaces — How Containers Have Their Own Ports

Linux network namespaces give each container:
- Own isolated network interface
- Own complete set of 65,535 ports
- Own IP address on the Docker network
- Complete isolation from host and other containers

This is why two containers can both use port 8080 internally without conflict.
Each lives in its own namespace — separate from host and each other.

### -p flag bridges two namespaces:
-p 8080:8080
Host namespace port 8080 → forwards to → Container namespace port 8080

### Bridge network = namespaces + virtual switch:
- Each container still has own namespace (isolation)
- Bridge network adds a virtual switch connecting them
- Containers find each other using DNS (container names)
- No -p flag needed for container-to-container traffic
