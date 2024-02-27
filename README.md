## Overview

This project is a FastAPI application designed to scrape and return the UF value from the SII website. It leverages Docker for easy setup and deployment, ensuring consistency across different environments.

## Key Components:

- FastAPI: For the web framework to create RESTful endpoints.
- BeautifulSoup: For scraping the required UF value from the SII website.
- Docker: To containerize the application, ensuring it runs the same in every environment.
- docker-compose: To define and run multi-container Docker applications.
- Makefile (for macOS/Linux users): To simplify the command execution for building, running, and managing the Docker containers.

## Running the API

### MacOS

Ensure Docker and Docker Compose are installed on your system. make should be available by default on macOS.

Build the Docker images:

```bash
make build
```

Start the application:

```bash
make up
```

Stop the application (when done):

```bash
make down
```

### Windows

Build the Docker images:

```bash
docker-compose build
```

Start the application:

```bash
docker-compose up -d
```

Stop the application (when done):

```bash
docker-compose down
```

## Accessing the API

Once running, access the API at `http://localhost:8000`. Use the `value_uf/{date}` endpoint to interact with the API.

**Also, you can access `http://localhost:8000/docs` to see the api documentation**

#### Note: {date} parameter must be in YYYY-MM-DD Format

## Running tests

### MacOS

```bash
make test
```

```bash
make coverage
```

### Windows

```bash
docker-compose run --rm test pytest -v
```

```bash
docker-compose run --rm test pytest --cov=app --cov-report term-missing --cov-report html
```

## Entering the container

### MacOS

```bash
make bash
```

### Windows

```bash
docker exec -ti api_uf_backend /bin/bash
```
