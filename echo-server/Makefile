REPO=registry-jpe.ubitus.net/library/qy-echo-server:latest

build:
	docker build --platform=linux/amd64 -t ${REPO} .
push:
	docker push ${REPO}
all: build push