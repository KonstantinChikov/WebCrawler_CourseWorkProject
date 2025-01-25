FROM python:3.10

# copy source code to image
COPY . /app
WORKDIR /app
# VOLUME [ "/data" ]

# install system dependencies for the project
RUN rm -rf Pipfile.lock
RUN pip install pipenv
# RUN pipenv lock --clear

# install from Pipfile
RUN pipenv install --verbose
# RUN mkdir logs

# CMD ["pipenv", "run", "python", "main.py"]