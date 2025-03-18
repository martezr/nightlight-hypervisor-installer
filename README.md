# Nightlight Hypervisor

## Build docker image
```
docker build --platform linux/amd64 -t alpine-iso-builder .
```

## Build ISO image
```
docker run --platform linux/amd64 -v "$(pwd):/build" -it alpine-iso-builder
```