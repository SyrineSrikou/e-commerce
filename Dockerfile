FROM ubuntu:20.04
RUN apt-get -y update
RUN apt-get install python3 -y
RUN apt-get install -y python3-pip

ENV PYTHONUNBUFFERED 1
#directory to store app source code
RUN mkdir /GTA_marketplace

WORKDIR /GTA_marketplace

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]