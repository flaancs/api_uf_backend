# Makefile for managing the lifecycle of the application using docker-compose

.PHONY: up down build help

up:
	@echo "Starting up UF API..."
	docker-compose up -d web

down:
	@echo "Stopping UF API..."
	docker-compose down

build:
	@echo "Building docker images..."
	docker-compose build

bash:
	@echo "Starting bash..."
	docker exec -ti api_uf_backend /bin/bash

test:
	@echo "Running tests..."
	docker-compose run --rm test pytest -v

coverage:
	@echo "Running coverage..."
	docker-compose run --rm test pytest --cov=app --cov-report term-missing --cov-report html

help:
	@echo "Makefile commands:"
	@echo "up       - Start all services (in background) for the API."
	@echo "down     - Stop all services for the API."
	@echo "build    - Build all docker images for the API."
	@echo "bash     - Start bash in the container."
	@echo "test     - Run all tests."
	@echo "coverage - Show code coverage."
	@echo "help     - Show this help message."
