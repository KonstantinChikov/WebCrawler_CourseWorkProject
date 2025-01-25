# basic-sentiment-analysis

This project is a very simple example of sentiment analysis with Python.

There is a prebuilt image available on DockerHub.

# Build steps

```commandline
docker build .
```

```commandline
docker tag <image-id> boneff/basic-python-sentiment-analysis:latest
```

```commandline
docker push boneff/basic-python-sentiment-analysis:latest
```

# Usage
Runs with default values and a CSV pre-baked into the Docker image.

```commandline
docker run --rm -it boneff/basic-python-sentiment-analysis:latest bash
```

```commandline
pipenv run python main.py
```

Running with Docker Compose for and has mounted the project dir to the image, so we can debug in the container or run with custom parameters:

```commandline
docker-compose up -d
```

Accepted parameters as environment variables are `CSV_PATH` and `FIELD_NAME`.
`CSV_PATH` - path to the CSV you want to analyze.
`FIELD_NAME` - the name of the field from the CSV you want to run sentiment analysis on.

Then exec into it
```commandline
docker exec -it -e CSV_PATH=/app/data/avatar_modified.csv -e FIELD_NAME=character_lines  basic-sentiment-analysis-python_app-1 bash
```
