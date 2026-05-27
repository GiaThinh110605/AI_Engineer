FROM ubuntu

WORKDIR /src

RUN apt-get update 
RUN apt-get install -y python3

COPY ml.py ./ml.py

RUN apt-get install -y python3-sklearn

CMD ["python3", "ml.py"]