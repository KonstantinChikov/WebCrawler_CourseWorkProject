FROM python:3.10

# copy source code to image
COPY . /app
WORKDIR /app

# install system dependencies for the project
RUN pip install pipenv

# install from Pipfile
RUN pipenv install
# install NLTK data (https://www.nltk.org/data.html) (downloading only "vader_lexicon", if needed we could download "all")
RUN pip install nltk && python -m nltk.downloader -d /usr/local/share/nltk_data vader_lexicon
RUN mkdir logs

#CMD ["pipenv", "run", "python", "main.py"]
