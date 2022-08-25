.PHONY: build

build:
	docker build -t josephstool .

run:
	mkdir -p result && docker run -d -v $(shell pwd)/input:/input -v $(shell pwd)/result:/result josephstool:latest

go:
	docker pull gcr.io/ytpurge-420/github.com/paulmikulskis/josephstool:latest && make run